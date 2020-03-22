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

class TwoSum(object):
 
    def __init__(self):
        self.nums = []
        self.sums = {}

    def add(self, number):
        for i in self.nums:
            self.sums[i + number] = 1
        self.nums.append(number)

    def find(self, value):
        return value in self.sums

        

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