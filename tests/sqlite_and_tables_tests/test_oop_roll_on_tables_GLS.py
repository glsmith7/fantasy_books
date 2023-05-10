import sqlite3
import pytest
import sys
sys.path.append('../') # to see parallel folders for module import

# GLS modules
# import logging_tools_GLS
import oop_roll_on_tables_GLS as t
import tests.test_settings_GLS as s

# @pytest.mark.skip(reason = "Testing")
def test_OOP_database_and_tables_en_masse():
  
    test_path = s.PATH_DEFAULT
    test_query = s.SQL_QUERY_DEFAULT
    test_table = s.TABLE_NAME_DEFAULT

    sql_test = t.SQL_object_GLS(test_path) # tests base class
    assert type(sql_test) == t.SQL_object_GLS
    sql_test.connection.close()

    RPG_table_test = t.RPG_table(test_table,query = test_query, path = test_path) # tests subclass
    assert type (RPG_table_test) == t.RPG_table

    assert RPG_table_test.table_name == "TestTableReactionRollStandard"
    assert RPG_table_test.query == "SELECT * FROM 'TestTableReactionRollStandard'"
    assert RPG_table_test.column_names == ['Result']
    assert RPG_table_test.row_names == ['2-', '3-5', '6-8', '9-11', '12+']
    assert RPG_table_test.database_results == [{'Result': 'First', 'DieLow': -1000, 'DieHigh': 2}, {'Result': 'Second', 'DieLow': 3, 'DieHigh': 5}, {'Result': 'Third', 'DieLow': 6, 'DieHigh': 8}, {'Result': 'Fourth', 'DieLow': 9, 'DieHigh': 11}, {'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}]
    assert RPG_table_test.final_table == {'2-': {'Result': 'First', 'DieLow': -1000, 'DieHigh': 2}, '3-5': {'Result': 'Second', 'DieLow': 3, 'DieHigh': 5}, '6-8': {'Result': 'Third', 'DieLow': 6, 'DieHigh': 8}, '9-11': {'Result': 'Fourth', 'DieLow': 9, 'DieHigh': 11}, '12+': {'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}}
    assert RPG_table_test.roll(12) == {'Result': 'Fifth', 'DieLow': 12, 'DieHigh': 1000}
    RPG_table_test.connection.close()
