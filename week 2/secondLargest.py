def find_max_with_comparisons(a):
  if len(a) == 2:
    if a[0] > a[1]:
      return a[0], [a[1]]
    else:
      return a[1], [a[0]]
  max_l, comparisons_l = find_max_with_comparisons(a[0:int(len(a)/2)])
  max_r, comparisons_r = find_max_with_comparisons(a[int(len(a)/2):])

  if (max_l > max_r):
    #print(max_l, comparisons_l + [max_r])
    return max_l, comparisons_l + [max_r]
  else:
    #print(max_r, comparisons_r + [max_l])
    return max_r, comparisons_r + [max_l]


def find_second_largest(a):
  max, x = find_max_with_comparisons(a)
  second_largest = x[0]
  for i in range (1, len(x)):
    #print('i', i, 'x[i]', x[i])
    if x[i] > second_largest:
      second_largest = x[i]

  print(second_largest)
  return second_largest
    
a1 = [4,2,6,1,0,9,3,5]
a2 = [0,1,14,3,4,5,6,7,8,9,10,11,12,13,2,15]
a3 = [11,2,4,1,6,5,9,3]

#find_max_with_comparisons(a2)
find_second_largest(a2)