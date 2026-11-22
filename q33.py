digits = special = 0
with open("sample.txt", "r") as f:
    for ch in f.read():
        if ch.isdigit():
            digits += 1
        elif not ch.isalpha() and not ch.isspace():
            special += 1
print(f"Digits: {digits}, Special characters: {special}")