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


def test():
    # is_odd_number test

    assert is_odd_number('') == ''
    assert is_odd_number(5) is False
    assert is_odd_number(6) is True

    # five_prime_numbers test

    assert five_prime_numbers() == 28

    # sum_of_rows test

    assert sum_of_rows(4) == 1234
    assert sum_of_rows(5) == 12345
    assert sum_of_rows(9) == 123456789


test()
