# З чисел від 1 до 30 знайти ті, які без остачі діляться на 3 та записати їх у вигляді масиву. І вивести цей масив на
# екран.
my_list = list()
for i in range(1, 31):
    if i % 3 == 0:
        my_list.append(i)
print(my_list)
del my_list

# Є числа від 1 до 100. Якщо число ділиться без остачі на 3 - вивести на екран Tik, якщо на 5 - Tak,
# якщо і на 3 і на 5 - TikTak.
my_list = list()
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, '---> TikTak')
    elif i % 3 == 0:
        print(i, '---> Tik')
    elif i % 5 == 0:
        print(i, '---> Tak')
