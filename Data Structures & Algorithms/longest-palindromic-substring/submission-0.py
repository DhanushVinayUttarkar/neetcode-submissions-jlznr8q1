class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        best_start, best_len = 0, 1
        def expand(left, right):
            nonlocal best_start, best_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > best_len:
                    best_len = right - left + 1
                    best_start = left
                
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i,i)
            expand(i, i+1)
        
        return(s[best_start : best_start+best_len])