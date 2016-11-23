import unittest
import sys
import json

sys.path.append(".")

from CmdTool.CmdClient import CmdClient
from Compilers.MockCompiler import MockCompiler
from PdfGenerators.MockGenerator import MockGenerator

class TestCmdTool (unittest.TestCase):
    ''' Unit tests for the CmdTool class '''

    def setUp(self):
        self.cmdTool = CmdClient()
        self.testData = {"compiler": "Compilers.MockCompiler.MockCompiler", "moduleFile": "modules.json", "generator": "PdfGenerators.MockGenerator.MockGenerator"}

        with open("test.json", "w") as dataFile:
            json.dump(self.testData, dataFile)

    def test_loadProperties(self):

        self.cmdTool.loadProperties("test.json")
        self.assertTrue(isinstance(self.cmdTool.compiler, MockCompiler))
        self.assertEqual(self.cmdTool.filename, self.testData["moduleFile"])
        self.assertTrue(isinstance(self.cmdTool.pdfGenerator, MockGenerator))

    def test_loadProperiesBadJson(self):

        badData = {"this is a test":"test"}

        with open("badTest.json", "w") as dataFile:
            json.dump(badData, dataFile)

        with self.assertRaises(KeyError):
            self.cmdTool.loadProperties("badTest.json")

    def test_loadPropertiesNoFile(self):

        with self.assertRaises(FileNotFoundError):
            self.cmdTool.loadProperties("noFile.json")

    def test_loadPropertiesNotJson(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.loadProperties("test.txt")

if __name__ == '__main__':
    unittest.main()
