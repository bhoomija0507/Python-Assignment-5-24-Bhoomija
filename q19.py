num = int(input("Enter a number: "))
with open("sample.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{num} x {i} = {num * i}\n")