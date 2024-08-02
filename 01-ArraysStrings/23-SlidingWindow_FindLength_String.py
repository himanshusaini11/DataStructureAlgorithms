from typing import List
import time

start_time = time.time()

class Solution:
    def findLength(self, arr: str) -> int:
        left = 0
        curr = 0
        length = 0
        for right in range(0, len(arr)):
            if arr[right] == "0":
                curr += 1
            
            while curr > 1:
                if arr[left] == "0":
                    curr -= 1
                left += 1
            length = max(length, right - left + 1)
        return length

if __name__ == "__main__":
    solution = Solution()
    arr = "1101100111"
    print(solution.findLength(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
