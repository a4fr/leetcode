# 328. Odd Even Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"<{self.val}>"

class Solution:
    def oddEvenList_approach1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        even_head = None
        even_last  = None
        odd_head = None
        odd_last = None
        pointer = head
        i = 0
        while pointer:
            node = ListNode(pointer.val)
            if i % 2 == 0:
                if even_last:
                    even_last.next = node
                else:
                    even_head = node
                even_last = node
            else:
                if odd_last:
                    odd_last.next = node
                else:
                    odd_head = node
                odd_last = node
            pointer  = pointer.next
            i += 1
        
        even_last.next = odd_head
        return even_head
    
    def oddEvenList_approach1_o1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        even_head = None
        even_last  = None
        odd_head = None
        odd_last = None
        pointer = head
        i = 0
        while pointer:
            node = ListNode(pointer.val)
            if i % 2 == 0:
                if even_last:
                    even_last.next = node
                else:
                    even_head = node
                even_last = node
            else:
                if odd_last:
                    odd_last.next = node
                else:
                    odd_head = node
                odd_last = node
            pointer  = pointer.next
            i += 1
        
        even_last.next = odd_head
        return even_head

    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Time:  O(n)
            Space: O(1)
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
        
inputs = [
    ([1,2,3,4,5], [1,3,5,2,4]),
    ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]),
]
s =Solution()
for nums, result in inputs:
    head = ListNode(nums[0])
    last = head
    for i in range(len(nums)-1):
        last.next = ListNode(nums[i+1])
        last = last.next

    pointer = s.oddEvenList(head)
    my_result = []
    while pointer:
        my_result.append(pointer.val)
        if pointer.next:
            pointer = pointer.next
        else:
            break
    print(my_result, my_result == result)