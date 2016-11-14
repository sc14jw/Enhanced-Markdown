import unittest
import sys
import json

sys.path.append(".")

from CmdTool.CmdTool import CmdTool

class TestCmdTool (unittest.TestCase):

    def setUp(self):
        self.cmdTool = CmdTool()
        self.testData = {"compiler": "Compilers.MockCompiler.MockCompiler", "moduleFile": "modules.json", "generator": "PdfGenerators.MockGenerator.MockGenerator"}

        with open("test.json", "w") as dataFile:
            json.dump(testData, dataFile)

    def test_loadProperties(self):

        self.cmdTool.loadProperties("test.json")
        
