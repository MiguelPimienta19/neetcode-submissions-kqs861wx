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

        
        second_half = slow.next 
        slow.next = None #split our list into two
        prev = None

        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp #all this does is reverses our second half of our list. 

        #now merge the two halfs! 

        second = prev #need to reset this so we get the new head our of second half
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2