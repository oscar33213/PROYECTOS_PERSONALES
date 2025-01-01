

numerosF = []

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    

for i in range(10):
    numerosF.append(fibonacci(i))
    
print(numerosF)


# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

# In this case, the function fibonacci(n) is defined to calculate the Fibonacci sequence. The function is recursive, meaning that it calls itself within the function definition.

# The for loop iterates over the range of 10 numbers and appends the result of the fibonacci function for each number to the list numerosF.

# Finally, the list numerosF is printed to display the Fibonacci sequence up to the 10th number.

# The output of the code will be:

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# This represents the first 10 numbers in the Fibonacci sequence.

# The code snippet demonstrates the use of recursion to calculate the Fibonacci sequence in Python. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1. The function fibonacci(n) is defined to calculate the Fibonacci sequence using recursion. The for loop iterates over the range of 10 numbers and appends the result of the fibonacci function for each number to the list numerosF. Finally, the list numerosF is printed to display the Fibonacci sequence up to the 10th number. The output of the code will be the first 10 numbers in the Fibonacci sequence.
