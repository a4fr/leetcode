# 735. Asteroid Collision

class Solution:
    def collision_result(self, al, ar):
        if al > 0 and ar < 0:
            if abs(al) > abs(ar):
                return [al]
            if abs(al) < abs(ar):
                return [ar]
            if abs(ar) == abs(al):
                return []
        else:
            return [al, ar]

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            if len(stack) < 2:
                continue

            # If we have collision
            while len(stack) >= 2:
                al = stack.pop()
                ar = stack.pop()
                result = self.collision_result(ar, al)
                stack.extend(result)
                if len(result) == 2 or len(result) == 0:
                    break
        return stack
    
inputs = [
    ([5,10,-5], [5,10]),
    ([8, -8], []),
    ([10,2,-5], [10]),
    ([3,5,-6,2,-1,4], [-6, 2, 4])
]
s = Solution()
for asteroids, result in inputs:
    my_result = s.asteroidCollision(asteroids)
    print(my_result, my_result == result)