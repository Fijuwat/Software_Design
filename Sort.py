# File: Triangle.py
# Description: A basic 2D Triangle class
# Student Name: Kelly Zhao
# Student UT EID: kfz77
# Course Name: CS 313E
# Unique Number:

import sys
import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


class Triangle(Point):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.PointA = PointA
        self.PointB = PointB
        self.PointC = PointC

    # print string representation of Triangle
    def __str__(self):
        return 'Point1: (' + str(float(PointA.x)) + ',' + str(float(PointA.y)) + '), Point2: (', str(
            float(PointB.x)) + ',' + str(float(PointB.y)) + '), Point3: (', + str(float(PointC.x)) + ',' + str(
            float(PointC.y)) + ')'

    # equality function
    def __eq__(self, other):
        tol = 1e-8
        return (abs(float(self.PointA.x) - float(other.PointA.x)) < tol) and (abs(float(self.PointA.y) - float(other.PointA.y)) < tol) and (abs(float(self.PointB.x) - float(other.PointB.x)) < tol) and (abs(float(self.PointB.y) - float(other.PointB.xy)) < tol) and (abs(float(self.PointC.x) - float(other.PointC.x)) < tol) and (abs(float(self.PointC.y) - float(other.PointC.y)) < tol)





        # return side lengths of triangle

    def side_length(self):
        sideA = self.PointA.dist(self.PointB)
        sideB = self.PointB.dist(self.PointC)
        sideC = self.PointC.dist(self.PointA)

    # check if the triangle is similar to another triangle
    def is_similar(self, other):
        return (self.sideA % other.sideA == 0 or self.sideA % other.sideB == 0 or self.sideA % self.sideC == 0) and (
                self.sideB % other.sideA == 0 or self.sideB % other.sideB == 0 or self.sideB % self.sideC == 0) and (
                       self.sideC % other.sideA == 0 or self.sideC % other.sideB == 0 or self.sideC % self.sideC == 0)

    # check if triangle is obtuse or not
    def is_obtuse(self):
        return (self.sideA ** 2) + (self.sideB ** 2) < (self.sideC ** 2)

    # check if triangle is scalene
    def is_scalene(self):
        return self.sideA != self.sideB and self.sideA != self.sideC and self.sideB != self.sideC


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################
# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)] * 2)]


def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())
    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])
    # Print final output
    print('A', triangleA)
    print('B', triangleB)
    print('A obtuse', triangleA.is_obtuse())
    print('B obtuse', triangleB.is_obtuse())
    print('A scalene', triangleA.is_scalene())
    print('B scalene', triangleB.is_scalene())
    print('A equals b', triangleA == triangleB)


if __name__ == "__main__":
    main()
