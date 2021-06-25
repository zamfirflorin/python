import os 

directory = 'Python Directory'

parent_directory = 'C:/Users/fszamfi/Desktop/'

path = os.path.join(parent_directory, directory)

os.mkdir(path)

print("Directory created " % directory)
