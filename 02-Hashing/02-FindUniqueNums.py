# Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

from typing import List
import time

start_time = time.time()

class Solution:
    def findUniqueNums(self, nums: List[int]) -> List[int]:
        temp = set(nums)
        result = []
        for i in range(0, len(nums)):
            if (nums[i] + 1 not in temp) and (nums[i] - 1 not in temp):
                result.append(nums[i])
            else:
                temp.add(nums[i])
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 15]
    print(solution.findUniqueNums(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
