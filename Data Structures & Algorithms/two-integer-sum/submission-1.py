class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for num in nums:
            if target-num in nums:
                nums2 = nums.copy()
                nums2.remove(num)
                if target-num in nums2:
                    return [nums.index(num), nums2.index(target-num)+1]
            