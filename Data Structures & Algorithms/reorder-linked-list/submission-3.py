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
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        #reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #now to merge
        first, other_half = head, prev

        while other_half:
            temp1, temp2 = first.next, other_half.next
            first.next = other_half
            other_half.next = temp1

            first, other_half = temp1, temp2


        
