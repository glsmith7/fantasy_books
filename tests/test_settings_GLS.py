# test settings file

PATH_DEFAULT = "./tests/testSQL.db3"
SQL_QUERY_DEFAULT = "SELECT * FROM '_replace_'"
TABLE_NAME_DEFAULT = "TestTableReactionRollStandard"

# Test Constants for test_table_tools_GLS
test_get_column_names_constant = ['TestUniqueID','DiceFormula','DescriptionString','TestInteger01']

test_get_2d_array_constant = [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}, {'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}, {'TestUniqueID': 3, 'DiceFormula': '3d6+3', 'DescriptionString': 'Three', 'TestInteger01': 3123}, {'TestUniqueID': 4, 'DiceFormula': '4d6+4', 'DescriptionString': 'Four', 'TestInteger01': 4123}]

test_get_table_as_array_constant_01 = [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}, {'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}, {'TestUniqueID': 3, 'DiceFormula': '3d6+3', 'DescriptionString': 'Three', 'TestInteger01': 3123}, {'TestUniqueID': 4, 'DiceFormula': '4d6+4', 'DescriptionString': 'Four', 'TestInteger01': 4123}]

test_get_table_as_array_constant_02 = [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}]
test_get_table_as_array_constant_03 = [{'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}]

test_die_range_conversation_constant = [{'DieRange': '2-', 'Result': 'First', 'DieLow': -1000, 'DieHigh': 2}, {'DieRange': '3-5', 'Result': 'Second', 'DieLow': 3, 'DieHigh': 5}, {'DieRange': '6', 'Result': 'Third', 'DieLow': 6, 'DieHigh': 6}, {'DieRange': '7-11', 'Result': 'Fourth', 'DieLow': 7, 'DieHigh': 11}, {'DieRange': '12+', 'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}]

test_rolling_on_table_and_getting_row_test_data = [-999,2,3,6,7,12,999]
test_rolling_on_table_and_getting_row_desired_results_constant = [ 
         {'DieRange': '2-', 'Result': 'First', 'DieLow': -1000, 'DieHigh': 2},
         {'DieRange': '2-', 'Result': 'First', 'DieLow': -1000, 'DieHigh': 2},
         {'DieRange': '3-5', 'Result': 'Second', 'DieLow': 3, 'DieHigh': 5},
         {'DieRange': '6', 'Result': 'Third', 'DieLow': 6, 'DieHigh': 6},
         {'DieRange': '7-11', 'Result': 'Fourth', 'DieLow': 7, 'DieHigh': 11},
         {'DieRange': '12+', 'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000},
         {'DieRange': '12+', 'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}
     ]

test_roll_table_one_step_constant_1 = {'DieRange': '6', 'Result': 'Third', 'DieLow': 6, 'DieHigh': 6}
test_roll_table_one_step_constant_2 = {'DieRange': '2-', 'Result': 'First', 'DieLow': -1000, 'DieHigh': 2}