from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_dict = defaultdict(int)
        loser_dict = defaultdict(int)
        ans = [[], []]
        
        # Count wins and losses for each player
        for i in matches:
            winner_dict[i[0]] += 1
            loser_dict[i[1]] += 1
        
        # Find players with wins but no losses
        for i in winner_dict:
            if i not in loser_dict:
                ans[0].append(i)
        
        # Find players with exactly one loss
        for i in loser_dict:
            if loser_dict[i] == 1:
                ans[1].append(i)
                
        # Sort the result lists
        ans[0].sort()
        ans[1].sort()
        
        return ans
        
if __name__ == "__main__":
    solution = Solution()
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    print(solution.findWinners(matches))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
