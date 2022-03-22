#Lesson4 Backon coding
import sys
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_message = sys.argv [1]
message_wo_spaces = ""
coded_sequentials = []
current_group = 0
output_message = ""
message_wo_spaces = input_message.replace(" ", "")

while current_group < len(message_wo_spaces) / 5:
    coded_sequentials.append(message_wo_spaces[current_group * 5:current_group * 5 + 5])
    
    for character in coded_sequentials[current_group]:
    
        if character.islower():

            coded_sequentials[current_group] = coded_sequentials[current_group] + "a"

        else:

            coded_sequentials[current_group] = coded_sequentials[current_group] + "b"

    if key.find(coded_sequentials[current_group][5:10]) != -1:
         output_message = output_message + alphabet[key.find(coded_sequentials[current_group][5:10])]
    else:
         output_message = "Error"   
    

    current_group = current_group + 1

print output_message