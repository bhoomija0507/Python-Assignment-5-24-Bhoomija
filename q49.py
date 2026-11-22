import os

os.rename("sample.txt", "renamed_sample.txt")
with open("renamed_sample.txt", "r") as f:
    print(f.read())