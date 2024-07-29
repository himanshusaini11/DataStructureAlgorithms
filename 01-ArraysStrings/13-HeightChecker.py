from typing import List
import time

start_time = time.time()

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        count = 0
        for i in range(0, len(expected)):
            for j in range(i, len(expected)):
                if expected[j] < expected[i]:
                    expected[i], expected[j] = expected[j], expected[i]
                    
        for i in range(0, len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    heights = [1,1,4,2,1,3]
    print(solution.heightChecker(heights))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
