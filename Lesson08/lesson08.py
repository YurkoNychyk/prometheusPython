from combStr import *
from FindFraction import *


s0 = CombStr('qqqqqqweqqq%')

print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0

print ("Find Fraction")
print find_fraction(2) # (1, 2)
