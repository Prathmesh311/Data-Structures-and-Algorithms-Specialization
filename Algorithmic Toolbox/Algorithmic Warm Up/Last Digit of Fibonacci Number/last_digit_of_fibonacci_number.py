# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n == 0:
        return 0
    if n == 1:
        return 1

    numbers = []
    numbers.append(0)
    numbers.append(1)

    for i in range(2, n+1):
        numbers.append((numbers[i-1] + numbers[i-2])%10)

    return numbers[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
