class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1),len(word2)

        last_pos = [-1]*(m+1)
        last_pos[m] = n

        j = m-1
        for i in range(n-1, -1, -1):
            if j>=0 and word1[i] == word2[j]:
                last_pos[j] = i
                j -= 1
        
        ans = []
        changed = False
        w1_idx = 0

        for w2_idx in range(m):
            flag = False

            while w1_idx < n:
                if word1[w1_idx] == word2[w2_idx]:
                    ans.append(w1_idx)
                    w1_idx += 1
                    flag = True
                    break
                elif not changed and last_pos[w2_idx +1] > w1_idx:
                    ans.append(w1_idx)
                    w1_idx += 1
                    changed = True
                    flag = True
                    break
                w1_idx += 1
            
        if not flag: return []
        return ans  