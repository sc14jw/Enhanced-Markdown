import sys
from datetime import datetime

sys.path.append(".")

from Modules.Module import Module
from Modules.LinksModule import LinksModule

''' Module to handle references with ref command '''
class ReferenceModule(Module):

    ''' Handles formatting of reference attributes '''
    class AttributeFormatter():
        def __init__(self):
            self.linksmodule = LinksModule()

        def formatDate(self, datestr):
            try:
                return datetime.strptime(datestr,'%d/%m/%Y').strftime('%d %b %Y')
            except ValueError:
                raise ValueError("'" + yearstr + "' did not match the format 'dd/mm/yyyy'")

        def isYear(self, yearstr):
            try:
                return datetime.strptime(yearstr,'%Y').strftime('%Y')
            except ValueError:
                raise ValueError("'" + yearstr + "' did not match the format 'yyyy'")

        def generateRefLink(self, link):
            return self.linksmodule.completeCommand("link(" + link + ")")

        def toUpper(self, string):
            words = filter(lambda a: a != '', string.split(' '))
            if len(words) <= 1:
                return '' if len(string) == 0 else string[0].upper() if len(string) == 1 else string[0].upper() + string[1:]
            else:
                return ' '.join(['' if len(string) == 0 else word[0].upper()
                                 if len(string) == 1 else word[0].upper() + word[1:]
                                 for word in words])

        def isInt(self, num):
            try:
                return str(int(num))
            except ValueError:
                raise ValueError("'" + num + "' is not convertable to int.")

        def isPages(self, num):
            if '-' not in num:
                try:
                    return str(int(num))
                except ValueError:
                    raise ValueError("'" + num + "' is not convertable to int.")
            else:
                if num.count('-') != 1:
                    raise ValueError("'num' does not match the format '<num>' or '<num>-<num>'")
                page_range = num.split('-')
                try:
                    return str(int(page_range[0])) + '-' + str(int(page_range[1]))
                except ValueError:
                    raise ValueError("Could not parse range values in '" + num + "' to int.")

        def toUpperLetter(self, char):
            if len(char) == 1:
                return char.upper()
            else:
                raise ValueError("'" + char + "' initial is not of length 1")

        def parseAuthors(self, authors):
            if authors:
                authors = authors.split('|')
                authors_str = ''
                for num_of_authors, author in enumerate(authors):
                    author_name = filter(lambda a: a != '', author.split(' '))
                    if len(author_name) != 2:
                        raise ValueError("'" + author + "' does not match the format '<first name> <last name>'")
                    authors_str += self.toUpper(author_name[1]) + ', ' + self.toUpperLetter(author_name[0][0]) + '.'
                    authors_str += ' and ' if num_of_authors + 2 == len(authors) else ', ' if num_of_authors + 1 != len(authors) else ''
                return authors_str
            return "<No 'authors'>"

    def __init__(self):
        self.attrFormat = self.AttributeFormatter()
        self.REF_PREFIX = 'ref'
        # A list of supported attribute types
        self.ATTR_TYPES = ['name', 'first name', 'last name', 'first initial', 'published', 'title', 'journal', 'volume',
                           'pages', 'url', 'accessed', 'authors', 'city', 'publisher', 'newspaper', 'magazine']

        # The reference types along with the attributes they use with the string that comes before the attribute ('pre'), the string
        # that comes after the attribute ('post'), the formatting/validation method to be called on an attribute ('function') and
        # the pos of the attribute in the reference ('pos')
        self.REF_TYPES = {'website': {'attrs': {'last name': {'post': ', ', 'function': self.attrFormat.toUpper, 'pos': 1},
                                                'first initial': {'post': '. ', 'function': self.attrFormat.toUpperLetter, 'pos': 2},
                                                'published': {'pre': '(', 'post': '). ', 'function': self.attrFormat.isYear, 'pos': 3},
                                                'title': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 4},
                                                'journal': {'post': ', ', 'function': self.attrFormat.toUpper, 'pos': 5},
                                                'volume': {'pre': '[online] Volume ', 'post': ', ', 'pos': 6},
                                                'pages': {'pre': 'p. ', 'post': '. ', 'function': self.attrFormat.isPages, 'pos': 7},
                                                'url': {'pre': 'Available at: ', 'post': ' ', 'function': self.attrFormat.generateRefLink, 'pos': 8},
                                                'accessed': {'pre': '[Accessed ', 'post': '].', 'function': self.attrFormat.formatDate, 'pos': 9}}
                                     },
                          'book': {'attrs': {'authors': {'post': ' ', 'function': self.attrFormat.parseAuthors, 'pos': 1},
                                             'published': {'pre': '(', 'post': '). ', 'function': self.attrFormat.isYear, 'pos': 2},
                                             'title': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 3},
                                             'city': {'post': ': ', 'function': self.attrFormat.toUpper, 'pos': 4},
                                             'publisher': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 5},
                                             'pages': {'pre': 'p. ', 'post': '.', 'function': self.attrFormat.isPages, 'pos': 6}}
                                  },
                          'newspaper': {'attrs': {'last name': {'post': ', ', 'function': self.attrFormat.toUpper, 'pos': 1},
                                                  'first initial': {'post': '. ', 'function': self.attrFormat.toUpperLetter, 'pos': 2},
                                                  'published': {'pre': '(', 'post': '). ', 'function': self.attrFormat.isYear, 'pos': 3},
                                                  'title': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 4},
                                                  'newspaper': {'pre':'<a style="text-decoration:none;font-style:italic;">',
                                                                'post': '</a>. ', 'function': self.attrFormat.toUpper, 'pos': 5},
                                                  'pages': {'pre': 'p. ', 'post': '.', 'function': self.attrFormat.isPages, 'pos': 6}}
                                       },
                          'onlinenewspaper': {'attrs': {'last name': {'post': ', ', 'function': self.attrFormat.toUpper, 'pos': 1},
                                                        'first initial': {'post': '. ', 'function': self.attrFormat.toUpperLetter, 'pos': 2},
                                                        'published': {'pre': '(', 'post': '). ', 'function': self.attrFormat.isYear, 'pos': 3},
                                                        'title': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 4},
                                                        'newspaper': {'pre':'<a style="text-decoration:none;font-style:italic;">',
                                                                      'post': '</a>, ', 'function': self.attrFormat.toUpper, 'pos': 5},
                                                        'pages': {'pre': '[online] p. ', 'post': '. ', 'function': self.attrFormat.isPages, 'pos': 6},
                                                        'url': {'pre': 'Available at: ', 'post': ' ', 'function': self.attrFormat.generateRefLink, 'pos': 7},
                                                        'accessed': {'pre': '[Accessed ', 'post': '].', 'function': self.attrFormat.formatDate, 'pos': 8}}
                                             },
                          'magazine': {'attrs': {'last name': {'post': ', ', 'function': self.attrFormat.toUpper, 'pos': 1},
                                                 'first initial': {'post': '. ', 'function': self.attrFormat.toUpperLetter, 'pos': 2},
                                                  'published': {'pre': '(', 'post': '). ', 'function': self.attrFormat.isYear, 'pos': 3},
                                                  'title': {'post': '. ', 'function': self.attrFormat.toUpper, 'pos': 4},
                                                  'magazine': {'pre':'<a style="text-decoration:none;font-style:italic;">',
                                                                'post': '</a>, ', 'function': self.attrFormat.toUpper, 'pos': 5},
                                                  'volume': {'pre': '(', 'post': '), ', 'pos': 6},
                                                  'pages': {'pre': 'p.', 'post': '. ', 'function': self.attrFormat.isPages, 'pos': 7}
                                                 }
                                      }
                         }

        assert set(self.ATTR_TYPES).issuperset(set([attr for ref_type in self.REF_TYPES
                                               for attr in self.REF_TYPES[ref_type]['attrs'].keys()]))

    def parseReference(self, attr_dict, ref_type):
        attr_dict.update(self.extrapolateAttributes(attr_dict))
        attr_ordered = self.REF_TYPES[ref_type]['attrs'].keys()
        attr_ordered.sort(key=lambda attr: self.REF_TYPES[ref_type]['attrs'][attr]['pos'])

        attr_dict = {attr:self.REF_TYPES[ref_type]['attrs'][attr]['function'](attr_dict[attr])
                    if 'function' in self.REF_TYPES[ref_type]['attrs'][attr] else attr_dict[attr]
                    for attr in attr_dict if attr in self.REF_TYPES[ref_type]['attrs']}

        reference = [self.REF_TYPES[ref_type]['attrs'][attr].get('pre', '') +
                     attr_dict.get(attr, "<No '" + attr + "'>") +
                     self.REF_TYPES[ref_type]['attrs'][attr].get('post', '')
                     for attr in attr_ordered]
        return '<p>' + ''.join(reference) + "</p>"

    def extrapolateAttributes(self, attr_dict):
        ex_dict = {}
        if 'name' in attr_dict:
            name = filter(lambda n: n != '', attr_dict['name'].split(' '))
            if name:
                if len(name) >= 1:
                    ex_dict['first initial'] = name[0][0]
                if len(name) >= 1 and len(name[0]) > 1:
                    ex_dict['first name'] = name[0]
                if len(name) == 2 and len(name[1]) > 1:
                    ex_dict['last name'] = name[1]
        elif 'first name' in attr_dict:
            ex_dict['first initial'] = attr_dict['first name'][0]

        return ex_dict

    def getCommands(self):
        return {"link" : "add a link into the document - can be optionally paramatised with [] to alter link text"}

    def validateCommand(self, command):
        if not command[len(self.REF_PREFIX)] == ':':
            raise SyntaxError("ref commands must be followed by a colon")
        elif ' ' not in command:
            raise SyntaxError("ref:<type> must contain a space after the type")
        elif '{' not in command:
            raise SyntaxError("Missing '{' after ref:<type>")
        elif '}' not in command:
            raise SyntaxError("Missing '}' after attributes")

    def removeWhitespacePadding(self, string):
        if not (isinstance(string, str)):
            raise AttributeError("Text is not a string")
        return string.lstrip()[::-1].lstrip()[::-1]

    def completeCommand(self, command):

        if not (isinstance(command, str)):
            raise AttributeError("Text is not a string")

        html = command

        if command.startswith(self.REF_PREFIX):

            self.validateCommand(command)

            ref_type = command[command.index(':') + 1:command.index(' ')]

            if ref_type in self.REF_TYPES:
                # Get attributes, removing whitespace from the start and end of the statement
                attrs = self.removeWhitespacePadding(command[command.index(' ') + 1:])

                if not attrs.startswith('{'):
                    raise SyntaxError("Expected a '{' after ref:<type>")
                elif not attrs.endswith('}'):
                    raise SyntaxError("Expected a '}' at the end of the line")

                attrs_contents = attrs[1:len(attrs) - 1].split(',')

                attr_dict = {}
                for attr in attrs_contents:
                    if ':' not in attr:
                        raise SyntaxError("Attribute name and value pair '%s' missing colon seperator" % attr)
                    if not attr.count(':') == 1:
                        raise SyntaxError("Attribute name and value pair '%s' has more than one colon seperator" % attr)

                    attr_name, attr_val = attr.split(':')
                    attr_name = self.removeWhitespacePadding(attr_name)
                    attr_val = self.removeWhitespacePadding(attr_val)

                    if attr_name in attr_dict:
                        raise NameError("Duplicate attribute name '%s'" % attr_name)

                    attr_dict[attr_name] = attr_val

                html = self.parseReference(attr_dict, ref_type)
            else:
                raise NameError("Reference type '%s' does not exist. Reference types must be declared in the format ref:<type>" % ref_type)


        return html



if __name__ == '__main__':
    module = ReferenceModule()
    output = module.completeCommand("ref:website {last name:esc, first initial:k, published:2015, \
                                                  title:testtitle, journal:bookofsomething, volume:3, pages:24-36, \
                                                  url:www.test.com, accessed:23/07/2008}")
    output += '\n\n'
    output += module.completeCommand("ref:book {authors:fname1 sname1|fname2 sname2, published:2014, title:testtitle, \
                                                city:Leeds, publisher:Some Book Publisher(tm), pages:134-146}")
    output += '\n\n'
    output += module.completeCommand("ref:newspaper {last name:esc, first initial:k, published:2015, \
                                                     title:testtitle, newspaper:the something times, pages:24-36}")
    output += '\n\n'
    output += module.completeCommand("ref:onlinenewspaper {last name:esc, first initial:k, published:2015, \
                                                           title:testtitle, newspaper:the something times, pages:24-36, \
                                                           url:www.test.com, accessed:23/07/2008}")
    output += '\n\n'
    output += module.completeCommand("ref:magazine {first name:kevin, last name:hodgson, published:2015, \
                                                    title:testtitle, magazine:the something mag, volume:43, \
                                                    pages:24-36}")


    print("output = " + str(output))
