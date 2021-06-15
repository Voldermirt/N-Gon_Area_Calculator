import math

### Vector class ###
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def multiply_scalar(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def distance_to(self, vector):
        return math.sqrt((vector.x - self.x)**2 + (vector.y - self.y)**2)

### The program ###

side_num = int(input("Number of sides: "))
radius = float(input("Radius: "))

internal_angle = math.radians(360.0 / side_num)

point_1 = Vector(math.sin(0), math.cos(0)).multiply_scalar(radius)
point_2 = Vector(math.sin(internal_angle), math.cos(internal_angle)).multiply_scalar(radius)

distance = point_1.distance_to(point_2)

p = (radius + radius + distance) / 2

area_triangle = math.sqrt(p * (p - radius) * (p - radius) * (p - distance))
area_ngon = area_triangle * side_num

print("Area: " + str(area_ngon))