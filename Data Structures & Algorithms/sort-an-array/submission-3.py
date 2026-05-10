class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quicksort(nums, 0, len(nums) - 1)
        return nums
        
def quicksort(arr, low, high):
    if low < high:
        idx = partition(arr, low, high)
        quicksort(arr, low, idx - 1)
        quicksort(arr, idx + 1, high)

def partition(arr, low, high):
    idx = low + (high - low) // 2
    arr[idx], arr[high] = arr[high], arr[idx]
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i