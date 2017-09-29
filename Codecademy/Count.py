"""
Return the number of times the item occurs in the list.

For example: 
    count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).
    
"""


def count(sequence, item):
  count = 0
  for i in sequence:
    if item == i:
      count += 1
  return count
