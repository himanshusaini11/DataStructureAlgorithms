from typing import List
import time
start_time = time.time()
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums) - 1
        result = [0] * len(nums)
        result_pointer =  len(nums) - 1
        
        while left_pointer <= right_pointer:
            sqr_left = nums[left_pointer]**2
            sqr_right = nums[right_pointer]**2
            if sqr_left > sqr_right:
                result[result_pointer] = sqr_left
                left_pointer += 1
                result_pointer -= 1
            else:
                result[result_pointer] = sqr_right
                right_pointer -= 1
                result_pointer -= 1
        
        return result
        
if __name__ == "__main__":
    solution = Solution()
    test_case = [-4,-1,0,3,10]
    print (solution.sortedSquares(test_case))
    print("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")

"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_nums = [i**2 for i in nums]
        for i in range(0, len(sqr_nums)):
            for j in range(i+1, len(sqr_nums)):
                if sqr_nums[i] >= sqr_nums[j]:
                    temp = sqr_nums[i]
                    sqr_nums[i] = sqr_nums[j]
                    sqr_nums[j] = temp
        return sqr_nums
"""
