# Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.




print("Writing the contents to file: ")
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first note.\n")
    file.write("Python file handling is simple.\n")
    file.write("End of file.\n")
print("Writing completed...\n")


print("Reading the contents of file: ")
with open("notes.txt", "r") as file1:
    content = file1.read()
    print(content)
