# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #this is literally linked list stuff


        slow, fast = head, head.next #these are here because we need to find mid and end of list. 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now reverse second half of list once we get mid and end

        second = slow.next #gives us first from second half then we set it to null but since second is defined as it already we are good. 
        slow.next = None #we now make it to null to split it
        prev = None 
        
        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp #this is regular reversing a list
        

        #this gives head of first half, and prev gives head of second half. Now we use this to merge our list. 
        first, second = head, prev 
        while second: #we use second because its usually smaller
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1 #do temp one here because we changed it on line 35
            first, second = temp1, temp2
