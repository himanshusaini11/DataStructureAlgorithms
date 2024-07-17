from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            if len(str(i))%2 == 0:
                s += 1
        return s
      
if __name__ == "__main__":
    solution = Solution()
    test_case = [12,345,2,6,7896, 12124578, 12458, 11254215, 112255448899]
    print (solution.findNumbers(test_case))
