class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)


        for i in range(len(nums)):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            
            l = i + 1
            r = len(nums) -1 

            while (l<r):
                sum = nums[l] + nums[i] + nums[r]
                if sum > 0:
                    r = r-1
                elif sum < 0:
                    l = l+1
                else:
                    output.append([nums[l],nums[i],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1

        return output