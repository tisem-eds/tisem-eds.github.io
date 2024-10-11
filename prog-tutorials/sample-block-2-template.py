################################
# 30M015 Sample Exam, Block 2. #
################################

# Grading (do not remove):
# a) 
# b) 

snr = 1234567  # replace with your student number

### Question a) ###
# Complete the findRoot(x, tol) function:

def findRoot(x, tol):
    # Set initial guess:
    (y_0, y_1) = (0.0, 1.0)

    # Initialize distance:
    dist = 1 + tol

    while dist > tol:

        # Compute y_2 according to the equation in step 2

        # Compute distance

        # Replace y_0 with y_1 and y_1 with y_2

    return(y_1)

# Test the function:
print(round(findRoot(2, 1e-6), 8))

# Calculate the square root of x=7 with tol=0.01:



### Question b) ###

# Rewrite the function to add a counter:


# Find the square root of 2 with tol=1e-6
