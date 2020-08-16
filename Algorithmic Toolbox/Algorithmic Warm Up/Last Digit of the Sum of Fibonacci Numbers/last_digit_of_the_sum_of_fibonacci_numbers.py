# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    numbers = []
    fibo    = []
    numbers.append(0)
    numbers.append(1)
    numbers.append(1)

    fibo.append(0)
    fibo.append(1)
    fibo.append(1)
    prev,curr = 0,1
    sum =1

    for i in range(2, n+1):

        '''currNum = (fibo[i-1] + fibo[i-2])%10
        fibo.append(currNum)
        numbers.append((((sum(numbers))%10 + currNum)%1)'''
        prev,curr = curr, (curr + prev)%10
        sum = (sum + curr)%10

    return sum


    '''rem = (n-1)%4
    if rem==1:
        return 2
    if rem==2:
        return 4
    if rem==3:
        return 8
    if rem==0:
        return 6'''


    '''if n <= 14:
        numbers = []
        numbers.append(0)
        numbers.append(1)
        total = 1
        for i in range(2,n+1):
            numbers.insert(i,numbers[i-1] + numbers[i-2])
            total += numbers[i]
        return total%10

    if n > 14:
        rem = (n-14)%6
        div = (n-14)/6
        if rem == 1:
            return 49 + (div * 28) + 7
        if rem == 2:
            return 49 + (div * 28) + 7
        if rem == 3:
            return 49 + (div * 28) + 14
        if rem == 4:
            return 49 + (div * 28) + 21
        if rem == 5:
            return 49 + (div * 28) + 25'''


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
