# fantasy_books_gui.py

import PySimpleGUI as sg

sg.theme('Dark Blue 3') 

def master_books_settings_window():

    layout = [

                # default spreadsheets x 2
            # line 1 ##################################################################
            [
             sg.Text('Default spreadsheet out:'),  
             sg.Combo(sorted(sg.user_settings_get_entry('-default_out_filenames-', [])), 
                      default_value=sg.user_settings_get_entry('-last_default_out_filename-', ''), 
                      size=(50, 1), 
                      key='-EXCEL_OUT_FILENAME-',
                      ),   
            
            sg.FileBrowse(),   
            sg.Button('Clear History',  
                 key = 'Clear_History_Default_Out',
                     ), 
            sg.Text('Worksheet:'), 
            sg.Combo(sorted(sg.user_settings_get_entry('-default_out_worksheets-', [])), 
                default_value=sg.user_settings_get_entry('-last_default_out_worksheet-', ''), 
                size=(20, 1), 
                key='-EXCEL_OUT_WORKSHEET-',
                ), 

            sg.Button('Clear History',  
                 key = 'Clear_History_Default_Out_Worksheet')
            ],
            
            # line 2 ##################################################################
            [
             sg.Text('Default master list:'),  
             sg.Combo(sorted(sg.user_settings_get_entry('-default_master_filenames-', [])), 
                    default_value=sg.user_settings_get_entry('-last_default_master_filename-', ''), 
                    size=(50, 1), 
                    key='-MASTER_FILENAME-',
                    ),   
            sg.FileBrowse(),   
            sg.Button('Clear History', 
                 key = 'Clear_Master_History',
                 ),
            sg.Text('Worksheet:'), 
            sg.Combo(sorted(sg.user_settings_get_entry('-default_master_worksheets-', [])), 
                    default_value=sg.user_settings_get_entry('-last_default_master_worksheet-', ''),
                    size=(20, 1), 
                    key='-MASTER_WORKSHEET-',
                    ), 
            sg.Button('Clear History',  
                 key = 'Clear_History_Master_Worksheet',
                 )
            ],

            # line 3 ##################################################################
            [sg.Text('Allow last book to exceed budget:'), 
                sg.Button (
                    key='Overshoot', 
                    button_text='Yes' if sg.user_settings_get_entry('-overshoot_status-') == 'Yes' else 'No', 
                    button_color='white on green' if sg.user_settings_get_entry('-overshoot_status-') == 'Yes' else 'white on red', 
                    size=(4, 1), 
                    tooltip=' If a certain value of book hoard is requested: if YES, the last book allowed to bring the hoard total to more than requested. If NO, the last book will not be included, and the hoard total value will thus be less than requested amount. ',
                    ),
            ],

            # Final buttons
            [sg.Button('Ok', 
                       bind_return_key=True,
                       ),  
            sg.Button('Cancel')
            ]
            ]
    
    return layout

window = sg.Window('Fantasy Books Generator', master_books_settings_window())

### Set window based on saved statuses

if sg.user_settings_get_entry('-overshoot_status-') == 'Yes':
     overshoot_toggle = True 
else:
     overshoot_toggle = False

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Ok':
        # Save combo boxes and contents
        sg.user_settings_set_entry('-default_out_filenames-', list(set(sg.user_settings_get_entry('-default_out_filenames-', []) + [values['-EXCEL_OUT_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_out_filename-', values['-EXCEL_OUT_FILENAME-'])
        sg.user_settings_set_entry('-default_out_worksheets-', list(set(sg.user_settings_get_entry('-default_out_worksheets-', []) + [values['-EXCEL_OUT_WORKSHEET-'], ])))
        sg.user_settings_set_entry('-last_default_out_worksheet-', values['-EXCEL_OUT_WORKSHEET-'])

        ####

        sg.user_settings_set_entry('-default_master_filenames-', list(set(sg.user_settings_get_entry('-default_master_filenames-', []) + [values['-MASTER_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_master_filename-', values['-MASTER_FILENAME-'])
        sg.user_settings_set_entry('-default_master_worksheets-', list(set(sg.user_settings_get_entry('-default_master_worksheets-', []) + [values['-MASTER_WORKSHEET-'], ])))
        sg.user_settings_set_entry('-last_default_master_worksheet-', values['-MASTER_WORKSHEET-'])

        sg.user_settings_set_entry('-overshoot_toggle_status', values['-MASTER_WORKSHEET-'])
        sg.user_settings_set_entry('-overshoot_status-', window['Overshoot'].get_text())
        break
    
    elif event == 'Overshoot':                # if the normal button that changes color and text
            overshoot_toggle = not overshoot_toggle
            window['Overshoot'].update(
                 text='Yes' if overshoot_toggle else 'No', 
                 button_color='white on green' if overshoot_toggle else 'white on red'
                 )

    elif event == 'Clear_History_Default_Out':
        sg.user_settings_set_entry('-default_out_filenames-', [])
        sg.user_settings_set_entry('-last_default_out_filename-', '')
        window['-EXCEL_OUT_FILENAME-'].update(values=[], value='')

    elif event == 'Clear_Master_History':
        sg.user_settings_set_entry('-default_master_filenames-', [])
        sg.user_settings_set_entry('-last_default_master_filename-', '')
        window['-MASTER_FILENAME-'].update(values=[], value='')

    elif event == 'Clear_History_Default_Out_Worksheet':
        sg.user_settings_set_entry('-default_out_worksheets-', [])
        sg.user_settings_set_entry('-last_default_out_worksheet-', '')
        window['-EXCEL_OUT_WORKSHEET-'].update(values=[], value='')

    elif event == 'Clear_History_Master_Worksheet':
        sg.user_settings_set_entry('-default_master_worksheets-', [])
        sg.user_settings_set_entry('-last_default_master_worksheet-', '')
        window['-MASTER_WORKSHEET-'].update(values=[], value='')

window.close()