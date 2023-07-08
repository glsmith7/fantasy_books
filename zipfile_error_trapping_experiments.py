import openpyxl
import pandas as pd
from zipfile import Zipfile

try_to_save = True
while try_to_save:
    filename = 'master_fantasy_book_list.xlsx'
    worksheet = 'Master List'
    try:
        excel_file_pandas = pd.read_excel(filename, sheet_name=worksheet, header=0, index_col=None, usecols=None, dtype=None, engine="openpyxl", decimal='.')

    except PermissionError:
            
        print ("Permission error")

    except FileNotFoundError:
       print ("File not found")
            
    except Zipfile.badzipfile:
        print ("ZipFile")        
    else:
        try_to_save = False # succeeded!     
        print ("DOne")