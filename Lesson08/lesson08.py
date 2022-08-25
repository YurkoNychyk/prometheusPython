import datetime

from combStr import *
from FindFraction import *
from bouquets import *
from sudoku import *
s0 = CombStr('qqqqqqweqqq%')

print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0

print ("Find Fraction")
print find_fraction(2) # (1, 2)

print ("Bouquets")
print bouquets(21.25,13.6,10.5,100)  # 34
print "SUDOKU"
x = datetime.datetime.today().time().minute * 60 +  datetime.datetime.today().time().second
make_sudoku(42)
y = datetime.datetime.today().time().minute * 60 +  datetime.datetime.today().time().second
print y-x

x = datetime.datetime.today().time().minute * 60 +  datetime.datetime.today().time().second
make_sudoku1(42)

y = datetime.datetime.today().time().minute * 60 +  datetime.datetime.today().time().second
print y-x
