#File Input/Output in Python
#Creating and manipulating files
#Open a file, read its content, write to it, and close it properly.
#Type of all files
#Text files and Binary files
#Example of text files are - .txt, .csv, .py, .html
#Example of binary files are - .jpg, .png, .exe

#File modes
# 'r' - read (default)
# 'w' - write (creates a new file or truncates an existing file)
# 'a' - append (writes data to the end of the file)
# 'b' - binary mode
# 't' - text mode (default)
# '+' - read and write
# 'r+' - (Read + Write (existing file)) overwrite the file from starting of the pointer.
# 'a+' - Append + Read (File exist na ho → ✔️ create ho jaati hai, Write hamesha END me hota hai)

#Reading from a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

#Writing to a file
file = open("example.txt", "w") # open file if exist and if not exist then it will create file.
file.write("Hello, World!") #This will overwrite existing content
file.close()

#Appending to a file
file = open("example.txt", "a")
file.write("\nThis is an appended line.") #This will add content to the end of the file
file.close()

#Using 'with' statement for file operations
with open("example.txt", "r") as file:
    content = file.read() #Reads entire file content
    print(content)

with open("example.txt", "a") as file:
    file.write("\nAnother appended line using 'with'.") #No need to explicitly close the file

with open("example.txt", "w") as file:
    file.write("Overwriting the file content using 'with'.") #File is automatically closed after this block

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) #Reads line by line

with open("example.txt", "r") as file:
    lines = file.readlines() #Reads all lines into a list
    print(lines)

#Delete a file
import os
os.remove("example.txt")

#Check if a file exists
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")

#Binary file operations
#Writing binary data to a file
with open("example.bin", "wb") as binary_file:
    binary_file.write(b'\x00\x01\x02\x03\x04')

#Reading binary data from a file
with open("example.bin", "rb") as binary_file:
    binary_content = binary_file.read()
    print(binary_content)

#Clean up binary file
os.remove("example.bin")

#Example of reading and writing in binary mode
with open("example2.bin", "wb+") as binary_file:
    binary_file.write(b'Hello Binary World!')
    binary_file.seek(0)
    print(binary_file.read())

#Clean up binary file
os.remove("example2.bin") 

## 'r+' - overwrite the file from starting of the pointer.
# File content - Hello World
with open("test.txt", "r+") as f:
    f.write("Hi")

#Result - Hillo World

with open("test.txt", "r+") as f:
    f.seek(6)
    f.write("Python")

#Result - Hello Python

## 'a+' - Append + Read
# File content - Hello
with open("test.txt", "a+") as f:
    f.write(" World")

#Result - Hello World

with open("test.txt", "a+") as f:
    f.seek(0)
    f.write("Hi ")

#Result - Hello WorldHi

##Read behavior (a+ me reading ka twist)
# ✔️ Correct way:
with open("test.txt", "a+") as f:
    f.seek(0)
    print(f.read())

### replace() function uses ---------
#input.txt file content----
# Hello World
# File se data read karo
with open("input.txt", "r") as f:
    text = f.read()

# Replace operation
new_text = text.replace("World", "Python")

# Wapas file me likho (overwrite)
with open("input.txt", "w") as f:
    f.write(new_text)

print("File updated successfully")

#Now output - Hello Python
#End of file input_output.py