from typing import List
import time

start_time = time.time()

class Solution:
    def prefixSum(self, nums: List[int]) -> List[int]:
        curr = 0
        result = []
        for i in range(0, len(nums)):
            curr += nums[i]
            result.append(curr)
        return result
        

if __name__ == "__main__":
    solution = Solution()
    nums = [5, 2, 1, 6, 3, 8]
    print(solution.prefixSum(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
