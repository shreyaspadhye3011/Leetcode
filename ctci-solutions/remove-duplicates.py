# Reference: CTCI
# Author: Shreyas Padhye
# Problem 1.3 (Pg 97) : Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. 
# NOTE: One or two additional variables are fine. An extra copy of the array is not. FOLLOW UP Write the test cases for this method
# Solution Approach: Do a single pass. Create a dictionary to keep track of already passed elements and delete from dictionary if you encounter repeats. Merge dict elements to get string back

class solution():
    def remove_duplicates(self, s):
        d = {}

        # single pass and delete on duplicate entry
        for char in s:
            if char not in d:
                d[char] = True
            else:
                del d[char]
        
        # recombine caharters to form string
        res = ""
        for val in d:
            res += val

        return res
    
t = solution()
t.remove_duplicates("abssateryyv")