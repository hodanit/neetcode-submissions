class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmps = set()
        for num in nums:
            if num in tmps:
                return True
            else:
                tmps.add(num)
        return False
