# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #simple operation if curr == past then we delete, iterate as we go
        past = head
        if head is not None:
            ahead = head.next
        else:
            return head

        while ahead is not None:
            if ahead.val == past.val:
                #delete ahead 
                past.next = ahead.next
                
                #move ahead as the new past.next node
                ahead = past.next
            else:
                ahead = ahead.next
                past = past.next
        
        return head
