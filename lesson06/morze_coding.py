def encode_morze(text):
    morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--.."
}
    radio_codes = {
        "." : "^_",
        "-" : "^^^_",
        " " : "_______"
}

    output = ""
    encoded_character=""
    text = text.upper()
    text = text.split(" ")
    for word in text:
        current_word = ""
        for character_index in range(len(word)):

            character = word[character_index]
            if character in morse_code:
                for symbol_index in range (len(morse_code[character])):
                    symbol = morse_code[character][symbol_index]
                    encoded_character = encoded_character + radio_codes[symbol]

                encoded_character = encoded_character[:len(encoded_character)-1] + "___"
                #print "character:" + word[character_index] + " its code: " + encoded_character

                current_word = current_word + encoded_character
                encoded_character = ""
        current_word = current_word[:len(current_word)-3]
        output = output + current_word + "_______"
    output = output[:len(output)-7]
    #print output
    return output
