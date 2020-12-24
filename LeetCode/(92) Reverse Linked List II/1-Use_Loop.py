# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외처리
        if not head or m == n :
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        # start와 end 찾기
        for _ in range(m-1) :
            start = start.next
        end = start.next
        
        # 반복하며 노드 역순으로 연결
        for _ in range(n-m) :
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            
        return root.next

'''
Runtime : 28 ms
Memory : 14.4 MB
'''
