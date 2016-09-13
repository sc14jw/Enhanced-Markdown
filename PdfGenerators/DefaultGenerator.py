import PdfGenerator.PdfGenerator

class DefaultGenerator(PdfGenerator):

    def generatePdf(filename, text):

        if (not filename is str) or (not text is str):
            raise AttributeError("either filename or text is not a string")
