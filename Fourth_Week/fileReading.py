# f = open ('sample1.txt', "r")
# print(type(f), f)
# lines = f.readlines()
# print(type(lines))

# print(lines[5])
# for line in lines:
#     if line !=" ":
#         print(line)

with open ("sample1.txt") as my_file:
    print(my_file.read())
    
with open ("numma.txt", "w") as my_file1:
    my_file1.write("Hello World \n")
    my_file1.write("I hope you're doing well \n")

# with open("sample1.txt") as my_file:

# This line uses the with statement to open the file named sample1.txt in read mode ("r").
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
# my_file is the file object representing the opened file.
# print(my_file.read())

# my_file.read() reads the entire content of the file and returns it as a string.
# print() then outputs this string to the console.

# with open("numma.txt", "w") as my_file1:

# This line opens (or creates if it doesn't exist) a file named numma.txt in write mode ("w").
# my_file1 is the file object representing the opened file.
# In write mode, if the file already exists, its content is truncated (deleted) before writing new data.
# my_file1.write("Hello World \n")

# This writes the string "Hello World \n" to the file numma.txt.
# \n is a newline character, so the next write will be on a new line.
# my_file1.write("I hope you're doing well \n")

# This writes the string "I hope you're doing well \n" to the file numma.txt.