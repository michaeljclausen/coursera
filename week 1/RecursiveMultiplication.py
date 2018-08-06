import math
import sys

def recursive_multiplication (x, y):
  len_x = len(str(x))
  len_y = len(str(y))
  print("x: ", x, "y: ", y, "len_x:", len_x, "len_y: ", len_y)
  if len_x == 1 and len_y == 1:
    return int(x)*int(y)
  else:  
    midX = int(math.floor(len_x/2))
    midY = int(math.floor(len_y/2))
    x = str(x)
    y = str(y)
    a = x[0:midX]
    b = x[midX:]
    c = y[0:midY]
    d = y[midY:]
    ac = recursive_multiplication(str(a), str(c))
    ad = recursive_multiplication(str(a), str(d))
    bc = recursive_multiplication(str(b), str(c))
    bd = recursive_multiplication(str(b), str(d))
    ans = 10**len_x * ac + 10**(len_x/2) * (ad + bc) + bd
    #print(ans)

  return ans


if __name__ == '__main__':
    recursive_multiplication(sys.argv[1], sys.argv[2])
