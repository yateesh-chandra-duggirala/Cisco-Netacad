from os import strerror

# Prompt the user to enter the name of the file to copy
srcname = input("Enter the Source file : ")

try :
    src = open(srcname, 'rb')
except IOError as e : 
    print("Failed with : ", strerror(e.errno))

    # Use the exit function to stop program execution and to pass the completion code to the OS.
    # Any completion code other than 0 would say the program has encountered problems
    exit(e.errno)

destname = input("Enter the Destination file : ")

try :
    dest = open(destname, 'wb')
except IOError as e :
    print("Can not create destination", strerror(e.errno))
    src.close()
    exit(e.errno)

# Prepare a piece of memory for transferring data from source file to target one, such a transfer area is called buffer
# The size of the buffer is arbitrary
# A larger buffer is faster at copying items as a large buffer means fewer IO operations, actually there is always a limit.
# The crossing of which renders no further improvement.
buffer = bytearray(65535)

# Count the bytes copied
total = 0

try : 
    # Fill the buffer at the very first time
    readin = src.readinto(buffer)
    while readin > 0:
        # Write the buffer contents to the output files
        written = dest.write(buffer[:readin])

        total += written

        # Read the next chunck of code.
        readin = src.readinto(buffer)
except IOError as e : 
    print("Cannot create destination file : ", strerror(e.errno))
    exit(e.errno)

print(total, "Bytes successfully written")
src.close()
dest.close()