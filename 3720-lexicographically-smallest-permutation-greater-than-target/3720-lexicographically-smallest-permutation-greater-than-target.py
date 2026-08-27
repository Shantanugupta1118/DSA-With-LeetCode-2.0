from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Check if a given prefix of target can be formed using s's characters
        def can_form(prefix_counts, target_prefix):
            req = Counter(target_prefix)
            return all(prefix_counts[c] >= req[c] for c in req)

        # Iterate right-to-left for the position i where s[i] > target[i]
        for i in range(n - 1, -1, -1):
            prefix_to_match = target[:i]
            
            if can_form(total_counts, prefix_to_match):
                # Calculate remaining characters after matching target[:i]
                rem_counts = total_counts.copy()
                for c in prefix_to_match:
                    rem_counts[c] -= 1
                
                # Try picking the smallest character strictly greater than target[i]
                for ch in sorted(rem_counts.keys()):
                    if ch > target[i] and rem_counts[ch] > 0:
                        rem_counts[ch] -= 1
                        
                        # Build remaining suffix in sorted order
                        suffix = []
                        for char in sorted(rem_counts.keys()):
                            suffix.append(char * rem_counts[char])
                        
                        return prefix_to_match + ch + "".join(suffix)
                        
        return ""