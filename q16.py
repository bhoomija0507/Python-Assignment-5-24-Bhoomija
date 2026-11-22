# Write mode overwrites existing content
with open("sample.txt", "w") as f:
    f.write("First line.\n")

# Append mode adds to existing content without deleting it
with open("sample.txt", "a") as f:
    f.write("Second line appended.\n")

with open("sample.txt", "r") as f:
    print(f.read())