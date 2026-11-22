students = ["Aman\n", "Priya\n", "Rohan\n", "Neha\n", "Kabir\n"]
with open("sample.txt", "w") as file:
    for name in students:
        file.write(name)