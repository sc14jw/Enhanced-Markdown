from Modules.Module import Module

''' Mock module implementation to test functionality '''
class MockModule(Module):

    def getCommand(self):
        return {"test":"this is a test module to test functionality"}

    def completeCommand(self,command):
        if command == "test":
            return "accepted"

        return command
