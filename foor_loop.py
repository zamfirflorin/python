temp = [9, 8.8, 2, 4.5]

names = ['hello', 'temp', 'first']

student_grades = {"marry": 7, "cool": 8, "test": 9}

for i in temp:
    print(round(i))

for i in 'hello':
    print(i)

for i in names:
    print(i)
    print("%s is printed" % (i))

for i in student_grades.items():
    print(i)

for i in student_grades.keys():
    print(i)

for i in student_grades.values():
    print(i)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

for value in phone_numbers.values():
    print(value.replace('+', '00'))