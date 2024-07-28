# Problem Statement
## Given an array of integers where ```1 ≤ a[i] ≤ n``` (n = size of array), some elements appear twice and others appear once. Find all the elements of ```[1, n]``` inclusive that do not appear in this array.

```
Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
```

## Solution Explanation

### Marking Phase:
The idea is to use the indices of the array to mark the presence of numbers. For each number ```nums[i]```, we calculate the corresponding index as ```abs(nums[i]) - 1``` and mark the element at this index as negative. This marking will help us identify which numbers are present in the array.

### Collection Phase:
After marking the presence of numbers, we iterate through the array again. If any element is still positive, it means the ```index + 1``` (because of 0-based indexing) is missing in the array.

Let's take the example array ```arr = [4, 3, 2, 7, 8, 2, 3, 1]```.
```
Initial Array
Index:  0  1  2  3  4  5  6  7
Array: [4, 3, 2, 7, 8, 2, 3, 1]
Marking Phase
We iterate through each element in the array and mark the corresponding index as negative.

For i = 0, nums[0] = 4, index to mark = 4 - 1 = 3
Mark nums[3] as negative: [4, 3, 2, -7, 8, 2, 3, 1]

For i = 1, nums[1] = 3, index to mark = 3 - 1 = 2
Mark nums[2] as negative: [4, 3, -2, -7, 8, 2, 3, 1]

For i = 2, nums[2] = -2 (already marked), index to mark = 2 - 1 = 1
Mark nums[1] as negative: [4, -3, -2, -7, 8, 2, 3, 1]

For i = 3, nums[3] = -7 (already marked), index to mark = 7 - 1 = 6
Mark nums[6] as negative: [4, -3, -2, -7, 8, 2, -3, 1]

For i = 4, nums[4] = 8, index to mark = 8 - 1 = 7
Mark nums[7] as negative: [4, -3, -2, -7, 8, 2, -3, -1]

For i = 5, nums[5] = 2, index to mark = 2 - 1 = 1
nums[1] is already negative

For i = 6, nums[6] = -3 (already marked), index to mark = 3 - 1 = 2
nums[2] is already negative

For i = 7, nums[7] = -1 (already marked), index to mark = 1 - 1 = 0
Mark nums[0] as negative: [-4, -3, -2, -7, 8, 2, -3, -1]

Final Marked Array
Index:  0  1  2  3  4  5  6  7
Array: [-4, -3, -2, -7, 8, 2, -3, -1]

Collection Phase
Now, we iterate through the array again. If an element is positive, it means the index + 1 is missing.

For i = 0, nums[0] = -4 (negative)
For i = 1, nums[1] = -3 (negative)
For i = 2, nums[2] = -2 (negative)
For i = 3, nums[3] = -7 (negative)
For i = 4, nums[4] = 8 (positive), missing number = 5
For i = 5, nums[5] = 2 (positive), missing number = 6
For i = 6, nums[6] = -3 (negative)
For i = 7, nums[7] = -1 (negative)
Missing numbers are [5, 6].
```
~~~python
from typing import List
import time

start_time = time.time()

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Marking Phase
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Calculate the corresponding index
            nums[index] = -abs(nums[index])  # Mark as negative
        
        # Collection Phase
        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]  # Collect positive indices
        
        return result

if __name__ == "__main__":
    solution = Solution()
    arr = [4,3,2,7,8,2,3,1]
    print(solution.findDisappearedNumbers(arr))  # Output: [5, 6]
    print("The time of execution of above program is:", (time.time() - start_time) * 10**3, "ms")
~~~

```
Time Complexity
Marking Phase: O(n) because we iterate through the array once.
Collection Phase: O(n) because we iterate through the array again.
Overall Time Complexity: O(n)
Space Complexity
No extra space used other than the result list.
Overall Space Complexity: O(1) (excluding the output list)
This solution efficiently finds the disappeared numbers in O(n) time complexity and O(1) space complexity.
```

#### Reference : This explaination was generated using ChatGPT-4o
