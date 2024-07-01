# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nextNode = None
        
        while curr: # Recursuve Approach
            nextNode = curr.next # variable used to complete the turn around.
            curr.next = prev # logic start recursively.
            prev = curr 
            curr = nextNode
        return prev
