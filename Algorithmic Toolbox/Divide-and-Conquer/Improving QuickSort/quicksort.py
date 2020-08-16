# python3

from random import randint


def partition3(array, left, right):
    m1 = array[left]
    lt = left

    gt = right
    i = lt
    while i <= gt:
        if array[i] < m1:
            array[i], array[lt] = array[lt], array[i]
            lt += 1
            i +=1
        elif array[i] == m1:
            i += 1
        else:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1




    return lt,gt
    
    '''
    for i in range(left+1, right+1):
        if array[i] <= m1:
            j = j + 1
            k = j
            array[i], array[j] = array[j], array[i]

            count = 0
            while j > 0 and array[j-1] == m1:
                array[j], array[j-1] = array[j-1],array[j]
                j = j-1
                count = count + 1
            if count > r:
                r = count
            j = k

    array[left],array[j] = array[j], array[left]'''

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
