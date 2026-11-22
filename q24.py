with open("sample.txt", "r+") as f:
    print("Before:", f.read())
    f.write("\nAdded via r+ mode.")