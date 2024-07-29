from typing import List
import time

start_time = time.time()

class Solution:
    def check_if_sorted(self, arr: List[int]) -> str:
        if len(arr) <= 1:
            return str("Array sorted in ascending order.")
        
        a = True
        d = True
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                d = False
            
            if arr[i-1] > arr[i]:
                a = False
                
        if a:
            return str("Array sorted in acending order.")
        elif d:
            return str("Array sorted in decending order.")
        else:
            return str("Unsorted array.")
        

if __name__ == "__main__":
    solution = Solution()
    arr = [10, 1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.check_if_sorted(arr))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
