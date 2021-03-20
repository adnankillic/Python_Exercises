# Problem
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of 
# each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with 
# absolute error of up to  are acceptable.

arr = [-4,3,-9,0,4,1]

def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)
    
    print("%f" %(len(positive)/ len(arr)))
    print("%f" %(len(negative)/ len(arr)))
    print("%f" %(len(zero)/ len(arr)))

plusMinus(arr)