#列表
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("The first three items in the list are:")

for first in number[:3]:
    print(first)

print("Three items from the middle of the list are:")

for second in number[5:8]:
    print(second)

print("The last three items in the list are:")

for last in number[-3:]:
    print(last)


#元组
foods = ("hamberger", "chips", "fried chicken", "cola", "ice cream")

for food in foods:
    print(food)

try:
    foods[0] = "pie"
    if foods[0] == "pie":
        print("I like pie")
except TypeError:
    print("Tuples cannot be changed")

foods_change = ("pie", "noodles", "fried chicken", "cola", "ice cream")

for food1 in foods_change:
    print(food1)
