text = input("Enter text to save: ")
with open("welcome.txt", "w") as file:
    file.write(text)