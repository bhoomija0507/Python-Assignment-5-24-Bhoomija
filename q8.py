with open("sample.txt", "r") as file:
    words = file.read().split()
    print("Total words:", len(words))