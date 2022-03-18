#Coding/Encoding strings with Ceasar code
import sys
#input_message = str(raw_input('Enter the message to encode:'))
#encoding_shift = str(raw_input('Enter code shift:'))
input_message = str(sys.argv[1])
encoding_shift = int(sys.argv[2])
encoded_message = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print "Input string: " + input_message
print "Encoding shift: " + str(encoding_shift)
alphabet_index = 0
for letter in input_message:
    print "Letter " + letter
    alphabet_index = 0
    while alphabet_index < len(alphabet):
        if letter == alphabet[alphabet_index]:
            print alphabet[alphabet_index + encoding_shift]
            encoded_message.append(alphabet[alphabet_index + encoding_shift])
            break
        alphabet_index = alphabet_index + 1
    
print encoded_message