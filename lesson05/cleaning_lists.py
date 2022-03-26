#Lesson05 Clean list function
def clean_list (list_to_clean):
    print "Input list:"
    print list_to_clean
    checked_element = len(list_to_clean)-1
    
    while checked_element > 0:
        element = checked_element - 1

        while element >= 0:

            if (list_to_clean[checked_element] == list_to_clean[element] and type(list_to_clean[checked_element]) == type(list_to_clean[element])) :

                del list_to_clean[checked_element]
                checked_element-=1

            element -= 1

        checked_element -= 1    

    return list_to_clean