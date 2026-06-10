class Solution:
    def jump(self, nums: List[int]) -> int:
        
        total_len = len(nums)
        
        if total_len <= 1:
            return 0
        
        total_jumps = 0
        current_end = 0
        furthest_end = 0

        for i in range(total_len - 1):
            furthest_end = max(furthest_end, i+nums[i])

            if i == current_end:
                total_jumps += 1
                current_end = furthest_end
            
            if current_end >= total_len-1:
                break
        
        return total_jumps