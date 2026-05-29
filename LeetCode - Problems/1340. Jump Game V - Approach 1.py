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
                if arr[index] > arr[index+i]:
                    all_indice.add(index+i)
                    continue
                break
            
            for i in range(1, d+1):
                if (index-i) < 0:
                    break
                if arr[index] > arr[index-i]:
                    all_indice.add(index-i)
                    continue
                break
            return all_indice
        #########

        jumps = {}
        num_jumps = [0] * len(arr)
        for i in range(len(arr)):
            indice = get_possible_jumps_for(i)
            jumps[i] = indice
            num_jumps[i] = len(indice)
                
        # pprint(jumps)
        steps = 0
        while len(jumps):
            steps += 1
            for zero_k in [k for k in range(len(num_jumps)) if num_jumps[k] == 0]:
                jumps.pop(zero_k)
                num_jumps[zero_k] = None
                for k,v in jumps.items():
                    if zero_k in v:
                        jumps[k].remove(zero_k)
                        num_jumps[k] -= 1
            # print(jumps)
        return steps
    

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