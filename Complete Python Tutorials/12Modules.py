# **********---- Modules
# A module is a file containing Python definitions and statements. The file name is the
# module name with the suffix .py appended. Within a module, the module’s name (as a string)
# is available as the value of the global variable __name__.
# Every python file you create can be used as module
# The syntax to use a python file as module is import pythonfilename
import SampleModule
x = SampleModule.funNumbers(300)
print("printing the result of Fibonacci from an external file", x)
print("\n"*2)


# Every python file we write has an global variable __name__ with value which sets itself to the filename
# Lets check for the SampleModule
print("__name__ of SampleModule is: ", SampleModule.__name__)
print("\n"*2)


# By using modules you can call methods, classes, variables from the desired module
# If you are using a function frequently you can assign the function to a variable
y = SampleModule.funNumbers
print("if you are using a function frequently you can assign the function to a variable")
print(y(400))
print("\n"*2)


# Note: Modules are executed the first time the module name is encountered in an import statement
# Each Module has it its own private symbol table, which is used as the
# global symbol table by all functions defined in the module.
# Thus, the author of a module can use global variables in the module without worrying about
# accidental clashes with a user’s global variables.
# If you ever want to use the variables used in the module, you can use them by
# modulename.variablename

# Note: Modules can import other modules, It is good practice to use all the import statements at
# beginning of the file.
# The imported module names are placed in the importing module’s global symbol table.
# There is a variant of the import statement that imports from a module directly
# into the importing module’s symbol table.
# If you are specific about a function that you want to import you can do this
# from module import function
from SampleModule import funNumbers
print("printing the result of Fibonacci using 'from import'", funNumbers(300))
print("\n"*2)

# You can use * to import everything, except those beginning with an underscore (_).
# for best practice try to avoid using * to import everything
# In most cases Python programmers do not use this facility since it introduces an
# unknown set of names into the interpreter, possibly hiding some things you have already defined.
from SampleModule import *                      # this will import everything from SampleModule


# Note: For efficiency reasons, each module is only imported once per interpreter session.
# Therefore, if you change your modules, you must restart the interpreter – or,
# if it’s just one module you want to test interactively, use importlib.reload(),
# e.g. import importlib; importlib.reload(modulename).


# **********---- Executing modules as scripts
# You can run a Python module with
# python filename.py arguments
# To run the above file you have to include the following code at the end.

# if __name__ == "__main__":
#     import sys
#     funNumbers(int(sys.argv[1]))

# you can make the file usable as a script as well as an importable module, because the code that parses the command
# line only runs if the module is executed as the “main” file

# **********---- The Module Search Path
# when ever a module is imported python interpreter will search for a built-in module with that name.
# It then searches for a file named spam.py in a list of directories given by the
# variable sys.path.
# sys.path is initialized from these following locations
# The directory containing the input script (or the current directory when no file is specified).
# PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# The installation-dependent default.


# **********----  Standard Modules
# Python comes with a library of standard modules, described in a separate document, the Python Library Reference
# (“Library Reference” hereafter). Some modules are built into the interpreter; these provide access to operations
# that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide
# access to operating system primitives such as system calls.


# **********----  The dir() Function
# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings
# Without arguments, dir() lists the names you have defined currently:
import SampleModule
print("Whats in the file\n", dir())
print("\nPrinting everything present in SampleModule\n", dir(SampleModule))

# dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in
# the standard module builtins
import builtins
print("\nPrinting everything present in builtins which contains dir\n", dir(builtins))


# **********----  Packages
# packages are collection of modules in a directory with a directory name
# If you want to access the modules from a specific directory the syntax is import packagename.modulename
# Just like the use of modules saves the authors of different modules from having to worry about each other’s global
# variable names, the use of dotted module names saves the authors of
# multi-module packages like NumPy or the Python Imaging Library from having to worry about each other’s module names.

# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package,
# or some other name defined in the package, like a function, class or variable. The import statement first tests
# whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails
# to find it, an ImportError exception is raised.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package;
# the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

# Now what happens when the user writes from sound.effects import *? Ideally, one would hope that this somehow goes
# out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a
# long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module
# is explicitly imported.

# The only solution is for the package author to provide an explicit index of the package. The import statement uses
# the following convention: if a package’s __init__.py code defines a list named __all__, it is taken to be the list
# of module names that should be imported when from package import * is encountered. It is up to the package author
# to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to
# support it, if they don’t see a use for importing * from their package. For example,
# the file Beginner/Lesson/__init__.py could contain the following code:
# __all__ = ["Functions", "List", "Sets"]
# This would mean that from Beginner.Lesson import * would import the three named submodules of the sound package.

# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package
# sound.effects into the current namespace; it only ensures that the package sound.effects has been imported
# (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package.
# This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules
# of the package that were explicitly loaded by previous import statements.

# ---- Consider this code:
# import Beginner.Lesson.List
# import Beginner.Lesson.Functions
# from Beginner.Lesson import *

# In this example, the List and Functions modules are imported in the current namespace because they are
# defined in the Beginner.Lesson package when the from...import statement is executed.
# (This also works when __all__ is defined.)

# Although certain modules are designed to export only names(can be anything in a module) that follow certain patterns
# when you use import *, it is still considered bad practice in production code.

# Remember, there is nothing wrong with using from Package import specific_submodule! In fact, this is the
# recommended notation unless the importing module needs to use submodules with the same name from different packages.

# **********----  Intra - package References (packages inside packages)

# When packages are structured into subpackages (as with the sound package in the example), you can use absolute
# imports to refer to submodules of siblings packages. For example, if the module sound.filters.vocoder needs to use
# the echo module in the sound.effects package, it can use from sound.effects import echo.

# You can also write relative imports, with the from module import name form of import statement. These imports use
# leading dots to indicate the current and parent packages involved in the relative import. From the surround module
# for example, you might use:

# from . import echo
# from .. import formats
# from ..filters import equalizer

# Note that relative imports are based on the name of the current module. Since the name of the main module is always
# "__main__", modules intended for use as the main module of a Python application must always use absolute imports.


# **********----  Packages in Multiple Directories

# Packages support one more special attribute, __path__. This is initialized to be a list containing the name of
# the directory holding the package’s __init__.py before the code in that file is executed. This variable can be
# modified; doing so affects future searches for modules and subpackages contained in the package.