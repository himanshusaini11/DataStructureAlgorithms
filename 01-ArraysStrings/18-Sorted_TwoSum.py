from typing import List
import time

start_time = time.time()

class Solution:
    def check_for_target(self, arr: List[int], target: int) -> str:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            temp = arr[left] + arr[right]
            if temp == target:
                print (arr[left], arr[right])
                return True
            
            if temp > target:
                right -= 1
            else:
                left += 1
        return False
        

if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 4, 6, 8, 9, 14, 15]
    print(solution.check_for_target(arr, 13))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
