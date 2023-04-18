import sql_wrapper_GLS
import sqlite3
import logging_tools_GLS
import pytest
import table_tools_GLS

def test_connect_to_database():
    path = "./tests/testSQL.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path)

    assert type(to_test) is sqlite3.Connection
    
    to_test.close()


def test_fail_connect_since_file_not_exist():
    with pytest.raises(FileNotFoundError):
        path = "xxBogusNonexistantDatabase.db3"
        to_test = sql_wrapper_GLS.connect_to_database(path)



def test_query_fails_for_lack_of_connection_object():
    assert type (sql_wrapper_GLS.retrieve_from_database("Not A Connection", "Not A Query")) is sqlite3.DatabaseError



def test_reading_database():
    def test_column1(the_results,first_column,x):
        assert (first_column) == the_results[x][0]

    def test_column2(the_results,second_column,x):
        assert (second_column) == the_results[x][1]

    def test_column3(the_results,third_column,x):
        assert (third_column) == the_results[x][2]

    def test_column4(the_results,fourth_column,x):
        assert (fourth_column) == the_results[x][3]
    # connect

    path = "./tests/testSQL.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path)

    # create SQL query
    query = "SELECT * FROM TestTable01"
    the_results = sql_wrapper_GLS.retrieve_from_database(to_test, query)
    
    sql_wrapper_GLS.print_SQL_results(the_results)

    the_words = ("One","Two","Three","Four") # these are in the 3rd column of the test database.

    for x in range(0,4): # there are 4 lines in test table
        first_column = x+1 # Column 0 of each row is numbered 1-4, hence x+1.
        second_column = str(first_column) + "d6+" + str(first_column)
        third_column = the_words[x]
        fourth_column = int(str(first_column) + str("123"))

        test_column1(the_results,first_column,x)
        test_column2(the_results,second_column,x)
        test_column3(the_results,third_column,x)
        test_column4(the_results,fourth_column,x)
    
    to_test.close()

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

