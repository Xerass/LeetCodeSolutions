class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(0)
        current  = dummy_node
        carry = 0

        #since they  are in reverse order, we can just add each node normally and hold a carry

        #while any of these are not empty
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            #to get the carry, just integer div by 10
            carry = total//10
            
            #conversely, we want to get the modulo for the value we keep
            current.next = ListNode(total % 10)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_node.next
