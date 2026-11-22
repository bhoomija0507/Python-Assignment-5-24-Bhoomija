upper = lower = 0
with open("sample.txt", "r") as f:
    for ch in f.read():
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
print(f"Uppercase: {upper}, Lowercase: {lower}")