"""
The following implementation of the Insertion Sort Algorithm is used to sort an array in ascending order and has a time compelxity of O(n^2). 

"""

# Define the funciton
def insertionSort (A):

    # Start iterating from the second element onwards
    for i in range(1, len(A)):
        
        # Store the value of the current element
        val = A[i]
        
        # Let j be the index of the previous element
        j = i - 1
        
        # Start iterating backward from j till 0, until the jth value becomes lesser than the current ith value
        while (j >= 0) and (A[j] > val):
            
            # Since the jth element is still greater than the current one, shift the jth element to the right, to the j+1th position.
            A[j+1] = A[j]
            
            # Now move on to the element before the jth one, and check whether that too is greater than the current one.
            j = j - 1
            
        # If the jth element is smaller than current one, the while will break, and we can set the element after the jth one, as the current val.
        A[j+1] = val

    #We can print our sorted array now
    return print(A)
