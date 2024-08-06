from typing import List
import time

start_time = time.time()

class Solution:
    def prefixSum(self, nums: List[int], queries: List[int], limit) -> List[bool]:
        curr = 0
        result = []
        ans = []
        for i in range(0, len(nums)):
            curr += nums[i]
            result.append(curr)
        for i in queries:
            if i[0] == 0 and result[i[1]] < limit:
                ans.append(True)
            elif result[i[1]] - result[i[0] - 1] < limit:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13
    print(solution.prefixSum(nums, queries, limit))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
