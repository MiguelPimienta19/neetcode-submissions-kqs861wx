# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #just makes our new linked list object. do we even need this im a little lost.
        node = dummy # just a node in our list. 

        while list1 and list2: #whle they are non empty 
            if list1.val < list2.val:  #grab the smaller number!
             node.next = list1 #I wonder why its not list1.val? 
             list1 = list1.next #again I dont know why its not list1.val
            else:
                node.next = list2
                list2 = list2.next
            node = node.next #we need to always update out tail pointer at the end

        if list1:
            node.next = list1

        elif list2:
            node.next = list2

        return dummy.next


    