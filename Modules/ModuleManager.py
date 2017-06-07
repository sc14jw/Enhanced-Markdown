from Modules.Module import Module

class ModuleManager:
    ''' class to help manage the modules available to a compiler '''
    def __init__(self, modules=None):
        if not modules == None:
            if not all(isinstance(elem, Module) for elem in modules):
                raise AttributeError("modules must be a list of Module objects")

        self._modules = modules


    def addModule(self, module):
         ''' add a module to the manager '''
        if not isinstance(module, Module):
            raise AttributeError("module must be a subclass of Module")

        if self._modules == None:
            self._modules = {}

        for command in module.getCommands():
            # Check we don't already have a module for a command before mapping it
            if self._modules[command] == None:
                self._module[command] = module


    def removeModule(self, module):
        ''' remove a module from the manager - raises AttributeError if module isn't a Module '''
        if not isinstance(module, Module):
            raise AttributeError("module does not inherit Module")

        if self._modules == None:
            return

        elif not module in self._modules:
            return


        self._modules.remove(module)


    def moduleCommand(self, text):
        ''' complete a given module command '''
        if self._modules == None:
            return text

        if not "@" in text:
            return text

        commands = text.split("@")

        if not self._modules:
            return text

        newText = ""

        for commandLine in commands:

            # Check if the commandLine has optional parameters
            if commandLine.find(']') == -1:
                # Check that the commandLine actually contains a completeCommand
                if commandLine.find(')') == -1:
                    continue

                command = commandLine[0:commandLine.find(')') + 1]

            elif commandLine.find(']') != -1:
                command = commandLine[0:commandLine.find(']') + 1]

            output = commandLine

            module = self._modules[command[:command.find('(')]]

            # Check that we actually have a module loaded for the command itself
            if module:
                output = module.completeCommand(command)
            else:
                output = command
 
            newText += commandLine.replace(command, output)


        if newText:
            text = newText

        text = text.replace("\\@", "@")
        return text

    def getModules(self):
        ''' return the modules currently in use by a Manager object - might return None '''
        return self._modules

    def getModuleCommands(self):
         ''' return the module commands currently supported by a given Manager object
             as a list - might return None if no modules were added to the manager '''
        if self._modules == None:
            return None

        return [module.getCommands() for module in self._modules]
