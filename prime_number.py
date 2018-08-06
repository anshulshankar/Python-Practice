n = int(input(''))


# checking whether a given no is prime or not
def prime_or_not(number):
    flag = 0
    for i in range(1, number + 1):
        if number % i == 0:
            flag += 1
    if flag == 2:
        return number


for item in range(2, n + 1):
    if prime_or_not(item) is not None:
        print(item, end=' ')
