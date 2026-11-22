target = input("Enter word to count: ")
with open("sample.txt", "r") as f:
    words = f.read().split()
    print(f"Occurrences of '{target}':", words.count(target))