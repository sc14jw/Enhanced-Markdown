import json
import sys

from ClassLoader.classLoader import ClassLoader

class CmdClient:
    ''' Class to handle the commandline input for markdown-pdf conversion '''

    def __init__ (self):

        self.loadProperties()
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

            self.compiler = ClassLoader.importClass(data["compiler"])()

            self.pdfGenerator = ClassLoader.importClass(data["generator"])()


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
            data["modules"].remove(module)

        with open(self.filename,'w') as moduleFile:

            moduleFile.write("")
            json.dump(data,moduleFile)
