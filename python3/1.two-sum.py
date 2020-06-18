#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        for first_i, first_num in enumerate(nums):
            second_i = first_i + 1
            for second_num in nums[first_i+1:]:
                if first_num + second_num == target:
                    return [first_i, second_i]
                second_i += 1

# @lc code=end

