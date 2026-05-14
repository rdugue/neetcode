class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        prod = 1
        zeroes = 0

        for num in nums:
            if num == 0:
                zeroes += 1
                if zeroes > 1:
                    return output 
            if num != 0:
                prod *= num

        for i, num in enumerate(nums):
            if zeroes > 0 and num ==0:
                output = [0] * n
                output[i] = prod
                return output 
            output[i] = prod if num == 0 else prod // num

        return output 