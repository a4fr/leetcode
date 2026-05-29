# 33. Search in Rotated Sorted Array

class Solution:
    def binary_search(self, nums, target, start, end):
        while start <= end:
            middle = (end + start) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
            
        return -1

    def search(self, nums, target: int) -> int:
        # len == 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        rotation_index = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                rotation_index = i+1
                break
        # print("Rotaiton Index:", rotation_index)
        
        if target == nums[rotation_index]:
            return rotation_index
        
        if rotation_index == 0:
            return self.binary_search(nums, target, 0, len(nums)-1)
        
        if target <= nums[-1]:
            return self.binary_search(nums, target, rotation_index, len(nums)-1)
        return self.binary_search(nums, target, 0, rotation_index-1)
    

inputs = [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([1,2,3,4,5,6,7], 0, -1),
    ([3,1], 3, 0)
]

s = Solution()
for nums, target, result in inputs:
    my_result = s.search(nums, target)
    print(nums, my_result, my_result==result)
