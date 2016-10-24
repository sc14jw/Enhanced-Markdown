import sys
import argparse

sys.path.append(".")

from CmdTool.markdownToPdf import MarkdownToPdf


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("incorrect usage please use as so: emd.py <.emd file> <output file name>")
        sys.exit(1)

    inputName = sys.argv[0]
    outputName = sys.argv[1]

    markdownToPdf = MarkdownToPdf()

    markdownToPdf.createPdf(inputName, outputName)
