# DESCRIPTION

    """
    
    Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
    
    """
    
#SOLUTION

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        original_num = num
        num = abs(num)
        remainders = []    
        
        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7

        if original_num < 0:
            remainders.append('-')
        remainders.reverse()
        return''.join(remainders)