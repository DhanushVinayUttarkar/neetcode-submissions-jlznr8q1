class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        best = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(current, best)
        
        return best