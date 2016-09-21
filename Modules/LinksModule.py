import sys

sys.path.append(".")

from Modules.Module import Module

''' Module to handle links with @link command '''
class LinksModule(Module):

    def getCommands(self):
        return {"link" : "add a link into the document - can be optionally paramatised with [] to alter link text"}

    def completeCommand(self, command):

        if not (isinstance(command, str)):
            raise AttributeError("text is not a string")

        if command[0:4] == "link":

            link = command[5:command.find(")")]

            linkText = command[7 + len(link):command.find("]")]

            if not linkText == "":
                html = "<a href=\"" + link + "\">" + linkText + "</a>"
                command = command.replace("link(" + link + ")[" + linkText + "]", html)

            else:
                html = "<a href=\"" + link + "\">" + link + "</a>"
                command = command.replace("link(" + link + ")", html)

        return command



if __name__ == '__main__':
    module = LinksModule()
    output = module.completeCommand("test")

    print("output = " + str(output))
