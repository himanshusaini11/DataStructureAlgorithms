from typing import List
import time

start_time = time.time()

class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

if __name__ == "__main__":
    solution = Solution()
    s = ["h","e","l","l","o"]
    print(solution.reverseString(s))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
