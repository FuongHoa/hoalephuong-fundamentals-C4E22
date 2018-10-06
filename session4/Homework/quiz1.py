print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4 * (x + 3)?")
choices = {
    1: 35,
    2: 36,
    3: 40,
    4: 44,
}
for k,v in choices.items():
    print(k,v,sep =". ")

answer = int(input("Your choice: "))
ans = answer - 1
if ans == 3:
    print("Bingoooooooooooo")
else:
    print(":(")
