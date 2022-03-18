#Lesson04 Test Palindrome
import sys

input_word = str(sys.argv[1])
input_word = input_word.lower()

input_range = []
reversed_range = []
for letter in input_word:
    if letter != " ":
        input_range.append(letter)
        reversed_range.append(letter)

reversed_range.reverse()


if input_range == reversed_range:
    print "YES"
else:
    print "NO"