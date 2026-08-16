information = [
    {"name": "Tom", "score": 100},
    {"name": "Mike", "score": 95},
    {"name": "Peter", "score": 95}
]

for person in information:
    print(person["name"] + "'s score is:" + str(person["score"]))

score_list = [student["score"] for student in information]
average = sum(score_list) / len(information)
print("The average is:", average)
