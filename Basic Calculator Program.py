"""
Create a simple calculator in python to using two numbers.
This is simple calculator program with basic functionality, here user will enter operator
and two numbers for calculations.
"""

print('\nChoose one of following operator for calculation:')

print('************************')
print('+ : for addition')
print('- : for subtraction')
print('/ : for divison')
print('* : for multiplication')
print('************************')

choose_operator = input('Enter operator: ')
number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))

if choose_operator == "+":
    print('Output: {} {} {} ='.format(number_1, choose_operator, number_2), number_1 + number_2)
elif choose_operator == "-":
    print('Output: {} {} {} ='.format(number_1, choose_operator, number_2), number_1 - number_2)
elif choose_operator == "*":
    print('Output: {} {} {} ='.format(number_1, choose_operator, number_2), number_1 * number_2)
elif choose_operator == "/":
    print('Output: {} {} {} ='.format(number_1, choose_operator, number_2), number_1 / number_2)
else:
    print('Something went wrong, try again with correct input.')



