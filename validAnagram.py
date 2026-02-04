class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        newhashmap = {}

        for char in s:
            if char in newhashmap:
                newhashmap[char] += 1
            else:
                newhashmap[char] = 1

        for char in t:
            if char in newhashmap:
                newhashmap[char] -= 1
            else:
                newhashmap[char] = 1

        for value in newhashmap.values():
            if value != 0:
                return False

        return True


# for this problem, we want to check if two strings are anagrams of each other
# anagram means that the two strings have the same frequency of characters

# HASH MAP SOLUTION
# te first solution is since we know these two strings have to be the same length, we first test if theyre teh same length
# if not then we can instantly return false because they cannot be anagrams of each other
# if they are teh same lenght, we want to create a hashmap and we want to store the frequency of each char
# we loop through s and write down how many times each charactger appearfs
# we do the same for t
# we compare the hashmaps and if they are the same, then we return true
# if they are not the same, then we return false
# the time complexity is O(n) because we are iterating through the strings once
# the space complexity is O(n) because we are storing the frequency of each character in the hashmap which can contain up to n characters 
# if all the characters are different


# BRUTE FORCE TWO POINTER SOLUTION
# lets think about the brute force solution for this problem
# we can use a nested for loop to iterate through the strings
# we can use a for loop to iterate through s and a for loop to iterate through t
# we can use a nested for loop to iterate through the strings and compare the characters
# if the characters are the same, then we return true
# if the characters are not the same, then we return false
# the time complexity is O(n^2) because we are iterating through the strings twice
# the space complexity is O(1) because we are not storing any additional data
# this is because we are not using any additional data structures to store the characters

#-------------------------------------

# after looking at the solution, i see that we can also implement sorting also
# we can also use sorting for characters/strings. for the anagrams, it should be so that after we sort it the two strings should be teh same
# so we sort them and then compare
# if its equal then we return true, if not then we return false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

# also another way we can do it is the hashmap solution 
# essentially we want to make two hash maps - one for each string
# we want to iterate through each string and increase the frequency of each character count
# then once we finish iterating we compare the maps = if theyre equal then we return true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            # Count characters in s
            if s[i] in countS:
                countS[s[i]] = countS[s[i]] + 1
            else:
                countS[s[i]] = 1

            # Count characters in t
            if t[i] in countT:
                countT[t[i]] = countT[t[i]] + 1
            else:
                countT[t[i]] = 1

        return countS == countT