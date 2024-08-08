from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        result = []
        for i in nums:
            for j in i:
                count[j] += 1
        
        for key, val in count.items():
            if val == len(nums):
                result.append(key)
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    print(solution.intersection(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
