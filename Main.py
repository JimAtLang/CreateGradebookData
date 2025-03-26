from types import new_class

from Assessment import Assessment
from DataReader import read_names
from random import choice, gauss, randint
from Student import Student
from Clasz import Clasz

names = read_names()

math_classes = ["Algebra 1", "Geometry", "Algebra 2", "Pre-Calculus", "Calculus"]
science_classes = ["Biology","Earth Science", "Chemistry","Physics"]
history_classes = ["Social Studies", "American History", "World History"]
electives = ["Art", "Music", "Coding", "Wood shop"]
ela_classes = ["ELA 1", "ELA 2", "American Literature", "World Literature"]
language_classes = ["Spanish 1", "Spanish 2", "French 1", "French 2", "Sign language"]
assignment_types = {"HW":10,"Project":2,"Quiz":4,"Test":2,"Final":1}
subjects = [math_classes,science_classes,history_classes,electives,language_classes]
student_count = 500


student_names = []
for i in range(student_count):
    n = ""
    while not n or n in student_names:
        n = choice(names)
    student_names.append(n)

students = []
for sn in student_names:
    classes=[]
    for subject in subjects:
        classes.append(choice(subject))
    name_split = sn.split()
    students.append(Student(name_split[0], name_split[1], classes))

classes = []
new_class = None
for subject in subjects:
    for option in subject:
        new_class = Clasz(option)
        for assignment in assignment_types:
            for i in range(assignment_types[assignment]):
                new_class.assessments.append(assignment+str(i+1))
        classes.append(new_class)

for student in students:
    for clasz in student.class_names:
        for clasy in classes:
            if clasy.name == clasz:
                clasy.students.append(student)
                break

for clasz in classes:
    print(clasz.name)
    f = open("data/"+clasz.name, "w")
    f.write("Name,")
    for i,assessment in enumerate(clasz.assessments):
        f.write(assessment)
        if i<len(clasz.assessments)-1:
            f.write(",")
    f.write("\n")
    for student in clasz.students:
        f.write(student.first_name + " " + student.last_name + ",")
        ability = -1
        while ability < 0 or ability > 100:
            ability = gauss(75, 10)
        consistency = -1
        while consistency < 0 or consistency > 100:
            consistency = gauss(95, 5)
        for i,assessment in enumerate(clasz.assessments):
            if randint(0,100) > consistency:
                f.write("NTI")
            elif randint(0,100) < 5:
                f.write("EXC")
            else:
                grade = -1
                while grade < 0 or grade > 100:
                    grade = round(gauss(ability, 10))
                f.write(str(grade))
            if i < len(clasz.assessments) - 1:
                f.write(",")
        f.write("\n")
    f.close()

