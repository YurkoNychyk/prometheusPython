#Coding/Encoding strings with Ceasar code
import sys

encode_decode_answer = " "


while encode_decode_answer != 'e' and encode_decode_answer != 'd' and encode_decode_answer !='q':
    
    print " "
    encode_decode_answer = str(raw_input ('Dou you want to Encode(e) or Decode(d) your message? If neither -- press (q) '))     

    if encode_decode_answer != 'q':

        output_message = ''

        input_message = str(raw_input('Enter your message:'))
        encoding_shift = int(raw_input('Enter code shift:'))    
        print ""
    
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for letter in input_message:
    
            current_letter_index = alphabet.find (letter)
            if current_letter_index != -1:
           
                if encode_decode_answer == 'e':
                    
                    print 'Encoding...'
                    
                    if current_letter_index + encoding_shift < len(alphabet):
                        
                        output_message = output_message + alphabet[current_letter_index + encoding_shift]
                        
                    else:
                        
                        output_message = output_message + alphabet[current_letter_index + encoding_shift - len(alphabet)]


                elif encode_decode_answer == 'd':
                    print 'Decoding...'
                    output_message = output_message + alphabet[current_letter_index - encoding_shift]
     
            else:
    
                output_message = output_message + letter    
        
        print ""
        print "Your message:"
        print output_message
        encode_decode_answer = " "

    else:
        print ""
        print 'Quitting'
        break

    
    