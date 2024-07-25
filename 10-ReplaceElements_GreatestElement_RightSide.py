from typing import List
import time

start_time = time.time()

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = max_val
            if arr[i] > max_val:
                max_val = arr[i]
            arr[i] = temp
        return arr

if __name__ == "__main__":
    solution = Solution()
    arr = [17,18,5,4,6,1]
    print(solution.replaceElements(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
