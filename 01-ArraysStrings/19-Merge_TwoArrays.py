from typing import List
import time

start_time = time.time()

class Solution:
    def combine(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    arr1 = [1, 2, 4]
    arr2 = [3, 5, 6]
    print(solution.combine(arr1, arr2))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
