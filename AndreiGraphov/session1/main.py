#task1

def findLen(result):
    counter = 0
    for i in result:
        counter +=1
    return counter
result = "Python"
print("Task 1 result:")
print(findLen(result))
print()

#task2

from collections import Counter
test_str = "Oh, it is python"
test_str.lower()
res = Counter(test_str)
print("Task 2 result:")
print("Count of all characters in _ is :\n " + str(res))
print()

#task3
list = ['red', 'white', 'black', 'red', 'green', 'black']
set = set(list)
set = sorted(set)
print("Task 3 result:")
print(set)
print()

#task4
divisors = []
number = 123
for i in range(1, number + 1):
  if number % i == 0:
    divisors.append(i)
print("Task 4 result:")
print(divisors)
print()

#task5
myDict = {
    5: "cafe",
    7: "bread",
    3: "office",
    4: "ball",
    1: "stand"
}
print("Task 5 result:")
for key in sorted(myDict):
    print(key, myDict[key])
print()

#task6
list6 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s = set()
print("Task 6 result:")
for dic in list6:
   for val in dic.values():
      s.add(val)
print(s)
print()


#task7
tuple = (1, 2, 3, 4)
a = int("".join(str(x) for x in tuple))
print("Task 7 result:")
print(a)
print()

#task8
a = 2
b = 4
c = 3
d = 7
END = 1
inc = 0
print("Task 8 result:")
for z in range(c, d + END):
    print("    " + str(c+inc), end="")
    inc+=1
print()
inc2=0
for i in range(a, b + END):
    print(a+inc2, end="")
    inc2 += 1
    for g in range (c, d + END):
        print(repr(i*g).rjust(4), end=" ")
    print()
