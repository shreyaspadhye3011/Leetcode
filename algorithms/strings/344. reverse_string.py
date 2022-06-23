# https://leetcode.com/problems/reverse-string/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        lo = 0
        hi = s_len - 1
        while lo < hi:
            # swap values             
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1