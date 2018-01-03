"""
Data type to store more than one value in on variable name in terms of key value pair.
Dictionary items are in brackets {} in key:value pairs,  separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced,  no indexing -> Mapping
"""

car = {'make':'bmw','model':'550i','year':2016}
d = {}
print(car)
print("*"*20)

make = (car['make'])
model = (car['model'])
year = (car['year'])

print("Make: "+ (car['make']))
print("Model: "+ (car['model']))
print("Year: "+ str((car['year'])))
print("*"*20)

print("Make: "+ make)
print("Model: "+ model)
print("Year: "+ str(year))
print("*"*20)

d['one'] = 1
d['two'] = 2
d['three'] = 3
d['four'] = 4


eight = 8

sum = d['two'] + eight
print(str((d['two']))+ " + " + str(eight) + " = " + (str(sum)))
print(d)
d['two'] = d['two'] + eight
print (d)