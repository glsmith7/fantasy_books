import sqlite3
import pytest
import sys
sys.path.append('../') # to see parallel folders for module import

# GLS modules
import logging_tools_GLS
import oop_tables_GLS as t
import tests.test_settings_GLS as s

# @pytest.mark.skip(reason = "Testing")
def test_OOP_database_and_tablesen_masse():
  
    test_path = s.PATH_DEFAULT
    test_query = s.SQL_QUERY_DEFAULT
    test_table = s.TABLE_NAME_DEFAULT

    sql_test = t.SQL_object_GLS(test_path) # tests base class
    assert type(sql_test) == t.SQL_object_GLS

    RPG_table_test = t.RPG_table(test_table,query = test_query) # tests subclass
    assert type (RPG_table_test) == t.RPG_table

    assert RPG_table_test.table_name == "TestTableReactionRollStandard"
    assert RPG_table_test.query == "SELECT * FROM 'TestTableReactionRollStandard'"
    assert RPG_table_test.column_names == ['DieRange', 'Result']
    assert RPG_table_test.database_results == [{'DieRange': '2-', 'Result': 'First', 'DieLow': -1000, 'DieHigh': 2}, {'DieRange': '3-5', 'Result': 'Second', 'DieLow': 3, 'DieHigh': 5}, {'DieRange': '6', 'Result': 'Third', 'DieLow': 6, 'DieHigh': 6}, {'DieRange': '7-11', 'Result': 'Fourth', 'DieLow': 7, 'DieHigh': 11}, {'DieRange': '12+', 'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}]