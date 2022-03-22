#Lesson04 Lucky ticket
import sys

first_number = (sys.argv[1])
last_number = (sys.argv[2])
lucky_count = 0

while int(first_number) <= int(last_number):
    
    first_number = str(first_number)
    
    while len(first_number) < 6:
        
        first_number = "0" + first_number

    #print "First number: " + first_number
     
    sum1 = int(first_number[0]) + int(first_number[1]) + int(first_number[2])
    sum2 = int(first_number[3]) + int(first_number[4]) + int(first_number[5])
    
    #print "sum1: " + str(sum1) + " sum2: " + str(sum2)
    if sum1 == sum2:
        #print "BINGO! " + first_number
        lucky_count = lucky_count + 1
        
    first_number = int(first_number) + 1
    
print lucky_count