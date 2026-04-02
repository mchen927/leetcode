#Replace Elements With Greatest Element On Right Side
from typing import List

# we want to loop through this array, and for every index we want to check everything 
# to the right and see if theres anything bigger. it seems we have to compare
# the index with every number to the right. my initial thought is that we can
# set a currentMax and a maxMax. we go across every number to the right
# and keep gradually setting maxMax and evetnaully it will be the biggest number
# then we do arr[i] = maxCount and set it to that number. then we iterate through
# the loop, now were on the second index, etc. so we may need a double for
# loop here? and then we need to say if theres nothing else - which means were
# on the last index we sub it with -1 


# AI FEEDBACK

# Your logic is correct — that would produce the right answer. Double for loop, inner loop finds the max to the right, replace the element, last element gets -1. It works.

# But think about the time complexity of that approach. If the array has n elements, for each element you're scanning everything to its right. What does that add up to?

# And here's a nudge: you're recalculating a lot of the same information. When you find the max to the right of index 0, you already looked at every element. When you move to index 1, you scan almost all the same elements again. Is there a way to avoid that repeated work?

# Hint: What if you iterated in a different direction?


# Let's make it concrete. Take [17, 18, 5, 4, 6, 1]:

# What's the answer for each index?

# Index 5: greatest to the right = nothing = -1
# Index 4: greatest to the right = max of [1] = 1
# Index 3: greatest to the right = max of [6, 1] = 6
# Index 2: greatest to the right = max of [4, 6, 1] = 6
# Index 1: greatest to the right = max of [5, 4, 6, 1] = 6
# Index 0: greatest to the right = max of [18, 5, 4, 6, 1] = 18
# Now look at index 2. Its answer is max of [4, 6, 1] which is 6. But you could also write that as:

# max(arr[3], answer for index 3) = max(4, 6) = 6

# And index 1's answer is:

# max(arr[2], answer for index 2) = max(5, 6) = 6

# See? Each answer is just: "take the element one step to the right, and compare it to the already-computed answer one step to the right."

# That's what "depends on the one after it" means. Index 2's answer needs index 3's answer. Index 1's answer needs index 2's answer.

# So if you go right to left, by the time you get to index 2, you've already figured out index 3's answer and it's sitting in maxSoFar. You just reuse it. No re-scanning.

# If you went left to right, you'd get to index 0 first — but you don't have index 1's answer yet, so you'd have to scan the whole right side. That's the double loop.

# The direction you iterate is whichever direction lets you already have the answer you need.

# Tracing through [17, 18, 5, 4, 6, -1]:

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxSoFar
            maxSoFar = max(maxSoFar, temp)
        return arr


# 17 18 5 4 6 2


# walk me through everythign one mor etime and go step by step explaining the explanation and lgoic

# [17, 18, 5, 4, 6, 2], maxSoFar = -1

# i=5, arr[5] = 2

# We're at the last element. What's the biggest thing to its right? Nothing. And that's exactly what maxSoFar is right now: -1.

# Save: temp = 2. We grab the 2 because we're about to overwrite it, and the elements to the left will need to know about it later.

# Replace: arr[5] = -1. The last element always gets -1. Done with this element.

# Update: maxSoFar = max(-1, 2) = 2. Why? Because we're about to move to index 4, and the 2 that used to live at index 5 is to index 4's right. So it needs to be part of the max going forward.

# Array: [17, 18, 5, 4, 6, -1]

# i=4, arr[4] = 6

# What's the biggest thing to the right of index 4? maxSoFar says 2. That's correct — the only element to the right was 2.

# Save: temp = 6. Grab it before we lose it.

# Replace: arr[4] = 2. Index 4 now holds the greatest to its right. Done with this element.

# Update: maxSoFar = max(2, 6) = 6. Why? Because we're about to move to index 3, and the 6 that used to be at index 4 is to index 3's right. Is 6 bigger than the old max of 2? Yes. So the new max is 6.

# Array: [17, 18, 5, 4, 2, -1]

# i=3, arr[3] = 4

# What's the biggest thing to the right of index 3? maxSoFar says 6. Is that right? To the right of index 3 was 6, 2 — max is 6. Correct.

# Save: temp = 4.

# Replace: arr[3] = 6. Done with this element.

# Update: maxSoFar = max(6, 4) = 6. The 4 isn't bigger than 6, so max stays at 6. This makes sense — index 2 still has 6 as the biggest thing to its right.

# Array: [17, 18, 5, 6, 2, -1]

# i=2, arr[2] = 5

# What's the biggest thing to the right of index 2? maxSoFar says 6. To the right was 4, 6, 2 — max is 6. Correct.

# Save: temp = 5.

# Replace: arr[2] = 6. Done with this element.

# Update: maxSoFar = max(6, 5) = 6. 5 isn't bigger, max stays 6.

# Array: [17, 18, 6, 6, 2, -1]

# i=1, arr[1] = 18

# What's the biggest thing to the right of index 1? maxSoFar says 6. To the right was 5, 4, 6, 2 — max is 6. Correct.

# Save: temp = 18.

# Replace: arr[1] = 6. Done with this element.

# Update: maxSoFar = max(6, 18) = 18. Big change. The 18 is way bigger than 6. Why does this matter? Because we're about to visit index 0, and 18 is to index 0's right. It better be in maxSoFar.

# Array: [17, 6, 6, 6, 2, -1]

# i=0, arr[0] = 17

# What's the biggest thing to the right of index 0? maxSoFar says 18. To the right was 18, 5, 4, 6, 2 — max is 18. Correct.

# Save: temp = 17.

# Replace: arr[0] = 18. Done with this element.

# Update: maxSoFar = max(18, 17) = 18. Doesn't matter anymore since the loop is over, but the code doesn't need to special-case the last iteration.

# Array: [18, 6, 6, 6, 2, -1]

# Return [18, 6, 6, 6, 2, -1]

# Notice how every single step is the same three lines. No special cases, no if statements, no inner loops. Save, replace, update. Every time.





