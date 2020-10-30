#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums):
        largest_num_idx = -1
        largest_num = -1
        for i in range(len(nums)):
            if nums[i] > largest_num:
                largest_num = nums[i]
                largest_num_idx = i
        for i in range(len(nums)):
            if (i != largest_num_idx) and (nums[i] * 2 > largest_num):
                return -1
        return largest_num_idx
        
# @lc code=end

