import sys
sys.path.append(".")

from Modules.Module import Module
from Modules.ModuleManager import ModuleManager

''' Generic Compiler class '''
class Compiler:
    def __init__(self, manager):
        self.manager = manager

        if manager == None:
            self.manager = ModuleManager()

    ''' compile a piece of test
        should return a String representing compiled text '''
    def compile(self, text):
        pass

    ''' add a module to the Compiler - raises AttributeError if module isn't a Module '''
    def addModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self.manager == None:

            self.manager = ModuleManager();
            self.manager.addModule(module)

        else:

            self.manager.addModule(module)


    ''' remove a module from the compiler - raises AttributeError if module isn't a Module '''
    def removeModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self.manager == None:
            return

        else:
            self.manager.removeModule(module)



    ''' complete a given module command - may raise an AttributeError if text
        isn't a string '''
    def moduleCommand(self, text):

        if not (isinstance(text, str)):
            raise AttributeError("text is not a string")

        text = self.manager.moduleCommand(text)

        return text

    ''' return the modules currently in use by a Compiler object - might return None '''
    def getModules(self):

        return self.manager.getModules()

    ''' return the module commands currently supported by a given Compiler object
        as a list - might return None if no modules were added to the compiler '''
    def getModuleCommands(self):

        if self.manager == None:
            return None

        return self.manager.getModuleCommands()
