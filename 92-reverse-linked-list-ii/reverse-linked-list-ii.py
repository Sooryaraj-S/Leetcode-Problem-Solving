class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: move prev to node before left
        for _ in range(left-1):
            prev = prev.next

        # Step 2: reverse sublist
        curr = prev.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next