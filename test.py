import sys
from DefaultCompiler import DefaultCompiler

if __name__ == '__main__':

    inputText = ""
    with open("test.md", "r") as inputFile:
        inputText = inputFile.read()

    compiler = DefaultCompiler(None)
    outputText = compiler.compile(inputText)

    with open("test.html", "w") as outputFile:
        outputFile.write(outputText)
