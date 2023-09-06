# https://leetcode.com/problems/split-linked-list-in-parts/?envType=daily-question&envId=2023-09-06

# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, 
# and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head

        while current is not None:
            length += 1
            current = current.next

        part_size = length // k
        longer_parts = length % k

        current = head
        resultList= []
        
        for i in range(k):
            dummy = ListNode(0)
            subListNode = dummy

            current_part_size = part_size + (1 if i < longer_parts else 0)

            for j in range(current_part_size):
                subListNode.next = current
                subListNode = subListNode.next
                if current:
                    current = current.next

            if subListNode:
                subListNode.next = None


            resultList.append(dummy.next)

        return resultList
                