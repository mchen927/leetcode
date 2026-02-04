class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set  ()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                 if nums[i] == nums[j]:
                    return True

        return False

class Solutrion:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num.sort()

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False


# SET SOLUTION
# we can use a set to store the numbers we have seen so far
# then we use a for loop to iterate through the list and check if the number is in the set
# if not in the set, we add it to the set
# if it is in the set, we return treu because it is a duplicate
# remember, sets cannot contain duplicates, you only have one of each number in a set
# this time complexity is O(n) is because we are iterating through the list once and checking if the
# number is in the set is O(1) time complexity
# the space complexity is O(n) because we are storing the numbers in the set
# this is because the set can contain up to n numbers if all the numbers are different

# BRUTE FORCE NESTED TWO POINTER SOLUTION
# the brute force solution is to use a nested for loop to iterate through the list
# we have a first for loop at i = 0 and the second one at j = 1 - we want to check from j = 1 to the end of the list
# if any of them equal i  then it is a duplicate and we return true
# we then iterate i to 1, and j will always be i + 1
# this time complexity is O(n^2) because we are iterating thjrough the list n * n times
# the space complexity is O(1) because we are not storing any additional data

# SORTED SINGLE POINTER SOLUTION
# another way we can do it is by sorting the list and doing a single linear scan through the list
# we know if we sort it, if we do have duplicatges, they will be next to each other
# so we sort, tghen iterate throughj the list starting from i = 1 and check everything before it
# additionally we can start from i = 0 and check i + 1 for the linear scan, making sure we stop at one before the last index
# so we dont go out of bounds, becaused i+1 will be the last index
# the time complexity is O(n log n) because we are sorting the list and then iterating through the list
# most sorting algorithms are O(n log n) time complexity and iterating through the list is O(n) time complexity
# so when you add those together, you get O(n log n) time complexity
# the space complexity is O(1) because we are not storing any additional data
# this is because we are sorting the list in place and not creating any new lists
# this is because we are not using any additional data structures to store the numbers