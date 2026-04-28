class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in match:
                if not stack or stack[-1] != match[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0




# if char == ')':
#     if not stack or stack[-1] != '(':
#         return False
#     stack.pop()
# elif char == ']':
#     if not stack or stack[-1] != '[':
#         return False
#     stack.pop()
# elif char == '}':
#     if not stack or stack[-1] != '{':
#         return False
#     stack.pop()
# else:
#     stack.append(char)

# to be honest every time i see this problem i forget how to do it
# the most obvious thing is that we need to iterate through the list 
# and do some kind of matching. we need to match the beginning to the 
# end ex a { to a }. 

# ai explanation
# however you have to remember in an ideal world, if the string is in
# fact valid, then all the initial will be opening brackets, and all 
# the latter ones will be closing brackets. so then we need to decide 
# what we do when we iterate. when we iterate it will first most likely
# be opening brackets. what do we do for an open bracket? we just add it 
# to a stack. now the bulk of our logic comes from the closing brackets.
# what happens when we come across a closed bracket? 
 
#  so instead of thinking about every single closed bracket, lets think
#  about what happens at the first instnace. so we add all the opening 
#  brackets into our stack. it looks like this now

#  { [ 

# then now in our string, we have ] } left. we go to ]. obviously this is 
# correct and it is the closing string. the correlation is that
# the first closing string we see should be matches the top of the stack.
# weve been putting all the opening brackets in the stack. and so once we 
# reach the first end bracket, it should match with the top of the stack, 
# aka the most recent one.

# then we pop this pair. now the new top of the stack will be the second to
# last one. and then when we iterate and if the string is valid, the closing 
# bracket now should match the new stack after we popped .