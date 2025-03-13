from Assessment import Assessment
from DataReader import read_names
from random import choice, gauss
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
        n = choice(student_names)
    student_names.append(n)

students = []
for sn in student_names:
    classes=[]
    for subject in subjects:
        classes.append(choice(subject))
    name_split = sn.split()
    students.append(Student(name_split[0], name_split[1], classes))

classes = []
for subject in subjects:
    new_class = Clasz(subject)
    for i,assignment in enumerate(assignment_types):
        grade = -1
        while grade < 0 or grade > 100:
            grade = gauss(75,10)
        new_class.assessments.append(assignment+str(i+1))
    classes.append(new_class)

for student in students:
    pass
