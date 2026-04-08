# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #this gets slow to be the middle and fast will be the end of the list

        mid = slow.next 
        prev = slow.next = None

        #reverse second half of list
        while mid:
            temp = mid.next 
            mid.next = prev 
            prev = mid 
            mid = temp 
        
        #grabs ends of first half and second half.
        first, second = head, prev

        #now merge
        while second: #second should be smaller
            tmp1, tmp2 = first.next, second.next
            first.next = second #makes the next value from index 0, n - 1
            second.next = tmp1 #then the second to last value from the front
            first = tmp1
            second = tmp2