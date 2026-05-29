# 1448. Count Good Nodes in Binary Tree

from typing import Optional
from binary_tree import *


class Solution:
    def getPaths(self, root: TreeNode):
        if not root:
            return []
        
        paths = []
        if root.left:
            paths.append([root.val, root.left.val])
            new_path = self.getPaths(root.left)
            for p in new_path:
                paths.append([root.val] + p)
        if root.right:
            paths.append([root.val, root.right.val])
            new_path = self.getPaths(root.right)
            for p in new_path:
                paths.append([root.val] + p)
        return paths

    def goodNodes_approach1(self, root: TreeNode) -> int:
        counter = 1
        for values in self.getPaths(root):
            print(values)
            if max(values) <= values [-1]:
                counter += 1
        return counter
    
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            if not root:
                return 0
            
            count = 0
            if root.val >= max_so_far:
                count = 1
                max_so_far = root.val
            
            count += dfs(root.left, max_so_far)
            count += dfs(root.right, max_so_far)
            
            return count
        
        return dfs(root, root.val)
            


inputs = [
    ([3,1,4,3,None,1,5], 4),
    ([3,3,None,4,2], 3),
    ([1], 1),
    ([2,None,4,10,8,None,None,4], 4),
]
s = Solution()
for root1, result in inputs:
    my_result = s.goodNodes(create_tree(root1)[0])
    print(my_result, my_result == result)