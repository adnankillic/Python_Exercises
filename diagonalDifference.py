# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1 +5+9= 15. The right to left diagonal = 3+5+9= 17. Their absolute difference is |15-17| = 2

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# arr = [[11,2,4], [4,5,6],[10,8,-12]]
# print(len(arr) -1 )


def diagonalDifference(arr):
    counter = 0
    left_array = []
    right_array = []
    
    for i in range(len(arr)):
        left_array.append(arr[counter][counter])
        counter += 1
    print(left_array)
    
    counter = 0
    counter2 = len(arr) -1
    
    for i in range(len(arr)):
        right_array.append(arr[counter][counter2])
        counter += 1
        counter2 -= 1
    print(right_array)
    
    return abs(sum(left_array) - sum(right_array))

