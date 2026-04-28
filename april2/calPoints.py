    
# for this problem, at first glance we will need an if else 
# for a bunch of operations that can happen. so adding to
# the record is push. C is pop. D is double so we take the value,
# then double it, then push it. + is popping the last two and
# then adding them.

# so what we have to do here is pop from the ops arry and add ...

# let me stop myself from that logic. im forgetting that the peek
# operation exists, which lets you look at it without popping it.

# also we arent popping or peeking from this list. we are iterating
# through the array and then adding the numbers to the
# record. if they are operations then we have to do some kind of
# peek or pop on the stack we create dthat has numbers in it

# AI help:
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        return sum(record)
    

# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
        
# for this problem, at first glance we will need an if else 
# for a bunch of operations that can happen. so adding to
# the record is push. C is pop. D is double so we take the value,
# then double it, then push it. + is popping the last two and
# then adding them.

# so what we have to do here is pop from the ops arry and add ...

# let me stop myself from that logic. im forgetting that the peek
# operation exists, which lets you look at it without popping it.

# AI help:

# Good question — I think the confusion is that you're mixing up two things:

# The operations list — this is your input. You just iterate through it left to right with a regular loop. You don't pop from it.

# The stack — this is a separate list that you create. This is your record of scores. This is what you push to, pop from, and peek at.

# Walk through your example with that mental model:

# ops = ["5", "D", "+", "C"]
# You create an empty stack: record = []
# Now iterate left to right through ops:

# "5" → it's a number, so push it → record = [5]
# "D" → peek at last in record (5), double it, push 10 → record = [5, 10]
# "+" → peek at last two (5 and 10), add them, push 15 → record = [5, 10, 15]
# "C" → pop last from record → record = [5, 10]
# Then return sum(record) → 15.

# something to ntoice is that instead of trying to do
# else -> then append the number. two things - 1, we need to remember
# to convert it to an int, becuase the "number" is actually a string
# if we did "5" + "4" wed get 54. so we do int(op) to convert it
# also we didnt do a check explicitly for if its an int. actually, this
# wouldnt even work becuase "5" is a string anyway. i just defaulted to 
# thinking about checking if op is int, but this wouldnt even work

# RECOGNIZING ITS A STACK
# A stack is perfect for this problem because each operation depends on the most recent scores. When we see +, we need the last two scores. When we see D, we need the last score. When we see C, we need to remove the last score. A stack gives us efficient access to these recent elements.