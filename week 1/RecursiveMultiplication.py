import math
import sys

def RecursiveMultiplication (x, y):
  lenX = len(str(x))
  lenY = len(str(y))
  print("x: ", x, "y: ", y, "lenX:", lenX, "lenY: ", lenY)
  if lenX == 1 and lenY == 1:
    return int(x)*int(y)
  else:  
    midX = int(math.floor(lenX/2))
    midY = int(math.floor(lenY/2))
    x = str(x)
    y = str(y)
    a = x[0:midX]
    b = x[midX:]
    c = y[0:midY]
    d = y[midY:]
    ac = RecursiveMultiplication(str(a), str(c))
    ad = RecursiveMultiplication(str(a), str(d))
    bc = RecursiveMultiplication(str(b), str(c))
    bd = RecursiveMultiplication(str(b), str(d))
    ans = 10**lenX * ac + 10**(lenX/2) * (ad + bc) + bd
    print(ans)

  return ans


if __name__ == '__main__':
    RecursiveMultiplication(sys.argv[1], sys.argv[2])
