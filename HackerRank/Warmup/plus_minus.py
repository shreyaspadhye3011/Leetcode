# https://www.hackerrank.com/challenges/plus-minus/problem
# Learning: decimal precision
def plusMinus(arr):
    totalCount = len(arr)
    positives, negatives, zeroes = 0, 0, 0
    for item in arr:
        if item > 0:
            positives += 1
        elif item < 0:
            negatives += 1
        else:
            zeroes += 1
            
    print("{:.6f}".format(positives/totalCount))
    print("{:.6f}".format(negatives/totalCount))
    print("{:.6f}".format(zeroes/totalCount))