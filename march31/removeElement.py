from typing import List

#INITIAZL THOUGHTS

# we iterate over this and see val. what do we do?
# i would think that we need a way to get rid of the 2s here. one way im
# thinking is that we can swap values and move it to the end? or somewhere
# else in the array? 
# so once we see the 2 we stop - because we actually want that to be something
# else. im thinking we need another pointer to keep track of the next number thats
# actually not 2 or whatever the val is, and then swap its value with
# wherever our val is 
# so what happens after the swap? we have to iterate right after, right, because
# our i is still pointing to a value that has been swapped already. we want to point
# it to the next available spot. so we increment i
# then we check again, is the number at index i the val 2? it is. so then we
# look at j. before we didnt run into this issue of j being the same as index i
# so im assuming we have to iterate j until we reach a non val num
# so we switch 0 and 2. then we repeat after the switcheroo and iterate i. i think
# we have to iterate j also? so now we see i  is 2 again. switch time .
# then we iterate i and j both. looks like j reached the end. i think this is 
# a condition we haev to take in - as long as j doesnt reach the end. 
# then we return where i is. we want the legnth so we return index i. `

# FIRST CODE ITERATION


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0

        for i in range(len(nums))
            if nums[i] != val:
                j += 1
            else:
                for j in range(i+1, length):
                    if nums[j] == val:
                        j += 1
                    else:
                        nums[i] = nums[j]
        
        return i

# POST INITIAL CODE THOUGHTS / ANALYSIS

# The key insight: Instead of finding vals and swapping them away, think about it as collecting the good values and writing them to the front.

# You only need two things:

# i — scans through every element
# k — tracks where to write the next valid element
# Walkthrough with [0, 1, 2, 2, 2, 3, 0, 4, 2], val = 2:


# k=0  i=0: nums[0] is 0, not val → write 0 at position k → nums[0]=0, k becomes 1
# k=1  i=1: nums[1] is 1, not val → write 1 at position k → nums[1]=1, k becomes 2
# k=2  i=2: nums[2] is 2, IS val  → skip, do nothing
# k=2  i=3: nums[3] is 2, IS val  → skip, do nothing
# k=2  i=4: nums[4] is 2, IS val  → skip, do nothing
# k=2  i=5: nums[5] is 3, not val → write 3 at position k → nums[2]=3, k becomes 3
# k=3  i=6: nums[6] is 0, not val → write 0 at position k → nums[3]=0, k becomes 4
# k=4  i=7: nums[7] is 4, not val → write 4 at position k → nums[4]=4, k becomes 5
# k=5  i=8: nums[8] is 2, IS val  → skip, do nothing
# Done! Array is now [0, 1, 3, 0, 4, ...] and k = 5. Return k.

# How this differs from your code:

# You were trying to find a val, then scan ahead for a non-val, then swap. That needed an inner loop, a scan-ahead pointer, and break logic — lots of moving parts.
# This approach flips it: just scan everything with i, and when it's not val, copy it forward to k. No inner loop, no swapping, no scan-ahead.
# The pseudocode is just:

# k = 0
# for each index i:
#     if nums[i] is not val:
#         write nums[i] at position k
#         increment k
# return k



# we are given a problem where we have to get rid of the occurences of
# val. my first thought is some kind of deletion problem, where we pass
# through the array and delete the instances of val that we see

# 0 1 2 2 2 3 0 4 2
#     i     j
# 0 1 3 2 2 2 0 4 2
#     i     j
# 0 1 3 2 2 2 0 4 2
#       i   j
# 0 1 3 2 2 2 0 4 2
#       i     j
# 0 1 3 0 2 2 2 4 2
#       i     j
# 0 1 3 0 2 2 2 4 2
#         i     j
# 0 1 3 0 4 2 2 2 2
#           i     j


#SOLUTION
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
                

#  for my approach i was using the for loop to find val and then try to find something to replace it with.
#  however, the way i should have though about it is if you see val, justy iterate over it and use another
#  variable to keep track of the next placement of val. and use the value at i to swap where the val is


# Exactly. That's the mental shift. Your approach was:

# "Stop at the bad, then go find something good to fix it with"
# The cleaner approach is:

# "Stop at the good, and place it where it belongs"
# Both approaches work, but the second one is simpler because you only need to act on one condition. The bad elements? You don't do anything with them — you just let i walk right past them. They get overwritten later when a good value lands on their spot.

# That's the key flip. Instead of "find problem, fix problem," it's "find good stuff, collect it."

# Almost — just one tweak. You said "use another variable to keep track of val." It's more like k keeps track of where the next good value should go, not where val is.

# To put it more precisely:

# i visits every element
# If nums[i] is not val, copy it to nums[k] and advance k
# If nums[i] is val, just keep going — don't do anything with k
# k always points to the next open slot for a good value
# So k isn't tracking val — it's tracking the boundary between "done" and "not done yet". Everything before k is your clean, val-free result.


# when you first see this problem, how would u think about it?



# how would u know that u want to chcekc if nums[i] = val or nums[i] != val

# Great question. Here's how I'd think about it from the very start:

# Step 1: What does the problem actually want?

# It wants the first k elements of the array to be all the non-val elements. It doesn't care about what comes after, and it doesn't care about order.

# Step 2: So what am I really building?

# A smaller array at the front of nums that only has the good stuff. I'm essentially filtering.

# Step 3: How do I filter an array?

# If I were building a brand new list, I'd do something like:

# result = []
# for num in nums:
#     if num != val:
#         result.append(num)
# That's the most natural way to think about filtering — you check for what you want to keep, not what you want to throw away. You don't write if num == val: skip. You write if num != val: keep it.

# Step 4: But the problem says do it in-place.

# So instead of result.append(num), I need a pointer k that acts like the end of my "result" array inside nums. Writing to nums[k] and incrementing k is the in-place version of append.

# That's the whole thought process. The reason you check != val instead of == val is because the more natural question is "what do I keep?" not "what do I remove?" You're building a result, not destroying elements.

# so how would u know that you have to do this                 nums[k] = nums[i] - for if your index val at i is not val.



# because its not intuitive to me, as say when i = 0 and k = 0 then were swapping teh same thing.

# Forget about i = 0, k = 0 for a second. That's the boring case. Think about the case that matters:

# What if the array is [2, 3, 4] and val = 2?

# 2  3  4
# k
# i
# i = 0, it's val. Skip. Only i moves:

# 2  3  4
# k
#    i
# Now i = 1, it's 3 — a good value. But 3 is sitting at index 1, and your result needs to start at index 0. The good value is in the wrong place. How do you fix that?

# nums[k] = nums[i] — put the 3 where it belongs:

# 3  3  4
# k
#    i
# That's why you need nums[k] = nums[i]. It moves good values forward to fill the gaps left by vals.

# The i = 0, k = 0 case where nothing happens is just a side effect of the code being general. It's not the case the line was designed for. It was designed for exactly the situation above — when a good value is stranded behind a val and needs to be pulled forward.

# So don't think about it as "swapping the same thing." Think about it as: "when k falls behind i, good values need to be copied to the front." The fact that it also runs when k == i is just the code not bothering to check — because checking would add complexity for no benefit.