
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.val})"
    


# Create tree
def create_tree(values):
    if not values:
        return None
        
    nodes = [TreeNode(v) if v is not None else None for v in values]
    childrens = deque(nodes[1:])

    for n in nodes:
        if n is None:
            continue
        
        if childrens:
            n.left = childrens.popleft()
        if childrens:
            n.right = childrens.popleft()
    return nodes


if __name__ == "__main__":
    # Inputs
    inputs =[
        [3,9,20,None, None,15,7],
        [1,None,2],
    ]
    for values in inputs:
        nodes = create_tree(values)
        print([str(n) for n in nodes])