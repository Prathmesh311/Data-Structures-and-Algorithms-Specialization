# python3
import numpy


def edit_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    #result = [[0] * len1] * len2
    result = numpy.zeros((len1+1,len2+1))
    for i in range(len2 + 1):
        result[0][i] = i

    for i in range(len1 + 1):
        result[i][0] = i

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            insertion = result[i][j - 1] + 1
            deletion = result[i - 1][j] + 1
            match = result[i - 1][j - 1]
            misMatch = result[i - 1][j - 1] + 1

            if s1[i-1] == s2[j-1]:
                result[i][j] = min(insertion, deletion, match)
            else:
                result[i][j] = min(insertion, deletion, misMatch)

    return int(result[len1][len2])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
