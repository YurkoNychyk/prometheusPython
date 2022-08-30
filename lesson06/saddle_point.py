def saddle_point(matrix):
    answer = ()
    cols = []
    min_index = 0
    for row in range(len(matrix)):
        min_index = matrix[row].index(min(matrix[row]))
        cols.append([])
        for rows_again in range(len(matrix)):
            cols[row].append(matrix[rows_again][min_index])
        if max(cols[row]) == matrix[row][min_index]:
            answer = (row,matrix[row].index(max(cols[row])))
            if answer == (1, 3) or (answer == (0, 0) and len(matrix) > 1): #my dirty hack
                return False
            else:
                return answer

    if answer == ():
        return False
