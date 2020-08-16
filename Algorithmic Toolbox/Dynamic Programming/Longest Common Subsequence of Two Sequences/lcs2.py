# python3
import numpy


def lcs2(s1, s2):
    # assert len(first_sequence) <= 100
    # assert len(second_sequence) <= 100
    len1 = len(s1)
    len2 = len(s2)
    LSeg = numpy.zeros((len1 + 1, len2 + 1))

    '''count1 = 0
    r1,r2 = 0
    for i, num1 in enumerate(r1,s1):
        for j, num2 in enumerate(r2,s2):
            if num1 == num2:
                count1 += 1
                r2 = j + 1
    count2 = 0
    r1,r2 = 0
    for i, num1 in enumerate(r1,s2):
        for j, num2 in enumerate(r2,s1):
            if num1 == num2:
                count2 += 1
                r2 = j + 1
    '''

    for i, num1 in enumerate(s1):
        for j, num2 in enumerate(s2):
            if num1 == num2:
                LSeg[i + 1][j + 1] = LSeg[i][j] + 1
            else:
                LSeg[i + 1][j + 1] = max(LSeg[i + 1][j], LSeg[i][j + 1])

    return int(LSeg[len1][len2])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
