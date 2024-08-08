"""
Example : Subarray Sum Equals K

Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
"""

from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans = curr = 0
        
        for i in range(0, len(nums)):
            curr += nums[i]
            if curr - k in count:
                ans += 1
            count[curr] += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2, 1]
    k = 3
    print(solution.subarraySum(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
