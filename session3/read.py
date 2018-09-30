items = ["BTS", "LOL", "Fornite", "PUBG"]
print(*items, sep="\n")
i = int(input("Which element do you want to read? "))
print(items[i-1])