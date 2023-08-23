# 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(val=0)
    current = head
    add = 0
    while l1 or l2:
        if l1 and not l2:
            sum_l = l1.val + add
            add = sum_l // 10
            current.val = sum_l - add * 10
            l1 = l1.next
        elif l2 and not l1:
            sum_l = l2.val + add
            add = sum_l // 10
            current.val = sum_l - add * 10
            l2 = l2.next
        else:
            sum_l = l1.val + l2.val + add
            add = sum_l // 10
            current.val = sum_l - add * 10
            l1 = l1.next
            l2 = l2.next
        if l1 or l2 or add:
            current.next = ListNode(val=0)
            current = current.next
    if add>0:
        current.val=add
    return head