# A true can be transformed into a real python package
# Package, like modules, may require initialization.
# The initialization of a module is done by an unbound code located inside the module's file.
# As a package is not a file, This technique is useless for initializing packages.
# The contents of the file are executed when any of the package's module is imported. 
# If you don't want any special intializations, you can leave the file empty, but you can't omit it.