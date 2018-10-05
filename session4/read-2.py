pokemon = {
    "name": "pikachu",
    "owner": "Ash",
}

key = input("Enter the information that you want to know: ")

# if key == "name":
    # print(pokemon["name"])
# elif key == "owner":
    # print(pokemon["owner"])
# else:
    # print("Error!")

if key in pokemon:
    value = pokemon[key]
    print(value) 
else: 
    print("Error!")