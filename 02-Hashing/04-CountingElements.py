from typing import List
import time

start_time = time.time()

class Solution:
    def countElements(self, arr: List[int]) -> int:
        temp = set(arr)
        count = 0
        for i in range(0, len(arr)):
            if arr[i] + 1 in temp:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,3,3,5,5,7,7]
    print(solution.countElements(nums))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
