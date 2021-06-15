#MIT License
#
#Copyright (c) 2021 Voldermirt
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
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

### Input helper
def get_idiotproof_input(message, type):
    user_input = None
    while True:
        user_input = input(message)
        try:
            return type(user_input)
        except:
            print("Invalid.")
            continue

### The program ###
side_num = get_idiotproof_input("Number of sides: ", int)
radius = get_idiotproof_input("Radius: ", float)

internal_angle = math.radians(360.0 / side_num)

point_1 = Vector(math.sin(0), math.cos(0)).multiply_scalar(radius)
point_2 = Vector(math.sin(internal_angle), math.cos(internal_angle)).multiply_scalar(radius)

distance = point_1.distance_to(point_2)

p = (radius*2 + distance) / 2

# Area of a triangle given 3 sides: sqrt(p(p - a)(p - b)(p - c)) where p = (a + b + c) / 2

area_triangle = math.sqrt(p * (p - radius) * (p - radius) * (p - distance))
area_ngon = area_triangle * side_num

print("Area: " + str(area_ngon))
input("Press ENTER to close...")