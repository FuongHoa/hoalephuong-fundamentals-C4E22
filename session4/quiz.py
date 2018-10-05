print("Round 1: Today C4E22 has a lot of boys.")
print("Which one is the most handsome? ")
choices = [{1: "Quan", 2: "An", 3: "Both", 4: "None"}]
print(choices)
answer = int(input("Choose the correct answer: "))
r = answer - 1
if r == 2:
    print("Correct!!!")
else:
     print("Wrong :(")
