# Generators - Iterators - Closures
## Generators :
- A Python generator is a piece of specialized code able to produce a series of values and to control the iteration processes.
- This is the reason why generators are also called as Iterators.
- Consider the following piece of code :
    ```
    for i in range(5):
        print(i)
    ```
  Here, The range() is a generator and again an iterator

- The difference is A function returns one, well-defined value - It may be the result of a more or less complex evaluation of, something like a polynomial, and is invoked once - only once.
- A generator returns a series of values and in general is invoked more than once.
- In example, the range() generator is invoked six times, providing five subsequent values from zero to four and finally signaling that the series is complete.
- The Iterator protocol is a way in which an object should behave to confirm to the rules imposed by the context of the for and in statements. 
- An object conforming to the iterator protocol is called an iterator.

- An iterator must provide 2 methods :
    a. __iter__() which should return the object itself and which is invoked once
    b. __next__() which is intended to return the next value of the desired series - It will be invoked by the for / in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.
- The process goes like this :
    a. The iterator object is instantiated first.
    b. Python invokes the __iter__() method to get access to the actual iterator
    c. The __next__() method will be invoking n+1 times. The result woould run for n invocations by terminating the iteration at n+1 th time.

## yield statement :
- The iterator protocol is not particularly difficult to understand and use, but it is also indisputable that the protocol is rather inconvenient.
- The Main disadvantage is the need to save the state of the iteration between subsequent __iter__  invocations.
- For example, the Fib iterator is forced to precisely store the place in which the last invocation has been stopped. This makes the code larger and less comprehensible.
- Hence, Python offers a much more effective, convenient and elegant way of writing iterators.
- This concept is fundamentally based on a very specific and powerful mechanism provided by the yield keyword.
- yield and return statement have one essential difference.

- For loop has no chance to finish the first execution as the return will break it irrevocably.
- Invoking the function will not change anything - the for loop will start from scratch and will be broken immediately.
- We can say that such a function is not able to save and restore its state between subsequent invocations.
- This also means that a function like this cannot be used as a generator.
- Meanwhile we can add yied, instead of return.
- This little amendment turns the function into a generator, and executing the yield statement has some very interesting effects.
- First of all, it provides the value of the expression specific after the yield keyword, just like return but does not lose the state of the function. 
- All the variables' values are frozen and wait for the next invocation, when the execution is resumed
- There is one important limitation; such a function should not be invoked explicitly as - in fact - it is not a function anymore; It is a generator object.
- The invocation will return the object's identifier, not the series we expect from the generator.
- Due to the same reasons, the previous function may only be invoked explicitly and must not be used as a generator.

a. List Comprehensions : Generators may also be used within the list comprehensions.
b. list() function : The list() function can transform a series of subsequent generator invocations into real list.
c. in operator : Moreover the context created by the in operator allows you to generate an operator.

## Conditional Expression :
- This is a way of selecting one of two different values based on the result of a boolean expression. 
- Just Something `exp1 if condition else exp2`
- This is not a conditional expression, This is not even instruction.. this is a operator.
- Two main words should come into mind while looking into code : Compactness and Elegance.
- Just only one change can turn any list comprehension into a generator.
- [] Closed brackets make a Comprehension and () Parentheses make a generator.
- We can work on the lists and generators without creating.
- However, List is automatically created but Generator is not automatically created.

## Lambda Function :
- The Lambda Function is used to simplify the code, to make it clearer and easier to understand.
- A lambda function is a function without name (Anonymous function).
- It is declared as :
    `lamdba parameters : expression`
- This clause returns the value of the expression when taking into account the current value of the current lambda argument.
- From lambda-function example, It is clear that :
    a. The first Lambda is an anonymous parameterless function that always returns 2. As we have assigned it to a variable named two, we can say that the function is not anonymous anymore and we can use that name to invoke it.
    b. The second one is a one parametered function that returns the value of its squared argument.
    c. The third lambda takes two parameters and returns the value of the first one raised to the power of the second one. The name of the variable which carries the lambda speaks for itself.
- This is how code is made shorter, clearer and more legible

## Lambdas and the map() function :
- map() function is declared as map(function, list).
- The second map() argument may be an entity that can be iterated  (eg. Tuple or just a generator)
- map() can accept more than two arguments.
- The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent result.
- You can use the resulting iterator in a loop or convert it into a list using the list() function.

