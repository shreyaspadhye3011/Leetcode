# https://leetcode.com/problems/minimum-window-substring/

# status - Correct answer but TLE. Optimize!
def smallest_substr(str, pattern):
    length = len(str)
    patternLen = len(pattern)
    min = ""
    minLength = length + 1
    for i in range(0, length):
        j = i
        while j <= length:
            sublen = len(str[i:j])
            if patternLen <= sublen:
                if set(pattern).issubset(set(str[i:j])):
                    if sublen < minLength:
                        min = str[i:j]
                        minLength = sublen
            j += 1
    return min

# smallest_substr('abaacbab', 'abc') #acb
# smallest_substr('bcaacbc', 'abc')  #bca
# smallest_substr('aabaaccbcbcca', 'abc')  #baac
# smallest_substr('bbcbbdbccccabbbbd', 'abcd')  #dbcccca
# smallest_substr('abaacbab', 'abc') #acb
# smallest_substr('ADOBECODEBANC', 'ABC') #BANC
# smallest_substr('a', 'a') #a
# smallest_substr('ba', 'ab') #ba
# smallest_substr('bac', 'abc') #bac
smallest_substr('bac', 'A') #''