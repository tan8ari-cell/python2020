def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean


a = [8.8, 9.1, 9.5]
b = {"Marry": 9.1, "Sam": 8.8, "John": 9.5}  # dict
print(mean(a))
