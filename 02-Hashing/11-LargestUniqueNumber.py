from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        # Count occurrences of each number
        for i in range(0, len(nums)):
            count[nums[i]] += 1
        
        # Find the largest unique number
        largest = -1
        for i in count:
            if count[i] == 1:
                largest = max(largest, i)
        return largest
        
if __name__ == "__main__":
    solution = Solution()
    nums = [5,7,3,9,4,9,8,3,1]
    print(solution.largestUniqueNumber(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
