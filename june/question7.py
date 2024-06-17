'''7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21 

Constraints:

-231 <= x <= 231 - 1'''

class Solution:
    def reverse(self, x: int) -> int:
       
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        reversed_x = int(str(x_abs)[::-1])
        
        reversed_x *= sign
        
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x


solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))  
print(solution.reverse(120))   
