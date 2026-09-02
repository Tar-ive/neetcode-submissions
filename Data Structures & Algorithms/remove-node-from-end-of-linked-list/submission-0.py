# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy 
        # move right so that it is at head + n position
        right = head 

        while right and n !=0: 
            right = right.next 
            n-=1 

        # shift both pointers 
        while right: 
            left = left.next 
            right = right.next 

        # at this point left.next -> points to the node we want to delete. 
        left.next = left.next.next 

        return dummy.next
