# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=res= ListNode(0)
        carry=0
        while (l1 or l2 or carry):
            val1=val2=0
            if (l1):
                val1=l1.val
                l1=l1.next
            if (l2):
                val2=l2.val
                l2=l2.next
            s=carry+val1+val2
            carry=s//10
            res.next=ListNode(s%10)
            res=res.next
            
        return head.next
