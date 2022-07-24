# https://www.hackerrank.com/challenges/mini-max-sum/problem
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    arr.sort()
    minSum, maxSum = 0, 0
    for idx, item in enumerate(arr):
        if idx < len(arr) - 1:
            minSum += item
        if idx > 0:
            maxSum += item
    print(minSum, maxSum)