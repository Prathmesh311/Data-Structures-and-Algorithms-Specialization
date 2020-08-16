# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def IsGreaterOrEqual(i, max_digit):
    return int((i)+(max_digit)) >= int((max_digit)+ (i))


def largest_number(numbers):
    result=[]

    numbers = [int(numbers[i]) for i in range(len(numbers))]
    while numbers:
        res = ""
        for i in range(len(numbers)):
            maxNum = max(numbers)
            numbers.remove(maxNum)
            strNum = str(maxNum)
            res = res + strNum





    return res

if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
