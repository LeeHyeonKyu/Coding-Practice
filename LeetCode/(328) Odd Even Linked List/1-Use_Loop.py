# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if not head :
            return head 
        
        odd = head
        even_head = even = head.next

        # 반복하며 odd와 even연결
        while even and even.next :
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # odd의 끝과 even의 처음 연결
        odd.next = even_head
        return head

'''
Runtime : 40 ms
Memory : 16.4 MB
'''
