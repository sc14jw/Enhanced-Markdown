import unittest
import sys

sys.path.append('.')

from Modules.TableModule import TableModule

class TestTableModule(unittest.TestCase):

    def setUp(self):
        self.tableModule = TableModule()

    def test_getCommands(self):

        expectedOutput = {"table": "create a new table or close a currently open table - can optionally use [<id>]",
                "row": "create a new row or close a currently open row",
                "column": "create a new column or close a currently open column - can optionally use [<colSpan>, <rowSpan>]",
                "section": "create a new section or close a currently open section - requires the parameter head or body relating to the section to interact with",
                "header": "create a new column header or close a currently open header"}

        self.assertEqual(expectedOutput, self.tableModule.getCommands())

    def test_tableCommand(self):

        expectedOutput = "<table>"
        self.assertEqual(expectedOutput, self.tableModule.completeCommand("table()"))

    def test_openTableCommand(self):

        expectedOutput = "</table>"
        self.tableModule.completeCommand("table()")
        self.assertEqual(expectedOutput, self.tableModule.completeCommand("table()"))

    def test_tableCommandId(self):

        self.assertEqual("<table id='test'>", self.tableModule.completeCommand("table()[test]"))

    def test_rowCommand(self):

        self.assertEqual("<tr>", self.tableModule.completeCommand("row()"))
        self.assertEqual("</tr>", self.tableModule.completeCommand("row()"))

    def test_columnCommand(self):

        self.assertEqual("<td>", self.tableModule.completeCommand("column()"))
        self.assertEqual("</td>", self.tableModule.completeCommand("column()"))

    def test_columnCommandColspan(self):

        self.assertEqual("<td colspan=2>", self.tableModule.completeCommand("column()[2]"))

    def test_columnCommandColspanRowspan(self):

        self.assertEqual("<td colspan=2 rowspan=2>", self.tableModule.completeCommand("column()[2,2]"))

    def test_sectionCommand(self):

        self.assertEqual("<thead>", self.tableModule.completeCommand("section(head)"))
        self.assertEqual("</thead>", self.tableModule.completeCommand("section(head)"))

        self.assertEqual("<tbody>", self.tableModule.completeCommand("section(body)"))
        self.assertEqual("</tbody>", self.tableModule.completeCommand("section(body)"))

    def test_sectionCommandBadSection(self):

        with self.assertRaises(AttributeError):
            self.tableModule.completeCommand("section(test)")

        with self.assertRaises(AttributeError):
            self.tableModule.completeCommand("section()")

    def test_headerCommand(self):

        self.assertEqual("<th>", self.tableModule.completeCommand("header()"))
        self.assertEqual("</th>", self.tableModule.completeCommand("header()"))

if __name__ == '__main__':
    unittest.main()
