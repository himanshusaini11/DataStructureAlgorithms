from typing import List
import time

start_time = time.time()

class Solution:
    def maxConsecutiveOnes3(self, nums: List[int], k: int) -> float:
        curr = 0
        left = 0
        ans = 0
        for right in range(0, len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left +1)
        return ans
        

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(solution.maxConsecutiveOnes3(nums, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
