class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        for n1 in nums1 :
            # 이진 검색으로 일치 여부 판별
            idx = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > idx and n1 == nums2[idx] :
                result.add(n1)
        return result

'''
Runtime : 44 ms
Memory : 14.4 MB
'''
