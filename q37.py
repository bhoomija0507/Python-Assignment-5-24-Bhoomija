char = input("Enter starting character: ")
with open("sample.txt", "r") as f:
    for line in f:
        if line.startswith(char):
            print(line, end="")