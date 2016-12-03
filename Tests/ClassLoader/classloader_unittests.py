import sys
import unittest

sys.path.append(".")

from ClassLoader.ClassLoader import ClassLoader
from Modules.Module import Module

''' Testcase to test the functionality fo the ClassLoader '''
class TestClassLoader(unittest.TestCase):

    def test_importClass(self):

        testClass = ClassLoader.importClass("Modules.MockModule.MockModule")()
        self.assertTrue(isinstance(testClass, Module))

    def test_importUnknownClass(self):

        with self.assertRaises(ImportError):
            ClassLoader.importClass("Tests.Test.Test")

if __name__ == '__main__':
    unittest.main()
