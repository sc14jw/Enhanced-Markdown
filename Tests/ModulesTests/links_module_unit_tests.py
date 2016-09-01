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

        print("output = " + str(output))

        self.assertEquals(expectedOutput, output)

    def test_noCommand(self):

        self.assertEquals(None, self.module.completeCommand("test"))

    def test_CommandNoParams(self):

        expectedOutput = '<a href="www.test.com">www.test.com</a>'

        self.assertEquals(expectedOutput, self.module.completeCommand("@link(www.test.com)"))

    def test_CommandWithParams(self):

        expectedOutput = '<a href="www.test.com">test</a>'
        self.assertEquals(expectedOutput, self.module.completeCommand("@link(www.test.com)[test]"))


if __name__ == '__main__':
    unittest.main()
