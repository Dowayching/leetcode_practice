#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = prev_l3_node = None
        carry = 0
        while((l1 is not None) or (l2 is not None) or (carry != 0)):
            val1 = val2 = 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            sum = val1 + val2 + carry

            ltmp = ListNode()
            ltmp.val = sum % 10
            carry = int(sum / 10)
            if prev_l3_node is not None:
                prev_l3_node.next = ltmp
                prev_l3_node = prev_l3_node.next
            else:
                l3 = prev_l3_node = ltmp

        return l3

# @lc code=end

