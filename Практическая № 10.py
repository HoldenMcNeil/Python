import math
def distance(x1,y1,x2,y2):
    A=math.fabs(x1)+math.fabs(y1)
    B=math.fabs(x2)+math.fabs(y2)
    C=A*A+B*B
    return math.sqrt(C)
print(distance(-2,4,3,-5))