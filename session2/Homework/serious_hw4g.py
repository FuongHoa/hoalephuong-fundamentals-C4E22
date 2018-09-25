n = int(input("Enter the column number: "))
m = int(input("Enter the row number: "))

for _ in range(m):
    for _ in range(n):
        print("*", end="")
        print(" ", end="")
    print(" ")