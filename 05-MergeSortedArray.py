from typing import List
import time
start_time = time.time()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums 1, m, num2, n
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif m != 0 and n != 0:
            ptr = 0
            for i in range(m, len(nums1)):
                nums1[i] = nums2[ptr]
                ptr += 1
            str_ptr = 0
            end_ptr = m+n-1
            
            for i in range(0, len(nums1)):
                for j in range(i, len(nums1)):
                    temp = nums1[i]
                    if nums1[j] < nums1[i]:
                        nums1[i] = nums1[j]
                        nums1[j] = temp
        return nums1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    print (solution.merge(nums1, m, nums2, n))
    print ("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")
