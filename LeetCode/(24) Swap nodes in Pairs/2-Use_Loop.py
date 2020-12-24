# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = curr = head
        prev = None
        while curr and curr.next :
            next = curr.next
            if prev :
                prev.next, curr.next, next.next = next, next.next, curr
                prev = curr
                curr = prev.next
            else :
                curr.next, next.next = next.next, curr
                root = next
                prev = curr
                curr = prev.next
        return root

'''
Runtime : 32 ms
Memory : 14 MB
'''