## Lambdas and filter() function :
- This function expects same type of arguments as of map() function
- It filters the second argument while being guided by directions flowing from the function specified as the first argument.

## Closures :
- A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore.
- Consider the example outer.py
- inner() may be invoked only from within outer().
- We can say that inner() is outer()'s private tool. No other part of the code can access it.
- The inner() function is parameterless, so we have to invoke it without arguments.
- Now It is fully possible to declare a closure equipped with an arbitrary number of parameters.
- Closure not only makes use of the frozen environment, but it also can modify its behavior by using values taken from the outside.
- This example shows one more interesting circumstance - you can create as many closures as you want using one and the same piece of code. This is done with a function named make_closure().

# Files :
- One of the most common issues in the developer's job is to process data stored in files while the files are usually physically stored using storage devices - hard, optical, network, or solid-state disks.
- Our program can can sort twenty numbers and it is equally easy to imagine the user of this program entering these twenty numbers directly from the keyboard.
- When There are more than 20000 numbers to be sorted, and there is a single user who is able to enter these numbers without making a mistake.
- It is much easier to imagine that these numbers are stored in the disk file which is read by the program. The program sorts the numbers and doesnot send them to the screen, but instead creates a new file and saves the sorted sequence of numbers there.
- If we want to implement a simple database, the only way to store the information between program runs is to save into a file.
- In principle, any non-trivial programming problem relies on the usage of files, whether it processes images or multiplies matrices or calculates wages and taxes.
- Python's way of accessing and processing files is implemented using a consistent set of objects.

## File names :
- If we use the notion of a canonical file name, we can realize that these names look different in windows
- Unix and Linux file names are case sensitive but windows are not.
- The main and most striking difference is that you have to use two different seperators for the directory names : \ for windows and / for unix or linux.
- But later both '/' and '\' are accepted for windows.
- Any program written in Python does not communicate with the files directly, but through some abstract entities that are named differently in different languages or environments - the most - used terms are handles or streams.
- The programmer, having a more- or less-rich set of functions/ methods is able to perform certain operation on the stream, which affect the real files using mechanisms contained in the operating system kernel.
- In this way, you can implement the process of accessing any file, even when the name of the file is unknown at the time of writing the program.
- The operations performed with the abstract stream reflect the activities related to the physical file.
- To connect the stream with the file, It is necessary to perform an explicit operation.
- The operation of connecting the stream with a file is called opening the file, while disconnecting this link is named as closing the file.
- Hence the conclusion is that the very first operation performed on the stream is always open and the last one is close.
- The program is free to manipulate the stream between these two events and to handle the associated file.
- This freedom is limited, of course by the physical characteristics of the file and the way in which the file has been opened.
- Opening of the stream can fail, and it may happen due to several reasons : The most common is the lack of a file with a specified name.
- It can also happen that the physical file exists, but the program is not allowed to open it.
- There is also the risk that the program has opened too many strams and the specific operating system may not allow the simultaneous opening of more than n files (may be 200)
- A well written program should detect these failed openings and react accordingly.

## File Streams : 
- The opening of the stream is not only associated with the file, but should also declare the manner in which the stream will be processed.
- This declaration is called an open mode.
- If the opening is successful, the program will be allowed to perform only the operations which are consistent with the declared open mode.
- There are two basic operations performed on the stream :
    a. read from the stream : the portions of the data are retrieved from the file and placed in a memory area managed by the program.
    b. write to the stream : The portions of the data from the memory are transferred to the file.
- There are three basic modes used to open the stream :
    a. read mode : A stream opened in this mode allows read operations only, trying to write the stream will cause an exception (UnsupportedOperation - inherits from OSError and ValueError).
    b. write mode : A stram opened in this mode allows write operations only, attempting to read the stream will cause the exception mentioned above.
    c. update mode : A stream openend in this mode allows both read and write operations.
- The stream almost behaves like a tape recorder.
- When you read something from a stream, a virtual head moves over the stream according to the number of bytes transferred from the stream.
- When you write something to the stream, the same head moves along the stream recording the data from the memory.

