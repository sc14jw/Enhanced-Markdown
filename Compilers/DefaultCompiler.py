from Compilers.Compiler import Compiler

''' Default implementation of the Compiler abstract class '''
class DefaultCompiler(Compiler):

    ''' compile some text to from markdown to html '''
    def compile(self, text):
        html = ""

        textArray = text.split("\n")

        for line in textArray:
            if(line == ""):
                continue

            line = super().moduleCommand(line)

            if line[0] == "#":

                titleLevel = line.count("#")
                newLine = line.replace("#","")

                htmlTag = "h" + str(titleLevel) + ">"
                html += "<" + htmlTag + newLine + "</" + htmlTag

            elif line[0] == "*" and line[1] == "-":
                html += "<ul>"

            elif line[0] == "-" and line[1] == "*":
                html += "</ul>"

            elif line[0] == "*" and line[1] == "." and line[2] == ".":
                html += "<ol>"

            elif line[0] == "." and line[1] == "." and line[2] == "*":
                html += "</ol>"

            elif line[0] == "-" and line[1] == "-" and line[2] == "-":

                html += "</hr>"

            elif line[0] == "-":

                newLine = line.replace("-", "")
                html += "<li>" + newLine + "</li>"


            elif line[0] == "." and line[1] == ".":

                newLine = line[2:]
                html += "<li>" + newLine + "</li>"


            else:

                html += "<p>" + line + "</p>"


        return html



if __name__ == '__main__':
    compiler = DefaultCompiler(None)

    text = """# this is a test\n- this should be a list item :)\n- this should be another list item\n## this should close the list\n.. this should start a numbered list\n.. this should continue the list\nthis should just be a paragraph """

    print(compiler.compile(text))
