# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        #two pointer sliding window style approach, one holding the start of the sublist and the kth element from the start of the sublist. within that window, we reverse, and stitch back the list

        #dummy to safely store head
        dummy = ListNode(0, head)
        windowL = dummy

        #engine for the lookeahed node
        def getKthNode(node):
            moves = 0
            while node != None and moves < k:
                node = node.next 
                moves += 1
            return node

        while True:
            windowR = getKthNode(windowL)
            #added check that if windowR is none we back out
            if not windowR:
                break
            
            lastNodeinWindow = windowR.next

            #reverse the sublist
            prev, curr = lastNodeinWindow, windowL.next
            #keep moving till curr is finally at the last node
            while curr != lastNodeinWindow:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            #relink the list, point windowR to windowL last point and link old windowL to new start
            newEnd = windowL.next 
            windowL.next = windowR 
            windowL = newEnd


        return dummy.next
