from geom2d.point import *

l = []

for i in range (-5, 6):
    l.append(Point(i, i*i))

for el in l:
    print(el) #цикл for

l2 = list(map (lambda i: Point(i, i*i), range(-5, 6))) #операция map

print(l2)

l3 = list(filter(lambda p: p.x > 0, l)) #операция filter

print(l3)

l4 = list(filter (lambda p: p.x % 2 == 0, l)) # функция filter, которая фильтрует только четные числа

print (l4)


