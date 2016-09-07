import unittest
import sys

sys.path.append(".")

from Modules.LinksModule import LinksModule
from Compilers.Compiler import Compiler

class TestCompiler(unittest.TestCase):

    def setUp(self):

        self.compiler = Compiler(None)

    def test_AddModule(self):

        module = LinksModule()
        self.compiler.addModule(module)

        expected = [module]

        self.assertEqual(expected, self.compiler.modules)

    def test_AddModuleWrongAttributeType(self):

        with self.assertRaises(AttributeError):
            self.compiler.addModule("test")


    def test_RemoveModule(self):

        module = LinksModule()

        self.compiler.modules = [module]
        self.compiler.removeModule(module)

        self.assertEqual([], self.compiler.modules)

    def test_RemoveModuleNoneModulesList(self):

        self.compiler.removeModule(LinksModule())
        self.assertEqual(None, self.compiler.modules)

    def test_RemoveModuleModuleEmptyList(self):

        self.compiler.modules = []

        self.compiler.removeModule(LinksModule())
        self.assertEqual([], self.compiler.modules)

    def test_RemoveModuleModuleNotHeldByCompiler(self):

        modulesList = [LinksModule()]

        self.compiler.modules = modulesList

        self.compiler.removeModule(LinksModule())
        self.assertEqual(modulesList, self.compiler.modules)

    def test_RemoveModuleModuleNotModule(self):

        with self.assertRaises(AttributeError):
            self.compiler.removeModule("test")

    def test_GetModuleCommands(self):

        module = LinksModule()
        self.compiler.modules = [module]

        self.assertEqual([module.getCommands()], self.compiler.getModuleCommands())

    def test_GetModuleCommandsNoneModules(self):

        self.assertEqual(None, self.compiler.getModuleCommands())

    def test_GetModuleCommandsEmptyModules(self):

        self.compiler.modules = []

        self.assertEqual([], self.compiler.getModuleCommands())


if __name__ == '__main__':
    unittest.main()
