from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev_node = head
        count = 0
        
        while ptr and ptr.next:
            ptr = ptr.next
            
            if ptr.val == prev_node.val:
                prev_node.next = ptr.next
                ptr = prev_node
            else:
                prev_node = ptr
        return
            

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
    head = create_linked_list([1, 1, 2, 3, 3, 4, 4, 5, 6])
    solution.deleteDuplicates(head)
    print(print_linked_list(head))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
