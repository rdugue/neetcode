class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = sum(nums)
        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums:
                j = nums.index(val)
                if i != j:
                    return sorted([i, j])
                

        return None