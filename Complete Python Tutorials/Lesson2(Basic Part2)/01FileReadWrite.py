# **********---- Reading and Writing Files
# to work with files with ease make sure the files are in the same working directory or
# in the same folder where you are saving your python files

fileVariable = open('workfile','r+')
# The first argument is a string containing the filename.
# The second argument is another string containing a few characters describing the way in which the file will be used.
# Mode can be 'r', 'w', 'a', 'r+'
# 'r' when the file will only be read,
# 'w' for only writing (an existing file with the same name will be erased), and
# 'a' opens the file for appending; any data written to the file is automatically added to the end.
# 'r+' opens the file for both reading and writing. The mode argument is optional;
# 'r' will be assumed if it’s omitted.


# Normally, files are opened in text mode, that means,
# you read and write strings from and to the file, which are encoded in a specific encoding.
# If encoding is not specified, the default is platform dependent (see open()).
# 'b' appended to the mode opens the file in binary mode: now the data is read and written in the form of bytes objects.
# This mode should be used for all files that don’t contain text.

# In text mode, the default when reading is to convert platform-specific line endings
# (\n on Unix, \r\n on Windows) to just \n.
# When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings.
# This behind-the-scenes modification to file data is fine for text files,
# but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode
# when reading and writing such files.

# **********---- Methods of File Objects
# fileVariable.read()
# for each in fileVariable:
#     print(each)
# To read a file’s contents, call fileVariable.read(size),
# which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).
# Size is an optional numeric argument.
# When size is omitted or negative, the entire contents of the file will be read and returned;
# it’s your problem if the file is twice as large as your machine’s memory.
# Otherwise, at most size bytes are read and returned.
# If the end of the file has been reached, fileVariable.read() will return an empty string ('').


fileVariable.readline()
file = list(fileVariable)

# f.readline() reads a single line from the file;
# A newline character (\n) is left at the end of the string, and is only omitted on the last line of the file
# If the file doesn’t end in a newline. This makes the return value unambiguous;
# If f.readline() returns an empty string, the end of the file has been reached,
# while a blank line is represented by '\n', a string containing only a single newline.
# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

# ***** We can use print to see what is in the file
for each in fileVariable:
    print(each)

# f.write(string) writes the contents of string to the file, returning the number of characters written.
fileVariable.write("\nThis is a new line\n")            # returning the number of characters written.
# Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode)
# – before writing them:
value = ('the answer', 42)
s = str(value)                      # convert the tuple to string
print(fileVariable.write(s))

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes
# from the beginning of the file when in binary mode and an opaque number when in text mode.
print("Position of the object is: ",fileVariable.tell())

# To change the file object’s position, use f.seek(offset, from_what).
# The position is computed from adding offset to a reference point;
# the reference point is selected by the from_what argument.
# A from_what value of 0 measures from the beginning of the file, 1 uses the current file position,
# and 2 uses the end of the file as the reference point.
# from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
fileVariable = open('workfile', 'rb+')
print(fileVariable.write(b'0123456789abcdef'))
print(fileVariable.seek(5))      # Go to the 6th byte in the file
print(fileVariable.read(1))
print(fileVariable.seek(-3, 2))  # Go to the 3rd byte before the end
print(fileVariable.read(1))
# In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file
# are allowed (the exception being seeking to the very file end with seek(0, 2)) and
# the only valid offset values are those returned from the f.tell(), or zero.
# Any other offset value produces undefined behaviour.
#
# When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file.
# After calling f.close(), attempts to use the file object will automatically fail.

# It is good practice to use the with keyword when dealing with file objects.
# This has the advantage that the file is properly closed after its suite finishes, even if an exception is
# raised on the way. It is also much shorter than writing equivalent try-finally blocks:
with open('workfile', 'r') as f:
    read_data = f.read()
f.closed

# **********---- Saving structured data with json
# Standard module called json can take Python data hierarchies, and convert them to string representations;
# this process is called serializing.
# Reconstructing the data from the string representation is called deserializing.
# Between serializing and deserializing, the string representing the object may have been stored in a file or data,
# or sent over a network connection to some distant machine.


import json
# If you have an object x, you can view its JSON string representation with a simple line of code:
x = json.dumps([1, 'simple', 'list'])
print(x)
# Another variant of the dumps() function, called dump(), simply serializes the object to a text file.
# So if f is a text file object opened for writing, we can do this:
# json.dump(x, f)


# To decode the object again, if f is a text file object which has been opened for reading
# x = json.load(f)


# This simple serialization technique can handle lists and dictionaries,
# but serializing arbitrary class instances in JSON requires a bit of extra effort.
# The reference for the json module contains an explanation of this.