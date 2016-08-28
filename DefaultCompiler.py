from Compiler import Compiler

''' Default implementation of the Compiler abstract class '''
class DefaultCompiler(Compiler):
    __unorderedListRunning = False
    __ordererdListRunning = False


    ''' method to check if a unordered list tag is currently open '''
    def __checkUnorderedListRunning(self, html):
        if(self.__unorderedListRunning):
            html += "</ul>"
            self.__unorderedListRunning = False
            return html

        return html

    ''' method to check if an orderered list tag is currently open '''
    def __checkOrderedListRunning(self, html):
        if(self.__ordererdListRunning):
            html += "</ol>"
            self.__ordererdListRunning = False
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

                html = self.__checkUnorderedListRunning(html);
                html = self.__checkOrderedListRunning(html);

                titleLevel = line.count("#")
                newLine = line.replace("#","")

                htmlTag = "h" + str(titleLevel) + ">"
                html += "<" + htmlTag + newLine + "</" + htmlTag

            elif line[0] == "-" and line[1] == "-" and line[2] == "-":

                html = self.__checkOrderedListRunning(html)
                html = self.__checkUnorderedListRunning(html)

                html += "</hr>"

            elif line[0] == "-":

                html = self.__checkOrderedListRunning(html)

                if(not self.__unorderedListRunning):
                    html += "<ul>"

                newLine = line.replace("-", "")
                html += "<li>" + newLine + "</li>"

                self.__unorderedListRunning = True

            elif line[0] == "." and line[1] == ".":

                html = self.__checkUnorderedListRunning(html)

                if(not self.__ordererdListRunning):
                    html += "<ol>"

                newLine = line[2:]
                html += "<li>" + newLine + "</li>"

                self.__ordererdListRunning = True

            else:

                html = self.__checkUnorderedListRunning(html)
                html = self.__checkOrderedListRunning(html)

                html += "<p>" + line + "</p>"


        return html



if __name__ == '__main__':
    compiler = DefaultCompiler(None)

    text = """# this is a test\n- this should be a list item :)\n- this should be another list item\n## this should close the list\n.. this should start a numbered list\n.. this should continue the list\nthis should just be a paragraph """

    print(compiler.compile(text))
