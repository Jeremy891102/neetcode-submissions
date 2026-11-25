class Solution:
    def maxArea(self, heights: List[int]) -> int:
        interval = len(heights)-1
        water = set()
        l,r = 0, len(heights)-1
        while l<r:
            if heights[l] < heights[r]:
                water.add(heights[l]*interval)
                l+=1
                interval-=1
            elif heights[l] >= heights[r]:
                water.add(heights[r]*interval)
                r-=1
                interval-=1

        return max(water)
