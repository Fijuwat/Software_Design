#  File: Interval.py

#  Description: A basic interval class.

#  Student Name: Ting Wei Wu

#  Student UT EID: tw28634

#  Course Name: CS 313E

#  Unique Number:

import sys

class IntegerInterval (object):
    # constructor with default values
    def __init__(self, beginning = 0, end = 0):
        self.beginning = beginning
        self.end = end


    # creates a string representation of an Interval
    # returns a string in the form "Beginning: startTime, End: endTime"
    def __str__(self):
        return "Beginning: " + str(self.beginning) + ", End: " + str(self.end)



    # test for equality between two intervals
    # other is an interval object
    # returns a Boolean
    def __eq__(self, other):
        if self.beginning == other.beginning and self.end == other.end:
            return True
        else:
            return False


    # returns the length of this interval
    # returns an integer 
    def __len__(self):
        return self.end - self.beginning

    # determine if this interval overlaps with another
    # other is an interval object
    # returns a Boolean
    def overlap(self, other):
        if self.beginning > other.beginning and self.beginning < other.end:
            return True
        elif self.end > other.beginning and self.end < other.end:
            return True
        elif other.beginning > self.beginning and other.beginning < self.end:
            return True
        elif other.end > self.beginning and other.end < self.end:
            return True
        elif self.beginning == other.beginning and self.end == other.end:
            return True
        else:
            return False

    # determine the time in the intersection of this interval with another
    # other is an interval object
    # returns an Integer
    def intersection(self, other):
        if self.overlap(other) == False:
            return 0
        else:
            return min(self.end, other.end) - max(self.beginning, other.beginning)

    # determine the time in the union of this interval with another
    # other is an interval object
    # returns an Integer
    def union(self, other):
        return (self.end - self.beginning) + (other.end - other.beginning) - self.intersection(other)

# do NOT change main, it has been fully completed for you
def main():
    # read the two intervals
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line1 = line1.split(" ")
    line2 = line2.split(" ")

    interval1 = IntegerInterval(int(line1[0]), int(line1[1]))
    interval2 = IntegerInterval(int(line2[0]), int(line2[1]))

    # print the output
    print(interval1)
    print(interval2)
    print(len(interval1))
    print(len(interval2))
    print(interval1 == interval2)
    print(interval1.overlap(interval2))
    print(interval2.overlap(interval1))
    print(interval1.intersection(interval2))
    print(interval2.intersection(interval1))
    print(interval1.union(interval2))
    print(interval2.union(interval1))

if __name__ == "__main__":
    main()
