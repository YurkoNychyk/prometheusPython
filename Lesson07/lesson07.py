from lecture7_example import *
from sphere import *


yurko = Human('Yurko Mykolayovych', 1986)
# yurko.name = 'Yurko Mykolayovych'
# yurko.birth_year = 1986

print (yurko.name)
print (yurko.get_age())

student001 = Student('Yurko', 1986, [5, 4, 3, 5, 5])
print (student001.get_average_mark())




s0 = Sphere(1) # test sphere creation with radius and default center
print (s0.get_center()) # (0.0, 0.0, 0.0)
print (s0.get_volume()) # 0.523598775598
print (s0.get_square())
print (s0.is_point_inside(0, -1.5, 0)) # False
s0.set_radius(1.6)

print (s0.is_point_inside(0, -1.5, 0)) # True
print (s0.get_radius()) # 1.6

print ("S1")

s1 = Sphere()
print (s1.get_center()) # '== (0, 0, 0)'
print (s1.get_radius()) # '== 1'
print (s1.get_volume()) # '== 4.18879020479'
print (s1.get_square()) # '== 12.5663706144'
print (s1.is_point_inside(0, 0.99, 0)) # '== True'
print (s1.is_point_inside(0.99, 0, 0)) # '== True'
print (s1.is_point_inside(0, 0, 0.99)) # '== True'
s1.set_radius(1.1)
print ("radius now is " + str(s1.get_radius()))
s1.set_center(0.5, 1, 0)
print ("center now is " + str(s1.get_center()))
print (s1.is_point_inside(0, 0.99, 0)) # '== True'
print (s1.is_point_inside(0.99, 0, 0)) # '== False'
print (s1.is_point_inside(0, 0, 0.99)) # '== False'
print (s1.get_center()) # '== (0.5, 1, 0)'
print (s1.get_radius()) # '== 1.1'
print ("S2")
s2 = Sphere(2)
print (s2.get_center()) # '== (0, 0, 0)'
print (s2.get_radius()) # '== 2'
print (s2.is_point_inside(0, 0.99, 0)) # '== True'
print (s2.is_point_inside(1.99, 0, 0)) # '== True'
print (s2.is_point_inside(0, 0, 2.99)) # '== False'
s3 = Sphere(1.99, 1, 2, -1)
print (s3.get_center()) # '== (1, 2, -1)'
print (s3.get_radius()) # '== 1.99'
print (s3.is_point_inside(0, 0.99, 0)) # '== True'
print (s3.is_point_inside(0.99, 0, 0)) # '== False'
print (s3.is_point_inside(0, 0, 0.99)) # '== False'