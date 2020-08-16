# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def Enquiry(stack):
    if len(stack) == 0:
        return True
    else:
        return False


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index_num = []
    index = -1
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            index_num.append(i)

        if next in ")]}":
            # Process closing bracket, write your code here
            if Enquiry(opening_brackets_stack):
                index = i
                break
            else:
                top = opening_brackets_stack.pop()
                stack_index = index_num.pop()
                if not are_matching(top, next):
                    index = i
                    break
                '''if top == "[" and next != "]" or top == "(" and next != ")":
                    return False'''
    if index != -1:
        return index

    if not Enquiry(opening_brackets_stack):
        first_opening_bracket = index_num.pop()
        return first_opening_bracket

    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch + 1)


if __name__ == "__main__":
    main()
