#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums):
        total_sum = 0
        left_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        for i in range(len(nums)):
            if i != 0:
                left_sum += nums[i - 1]
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1
        
# @lc code=end

