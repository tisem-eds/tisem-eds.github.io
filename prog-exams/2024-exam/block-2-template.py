##############################
# 30M015 Exam 2024, Block 2. #
##############################

# Grading (do not remove):
# a) 4
# b) 2

snr = 1234567  # replace with your student number

### Question a) ###
# Complete the findRoot(x, tol) function:

def findRoot(x, tol):
    # Set initial guess of a, b

    # Initialize distance:
    dist = 1 + tol

    while dist > tol:

        # Compute c according to the equation in step 2:

        # Compute distance:

        # Update guesses a and b:

    return(c)


# Test the function using test values provided:
print(round(findRoot(2, 1e-6), 8))

# Calculate the square root of x=7 with tol=0.01:



### Question b) ###

# Rewrite the function to add a counter:


# Find the square root of 2 with tol=1e-6
