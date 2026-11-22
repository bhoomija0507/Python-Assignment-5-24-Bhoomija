lines = ["Line 1: Python\n", "Line 2: File Handling\n", "Line 3: Assignment 5\n"]
with open("welcome.txt", "w") as file:
    file.writelines(lines)