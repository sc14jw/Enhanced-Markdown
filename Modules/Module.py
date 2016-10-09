''' Generic Module class which should be inherited from to create new Modules '''
class Module:
    ''' complete a singular module command - even if the module is unable to complete
        the command this method should ALWAYS return a string (either the original text)
        or new text from the module in response to a command '''
    def completeCommand(self, text):
        pass

    ''' return the commands available to a module as a list '''
    def getCommands(self):
        print("running module getCommands()")
        pass
