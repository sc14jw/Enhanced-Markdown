import sys
sys.path.append(".")

from PdfGenerators.PdfGenerator import PdfGenerator
from weasyprint import HTML, CSS

class DefaultGenerator(PdfGenerator):

    def __init__(self):
        self.styleSheet = None

    def generatePdf(self,filename, text):

        if (not isinstance(filename,str)) or (not isinstance(text,str)):
            raise AttributeError("either filename or text is not a string")

        if not self.styleSheet:
            HTML(string=text).write_pdf(filename + ".pdf")

        else:
            HTML(string=text).write_pdf(filename + ".pdf", stylesheets=[self.styleSheet])


    def addStylesheet(self,filename):

        if (not filename is str):
            raise AttributeError("filename must be a string")

        self.styleSheet = CSS(filename=filename + ".css")


if __name__ == '__main__':

    generator = DefaultGenerator()
    generator.generatePdf("test", "<p> this is a test </p>")
