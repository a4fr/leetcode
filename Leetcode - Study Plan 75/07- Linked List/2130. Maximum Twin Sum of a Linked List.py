# 2130. Maximum Twin Sum of a Linked List


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"<{self.val}>"
    
    def show_all(self):
        nodes = [str(self.val)]
        next = self.next
        while next:
            nodes.append(str(next.val))
            next = next.next
        print(" -> ".join(nodes))

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        # head.show_all()

        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head_2 = prev
        # head_2.show_all()

        max_sum = 0
        while head:
            max_sum = max(max_sum, head.val + head_2.val)
            head = head.next
            head_2 = head_2.next
        return max_sum

        
inputs = [
    ([5,4,3,3,2,1], 6),
    ([4,2,2,3], 7),
    ([1,100000], 100001),
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

    my_result = s.pairSum(head)
    print(my_result, my_result == result)