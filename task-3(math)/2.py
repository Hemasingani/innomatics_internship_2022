import math
ab=int(input())
bc=int(input())
angle=math.degrees(math.atan(ab/bc))
angle=str(round(angle))
print(angle+chr(176))
