from sphere import *
from Student import *
from SuperStr import *
from CreateCalendar import *

print "\nTest 7.1\n "

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

print "\nTest 7.2\n"

conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)


oleg.make_lab(1)  # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
#print oleg.labs
oleg.make_lab(8,0)  # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
#print oleg.labs
oleg.make_lab(1)  # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
#print oleg.labs
oleg.make_lab(10,7)  # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
#print oleg.labs
oleg.make_lab(4,1)  # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
#print oleg.labs
oleg.make_lab(5)  # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
#print oleg.labs
oleg.make_lab(6.5)  # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
#print oleg.labs
oleg.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
#print ('labs:' + str(oleg.labs) + " exam:" +  str(oleg.exam))
print oleg.is_certified() # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
#print ('labs:' + str(oleg.labs) + " exam:" +  str(oleg.exam))
print oleg.is_certified() # (62.5, True)

s = SuperStr('123123123123')
print s.is_repeatance('123')
# True
print s.is_repeatance('123123')
# True
print s.is_repeatance('123123123123')
# True
print s.is_repeatance('12312')
# False
print type(123)
print s.is_repeatance(123)
# False
print s.is_palindrom()
# False
print s
print int(s)
print s + 'qwe'
# 123123123123qwe
p = SuperStr('mystring1gnirtsym')
print p.is_palindrom()
# True
print (create_calendar_page(1) + "\n")
print (create_calendar_page() + "\n")
print (create_calendar_page(3) + "\n")
print (create_calendar_page(04, 1992) + "\n")

