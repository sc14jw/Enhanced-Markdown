import sys
sys.path.append(".")

from Modules import Module

''' Generic Compiler class '''
class Compiler:
    def __init__(self, modules):
        self.modules = modules

    ''' compile a piece of test
        should return a String representing compiled text '''
    def compile(self, text):
        pass

    ''' add a module to the Compiler '''
    def addModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self.modules == None:

            self.modules = []
            self.modules.append(module)

        else:

            self.modules.append(module)


    ''' complete a given module command '''
    def moduleCommand(self, text):

        if self.modules == None:
            return text

        for module in self.modules:

            text = module.completeCommand(text)

        return text
