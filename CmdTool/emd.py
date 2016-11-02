import sys
import argparse

sys.path.append(".")

from CmdTool.CmdClient import CmdClient

def addStyleSheet(cmdClient):
    ''' add a stylesheet for compilation '''

    if not isinstance(cmdClient, CmdClient):
        raise AttributeError("cmdClient must be a CmdClient")

    cmdClient.addCss(sys.argv[2])

    inputName = sys.argv[3]
    outputName = sys.argv[4]

    cmdClient.createPdf(inputName, outputName)


def addModule(cmdClient):
    ''' add a module to the compiler '''

    if not isinstance(cmdClient, CmdClient):
        raise AttributeError("cmdClient must be a CmdClient")

    cmdClient.addModule(sys.argv[2])

def removeModule(cmdClient):
    ''' remove a module from the compiler '''

    if not isinstance(cmdClient, CmdClient):
        raise AttributeError("cmdClient must be a CmdClient")

    cmdClient.removeModule(sys.argv[2])

if __name__ == '__main__':

    FLAGS = {"-css":addStyleSheet, "-addModule":addModule, "-removeModule":removeModule}

    if len(sys.argv) < 2:
        print("incorrect usage please use as so: emd.py <.emd file> <output file name>")
        sys.exit(1)

    cmdClient = CmdClient()


    if len(sys.argv) > 2:

        for key in FLAGS:

            if sys.argv[1] == key:

                FLAGS[key](cmdClient)

                sys.exit(0)

    inputName = sys.argv[1]
    outputName = sys.argv[2]
    cmdClient.createPdf(inputName, outputName)
