# 2095. Delete the Middle Node of a Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"<{self.val}>"

class Solution:
    def deleteMiddle_approach1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointers = []
        pointer = head
        while True:
            pointers.append(pointer)
            if pointer.next:
                pointer = pointer.next
            else:
                break
        # print(pointers)
        n = len(pointers)
        middle = n // 2
        if middle == 0:
            return pointers[0].next
        elif middle == n -1:
            pointers[middle-1].next = None
        else:
            pointers[middle-1].next = pointers[middle+1]
        return pointers[0]
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


inputs = [
    ([1,3,4,7,1,2,6], [1,3,4,1,2,6]),
    ([1,2,3,4], [1,2,4]),
    ([2,1], [2]),
    ([1], [])
]
s =Solution()
for nums, result in inputs:
    head = ListNode(nums[0])
    last = head
    for i in range(len(nums)-1):
        last.next = ListNode(nums[i+1])
        last = last.next

    pointer = s.deleteMiddle(head)
    my_result = []
    while pointer:
        my_result.append(pointer.val)
        if pointer.next:
            pointer = pointer.next
        else:
            break
    print(my_result, my_result == result)