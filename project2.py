students = [
    {"name": "Tom", "score": 100},
    {"name": "Mike", "score": 95},
    {"name": "Peter", "score": 95}
]

with open("students.txt", "w", encoding = "utf-8") as f:

    for s in students:

        f.write(s["name"] + "," + str(s["score"]) + "\n")

print("Data save successfully, please check students.txt in your folder")
