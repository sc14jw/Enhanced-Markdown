from Modules.Module import Module

class TableModule(Module):
    ''' Module to deal with the creation of tables '''

    self.commands = {"table": self.createTable, "row": self.row, "column": self.column, "closeTable": self.closeTable}

    def __init__(self):

        self.openRow = False
        self.openCol = False

    def completeCommand(self, command):

        if command[:command.find('(')] not in self.commands.keys():
            return command

        self.command = command
        return self.commands[command[:command.find('(')]]()


    def getCommands(self):
        return {"table": "create a new table - can optionally use [<id>]",
                "closeTable": "close an opened tabled",
                "row": "create a new row"}


    def createTable(self):
        ''' create a new table '''

        if '[' in self.command:

            return "<table id=" + self.command[self.command.find('['):self.command.find(']') - 1] + ">"

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
