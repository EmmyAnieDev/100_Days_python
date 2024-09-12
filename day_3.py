##            IF - ELSE STATEMENT


# print('Welcome to the rollercoaster!')
# height = int(input('what is your height?: '))
#
# if height >= 120:
#     print('You can ride the rollercoaster')
# else:
#     print('Sorry you have to grow taller!')



# #              MODULO OPERATOR.    IT CHECK THE REMAINDER OF A NUMBER
#
# number_to_check = int(input('Number to check: '))
#
# if number_to_check % 2 == 0:
#     print('Number is even')
# else:
#     print('Number is odd')



# #                    NESTED IF AND ELIF STATEMENT
# print('Welcome to the rollercoaster!')
# height = int(input('what is your height?: '))
# age = int(input('what is your age?: '))
#
# if height >= 120:
#     if age >= 18:
#         print('please pay $7.99')
#     elif age >= 13:
#         print('please pay $2.99')
#     else:
#         print('you are a bit younger')
# else:
#     print('Sorry you have to grow taller!')



# #                   PIZZA PRACTICE
# print('Welcome to python pizza Deliveries!')
# size = input('What size of pizza do you want? S, M or L: ')
# pepperoni = input('Do you want Pepperoni on your pizza? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
#
#
#
# price = 0
# pepperoni_amount = 2
# extra_cheese_amount = 1


# if size == 'L':
#     price = 25
#     if pepperoni == 'Y':
#         price += pepperoni_amount
#     if extra_cheese == 'Y':
#         price += extra_cheese_amount
# elif size == 'M':
#     price = 20
#     if pepperoni == 'Y':
#         price += pepperoni_amount
#     if extra_cheese == 'Y':
#         price += extra_cheese_amount
# elif size == 'S':
#     price = 15
#     if pepperoni == 'Y':
#         price += pepperoni_amount
#     if extra_cheese == 'Y':
#         price += extra_cheese_amount
# else:
#     print('You typed a wrong keyword!')
#
# total_price = price
#
#
# print(f'this is your total price ${total_price}')



#                LOGICAL OPERATORS
print('Welcome to Python Pizza Deliveries!')
size = input('What size of pizza do you want? S, M or L: ').upper()
pepperoni = input('Do you want Pepperoni on your pizza? Y or N: ').upper()
extra_cheese = input('Do you want extra cheese? Y or N: ').upper()

price = 0

# Set the price based on the size
if size == 'S':
    price = 15
elif size == 'M':
    price = 20
elif size == 'L':
    price = 25
else:
    print("Invalid size. Please choose S, M, or L.")

# Add price for pepperoni (with logical operators)
if pepperoni == 'Y' and size == 'S':
    price += 2
elif pepperoni == 'Y' and (size == 'M' or size == 'L'):
    price += 3

# Add price for extra cheese (logical operator)
if extra_cheese == 'Y':
    price += 1

print(f'Your final bill is: ${price}')