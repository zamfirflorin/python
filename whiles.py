

#  while a > 10: 
#     print(a)
#     a-=1 

# while True:
#     username = input("Enter username: ")
#     if username == 'pypy':
#         break
#     else:
#         continue

temps = [22.1, 234, 340, 230]
new_temps = []
another_temps = [temps / 10 for  temp in temps]

for temp in temps: 
    new_temps.append(temp / 10)

print(new_temps)
print(another_temps)