from Compilers.Compiler import Compiler

class MockCompiler (Compiler):
    ''' Mock compiler for testing other elements of the system '''

    def compile(self, text):
        return str(text)
