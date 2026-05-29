# 206. Reverse Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"<{self.val}>"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        while curr_node:
            # Change the next
            next_node = curr_node.next
            curr_node.next = prev_node
            # Change prev and curr
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node

        
inputs = [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], [])
]
s =Solution()
for nums, result in inputs:
    head = None
    if nums:
        head = ListNode(nums[0])
        last = head
        for i in range(len(nums)-1):
            last.next = ListNode(nums[i+1])
            last = last.next

    pointer = s.reverseList(head)
    my_result = []
    while pointer:
        my_result.append(pointer.val)
        if pointer.next:
            pointer = pointer.next
        else:
            break
    print(my_result, my_result == result)