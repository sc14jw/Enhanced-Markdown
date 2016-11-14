from Compilers.Compiler import Compilers

class MockCompiler (Compiler):
    ''' Mock compiler for testing other elements of the system '''

    def compiler(self, text):
        return text
