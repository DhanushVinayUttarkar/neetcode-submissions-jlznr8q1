class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = count.most_common(k)
        return [num for num, _ in most_freq]