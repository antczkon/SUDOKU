import random
import copy


class Sudoku:
    def __init__(self, table):
        self.table = table

    @classmethod
    def for_empty(cls):
        return cls(table = [["X" for i in range(9)] for j in range(9)])
    
    def __str__(self):
        to_print = ''
        board = self.table
        for i in range (len(board)):
            if i == 3 or i == 6:
                to_print += ' - - - - - - - - - - -\n'
            for j in range (len(board[i])):
                if j == 0:
                    to_print += f" {board[i][j]} "
                elif j==8:
                    to_print += f"{board[i][j]}\n"
                elif j == 2 or j == 5:
                    to_print += f"{board[i][j]} | "
                else:
                    to_print += f"{board[i][j]} "
        return to_print


    def check_row_for_num(self, num, x, _) -> bool:
        row = self.table[x]
        for i in range(9):
            if row[i] == num:
                return False
        return True
    
    def check_col_for_num(self, num, _, y) -> bool:
        for i in range(9):
            if self.table[i][y] == num:
                return False
        return True
    
    def check_square_for_num(self, num, x, y) -> bool:
        begin_row = (x//3)*3
        begin_col = (y//3)*3
        for i in range (begin_row,begin_row+3):
            for j in range (begin_col, begin_col+3):
                if self.table[i][j] == num:
                    return False
        return True
    
    def find_unfilled_pos(self) -> list:

        tab=[]
        for i in range (9):
            for j in range (9):
                if self.table[i][j]=='X':
                    tab.append([i,j])
        return tab

    def check_all(self,num,x,y) -> bool:
        if self.check_col_for_num(num,x,y) and self.check_row_for_num(num,x,y) and self.check_square_for_num(num,x,y):
            return True
        return False


class Solver:
    def __init__(self, sudoku_to_solve: Sudoku):
        self.sudoku_to_solve = sudoku_to_solve


    def solve(self) -> bool or Sudoku:

        unfilled = self.sudoku_to_solve.find_unfilled_pos()
        if unfilled == []:
            return True
        row,col = unfilled[0][0],unfilled[0][1]
        for num in range (1,10):
            num = f"{num}"
            if self.sudoku_to_solve.check_all(num,row,col):
                self.sudoku_to_solve.table[row][col] = num
            
                if self.solve():
                    return self.sudoku_to_solve
            
                self.sudoku_to_solve.table[row][col] = 'X'
        
        return False
    

class FilledGenerator(Sudoku):
    
    def __init__(self):
        self.table = [["X" for i in range(9)] for j in range(9)]
    
    
    def fill_unconnected_squares(self) -> None:

        pos = self.find_unfilled_pos()
        if len(pos) != 81:
            return False
        digits1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        indexes = [[0,1,2],[3,4,5],[6,7,8]]
        
        for i in range (9):
            for j in range(9):
                if i in indexes[0] and j in indexes[0]:
                    chosen = random.choice(digits1)
                    digits1.remove(chosen)
                    self.table[i][j] = chosen
                elif i in indexes[1] and j in indexes[1]:
                    chosen = random.choice(digits2)
                    digits2.remove(chosen)
                    self.table[i][j] = chosen
                elif i in indexes[2] and j in indexes[2]:
                    chosen = random.choice(digits3)
                    digits3.remove(chosen)
                    self.table[i][j] = chosen


    def generate_filled(self) -> None:

        self.fill_unconnected_squares()
        unfilled_positions = self.find_unfilled_pos()
        for position in unfilled_positions:
            digits =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for iteration in range(9): 
                chosen = random.choice(digits)
                if self.check_all(chosen,position[0],position[1]):
                    temp = copy.deepcopy(self.table)
                    self.table[position[0]][position[1]] = chosen
                    board_to_be_checked_by_solver = copy.deepcopy(self.table)
                    checking_by_solver = Solver(Sudoku(board_to_be_checked_by_solver)).solve()
                    if checking_by_solver != False:
                        self.table = temp
                        self.table[position[0]][position[1]] = chosen
                        break
                    else:
                        self.table = temp
                        digits.remove(chosen)
                else:
                    digits.remove(chosen)


class SudokuGenerator(FilledGenerator):
    
    def fill_removal(self, how_many_remain):

        positions= [(i,j) for i in range(9) for j in range(9)]

        while len(positions) != how_many_remain:
            chosen = random.choice(positions)
            self.table[chosen[0]][chosen[1]] = "X"
            positions.remove(chosen)
    
    def check_how_many_solutions(self, count):

        unfilled = self.find_unfilled_pos()
        if unfilled == []:
            count = count+1
            return True
        row,col = unfilled[0][0],unfilled[0][1]
        for num in range (1,10):
            num = f"{num}"
            if count > 1:
                return 2
            if self.check_all(num, row, col):
                self.table[row][col] = num
            
                result = self.check_how_many_solutions(count)
                if type(result) == type(2):
                    if result > count:
                        count = result
                        if count > 1:
                            return 2
                
                elif result == True:
                    count += 1 
                    if count > 1:
                        return 2
            
                self.table[row][col] = 'X'
        return count

    def generate_single_solutional_final(self, how_many_remain):

        if how_many_remain>=30:
            while True:
                self.generate_filled()
                self.fill_removal(how_many_remain)
                if self.check_how_many_solutions(0) == 1:
                    return self
                self.table = [["X" for i in range(9)] for j in range(9)]
        return "I cannot generate single solutional sudoku with that few numbers"


