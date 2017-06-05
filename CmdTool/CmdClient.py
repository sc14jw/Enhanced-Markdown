import json
import sys

from ClassLoader.ClassLoader import ClassLoader
from Compilers.DefaultCompiler import DefaultCompiler
from PdfGenerators.DefaultGenerator import DefaultGenerator

DEFAULT_COMPILER = "Compilers.DefaultCompiler.DefaultCompiler"
DEFAULT_GENERATOR = "PdfGenerators.DefaultGenerator.DefaultGenerator"

class CmdClient:
    ''' Class to handle the commandline input for markdown-pdf conversion '''

    def __init__(self):

        self.moduleStrings = ["Modules.LinksModule.LinksModule"]
        self.compiler = DefaultCompiler()
        self.pdfGenerator = DefaultGenerator()

    def loadProperties(self, filename="properties.json"):
        ''' load properties for CmdTool '''

        if not isinstance(filename, str):
            raise AttributeError("filename must be a string")

        if filename[-5:] != ".json":
            raise AttributeError("filename must be a json file")
        
        try:
            with open(filename) as jsonFile:
                data = json.load(jsonFile)
                self.filename = data["moduleFile"]
                self.compiler = ClassLoader.importClass(data["compiler"])()
                self.pdfGenerator = ClassLoader.importClass(data["generator"])()
                
        except FileNotFoundError:
            print("got here!!!!")
            with open(filename, 'w') as jsonFile:
               data = {"moduleFile": "modules.json", "compiler": DEFAULT_COMPILER, "generator": DEFAULT_GENERATOR}
               json.dump(data, jsonFile)


    def loadModuleNames(self, filename="modules.json"):
        ''' load currently used modules '''

        if not isinstance(filename, str):
            raise AttributeError("filename must be a string")

        if filename[-5:] != ".json":
            raise AttributeError("filename must end in .json")
        
        try:
            with open(filename) as jsonFile:
                data = json.load(jsonFile)
                self.moduleStrings = data["modules"]

        except FileNotFoundError:
            with open(filename, 'w') as jsonFile:
                data = {"modules": self.moduleStrings}
                json.dump(data, jsonFile)


    def loadModules(self):
        ''' load an instance of each named module '''

        if not self.moduleStrings:
            raise AttributeError("moduleStrings has not been properly initialised")

        self.modules = []

        for name in self.moduleStrings:
            self.compiler.addModule(ClassLoader.importClass(name)())


    def createPdf(self,inputFile, outputFile):
        ''' use loaded transposers to create a pdf from a .emd file '''


        if not isinstance(inputFile, str) or not isinstance(outputFile, str):
            raise AttributeError("both inputFile and outputFile must be a string")

        if not self.pdfGenerator or not self.compiler :
            raise AttributeError("Class not properly initialised, please use loadProperties, loadModuleNames and loadProperties")

        if inputFile[-4:len(inputFile)] != ".emd":
            raise AttributeError("input file must be of .emd file type")

        if outputFile[-4:len(outputFile)] == ".pdf":
            outputFile = outputFile[:-4]

        html = ""

        with open(inputFile) as emdFile:
            html = self.compiler.compile(emdFile.read())

        print("html = " + html)

        self.pdfGenerator.generatePdf(outputFile, html)


    def addCss(self, cssFile):
        ''' add a css file to the compiler '''

        if not isinstance(cssFile, str):
            raise AttributeError("cssFile must be a string")

        if cssFile[-4:len(cssFile)] != ".css":
            raise AttributeError("cssFile must end in '.css'")

        self.pdfGenerator.addStylesheet(cssFile)

    def addModule(self, module):
        ''' add a module to the compiler '''

        if not isinstance(module,str):
            raise AttributeError("module must be a string")

        print("adding module: " + module)

        data = ""

        with open(self.filename) as moduleFile:

            data = json.load(moduleFile)
            data["modules"].append(module)

        with open(self.filename,'w') as moduleFile:

            moduleFile.write("")
            json.dump(data,moduleFile)

    def removeModule(self, module):
        ''' remove a module from the compiler '''

        if not isinstance(module,str):
            raise AttributeError("module must be a string")

        print("removing module: " + module)

        data = ""

        with open(self.filename) as moduleFile:

            data = json.load(moduleFile)

            try:
                data["modules"].remove(module)

            except ValueError as error:
                # this is ok, just means module wasn't in the list
                pass

        with open(self.filename,'w') as moduleFile:

            moduleFile.write("")
            json.dump(data,moduleFile)
