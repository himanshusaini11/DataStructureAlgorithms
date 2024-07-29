from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int], n) -> int:
        s = 0
        max_num = 0
        for i in nums:
            if i == n:
                s += 1
                if max_num <= s:
                    max_num = s
            else:
                s = 0
        return max_num
if __name__ == "__main__":
    solution = Solution()
    test_case = [1, 2, 3, 3, 4, 1, 2, 7, 8, 4, 9, 9, 2, 3, 6, 6, 6, 6, 6, 0, 0, 1, 2, 3, 4]
    print(solution.findMaxConsecutiveOnes(test_case, 0))
