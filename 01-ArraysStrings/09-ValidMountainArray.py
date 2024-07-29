# First attempt
from typing import List
import time

start_time = time.time()

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        temp = []
        if len(arr) < 3:
            return False
        else:
            for i in range(0, len(arr)-1):
                if arr[i+1] - arr[i] > 0:
                    temp.append(1)
                elif arr[i+1] - arr[i] == 0:
                    return False
                else:
                    temp.append(0)
        count = 0
        for i in range(0, len(temp)-1):
            if temp[i+1] - temp[i] == -1:
                count += 1
            elif temp[i+1] - temp[i] == 1:
                return False
        if count == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    arr = [0, 3, 2, 1]
    print (solution.validMountainArray(arr))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
  

# Second attempt with the help of internet.
"""
from typing import List
import time

start_time = time.time()

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1    
        if i == 1 or i == len(arr):
            return False
        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1
        return i == len(arr)

if __name__ == "__main__":
    solution = Solution()
    arr = [3, 5, 5]
    print (solution.validMountainArray(arr))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
"""
