def mean(value):
    if type(value) == dict: 
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

list = [1, 4, 5, 4, 2, 6, 9]

print(mean([1, 4, 5, 4, 2, 6, 9]))

print(type(mean), type(len))

def mean2(value):
    if isinstance(value, dict):
        mean = sum(values.values()) / len(value)
    else: 
        mean = sum(value) / len(value)
    
    return mean

print(mean2(list))