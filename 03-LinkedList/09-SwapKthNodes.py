from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        
        for _ in range(0, k - 1):
            left = left.next
        
        curr = left
        while curr.next:
            curr = curr.next
            right = right.next
        
        left.val, right.val = right.val, left.val
        
        return head
            

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solution = Solution()
    head = create_linked_list([1])
    temp = solution.swapNodes(head, k = 1)
    print (print_linked_list(temp))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