## File Handles :
- Python assumes that every file is hidden behind an object of an adequate class.
- Of Course, It is hard not to ask how to interpret the word adequate.
- Files can be processed in many different ways - some of them depends on the file's contents, some on the programmer's intentions.
- In any case, different files may require sets of operations and behave in different ways.
- An object of an adequate class is created when you open the file and annihilate it at the time of closing.
- Between these two events, you can use the object to specify what operations should be performed on a particular stream.
- The operations you are allowed to use are imposed by the way in which you have opened the file.
- In general, The object comes from one of the classes shown here :
    (RawIOBase, BufferedIOBase, TextIOBase from IOBase)

- Note : You can never use constructors to bring these objects to life. The only way you obtain them is to invoke the function named open().
- This function analyses the arguments you have provided and automatically creates the required object.
- If you want to get rid of the object, you invoke the method named close()
- The invocation will serve the connection to the object and the file, and will remove the object.
- for our purposes, we will concern ourselves only with streams represented by BufferIOBase and TextIOBase objects.
- Due to the type of stream's contexts, all the streams are divided into text and binary streams.
- The text streams are structured in lines; That is, they contain typographical characters (letters, digits, punctuation, etc.) arranged in rows, as seen with the naked eye when you look at the contents of the file in the editor.
- This file is written or read mostly character or character, or line by line.
- The binary streams do not contain text but a sequence of bytes of any value.
- This sequence can be for example, an executable program, an image, an audio or a video clip a database file,etc. As these files do not contain lines, the reads and writes relate to portions of data of any size.
- Hence the data is read/ written byte by byte or block by block, where the size of the block usually ranges from one to an arbitrary chosen value.
- In Unix/ Linux systems, the line ends are marked by a single character named LF (ASCII code 10) designed in python programs as \n.
- Other OS, especially these derived from the prehistoric CP/M system (which applies to Windows family systems, too) use a different convention : The end of the line is marked by a pair of characters CR and LF which can be encoded as \r\n.
- If a program is created responsible for processing a text file and it is written for windows, you can recongnize the ends of the lines by finding the \r\n characters, but the same program running in a Linux / Unix environment can be completely useless and vice versa : the program written for Unix / Linux systems may be useless in Windows. This undesirable feature of preventing the use of program in different environments are called non-portable.

- It was done at the level of classes, which are responsible for reading and writing characters to and from the stream. It works in the following way :
    a. When the stream is open and it is advised that the data in the associated file will be processed as text, it is switched into text mode.
    b. During Reading / Write of lines from / to the associated file, nothing special occurs in the Unix Environment, but when the same operations are performed in the Windows environment, A process called a translation of newline characters occurs : When you read a line from the file, every pair of \r\n characters is replaced with a single \n character and vice versa during write operations, every \n characters is replaced with a pair of \r\n characters.
    c. The mechanism is completely transparent to the program, which can be written as if it was intended for processing Unix / Linux text files only. The source code run in a windows environment all work properly, too
    d. When the stream is open and it is advised to do so, its contents are taken as-is, without any conversion - no bytes are added or omitted.

## Opening the Streams :
- The opening of the Stream is performed by a function which can be invoked :
    `stream = open(file, mode = 'r', encoding = None)`
    a. The name of the function 'open' speaks for itself, if the opening is successful, the function returns a stream object; otherwise an exception is raised(FileNotFoundError, If the file to read does not exist).
    b. The first parameter of the function specifies the name of the file to be associated with the stream
    c. The second parameter mode specifies the open mode used for the stream, it is a string filled with a sequence of characters, and each of them has its own special meaning.
    d. The third parameter encoding specifies the encoding type (eg. UTF-8 when working with text files)
    e. The opening must be very first operation performed on the stream.
- Note the mode and encoding arguments may be omitted - their default values are assumed then.
- The default opening mode is read in text mode, while the default encoding depends on the platform used.

### Modes :
1. open mode : read (r)
    - The stream will be opened in read mode.
    - The file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.
2. open mode : write (w)
    - The stream will be opened in write mode.
    - The file associated with the stream does not need to exist; if it doesn't exist it will be created; if it exists, it will be truncated to the length of zero; If the creation is not possible due to system permissions, the open() function rasies an exception.
