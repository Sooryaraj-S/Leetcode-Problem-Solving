# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        h=head
        dummy=ListNode(0)
        curr=dummy
        if not head or not head.next:
            return head
        while h:
            if(h.next and h.val==h.next.val):
                value=h.val
                while h and h.val==value:
                    h=h.next 
            else:
                curr.next=ListNode(h.val)
                curr=curr.next
                h=h.next
    

        return dummy.next

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        