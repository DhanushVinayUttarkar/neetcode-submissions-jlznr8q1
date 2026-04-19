class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res

    def decode(self, s: str) -> List[str]:
        
        decrypted_sig = []

        i = 0

        while i < len(s):
            
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+length+1]
            decrypted_sig.append(word)
            i = j + length + 1
        
        return decrypted_sig