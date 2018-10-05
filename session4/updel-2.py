person = {
    "name": "Hoa",
    "age": 18,
}

print(person)

ask = input("Update (u) or delete (d)? ")

if ask == "d":
    d = input("Which key to delete? ")
    if d in person:
        del person[d]
        print(person)
    else:
        print("Not found!")
elif ask == "u":
    key = input("Enter key: ")
    if key in person:
        new_value = input("Enter new value: ")
        person[key] = new_value
        print(person)
    else:
        print("Not found!")