items = ["Buch", "Obst", "Kleidung"]
print(*items, sep = ", ")
i = input("Enter the element that you want to delete: ")
if i.isdigit():
    position = int(i)
    items.pop(position - 1)
else:
    items.remove(i)

print(*items, sep = ", ")
