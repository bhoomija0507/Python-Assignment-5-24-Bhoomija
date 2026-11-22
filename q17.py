with open("sample.txt", "r") as src, open("welcome.txt", "w") as dest:
    dest.write(src.read())