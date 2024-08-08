from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def find_longest_substring(self, s: str, k: int) -> str:
        count = defaultdict(int)
        left = ans = 0
        for right in range(0, len(s)):
            count[s[right]] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "eceba"
    k = 2
    print(solution.find_longest_substring(s, k))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
