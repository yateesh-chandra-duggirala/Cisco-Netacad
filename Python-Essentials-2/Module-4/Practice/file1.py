## Opening the stream for the first time
# We open the try-except block as we want to handle run time errors
try:

    # Use open() function to try to open the specified file
    # The mode is set to read text (rt). You can also skip t if you need.
    stream = open("C:/Users/Yateesh Chandra/OneDrive/Desktop/pro.txt", 'r')
    
    # if we are successful, we get an object from the open() function and we assign it to the stream variable
    stream.close()

# If open() fails, we handle the exception by printing the full error information.
except Exception as e :
    print(e)