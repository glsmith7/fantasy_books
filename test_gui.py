import PySimpleGUI as sg
import icons as i

radio_unchecked_icon = i.radio_unchecked() 
radio_checked_icon = i.radio_checked()
books_icon = i.books_icon()
excel_icon = i.excel_icon()

# # sg.popup_non_blocking("This is a test. This is a test. This is only a test.",
#     title = None,
#     alpha = 0.5,
#     button_type = 5,
#     button_color = None,
#     background_color = None,
#     text_color = None,
#     auto_close = True,
#     auto_close_duration = 5,
#     non_blocking = True,
#     icon = None,
#     line_width = None,
#     font = None,
#     no_titlebar = True,
#     grab_anywhere = True,
#     keep_on_top = None,
#     location = (None, None),
#     relative_location = (None, None),
#     image = None,
#     modal = False)

# sg.theme("Dark Green 5")

# sg.popup_notify("\tExport to Excel file \n\n" + "greg" + "\n\nis complete.",
#         title = "Excel export done.",
#         # icon = excel_icon,
#         display_duration_in_ms = 3000,
#         fade_in_duration = 500,
#         alpha = 0.9,
#         location = None)
def get_layout():
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
                    disabled=True,
                    ),   
            sg.FileBrowse(
                disabled = True,
            ),   
            sg.Button('Clear History', 
                 key = 'Clear_Master_History',
                 disabled = True,
                 ),
            sg.Text('Worksheet:'), 
            sg.Combo(sorted(sg.user_settings_get_entry('-default_master_worksheets-', [])), 
                    default_value=sg.user_settings_get_entry('-last_default_master_worksheet-', ''),
                    size=(20, 1), 
                    key='-MASTER_WORKSHEET-',
                    disabled = True,
                    ), 
            sg.Button('Clear History',  
                 key = 'Clear_History_Master_Worksheet',
                 disabled = True,
                 )
            ],

            # line 3 ##################################################################
            [sg.Image(radio_checked_icon if sg.user_settings_get_entry('-R1_status-') else radio_unchecked_icon,
                      enable_events=True, 
                      k='-R1-', 
                      metadata=sg.user_settings_get_entry('-R1_status-'),
                      tooltip = ' A book collection of a given value will be generated. '
                      ),
            
            sg.Text('Generate books by value ⟶', 
                    enable_events=True, 
                    k='-T1-',
                    
                    ),
            
            sg.Input(
                    key = "-value_of_books_to_make-",
                    default_text = sg.user_settings_get_entry('-books_value-'),
                    size = (15, 1),
                    enable_events = True,
                    
            ),

            sg.Text('gp total',
                    expand_x=True,
                    ), 

            sg.Text('Allow last book to exceed budget:',
                    ), 

            sg.Button (
                    key='Overshoot', 
                    button_text='Yes' if sg.user_settings_get_entry('-overshoot_toggle-') else 'No', 
                    button_color='white on green' if sg.user_settings_get_entry('-overshoot_toggle-') else 'white on red',
                    size=(4, 1), 
                    tooltip=' If YES, the last book allowed to bring the hoard total to more than requested. If NO, the last book will not be included, and the hoard total value will thus be less than requested amount. ',
                    ),
            ],

        

            # line 4 ###################################################################

            [sg.Image(radio_checked_icon if sg.user_settings_get_entry('-R2_status-') else radio_unchecked_icon,
                      enable_events=True, 
                      k='-R2-', 
                      metadata=sg.user_settings_get_entry('-R2_status-'),
                      tooltip = ' A given number of books will be generated. '),

            sg.Text('Generate books by number ⟶', 
                    enable_events=True, 
                    k='-T2-',
                    tooltip = ' A given number of books will be generated. ',
                    ),
            
            sg.Input(
                    key = "-number_of_books_to_make-",
                    default_text = sg.user_settings_get_entry('-books_number-'),
                    size = (13, 1),
                    enable_events = True,
                    
            ),

            sg.Text('books',
                    expand_x=True,
                    ), 
            ],

            # Final buttons
            [sg.Button('Generate Books', 
                       bind_return_key=True,
                       ),
            sg.Button("Save settings"),  
            sg.Button('Cancel'),
            sg.Button('Reset to defaults'),
            ]
            ]
    
        return layout

window1 = sg.Window(
    'Fantasy Books Generator', 
    layout = get_layout(),
    grab_anywhere = True,
    resizable = False,
    finalize = True
    )

window1.set_cursor("watch")

# turn off tabbing to all elements
for element in window1.key_dict.values():
        element.block_focus()

# retore tabbing
window1['-number_of_books_to_make-'].block_focus(block=False)
window1['-value_of_books_to_make-'].block_focus(block=False)

########## Main Event Loop of GUI

while True:
    window,event, values = sg.read_all_windows()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    else:
          print (event)
