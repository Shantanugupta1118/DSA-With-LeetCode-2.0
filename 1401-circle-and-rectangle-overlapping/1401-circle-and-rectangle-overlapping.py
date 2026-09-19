class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closeX, closeY = max(x1, min(xCenter, x2)), max(y1, min(yCenter, y2))

        dx, dy = xCenter - closeX, yCenter - closeY

        return (dx*dx + dy*dy) <= (radius * radius)