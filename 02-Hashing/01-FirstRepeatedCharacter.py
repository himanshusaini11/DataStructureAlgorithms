from typing import List
import time

start_time = time.time()

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        temp = set()
        for c in s:
            if c in temp:
                return c
            else:
                temp.add(c)
        return None

if __name__ == "__main__":
    solution = Solution()
    s = "abdcade"
    print(solution.repeatedCharacter(s))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
