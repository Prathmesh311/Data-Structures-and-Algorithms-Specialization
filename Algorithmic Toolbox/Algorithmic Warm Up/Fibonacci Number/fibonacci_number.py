# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n == 0:
        return 0
    if n == 1:
        return 1

    numbers = []
    numbers.append(0)
    numbers.append(1)

    for i in range(2,n+1):
        numbers.insert(i,numbers[i-1] + numbers[i-2])

    return numbers[n]



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
