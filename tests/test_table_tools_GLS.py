import sql_wrapper_GLS
import sqlite3
import logging_tools_GLS
import pytest
import table_tools_GLS

def test_get_column_names():
    
    # connect
    path = "./tests/testSQL.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path)
    result_should_equal_this = ['TestUniqueID','DiceFormula','DescriptionString','TestInteger01']
    # create SQL query
    query = "PRAGMA table_info(TestTable01);"
    the_results = sql_wrapper_GLS.retrieve_from_database(to_test, query)

    # check results
    list_of_column_names = table_tools_GLS.give_column_names(the_results)

    assert list_of_column_names == result_should_equal_this

def test_get_2d_array():
    
    # desired results
    result_should_equal_this = [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}, {'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}, {'TestUniqueID': 3, 'DiceFormula': '3d6+3', 'DescriptionString': 'Three', 'TestInteger01': 3123}, {'TestUniqueID': 4, 'DiceFormula': '4d6+4', 'DescriptionString': 'Four', 'TestInteger01': 4123}]

    # connect
    path = "./tests/testSQL.db3"
    dB = sql_wrapper_GLS.connect_to_database(path)

    # get column names
    query = "PRAGMA table_info(TestTable01);"
    the_results = sql_wrapper_GLS.retrieve_from_database(dB, query)
    list_of_column_names = table_tools_GLS.give_column_names(the_results)

    # create SQL query for entire table
    query = "SELECT * from 'TestTable01'"
    results = sql_wrapper_GLS.retrieve_from_database(dB,query)

    # get 2D database
    results = table_tools_GLS.get_2d_array(list_of_column_names,results)

    assert results == result_should_equal_this
    

def test_get_table_as_array():
     # desired results
    result_should_equal_this = [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}, {'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}, {'TestUniqueID': 3, 'DiceFormula': '3d6+3', 'DescriptionString': 'Three', 'TestInteger01': 3123}, {'TestUniqueID': 4, 'DiceFormula': '4d6+4', 'DescriptionString': 'Four', 'TestInteger01': 4123}]
    
    # search factors
    path = "./tests/testSQL.db3"
    table_name = "TestTable01"

    # test with default search (the entire table)
    results = table_tools_GLS.get_table_as_array(path, table_name)
    assert results == result_should_equal_this

    # test with keyword search (an SQL search query included)
    results = table_tools_GLS.get_table_as_array(path, table_name, query="SELECT * FROM 'TestTable01' WHERE TestUniqueID = 1")
    assert results == [{'TestUniqueID': 1, 'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}]

    # test with keyword search (an SQL search query included, with "_replace_" to represent the table name
    results = table_tools_GLS.get_table_as_array(path, table_name, query="SELECT * FROM '_replace_' WHERE TestUniqueID = 2")
    assert results == [{'TestUniqueID': 2, 'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}]

def test_die_range_conversion():
      # desired results
    result_should_equal_this = [{'DieRange': '2-', 'Results': 'First', 'Order': 1, 'DieLow': -1000, 'DieHigh': 2}, {'DieRange': '3-5', 'Results': 'Second', 'Order': 2, 'DieLow': 3, 'DieHigh': 5}, {'DieRange': '6', 'Results': 'Third', 'Order': 3, 'DieLow': 6, 'DieHigh': 6}, {'DieRange': '7-11', 'Results': 'Fourth', 'Order': 4, 'DieLow': 7, 'DieHigh': 11}, {'DieRange': '12+', 'Results': 'Fifth', 'Order': 5, 'DieLow': 12, 'DieHigh': 1000}]
    
    # search factors
    path = "./tests/testSQL.db3"
    table_name = "TestTableReactionRollStandard"

    # test with
    results = table_tools_GLS.get_table_as_array(path, table_name)
    final_results = table_tools_GLS.convert_die_range_to_low_and_high(results)
    assert final_results == result_should_equal_this
