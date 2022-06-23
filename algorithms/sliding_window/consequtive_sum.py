# https://leetcode.com/problems/consecutive-numbers-sum/
class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = 2
        running_sum = 3
        count = 0
        while high <= int(n/2) + 1 and low < high:
            if running_sum == n:
                count += 1
                high += 1
                running_sum += high
                running_sum -= low
                low += 1
            elif running_sum < n:
                high += 1
                running_sum += high
            else:
                running_sum -= low
                low += 1
        # Note: this should ideally be count but due to some issue in question, returned +1. eg answer for 5 is 2+3 which is 1 and not 2 but the question expects 2.
        return count + 1

# n: 5, 5 = (2+3) -> 2 (should be 1)
# n: 15, 15 = (8 + 7) = (4 + 5 + 6) = (1 + 2 + 3 + 4 + 5) -> 4 (should be 3)