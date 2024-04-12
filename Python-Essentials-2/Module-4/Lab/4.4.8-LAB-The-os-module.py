'''
It goes without saying that operating systems allow you to search for files and directories. 
While studying this part of the course, you learned about the functions of the os module, 
which have everything you need to write a program that will search for directories in a given location.

To make your task easier, we have prepared a test directory structure for you:

Your program should meet the following requirements:

- Write a function or method called find that takes two arguments called path and dir. 
- The path argument should accept a relative or absolute path to a directory where the search should start,
 while the dir argument should be the name of a directory that you want to find in the given path.
- Your program should display the absolute paths if it finds a directory with the given name.
- The directory search should be done recursively. 
- This means that the search should also include all subdirectories in the given path.

Example input:
path="./tree", dir="python"

Example output:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python

'''

import os

os.chdir("Python-Essentials-2/Module-4/Lab")
print(os.getcwd())

def create_dirs():
    os.makedirs("./tree/python/other_courses/c")
    os.makedirs("./tree/python/other_courses/cpp")
    os.makedirs("./tree/c/other_courses/cpp")
    os.makedirs("./tree/c/other_courses/python")
    os.makedirs("./tree/cpp/other_courses/c")
    os.makedirs("./tree/cpp/other_courses/python")

create_dirs()

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "\\" + dir)
            self.find(current_dir + "\\" + entry, dir)


ds = DirectorySearcher()
ds.find("./tree", "python")