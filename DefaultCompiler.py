from Compiler import Compiler

''' Default implementation of the Compiler abstract class '''
class DefaultCompiler(Compiler):
    unorderedListRunning = False
    ordererdListRunning = False


    ''' method to check if a unordered list tag is currently open '''
    def checkUnorderedListRunning(self, html):
        if(self.unorderedListRunning):
            html += "</ul>"
            self.unorderedListRunning = False
            return html

        return html

    ''' method to check if an orderered list tag is currently open '''
    def checkOrderedListRunning(self, html):
        if(self.ordererdListRunning):
            html += "</ol>"
            self.ordererdListRunning = False
            return html

        return html


    ''' compile some text to from markdown to html '''
    def compile(self, text):
        html = ""

        textArray = text.split("\n")
        #print("textArray = " + str(textArray))

        for line in textArray:
            if(line == ""):
                continue

            if line[0] == "#":

                html = self.checkUnorderedListRunning(html);
                html = self.checkOrderedListRunning(html);

                titleLevel = line.count("#")
                newLine = line.replace("#","")

                htmlTag = "h" + str(titleLevel) + ">"
                html += "<" + htmlTag + newLine + "</" + htmlTag

            elif line[0] == "-":

                html = self.checkOrderedListRunning(html)

                if(not self.unorderedListRunning):
                    html += "<ul>"

                newLine = line.replace("-", "")
                html += "<li>" + newLine + "</li>"

                self.unorderedListRunning = True

            elif line[0] == "." and line[1] == ".":

                html = self.checkUnorderedListRunning(html)

                if(not self.ordererdListRunning):
                    html += "<ol>"

                newLine = line[2:]
                html += "<li>" + newLine + "</li>"

                self.ordererdListRunning = True

            else:

                html = self.checkUnorderedListRunning(html)
                html = self.checkOrderedListRunning(html)

                html += "<p>" + line + "</p>"


        return html



if __name__ == '__main__':
    compiler = DefaultCompiler(None)

    text = """# this is a test\n- this should be a list item :)\n- this should be another list item\n## this should close the list\n.. this should start a numbered list\n.. this should continue the list\nthis should just be a paragraph """

    print(compiler.compile(text))