3. open mode : append (a)
    - The stream will be opened in append mode.
    - The file associated with the stream doesn't need to exist. If it does not exist, it will be created. If it exists, The virtual recording head will be set at the end of the file (The previous content of the file remains untouched).
4. open mode : read and update (r+)
    - The stream will be opened in read and update mode.
    - The file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception.
    - both read and write operations are allowed for the stream.
5. w+ open mode : write and update
    - The stream will be opened in write and update mode.
    - The file associated with the stream doesn't need to exist; it will be created; the previous content of the file remains untouched
    - both read and write operations are allowed for the stream

## Selecting text and binary modes : 
- If there is a letter at the end of the mode string, it means that the stream is to be opened in binary mode.
- If the mode string ends with a letter t, the stream is opened in Text mode.
- Text mode is the default behavior assumed when no binary / text mode specifier is used.
- Finally, the successful opening of a file will set the current file position before the first byte of the file if the mode is not a and after the last byte of the file if the mode is set to a.

                    text    binary
read                rt      rb
write               wt      wb
append              at      ab
read and update     r+t     w+t
write and update    w+t     w+b

- You can also open a file for its exclusive creation.
- You can do this using the x open mode.
- If the file already exists, the open() will raise an exception

## Pre-opened Streams :
- Any Stream operation must be preceded by the open() function. There are three well-defined exceptions.
- When our program starts, the three streams are already opened and do not require any extra preparations.
- Our program can use these streams explicitly if you take care to import the sys module. because that is where the declaration of the three streams is placed.
- The names of these streams are : sys.stdin, sys.stdout, sys.stderr.
- Let us analyze them :
    a. sys.stdin (as standard input) stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs. The well known input() function reads the data from stdin by default.
    b. sys.stdout (as standard output) stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program. The well know print() function outputs the data to the stdout stream.
    c. sys.stderr (as standard error output) stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work. We have not presented any method to send the data to this stream.
    - The seperation of stdout gives the possibility of redirecting these two types of information to the different targets.
    - More extensive discussion of this issue is beyond the scope of our course.
    - The operation system handbook will provide more information on these issues
## Closing Streams :
- The last operation performed on a stream should be closing.
- This action should be done by `stream.close()`
    a. The name of the function is definitely self-commenting : close()
    b. The function expects exactly no arguments; the stream does not need to be opened.
    c. The function returns nothing, but raises an IOError exception in case of any error.
    d. Most developers believe that the close() function always succeeds and thus there is no need to check if it is done its task properly.
- This belief is only partly justified. If the stream was opened for writing and then series of write operations were performed, it may happen that the data sent to the stream has not been transferred to the physical device yet.
- Since the closing of the stream forces the buffers to flush them, it may be that flushes fail and therefore the close() fails too.

## Diagnosing stream problems :
- The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can access it as follows :

    `try :
        # Some Stream operations
    except IOError as exc: 
        print(exc.errno)
    `
- The value of the errno attribute can be compared with one of the predefined symbolic constants defined in the errno module.
- Let us take a look at some selected constants useful for detecting stream errors :

    a. errno.EACCES -> Permission Denied (Occurs when try to open a file for writing but it actually has read-only attribute)
    b. errno.EBADF -> Bad File Number (Occurs when try to operate with an unopened stream).
    c. errno.EEXIST -> File exists (Try to rename file with previous name)
    d. errno.EFBIG -> Files too large (try to create a file that is larger than the maximum allowed by the operating system)
    e. errno.EISDIR -> Is a Directory (Try to treat a directory name as the name of an ordinary file.)
    f. errno.EMFILE -> Too many open files (try to simultaneously open more streams than acceptable for your OS)
    g. errno.ENOENT -> No Such file or directory (Try to access a non-existent file / directory).
    h. errno.ENOSPC -> No space left on the device. (The error occurs when there is no free space on media).
- We have a function that can dramatically simplify the error handling code, named strerror() and it comes from the os module and expects just one argument - an error number.

## Processing text files :
- We can read the file contents to process them by copying the file contents to the console and count all the characters the program has read in.
- The file should be strict text file (No decorations, no different fonts, no characters unrecognized by ASCII).
- We can read the function as `stream = open('file.txt', 'rt', encoding = 'utf-8')`
### Method - 1 : read() 
- read() function when applied to a text file, the function is able to :
    a. Read a desired number of characters from the file, and return them as a string
    b. Read all the file contents and return them as string.
    c. If there is nothing more to read, the function returns an empty string.
