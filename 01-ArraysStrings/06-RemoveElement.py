from typing import List
import time
start_time = time.time()

# Using Two pointer method

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        start_ptr = 0
        end_ptr = len(nums)-1
        while start_ptr <= end_ptr:
            if nums[start_ptr] == val:
                nums[start_ptr] = nums[end_ptr]
                nums[end_ptr] = "_"
                end_ptr -= 1
            else:
                start_ptr += 1
                k += 1
        return k, nums
        
        
if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print (solution.removeElement(nums, val))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
