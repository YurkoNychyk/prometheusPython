from combStr import *
from FindFraction import *
from bouquets import *

s0 = CombStr('qqqqqqweqqq%')

print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0

print ("Find Fraction")
print find_fraction(2) # (1, 2)

print ("Bouquets")
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556
print bouquets(15.5,4.1,5.99,21.75)
