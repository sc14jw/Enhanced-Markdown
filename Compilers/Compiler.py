import sys
sys.path.append(".")

from Modules.Module import Module

''' Generic Compiler class '''
class Compiler:
    def __init__(self, modules):
        self.modules = modules

    ''' compile a piece of test
        should return a String representing compiled text '''
    def compile(self, text):
        pass

    ''' add a module to the Compiler - raises AttributeError if module isn't a Module '''
    def addModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self.modules == None:

            self.modules = []
            self.modules.append(module)

        else:

            self.modules.append(module)


    ''' remove a module from the compiler - raises AttributeError if module isn't a Module '''
    def removeModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self.modules == None:
            return

        elif not module in self.modules:
            return

        else:
            self.modules.remove(module)



    ''' complete a given module command '''
    def moduleCommand(self, text):

        if self.modules == None:
            return text

        for module in self.modules:

            text = module.completeCommand(text)

        return text

    ''' return the modules currently in use by a Compiler object - might return None '''
    def getModules(self):

        return self.modules

    ''' return the module commands currently supported by a given Compiler object
        as a list - might return None if no modules were added to the compiler '''
    def getModuleCommands(self):

        if self.modules == None:
            return None

        commands = []

        for module in self.modules:

            commands.append(module.getCommands())

        return commands
