items = ["Buch", "Obst", "Kleidung"]
print(*items, sep = ", ")
i = int(input("Enter the location where you want to replace: "))
print(items[i-1])
# print(items[i-1], "=", n)
items[i-1] = str(input("Enter the content that you want to replace: "))
print(*items, sep = ", ")