import sql_wrapper_GLS
import sqlite3
import logging_tools_GLS

def test_connect_to_database():
    path = "testSQL.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path)

    assert type(to_test) is sqlite3.Connection
    to_test.close()


def test_fail_connect_since_file_not_exist():
    path = "xxBogusNonexistantDatabase.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path)

    assert type(to_test) is not sqlite3.Connection # no connection since DB doesn't exist
    assert to_test is FileNotFoundError # returns FileNotFound if database doesn't exist


def test_query_fails_for_lack_of_connection_object():
    assert type (sql_wrapper_GLS.retrieve_from_database("Not A Connection", "Not A Query")) is sqlite3.DatabaseError


def test_query_fails_for_improper_SQL_query():

    path = "testSQL.db3"
    to_test = sql_wrapper_GLS.connect_to_database(path) # need a database Object to pass to test

    assert type (sql_wrapper_GLS.retrieve_from_database(to_test, "Not A Query")) is sqlite3.DatabaseError
    to_test.close()
    



