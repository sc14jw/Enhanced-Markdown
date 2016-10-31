import sys
import argparse

sys.path.append(".")

from CmdTool.CmdClient import CmdClient

def addStyleSheet(cmdClient):
    ''' add a stylesheet for compilation '''

    if not isinstance(cmdClient, CmdClient):
        raise AttributeError("cmdClient must be a CmdClient")

    print("sys.argv[2] = " + sys.argv[2])

    cmdClient.addCss(sys.argv[2])

if __name__ == '__main__':

    FLAGS = {"-css":addStyleSheet}

    if len(sys.argv) < 2:
        print("incorrect usage please use as so: emd.py <.emd file> <output file name>")
        sys.exit(1)

    inputName = sys.argv[1]
    outputName = sys.argv[2]

    cmdClient = CmdClient()


    if len(sys.argv) > 2:

        for key in FLAGS:

            if sys.argv[1] == key:

                FLAGS[key](cmdClient)
                inputName = sys.argv[3]
                outputName = sys.argv[4]

                break


    cmdClient.createPdf(inputName, outputName)
