import rpg_tables as r
import random as random
import string as string
import d20
import pandas as pd
import sqlite3

path = "./sqlite_db/ACKS_SQL_01.db3"
query1 = "SELECT * from {}".format("_names_anglo_saxon_male")
query2 = "SELECT * from {}".format("_names_french_male")

conn = sqlite3.connect(path)

a = pd.read_sql_query(query1,conn)
b = pd.read_sql_query(query2,conn)
conn.close()

c = pd.concat([a,b], ignore_index=True)
print (a)
print (b)
print (c)