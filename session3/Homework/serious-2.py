#2.1
sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hoa and here is my sheeps' sizes: ")
print(sizes)

#2.2
print("The size of my biggest sheep is: ", end="")
print(max(sizes), end="")
print(". Let's shear it")

#2.3
index = sizes.index(max(sizes))
sizes[index] = 8
print("After shearing, here is my flock:")
print(sizes)

#2.4
l = len(sizes)
for i in range(l):
    sizes[i] += 50
print("Afer a month, here is my flock:")
print(sizes)

sizes = [5, 7, 300, 90, 24, 50, 75]
#2.5
n = int(input("Enter the number of month: "))
for i in range(n):
    i += 1
    print("MONTH", i)
    print("One month has passed, now here is my flock:")
    for i in range(l):
        sizes[i] += 50
    print(sizes)
    print("Now my biggest sheep is", max(sizes),". Let's shear it")
    index = sizes.index(max(sizes))
    sizes[index] = 8
    print("After shearing, here is my flock:")
    print(sizes)

#2.6
s = sum(sizes)
print("my flock has size in total:", s)
money = s * 2
print("I would get 1010 * 2$ = ",money,"$")