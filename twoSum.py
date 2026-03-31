class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# BRUTE FORCE NESTED TWO POINTER SOLUTION
# initial thoughts:
# for this two sum problem, we want to find two numbers that equal to the target
# the brute force approach is for each number in the list, we can test every other number in the list to see if they add up to the target
# so we can use a nested for loop where we have i starting at 0 and then j starting at one after i, i+1 
# and then once j goes all the way to the end, we can increment i, and then the updated j will be i + 1 still
# when we find something that equals the target, we return the indices of the two numbers

# HASH MAP SOLUTION
# another way we can do this is by using a hash map
# we iterate through out list - in this case all the values will be the keys and all the values will be the number needed to reach the target
# so if our first number is 2 and our target is 9, then our value will be 7
# we then check if this value is any of the keys in our hash map, if it is, then we return the indices of the two numbers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


#enumerate() gives you both the index AND the value at the same time when looping.