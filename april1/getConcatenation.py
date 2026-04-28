class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(2 * n):
            ans[i] = nums[i % n]
        return ans
        
#INITIAL APPROACH

# so for this problem we want to kind of repeat the nums array twice
# the first thing we need to do is create an array ans thats length
# of 2n and it will be empty. we will have to populate through this
# array. so lets see. we want the same val at index

# 1 4 1 2 1 4 1 2
# 0 1 2 3 4 5 6 7

# 0, 4 - 0 mod length = 0, 4 mod length = 0
# 1, 5 - 1 mod length = 1, 5 mod length = 1
# 2, 6 - 2 mod length = 2, 6 mod length = 2
# 3, 7


# 1 3 2 1 3 2
# 0 1 2 3 4 5

# 0, 3
# 1, 4
# 2, 5

# we know that the logic will have to do with some kind of math
# and that its dependent on length? 

# for i from index 0 to length:

# i found the math. its the remainder/mod. we know that after each
# length passby of the new array, we will reach the same number. so 
# after the length passes again, were starting at 0. so we mod by the 
# length and it should be the same.

# kind of a bad explanation lol

#AI HELP
# One question for you: the mod approach works great, but is there an even simpler way to think about this problem? What if you didn't need any math at all — what operation could you do to nums directly to get the result?

#TIP TO REMMEBER

# The intuition behind mod you should internalize:

# Mod is the "wrapping around" operator. Whenever you need something to cycle or repeat, think mod. Picture a clock — after 12, it doesn't go to 13, it wraps back to 1. That's mod. Here, you have 3 values and you want them to repeat. Once your index hits 3, you need it to "wrap" back to 0. That's exactly what i % n does — it keeps the index cycling through 0, 1, 2, 0, 1, 2. So the mental trigger is: "I need a pattern to repeat" → mod.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# you can also do nums + nums. in python + join two lists end to end

