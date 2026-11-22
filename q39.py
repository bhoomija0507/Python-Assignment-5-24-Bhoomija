with open("sample.txt", "r") as src, open("reversed_sample.txt", "w") as dest:
    content = src.read()
    dest.write(content[::-1])