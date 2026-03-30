# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #technically a 2 pointer approach solution
        #we need to have a dummy in the case where head is removed
        dummy = ListNode(0, head)
        #one fast one slow

        slow = dummy
        fast = dummy

        #move fast ahead by n times
        #rare for loop for the sake of loopingm n+1 since we started at dummy
        for _ in range(n + 1):
            fast = fast.next
        
        # we move each one by one, the moment fast hits none, slow must be at nth from end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        #perform the classic skip over to remove
        target = slow.next
        slow.next = slow.next.next
        
        #remove safely
        del(target)

        return dummy.next




