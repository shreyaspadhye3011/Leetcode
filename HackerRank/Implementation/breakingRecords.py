# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.

def breakingRecords(scores):
    result = [0, 0]
    minScore, maxScore = scores[0], scores[0]
    for score in scores:
        if score < minScore:
            minScore = score
            result[1] += 1
        if score > maxScore:
            maxScore = score
            result[0] += 1
    return result