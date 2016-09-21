import unittest
import sys

sys.path.append(".")

from Modules.LinksModule import LinksModule

class TestLinksModule(unittest.TestCase):

    def setUp(self):

        self.module = LinksModule()

    def test_getCommands(self):

        expectedOutput = {"link" : "add a link into the document - can be optionally" +
        " paramatised with [] to alter link text"}
        output = self.module.getCommands()

        self.assertEqual(expectedOutput, output)

    def test_CommandNoParams(self):

        expectedOutput = '<a href="www.test.com">www.test.com</a>'

        self.assertEqual(expectedOutput, self.module.completeCommand("link(www.test.com)"))

    def test_CommandWithParams(self):

        expectedOutput = '<a href="www.test.com">test</a>'
        self.assertEqual(expectedOutput, self.module.completeCommand("link(www.test.com)[test]"))

    def test_NoModuleCommand(self):

        expectedOutput = "test"
        output = self.module.completeCommand(expectedOutput)

        print("output = " + output)

        self.assertEqual("test", output)

    def test_WrongModuleCommand(self):

        expectedOutput = "@test(this is a test) to be honest"
        self.assertEqual(expectedOutput, self.module.completeCommand(expectedOutput))


if __name__ == '__main__':
    unittest.main()
