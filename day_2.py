#                                         DATA TYPES


# # Subscripting
# print('Hello'[0])
# print('Hello'[-2])
#
# # String
# print('1234' + '5678')
#
# #integer  ===>    Whole number
# print(1234 + 5678)
#
# # Float   ===>   Number with decimal point
# print(12.6 + 10)
#
# # Boolean     ===> True and False
# print(4+4 == 8)
# print(10 - 6 == 2)

# name = 'Abel'
# print(f'name is a {type(name)} type')




# #             MATHEMATICAL OPERATION
#
#
# print(7 + 9)
# print(10 - 3)
# print(3 * 2)
# print(3 ** 2)  # raise to the power of 2
# print(10 / 6)
# print(10 // 6)  # print just the whole number(s) before decimal point.
#
#
# # PEMDAS # Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction
# print(20.0 - 3 / 3 - 3 * 2 + 10 - (4 ** 2))



# #            Round Function
# weight = 68
# height = 1.85
#
# bmi = weight / height ** 2
#
# print(bmi)
# print(round(bmi))       # approximate and round to whole number.
# print(round(bmi, 2))  # approximate and round to 2 decimal places.




# #        Assignment Operator
#
# score = 0
# print(score)
# print('')
# score += 1
# print(score)



#        TEST

print('Welcome to the tip calculator!')
total_bill = input('What was the total bill?: ')
tip = input('How much would you like to tip? 10, 12, or 15: ')
percent = int(tip) / 100
bill_including_tip = float(total_bill) + (float(total_bill) * percent)
split_bill = input('How many people to split the bill?: ')
each_bill = bill_including_tip / int(split_bill)
rounded_bill = round(each_bill, 2)
print(f'Each person should pay: ${rounded_bill}')