#Lesson04 Reversed arguments
import sys
output_string = ""
sys.argv.reverse()
args = 0
for index in sys.argv[ : len(sys.argv)-1 : ]:
    output_string = output_string + str (index)
    args = args + 1
    if args != len(sys.argv)-1:
        output_string = output_string + " "

print output_string