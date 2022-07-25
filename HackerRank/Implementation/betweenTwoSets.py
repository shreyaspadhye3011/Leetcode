# https://www.hackerrank.com/challenges/between-two-sets/problem
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def getTotalX(a, b):
    limit = min(b)
    dividor = lcm(a)
    factors = getCommonFactorsUntil(dividor, limit) 
    return countBetween(factors, b)

def lcm(a):
    multiplier = max(a)
    len_a = len(a)
    i = 1
    # a[i] & b[i] limit given as 100
    while i <= 100:
        count = 0
        lcm = multiplier * i
        for item in a:
            if (lcm) % item == 0:
                count += 1
        if count == len_a:
            break
        i += 1
    return lcm
 
def getCommonFactorsUntil(dividor, limit):
    factors = []
    i = 1
    while dividor * i <= limit:
        factors.append(dividor * i)
        i += 1
    return factors
  
def countBetween(factors, b):
    result = 0
    for factor in factors:
        count = 0
        for num in b:
            if num % factor == 0:
                count += 1
        if count == len(b):
            result += 1
    return result