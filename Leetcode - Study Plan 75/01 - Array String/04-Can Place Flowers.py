# 605. Can Place Flowers
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def can_we_plant_in(index):
            if flowerbed[index-1] + flowerbed[index] + flowerbed[index+1] == 0:
                return True
            return False
        # Edge cases
        if n == 0:
            return True

        # Logic
        length_flowerbed = len(flowerbed)
        flowerbed += [0]
        can_we_plant = 0
        for i in range(length_flowerbed):
            if flowerbed[i]:
                continue
            
            if can_we_plant_in(i):
                flowerbed[i] = 1
                can_we_plant += 1
                if can_we_plant == n:
                    return True
        return False

if __name__ == "__main__":
    problem_inputs = [
        ([1,0,0,0,1], 1, True),
        ([1,0,0,0,1], 2, False),
        ([0,0,1,0,1], 1, True),
        ([1,0,0,0,1,0,0], 2, True)
    ]
    solution = Solution()
    for flowerbed, n, result in problem_inputs:
        my_result = solution.canPlaceFlowers(flowerbed, n)
        print(flowerbed, n, my_result, result==my_result, sep="\t")
