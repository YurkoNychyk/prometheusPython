def make_sudoku(size):
    import random
    print "SUDOKU"
    matrix = [[]]
    print matrix[0]
    for r in range(0, size*size):
        matrix.append([])
        while len(matrix[r]) < size*size:
            n = random.randint(1, size*size)
            #print "matrix %d row is %d of length" % (r, len(matrix[r]))

            if n not in matrix[r]:
                if r > 0:
                    if n != matrix[r-1][len(matrix[r])]:
                        #print "add %d in %s" % (n, str(matrix[r]))
                        matrix[r].append(n)
                else:
                    #print "add %d in %s" % (n, str(matrix[r]))
                    matrix[r].append(n)
            print n
            print matrix
        print str(matrix[r]) + " " + str (r)
