##############################
# 30M015 Exam 2024, Block 5. #
##############################

# Grading (do not remove):
# a) 1
# b) 2
# c) 3

snr = 1234567  # replace with your student number


# Import any packages needed here
import math


# Define your class here below
class Circle:
    ### Question a) ###
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    ### Question b) ###  
    def area(self):
        return math.pi*self.radius**2
    
    def circumference(self):
        return 2*self.radius*math.pi
    
    ### Question c) ###      
    def circle_check(self,a):
        distance = math.sqrt((self.center[0] - a[0])**2 + (self.center[1] - a[1])**2)
        return distance < self.radius    



### Question a) ###
# Create circle with center [2,3] and radius 3 here and print attributes
circle1 = Circle([2,3],3)
print(circle1.center)
print(circle1.radius)

### Question b) ###
# Print area and circumference of circle with center [2,3] and radius 3 here
print(circle1.area())
print(circle1.circumference())


### Question c) ###
# Check if a = [3,6] is contained, or not, in circle with center [2,3]
# and radius 3 here
a = [3,6]
print(circle1.circle_check(a))

