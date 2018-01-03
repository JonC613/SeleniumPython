"""
Nested Dictionary
d = {'k1':{'nestk1':'nestvalue1','nestk2':'nestvalue2'}}
d['k1]['nestk1']
"""

cars = {'bmw': {'model':'550i','year':2016}, 'honda': {'model':'Accord','year':2017} }
print (cars)
print("*"*20)
bmw_year = cars['bmw']['year']
print ("BMW")
print ("Year: " + str((bmw_year)))
print ("Model: " + str(cars['bmw']['model']))