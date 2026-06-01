# 2300. Successful Pairs of Spells and Potions


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(potions)
        potions = sorted(potions)

        result = [0] * len(spells)
        for i, spell in enumerate(spells):
            num = success / spell  # Reduced number of operations

            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2

                if  num <= potions[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            result[i] = n - left

        return result



inputs = [
    ([5,1,3], [1,2,3,4,5], 7, [4,0,3]),
    ([3,1,2],[8,5,8],16, [2,0,2]),
    ([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], 25, [0,0,0,1,3,3,4]),
    ([15,8,19], [38,36,23], 328, [3,0,3])
]

s = Solution()
for spells, potions, success, result in inputs:
    my_result = s.successfulPairs(spells, potions, success)
    print(my_result, my_result==result)
