from typing import List
from collections import defaultdict
import time

start_time = time.time()

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        temp = defaultdict(int)
        
        for i in "balloon":
            count[i] += 1
        for i in text:
            temp[i] += 1

        min_balloons = float('inf')
        for i in count:
            min_balloons = min(min_balloons, temp[i] // count[i])
        
        return min_balloons
        
if __name__ == "__main__":
    solution = Solution()
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    print(solution.maxNumberOfBalloons(text))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
