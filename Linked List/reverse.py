# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time: O(n), Memory: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=None
        while head:
            current=ListNode(val=head.val,next=current)
            head=head.next
        return current
    
    