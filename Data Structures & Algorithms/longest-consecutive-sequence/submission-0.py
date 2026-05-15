class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = sorted(nums)
        top = 1
        current = 1
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == 1:
                current += 1
                top = max(top, current)
            elif arr[i] != arr[i+1]:
                current = 1
        return top