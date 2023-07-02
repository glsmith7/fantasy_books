# fantasy_books_gui.py

import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

def master_books_settings_window():

    layout = [

                # default spreadsheets x 2
            [sg.Text('Default spreadsheet out:'),  sg.Combo(sorted(sg.user_settings_get_entry('-default_out_filenames-', [])), default_value=sg.user_settings_get_entry('-last_default_out_filename-', ''), size=(50, 1), key='-EXCEL_OUT_FILENAME-'),   sg.FileBrowse(),   sg.B('Clear History',  key = 'Clear_History_Default_Out')],
            
            [ sg.Text('Default master list:'),  sg.Combo(sorted(sg.user_settings_get_entry('-default_master_filenames-', [])), default_value=sg.user_settings_get_entry('-last_default_master_filename-', ''), size=(50, 1), key='-MASTER_FILENAME-'),   sg.FileBrowse(),   sg.B('Clear History', key = 'Clear_Master_History')],


                # 4 boxes
            [sg.Text('Total unique titles in master:'),sg.Input(size = (10,1), key = ('-TOTAL_UNIQUE_IN_MASTER-'), default_text = sg.user_settings_get_entry('-total_unqiue_in_master-'))],
            
            [sg.Text('Total value unique titles in master:'),sg.Input( size = (10,1), key = ('-TOTAL_VALUE_ALL_UNIQUE_TITLES_MASTER-'),default_text = sg.user_settings_get_entry('-total_value_all_unique_titles_master-'))],
            
            [sg.Text('Total books in master:'),sg.Input( size = (10,1), key = ('-TOTAL_BOOKS_IN_MASTER-'),default_text = sg.user_settings_get_entry('-total_books_in_master-'))],

            [sg.Text('Total books avail to place still in master:'),sg.Input( size = (10,1), key = ('-TOTAL_BOOKS_IN_MASTER_FOR_PLACEMENT-'),default_text = sg.user_settings_get_entry('-total_books_in_master_avail_for_placement-'))],

                # Final buttons
            [sg.Button('Ok', bind_return_key=True),  sg.Button('Cancel')]]
    
    return layout

window = sg.Window('Filename Chooser With History', master_books_settings_window())

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Ok':
        # Save combo boxes and contents
        sg.user_settings_set_entry('-default_out_filenames-', list(set(sg.user_settings_get_entry('-default_out_filenames-', []) + [values['-EXCEL_OUT_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_out_filename-', values['-EXCEL_OUT_FILENAME-'])

        sg.user_settings_set_entry('-default_master_filenames-', list(set(sg.user_settings_get_entry('-default_master_filenames-', []) + [values['-MASTER_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_master_filename-', values['-MASTER_FILENAME-'])

        # Save 4 data boxes
        sg.user_settings_set_entry('-total_unqiue_in_master-', values['-TOTAL_UNIQUE_IN_MASTER-'])
        sg.user_settings_set_entry('-total_value_all_unique_titles_master-', values['-TOTAL_VALUE_ALL_UNIQUE_TITLES_MASTER-'])
        sg.user_settings_set_entry('-total_books_in_master-', values['-TOTAL_BOOKS_IN_MASTER-'])
        sg.user_settings_set_entry('-total_books_in_master_avail_for_placement-', values['-TOTAL_BOOKS_IN_MASTER_FOR_PLACEMENT-'])

        break

    elif event == 'Clear_History_Default_Out':
        sg.user_settings_set_entry('-default_out_filenames-', [])
        sg.user_settings_set_entry('-last_default_out_filename-', '')
        window['-EXCEL_OUT_FILENAME-'].update(values=[], value='')

    elif event == 'Clear_Master_History':
        sg.user_settings_set_entry('-default_master_filenames-', [])
        sg.user_settings_set_entry('-last_default_master_filename-', '')
        window['-MASTER_FILENAME-'].update(values=[], value='')

window.close()