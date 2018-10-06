person_list = [
    {   #p1
        "name": "Hoa",
        "age": 18,
    },
    {    #p2                      #JSON
        "name": "An",
        "age": 19
    }
]

# person_list.append(p1)
# person_list.append(p2)

#Read
print(person_list)
#print(person_list[1])

#Update
#person_list[0] = {
#   "name": "Hund",
#   "age": 1,
#}

#print(person_list)

#Del
# person_list.pop(0)
# print(person_list)
# p = person_list[0]
# print(p["age"])
# print(person_list[0]["age"])
for p in person_list:
    print(p["age"])
