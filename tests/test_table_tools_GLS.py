import sqlite3
import pytest

# GLS modules
import logging_tools_GLS
import sql_wrapper_GLS
import table_tools_GLS
import test_settings_GLS as s


def test_get_column_names():
    
    # connect
    path = s.PATH_DEFAULT
    to_test = sql_wrapper_GLS.connect_to_database(path)
    result_should_equal_this = s.test_get_column_names_constant
    # create SQL query
    query = "PRAGMA table_info(TestTable01);"
    the_results = sql_wrapper_GLS.retrieve_from_database(to_test, query)

    # check results
    list_of_column_names = table_tools_GLS.give_column_names(the_results)

    assert list_of_column_names == result_should_equal_this

def test_get_2d_array():
    
    # desired results
    result_should_equal_this = s.test_get_2d_array_constant

    # connect
    path = s.PATH_DEFAULT
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
    result_should_equal_this = s.test_get_table_as_array_constant_01
    
    # search factors
    path = s.PATH_DEFAULT
    table_name = "TestTable01"

    # test with default search (the entire table)
    results = table_tools_GLS.get_table_as_array(path, table_name)
    assert results == result_should_equal_this

    # test with keyword search (an SQL search query included)
    results = table_tools_GLS.get_table_as_array(path, table_name, query="SELECT * FROM 'TestTable01' WHERE TestUniqueID = 1")
    assert results == s.test_get_table_as_array_constant_02

    # test with keyword search (an SQL search query included, with "_replace_" to represent the table name
    results = table_tools_GLS.get_table_as_array(path, table_name, query="SELECT * FROM '_replace_' WHERE TestUniqueID = 2")
    assert results == s.test_get_table_as_array_constant_03

def test_die_range_conversion():
      # desired results
    result_should_equal_this = s.test_die_range_conversation_constant
    
    # search factors
    path = s.PATH_DEFAULT
    table_name = "TestTableReactionRollStandard"

    # test with
    results = table_tools_GLS.get_table_as_array(path, table_name)
    final_results = table_tools_GLS.convert_die_range_to_low_and_high(results)
    assert final_results == result_should_equal_this

def test_rolling_on_table_and_getting_row():
     path = s.PATH_DEFAULT
     table_name = "TestTableReactionRollStandard"
     test_data = s.test_rolling_on_table_and_getting_row_test_data
     
     desired_results = s.test_rolling_on_table_and_getting_row_desired_results_constant

     table_as_array = (table_tools_GLS.get_table_as_array(path,table_name,query="SELECT * FROM '_replace_'"))
     final_dictionary = (table_tools_GLS.convert_die_range_to_low_and_high(table_as_array))
     
     counter = 0
     for dice_roll in test_data:
         assert table_tools_GLS.table_roll(final_dictionary,dice_roll) == desired_results[counter]
         counter += 1

def test_roll_table_one_step():
    desired_results_1 = s.test_roll_table_one_step_constant_1
    desired_results_2 = s.test_roll_table_one_step_constant_2
    feed_result_on_table = table_tools_GLS.roll_table_one_step("TestTableReactionRollStandard",path = s.PATH_DEFAULT,result=6)

    assert feed_result_on_table == desired_results_1

    roll_result_on_table = table_tools_GLS.roll_table_one_step("TestTableReactionRollStandard",path = s.PATH_DEFAULT,roll="1d2") # 1d2 so always 1-2 to be sure matches

    assert roll_result_on_table == desired_results_2