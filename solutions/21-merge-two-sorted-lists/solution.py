class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy
        
        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes, if any
        current.next = list1 or list2
        
        # Return the head of the merged list
        return dummy.next