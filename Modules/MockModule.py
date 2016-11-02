from Modules.Module import Module

''' Mock module implementation to test functionality '''
class MockModule(Module):

    def getCommands(self):
        return {"test":"this is a test module to test functionality"}

    def completeCommand(self,command):

        if command[0:7] == "test()[":
            return "accepted optional params"

        if command[0:6] == "test()":
            return "accepted"



        return command
