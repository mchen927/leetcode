READING FROM AN ARRAY
-accessing a single element in an array is always instant because each index of myArray is mapped to an address in the RAM
-O(1) time complexity

TRAVERSING THROUGH AN ARRAY
-we can also read all values within an array by traversing through it 

for i in range(len(myArray)):
    print(myArray[i])

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1

last element is always n - 1 where n is the size of the array. if our array is size 3 the last accessible index is 2.

to traverse through an array of size n the time complexity ity O(n). the number of operations grows linearly with the size of the array. for example, with an array of size 10 we would have to perform 10 operations to traverse through it, with an array of size 100 we would have to perform 100 operations, and so on.

DELETING FROM AN ARRAY
from the end -
from the middle - 
notice that deleting from the end of an array doesnt make it non contigious but deleting from the middle will

a better approach is to look at index that is deleted i and start from i+1. then starting from i+1 to the end of the array and shift every position left. we can even replace the last element with a 0 or null and decrease the length by 1. 

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted

- remember that range doesnt include the last one, so instead of going to length it goes to length - 1, which is the last element

- the worst case would be that we need to shift all of the elements to the left. This would occur if the target index is the first index of the array. Therefore, the code above is O(n)


INSERTION AT THE END

If we want to insert an element at the end of the array, we can simply insert it at the next open position which will be at index length where length is the number of elements in the array.

remember last element is n = length-1 so next available space will be n = length

def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

were doing the same operation every time, just writing a single value to the end of the array, so the time complexirt is O(1)



INSERTING AT THE ITH INDEX

inserting at random index i is more complicated since it can be inserted into the middle of the array

Consider the array [4, 5, 6]. If we need to insert at index i = 1, or i = 0, we cannot overwrite the original value because we would lose it. Instead, we will need to shift all values, starting at index i, one position to the right. Below is the code and visual demonstrating this.

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.

def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    # Insert at i
    arr[i] = n

for inserting into the middle - lets think about this
we want to keep the space that we want to insert, which is n, free. right now its occupied. 

Why backwards works:

When you go from length-1 down to i, you move the "last" element first into the empty slot, then the second-to-last into where the last was, etc. Each element moves into a spot that's already been vacated.

arr = [1, 2, 3, 4, _]   insert at i=1
                   ^start here
Step 1: arr[4] = arr[3]  →  [1, 2, 3, 4, 4]
Step 2: arr[3] = arr[2]  →  [1, 2, 3, 3, 4]
Step 3: arr[2] = arr[1]  →  [1, 2, 2, 3, 4]
Now insert: arr[1] = n   →  [1, n, 2, 3, 4]  ✓
Why forwards fails:

You overwrite values before copying them. Each step destroys the data you need for the next step.

The principle: When shifting elements in one direction, you need to start from the opposite end to avoid clobbering data. Same idea applies to deleting (shift left → start from the deletion point going forward).


Think of it this way: always move toward the empty space.

Insert: Empty space is at the end → move backward toward it
Delete: Empty space is where you deleted → move forward from there, pulling elements into the gap

so if insert (shifting right) - start from end and go right to left
so if delete (shift left) - start from index and go left to right