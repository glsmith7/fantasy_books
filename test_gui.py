import PySimpleGUI as sg

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

sg.theme("Dark Green 5")
sg.popup_notify("\tExport to Excel file \n\n" + "greg" + "\n\nis complete.",
        title = "Excel export done.",
        # icon = excel_icon,
        display_duration_in_ms = 3000,
        fade_in_duration = 500,
        alpha = 0.9,
        location = None)

g = input ("Hit enter to end.")