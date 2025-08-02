TwoSum

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :type: Optional[ListNode]

        dummy = ListNode(0)  # Dummy node to simplify result list creation
        current = dummy      # Pointer to build the new list
        carry = 0            # Initialize carry to 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get current value or 0 if None
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10        # Update carry for next step
            current.next = ListNode(total % 10)  # Create new node with digit
            current = current.next

            if l1: l1 = l1.next        # Move to next node
            if l2: l2 = l2.next

        return dummy.next  # Return head of the resulting linked list
