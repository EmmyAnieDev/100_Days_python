#                            LIST
import random

names = ['David', 'Derek', 'Daniel', 'Tammy', 'Sharon', 'Telma']
print(names)

names.append('Joy')       # add tot the list in this case, the end of the list
names.extend(['Angela', 'Phil'])     # add two or more items
print(names)
print(len(names) + 1)

names[4] = 'Terry'         # change the name of a particular index
print(names)

names.pop()               # remove the last data in the list
print(names)

names.remove('Daniel')       # remove using the data
print(names)


print(names[2])         # print the name with index 2
print(names[-1])       # print the name of the last index
print(len(names) + 1)     # print length of the list



#            Randomization
print(random.choice(names))



#                           Nested List
foods = [['Apple', 'Orange', 'Banana'], ['Onions', 'Tomatoes', 'Pepper'], ['Salt', 'Sugar', 'Water']]
print(foods[2])


foods[2].append('Curry')
print(foods[2])
print(foods)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
print(fruits[-4])