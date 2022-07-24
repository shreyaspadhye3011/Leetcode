# https://www.hackerrank.com/challenges/kangaroo/problem
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

def kangaroo(x1, v1, x2, v2):
    # As x1 < x2 (given), if v1 <= v2, it will never overtake
    if v1 <= v2:
        return 'NO'
    # If they'll meet, they will meet before x1 overtakes x2. If they don't meet before overtake, then as v2 > v1, they won't ever meet after
    while x1 < x2:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return 'YES'
    return 'NO'