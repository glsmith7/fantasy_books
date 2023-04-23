import pytest
import sqlite3

#GLS modules
import logging_tools_GLS
import sql_wrapper_GLS
import table_tools_GLS
import tests.test_settings_GLS as s




def test_connect_to_database():
    path = s.PATH_DEFAULT
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

    path = s.PATH_DEFAULT
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



