# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Ting Wei Wu

# Student UT EID: tw28634

# Course Name: CS 313E

# Unique Number:

from collections import defaultdict

# Output: True or False
def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    res = defaultdict(list)
    for word in lst:
        res[str(sorted(word))].append(word)
    finalres = list(res.values())
    return len(finalres)
def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
