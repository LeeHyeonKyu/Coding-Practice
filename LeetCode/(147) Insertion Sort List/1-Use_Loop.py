# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = root = ListNode(0)
        while head :
            while curr.next and curr.next.val < head.val :
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            
            # 필요한 경우에만 curr 포인터가 처음으로 가도록 처리
            if head and curr.val > head.val :
                curr = root
        return root.next

'''
Runtime : 168 ms
Memory : 16.3 MB
'''
