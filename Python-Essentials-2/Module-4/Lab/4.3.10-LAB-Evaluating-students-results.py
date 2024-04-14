'''
Scenario : 
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. 
Each line of the file contains three elements: 
    - the student's first name, 
    - the student's last name, 
    - and the number of points the student received during certain classes.

The elements are separated with white spaces. 
Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

samplefile.txt :
John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5

Your task is to write a program which:
    - asks the user for Prof. Jekyll's file name;
    - reads the file contents and counts the sum of the received points for each student;
    - prints a simple (but sorted) report, just like this one:

Output :
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0


Note:
- your program must be fully protected against all possible failures: 
    a. the file's non-existence, 
    b. the file's emptiness, 
    c. or any input data failures;
encountering any data error should cause immediate program termination, 
and the error should be presented to the user;
implement and use your own exceptions hierarchy - we've presented it in the editor; 
the second exception should be raised when a wrong line is detected, 
and the third when the source file exists but is empty.
Tip: Use a dictionary to store the students' data.
'''

# A base exception class for our Code
class StudentsDataException(Exception):
    pass

# Exception for erroneous file
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string
    
# An exception for file empty 
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

from os import strerror

# Create an empty dictionary for student's data.
student_data = { }

# Prompt the file path
file_name = input("Enter the Student's Data File Path :")
line_num = 1
try : 
    f = open(file_name, 'rt')
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        raise FileEmpty()

    # Scan the files line by line
    for i in range(len(lines)):
    
        # Get the i'th line
        line = lines[i]

        # Divide it into columns
        columns = line.split()

        # There should be 3 columns.
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        
        # Build a key from students' given name and surname
        student = columns[0] + ' ' + columns[1]

        # Get Point
        try :
            points = float(columns[2])
        except ValueError :
            raise WrongLine(i + 1, line)
        
        # Update the Dictionary
        try :
            student_data[student] += points
        except KeyError:
            student_data[student] = points
    
    # Print Results.
    for student in sorted(student_data.keys()):
        print(student, '\t', student_data[student])

except IOError as e:
    print("I/O Error occured", strerror(e.errno))

except WrongLine as e :
    print("Wrong Line #" + str(e.line_number) + "in source file :" + e.line_string)

except FileEmpty:
    print("Source file empty")
