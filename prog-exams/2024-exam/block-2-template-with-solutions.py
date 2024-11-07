##############################
# 30M015 Exam 2024, Block 2. #
##############################

# Grading (do not remove):
# a) 4
# b) 2

snr = 1234567  # replace with your student number

### Question a) ###
# Complete the findRoot(x, tol) function:
def f(z, x):
    return(z ** 2 - x)

def findRoot(x, tol):
    # Set initial guess:
    (a, b) = (0.0, max(1, x))

    # Initialize distance:
    dist = 1 + tol

    while dist > tol:

        # Compute c according to the equation in step 2:
        c = b - (b - a) * f(b, x) / (f(b, x) - f(a, x))

        # Compute distance:
        dist = abs(f(c, x))

        # Update guesses a and b:
        if f(c, x) > 0:
          b = c
        else:
          a = c

    return(c)

# Test the function using test values provided:
print(round(findRoot(2, 1e-6), 8))

# Calculate the square root of x=7 with tol=0.01:
print(findRoot(7, 0.01))


### Question b) ###

# Rewrite the function to add a counter:
def findRoot(x, tol):
    # Set initial guess:
    (a, b) = (0.0, max(1, x))

    # Initialize distance:
    dist = 1 + tol

    # Initialize counter
    counter = 0

    while dist > tol:

        # Compute c according to the equation in step 2:
        c = b - (b - a) * f(b, x) / (f(b, x) - f(a, x))
        counter += 1

        # Compute distance:
        dist = abs(f(c, x))

        # Update guesses a and b:
        if f(c, x) > 0:
          b = c
        else:
          a = c

    print(counter)
    return(c)

# Find the square root of 2 with tol=1e-6
print(findRoot(2, 1e-6))
