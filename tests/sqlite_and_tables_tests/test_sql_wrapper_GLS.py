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

test_connection = tested_module.connect_to_database()
assert  type(test_connection) == test_1_answer

test_column_names = tested_module.get_column_names(connection=test_connection,table_name="MercenaryTableRealms")
assert test_column_names == test_2_answer

test_full_table = tested_module.query_database (connection=test_connection, query = "SELECT * FROM MercenaryTableRealms WHERE Race LIKE '%Kobold%'")
assert test_full_table == test_3_answer
