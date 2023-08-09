# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Time: O(n), Memory: O(n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while list1 or list2:
            if list2 is None:
                arr.append(list1.val)
                list1=list1.next
                continue
            elif list1 is None:
                arr.append(list2.val)
                list2=list2.next
                continue
            if list1.val==list2.val:
                arr.append(list1.val)
                arr.append(list2.val)
                list1=list1.next
                list2=list2.next
            elif list1.val<list2.val or list2 is None:
                arr.append(list1.val)
                list1=list1.next
            elif list1.val>list2.val:
                arr.append(list2.val)
                list2=list2.next
        if not arr:
            return None
        head = ListNode(val=arr[0])
        current = head

        for n in arr[1:]:
            current.next = ListNode(val=n)
            current = current.next

        return head