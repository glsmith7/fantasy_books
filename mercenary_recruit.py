from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header, Footer
import sys
import oop_roll_on_tables_GLS as rpg

class MercTable(DataTable):

    def on_mount(self) -> None:
        
        table = rpg.RPG_table(self.id, query = "SELECT mercenary_type, equipment,class_1 FROM MercenaryTableCities WHERE races_avail LIKE '%man%'")
        self.add_columns(*table.column_names_full)
        self.add_rows(table.table_list_rows[0:])
    
class TableApp(App):
    # CSS_PATH = 'mercenary_recruit.css'
    BINDINGS = [
        ("q,Q", "quit", "Quit Program"),
    ]
    
    def compose(self) -> ComposeResult:
        yield MercTable(id="MercenaryTableCities")
        yield Header()
        yield Footer()

    def quit(self):
        sys.quit(0)

def main():
    
    app = TableApp()

    app.run()
if __name__ == "__main__":
    main()




    