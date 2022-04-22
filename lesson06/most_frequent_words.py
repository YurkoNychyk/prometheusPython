def find_most_frequent(text):
    text = text.lower().replace(",", " ").replace(".", "").replace("?","").replace("-"," ").replace("!","")
    text = text.split(" ")
    words = {}
    output = []
    for word in text:
        words[word] = text.count(word)
    for word in words :
        if words[word] == max(words.values()) and word != "":
            output.append(word)
    return output
