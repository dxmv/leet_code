# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        if count<=n:
            return head.next
        current=head
        target=count-n -1
        while target>0:
            current=current.next
            target-=1
        current.next=current.next.next
        return head