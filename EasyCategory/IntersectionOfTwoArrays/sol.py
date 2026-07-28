class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #very literaly solution

        return list(set(nums1) & set(nums2))
