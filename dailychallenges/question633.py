'''633. Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false
 
Constraints:

0 <= c <= 231 - 1'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math

        a = 0
        b = int(math.sqrt(c))
        
        while a <= b:
            sum_of_squares = a * a + b * b
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                a += 1
            else:
                b -= 1
                
        return False

solution = Solution()
print(solution.judgeSquareSum(5)) 
print(solution.judgeSquareSum(3))  
