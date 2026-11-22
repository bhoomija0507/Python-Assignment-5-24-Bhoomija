with open("sample.txt", "r") as src, open("upper_sample.txt", "w") as dest:
    dest.write(src.read().upper())