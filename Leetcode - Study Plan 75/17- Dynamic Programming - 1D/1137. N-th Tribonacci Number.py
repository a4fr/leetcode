# 1137. N-th Tribonacci Number


class Solution:
    memory = [0,1,1,2]

    def tribonacci(self, n: int) -> int:
        if n < len(self.memory):
            # print('* memory')
            return self.memory[n]
        
        last_n = len(self.memory) - 1
        for i in range(last_n, n):
            self.memory.append(
                sum(self.memory[i-2:i+1])
            )
        return self.memory[n]
        



inputs = [
    (3, 2),
    (4, 4),
    (25, 1389537),
]
s = Solution()
for n, result in inputs:
    my_result = s.tribonacci(n)
    print(my_result, my_result==result)