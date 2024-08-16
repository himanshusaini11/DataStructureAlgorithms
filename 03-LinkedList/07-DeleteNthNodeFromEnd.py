from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        ptr = head
        l = 0

        while ptr:
            l += 1
            ptr = ptr.next
        if n == l:
            return head.next

        slow = head
        temp = None
        x = 0
        while slow and slow.next:
            x += 1
            if x == l - n + 1:
                break
            temp = slow
            slow = slow.next
        temp.next = slow.next

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
    temp = solution.removeNthFromEnd(head, n = 4)
    print (print_linked_list(temp))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
