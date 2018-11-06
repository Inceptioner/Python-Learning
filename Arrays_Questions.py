# Array Questions

def even_odd(A):
    #   An array boot camp. Input an array of integers and reorder its entries 
    # so that the even entris appear first.
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

#   q1: If we can define a function to switch element of array, that might
# increase time complexity, since the array itself has index searching.


