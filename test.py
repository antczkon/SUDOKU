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

    TAB7 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    TAB8 = [['6', '3', '7', '4', '1', '5', '2', '8', '9'],
            ['4', '1', '8', '2', '3', '9', '6', '5', '7'],
            ['2', '5', '9', '7', '6', '8', '3', '1', '4'],
            ['1', '2', '5', '9', '8', '3', '4', '7', '6'],
            ['8', '4', '6', '5', '7', '2', '9', '3', '1'],
            ['7', '9', '3', '6', '4', '1', '8', '2', '5'],
            ['3', '7', '1', '8', '9', '4', '5', '6', '2'],
            ['5', '8', '4', '1', '2', '6', '7', '9', '3'],
            ['9', '6', '2', '3', '5', '7', '1', '4', '8']]

    TAB9 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
            ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
            ['9', '1', '2', '3', '4', '5', '6', '7', '8'],
            ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
            ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
            ['2', '3', '1', '5', '6', '4', 'X', '7', 'X'],
            ['X', '6', '4', '8', 'X', 'X', 'X', 'X', 'X'],
            ['X', '9', '7', '2', 'X', 'X', '8', 'X', 'X']]

    TAB10 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', '4', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X']]

    TAB11 = [['7', '4', '3', '8', '1', '2', '5', '9', '6'],
             ['2', '1', '5', '9', '3', '6', '4', '8', '7'],
             ['8', '9', '6', '7', '5', '4', '1', '2', '3'],
             ['1', '3', '7', '4', '2', '8', '9', '6', '5'],
             ['4', '6', '2', '3', '9', '5', '8', '7', '1'],
             ['9', '5', '8', '6', '7', '1', '3', '4', '2'],
             ['5', '8', 'X', '2', '6', '9', '7', '3', '4'],
             ['6', '7', '4', '5', '8', '3', '2', '1', '9'],
             ['3', '2', '9', '1', '4', '7', '6', '5', '8']]

    TAB12 = [['X', '8', 'X', 'X', '1', 'X', '5', '7', '9'],
             ['3', '1', '9', '5', '4', '7', '2', 'X', '8'],
             ['7', '5', '2', '6', 'X', '8', 'X', 'X', '1'],
             ['2', '9', '8', '1', '7', '5', '6', '4', '3'],
             ['1', '3', '5', '4', 'X', '2', '8', '9', '7'],
             ['X', 'X', '4', '8', 'X', '9', '1', '2', 'X'],
             ['X', '6', '3', 'X', '2', '1', '7', 'X', '4'],
             ['5', 'X', '7', 'X', '8', 'X', '9', '1', '6'],
             ['9', '4', '1', '7', '5', '6', 'X', '8', 'X']]

    def test_is_there_a_sudoku_with_correct_lengths(self):
        sudoku = main.Sudoku.create_empty()
        result_sudoku_table = sudoku.table

        self.assertEqual(9,len(result_sudoku_table))
        for i in range(9):
            self.assertEqual(9,len(result_sudoku_table[i]))
            for j in range(9):
                self.assertEqual(1,len(result_sudoku_table[i][j]))

    def test_showing_the_board_correctly(self):
        result_sudoku_table = str(main.Sudoku.create_empty())
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
        sudoku = main.Sudoku(self.TAB0)
        result = sudoku.check_row_for_num('2',0,0)
        self.assertFalse(result)

    def test_checking_row_for_number__given_num_and_position_returns_True__for_place_in_which_the_num_can_be_in(self):
        sudoku = main.Sudoku(self.TAB3)
        result = sudoku.check_row_for_num('2',0,0)
        self.assertTrue(result)

    def test_checking_column_for_number_given_num_and_position_returns_False_for_place_in_which_the_num_cant_be_in(self):
        sudoku = main.Sudoku(self.TAB2)
        result = sudoku.check_col_for_num('2',0,0)
        self.assertFalse(result)

    def test_checking_column_for_number_given_num_and_position_returns_True_for_place_in_which_the_num_can_be_in(self):
        sudoku = main.Sudoku(self.TAB5)
        result = sudoku.check_col_for_num('2',0,0)
        self.assertTrue(result)

    def test_checking_square_for_number_given_num_and_position_returns_False_for_place_in_which_the_num_cant_be_in(self):
        sudoku = main.Sudoku(self.TAB4)
        result = sudoku.check_square_for_num('2',0,0)
        self.assertFalse(result)

    def test_checking_square_for_number__given_num_and_position_returns_True_for_place_in_which_the_num_can_be_in(self):
        sudoku = main.Sudoku(self.TAB6)
        result = sudoku.check_square_for_num('2',0,0)
        self.assertTrue(result)

    def test_if_finding_unfilled_positions_retrun_contains_specific_X_position(self):
        sudoku = main.Sudoku(self.TAB6)
        expected = [8,7]
        result = sudoku.find_unfilled_positions()
        self.assertIn(expected,result)

    def test_if_finding_unfilled_positions_retrun_not_contains_specific_not_X_position(self):
        sudoku = main.Sudoku(self.TAB6)
        expected = [1,2]
        result = sudoku.find_unfilled_positions()
        self.assertNotIn(expected,result)

    def test_solver_given_filled_board_returns_True(self):
        solver = main.Solver(main.Sudoku(self.TAB7))
        result = solver.solve()
        self.assertTrue(result)
    
    def test_solver_given_unfillable_board_retruns_False(self):
        solver = main.Solver(main.Sudoku(self.TAB9))
        result = solver.solve()
        self.assertFalse(result)

    def test_solver_given_fillable_board_retruns_filled_board(self):
        solver = main.Solver(main.Sudoku(self.TAB10))
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
        self.assertEqual(0,exes)


    def test_whether_after_filling_three_unconnected_squares_other_remain_unfilled(self):
        filled = main.Sudoku.create_empty()
        filled.fill_unconnected_squares()
        result = filled.table
        expeceted = "X"
        indexes =[]
        for k in range (3):
            indexes += [(i,j) for i in range (0+k*3,3+k*3) for j in range (0+k*3,3+k*3)]
        for i in range(9):
            for j in range (9):
                if (i,j) not in indexes:
                    self.assertEqual(expeceted,result[i][j])

    def test_whether_after_filling_three_unconnected_squares_three_squares_are_filled(self):
        filled = main.Sudoku.create_empty()
        filled.fill_unconnected_squares()
        result = filled.table
        expeceted = '123456789'
        indexes =[]
        for k in range (3):
            indexes += [(i,j) for i in range (0+k*3,3+k*3) for j in range (0+k*3,3+k*3)]
        for i in range(9):
            for j in range (9):
                if (i,j) in indexes:
                    self.assertIn(result[i][j],expeceted)

    def test_whether_generated_filled_sudoku_is_complitelly_filled(self):
        filled = main.Sudoku.create_empty()
        filled.generate_filled()
        result = filled.table
        expeceted = '123456789'    
        for i in range(9):
            for j in range (9):
                self.assertIn(result[i][j],expeceted)

    def test_whether_sudoku_fill_remover_removes_correct_number_of_positions(self):
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = self.TAB8
        sudoku.remove_fill(10)
        result = sudoku.sudoku_to_mask.table
        count_remaining = 0    
        for i in range(9):
            for j in range (9):
                if result[i][j]!='X':
                    count_remaining+=1
        expected = 10
        self.assertEqual(expected,count_remaining)


    def test_search_for_solutions_given_sudoku_with_unique_solution_returns_one(self):
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = self.TAB11
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertEqual(result,expected)

    def test_search_for_solutions_given_sudoku_with_unique_solution_returns_one_second_time(self):
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = self.TAB12
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertEqual(result,expected)

    def test_search_for_solutions_given_sudoku_with_more_than_one_solution_returns_more_than_one(self):
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = self.TAB1
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertGreater(result,expected)

    def test_search_for_solutions_given_empty_sudoku_returns_more_than_one(self):
        sudoku = main.SudokuGenerator()
        sudoku.sudoku_to_mask.table = self.TABE
        result = sudoku.search_for_solutions()
        expected = 1
        self.assertGreater(result,expected)




    def test_whether_generating_single_solutional_sudoku_returns_sudoku_shown_correctly_if_creates_one(self):
        sudoku = main.SudokuGenerator()
        result = str(sudoku.generate_single_solutional_sudoku(80))
        
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
        sudoku = main.SudokuGenerator()
        result = sudoku.generate_single_solutional_sudoku(10)
        expected = "I cannot generate single solutional sudoku with that few numbers in reasonable time"
        self.assertEqual(expected, result)