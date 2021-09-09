import math

# this is a comment and is ignored by the python interpreter

# floats are numeric values with decimal places
# ints are numeric whole numbers - integers
hourly_pay_rate = float(input('Enter your hourly pay rate: '))
hours_worked_this_week = float(input('Enter your hours worked this week: '))
pay_this_week = hourly_pay_rate * hours_worked_this_week
print('your pay this week:', pay_this_week)

# int - Integer - whole numbers
credits_this_semester = int(input('how many credits are you taking this semester?'))
total_credits_required_for_degree = int(input('how many credits do you need to get your degree?'))
credits_completed = int(input('How many credits do you already have completed?'))

credits_remaining = total_credits_required_for_degree - credits_completed - credits_this_semester

print('after this semester, you will need', credits_remaining, 'credits to complete your degree')

number_of_semesters_to_go = credits_remaining / credits_this_semester

# math.ceil( some_number_here ) - will round up to next integer
print('if you take', credits_this_semester, 'credits',
      'each semester, you have', math.ceil(number_of_semesters_to_go), 'semesters left until you graduate')


name = input('what is your name?')
print('hi', name)

