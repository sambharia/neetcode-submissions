class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) -1 
        maxL = height[l]
        maxR = height[r]
        amount = 0

        while (l<r):
            if maxL <= maxR:
                l = l+1
                maxL = max(maxL, height[l])
                amount += maxL - height[l]
            else:
                r = r- 1
                maxR = max(maxR, height[r])
                amount+= maxR - height[r]
        return amount