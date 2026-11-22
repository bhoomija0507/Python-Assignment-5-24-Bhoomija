with open("sample.txt", "r") as f:
    print("Initial position:", f.tell())
    f.read(5)
    print("Position after reading 5 chars:", f.tell())