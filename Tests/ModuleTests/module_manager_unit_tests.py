import unittest
import sys

sys.path.append(".")

from Modules.ModuleManager import ModuleManager
from Modules.MockModule import MockModule
from Modules.LinksModule import LinksModule

''' Class to test the functionality of the ModuleManager class '''
class TestModuleManager(unittest.TestCase):

    def setUp(self):
        self.manager = ModuleManager()

    def test_AddModule(self):
        module = MockModule()
        self.manager.addModule(module)

        self.assertEqual([module], self.manager.getModules())

    def test_AddModuleNotAModule(self):

        with self.assertRaises(AttributeError):
            self.manager.addModule("test")

    def test_AddModuleNoneModule(self):

        with self.assertRaises(AttributeError):
            self.compiler.addModule(None)

    def test_RemoveModule(self):
        module = MockModule()
        self.manager.addModule(module)

        self.manager.removeModule(module)

        self.assertEqual([], self.manager.getModules())

    def test_RemoveModuleEmpty(self):

        self.manager.removeModule(MockModule())

        self.assertEqual(None, self.manager.getModules())

    def test_RemoveModuleNotAModule(self):

        with self.assertRaises(AttributeError):
            self.manager.removeModule(None)

    def test_RemoveModuleModuleNotInList(self):
        module = MockModule()

        self.manager.addModule(module)
        self.manager.removeModule(MockModule())

        self.assertEqual([module], self.manager.getModules())

    def test_GetModuleCommands(self):

        self.manager.addModule(MockModule())

        self.assertEqual([{"test":"this is a test module to test functionality"}], self.manager.getModuleCommands())

    def test_GetModuleCommandsEmptyModules(self):
        self.assertEqual(None, self.manager.getModuleCommands())


    def test_CompileCommand(self):
        expectedOutput = "accepted this is a test accepted link(this is a test)"
        inputString = "@test() this is a test @test() @link(this is a test)"

        self.manager.addModule(MockModule())

        self.assertEqual(expectedOutput, self.manager.moduleCommand(inputString))


    def test_CompileCommandWithParams(self):
        expectedOutput = "accepted optional params this is a test"
        inputString = "@test()[test] this is a test"

        self.manager.addModule(MockModule())

        self.assertEqual(expectedOutput, self.manager.moduleCommand(inputString))

    def test_CompileCommandWithoutModules(self):
        self.assertEqual("this is a test", self.manager.moduleCommand("this is a test"))

    def test_CompileCommandMultipleModules(self):
        expectedOutput = "accepted this is a test <a href=\"www.test.com\">www.test.com</a>"
        inputString = "@test() this is a test @link(www.test.com)"

        self.manager.addModule(MockModule())
        self.manager.addModule(LinksModule())

        self.assertEqual(expectedOutput, self.manager.moduleCommand(inputString))

    def test_CompileCommandEmptyStringCommand(self):

        self.manager.addModule(MockModule())

        self.assertEqual("@", self.manager.moduleCommand("@"))

    def test_CompileCommandEscapeCharacter(self):

        self.manager.addModule(MockModule())

        self.assertEqual("this is a test @", self.manager.moduleCommand("this is a test \@"))

if __name__ == '__main__':
    unittest.main()
