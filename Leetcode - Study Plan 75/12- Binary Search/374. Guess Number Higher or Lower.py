PICKED = 6
def guess(n):
    if n == PICKED:
        return 0
    elif n > PICKED:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        min_num = 0
        max_num = n
        r = guess(n)
        while r != 0:
            if r == -1:
                max_num = n
            else:
                min_num = n
            n = (max_num + min_num) // 2
            r = guess(n)
        return n


inputs = [
    (10, 6),
    (1,1),
    (2, 1),
]
s = Solution()
for n, pick in inputs:
    PICKED = pick
    my_result = s.guessNumber(n)
    print(my_result, my_result==pick)
