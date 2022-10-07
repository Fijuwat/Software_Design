# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Ting Wei Wu

# Student UT EID: tw28634

# Course Name: CS 313E

# Unique Number: 86610

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x=0, y=0):
      self.x = x
      self.y = y



  # get the distance to another Point object
  def dist (self, other):
      dis = ((self.x - other.x)**2 + (self.y - other.y) ** 2)**(1/2)
      return dis


class Triangle (Point):
    # constructor
    def __init__(self, PointA, PointB, PointC):

        self.pointA = PointA
        self.pointB = PointB
        self.pointC = PointC
        Point.__init__(self, x=0, y=0)



    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):
        selfset = set()
        otherset = set()
        selfset.add(self.pointA.dist(self.pointB))
        otherset.add(other.pointA.dist(other.pointB))
        selfset.add(self.pointB.dist(self.pointC))
        otherset.add(other.pointB.dist(other.pointC))
        selfset.add(self.pointC.dist(self.pointA))
        otherset.add(other.pointC.dist(other.pointA))
        if selfset == otherset:
            return True
        else:
            return False


    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
        # a = self.pointA.dist(self.pointB)
        # b = self.pointB.dist(self.pointC)
        # c = self.pointC.dist(self.pointA)
        # if a + b >= c and b + c >= a and c + a >= b:
        #     return True
        # else:
        #     return False
        if abs((self.pointA.x * (self.pointB.y - self.pointC.y) + self.pointB.x * (self.pointC.y - self.pointA.y) + self.pointC.x * (self.pointA.y - self.pointB.y))) == 0:
            return False
        else:
            return True


    #return the area of the triangle:
    def area(self):
        area = abs((0.5)*(self.pointA.x * (self.pointB.y - self.pointC.y) + self.pointB.x * (self.pointC.y - self.pointA.y) + self.pointC.x * (self.pointA.y - self.pointB.y)))
        return area

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
