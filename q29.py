pos = int(input("Enter starting position: "))
with open("sample.txt", "r") as f:
    f.seek(pos)
    print(f.read())