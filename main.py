import random
import copy
import time



class Sudoku:
    def __init__(self, table):
        self.table = table

    @classmethod
    def create_empty(cls):
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
    
    def find_unfilled_positions(self) -> list:

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

    def fill_unconnected_squares(self):

        pos = self.find_unfilled_positions()
        if len(pos) != 81:
            return False
        
        digits1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        indexes =[]
        for k in range (3):
            indexes.append([(i,j) for i in range (0+k*3,3+k*3) for j in range (0+k*3,3+k*3)])
        
        for i in range (9):
            chosen = random.choice(digits1)
            digits1.remove(chosen)
            self.table[indexes[0][i][0]][indexes[0][i][1]] = chosen

            chosen = random.choice(digits2)
            digits2.remove(chosen)
            self.table[indexes[1][i][0]][indexes[1][i][1]] = chosen

            chosen = random.choice(digits3)
            digits3.remove(chosen)
            self.table[indexes[2][i][0]][indexes[2][i][1]] = chosen


    def generate_filled(self):

        self.fill_unconnected_squares()
        unfilled_positions = self.find_unfilled_positions()

        for position in unfilled_positions:
            digits =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for iteration in range(9): 
                chosen = random.choice(digits)
                if self.check_all(chosen,position[0],position[1]):

                    temp = copy.deepcopy(self.table)
                    self.table[position[0]][position[1]] = chosen
                    checking_by_solver = Solver(Sudoku(self.table)).solve()

                    if checking_by_solver != False:
                        self.table = temp
                        self.table[position[0]][position[1]] = chosen
                        break
                    else:
                        self.table = temp
                        digits.remove(chosen)
                else:
                    digits.remove(chosen)

class Solver:
    def __init__(self, sudoku_to_solve: Sudoku):
        self.sudoku_to_solve = sudoku_to_solve


    def solve(self) -> bool or Sudoku:

        unfilled = self.sudoku_to_solve.find_unfilled_positions()
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



class SudokuGenerator():

    def __init__(self):
        self.sudoku_to_mask = Sudoku.create_empty()
    
    def remove_fill(self, how_many_remain):

        positions= [(i,j) for i in range(9) for j in range(9)]

        while len(positions) != how_many_remain:
            chosen = random.choice(positions)
            self.sudoku_to_mask.table[chosen[0]][chosen[1]] = "X"
            positions.remove(chosen)
    
    def search_for_solutions(self, count=0):
        """
        This function has to receive count as 0 to work properly
        This function retruns 2 if there is no unique solution to Sudoku and 1 if there is one
        """
        unfilled = self.sudoku_to_mask.find_unfilled_positions()
        if unfilled == []:
            count = count+1
            return True
        row,col = unfilled[0][0],unfilled[0][1]
        for num in range (1,10):
            num = f"{num}"
            if count > 1:
                return 2
            if self.sudoku_to_mask.check_all(num, row, col):
                self.sudoku_to_mask.table[row][col] = num
            
                result = self.search_for_solutions(count)
                if type(result) == int:
                    if result > count:
                        count = result
                        if count > 1:
                            return 2
                
                elif result == True:
                    count += 1 
                    if count > 1:
                        return 2
            
                self.sudoku_to_mask.table[row][col] = 'X'
        return count


    def generate_single_solutional_sudoku(self, how_many_remain):

        if how_many_remain>=30:
            start = time.time()
            self.sudoku_to_mask.table = [["X" for i in range(9)] for j in range(9)]

            while True:
                self.sudoku_to_mask.generate_filled()
                self.remove_fill(how_many_remain)

                if self.search_for_solutions(0) == 1:
                    return self.sudoku_to_mask
                
                self.sudoku_to_mask.table = [["X" for i in range(9)] for j in range(9)]
                now = time.time()

                if now - start > 90:
                    break
        return "I cannot generate single solutional sudoku with that few numbers in reasonable time"


