# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

from typing import List
import time

start_time = time.time()

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        return [-1, -1]
        

if __name__ == "__main__":
    solution = Solution()
    nums = [5, 2, 7, 10, 3, 9]
    target = 15
    print(solution.twoSum(nums, target))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
