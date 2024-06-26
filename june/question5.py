''' Question 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters. '''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s:
            return ""

        longest = ""
        for i in range(len(s)):
           
            palindrome1 = expand_around_center(i, i)
           
            palindrome2 = expand_around_center(i, i + 1)

            
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest


solution = Solution()
s1 = "babad"
s2 = "cbbd"

print(solution.longestPalindrome(s1))  
print(solution.longestPalindrome(s2)) 
