# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    numSum = []

    if n==1:
        summands.append(1)
        return summands
    if n==2:
        summands.append(2)
        return summands
    if n==3:
        summands.append(1)
        summands.append(2)
        return summands

    numSum.append(1)
    numSum.append(2)
    numSum.append(3)

    index = 0
    cheack = 0
    for i in range(3,n):
        numSum.append(numSum[i-1] + i)
        index = i
        if numSum[i] >= n:
            if numSum[i] == n:
                cheack = 1
            break
    #print(numSum)

    if cheack == 1:
        for i in range(1,index+1):
            summands.append(i)
        return summands

    for i in range(1,index):

        if i==index-1:
            diff = n - numSum[index-1]
            summands.append(i+diff)
            return summands
        summands.append(i)




    return summands



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
