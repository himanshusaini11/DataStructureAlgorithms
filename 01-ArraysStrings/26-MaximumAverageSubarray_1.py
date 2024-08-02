from typing import List
import time

start_time = time.time()

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(0, k):
            curr += nums[i]
        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr)
        return round(ans/k, 5)

if __name__ == "__main__":
    solution = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(solution.findMaxAverage(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
