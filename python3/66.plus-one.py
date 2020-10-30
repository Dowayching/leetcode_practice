#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        lens = len(digits)
        for i in range(lens):
            index = lens - i - 1
            digits[index] += 1
            if digits[index] < 10:
                break
            digits[index] -= 10    
            if i == lens - 1:
                digits.insert(0, 1)
                break
        return digits    

# @lc code=end

