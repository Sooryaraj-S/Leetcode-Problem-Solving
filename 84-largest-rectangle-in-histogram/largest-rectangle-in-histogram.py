class Solution(object):
    def largestRectangleArea(self, heights):
        n=len(heights)
        area=0
        stack=[]
        for i in range(n):
            while stack and heights[i]< heights[stack[-1]]:
                h=heights[stack.pop()]
                if stack:
                    w=i-stack[-1]-1
                else:
                    w=i
                area=max(area,h*w)
            stack.append(i)
        while stack:
            h=heights[stack.pop()]
            if stack:
                w=n-stack[-1]-1
            else:
                w=n
            area=max(area,h*w)
        return area