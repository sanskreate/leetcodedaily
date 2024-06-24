'''995. Minimum Number of K Consecutive Bit Flips
You are given a binary array nums and an integer k.
A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 
Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length
'''

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        current_flips = 0
        flip_diff = [0] * (n + 1)

        for i in range(n):
            current_flips ^= flip_diff[i]
            
            if nums[i] == current_flips:
                if i + k > n:
                    return -1
                flips += 1
                current_flips ^= 1
                flip_diff[i + k] ^= 1

        return flips

solution = Solution()
nums1 = [0, 1, 0]
k1 = 1
print(solution.minKBitFlips(nums1, k1)) 
nums2 = [1, 1, 0]
k2 = 2
print(solution.minKBitFlips(nums2, k2))
nums3 = [0, 0, 0, 1, 0, 1, 1, 0]
k3 = 3
print(solution.minKBitFlips(nums3, k3))  
