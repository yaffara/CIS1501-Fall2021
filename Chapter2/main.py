import math

print('happy tuesday')

hourly_pay_rate = 15.5
hours_worked = 40
total_pay = hours_worked * hourly_pay_rate
name = 'Eric'

speed_of_light_approximate = 3e8

print(speed_of_light_approximate, 'meters/second')
# value is the default
print('your pay this week', total_pay)

print("type(total_pay): ", type(total_pay))
print("id(total_pay): ", id(total_pay))


print('Pi to 5 decimal places: {:.5f}'.format(math.pi))

# exponential operator, x^y
print("3 to the 5th power is: ", 3**5)

# modulus is like divison, but gives the integer remainder
print("13 % 5 == ", 13 % 5 )

# PEMDAS - parentheses , exponents, multiplication, division, addition, subtraction
print(' 10 - 5 + 10')

print('what is 10 - 10 / 5 x 10 + 10')

print(hourly_pay_rate)
hourly_pay_rate = hourly_pay_rate + 1
print(hourly_pay_rate)
hourly_pay_rate += 1
print(hourly_pay_rate)

# can use an underscore for digit grouping
one_billion = 1_000_000_000

# // is for integer division
print( '5/2 as an integer result == ', 5 // 2, 'remainder ', 5 % 2 )

print('A', ord('A'))
print('69 as a character', chr(69))
print('82 as a character', chr(82))
print('73 as a character', chr(73))
print('67 as a character', chr(67))

print('Tab: \t - newline: \n - single quote \'')
print(r'Tab: \t - newline: \n - single quote \'')



your_number = int(input("enter a number 1-100: "))
result = your_number * 9
hundreds_place = result // 100
tens_place = result % 100 // 10
ones_place = result % 10

print("your number * 9 is: ", result)
print("the sum of the digits in that is: ", hundreds_place + tens_place + ones_place )


sum = 0

#sum = sum +
sum += int(input("enter a number: "))
sum += int(input("enter a number: "))
sum += int(input("enter a number: "))
sum += int(input("enter a number: "))
sum += int(input("enter a number: "))

print("Total total is: ", sum)
print("The average is: ", sum/5)


first_initial = ord(input("Please enter your first initial"))
middle_initial = ord(input("Please enter your middle initial"))
last_initial = ord(input("Please enter your last initial"))

number_of_letters_to_shift_by = int(input("How many letters should we shift by? "))

print(chr(first_initial), chr(middle_initial), chr(last_initial))

first_initial += number_of_letters_to_shift_by
middle_initial += number_of_letters_to_shift_by
last_initial += number_of_letters_to_shift_by

print(chr(first_initial), chr(middle_initial), chr(last_initial))