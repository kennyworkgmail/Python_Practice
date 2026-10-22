#串列初始化
course_names = [
    "Python",
    "FastAPI",
    "MySQL"
]
tmp = []
print(course_names[0])
print(course_names[2])
# 超出範圍的位址
# print(course_names[3])

mystr = "Ⅰ Love Python"
print(mystr[0])

for course_name in course_names:
    print(course_name)

courses = [
    ["Python", 4],
    ["Java", 6],
    ["LLM", 4],
    ["DB", 2]
]

print(courses[0])
print(courses[0][0])
print(courses[0][1])

newcourse  = "AI Security"
newcourses = ["PA", "Cymulate"]
courses.append(newcourse)
print(courses)
courses.extend(newcourse)
print(courses)
courses.extend(newcourses)
print(courses)