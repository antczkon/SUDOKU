import random



def generate():
    table = [[[f"{i}"]for i in range (9)] for j in range(9)]
    return table

def check_row(sudoku_table, num_of_row):
    digits=[['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'],['9']]
    for digit in digits:
        if sudoku_table[num_of_row].count(digit)>=2:
            return False
    return True


def check_column(sudoku_table, num_of_column):
    column = [row[num_of_column] for row in sudoku_table]
    digits=[['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'],['9']]
    for digit in digits:
        if column.count(digit) >= 2:
            return False
    return True

def check_square(sudoku_table, num_of_row, num_of_column):
    begin_check_row=0
    begin_check_column=0
    if num_of_row > 5:
        begin_check_row=6
    elif num_of_row > 2:
        begin_check_row=3
    
    if num_of_column > 5:
        begin_check_column=6
    elif num_of_column > 2:
        begin_check_column=3
    
    square = []
    for i in range(begin_check_row,begin_check_row+3):
        for j in range(begin_check_column,begin_check_column+3):
            square.append(sudoku_table[i][j])
    digits=[['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'],['9']]
    for digit in digits:
        if square.count(digit) >= 2:
            return False
    return True


"""def generating_all_candidates():
    sudoku_table=[[[[f'{k+1}' for k in range(9)]]for j in range(9)] for i in range(9)]
    return sudoku_table


def generaing_all_positions():
    positions=[]
    for i in range(9):
        for j in range(9):
            positions.append([i,j])
    return positions


def pick_random_candidate(sudoku_table, passible_positions):
    chosen = random.choice(passible_positions)
    pos_row = chosen[0]
    pos_column = chosen[1]
    candidate = random.choice(sudoku_table[pos_row][pos_column][0])
    return pos_row, pos_column, candidate

def eliminate_candidates_after_choice(sudoku_table,passible_positions):
    row,col,can = pick_random_candidate(sudoku_table,passible_positions)
    pos = [row,col]
    passible_positions.remove(pos)
    sudoku_table[row][col][0] = [can]
    for column_not_chosen in range(9):
        if column_not_chosen != col and can in sudoku_table[row][column_not_chosen][0]:
            sudoku_table[row][column_not_chosen][0].remove(can)
    
    for row_not_chosen in range(9):
        if row_not_chosen != row and can in sudoku_table[row_not_chosen][col][0]:
            sudoku_table[row_not_chosen][col][0].remove(can)
    
    begin_check_column=0
    begin_check_row=0
    if row > 5:
        begin_check_row=6
    elif row > 2:
        begin_check_row=3
        
    if col > 5:
        begin_check_column=6
    elif col > 2:
        begin_check_column=3
    
    for i in range(begin_check_row,begin_check_row+3):
        for j in range(begin_check_column,begin_check_column+3):
            if can in sudoku_table[i][j][0] and i != row and j != col:
                sudoku_table[i][j][0].remove(can)
    return sudoku_table,passible_positions,pos,can

def generate_filled_sudoku():
    table = generating_all_candidates()
    passible_positions = generaing_all_positions()
    while len(passible_positions) != 0:
        for i in range(9):
            for j in range(9):
                if len(table[i][j][0])==0:
                    return generate_filled_sudoku()
        eliminate_candidates_after_choice(table,passible_positions)
    return table
"""