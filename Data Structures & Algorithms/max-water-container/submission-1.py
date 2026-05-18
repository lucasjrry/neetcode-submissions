class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) -1

        ans = float('-inf')

        while left < right:
            w = right - left
            h = min(heights[left], heights[right])

            vol = w*h
            ans = max(ans,vol)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        
        return ans

