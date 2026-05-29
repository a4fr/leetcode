# 649. Dota2 Senate
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        s_queue = deque()
        for i, sen in enumerate(senate):
            if sen == "R":
                r_queue.append(i)
            else:
                s_queue.append(i)

        n = len(senate)
        while r_queue and s_queue:
            r = r_queue.popleft()
            s = s_queue.popleft()

            if r < s:
                r_queue.append(r+n)
            else:
                s_queue.append(s+n)
        if r_queue:
            return "Radiant"
        return "Dire"
    

inputs = [
    ("RD", "Radiant"),
    ("RDD", "Dire"),
    ("DR", "Dire"),
    ("DDRRR", "Dire"),
    ("DRRDDR", "Dire")
]
s = Solution()
for senate, result in inputs:
    my_result = s.predictPartyVictory(senate)
    print(my_result, my_result==result)