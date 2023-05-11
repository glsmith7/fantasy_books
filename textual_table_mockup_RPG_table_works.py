from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header, Footer
import sys
import oop_roll_on_tables_GLS as rpg
global TITLE, ROWS



class TableApp(App):

    BINDINGS = [
        ("q", "quit", "Quit Program"),
    ]
    
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*TITLE)
        table.add_rows(ROWS[0:])

    def quit(self):
        sys.quit(0)



def main():
    global TITLE, ROWS

    t = rpg.RPG_table("SlaveTroopCost")

    TITLE = t.column_names_full
    ROWS = t.table_list_rows
    app = TableApp()
    app.run()
if __name__ == "__main__":
    main()