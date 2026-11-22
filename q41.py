import os

if os.path.isfile("sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")