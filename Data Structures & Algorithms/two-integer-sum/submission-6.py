class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            val = target - nums[i]
            try:
                return [hash[val], i]
            except KeyError:
                hash[nums[i]] = i 

        return None