''' given a sorted array is there an A[i] == i?
'''

def ith_equals_i(a, i = 0):
  if len(a) == 1:
    if a[0] == i:
      return True
    else:
      return False
  mid = len(a)//2 
  print(a, 'mid:', mid, 'i:', i)
  if a[mid] > mid + i:
    return ith_equals_i(a[0:mid], i)
  elif a[mid] < mid + i:
    return ith_equals_i(a[mid:], mid + i)
  elif a[mid] == mid + i:
    return True


a1 = [2,3,4,5]
a2 = [-4,-2,2,5]
a3 = [-2, -1, 0, 1, 2, 3]
a4 = [-2, -1, 0, 1, 2, 5]
a5 = [-20,-19,-18,-1,0,2,4,5,8,10,11,14,15,198]


print(ith_equals_i(a1))
print(ith_equals_i(a2))
print(ith_equals_i(a3))
print(ith_equals_i(a4))
print(ith_equals_i(a5))