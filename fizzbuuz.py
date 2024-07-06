
for numero in range(1, 101):  # Range should be (1, 101) to include numbers from 1 to 100
    if numero % 3 == 0 and numero % 5 == 0:  # Check for numbers divisible by both 3 and 5 first
        print("fizzbuzz")
    elif numero % 3 == 0:  # Check for numbers divisible by 3
        print("fizz")
    elif numero % 5 == 0:  # Check for numbers divisible by 5
        print("buzz")
    else:
        print(numero)  # Print the number if none of the above conditions are met
