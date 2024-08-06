from typing import List
import time

start_time = time.time()

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        """
        temp = set()
        
        if len(sentence) < 26:
            return False
        
        for i in sentence:
            if i not in temp:
                temp.add(i)
        
        if len(temp) == 26:
            return True
        else:
            return False
        """

if __name__ == "__main__":
    solution = Solution()
    sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
    print(solution.checkIfPangram(sentence))
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
