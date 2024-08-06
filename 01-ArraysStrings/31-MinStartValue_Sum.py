from typing import List
import time

start_time = time.time()

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            prefix += nums[i]
            if prefix < temp:
                temp = prefix
        if temp > 0:
            return 1
        else:
            return 1 - temp
        

if __name__ == "__main__":
    solution = Solution()
    nums = [-5,-2,4,4,-2]
    print(solution.minStartValue(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
