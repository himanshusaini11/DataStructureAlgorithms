from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        left_node = right_node = None
        n = 0
        left_ptr = None
        right_ptr = None
        
        # Traverse the list to find the nodes and their pointers at the left and right positions
        while curr:
            n += 1
            if n == left - 1:
                left_ptr = curr # Node just before the left position
            if n == right + 1:
                right_ptr = curr # Node just after the right position
            if n == left:
                left_node = curr # Node at the left position    
            if n == right:
                right_node = curr # Node at the right position
            curr = curr.next
        
        # Start reversing the sublist from left_node to right_node
        curr = left_node
        prev = None
        next_node = None
        
        for _ in range(0, right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Reconnect the reversed sublist with the left part and the right part
        if left_ptr:
            left_ptr.next = right_node # Connect the node before left to the new start of reversed sublist
        else:
            head = right_node  # If reversing starts at the head, update the head

        left_node.next = right_ptr # Connect the end of reversed sublist to the node after right

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
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    temp = solution.reverseBetween(head, left = 2, right = 8)
    print (print_linked_list(temp))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
