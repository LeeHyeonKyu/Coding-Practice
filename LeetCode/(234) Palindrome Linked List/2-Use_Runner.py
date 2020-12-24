# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head 
        
        # 런너가 이동하는 동안 역순 리스트 생성
        while fast and fast.next :
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # 리스트가 홀수인 경우
        if fast :
            slow = slow.next
        
        # 지나온 값(rev)과 중간 이후 값(slow)를 비교
        while rev and rev.val == slow.val :
            slow, rev = slow.next, rev.next
        
        return not rev

'''
Runtime : 52 ms
Memory : 24.3 MB
'''
