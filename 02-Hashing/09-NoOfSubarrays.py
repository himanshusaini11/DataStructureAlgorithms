"""
Example : Count Number of Nice Subarrays
Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1] and [1, 2, 1, 1].
"""

from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += count[curr - k]
            count[curr] += 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(solution.numberOfSubarrays(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
