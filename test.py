import main
import unittest


class TestSudokuTask(unittest.TestCase):
    TAB0 = [['X', '1', 'X', 'X', '2', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TABE = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
    
    TAB1 = [['9', '7', 'X', 'X', '2', '1', 'X', 'X', '8'],
            ['X', '2', '5', '4', '6', '8', 'X', '9', 'X'],
            ['X', 'X', 'X', 'X', '7', '9', 'X', 'X', '4'],
            ['5', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1'],
            ['X', '4', '9', 'X', 'X', 'X', 'X', 'X', '6'],
            ['6', '1', 'X', 'X', 'X', 'X', 'X', '4', 'X'],
            ['X', 'X', 'X', '9', '5', 'X', '7', 'X', 'X'],
            ['X', '5', '1', 'X', 'X', 'X', 'X', '8', 'X'],
            ['X', 'X', '3', 'X', 'X', '6', 'X', 'X', 'X']]
    
    TAB2 = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['2', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB3 = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB4 = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X'],
            ['X', '2', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB5 = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['4', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB6 = [['X', '1', 'X', 'X', '3', 'X', 'X', 'X', 'X'],
            ['X', '6', '8', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['7', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB7 = TAB6

    TAB8 = TAB6

    TAB9 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    TAB10 = [['6', '3', '7', '4', '1', '5', '2', '8', '9'],
             ['4', '1', '8', '2', '3', '9', '6', '5', '7'],
             ['2', '5', '9', '7', '6', '8', '3', '1', '4'],
             ['1', '2', '5', '9', '8', '3', '4', '7', '6'],
             ['8', '4', '6', '5', '7', '2', '9', '3', '1'],
             ['7', '9', '3', '6', '4', '1', '8', '2', '5'],
             ['3', '7', '1', '8', '9', '4', '5', '6', '2'],
             ['5', '8', '4', '1', '2', '6', '7', '9', '3'],
             ['9', '6', '2', '3', '5', '7', '1', '4', '8']]

    TAB11 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
             ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
             ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
             ['9', '1', '2', '3', '4', '5', '6', '7', '8'],
             ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
             ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
             ['2', '3', '1', '5', '6', '4', 'X', '7', 'X'],
             ['X', '6', '4', '8', 'X', 'X', 'X', 'X', 'X'],
             ['X', '9', '7', '2', 'X', 'X', '8', 'X', 'X']]

    TAB12 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', '4', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB13 = [['7', '4', '3', '8', '1', '2', '5', '9', '6'],
             ['2', '1', '5', '9', '3', '6', '4', '8', '7'],
             ['8', '9', '6', '7', '5', '4', '1', '2', '3'],
             ['1', '3', '7', '4', '2', '8', '9', '6', '5'],
             ['4', '6', '2', '3', '9', '5', '8', '7', '1'],
             ['9', '5', '8', '6', '7', '1', '3', '4', '2'],
             ['5', '8', 'X', '2', '6', '9', '7', '3', '4'],
             ['6', '7', '4', '5', '8', '3', '2', '1', '9'],
             ['3', '2', '9', '1', '4', '7', '6', '5', '8']]

    TAB14 = [['X', '8', 'X', 'X', '1', 'X', '5', '7', '9'],
             ['3', '1', '9', '5', '4', '7', '2', 'X', '8'],
             ['7', '5', '2', '6', 'X', '8', 'X', 'X', '1'],
             ['2', '9', '8', '1', '7', '5', '6', '4', '3'],
             ['1', '3', '5', '4', 'X', '2', '8', '9', '7'],
             ['X', 'X', '4', '8', 'X', '9', '1', '2', 'X'],
             ['X', '6', '3', 'X', '2', '1', '7', 'X', '4'],
             ['5', 'X', '7', 'X', '8', 'X', '9', '1', '6'],
             ['9', '4', '1', '7', '5', '6', 'X', '8', 'X']]

    def test_is_there_a_sudoku_with_correct_lengths(self):
        sudoku = main.Sudoku.for_empty()
        result_sudoku_table = sudoku.table

        expected_len = 9
        expected_elements = 1
        self.assertEqual(expected_len,len(result_sudoku_table))
        for i in range(expected_len):
            self.assertEqual(expected_len,len(result_sudoku_table[i]))
            for j in range(expected_len):
                self.assertEqual(expected_elements,len(result_sudoku_table[i][j]))

    def test_showing_the_board_correctly(self):
        result_sudoku_table = str(main.Sudoku.for_empty())
        digits = "X123456789"
        wall_1 = '|'
        wall_2 = '-'
        space = ' '
        divider = '\n'

        tab_wall_1 = []
        for k in range (3):
            for j in range(3):
                for i in range(7+23*j+92*k,23+23*j+92*k,8):
                    tab_wall_1.append(i)

        tab_wall_2 = [i for i in range(70,92,2)] + [i for i in range(162,184,2)]

        tab_spaces=[]
        for j in range(11):
            for i in range(0+j*23,22+j*23,2):
                tab_spaces.append(i)
        
        tab_n = [i for i in range(22,275,23)]

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

    def test_checking_row_for_number_given_num_and_position_returns_False_for_place_in_which_the_num_cant_be_in(self):
        inp_board = self.TAB0
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_row_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertFalse(result)

    def test_checking_row_for_number__given_num_and_position_returns_True__for_place_in_which_the_num_can_be_in(self):
        inp_board = self.TAB3
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_row_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertTrue(result)

    def test_checking_column_for_number_given_num_and_position_returns_False_for_place_in_which_the_num_cant_be_in(self):
        inp_board = self.TAB2
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_col_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertFalse(result)

    def test_checking_column_for_number_given_num_and_position_returns_True_for_place_in_which_the_num_can_be_in(self):
        inp_board = self.TAB5
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_col_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertTrue(result)

    def test_checking_square_for_number_given_num_and_position_returns_False_for_place_in_which_the_num_cant_be_in(self):
        inp_board = self.TAB4
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_square_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertFalse(result)

    def test_checking_square_for_number__given_num_and_position_returns_True_for_place_in_which_the_num_can_be_in(self):
        inp_board = self.TAB6
        inp_num = '2'
        inp_pos_x, inp_pos_y = 0,0
        sudoku = main.Sudoku(inp_board)
        result = sudoku.check_square_for_num(inp_num,inp_pos_x,inp_pos_y)
        self.assertTrue(result)

    def test_if_finding_unfilled_positions_retrun_contains_specific_X_position(self):
        inp_board = self.TAB7
        sudoku = main.Sudoku(inp_board)
        expected = [8,7]
        result = sudoku.find_unfilled_positions()
        self.assertIn(expected,result)

    def test_if_finding_unfilled_positions_retrun_not_contains_specific_not_X_position(self):
        inp_board = self.TAB8
        sudoku = main.Sudoku(inp_board)
        expected = [1,2]
        result = sudoku.find_unfilled_positions()
        self.assertNotIn(expected,result)

    def test_solver_given_filled_board_returns_True(self):
        inp_board = self.TAB9
        solver = main.Solver(main.Sudoku(inp_board))
        result = solver.solve()
        self.assertTrue(result)
    
    def test_solver_given_unfillable_board_retruns_False(self):
        inp_board = self.TAB11
        solver = main.Solver(main.Sudoku(inp_board))
        result = solver.solve()
        self.assertFalse(result)

    def test_solver_given_fillable_board_retruns_filled_board(self):
        inp_board = self.TAB12
        solver = main.Solver(main.Sudoku(inp_board))
        expected_X = 0
        exes=0
        result = solver.solve().table
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


    def test_whether_after_filling_three_unconnected_squares_other_remain_unfilled(self):
        filled = main.Sudoku.for_empty()
        filled.fill_unconnected_squares()
        result = filled.table
        expeceted = "X"
        indexes = [[0,1,2],[3,4,5],[6,7,8]]
        for i in range(9):
            for j in range (9):
                if not ((i in indexes[0] and j in indexes[0]) or (i in indexes[1] and j in indexes[1]) or (i in indexes[2] and j in indexes[2])):
                    self.assertEqual(expeceted,result[i][j])

    def test_whether_after_filling_three_unconnected_squares_three_squares_are_filled(self):
        filled = main.Sudoku.for_empty()
        filled.fill_unconnected_squares()
        result = filled.table
        expeceted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        indexes = [[0,1,2],[3,4,5],[6,7,8]]
        for i in range(9):
            for j in range (9):
                if (i in indexes[0] and j in indexes[0]) or (i in indexes[1] and j in indexes[1]) or (i in indexes[2] and j in indexes[2]):
                    self.assertIn(result[i][j],expeceted)

    def test_whether_generated_filled_sudoku_is_complitelly_filled(self):
        filled = main.Sudoku.for_empty()
        filled.generate_filled()
        result = filled.table
        not_expected = 'X'    
        for i in range(9):
            for j in range (9):
                self.assertNotEqual(result,not_expected)

    def test_whether_sudoku_fill_remover_removes_correct_number_of_positions(self):
        inp_how_many_remain = 10
        inp_board = self.TAB10
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = inp_board
        sudoku.remove_fill(inp_how_many_remain)
        result = sudoku.sudoku_to_mask.table
        count_remaining = 0    
        for i in range(9):
            for j in range (9):
                if result[i][j]!='X':
                    count_remaining+=1
        expected = inp_how_many_remain
        self.assertEqual(expected,count_remaining)


    def test_search_for_solutions_given_sudoku_with_unique_solution_returns_one(self):
        inp_table = self.TAB13
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = inp_table
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertEqual(result,expected)

    def test_search_for_solutions_given_sudoku_with_unique_solution_returns_one_second_time(self):
        inp_table = self.TAB14
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = inp_table
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertEqual(result,expected)

    def test_search_for_solutions_given_sudoku_with_more_than_one_solution_returns_more_than_one(self):
        inp_table = self.TAB1
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = inp_table
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertGreater(result,expected)

    def test_search_for_solutions_given_empty_sudoku_returns_more_than_one(self):
        inp_table = self.TABE
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = inp_table
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertGreater(result,expected)




    def test_whether_generating_single_solutional_sudoku_returns_sudoku_shown_correctly_if_creates_one(self):
        inp_how_many_remain = 80
        sudoku = main.SudokuGenerator()
        result = str(sudoku.generate_single_solutional_sudoku(inp_how_many_remain))
        
        digits = ['X','1','2','3','4','5','6','7','8','9']
        wall_1 = '|'
        wall_2 = '-'
        space = ' '
        divider = '\n'

        tab_wall_1 = []
        for k in range (3):
            for j in range(3):
                for i in range(7+23*j+92*k,23+23*j+92*k,8):
                    tab_wall_1.append(i)

        tab_wall_2 = [i for i in range(70,92,2)] + [i for i in range(162,184,2)]

        tab_spaces=[]
        for j in range(11):
            for i in range(0+j*23,22+j*23,2):
                tab_spaces.append(i)
        
        tab_n = [i for i in range(22,275,23)]

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


    def test_whether_generating_single_soulutional_sudoku_returns_message_if_fails_to_generate(self):
        inp_how_many_remain = 10
        sudoku = main.SudokuGenerator()
        result = sudoku.generate_single_solutional_sudoku(inp_how_many_remain)
        expected = "I cannot generate single solutional sudoku with that few numbers in risonable time"
        self.assertEqual(expected, result)