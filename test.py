import sys
from Compiler import Compiler

if __name__ == '__main__':


    if(len(sys.argv) < 3):
        print("incorrect usage, correct usage: python3 test.py <markdown> <filename>")


    print("markdown file = " + sys.argv[1])

    markdownCode = ""

    with open(sys.argv[1]) as inputFile:
        markdownCode = inputFile.read()

    print("markdownCode = \n" + markdownCode)

    compiler = Compiler()
    output = compiler.compile(markdownCode)

    with open(sys.argv[2], "w") as outputFile:
        outputFile.write(output)
