# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val==0:
            return head
        current = head
        res = []
        while current:
            res.append(current.val)
            current = current.next
        number = 0
        for digit in res:
            number = number * 10 + digit
        number *= 2
        res = []
        while number:
            res.append(number % 10)
            number //= 10
        dummy = ListNode(-1)
        current = dummy
        for digit in reversed(res):
            current.next = ListNode(digit)
            current = current.next
        return dummy.next
   
