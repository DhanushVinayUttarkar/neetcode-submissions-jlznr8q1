class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        measure = len(nums)

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for k in freq:
            if freq[k] > (measure/2):
                return k
        
        return 0
        