# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curr = dummyNode

        #dummy node will point to head
        #temp node will hold temporary nexts
        #it's already sorted beforehand so we can just compare them node by node and attach them accordingly to each other
        while list1 and list2:
            if list1.val > list2.val:
                #current builds the actual linked list we will pass
                curr.next = list2
                #move pointer forward
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            #make node as the next so we can attach more nodes from there
            curr = curr.next

        if list1 or list2:
            #cases when there are remaining elements in one of the lists
            curr.next = list1 or list2

        return dummyNode.next

        
