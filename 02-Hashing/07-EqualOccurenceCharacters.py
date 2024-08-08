"""
Example : Check if All Characters Have Equal Number of Occurrences
Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""

from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        frequencies = set(count.values())
        
        return len(frequencies) == 1

if __name__ == "__main__":
    solution = Solution()
    s = "abacbc"
    print(solution.areOccurrencesEqual(s))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
