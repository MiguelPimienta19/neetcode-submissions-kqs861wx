# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode() #this is going to be nothing as of now
        cur = dummy #this is good for now. I think will stay the whole time.
        #we need to account for the carry. 


        carry = 0 
        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 #just accounts for if they become null

            val = (val1 + val2 + carry)
            carry = val // 10 #to see if it is currently bigger than 2 digits
            val = val % 10 #if not larger then two digits we shouldn't worry


            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        
        return dummy.next