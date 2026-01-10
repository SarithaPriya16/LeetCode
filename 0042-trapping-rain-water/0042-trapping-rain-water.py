class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        leftmax = [0] * n
        rightmax = [0] * n

        # Prefix max
        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], height[i])

        # Suffix max
        rightmax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])

        # Calculate trapped water
        water = 0
        for i in range(n):
            water += min(leftmax[i], rightmax[i]) - height[i]

        return water
