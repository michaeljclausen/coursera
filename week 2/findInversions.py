arr = []
f=open("IntegerArrayData.txt", "r")
for line in f:
    arr.append(int(line.strip('\n\r')))

def sort_and_count(arr):
  if len(arr) == 1:
    return arr, 0
  (left, left_count) = sort_and_count(arr[0:len(arr)/2])
  (right, right_count) = sort_and_count(arr[len(arr)/2:])
  (sorted_arr, split_count) = merge_and_count(left, right)


  return sorted_arr, left_count + right_count + split_count

def merge_and_count(l, r):
  temp, count, i, j = [], 0, 0, 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      temp.append(l[i])
      i += 1
    elif r[j] < l[i]:
      temp.append(r[j])
      j += 1
      count += len(l) - i
  if i < len(l):
    temp += l[i:]
  if j < len(r):
    temp += r[j:]

  return temp, count



print (sort_and_count (arr)[1])
