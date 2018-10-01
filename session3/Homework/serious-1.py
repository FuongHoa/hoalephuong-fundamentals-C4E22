print("Welcome to our shop, what do you want? ")
items = ["T-Shirt", "Sweater"]

#Read
print("Our items: ", end="")
print(*items, sep = ", ")

#Create
new_item1 = str(input("Enter new item? "))
items.append(new_item1)
print("Our items: ", end="")
print(*items, sep =", ")

#Update
items[1] = str(input("New item? "))
print("Our items: ", end="")
print(*items, sep = ", ")

#Delete
items.pop(2)
print("Our items: ", end="")
print(*items, sep =", ")
