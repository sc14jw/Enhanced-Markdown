# Enhanced Markdown
This project aims to create a framework allowing for the creation of a pdf using a markdown like syntax. The framework also
allows for new commands to be dynamically added to a compiler through the idea of modules. Through the additional functionality
which can be dynamically added to a compiler through the modules system the framework hopes to provide an easy way to write reports
with functionality rivaling that of other report writing languages such as LaTeX. The framework also hopes to be flexible enough
to be customised to any needs and allow for additional functionality in the future.

## Modules
Modules are a way of adding additional functionality to the framework which is accessible through commands which the module will
add to the compiler. These commands always start with a '@' symbol and utilise '()' brackets to define required parameters and
'[]' braces to define optional parameters. For example the link command offered by the LinksModule looks as follows:

```
''' with out optional parameters
@link(<url of website (required)>)

''' with optional parameters
@link(<url of website (required)>)[<link text (optional)>])

```

## Contributors
- Jack Wainwright - jack.wainwright96@gmail.com [Project Owner]
- Kevin Hodgson - Creator of the Referencing Module
