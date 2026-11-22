f = open("sample.txt", "r")
print("Is file closed?", f.closed)
f.close()
print("Is file closed after close()?", f.closed)