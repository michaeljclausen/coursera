def find_max_unimodal(a):
  if len(a) == 1:
    return a[0]
  if len(a) == 2:
    return max(a[0], a[1])
  
  mid = len(a)//2

  if a[mid - 1] > a[mid] > a[mid + 1]:
    return find_max_unimodal(a[0:mid])
  elif a[mid + 1] > a[mid] > a[mid - 1]:
    return find_max_unimodal(a[mid:])
  else:
    print(a[mid])
    return a[mid]


a1 = [-3,-1,0,2,4,5,3,2,0,-10]

find_max_unimodal(a1)

  

