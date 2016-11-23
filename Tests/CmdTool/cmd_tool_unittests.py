import unittest
import sys
import json
import os

sys.path.append(".")

from CmdTool.CmdClient import CmdClient
from Compilers.MockCompiler import MockCompiler
from PdfGenerators.MockGenerator import MockGenerator

class TestCmdTool (unittest.TestCase):
    ''' Unit tests for the CmdTool class '''

    @classmethod
    def setUpClass(cls):

        cls.testData = {"compiler": "Compilers.MockCompiler.MockCompiler", "moduleFile": "modules.json", "generator": "PdfGenerators.MockGenerator.MockGenerator"}

        cls.jsonNames = {"testJson": "test.json", "badJson": "badTest.json"}

        with open("test.json", "w") as dataFile:
            json.dump(cls.testData, dataFile)

    def setUp(self):
        self.cmdTool = CmdClient()


    def test_loadProperties(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])
        self.assertTrue(isinstance(self.cmdTool.compiler, MockCompiler))
        self.assertEqual(self.cmdTool.filename, self.testData["moduleFile"])
        self.assertTrue(isinstance(self.cmdTool.pdfGenerator, MockGenerator))

    def test_loadProperiesBadJson(self):

        badData = {"this is a test":"test"}

        with open(self.jsonNames["badJson"], "w") as dataFile:
            json.dump(badData, dataFile)

        with self.assertRaises(KeyError):
            self.cmdTool.loadProperties(self.jsonNames["badJson"])

    def test_loadPropertiesNoFile(self):

        with self.assertRaises(FileNotFoundError):
            self.cmdTool.loadProperties("noFile.json")

    def test_loadPropertiesNotJson(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.loadProperties("test.txt")
    @classmethod
    def tearDownClass(cls):

        for key, value in cls.jsonNames.items():
            os.remove(value)


if __name__ == '__main__':
    unittest.main()
