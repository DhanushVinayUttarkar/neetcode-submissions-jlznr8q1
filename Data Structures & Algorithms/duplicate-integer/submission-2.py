class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        any_gen = (i > 1 for i in count.values())
        return any(any_gen)