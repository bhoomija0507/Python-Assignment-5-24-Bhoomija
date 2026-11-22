target = input("Enter word to search: ")
with open("sample.txt", "r") as f:
    if target in f.read().split():
        print("Word exists in the file.")
    else:
        print("Word does not exist.")