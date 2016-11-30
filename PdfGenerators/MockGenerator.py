from PdfGenerators.PdfGenerator import PdfGenerator

class MockGenerator(PdfGenerator):
    ''' Mock generator for testing other classes '''

    def generatePdf(self, filename, text):

        return text

    def addStylesheet(self, stylesheet):

        self.stylesheet = stylesheet
