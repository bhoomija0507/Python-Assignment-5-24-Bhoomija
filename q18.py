name = input("Enter Name: ")
roll = input("Enter Roll No: ")
marks = input("Enter Marks: ")

with open("welcome.txt", "w") as file:
    file.write(f"Name: {name}\nRoll No: {roll}\nMarks: {marks}\n")