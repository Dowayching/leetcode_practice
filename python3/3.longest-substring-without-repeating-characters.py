#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        longest_len = 0
        str_start = 0

        def judge_longest_string_size(ptr, str_start, longest_len):
            # get previous string length 
            str_len = ptr - str_start
            # check if string is the largest
            if str_len > longest_len:
                longest_len = str_len
            return longest_len

        for ptr in range(len(s)):
            if ptr != str_start:    # skip s[0]
                pos = s.find(s[ptr], str_start, ptr)
                if pos != -1:
                    longest_len = judge_longest_string_size(ptr, str_start, longest_len)
                    str_start = pos + 1
        longest_len = judge_longest_string_size(len(s), str_start, longest_len)

        return longest_len
# @lc code=end

