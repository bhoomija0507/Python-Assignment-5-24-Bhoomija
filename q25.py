with open("sample.txt", "w+") as f:
    f.write("Hello w+ mode")
    f.seek(0)  # Move pointer back to start to read
    print(f.read())