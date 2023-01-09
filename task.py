import json

file = open('students.json', 'r', encoding='utf-8')
data = json.load(file)
file.close()

for i in data['Students']:
    print(f"{i['FirstName']} {i['LastName']} ({i['Grade']})")

#Risinājums 1

grade_sum = 0
for i in data['Students']:
    grade_sum += int(i['Grade'])

average_grade = grade_sum / len(data['Students'])
print(f"Average grade is {average_grade}")

#Risinājums 2

grade_list = []
for i in data['Students']:
    grade_list.append(int(i['Grade']))
print(f"Average grade is {sum(grade_list)/len(grade_list)}")

female_grade_list = []
male_grade_list = []
other_grade_list = []
for i in data['Students']:
    if i['Gender'] == 'Female':
        female_grade_list.append(int(i['Grade']))
    elif i['Gender'] == 'Male':
        male_grade_list.append(int(i['Grade']))
    else:
        other_grade_list.aapend(int(i['Grade']))

print(f"Female count: {len(female_grade_list)}")
print(f"Female grade average: {sum(female_grade_list) / len(female_grade_list)}")
print(f"Male count: {len(male_grade_list)}")
print(f"Male grade average: {sum(male_grade_list) / len(male_grade_list)}")

majors_list = []

for i in data['Students']:
    if i['Major'] not in majors_list:
        majors_list.append(i['Major'])
print(majors_list)       
