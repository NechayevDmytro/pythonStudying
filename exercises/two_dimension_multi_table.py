result_size = 1


def build_multi_table(a, b):
    global result_size
    result_size = len(list(str(a * b))) + 1
    i = 1
    while i <= a:
        j = 1
        while j <= b:
            print(format_result(i * j), end='')
            j += 1
        print()
        i += 1


def format_result(number):
    return ' ' * (result_size - len(str(number))) + str(number)


answer_1 = input('Would you like a square multiplication table (y/n): ')

if answer_1 == 'y':
    answer_for_square = int(input('Enter the size: '))
    build_multi_table(answer_for_square, answer_for_square)
else:
    answer_2 = int(input('Enter height: '))
    answer_3 = int(input('Enter weight: '))
    build_multi_table(answer_2, answer_3)
