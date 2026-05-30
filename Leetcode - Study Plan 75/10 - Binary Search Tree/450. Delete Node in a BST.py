# 450. Delete Node in a BST


from binary_tree import *
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root: TreeNode):
            while root.left:
                root = root.left
            return root
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            successor = findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

inputs = [
    ([5,3,6,2,4,None,7], 3, [5,4,6,2,None,None,7]),
    ([5,3,6,2,4,None,7], 0, [5,3,6,2,4,None,7]),
    ([], 0, []),
]
s = Solution()
for root1, val, resuilt in inputs:
    my_result = s.deleteNode(None if not root1 else create_tree(root1)[0], val)
    print([] if my_result is None else my_result.as_list(),
          [] if my_result is None else my_result.as_list()==resuilt)
