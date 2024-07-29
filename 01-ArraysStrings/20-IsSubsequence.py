from typing import List
import time

start_time = time.time()

class Solution:
    def isSubsequence(self, s1: str, s2: str) -> bool:
        s1_ptr = 0
        s2_ptr = 0

        while s1_ptr < len(s1) and s2_ptr < len(s2):
            if s2[s2_ptr] == s1[s1_ptr]:
                s2_ptr += 1
            else:
                s1_ptr += 1
                
        return s2_ptr == len(s2)

if __name__ == "__main__":
    solution = Solution()
    s1 = "abcde"
    s2 = "ade"
    print(solution.isSubsequence(s1, s2))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
