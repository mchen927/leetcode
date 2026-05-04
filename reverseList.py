# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# to reverse a linked list theres brute force, iteration and recursion
# to brute force it we would make the linked list into an arry, reverse the array, and
# then make a loop that recreates the linked list, now reversed, from the array

# this is bad because space wise we need to create a new array size n to place the linked list it
# and also create the n amount of indiv nodes later on when converting the array back into a list

# when we reverse with iteration we want to think of it that we can flip the arrows that are currently 
# pointing forwards backwards. we need to keep into account a couple pointers. we need a pointer to 
# track the iteration of the nodes as keep going forward and keep flipping the arrows, which we are 
# changing what this node's next is pointing to. when we flip the arrows, were flipping them to point 
# backwards, which is the prev node. however the thing is lets say we have our current node, we flip it.
#  now its pointing backwards when is good. however we want to iterate to the next thing in the linked list
#   - but now the "next" thing is pointing backwards. what do we do? thus, we need to make sure we keep
#    track of the forward next iteration. so we do this by every time we are about to make the arrow flip,
#     before this we make a temp variable tracking what the next iteration is after we do the arrow flip

# one more thing is in the past i got confused whether to do x = y.next or y.next = x
# so for ex:
# curr.next = temp
# temp = curr.next

# so temp = curr.next means that we look at what curr.next's value or position is and point the variable temp to it. 

# curr.next = temp means that we want to point what curr's next is to where temp is right now. usualyl in this case we'd do curr.next = prev.
# we have the location of prev which is behind, and we say the next pointer of curr is pointing to prev now.


# AI EXPLANATION

# How I Think About This Problem
# Imagine a linked list as a chain of people in a line, each person pointing forward to the person in front of them.
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# Reversing means making every single person turn around and point at the person behind them instead. That's literally it. You're flipping arrows one at a time.
# The problem is: linked lists are a one-way street. When you're standing at node 2, you can see node 3 (your .next), but you have zero idea who's behind you. Node 1 is gone. So you need to carry that information with you manually. That's where the three pointers come in.
# The Three Pointers and Why Each One Exists
# pythonprev = None      # The node BEHIND the current one (starts as None because
#                  #   nothing comes before the head)

# curr = head      # The node you're currently working on

# next_node = ...  # A temporary save of curr.next BEFORE you overwrite it
# Think of it like this — you're a worker walking down the chain, and at each stop you do one job: flip this node's arrow to point backward. But the moment you flip curr.next to point at prev, you've destroyed your only link forward. You lose access to the rest of the list. So you need to save curr.next in a temp variable before you cut the wire. That's next_node.
# So every single iteration is four steps in this exact order:
# 1. Save what's ahead        (next_node = curr.next)
# 2. Flip the arrow backward  (curr.next = prev)
# 3. Advance prev             (prev = curr)
# 4. Advance curr             (curr = next_node)
# That's the entire algorithm. Four lines, repeated until curr is None.

# The Mental Model I Always Come Back To
# I think of it as a zipper. At any point during the algorithm, the list is split into two parts:
# REVERSED (built backward from prev)    UNREVERSED (from curr onward)

# None <- 1 <- 2 <- 3                   4 -> 5 -> None
#                    ↑                   ↑
#                   prev                curr

# Each iteration "unzips" one node from the unreversed side and "zips" it onto the reversed side. When the unreversed side is empty, you're done.
# Why This Is the Best Solution
# ApproachTimeSpaceWhy the space costBrute force (array)O(n)O(n)Storing all values in an arrayRecursiveO(n)O(n)Call stack goes n frames deepIterativeO(n)O(1)Only 3 pointers, no matter how long the list
# The iterative version uses constant extra space — just prev, curr, and next_node. Doesn't matter if the list has 5 nodes or 5 million. That's why interviewers consider it the optimal solution.
# One Last Thing — The "Why This Order" Question
# A common mistake is swapping the order of the four steps. The order is rigid and here's why:
# You must save next_node before flipping curr.next, because flipping destroys your forward path. And you must move prev before moving curr, because prev needs to land on curr's current position 
# (not wherever curr is about to go). Think of it as two pairs: save then flip, advance prev then advance curr.