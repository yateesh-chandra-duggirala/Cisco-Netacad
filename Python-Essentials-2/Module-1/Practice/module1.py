# Add an executable statement whenever any module calls this module.
print("I am a module 1")

# When a module is imported, it also creates a variable called "__name__"
# Moreover, each source file uses its own, seperate version of the variable, it isn't shared between modules.
# But for our understanding, let us print the __name__ . - __main__ is printed as this is the main method.
# print(__name__)

if(__name__ == "__main__") :
    print("I am executing from this module")    # If this module is executed here, This line will be executed
else :
    print("I am executing from", __name__)      # If this module is executed else where, The name of this module will be executed there.