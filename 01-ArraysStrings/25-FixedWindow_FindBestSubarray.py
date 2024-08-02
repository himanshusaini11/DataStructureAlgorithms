from typing import List
import time

start_time = time.time()

class Solution:
    def findBestSubarray(self, nums: List[int], k: int) -> int:
        curr = 0
        for i in range(0, k):
            curr += nums[i]
        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr)
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [3, -1, 4, 12, -8, 5, 6]
    k = 4
    print(solution.findBestSubarray(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
