# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        prevGroupTail = dummy
        
        while True:
            # Check whether k nodes remain starting after prevGroupTail
            kth = prevGroupTail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes left -> leave as-is
            
            groupStart = prevGroupTail.next
            groupNext = kth.next
            
            # reverse nodes groupStart..kth in place
            prev, curr = groupNext, groupStart
            while curr is not groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            prevGroupTail.next = kth      # kth is now the head of the reversed group
            prevGroupTail = groupStart    # groupStart is now the tail of the reversed group