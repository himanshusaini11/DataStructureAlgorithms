from typing import List
import time

start_time = time.time()

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> List[bool]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        ans = 0
        for i in range(0, len(nums) - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            
            if left_section > right_section:
                ans += 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [10, 4, -8, 7]
    print(solution.waysToSplitArray(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
