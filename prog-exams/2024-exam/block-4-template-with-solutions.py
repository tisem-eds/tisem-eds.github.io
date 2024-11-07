##############################
# 30M015 Exam 2024, Block 4. #
##############################

# Grading (do not remove):
# a) 1
# b) 4
# c) 1
# d) 3

snr = 1234567  # replace with your student number


# Import any packages needed here
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


### Question a) ###
# Define the function f here as Python function
def f(x):
    return -x**4 + 3*x**3 - 2*x**2 + 2


### Question b) ###
# Give code here to reproduce the desired figure
x = np.linspace(-3,3,600)

# Compute function values
y = f(x)

#Create the figure
plt.figure()

# Create the plot
plt.plot(x, y, label='$f(x) = -x^4 + 3x^3 - 2*x^2 + 2$')

# Create labels for axes
plt.xlabel('x')
plt.ylabel('f(x)')

# Create the legend with the specified labels
plt.legend()

# Fix the range of the axes
plt.xlim(-1,3)
plt.ylim(-2,3)

# Add title to the plot
plt.title('Plot of the function f')

# Add grid to the background
plt.grid()


### Question c) ###
# Define vector guesses = [-1,-0.9,\dots,0.9,1] belwo
guesses = np.linspace(-1,1,21)


### Question d) ###
# Create list of found solutions to equation f(x) = 3x here and print it
def g(x):
    return f(x) - 3*x

x = []
for i in guesses:
    x.append(optimize.fsolve(g,i)[0])

print(x)







