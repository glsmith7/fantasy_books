# fantasy_books_gui.py

import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful


layout = [[sg.Text('Default spreadsheet out:'), sg.Combo(sorted(sg.user_settings_get_entry('-default_out_filenames-', [])), default_value=sg.user_settings_get_entry('-last_default_out_filename-', ''), size=(50, 1), key='-EXCEL_OUT_FILENAME-'), sg.FileBrowse(), sg.B('Clear History',  key = 'Clear_History_Default_Out')],
          [sg.Text('Default master list:'), sg.Combo(sorted(sg.user_settings_get_entry('-default_master_filenames-', [])), default_value=sg.user_settings_get_entry('-last_default_master_filename-', ''), size=(50, 1), key='-MASTER_FILENAME-'), sg.FileBrowse(), sg.B('Clear History', key = 'Clear_Master_History')],
          [sg.Text('Total unique titles in master:'),sg.Input( size = (10,1), key = ('-TOTAL_UNIQUE_MASTER-'))],
          [sg.Button('Ok', bind_return_key=True),  sg.Button('Cancel')]]

window = sg.Window('Filename Chooser With History', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Ok':
        # If OK, then need to add the filename to the list of files and also set as the last used filename
        sg.user_settings_set_entry('-default_out_filenames-', list(set(sg.user_settings_get_entry('-default_out_filenames-', []) + [values['-EXCEL_OUT_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_out_filename-', values['-EXCEL_OUT_FILENAME-'])

        sg.user_settings_set_entry('-default_master_filenames-', list(set(sg.user_settings_get_entry('-default_master_filenames-', []) + [values['-MASTER_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_master_filename-', values['-MASTER_FILENAME-'])

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