import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("File deleted.")
else:
    print("File not found.")