import sql_wrapper_GLS as sqlW
import logging_tools_GLS as log
import re # reg expressions

def give_column_names(results):
    col_names = []
    for row in results:
        col_names.append(row[1])
    
    log.logging.info ("Column names returned as: " + str(col_names) + "\n")
    return col_names

def get_2d_array(columns, results):
    """ Returns a list with nested dictionaries. Each dictionary is a row of the table, with columns of the table as keywords
    
        j = iterates through each row
        i = iterates through each column
        columns = list containing name of each column
        results = SQL search result
    """

    for j in range (0,len(results)):
        d = {} # Empty the dictionary before each row started

        for i in range (0,len(columns)):
            d[columns[i]] = results[j][i]
        
        results[j] = d # set the row of results to the dictionary value
    
    rows_and_columns_log_message = "There are {} columns and {} rows in the 2D array.".format(len(columns),len(results))
    log.logging.info ("2D array is returned as: " + str(results) + "\n")
    log.logging.info (rows_and_columns_log_message + "\n")

    return results

def get_table_as_array(path, table_name, query = "Select * FROM(_replace_)", ): 
    """ Combines various subroutines to get a 2D array with in a single called step.
    path = path to an SQLite database.
    table_name = table name
    query = optional SQL query. If omitted, returns entire table. If query includes "_replace_", the _replace_ string will be automatically replaced with the table name."""

    dB = sqlW.connect_to_database(path)
    
    # get column names
    query_column = "PRAGMA table_info({});".format(table_name)
    column_results = sqlW.retrieve_from_database(dB, query_column)
    column_names = give_column_names(column_results)
    
    # replace the placeholder with tablename if it was included. Otherwise use the passed SQL query as is
    query = query.replace("_replace_",table_name)
    
    # get the full table
    
    full_table_results = sqlW.retrieve_from_database(dB, query)

    # create 2D array with column names as dictionary key words
    table_as_array = get_2d_array (column_names, full_table_results)
    
    return table_as_array

def convert_die_range_to_low_and_high(d):
    """
    Takes a 2-d table array as dictionary, and adds in the high and low dice values for each row.
        
        Converts 2- into 'DiceLow': -1000, 'DiceHigh':2 -- i.e., anything 2 or lower
        Converts 12+ into 'DiceLow': 12, 'DiceHigh':1000 -- i.e., anything 12 or higher
        Converts 3-7 into 'DiceLow': 3, 'DiceHigh':7
        Converts 9 into 'DiceLow': 9, 'DiceHigh':9

    NB: Direct copy/paste from ACKS PDF gives an en-dash, not a minus sign, for the "-" character, so be sure is in properly in the SQL database.
    """

# determine what kind of value in each row, returns true or false

    def die_is_low_range(die_range): # eg, "2-", two or lower
        reg_ex_string = r"\-$" # ie minus sign at end of string

        if (re.search(reg_ex_string,die_range)):
            return True
        else:
            return False
        

    def die_is_high_range(die_range): # eg "12+", twelve or higher
        reg_ex_string = r"\+$" # ie plus sign at end of string

        if (re.search(reg_ex_string,die_range)):
            return True
        else:
            return False
    
    def die_is_mid_range(die_range): # eg "7-9", ie, between 7 and 12.
        reg_ex_string = r"\-" # ie minus sign anywhere but end (at end will have been caught already)

        if (re.search(reg_ex_string,die_range)):
            return True
        else:
            return False

    def die_is_single_digit(die_range): # e.g., 10, ie, 10 and only 10.
        
        reg_ex_string = "^(\d)+$" # ie a NUMBER of one or more digits in length, with nothing else in the string (e.g., +,-)

        if (re.search(reg_ex_string,die_range)):
            return True # note logic is reverse of the others
        else:
            return False

# Edit the rows by adding dice ranges to the dictionary and returning the edited row
# note all values are converted from their string form to their integer form for storage and later comparison to die rolls.

    def create_low_range_entries(row):
        die_range = row["DieRange"]
        reg_ex_string = r"\-$" # ie minus sign at end of string
        split_die_string = re.split(reg_ex_string, die_range, 1)
        
        row ["DieLow"] = -1000
        row ["DieHigh"] = int (split_die_string[0])
        return row

    def create_high_range_entries(row):
        die_range = row["DieRange"]
        reg_ex_string = r"\+$" # ie plus at end of string
        split_die_string = re.split(reg_ex_string, die_range, 1)

        row ["DieLow"] = int(split_die_string[0])
        row ["DieHigh"] = +1000
        return row

    def create_mid_range_entries(row):
        die_range = row["DieRange"]
        reg_ex_string = r"\-" # ie minus within string
        split_die_string = re.split(reg_ex_string, die_range, 1)

        row ["DieLow"] = int (split_die_string[0])
        row ["DieHigh"] = int (split_die_string[1])
        return row

    def create_single_digit_entries(row):
        row["DieRange"] = str(row["DieRange"]) 
        die_range = row["DieRange"]
        row ["DieLow"] = int(die_range) # only one number so both take its value
        row ["DieHigh"] = int(die_range)
        return row

### Main die range parsing routine

    for row in d:
        die_range = row["DieRange"]
        if type (die_range) != "str": die_range = str(die_range) # single digits will be read as integers, not strings so we convert.
    
        if die_is_low_range (die_range):
            row = create_low_range_entries(row)
    
        elif die_is_high_range(die_range):
            row = create_high_range_entries(row)

        elif die_is_mid_range(die_range):
            row = create_mid_range_entries(row)
        
        elif die_is_single_digit(die_range):
            row = create_single_digit_entries(row)

        else:
            raise ValueError("The dice entry was not trapped anywhere. SQL table error?")
       
    return d

def table_roll (table,roll):
    to_return={}
    for row in table:
        if roll >= row['DieLow'] and roll <= row['DieHigh']:
            to_return = row
            break
    if not to_return:
        error_text = "Nothing was found on table {} when rolling {} on it.".format(table, roll)
        raise KeyError (error_text)
    return to_return

def main():
     log.setup_logging()
     log.start_logging()
     print ("Begin main.")

    # search factors
     path = "./tests/testSQL.db3"
     table_name = "TestTableReactionRollStandard"

     # path = "./sqlite_db/ACKS_SQL_01.db3"
     table_as_array = (get_table_as_array(path,table_name,query="SELECT * FROM '_replace_'"))
     final_dictionary = (convert_die_range_to_low_and_high(table_as_array))
     print (final_dictionary)
     dice_roll = 12
     print (table_roll(final_dictionary,dice_roll))
     

     print ("End of program")
     log.end_logging()

if __name__ == "__main__":
    main()
