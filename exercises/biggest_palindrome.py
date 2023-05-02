# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
def check_polindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


list_ = []
dict_ = {99: 10, 999: 100, 9999: 1000}
limit = 999
end = dict_[limit]
iteration = 0
a = limit
while a - end:
    b = limit - iteration
    while b - end:
        result = a * b
        # print(a, b, result)
        if check_polindrome(result):
            list_.append((result, a, b))
        b -= 1
    a -= 1
    iteration += 1

# print(list_)
biggest = 0
first_number = 0
second_number = 0

for tuple_ in list_:
    if tuple_[0] > biggest:
        biggest = tuple_[0]
        first_number = tuple_[1]
        second_number = tuple_[2]

print(f'The biggest palindrome is: {biggest} and it is result of multiplying {first_number} by {second_number}')