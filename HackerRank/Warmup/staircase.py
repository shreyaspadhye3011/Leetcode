# https://www.hackerrank.com/challenges/staircase/problem
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.

# Logic: Print one row at a time. Formulate the logic of spaces and # for one row. It is consistent 

def staircase(n):
    row = 0
    for row in range(n):
        pattern = ""
        # add spaces to the pattern
        numberOfSpaces = n - row - 1
        for i in range(numberOfSpaces):
            pattern += " "
        
        # add # to the pattern
        numberOfPounds = n - numberOfSpaces
        for i in range(numberOfPounds):
            pattern += "#"
            
        print(pattern)