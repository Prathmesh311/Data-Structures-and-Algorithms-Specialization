# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements,left, right):
    assert len(elements) <= 10 ** 5



    if left == right:
        return -1
    if left+1 ==right:
        return elements[left]
    m = (left + right +1)//2

    LElement = majority_element(elements,left,m)
    RElement = majority_element(elements,m,right)

    Lcount = 0
    for i in range(left,right):
        if elements[i] == LElement:
            Lcount += 1

    if Lcount >= right-left//2:
        return LElement

    RCcount = 0
    for i in range(left,right):
        if elements[i] == RElement:
            RCcount += 1
    if RCcount >= right-left//2:
        return RCcount

    return -1

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    if majority_element(input_elements,0,input_n) != -1:
        print(1)
    else:
        print(0)
