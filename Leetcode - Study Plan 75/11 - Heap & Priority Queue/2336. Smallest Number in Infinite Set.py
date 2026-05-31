# 2336. Smallest Number in Infinite Set

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = [1]
        self.next_num = 2
        self.added_back = set()

    def popSmallest(self) -> int:
        num = heapq.heappop(self.smallest)
        self.added_back.discard(num)

        if not self.smallest:
            heapq.heappush(self.smallest, self.next_num)
            self.next_num += 1
        
        return num

    def addBack(self, num: int) -> None:
        if (num < self.next_num
            and num not in self.added_back
            and num not in self.smallest):
            
            heapq.heappush(self.smallest, num)
            self.added_back.add(num)



# Test Cases
# actions = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# values = [[], [2], [], [], [], [1], [], [], []]
# outputs = [None, None, 1, 2, 3, None, 1, 4, 5]

actions = ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
values = [[],[],[],[3],[],[2],[],[]]
outputs = [None,1,2,None,3,None,2,4]
s = SmallestInfiniteSet()

for a, v, o in zip(actions, values, outputs):
    print(a, s.smallest)
    if a == "SmallestInfiniteSet":
        pass
    elif a == "addBack":
        s.addBack(v[0])
    elif a == "popSmallest":
        my_result = s.popSmallest()
        print(my_result, my_result == o)
