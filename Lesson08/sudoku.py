def make_sudoku(size):
    import random
    #print "SUDOKU"
    #random_row = random.sample(range(1, size*size+1), size*size)
    random_row = range(1,size*size+1)
    matrix = [random_row]
    #print matrix[0]
    for row in range(1, size*size):
        if row % size == 0 and row != 1:
            shift = size + 1
        else:
            shift = size

        matrix.append(matrix[row-1][shift:] + matrix[row-1][:shift])

    return matrix

def make_sudoku1(size):
    line = range(1,size**2+1)
    su = []
    for i in range(size**2):
        shift = i//size+i%size*size
        linex = line[shift:]+line[:shift]
        su.append(linex)
    return su

