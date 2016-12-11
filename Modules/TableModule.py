from Modules.Module import Module

class TableModule(Module):
    ''' Module to deal with the creation of tables '''

    self.commands = {"table": self.createTable, "row": self.row, "column": self.column, "closeTable": self.closeTable, "section" : self.section}

    def __init__(self):

        self.openRow = False
        self.openCol = False
        self.openBody = False
        self.openHead = False

    def completeCommand(self, command):

        if command[:command.find('(')] not in self.commands.keys():
            return command

        self.command = command
        return self.commands[command[:command.find('(')]]()


    def getCommands(self):
        return {"table": "create a new table - can optionally use [<id>]",
                "closeTable": "close an opened tabled",
                "row": "create a new row or close a currently open row",
                "column": "create a new column or close a currently open column - can optionally use [<colSpan>, <rowSpan>]"}


    def createTable(self):
        ''' create a new table '''

        if '[' in self.command:

            return "<table id=" + self.command[self.command.find('['):self.command.find(']') - 1] + ">"

        return "</table>"


    def closeTable(self):
        ''' close a table '''

        return "</table>"

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

        if '[' in self.command;

            parameters = self.command[self.command.find('['): self.command.find(']') - 1]
            parameters = parameters.split(',')

            if parameters.size() == 1:
                return "<td colspan=" + parameters[0] + ">"


            return "td colspan=" + parameters[0] + "rowspan=" + parameters[1] + ">"


    def section(self):
        ''' create/close a given section '''

        parameter = self.command[self.command.find('(') : self.command.find(')') - 1]

        if not (parameter == "body" or parameter == "head"):
            raise AttributeError(parameter + "not supported as a section. Please use either head or body")

        if parameter == "body":

            if self.bodyOpen:

                self.bodyOpen = False
                return "</tbody>"

            return "<tbody>"

        if self.headOpen:

            self.headOpen = False
            return "</thead>"

        return "<thead>"
