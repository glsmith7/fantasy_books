# fantasy_books_gui.py

import PySimpleGUI as sg

#########Graphics###############

# Base64 Encoded Radio Button Image of unchecked radio button
radio_unchecked = b'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAEwElEQVR4nI1W3W9URRT/nZm7ZXdpbajdWpCAjcFEqw88+CACrgaBmFBIwI3fPPpPaJYND/wjYsxFYgwP+BV2kY9gNCIJIhEIBZSWLl3aprvde2fOOT7c3W27fNSTTO7cMzO/35wz55wZYAVRVVMuaxCGoV2qD8PQlsvlQFXNShhPAqduYEr0lrrmhmFoVbVbvWzdQxKGoS0UCgwAFy6PvySx27cQRVvY80YGZyHaIKJbPUHqvCF8k3/tlb+61z2RJAzVFgrE5QuX1q9K9x6Oouj9TCazKmUBawiAglkQO0bsPOqNejOw9qsoan62Z8eWfx9FRMsJkgnnfrv6FgXBUWOD4UzAWJsb8L3ZNFlrCQSwZ8TO6excXe/eux/UY0EcuQkXRx/t3fX6qW6iDomqGiKS87///QaM/Q7K6efXD7rBgf5AVcl7hgBQEYgqVAQEgqroZLXmb9yeTLGgKRztHtu5/XQbr0NSVDU4dAhvj703LGouBpaGXhwZ5v6nem0cO2gCB002AxGBiICZwSwIrEVtZpav3LhjneN76YxsvnDq1D0AKJVKYgBg9NgxKpVKIkpH0ulVQyPrBvxTfb02ih2ICESAdp2darJHIkIUx+jrXW03rB30PT09zzTm5UipVJLR0VECAGqb9csfV16oN3H56f60Hd20gZzzRJR4UzvAusySxBoBi8A5DyLolWvjOv1gjldnUqN7duavFYtFYyoVGACIvd2fzWZSw4P9IqKkLfBugu4GKFSSr4hSbqBfMplMaiFyBwAgn88bU60eUwCI43hbYIBsJk2e+bHAiQVL/xWiSTB4ZmQzabKG4B1vBYBqtapBoVBgVaUfz13aaI3CEBGzgAjouEuXg3bARSG6pImADJEhwLN/TlWJiDhoecOqSHYpUIJPHYclY4CqdBElZ6Otfse9otlKBRaAb5OwqjbaYSnatqKzpEXQAleFsIAlCWERBbfyR4TBwlDVRj4PBgAThqElIgVhPPaicew02R0vi6ClESWcALEkkbV0bhQ7dZ4VpONEpGEYWpPL5QgArLVnYsc0N99QAuC5nWy8JPEYvtW4PS6LfVXFfL2hznkyxv4MALlcjkwlnxcACCj4ul6fjyeqNeOZ1Xu/COoXwX0XkbDAs8B7BjPrVLVm6vVGDOXjAFCpVMSUiCQMQ/vmlpevE+nRyJOZul9jYwix84sEfrG1d94h9A5EQHW6xrEXYwhffFLYe/3dMLSlUkmS2lUsGgB4Nf/OEIleJEPDI88Ocl/vauu8b5UQdA69nS/t2mWIMDM3x+P/TFp2flKM3Tz+569T7dr1UBU+8dPZbWRS30M4s25ojVvT3xcIlNpRpCpd+cI6XZvxd6emUyrUEPW7DhbGzi6twp37mVpu27Nj65lmo7lbgDsT9+dSV2/cotqDWR/HMYt4ERHx7CWKIq7NzPrrN2/TVG0uBcVt56PdBwtjZ1sRKx3sruLaubiOnzy51tq+wy6KP0j19GSsAQwtlnrPjNgxmgvNBWvNl41m8/NPP94/seLN2E0EACd+qGxyse5runi7Zz+iLL2imLcGN1PWnhYNvv3wwM5r3ev+lzzqtdLSB926lV4rK0qxWDTlcvmx7652ZD5J/gNoDCDS80MCGwAAAABJRU5ErkJggg=='

# Base64 Encoded Radio Button Image of checked radio button
radio_checked = b'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'

########################################################################################

sg.theme('Dark Blue 3') 

def check_radio(key): 
    radio_keys = ('-R1-', '-R2-')
    
    for k in radio_keys:
        window[k].update(radio_unchecked)
        window[k].metadata = False
    window[key].update(radio_checked)
    window[key].metadata = True

def radio_is_checked(key):
        return window[key].metadata

def fantasy_books_main_gui():
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
                    expand_x=True,
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
            [sg.Image(radio_checked,
                      enable_events=True, 
                      k='-R1-', 
                      metadata=True,
                      tooltip = ' A book collection of a given value will be generated. '
                      ),
            
            sg.Text('Generate books by value ⟶', 
                    enable_events=True, 
                    k='-T1-',
                    
                    ),
            
            sg.Input(
                    key = "-value_of_books_to_make-",
                    default_text = 0,
                    size = (15, 1),
                    
            ),

            sg.Text('gp total',
                    expand_x=True,
                    ), 

            sg.Text('Allow last book to exceed budget:',
                    ), 

            sg.Button (
                    key='Overshoot', 
                    button_text='Yes' if sg.user_settings_get_entry('-overshoot_status-') == 'Yes' else 'No', 
                    button_color='white on green' if sg.user_settings_get_entry('-overshoot_status-') == 'Yes' else 'white on red', 
                    size=(4, 1), 
                    tooltip=' If YES, the last book allowed to bring the hoard total to more than requested. If NO, the last book will not be included, and the hoard total value will thus be less than requested amount. ',
                    ),
            ],

        

            # line 4 ###################################################################

            [sg.Image(radio_unchecked,
                      enable_events=True, 
                      k='-R2-', 
                      metadata=True,
                      tooltip = ' A given number of books will be generated. '),

            sg.Text('Generate books by number ⟶', 
                    enable_events=True, 
                    k='-T2-',
                    tooltip = ' A given number of books will be generated. ',
                    ),
            
            sg.Input(
                    key = "-number_of_books_to_make-",
                    default_text = 0,
                    size = (13, 1),
                    
            ),

            sg.Text('books',
                    expand_x=True,
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


window = sg.Window('Fantasy Books Generator', fantasy_books_main_gui())

### Set window based on saved statuses

if sg.user_settings_get_entry('-overshoot_status-') == 'Yes':
     overshoot_toggle = True 
else:
     overshoot_toggle = False

radio_keys = ('-R1-', '-R2-')
########## Main Event Loop of GUI

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
        sg.user_settings_set_entry('-default_master_filenames-', list(set(sg.user_settings_get_entry('-default_master_filenames-', []) + [values['-MASTER_FILENAME-'], ])))
        sg.user_settings_set_entry('-last_default_master_filename-', values['-MASTER_FILENAME-'])
        sg.user_settings_set_entry('-default_master_worksheets-', list(set(sg.user_settings_get_entry('-default_master_worksheets-', []) + [values['-MASTER_WORKSHEET-'], ])))
        sg.user_settings_set_entry('-last_default_master_worksheet-', values['-MASTER_WORKSHEET-'])

        sg.user_settings_set_entry('-overshoot_toggle_status', values['-MASTER_WORKSHEET-'])
        sg.user_settings_set_entry('-overshoot_status-', window['Overshoot'].get_text())
        print (values)

        break
    
    elif event in radio_keys:
            check_radio(event)
    
    elif event.startswith('-T'):        # If text element clicked, change it into a radio button key
        check_radio(event.replace('T', 'R'))

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