- Reading a terabyte - long file using this method may corrupt your OS.

### Method - 2 : readline()
- If we want to treat the file's contents as a set of lines, not a bunch of characters, the readLine() method will help you with that.
- The method tries to read a complete line of text from the file, and returns it as a string in the case of success. or else, it returns an empty string.

## Writing into files :
- write() is a function and it expects a single argument - a string that should be transferred to an Open file.
- Open mode should reflect the way in which the data is transferred - writing a file opened in read mode will not succeed.
- No new line character is added to the write()'s argument, so you have to add it yourself if you want the file to be filled with a number of lines.

## Byte Array :
- Amorphous data is data that has no specific shape or form. - They are just series of bytes.
- This data can not be stored using any of the previously presented means - neither strings nor lists.
- There should be a special container able to handle such data.
- Python has more than one such special container -byterarra, an array containing bytes.
- In order to read in a bit map image and process it in any way, you need to create explicitly, using one of the available constructors.
- Such an invocation creates a byte array object able to store ten bytes.
- Note : Such a constructor fills the whole array with zeros.
- Bytearrays resemble lists in many aspects. For example, they are mutable they are a subject of the len() function, and you can access any of their elements using conventional indexing.
- It is important to note that we must not set any byte array elements with a value which is not an integer (Violating this rule will cause a TypeError Exception) and you are not allowed to assign a value that does not come from the range 0 to 255 inclusive (unless you want to provoke a valueError exception)
- You can treat any byte array elements as integer values.
- The write() method returns a number of successfully written bytes.
- If the value differ from the length of the method arguments, it may announce some write errors.

## Reads bytes from a stream : 
- Reading from a binary file requires the use of a specialized method name readinto(), as the method doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file.
- Note : 
    a. The method returns the number of successfully read bytes.
    b. The method tries to fill the whole space available inside its argument; if there are more data in the file than space in the argument, the read operation will stop before the end of the file.
    c. Otherwise, the method's result may indicate that the byte array has only been filled fragmentarily.

- Alternatively, we can use read() method to read the contents.
- it is invoked without arguments, it tries to read all the contents of the file into memory, making them a part of a newly created object of the bytes class.
- This class has some similarities to bytearray, with the exception of one significant difference - it is immutable.
- This read() should be not be used when we are not sure whether the file's contents will fit the available memory.
- If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read.
- The method tries to read the desired  number of bytes from the file, and the length of the returned object can be used to determine the number of bytes actually read.

## Copying files - a simple and functional tool
- We can copy files using this file stream, but that does not mean that it is efficient than commands of (cp) Linux and (copy) Windows.

# OS Module : 
- This module helps users to interact with Operating System using Python.
- It helps us to : 
    a. make directories and files.
    b. get information about the operating system
    c. Manage processes.
    d. Operate on I/O streams using file descriptors.

### a. Getting Information about the Operating System
- Before creating first directory structure, we can see how we get information about the current operating system.
- This is really easy because of the function uname, which returns an object.
- Systemname, nodename, release, version and machine are the attributes of the object.

### b. Making Directories in Python
- mkdir function helps us to create a directory.
- my_dir -> this will create in the current working directory
- ./my_dir -> This joins the path and creates the directory. This is also the same effect as previous.
- ../my_first_directory -> This will create directory in the parent directoryof current working Directory.
- /python/my_first_dictionary -> This is the absolute path that will create the directory which in turn is in the python directory in the root directory.

- mkdir() can only work if there is no existing directory with same name. It does not create twice.
- To change the directory permissions, chmod() function is used.

### c. Recursive Directory Creation 
- Instead of checking out to the folder and run mkdir command, OS module provides a method named makedirs()
- makedirs enable recursive directory creation, which means that all directories in the path are created.
- chdir() function works as cd command

### d. Deleting Directories 
- We can delete one directory with the help of rmdir function from os module that works similar to rmdir command.
- If we want to delete any directory with all its sub-directories, Then we use the removedirs()

### e. system function
- We can simply use a function called system() that helps user to run any command as it is how they run on any Operating System.
- If we get zero as exit status, It means the command ran successfully.