class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        nums1 = set(nums1)
        
        for num in nums2:
            if num in nums1 and num not in res:
                res.append(num)
            
        return res
                