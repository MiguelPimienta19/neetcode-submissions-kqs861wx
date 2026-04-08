# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 #if no number there just put 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry #the carry from previous iteration is here too. 

            carry = val//10 #if number is like 15 it will give 1 but lower then 10 will give 0
            val = val % 10 #give us the ones place because our carry is there. 
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None #edge cases 
            l2 = l2.next if l2 else None #edge cases and moving pointers

        
        return dummy.next
