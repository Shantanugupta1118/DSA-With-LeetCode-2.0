class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res, cur = set(), ['']
        
        for char in expression:
            if char == '{':
                stack.append((res, cur))
                res, cur = set(), ['']
            elif char == '}':
                prev_res, prev_cur = stack.pop()
                combined = res | set(cur)
                cur = [a + b for a in prev_cur for b in combined]
                res = prev_res
            elif char == ',':
                res.update(cur)
                cur = ['']
            else:
                cur = [s + char for s in cur]
                
        return sorted(list(res | set(cur)))