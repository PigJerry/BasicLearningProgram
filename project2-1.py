loaded_students = []

with open("students.txt", "r", encoding = "utf-8") as f:
    for line in f:
        name, score = line.strip().split(",")
        loaded_students.append({"name": name,"score": int(score)})

print("The data loaded form file:", loaded_students)

total = sum(s["score"] for s in loaded_students)
print("The average is still:", total / len(loaded_students))

