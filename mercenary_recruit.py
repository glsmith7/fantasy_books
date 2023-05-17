from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, DataTable, Footer, Header, Label, RadioButton, RadioSet
from textual import errors
import sys
import oop_roll_on_tables_GLS as rpg

# logging boilerplate
import settings_GLS as s
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)

class QuitScreen(ModalScreen):
    """Screen with a dialog to quit."""
   
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()

class RaceSelectScreen(Screen):
    '''Dialogue box to pick race of troops'''
    CSS_PATH = 'radio_set.css'
        
    def compose(self) -> ComposeResult:
        the_default = 'Human' # change to whatever is the current choice once figure out how to do that.
        the_table = rpg.RPG_table('RacesAvailable')
        list_of_race_options = the_table.database_results
        
        with Horizontal():
            with RadioSet(id="race_select"):
                for row in list_of_race_options:
                    if row['Race'] != the_default:
                        yield RadioButton(row['Race'])
                    else:    
                        yield RadioButton(row['Race'], value=True)
        

    def on_mount (self) -> None:
        self.query_one('#race_select').focus('Human')
        pass

class MercTable(DataTable):

    def on_mount(self) -> None:
        
        table = rpg.RPG_table(self.id,query = "SELECT mercenary_type, equipment,class_1 FROM MercenaryTableCities WHERE races_avail LIKE '%man%'")
        self.add_columns(*table.column_names_full)
        self.add_rows(table.table_list_rows[0:])
    
class TableApp(App):

    CSS_PATH = 'mercenary_recruit.css'
    BINDINGS = [
        ('q', 'quit', 'Quit Program'),
        ('r','race_pick', 'Race pick'),
        ('c','city_class_pick', 'Class market pick'),
        ('escape','escape','Escape back')
    ]

    def compose(self) -> ComposeResult:
        yield MercTable(id='MercenaryTableCities')
        yield Header()
        yield Footer()

    def action_quit(self):
        self.push_screen(QuitScreen())

    def action_race_pick(self):
        self.push_screen(RaceSelectScreen())

    def action_escape(self):
        try:
            self.pop_screen()
        except:
            pass # errors with ScreenStackError, but doesn't identify this, so just trapping all error here and passing it. Not great, but ....

def main():
    app = TableApp()
    app.run()
if __name__ == '__main__':
    main()