# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# https://leetcode.com/problems/middle-of-the-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# The problem is done in the leetcode editor

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow