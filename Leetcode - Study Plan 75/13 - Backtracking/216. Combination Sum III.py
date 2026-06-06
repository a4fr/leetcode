# 216. Combination Sum III

import math

class Solution:
    def combinationSum3_approach1(self, k: int, n: int) -> list[list[int]]:
        def get_combinations(arr):
            # print(arr)
            target = arr.pop()

            min_val = 1
            if arr:
                min_val = arr[-1] + 1
            
            result = []
            for i in range(min_val, math.ceil(target/2)):
                for j in range(min_val+1, target+1):
                    if i+j == target:
                        result.append(arr + [i, j])
                    elif i+j > target:
                        break
            return result
        
        result = get_combinations([n])
        i = 0
        while i < len(result):
            # print("*", result[i])
            if len(result[i]) == k:
                break
            result.extend(get_combinations(result[i]))
            i+=1
        
        return [arr for arr in result[i:] if arr[-1] <= 9]
    

    
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        def backtrack(strat: int, path: list, total: int):
            print("*", path)
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return
            
            for num in range(strat, 10):
                if total + num > n:
                    break

                path.append(num)
                backtrack(num+1, path, total+num)
                path.pop()


        backtrack(1, [], 0)
        return result
        

inputs = [
    (3,7, [[1,2,4]]),
    # (3,9,[[1,2,6],[1,3,5],[2,3,4]]),
    # (9, 45, [[1,2,3,4,5,6,7,8,9]]),
    # (2, 18, [])
]
s = Solution()
for k,n,result in inputs:
    my_result = s.combinationSum3(k,n)
    print(my_result, my_result==result)
