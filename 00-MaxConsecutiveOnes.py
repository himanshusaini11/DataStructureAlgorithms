##Max Consecutive Ones
### Example :
"""
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""
#Constraints:
"""
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s += 1
            if i == 0:
                s = 0
        return s
if __name__ == "__main__":
    solution = Solution()
    test_case = [1, 1, 0, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(test_case))  # Expected output: 3
