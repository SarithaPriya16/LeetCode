class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        left=[-1]*n
        right=[n]*n
        stack=[]
        #previous smallest element
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            left[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        #next smaller ele
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right[i]=stack[-1] if stack else n
            stack.append(i)
        
        max_area=0
        for i in range(n):
            width=right[i]-left[i]-1
            max_area=max(max_area,heights[i]*width)
        return max_area
        