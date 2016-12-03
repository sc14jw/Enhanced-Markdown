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

        cls.testData = {"compiler": "Compilers.MockCompiler.MockCompiler", "moduleFile": "modulesTest.json", "generator": "PdfGenerators.MockGenerator.MockGenerator"}
        cls.modules = {"modules": ["Modules.MockModule.MockModule"]}


        cls.emptyModules = {"modules": []}
        cls.removeModulesData = {"compiler": "Compilers.MockCompiler.MockCompiler", "moduleFile": "removeModules.json",
                                 "generator": "PdfGenerators.MockGenerator.MockGenerator"}
        cls.jsonNames = {"testJson": "test.json", "badJson": "badTest.json", "modulesJson": "modulesTest.json", "badModules": "badModules.json",
                         "removeModulesProperties": "removeModulesProperties.json", "removeModules": "removeModules.json"}

        with open (cls.jsonNames["removeModulesProperties"], "w") as dataFile:
            json.dump(cls.removeModulesData, dataFile)

        with open (cls.jsonNames["removeModules"], "w") as dataFile:
            json.dump(cls.emptyModules, dataFile)

        with open(cls.jsonNames["testJson"], "w") as dataFile:
            json.dump(cls.testData, dataFile)

        with open(cls.jsonNames["modulesJson"], "w") as dataFile:
            json.dump(cls.modules, dataFile)

        with open("test.json", "w") as dataFile:
            json.dump(cls.testData, dataFile)

        with open("emdTest.emd", "w") as dataFile:
            dataFile.write("this is a test")

        with open("emdTest.css", "w") as dataFile:
            dataFile.write("*\n{\nfont-family=\"sans-serif\"\n}")

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

    def test_loadModuleStrings(self):

        self.cmdTool.loadModuleNames(self.jsonNames["modulesJson"])
        self.assertEqual(self.cmdTool.moduleStrings, self.modules["modules"])

    def test_loadModuleStringsBadJson(self):

        badData = {"this is a test":"test"}

        with open(self.jsonNames["badModules"], "w") as dataFile:
            json.dump(badData, dataFile)

        with self.assertRaises(KeyError):
            self.cmdTool.loadModuleNames(self.jsonNames["badModules"])

    def test_loadModuleStringsNoJson(self):

        with self.assertRaises(FileNotFoundError):
            self.cmdTool.loadModuleNames("noFile.json")

    def test_loadModuleStringsNotJson(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.loadModuleNames("test.txt")

    def test_loadModules(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])
        self.cmdTool.loadModuleNames(self.jsonNames["modulesJson"])
        self.cmdTool.loadModules()

        self.assertTrue(self.cmdTool.modules != None, "cmdTool module list should not be None")

    def test_loadModulesNoModuleNames(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.loadModules()

    def test_createPdf(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])
        self.cmdTool.createPdf("emdTest.emd", "emdTest")

    def test_createPdfNotAFile(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])

        with self.assertRaises(FileNotFoundError):
            self.cmdTool.createPdf("empty.emd", "emdTest")


    def test_createPdfNotEmdFile(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])

        with self.assertRaises(AttributeError):
            self.cmdTool.createPdf("test", "emdTest")

    def test_createPdfNoProperties(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.createPdf("emdTest.emd", "emdTest")

    def test_addCss(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])
        self.cmdTool.addCss("emdTest.css")

        self.assertEqual(self.cmdTool.pdfGenerator.stylesheet, "emdTest.css", "stylesheet did not equal emdTest.css")

    def test_addCssNotCssFile(self):

        self.cmdTool.loadProperties(self.jsonNames["testJson"])

        with self.assertRaises(AttributeError):
            self.cmdTool.addCss("test.txt")

    def test_addCssEmptyFile(self):

        with open("empty.css","w") as dataFile:
            dataFile.write("")

        self.cmdTool.loadProperties(self.jsonNames["testJson"])
        self.cmdTool.addCss("empty.css")

        self.assertEqual(self.cmdTool.pdfGenerator.stylesheet, "empty.css", "stylesheet did not equal empty.css")

        os.remove("empty.css")

    def test_addCssNoProperties(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.addCss("emdTest.css")

    def test_addModule(self):

        self.cmdTool.loadProperties(self.jsonNames["removeModulesProperties"])
        self.cmdTool.addModule("Modules.Module.Module")

        with open(self.jsonNames["removeModules"]) as dataFile:
            self.assertEqual(json.load(dataFile)["modules"][0], "Modules.Module.Module")

        with open (self.jsonNames["removeModules"], "w") as dataFile:
            dataFile.write("")
            json.dump(self.emptyModules, dataFile)

    def test_addModuleNoProperties(self):

        with self.assertRaises(AttributeError):
            self.cmdTool.addModule("Modules.Module.Module")

    @classmethod
    def tearDownClass(cls):

        for key, value in cls.jsonNames.items():
            os.remove(value)

        os.remove("emdTest.emd")
        os.remove("emdTest.css")


if __name__ == '__main__':
    unittest.main()
