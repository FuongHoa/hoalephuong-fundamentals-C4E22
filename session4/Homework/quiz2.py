quiz = [{
    "stimulus": "Answer these following algebra questions: ",
    "question": "Question 1: If x = 8, then what is the value of 4 * (x + 3)?",
    "choices": ["1. 35", "2. 36", "3. 40", "4. 44"],
    "right_choice": 4,
},
{
    "stimulus": "Question 2: Estimate the answer(Exact calculation not needed):",
    "question" :"Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the average score that Jack got?",
    "choices": ["1. About 55", "2. About 65", "3. About 75", "4. About 85"],
    "right_choice": 2,
}]

total = 0
l = len(quiz)
for d in range(l):
    print(quiz[d]["stimulus"])
    print(quiz[d]["question"])
    print(*quiz[d]["choices"], sep = "\n")
    ans = int(input("Your choice: "))
    if ans == quiz[d]["right_choice"]:
        print("Bingoooooooo!")
        total += 1
    else:
        print(":(")

print("You correctly got ", total, "out of 2 questions")