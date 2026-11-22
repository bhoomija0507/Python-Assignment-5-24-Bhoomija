import os

# 1. Create and write
f = open("sample.txt", "w")
f.write("Temporary data for Q50.")
f.close()

# 2. Read and close
f = open("sample.txt", "r")
print("File content:", f.read())
f.close()

# 3. Delete
os.remove("sample.txt")
print("File deleted successfully.")