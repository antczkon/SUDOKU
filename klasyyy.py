import random

class Square:
    def __init__(self, n):
        self.n = n
        self.candidates = set(i for i in range(1,10))
        self.children = []
    
    def add_children(self,child):
        self.children.append(child)

    def return_childrean(self):
        return self.children

    def update_children_candidates(self):
        if len(self.children) != 0:
            for child in self.children:
                if child.value == 0:
                    child.candidates = self.candidates & child.candidates
                else:
                    child.candidates = set()

    def reset_self_candidates(self):
        self.candidates = set(i for i in range(1,10))
        for child in self.children:
            if child.value in self.candidates:
                self.candidates.remove(child.value)
            child.candidates = set(i for i in range(1,10))

class Row:
    def __init__(self, x):
        self.x = x
        self.candidates = set(i for i in range(1,10))
        self.children = []

    def __str__(self):
        to_print = ""
        for child in self.children:
            to_print+=str(child.value) + " "
        return to_print
    
    def add_children(self,child):
        self.children.append(child)

    def return_childrean(self):
        return self.children

    def update_children_candidates(self):
        if len(self.children) != 0:
            for child in self.children:
                if child.value == 0:
                    child.candidates = self.candidates & child.candidates
                else:
                    child.candidates = set()
    
    def reset_self_candidates(self):
        self.candidates = set(i for i in range(1,10))
        for child in self.children:
            if child.value in self.candidates:
                self.candidates.remove(child.value)
            child.candidates = set(i for i in range(1,10))

class Column:
    def __init__(self, y):
        self.y = y
        self.candidates = set(i for i in range(1,10))
        self.children = []
    
    def add_children(self,child):
        self.children.append(child)

    def return_childrean(self):
        return self.children

    def update_children_candidates(self):
        if len(self.children) != 0:
            for child in self.children:
                if child.value == 0:
                    child.candidates = self.candidates & child.candidates
                else:
                    child.candidates = set()

    def reset_self_candidates(self):
        self.candidates = set(i for i in range(1,10))
        for child in self.children:
            if child.value in self.candidates:
                self.candidates.remove(child.value)
            child.candidates = set(i for i in range(1,10))
class Field:
    def __init__(self, parent_row:Row, parent_column:Column, parent_square:Square):
        self.x = parent_row.x
        self.y = parent_column.y
        self.n = parent_square.n
        self.candidates = parent_row.candidates & parent_column.candidates & parent_square.candidates
        self.parents = [parent_row, parent_column, parent_square]
        self.value = 0
        
        parent_row.add_children(self)
        parent_column.add_children(self)
        parent_square.add_children(self)

    def __str__(self):
        return str(self.value)

    def update_parents_candidates(self):
        for parent in self.parents:
            if self.value in parent.candidates:
                parent.candidates.remove(self.value)

    def update_affected_fields_candidates(self):
        for parent in self.parents:
            parent.update_children_candidates()
    
    def update_candidates(self):
        self.update_parents_candidates()
        self.update_affected_fields_candidates()
    
    def reset_candidates(self):
        self.candidates = set(i for i in range(1,10))
        for parent in self.parents:
            parent.reset_self_candidates()
        self.update_candidates()

class Sudoku:
    def __init__(self):
        self.rows = []
        self.columns = []
        self.sqares = []
        self.fields = []
        for i in range (9):
            self.rows.append(Row(i))
            self.columns.append(Column(i))
            self.sqares.append(Square(i))
        for i in range(9):
            for j in range(9):
                n = i//3 + (j//3 * 3)
                self.fields.append(Field(self.rows[i],self.columns[j],self.sqares[n]))
    
    def __str__(self):
        to_print = ""
        for row in self.rows:
            to_print += row.__str__() + "\n"
        return to_print
    def find_unfilled_fields(self):
        unfilled = []
        for field in self.fields:
            if field.value == 0:
                unfilled.append(field)
        return unfilled

    def fill_unconnected_squares(self):
        pos = len(self.find_unfilled_fields())
        if pos != 81:
            return False
        
        digits1 = [1,2,3,4,5,6,7,8,9]
        digits2 = [1,2,3,4,5,6,7,8,9]
        digits3 = [1,2,3,4,5,6,7,8,9]
        indexes =[]
        for k in range (3):
            for j in range (0+k*3,3+k*3):
                for i in range (0+k*3,3+k*3):
                    indexes.append(i+9*j)
        print(indexes)

        for i in range (9):
            chosen = random.choice(digits1)
            digits1.remove(chosen)
            self.fields[indexes[i]].value = chosen
            self.fields[indexes[i]].update_candidates()

            chosen = random.choice(digits2)
            digits2.remove(chosen)
            self.fields[indexes[i+9]].value = chosen
            self.fields[indexes[i+9]].update_candidates()

            chosen = random.choice(digits3)
            digits3.remove(chosen)
            self.fields[indexes[i+18]].value = chosen
            self.fields[indexes[i+18]].update_candidates()


class Solver:
    def __init__(self, sudoku_to_solve: Sudoku):
        self.sudoku_to_solve = sudoku_to_solve


    def solve(self) -> bool or Sudoku:
        unfilled = self.sudoku_to_solve.find_unfilled_fields()
        if unfilled == []:
            return True
        print("---")
        print(self.sudoku_to_solve)
        row = unfilled[0].x
        column = unfilled[0].y
        for num in unfilled[0].candidates:
            print(num)
            print(self.sudoku_to_solve.fields[row*9+column].candidates)
            for parent in self.sudoku_to_solve.fields[row*9+column].parents:
                print(parent.candidates)
            if num in self.sudoku_to_solve.fields[row*9+column].candidates:
                unfilled[0].value = num
                unfilled[0].update_candidates()
                if self.solve():
                    return self.sudoku_to_solve
                
                field = self.sudoku_to_solve.fields[row*9+column]
                field.value = 0
                field.reset_candidates()
        
        return False

sud = Sudoku()
sud.fill_unconnected_squares()
for field in sud.fields:
    print(field.candidates)
for row in sud.rows:
    print(row)
print("---------------")
to_solve = Solver(sud)
solved = to_solve.solve()
for row in to_solve.sudoku_to_solve.rows:
    print(row)
print("---------------")
for row in sud.rows:
    print(row)