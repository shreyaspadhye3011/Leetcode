# https://www.hackerrank.com/challenges/apple-and-orange/problems
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    # count apples
    for loc in apples:
        if a + loc >= s and a + loc <= t:
            appleCount += 1
    
    # count oranges
    for loc in oranges:
        if b + loc >= s and b + loc <= t:
            orangeCount += 1
    print(appleCount)
    print(orangeCount)