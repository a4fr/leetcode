# 1340. Jump Game V

from pprint import pprint
from time import time


class Solution:
    def maxJumps(self, arr: list, d: int) -> int:
        def get_possible_jumps_for(index):
            all_indice = set()
            for i in range(1, d+1):
                if (index+i) > len(arr)-1:
                    break
                if arr[index] < arr[index+i]:
                    break
                
                all_indice.add(index+i)
            
            for i in range(1, d+1):
                if (index-i) < 0:
                    break
                if arr[index] < arr[index-i]:
                    break
                all_indice.add(index-i)
            return all_indice
        
        def get_max_step_for(max_step, index):
            if index in max_step:
                return max_step[index]
            
            max_step[index] = 0
            for i in get_possible_jumps_for(index):
                new_max_step = get_max_step_for(max_step, i) + 1
                if new_max_step > max_step[index]:
                    max_step[index] = new_max_step
            return max_step[index]
        #########

        max_step = {}
        for i, _ in sorted([(i, arr[i]) for i in range(len(arr))], key=lambda x: x[1]):
            get_max_step_for(max_step, i)
        return max(v for v in max_step.values()) + 1

    

inputs =[
    ([6,4,14,6,8,13,9,7,10,6,12], 2, 4),
    ([3,3,3,3,3], 3, 1),
    ([7,6,5,4,3,2,1], 1, 7),
]
s = Solution()
time_start = time()
for arr, d, result in inputs:
    my_result = s.maxJumps(arr, d)
    print(arr, my_result, my_result==result)
print(f"{int((time()-time_start) * 10**6)} microsec")