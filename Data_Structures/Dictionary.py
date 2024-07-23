d = {}

d[1] = "yes"
d['1'] = "no"

print(d[1])
print(d["1"])

d[2] = 9000

print(d[2])

class my_class:
    def __init__(self):
        self.data = "data"

instance = my_class()

# Adding a object to the dict 
d['object'] = instance
print(d['object'].data)

print(d)

print(' - ')

# keys() return a list of the keys
print(d.keys())

# items() return a list of tuples of the key/value pairs
print(d.items())

print(' - ')

# Iterating over the keys
for key in d.keys():
    print(f"key = {key}")

print(' - ')

#Iterating over the key/value pairs
for key,value in d.items():
    print(f"key = {key}, value = {value}")