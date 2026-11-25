class Solution:
    def maxArea(self, heights: List[int]) -> int:
        interval = len(heights)-1
        water = 0
        l,r = 0, len(heights)-1
        while l<r:
            if heights[l] < heights[r] :
                if heights[l]*interval > water :
                    water = heights[l]*interval
                l+=1
                interval-=1
            elif heights[l] >= heights[r]:
                if heights[r]*interval > water :
                    water = heights[r]*interval
                r-=1
                interval-=1

        return water
