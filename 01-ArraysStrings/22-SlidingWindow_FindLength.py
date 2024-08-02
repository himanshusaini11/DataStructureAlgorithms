from typing import List
import time

start_time = time.time()

class Solution:
    def findLength(self, arr: List[int], k: int) -> int:
        left = 0
        curr = 0
        length = 0
        for right in range(0, len(arr)):
            curr += arr[right]
            while curr > k:
                curr -= arr[left]
                left += 1
            length = max(length, right-left+1)
        return length

if __name__ == "__main__":
    solution = Solution()
    arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    k = 8
    print(solution.findLength(arr, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
