from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return any(v > 1 for v in count.values())