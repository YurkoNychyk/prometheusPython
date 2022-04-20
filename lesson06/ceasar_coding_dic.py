# Coding/Encoding strings with Caesar code
output_message = ''

input_message = str(raw_input('Enter your message:'))
encoding_shift = int(raw_input('Enter code shift:'))
print ""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
coder = {}
for i in range(len(alphabet)):
    coder[alphabet[i]] = alphabet[(i + encoding_shift) % len(alphabet)]

for letter in input_message:

    if letter in coder:

        print 'Encoding... ' + letter

        output_message = output_message + coder[letter]
print "Encoded message: %s" % (output_message)
