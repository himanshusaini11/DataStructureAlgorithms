from typing import List
import time

start_time = time.time()

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            if not arr:
                return False
            else:
                for j in range(0, len(arr)):
                    if arr[i] == 2 * arr[j] and i!= j:
                        return True
        return False

if __name__ == "__main__":
    solution = Solution()
    arr = [10,2,5,3]
    print (solution.checkIfExist(arr))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")

"""
from typing import List
import time

start_time = time.time()

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp = []
        for i in arr:
            if i*2 in temp or i/2 in temp:
                return True
            else:
                temp.append(i)
        return False

if __name__ == "__main__":
    solution = Solution()
    arr = [10,2,5,3]
    print (solution.checkIfExist(arr))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
"""

"""
from typing import List
import time

start_time = time.time()

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp = set()
        for i in arr:
            if i*2 in temp or i / 2 in temp:
                return True
            temp.add(i)
        return False

if __name__ == "__main__":
    solution = Solution()
    arr = [10,2,5,3]
    print (solution.checkIfExist(arr))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
"""
