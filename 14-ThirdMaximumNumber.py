from typing import List
import time

start_time = time.time()

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif first > num > second:
                second, third = num, second
            elif second > num > third:
                third = num
        
        return third if third != float('-inf') else first

if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 2, 5, 3, 5]
    print(solution.thirdMax(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
