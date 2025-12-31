# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #fast slow approach
        fast = head
        slow = head

        #fast is our main determiner, if it does not end up being null, then there must be a cycle
        #since fast moves 2 times as fast, it will eventually meet up with slow
        while fast:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
