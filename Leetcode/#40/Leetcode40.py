# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        m = head.next
        n = m
        while n:
            total = 0
            while n.val != 0:
                total += n.val
                n = n.next
            m.val = total
            n = n.next
            m.next = n
            m = m.next

        return head.next