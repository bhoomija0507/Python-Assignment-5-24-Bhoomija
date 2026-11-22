import os

f = open("sample.txt", "r")
print("File Name:", f.name)
print("File Mode:", f.mode)
print("Is Closed:", f.closed)
f.close()

stats = os.stat("sample.txt")
print("File Size (bytes):", stats.st_size)