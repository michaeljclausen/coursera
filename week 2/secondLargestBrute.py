#brute force solution
#runs in O(n) with 2n - 2 comparisons 
import math

def find_second_largest(arr):
  largest = float("-inf")
  second_largest = float("-inf")
  for i in range (0,len(arr)):
    if arr[i] > largest:
      largest = arr[i]
  
  for i in range (0,len(arr)):
    if arr[i] > second_largest and arr[i] < largest:
      second_largest = arr[i]

  print(second_largest)
  return second_largest


find_second_largest([3,55,4,9,1001,-44,3.2,3333,949,1,-44,1002,2222.222])
