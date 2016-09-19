from Modules.Module import Module

''' class to help manage the modules available to a compiler '''
class ModuleManager:
    def __init__(self, modules=None):
        if not modules == None:
            if not all(isinstance(elem, Module) for elem in modules):
                raise AttributeError("modules must be a list of Module objects")

        self._modules = modules


    ''' add a module to the manager '''
    def addModule(self, module):
        if not isinstance(module, Module):
            raise AttributeError("module must be a subclass of Module")

        if self._modules == None:
            self._modules = []

        self._modules.append(module)


    ''' remove a module from the manager - raises AttributeError if module isn't a Module '''
    def removeModule(self, module):

        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self._modules == None:
            return

        elif not module in self._modules:
            return

        else:
            self._modules.remove(module)


    ''' complete a given module command '''
    def moduleCommand(self, text):

        if self._modules == None:
            return text

        if not "@" in text:
            return text

        commands = text.split("@")

        for command in commands:

            for module in self._modules:

                text = module.completeCommand(command)


        return text

    ''' return the modules currently in use by a Manager object - might return None '''
    def getModules(self):

        return self._modules

    ''' return the module commands currently supported by a given Manager object
        as a list - might return None if no modules were added to the manager '''
    def getModuleCommands(self):

        if self._modules == None:
            return None

        commands = []

        for module in self._modules:

            commands.append(module.getCommands())

        return commands
