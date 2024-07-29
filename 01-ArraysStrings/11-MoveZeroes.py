from typing import List
import time

start_time = time.time()

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        check_ptr = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[check_ptr] = nums[check_ptr], nums[i]
                check_ptr += 1
        print (nums)
            

if __name__ == "__main__":
    solution = Solution()
    arr = [4,2,4,0,0,3,0,5,1,0]
    print(solution.moveZeroes(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")


"""
from typing import List
import time

start_time = time.time()

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_ptr = 0
        check_ptr = 1
        
        while check_ptr < len(nums):
            if nums[start_ptr] == 0 and nums[check_ptr] != 0:
                nums[start_ptr] = nums[check_ptr]
                nums[check_ptr] = 0
                start_ptr += 1
                check_ptr += 1
            elif nums[start_ptr] != 0 and nums[check_ptr] == 0:
                start_ptr += 1
                check_ptr += 1
            elif nums[start_ptr] != 0 and nums[check_ptr] != 0:
                start_ptr += 1
                check_ptr += 1
            else:
                check_ptr += 1
        print (nums)
            

if __name__ == "__main__":
    solution = Solution()
    arr = [4,2,4,0,0,3,0,5,1,0]
    print(solution.moveZeroes(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
"""
