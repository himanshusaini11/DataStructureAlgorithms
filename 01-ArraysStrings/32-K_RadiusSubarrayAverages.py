from typing import List
import time

start_time = time.time()

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        left = right = s_w = 0
        result = [-1] * len(nums)
        if len(nums) < 2 * k + 1:
            return [-1] * len(nums)
        while right <= 2 * k:
            s_w += nums[right]
            right += 1
        for i in range(k, len(nums)-k):
            result[i] = s_w // (2 * k + 1)
            if right < len(nums):
                s_w = s_w - nums[left] + nums[right]
                left += 1
                right += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [40527,53696,10730,66491,62141,83909,78635,18560]
    k = 2
    print(solution.getAverages(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
