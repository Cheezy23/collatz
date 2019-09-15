# The number we will perform the Collatz oporations on.
n = int(input("Enter a positive integer: "))


# Keep looping until we reach 1.
# Note: this assumes the collatz conjecture is true
while n != 1:
    # Print the current calue of n.
    print(n)
    # Check if n is even.
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1

# Finally print the 1.
print(n)