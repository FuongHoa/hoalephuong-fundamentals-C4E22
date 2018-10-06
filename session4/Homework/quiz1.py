print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4 * (x + 3)?")
quiz = {
    "choices": ["1. 35", "2. 36", "3. 40", "4. 44"],
    "right_choice": 4,
}   
print(*quiz["choices"], sep ="\n")

answer = int(input("Your choice: "))

if answer == quiz["right_choice"]:
    print("Bingoooooooooooo")
else:
    print(":(")
