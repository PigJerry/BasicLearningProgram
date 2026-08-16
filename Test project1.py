students = ["Peter", "Tom", "Andy"]

for name in students:
    print(name + "Class begin!")

students.append("Jerry")
print("Now there are:", students)

print("We have", len(students), "students at all")



person = {
    "name": "Jerry",
    "age": 18,
    "city": "Guiyang"
}

print(person["name"] + "live in" + person["city"])

person["age"] = 19
print("He will be", person["age"], "years old")

for key, value in person.items():
    print(key + ":" + str(value))
