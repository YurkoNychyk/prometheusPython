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
            print answer
            return answer

    if answer == ():
        return False
