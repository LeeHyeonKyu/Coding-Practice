# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def rev(node: ListNode, prev : ListNode = None) -> ListNode :
            if not node :
                return prev
            next, node.next = node.next, prev
            return rev(next, node)
        
        return rev(head)

'''
Runtime : 36 ms
Memory : 20.4 MB
'''
