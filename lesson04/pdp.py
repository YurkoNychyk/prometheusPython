#Lesson04 PravylnaDuzhkovaPoslidovnist
import sys
input_word = str(sys.argv[1])

input_range = []
score = 0
#print input_word
for ch in input_word:
    if score >= 0:
        if ch == ")":
            score = score - 1
        elif ch == "(":
            score = score + 1
        #print score
    else:
        #print score
        #print "NO"
        break

if score == 0:
    print "YES"
else:
    print "NO"