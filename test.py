import main
import unittest

class TestDictDates(unittest.TestCase):

    def test_is_there_a_sudoku_with_correct_lengths(self):
        result_sudoku_table = main.Sudoku().table

        expected_len = 9
        expected_elements = 1
        self.assertEqual(expected_len,len(result_sudoku_table))
        for i in range(expected_len):
            self.assertEqual(expected_len,len(result_sudoku_table[i]))
            for j in range(expected_len):
                self.assertEqual(expected_elements,len(result_sudoku_table[i][j]))

    def test_showing_the_board_correctly(self):
        result_sudoku_table = main.Sudoku().show()
        digits = ['X','1','2','3','4','5','6','7','8','9']
        wall_1 = '|'
        wall_2 = '-'
        space = ' '
        divider = '\n'
        tab_wall_1=[7, 15, 30, 38, 53, 61, 99, 107, 122, 130, 145, 153, 191, 199, 214, 222, 237, 245]
        tab_wall_2=[70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182]
        tab_spaces =[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250]
        tab_n=[22, 45, 68, 91, 114, 137, 160, 183, 206, 229, 252]
        for i in range(len(result_sudoku_table)):
            if i in tab_wall_1:
                self.assertEqual(result_sudoku_table[i],wall_1)
            elif i in tab_wall_2:
                self.assertEqual(result_sudoku_table[i],wall_2)
            elif i in tab_n:
                self.assertEqual(result_sudoku_table[i],divider)
            elif i in tab_spaces:
                self.assertEqual(result_sudoku_table[i],space)
            else:
                self.assertIn(result_sudoku_table[i],digits)

    def test_checking_row_for_number_given_num_and_position_returns_False(self):
        inp_board = [['X', '1', 'X', 'X', '2', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_row_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = False
        self.assertEqual(expected,result)

    def test_checking_row_for_number__given_num_and_position_returns_True(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_row_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = True
        self.assertEqual(expected,result)

    def test_checking_column_for_number_given_num_and_position_returns_False(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['2', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_col_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = False
        self.assertEqual(expected,result)

    def test_checking_column_for_number_given_num_and_position_returns_True(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['4', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_col_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = True
        self.assertEqual(expected,result)

    def test_checking_square_for_number_given_num_and_position_returns_False(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', '2', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_square_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = False
        self.assertEqual(expected,result)

    def test_checking_square_for_number__given_num_and_position_returns_True(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', '6', '8', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.check_square_for_num(inp_num,inp_pos_x,inp_pos_y)
        expected = True
        self.assertEqual(expected,result)

    def test_finding_unfilled_positions_retruns_all_X_positions_t(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', '6', '8', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        expected = [8,7]
        result = sudoku.find_unfilled_pos()
        self.assertIn(expected,result)

    def test_finding_unfilled_positions_retruns_all_X_positions_f(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', '6', '8', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        expected = [1,2]
        result = sudoku.find_unfilled_pos()
        self.assertNotIn(expected,result)

    def test_solver_given_filled_board_returns_True(self):
        inp_board = [['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['1', '2', '3', '4', '5', '6', '7', '8', '9']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        expected = True
        result = sudoku.solver()
        self.assertEqual(expected,result)
    
    def test_solver_given_unfillable_board_retruns_False(self):
        inp_board = [['1', '2', '3', '4', '5', '6', '7', '8', '9']
                     ,['7', '8', '9', '1', '2', '3', '4', '5', '6']
                     ,['4', '5', '6', '7', '8', '9', '1', '2', '3']
                     ,['9','1', '2', '3', '4', '5', '6', '7', '8']
                     ,['6', '7', '8', '9','1', '2', '3', '4', '5']
                     ,['3', '4', '5', '6', '7', '8', '9', '1', '2']
                     ,['2', '3', '1', '5', '6', '4', 'X', '7', 'X']
                     ,['X', '6', '4', '8', 'X', 'X', 'X', 'X', 'X']
                     ,['X', '9', '7', '2', 'X', 'X', '8', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        expected = False
        result = sudoku.solver()
        self.assertEqual(expected,result)

    def test_solver_given_fillable_board_retruns_filled_board(self):
        inp_board = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', '4', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        expected_X = 0
        exes=0
        result = sudoku.solver()
        tab = []
        self.assertEqual(type(result),type(tab))
        self.assertEqual(len(result),9)
        for i in range(9):
            self.assertEqual(len(result[i]),9)
        for i in range (9):
            for j in range (9):
                if result[i][j]=='X':
                    exes+=1
        self.assertEqual(expected_X,exes)
    
    def test_wheather_filling_three_unconnected_squares_returns_false_when_given_partially_filled_board(self):
        inp_board = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X']
                     , ['X', '2', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
                     , ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        result = sudoku.fill_unconnected_squares()
        expected = False
        self.assertEqual(result,expected)

    def test_wheather_after_filling_three_unconnected_squares_other_remain_unfilled(self):
        sudoku = main.Sudoku()
        sudoku.fill_unconnected_squares()
        result = sudoku.table
        expeceted = "X"
        indexes = [[0,1,2],[3,4,5],[6,7,8]]
        for i in range(9):
            for j in range (9):
                if not ((i in indexes[0] and j in indexes[0]) or (i in indexes[1] and j in indexes[1]) or (i in indexes[2] and j in indexes[2])):
                    self.assertEqual(expeceted,result[i][j])

    def test_wheather_three_squares_are_filled(self):
        sudoku = main.Sudoku()
        sudoku.fill_unconnected_squares()
        result = sudoku.table
        expeceted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        indexes = [[0,1,2],[3,4,5],[6,7,8]]
        for i in range(9):
            for j in range (9):
                if (i in indexes[0] and j in indexes[0]) or (i in indexes[1] and j in indexes[1]) or (i in indexes[2] and j in indexes[2]):
                    self.assertIn(result[i][j],expeceted)

    def test_wheather_generated_sudoku_is_complitelly_filled(self):
        sudoku = main.Sudoku()
        sudoku.generate_filled()
        result = sudoku.table
        not_expected = 'X'    
        for i in range(9):
            for j in range (9):
                self.assertNotEqual(result,not_expected)
    
    def test_whether_sudoku_fill_remover_removes_correct_number_of_positions(self):
        inp_how_many_remain = 10
        inp_board = [['6', '3', '7', '4', '1', '5', '2', '8', '9']
                     , ['4', '1', '8', '2', '3', '9', '6', '5', '7']
                     , ['2', '5', '9', '7', '6', '8', '3', '1', '4']
                     , ['1', '2', '5', '9', '8', '3', '4', '7', '6']
                     , ['8', '4', '6', '5', '7', '2', '9', '3', '1']
                     , ['7', '9', '3', '6', '4', '1', '8', '2', '5']
                     , ['3', '7', '1', '8', '9', '4', '5', '6', '2']
                     , ['5', '8', '4', '1', '2', '6', '7', '9', '3']
                     , ['9', '6', '2', '3', '5', '7', '1', '4', '8']]
        sudoku = main.Sudoku()
        sudoku.table = inp_board
        sudoku.fill_removal(inp_how_many_remain)
        result = sudoku.table
        count_remaining = 0    
        for i in range(9):
            for j in range (9):
                if result[i][j]!='X':
                    count_remaining+=1
        expected = inp_how_many_remain
        self.assertEqual(expected,count_remaining)

    def test_checking_how_many_solutions_given_sudoku_with_unique_solution_returns_one(self):
        inp_table = [['7', '4', '3', '8', '1', '2', '5', '9', '6']
                     , ['2', '1', '5', '9', '3', '6', '4', '8', '7']
                     , ['8', '9', '6', '7', '5', '4', '1', '2', '3']
                     , ['1', '3', '7', '4', '2', '8', '9', '6', '5']
                     , ['4', '6', '2', '3', '9', '5', '8', '7', '1']
                     , ['9', '5', '8', '6', '7', '1', '3', '4', '2']
                     , ['5', '8', 'X', '2', '6', '9', '7', '3', '4']
                     , ['6', '7', '4', '5', '8', '3', '2', '1', '9']
                     , ['3', '2', '9', '1', '4', '7', '6', '5', '8']]
        sudoku = main.Sudoku()
        sudoku.table = inp_table
        result = sudoku.check_how_many_solutions(0)
        expected = 1
        self.assertEqual(result,expected)

    def test_checking_how_many_solutions_given_sudoku_with_unique_solution_returns_one_2(self):
        inp_table = [['X', '8', 'X', 'X', '1', 'X', '5', '7', '9']
                     , ['3', '1', '9', '5', '4', '7', '2', 'X', '8']
                     , ['7', '5', '2', '6', 'X', '8', 'X', 'X', '1']
                     , ['2', '9', '8', '1', '7', '5', '6', '4', '3']
                     , ['1', '3', '5', '4', 'X', '2', '8', '9', '7']
                     , ['X', 'X', '4', '8', 'X', '9', '1', '2', 'X']
                     , ['X', '6', '3', 'X', '2', '1', '7', 'X', '4']
                     , ['5', 'X', '7', 'X', '8', 'X', '9', '1', '6']
                     , ['9', '4', '1', '7', '5', '6', 'X', '8', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_table
        result = sudoku.check_how_many_solutions(0)
        expected = 1
        self.assertEqual(result,expected)
    def test_checking_how_many_solutions_given_sudoku_with_more_than_one_solution_returns_more_than_one(self):
        inp_table = [['9', '7', 'X', 'X', '2', '1', 'X', 'X', '8']
                     , ['X', '2', '5', '4', '6', '8', 'X', '9', 'X']
                     , ['X', 'X', 'X', 'X', '7', '9', 'X', 'X', '4']
                     , ['5', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
                     , ['X', '4', '9', 'X', 'X', 'X', 'X', 'X', '6']
                     , ['6', '1', 'X', 'X', 'X', 'X', 'X', '4', 'X']
                     , ['X', 'X', 'X', '9', '5', 'X', '7', 'X', 'X']
                     , ['X', '5', '1', 'X', 'X', 'X', 'X', '8', 'X']
                     , ['X', 'X', '3', 'X', 'X', '6', 'X', 'X', 'X']]
        sudoku = main.Sudoku()
        sudoku.table = inp_table
        result = sudoku.check_how_many_solutions(0)
        expected = 1
        self.assertGreater(result,expected)
    
    def test_wheather_generating_single_solutional_final_returns_sudoku_if_creates_one(self):
        inp_how_many_remain = 80
        sudoku = main.Sudoku()
        result = sudoku.generate_single_solutional_final(inp_how_many_remain)
        digits = ['X','1','2','3','4','5','6','7','8','9']
        wall_1 = '|'
        wall_2 = '-'
        space = ' '
        divider = '\n'
        tab_wall_1=[7, 15, 30, 38, 53, 61, 99, 107, 122, 130, 145, 153, 191, 199, 214, 222, 237, 245]
        tab_wall_2=[70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182]
        tab_spaces =[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250]
        tab_n=[22, 45, 68, 91, 114, 137, 160, 183, 206, 229, 252]
        for i in range(len(result)):
            if i in tab_wall_1:
                self.assertEqual(result[i],wall_1)
            elif i in tab_wall_2:
                self.assertEqual(result[i],wall_2)
            elif i in tab_n:
                self.assertEqual(result[i],divider)
            elif i in tab_spaces:
                self.assertEqual(result[i],space)
            else:
                self.assertIn(result[i],digits)


    def test_wheather_generating_single_soulutional_final_returns_message_if_fails_to_generate(self):
        inp_how_many_remain = 10
        sudoku = main.Sudoku()
        result = sudoku.generate_single_solutional_final(inp_how_many_remain)
        expected = "I cannot generate single solutional sudoku with that few numbers"
        self.assertEqual(expected, result)