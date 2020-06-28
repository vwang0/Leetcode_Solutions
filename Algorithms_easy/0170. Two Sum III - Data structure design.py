"""
170. Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

class TwoSum:    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.is_sorted = False
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.is_sorted:
            self.nums.sort()
        dict1 = {}
        for i, num in enumerate(self.nums):
            if value - num in dict1.keys():
                return True
            else:
                dict1[num] = i
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

        

class TwoSum(object):

    def __init__(self):
        self.nums = []

    def add(self, number):
            nums = self.nums

            low, high, index = 0, len(nums) - 1, len(nums)
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] < number:
                    low = mid + 1
                else:
                    if (mid == 0) or (mid > 0 and nums[mid - 1] < number):
                        index = mid
                        break
                    high = mid - 1

            nums.insert(index, number)

    def find(self, value):
        nums = self.nums
        low, high = 0, len(nums) - 1

        while low < high:
            s = nums[low] + nums[high]
            if s < value:
                low += 1
            elif s > value:
                high -= 1
            else:
                return True

        return False