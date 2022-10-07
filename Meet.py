#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

def earliestPossibleMeeting(person1, person2, duration):
	newp1 = []
	newp2 = []
	for p in person1:
		if (p[1] - p[0]) >= duration:
			newp1.append(p)

	for p in person2:
		if (p[1] - p[0]) >= duration:
			newp2.append(p)

	available = []
	for time in newp1:
		count = 0
		for time2 in newp2:
			#or (time[0] < time2[0] and time[1] < time2[0])
			if (time[0] >= time2[0] and time[1] <= time2[1]):
		# 		count += 1
		# if count == len(person2):
				available.append(time)

	for time in newp2:
		count = 0
		for time2 in newp1:
			#or (time[0] < time2[0] and time[1] < time2[0])
			if (time[0] >= time2[0] and time[1] <= time2[1]):
		# 		count += 1
		# if count == len(person2):
				available.append(time)

	# for time in person2:
	# 	count = 0
	# 	for time2 in person1:
	# 		if (time[0] > time2[1] and time[1] > time2[1]) or (time[0] < time2[0] and time[1] < time2[0]):
	# 			count += 1
	# 	if count == len(person2):
	# 		available.append(time)


	for ele in available:
		if ele[1] - ele[0] >= duration:
			continue
		else:
			available.remove(ele)

	minimum = 9999
	for ele in available:
		if ele[0] < minimum:
			minimum = ele[0]

	for ele in available:
		if ele[0] == minimum:
			return [ele[0], ele[0] + duration]

	return []













def main():
        #test_cases()

	# read the input data and create a list of lists for each person
	f = sys.stdin
	# read in the duration
	dur = int(f.readline().strip())
	# person 1's number of avalible slots
	num1 = int(f.readline().strip())
	p1 = []
	for x in range(num1):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p1.append(tmp)

	# person 2's number of avalible slots
	num2 = int(f.readline().strip())
	p2 = []
	for x in range(num2):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p2.append(tmp)

	print(earliestPossibleMeeting(p1,p2,dur))

if __name__ == "__main__":
  main()
