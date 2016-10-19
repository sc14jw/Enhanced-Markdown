import json
import sys

from Compilers.DefaultCompiler import DefaultCompiler
from ClassLoader.classLoader import ClassLoader

class MarkdownToPdf:
    ''' Class to handle the commandline input for markdown-pdf conversion '''

    def __init__ (self):

        self.loadModuleNames(self.filename)
        self.loadModules()



    def loadProperties(self, filename="properties.json"):
        ''' load properties for CmdTool '''

        if not isinstance(filename, str):
            raise AttributeError("filename must be a string")

        if filename[-5:] != ".json":
            raise AttributeError("filename must be a json file")

        with open(filename) as jsonFile:

            data = json.load(jsonFile)

            self.filename = data["moduleFile"]

            self.compiler = ClassLoader.importClass(data["compiler"])




    def loadModuleNames(self, filename="modules.json"):
        ''' load currently used modules '''

        if not isinstance(filename, str):
            raise AttributeError("filename must be a string")

        if filename[-5:] != ".json":
            raise AttributeError("filename must end in .json")

        with open(filename) as jsonFile:

            data = json.load(jsonFile)

            self.moduleStrings = data["modules"]

    def loadModules(self):
        ''' load an instance of each named module '''

        if not self.moduleStrings:
            raise AttributeError("moduleStrings has not been properly initialised")

        self.modules = []

        for name in moduleStrings:
            self.modules.append(ClassLoader.getInstance(name))
