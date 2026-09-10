# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        match_count = 0
        def dfs(node):
            nonlocal match_count
            if not node:
                return 0, 0
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)

            totalSum = l_sum + r_sum + node.val
            totalCount = l_count + r_count + 1

            if totalSum // totalCount == node.val:
                match_count += 1
            
            return totalSum, totalCount
        dfs(root)
        return match_count
