with open("sample.txt", "r") as f:
    f.seek(6)  # Move pointer to 6th byte
    print("Moved pointer to:", f.tell())