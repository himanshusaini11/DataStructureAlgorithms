from typing import List
import time

start_time = time.time()

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        check_ptr = 0
        for i in range(0, len(nums)):
            if nums[i]%2 == 0:
                nums[i], nums[check_ptr] = nums[check_ptr], nums[i]
                check_ptr += 1
        return nums

if __name__ == "__main__":
    solution = Solution()
    arr = [3,1,2,4]
    print(solution.sortArrayByParity(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
