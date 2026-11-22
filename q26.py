with open("sample.txt", "a+") as f:
    f.write("\nAppended in a+ mode")
    f.seek(0)
    print(f.read())