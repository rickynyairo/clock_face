"""
module to draw a circle without using floating point arithmetic
"""

radius = 20

for row in range(radius, -radius-1, -1):
    for col in range(-radius, radius+1):
        point_is_in_circle = row**2 + col**2 <= radius**2
        if point_is_in_circle:
            print(".", end=" ") 
        else:
            print(" ", end=" ")
    print()

