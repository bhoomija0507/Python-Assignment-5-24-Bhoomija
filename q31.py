vowels = "aeiouAEIOU"
count = 0
with open("sample.txt", "r") as f:
    for ch in f.read():
        if ch in vowels:
            count += 1
print("Total vowels:", count)