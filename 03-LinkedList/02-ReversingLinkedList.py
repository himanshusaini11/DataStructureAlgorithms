from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        next_node = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
            
            

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
    head = create_linked_list([1, 2, 3, 4])
    temp = solution.reverseLinkedList(head)
    print(print_linked_list(temp))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
