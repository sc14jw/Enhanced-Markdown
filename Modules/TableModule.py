from Modules.Module import Module

class TableModule(Module):
    ''' Module to deal with the creation of tables '''

    def __init__(self):

        self.commands = {"table": self.createTable, "row": self.row, "column": self.column, "section" : self.section, "header" : self.header}

        self.openRow = False
        self.openCol = False
        self.bodyOpen = False
        self.headOpen = False
        self.tableOpen = False
        self.headerOpen = False

    def completeCommand(self, command):

        if command[:command.find('(')] not in self.commands.keys():
            return command

        self.command = command
        return self.commands[command[:command.find('(')]]()


    def getCommands(self):
        return {"table": "create a new table or close a currently open table - can optionally use [<id>]",
                "row": "create a new row or close a currently open row",
                "column": "create a new column or close a currently open column - can optionally use [<colSpan>, <rowSpan>]",
                "section": "create a new section or close a currently open section - requires the parameter head or body relating to the section to interact with",
                "header": "create a new column header or close a currently open header"}


    def createTable(self):
        ''' create a new table '''

        if self.tableOpen:

            self.tableOpen = False
            return "</table>"

        if '[' in self.command:

            return "<table id=" + self.command[self.command.find('[') + 1 :self.command.find(']')] + ">"

        return "<table>"


    def row(self):
        ''' create/close a row '''

        if self.openRow:

            self.openRow = False
            return "</tr>"

        return "<tr>"


    def column(self):
        ''' create/close a column '''

        if self.openCol:

            self.openCol = False
            return "</td>"

        if '[' in self.command:

            parameters = self.command[self.command.find('[') + 1: self.command.find(']')]
            parameters = parameters.split(',')

            if parameters.size() == 1:
                return "<td colspan=" + parameters[0] + ">"


            return "<td colspan=" + parameters[0] + "rowspan=" + parameters[1] + ">"

        return "<td>"

    def section(self):
        ''' create/close a given section '''

        parameter = self.command[self.command.find('(') + 1 : self.command.find(')')]

        print("parameter = " + parameter)

        if not (parameter == "body" or parameter == "head"):
            raise AttributeError(parameter + " not supported as a section. Please use either head or body")

        if parameter == "body":

            if self.bodyOpen:

                self.bodyOpen = False
                return "</tbody>"

            return "<tbody>"

        if self.headOpen:

            self.headOpen = False
            return "</thead>"

        return "<thead>"

    def header(self):

        if self.headerOpen:

            self.headerOpen = False
            return "</th>"

        return "<th>"
