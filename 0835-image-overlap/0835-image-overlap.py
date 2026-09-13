class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a_pts = [(r,c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        b_pts = [(r,c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        vCounts = Counter((r2-r1, c2-c1) for r1, c1 in a_pts for r2, c2 in b_pts)

        return max(vCounts.values()) if vCounts else 0