#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of black tea in each store, and a list of integers named money that contains the amount of money
#               Tim will spend in a given day, returns a list of integers representing how many different shops
#               Tim can buy a cup of black tea.

#  Student Name: Ting Wei Wu

#  Student UT EID: tw28634

#  Course Name: CS 313E

#  Unique Number:

import sys


# A binary search implementation
def binary_search (a, x):
  lo = 0
  hi = len(a) - 1
  index = -1


  while (lo <= hi):
    mid = (lo + hi) // 2
    if (x >= a[mid]):
      lo = mid + 1
    else:
        index = mid
        hi = mid - 1

  return index

# Input: prices a list of integers containing the price of black tea in each store
#        money  a list of integers containing the amount of money Tim will spend in a given day
# Returns: a list of integers representing how many different shops Tim can buy a cup of black tea.
def find_purchase_options(prices, money):
    res = []
    sortedprice = sorted(prices)

    for mon in money:
        if mon >= sortedprice[len(sortedprice)-1]:
            res.append(len(sortedprice))
        elif mon < sortedprice[0]:
            res.append(0)
        else:
            res.append(binary_search(sortedprice, mon))

    return res




#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
