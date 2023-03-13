from math import sqrt


def is_odd_number(num):
    if type(num) is int:
        return [False, True][num % 2 == 0]
    return ""


def five_prime_numbers():
    prime_numbers = []
    num = 1
    while len(prime_numbers) < 5:
        if num > 1:
            prime_flag = True
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_numbers.append(num)
        num += 1
    return sum(prime_numbers)


def sum_of_rows(n: int):
    if n <= 1:
        return 1
    return int("1" * n) + sum_of_rows(n-1)




