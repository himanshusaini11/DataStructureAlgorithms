from typing import List
import time

start_time = time.time()

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = ans = 0
        curr = 1 # because we are dealing with product.
        
        for right in range(0, len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left +1
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(solution.numSubarrayProductLessThanK(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
