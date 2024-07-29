from typing import List
import time
start_time = time.time()
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j in range(n-1, i, -1):
                    arr[j] = arr[j-1]
                arr[i] = 0
                i += 2
            else:
                i += 1
        return arr
                
if __name__ == "__main__":
    solution = Solution()
    #test_case = [1,0,2,3,0,4,5,0]
    test_case = [0,4,1,0,0,8,0,0,3]
    print (solution.duplicateZeros(test_case))
    print("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
