
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        for k in range(len(nums)):
            if zero_count > 1:
                products[k] = 0
            elif zero_count == 1:
                if nums[k] == 0:
                    products[k] = total_product
            else:
                products[k] = total_product // nums[k]

        return products
