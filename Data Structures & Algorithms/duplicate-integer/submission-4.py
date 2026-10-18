class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmps = []
        for num in nums:
            if num in tmps:
                return True
            else:
                tmps.append(num)
        return False
