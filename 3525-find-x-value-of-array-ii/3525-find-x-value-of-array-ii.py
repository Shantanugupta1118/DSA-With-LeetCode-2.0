class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1]*(2*n)
        tree_remain = [[0]*k for _ in range(2*n)]

        def set_leaf(idx: int, val: int):
            tree_prod[idx] = val
            tree_remain[idx] = [0]*k
            tree_remain[idx][val] = 1

        def merge(left_prod: int, left_rem: list[int], right_prod: int, right_rem: list[int]):
            prod = (left_prod * right_prod) % k
            rem = list(left_rem)
            for r in range(k):
                rem[(r * left_prod) % k] += right_rem[r]
            return prod, rem

        for i in range(n):
            set_leaf(n+i, nums[i]%k)

        for i in range(n-1, 0, -1):
            tree_prod[i], tree_remain[i] = merge(
                tree_prod[2*i], 
                tree_remain[2*i],
                tree_prod[2*i+1], 
                tree_remain[2*i+1]
            )
        ans = []
        for idx, val, start, x in queries:
            pos = n+idx
            set_leaf(pos, val%k)
            pos //= 2
            while pos>0:
                tree_prod[pos], tree_remain[pos] = merge(
                    tree_prod[2*pos], 
                    tree_remain[2*pos],
                    tree_prod[2*pos+1],
                    tree_remain[2*pos+1]
                )
                pos //= 2
            l, r = n + start, 2 * n - 1
            left_p, left_rem = 1, [0]*k
            right_nodes = []

            while l<= r:
                if l%2 == 1:
                    left_p, left_rem = merge(
                        left_p, 
                        left_rem,
                        tree_prod[l],
                        tree_remain[l]
                    )
                    l += 1
                if r%2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
            
            for node in reversed(right_nodes):
                left_p, left_rem = merge(
                    left_p, 
                    left_rem,
                    tree_prod[node],
                    tree_remain[node]
                )
            ans.append(left_rem[x])
        return ans
