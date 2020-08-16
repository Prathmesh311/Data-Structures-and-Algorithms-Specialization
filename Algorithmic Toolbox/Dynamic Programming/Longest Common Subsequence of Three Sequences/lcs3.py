# python3
import numpy

def lcs3(s1, s2, s3):
    assert len(s1) <= 100
    assert len(s2) <= 100
    assert len(s3) <= 100

    D = numpy.zeros((len(s1)+1, len(s2)+1, len(s3)+1))

    for i,num1 in enumerate(s1):
        for j,num2 in enumerate(s2):
            for k,num3 in enumerate(s3):
                if num1 == num2 == num3:
                    D[i+1][j+1][k+1] = D[i][j][k] + 1
                else:
                    D[i+1][j+1][k+1] = max(D[i][j+1][k+1], D[i+1][j][k+1], D[i+1][j+1][k])

    return int(D[len(s1)][len(s2)][len(s3)])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
