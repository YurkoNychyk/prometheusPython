def count_holes(n):
    print "n= " + str(n)
    if not isinstance(n, float):
        try:
            holes=0
            n=abs (int(n))
            n=str(n)
            digits ={'0':1, '4':1, '6':1, '8':2, '9':1}
            for letters in n:
                if letters in digits:
                    holes = holes + digits[letters]

            return holes
        except:
            return 'ERROR'
    else:
        return 'ERROR'
