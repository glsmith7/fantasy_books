import sqlite3
# # import pytest
import sys
sys.path.append('../') # to see parallel folders for module import

# # # GLS modules
# # import logging_tools_GLS
import sql_wrapper_GLS as tested_module
import tests.test_settings_GLS as s

# proper test answers
test_1_answer = sqlite3.Connection
test_2_answer = ['Mercenary Type', 'Continent', 'Empire', 'Kingdom', 'Principality', 'Duchy', 'County', 'March', 'Barony', 'Restrictions', 'Race', 'Default Equipment']
test_3_answer = [('Light Infantry', 340000, 28000, 6800, 1600, 360, 85, 17, 3, 'None', 'Human,Nomad,Elf, Kobold, Goblin, Orc, Gnoll, Hobgob, Lizardman, Bugbear, Ogre', '3 javelins, short sword, shield, leather armor')]

# ## begin testing

def test_sql_wrapper_parts():
    test_connection = tested_module.connect_to_database()
    assert  type(test_connection) == test_1_answer

    test_column_names = tested_module.get_column_names(connection=test_connection,table_name="MercenaryTableRealms")
    assert test_column_names == test_2_answer

    test_full_table = tested_module.query_database (connection=test_connection, query = "SELECT * FROM MercenaryTableRealms WHERE Race LIKE '%Kobold%'")
    assert test_full_table == test_3_answer

def test_sql_wrapper_all_together_now():
    # testing the complete algorithm to return tables

    test_connection = tested_module.connect_to_database()
    assert  type(test_connection) == test_1_answer
    
    test_4_answer = ['TestUniqueID', 'DiceFormula', 'DescriptionString', 'TestInteger01']
    test_5_answer = [1, 2, 3, 4]
    test_6_answer = {1: {'DiceFormula': '1d6+1', 'DescriptionString': 'One', 'TestInteger01': 1123}, 2: {'DiceFormula': '2d6+2', 'DescriptionString': 'Two', 'TestInteger01': 2123}, 3: {'DiceFormula': '3d6+3', 'DescriptionString': 'Three', 'TestInteger01': 3123}, 4: {'DiceFormula': '4d6+4', 'DescriptionString': 'Four', 'TestInteger01': 4123}}

    # returns 3 values
    column_names, row_names, final_dictionary_of_table = tested_module.get_table_as_dict (table_name="TestTable01", query = None, connection=test_connection, path = s.PATH_DEFAULT)

    assert column_names == test_4_answer