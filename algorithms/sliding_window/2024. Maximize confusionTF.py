# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/discuss/2022245/Python-or-Sliding-window-or-greater93-fast-or-Simple

# O(N) solution
# Working for basic test cases but failing for some
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        trueCounts = self.countSequence('T', answerKey, k)
        falseCounts = self.countSequence('F', answerKey, k)
        return max(trueCounts, falseCounts)
    
    # returns max count of target(T or F) possible in answerKey
    def countSequence(self, target, answerKey, k):
        targetCount = 0
        runningCount = 0
        original_k = k
        for val in answerKey:
            if val == target:
                runningCount += 1
            else:
                if k > 0:
                    runningCount += 1
                    k -= 1
                else:
                    k = original_k
                    targetCount = max(runningCount, targetCount)
                    runningCount = 0
        return max(targetCount, runningCount)


# "FFFTTFTTFT", 3 - Output: 7 | Expected: 8