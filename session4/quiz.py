quiz = {
    "stimulus": "Round 1: Today C4E22 has a lot of boys.",
    "question": "Which one is the most handsome? ",
    "choices": ["1. Quan", "2. An", "3. Both", "4. None"],
    "right_choice": 3,
    }

print(quiz["stimulus"])
print(quiz["question"])
print(*quiz["choices"], sep="\n")
answer = int(input("Your choice: "))

if answer == quiz["right_choice"]:
    print("Correct!!!")
else:
     print("Wrong :(")
