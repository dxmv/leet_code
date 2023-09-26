# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time:O(n), Memory: O(n)
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        res=[]
        l,r=0,len(arr)-1
        while l<r:
            res.append(arr[l])
            res.append(arr[r])
            l+=1
            r-=1
        if len(arr)%2!=0:
            res.append(arr[l])
        current=head
        for i in range(1,len(res)):
            current.next=ListNode(val=res[i])
            current=current.next