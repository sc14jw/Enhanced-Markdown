class ClassLoader:
    ''' allows for the loading of any class on the path - used for dynamically loading new
        modules '''
    @staticmethod
    def importClass(name):
        ''' import return an instance of a class with passed in name - name should be the fully qualified
            name of required class including module '''

        if not isinstance(name, str):
            raise AttributeError("name must be a string")

        components = name.split('.')

        # get the required class assuming it's at the end of the passed in string
        reqClassName = components[len(components) - 1]

        # remove the class from components list to create the module
        del components[-1]

        module = ""

        for moduleSection in components:
            module += moduleSection + "."

        reqModule = __import__(module[:-1], fromlist=[reqClassName])
        return getattr(reqModule, reqClassName)
