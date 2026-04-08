# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # left = dummy
        # right = head

        # while n > 0:
        #     right = right.next
        #     n -= 1
        
        # while right: 
        #     left = left.next
        #     right = right.next
        
        # #now we can finally delete 
        # left.next = left.next.next

        # return dummy.next

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        #just made our list

        remove = len(nodes) - n #gives us index of the thing we need to get rid of 
        if remove == 0:
            return head.next

        nodes[remove - 1].next = nodes[remove].next

        return head 