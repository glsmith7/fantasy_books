from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Button, DataTable, Footer, Header, Label, RadioButton, RadioSet
import sys
import oop_roll_on_tables_GLS as rpg

class QuitScreen(Screen):
    """Screen with a dialog to quit."""
    CSS_PATH = 'quit_screen.css'
    
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
    BINDINGS = [
        ("r",'race_pick', 'Race pick'),
    ]
    def compose(self) -> ComposeResult:
        with Horizontal():
            with RadioSet(id="race_select"):
                yield RadioButton("Human", value = True)
                yield RadioButton("Dwarf")
                yield RadioButton("Elf")
                yield RadioButton("Gnoll")
                yield RadioButton("Orc")
                yield RadioButton("Goblin")
                yield RadioButton("Kobold")
                yield RadioButton("Quit")

    def on_mount (self) -> None:
        self.query_one('#race_select')
    
    def action_race_pick(self) -> None:
        self.app.pop_screen()

class MercTable(DataTable):

    def on_mount(self) -> None:
        
        table = rpg.RPG_table(self.id, query = "SELECT mercenary_type, equipment,class_1 FROM MercenaryTableCities WHERE races_avail LIKE '%man%'")
        self.add_columns(*table.column_names_full)
        self.add_rows(table.table_list_rows[0:])
    
class TableApp(App):
    CSS_PATH = 'mercenary_recruit.css'
    BINDINGS = [
        ("q,Q", "quit", "Quit Program"),
        ("r",'race_pick', 'Race pick'),
        ("c",'city_class_pick', 'Class market pick'),
    ]

    def compose(self) -> ComposeResult:
        yield MercTable(id="MercenaryTableCities")
        yield Header()
        yield Footer()

    def action_quit(self):
        self.push_screen(QuitScreen())

    def action_race_pick(self):
        self.push_screen(RaceSelectScreen())

    

def main():
    app = TableApp()
    app.run()
if __name__ == "__main__":
    main()