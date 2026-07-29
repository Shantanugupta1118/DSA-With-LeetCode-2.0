class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
            
        odd_chars = [i for i, c in enumerate(counts) if c % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = chr(odd_chars[0] + 97) if odd_chars else ""
        
        half_counts = [c // 2 for c in counts]
        total_half_len = sum(half_counts)
        
        fact = [1] * (total_half_len + 1)
        for i in range(1, total_half_len + 1):
            fact[i] = fact[i - 1] * i
            
        def initial_permutations():
            denom = 1
            for c in half_counts:
                if c > 1:
                    denom *= fact[c]
            return fact[total_half_len] // denom

        current_perms = initial_permutations()
        if current_perms < k:
            return ""
            
        left_half = []
        rem_len = total_half_len
        
        for _ in range(total_half_len):
            for char_idx in range(26):
                count = half_counts[char_idx]
                if count > 0:
                    next_perms = (current_perms * count) // rem_len
                    
                    if k <= next_perms:
                        left_half.append(chr(char_idx + 97))
                        half_counts[char_idx] -= 1
                        current_perms = next_perms
                        rem_len -= 1
                        break
                    else:
                        k -= next_perms
                        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
