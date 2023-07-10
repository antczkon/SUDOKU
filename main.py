import random
import copy


class Sudoku:
    def __init__(self):
        self.table = [["X" for i in range(9)] for j in range(9)]


    def show(self):
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

    def check_row_for_num(self, num, x, y):
        row = self.table[x]
        for i in range(9):
            if row[i] == num:
                return False
        return True
    
    def check_col_for_num(self, num, x, y):
        for i in range(9):
            if self.table[i][y] == num:
                return False
        return True
    
    def check_square_for_num(self, num, x, y):
        begin_row = (x//3)*3
        begin_col = (y//3)*3
        for i in range (begin_row,begin_row+3):
            for j in range (begin_col, begin_col+3):
                if self.table[i][j] == num:
                    return False
        return True
    
    def find_unfilled_pos(self):
        tab=[]
        for i in range (9):
            for j in range (9):
                if self.table[i][j]=='X':
                    tab.append([i,j])
        return tab
    
    def solver(self):
        unfilled = self.find_unfilled_pos()
        if unfilled == []:
            return True
        row,col = unfilled[0][0],unfilled[0][1]
        for num in range (1,10):
            num = f"{num}"
            if self.check_row_for_num(num,row,col) and self.check_col_for_num(num,row,col) and self.check_square_for_num(num,row,col):
                self.table[row][col] = num
            
                if self.solver():
                    return self.table
            
                self.table[row][col] = 'X'
        
        return False
    
    def fill_unconnected_squares(self):
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

    def check_all(self,num,x,y):
        if self.check_col_for_num(num,x,y) and self.check_row_for_num(num,x,y) and self.check_square_for_num(num,x,y):
            return True
        return False

    def generate_filled(self):
        self.fill_unconnected_squares()
        unfilled_positions = self.find_unfilled_pos()
        for position in unfilled_positions:
            for iteration in range(9): 
                digits =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                chosen = random.choice(digits)
                if self.check_all(chosen,position[0],position[1]):
                    temp = self.table
                    self.table[position[0]][position[1]] = chosen
                    if self.solver() != False:
                        self.table = temp
                        self.table[position[0]][position[1]] = chosen
                        break
                    else:
                        self.table = temp
                        digits.remove(chosen)
                else:
                    digits.remove(chosen)
    def check_filler(self):
        unfilled_positions = self.find_unfilled_pos()
        for position in unfilled_positions: 
            digits =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for iteration in range(9):
                chosen = random.choice(digits)
                if self.check_all(chosen,position[0],position[1]):
                    temp = self.table
                    self.table[position[0]][position[1]] = chosen
                    if self.solver() != False:
                        self.table = temp
                        self.table[position[0]][position[1]] = chosen
                        break
                    else:
                        self.table = temp
                        digits.remove(chosen)
                else:
                    digits.remove(chosen)
    def fill_removal(self, how_many_remain):
        positions= []
        for i in range (9):
            for j in range (9):
                positions.append([i,j])
        while len(positions) != how_many_remain:
            chosen = random.choice(positions)
            self.table[chosen[0]][chosen[1]] = "X"
            positions.remove(chosen)

    
    def generate_single_solutional(self, how_many_remain):
        self.generate_filled()
        self.fill_removal(how_many_remain)

        after_removal = copy.deepcopy(self.table)

        random.seed(10)
        self.check_filler()
        first_try = copy.deepcopy(self.table)
        self.table = copy.deepcopy(after_removal)


        random.seed(11)
        self.check_filler()
        second_try = copy.deepcopy(self.table)
        self.table = copy.deepcopy(after_removal)


        random.seed(12)
        self.check_filler()
        third_try = copy.deepcopy(self.table)
        self.table = copy.deepcopy(after_removal)

        if first_try != second_try or first_try != third_try:
            self.table = [["X" for i in range(9)] for j in range(9)]
            return False

    def generate_single_solutional_final(self, how_many_remain):
        for i in range (100):
            seed = random.randint(0,100)
            random.seed(seed)
            if self.generate_single_solutional(how_many_remain) != False:
                return self.show()
        return "I cannot generate single solutional sudoku with that few numbers"

sud = Sudoku()
print(sud.generate_single_solutional_final(40))