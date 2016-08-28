from Module import Module

''' Module to handle links with @link command '''
class LinksModule(Module):
    def completeCommand(self, text):

        html = ""

        if not (isinstance(text, str)):
            raise AttributeError("text is not a string")

        if not "@" in text:
            return

        commands = text.split("@")
        print("commands = " + str(commands))

        for command in commands:
            print("command = " + command)
            print("command[0:4] = " + command[0:4])

            if command[0:4] == "link":

                link = command[5:command.find(")")]
                print("link = " + link)

                linkText = command[7 + len(link):command.find("]")]
                print("linkText = " + linkText)

                if not linkText == "":
                    html = "<a href=" + link + ">" + linkText + "</a>"
                    text = text.replace("@link(" + link + ")[" + linkText + "]", html)

                else:
                    html = "<a href=" + link + ">" + link + "</a>"
                    text = text.replace("@link(" + link + ")", html)

        return text

if __name__ == '__main__':
    module = LinksModule()
    output = module.completeCommand("this is a test @link(www.google.com)[]")

    print("output = " + output)
