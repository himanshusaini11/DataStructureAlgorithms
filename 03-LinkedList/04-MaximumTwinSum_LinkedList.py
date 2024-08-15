from typing import Optional
import time

start_time = time.time()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Leetcode solution.
class Solution:
    def twinSum(self, head: Optional[ListNode]) -> int : #Optional[ListNode]:
            slow = head
            fast = head
            temp = None
            n = 0
            
            while fast and fast.next:
                n += 1
                temp = slow
                slow = slow.next
                fast = fast.next.next
                
            curr = slow
            prev = None
            next_node = None

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            temp.next = prev
            
            result = 0
            ptr1 = head
            ptr2 = prev
            for _ in range(0, n):
                #print (ptr1.val, " + ", ptr2.val, " = ", ptr1.val + ptr2.val)
                #result.append(ptr1.val + ptr2.val)
                x = ptr1.val + ptr2.val
                if x > result:
                    result = x
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            #print (result)

            return result
            
            

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
    head = create_linked_list([4,2,2,3])
    print (solution.twinSum(head))
    #print (print_linked_list(temp))
    print("The time of execution of the above program is:", (time.time() - start_time) * 10**3, "ms")
