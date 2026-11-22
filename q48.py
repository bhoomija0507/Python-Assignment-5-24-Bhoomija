import os

filename = "sample.txt"
if os.path.exists(filename):
    print("File exists.")
    print("Size in bytes:", os.path.getsize(filename))
else:
    print("File does not exist.")