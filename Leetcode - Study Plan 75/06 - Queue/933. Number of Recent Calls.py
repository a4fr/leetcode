# 933. Number of Recent Calls

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
inputs = [
    (
        ["RecentCounter", "ping", "ping", "ping", "ping"],
        [[], [1], [100], [3001], [3002]],
        [None, 1, 2, 3, 3],
    ),
]

for inp in inputs:
    for event, t, result in zip(*inp):
        if event == "RecentCounter":
            obj = RecentCounter()
        else:
            my_result = obj.ping(t[0])
            print(my_result, my_result == result)
# obj = RecentCounter()
# param_1 = obj.ping(t)