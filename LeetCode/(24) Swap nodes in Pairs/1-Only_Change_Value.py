# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next :
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head

'''
Runtime : 28 ms
Memory : 14.2 MB
'''
