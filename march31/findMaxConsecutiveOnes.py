from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount = 0
        currentCount = 0

        for num in nums: 
            if num == 1:
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
            else: 
                currentCount = 0
    
        return maxCount
    
    

# INITIAL THOUGHTS
# we make a global variable totalCount = 0. this is because we need to update this every time we see a bigger
# count iteration. we also need to write somewhere to replace the global count if the temp count ends - which 
# would be the case if the next number isn't 1 anymore and then set the new global count as the old temp count

#AFTER
#so the way i coded it tests which is bigger - currentCount or maxCount simply with an if statement. however
# the way leetcode does it is they use the max function, see below. however, my way is correct also. just
# keep in mind we can use the max function for something like this

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # This is your "global variable totalCount"
        current_count = 0  # This is your temporary counter
        
        for num in nums:
            if num == 1:
                # Increment current streak
                current_count += 1
                # Update max if current streak is larger
                max_count = max(max_count, current_count)
            else:
                # Reset current streak when we see 0
                current_count = 0
        
        return max_count

#INTUITION 
# How to think about this problem step by step:

# Recognize it's a "streak" problem. You're looking for the longest consecutive run of a value. Anytime you hear "consecutive," think: "I need to track a current streak and a best streak."

# What resets the streak? Seeing a 0. That tells you the else branch just sets currentCount = 0.

# What extends the streak? Seeing a 1. Increment the counter.

# When do you update the best? Every time you extend the streak, check if it's the new best. You did this with if currentCount > maxCount — totally valid. The LeetCode version uses max() which is just a shorter way to write the same logic.

# What do you return? The best streak you ever saw.

# That's the whole mental model: track, reset, compare.