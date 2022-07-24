# https://www.hackerrank.com/challenges/diagonal-difference/problem
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

# Assumption: that input will always be a square matrix

def diagonalDifference(arr):
    matrixDimension = len(arr)
    # calculate left to right diagonal sum
    sum1 = 0
    row, col = 0, 0
    while row < matrixDimension:
        sum1 += arr[row][col]
        row += 1
        col += 1
        
    # calculate right to left diagonal sum
    sum2 = 0
    row, col = 0, matrixDimension - 1
    while row < matrixDimension:
        sum2 += arr[row][col]
        row += 1
        col -= 1
    
    return abs(sum1 - sum2)