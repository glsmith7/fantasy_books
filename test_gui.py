# def time_label(local_time):
#         the_label = (
#                 str(lt.tm_year) + 
#                 str(lt.tm_mon) + 
#                 str(lt.tm_mday) + 
#                 str(lt.tm_hour) + 
#                 str(lt.tm_min) + 
#                 str(lt.tm_sec))

# pass
        
# lt = time.localtime()

# the_label = time_label(lt)
# file_source = 'blank_excel_files_templates\master_fantasy_book_list_BLANK.xlsx'
# file_destination = 'excel_backups\master_fantasy_book_list_backup_XXLABELXX.xlsx'

# file_destination = file_destination.replace('XXLABELXX',the_label)
# print (file_destination)

from datetime import datetime

now = datetime.now().strftime("%Y%m%d_%H%M_%S") # current date and time
print ("Now:" + str (now))

# year = now.strftime("%Y%m%d_%H%M_%S")
# print(year)