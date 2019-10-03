# Reference: https://leetcode.com/problems/word-ladder/

# Approach 1: Create dictionary that stores all possible one letter variations from the wordlist given. Keep checking whether the endWord's variation have arrived in the dictionary. If yes, then return count of how many steps it took. If the whole list is complete and you do not reach any return point means that there is no solution

# Issue: The solution assumes connected graph. But there's no such restriction. What if log -> cog is a possible transition by "log" being one of the words and "cog" being the end word but there is no link between "Hit" the beginWord and "log" to finally reaching "cog". So the assumption of it being a connecgted graph doesn't fit the problem. Also the solution assumes the given wordList to grow in a transformative fashion to give out the count correctly. It's possible that "log" might be encountered as the first word in the list and would give out result as 1 but that's wrong.

############

# Approach 2: 