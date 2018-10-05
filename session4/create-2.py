# key = input("Enter the actress'name: ")
# value = input("Enter the actress's age: ")

# film = {
#     "name": "Stranger things",
#     "seasons": 2,
# }
# film[key] = value

# print(film)

pokemon = {
    "name": "pikachu",
    "owner": "Ash",
}

text = input("Enter new items: ")
pair = text.split(",")
key = pair[0]
value = pair[1]

pokemon[key] = value
print(pokemon)