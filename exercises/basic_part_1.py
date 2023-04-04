# https://www.w3resource.com/python-exercises/python-basic-exercises.php
import calendar
import math
import platform
from datetime import datetime
from calendar import Calendar
from calendar import TextCalendar


# 1. Write a Python program to print the following string in a specific format
def exercise_1():
    print('1)')
    print('Twinkle, twinkle, little star,')
    print('\tHow I wonder what you are!')
    print('\t\tUp above the world so high,')
    print('\t\tLike a diamond in the sky.')
    print('\tTwinkle, twinkle, little star,')
    print('How I wonder what you are')


# 2. Write a Python program to find out what version of Python you are using.
def exercise_2():
    print('2)', platform.python_version())


# 3. Write a Python program to display the current date and time.
def exercise_3():
    now = datetime.now()
    print('3)', 'Current date and time:', end=' ')
    print(now.strftime('%d-%m-%Y %H:%M:%S'))


# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
def exercise_4():
    radius = input('4) Enter radius, please: ')
    square = math.pi * (float(radius) ** 2)
    print('Square is: ', '{:.2f}'.format(square))


# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order
# with a space between them.
def exercise_5():
    first_name = input('5) Enter your first name, please: ')
    last_name = input('Enter your last name, please: ')
    print('Hello,', last_name, first_name)


# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple of those numbers.
def exercise_6():
    a = input('Enter first number: ')
    b = input('Enter second number: ')
    c = input('Enter third number: ')
    d = input('Enter fourth number: ')
    my_list = list((a, b, c, d))
    my_tuple = tuple(my_list)
    print('As list:', my_list)
    print('As tuple', my_tuple)


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
def exercise_7(file_name):
    print('7)', file_name.split('.')[1])


# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
def exercise_8(color_list):
    print('8)', color_list[0], color_list[1])


# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 22, 2014). Sample Output : The examination will start from : 11 / 22 / 2014
def exercise_9(exam_st_date):
    month = exam_st_date[0]
    day = exam_st_date[1]
    year = exam_st_date[2]
    formatted_date = datetime(year, month, day).strftime("%m / %d / %Y")
    print(formatted_date)


# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def exercise_10(number):
    once = str(number)
    double = str(number) * 2
    triple = str(number) * 3
    print(int(once) + int(double) + int(triple))


# 12. Write a Python program that prints the calendar for a given month and year.
def exercise_12(year, month):
    it = Calendar().monthdayscalendar(year, month)
    m = calendar.month_name[month]
    print('    ', m, year)
    for week in it:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                formatted_day = " " + str(day) if len(str(day)) == 1 else str(day)
                print(formatted_day, end=" ")
        print()


# 12+. Write a Python program that prints the calendar for a given year.
def exercise_12_2(year):
    year = TextCalendar().formatyear(year)
    print(year)


# 14. Write a Python program to calculate the number of days between two dates.
def exercise_14(from_date, to_date):
    date_1 = datetime(from_date[0], from_date[1], from_date[2])
    date_2 = datetime(to_date[0], to_date[1], to_date[2])
    delta = date_1.__sub__(date_2).days
    day_word = 'day.' if abs(delta) <= 1 else 'days.'
    print(f'The difference is {abs(delta)} {day_word}')


exercise_14((2014, 7, 2), (2014, 7, 10))
