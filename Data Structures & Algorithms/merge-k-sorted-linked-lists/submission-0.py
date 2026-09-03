# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: 
            return None 

        while len(lists) >1: 
            mergedLists = []
            for i in range(0, len(lists), 2): # since we want to merge 2 lists together 
                l1 = lists[i]
                l2 = lists[i +1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists 
        return lists[0]

    def merge(self, l1, l2): 
        # helper function to merge 2 linked lists together 
        arr = []
        while l1 is not None: 
            arr.append(l1.val)
            l1 = l1.next 
        
        while l2 is not None: 
            arr.append(l2.val)
            l2 = l2.next 

        arr.sort()

        tmp = ListNode(-1)
        curr = tmp 

        for value in arr: 
            curr.next = ListNode(value)
            curr = curr.next 

        return tmp.next

        
        