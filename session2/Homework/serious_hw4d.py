n = int(input("Enter the stars number: "))

for _ in range(int(n/2)):
    print("x", end="")
    print(" ", end="")
    print("*", end="")
    print(" ", end="")
print("x")