import os

# name prints the type of the Operating System
# nt for Windows, posix for Unix and java if the code is written in Jython
print(os.name)

# This method prints the List of the directories from the present path.
print(os.listdir())

# Create a new Directory in the path
os.makedirs("./my_first_dir")
# os.makedirs("./my_first_dir/sec_dir")

# getcwd helps to give the path where we are currently.
print(os.getcwd())

os.rmdir("my_first_dir")

# os.removedirs("my_first_dir/sec_dir")

# os.chdir("my_first_dir")

# print(os.listdir())