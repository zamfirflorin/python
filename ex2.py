#student_grades = [5, 4, 5]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
print(mysum)

temp = [1, 4, 5, 4, 6, 1, 2,]

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean