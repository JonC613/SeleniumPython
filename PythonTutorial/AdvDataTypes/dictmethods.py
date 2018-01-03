"""
Dictionary Methods
"""

car = {'make':'bmw','model':'550i','year':2016}
cars = {'bmw': {'model':'550i','year':2016}, 'honda': {'model':'Accord','year':2017} }

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
print(cars.items())

car_copy = car.copy()
print (car_copy)

#car.clear()

print(car.pop('model'))
print(car)