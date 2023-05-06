import sql_wrapper_GLS as sql
import settings_GLS as s
import sys
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static, Placeholder, DataTable

class Test(Static):


    def compose(self):
        
     yield DataTable (zebra_stripes=True)
        
    def on_mount(self) -> None:

        ROWS = [
        ("lane", "swimmer", "country", "time"),
        (4, "Joseph Schooling", "Singapore", 50.39, "the quick brown fox jumped over the lazy ", 0,0,2,3,1,1,1),
        (2, "Michael Phelps", "United States", 51.14),
        (5, "Chad le Clos", "South Africa", 51.14),
        (6, "László Cseh", "Hungary", 51.14),
        (3, "Li Zhuhao", "China", 51.26),
        (8, "Mehdy Metella", "France", 51.58),
        (7, "Tom Shields", "United States", 51.73),
        (1, "Aleksandr Sadovnikov", "Russia", 51.84),
        (10, "Darren Burns", "Scotland", 51.84),
        ]
        
        self.col_names = sql.get_column_names(table_name="MercenaryTableRealms")
        
        table = self.query_one(DataTable)
        table.add_columns(*self.col_names)
        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(str(cell)) for cell in row
            ]
            table.add_row(*styled_row)

class DomainsArmies (App):
    CSS_PATH = "mercenary_recruit.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q","quit_app","Quit")
        ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        # a = Test(table_name="Table 1")
        # b = Test(table_name="Table 2")

        a=Test()
        b=Test()
        yield a
        yield b

        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit_app(self) -> None:
        ''' Exit the app'''
        sys.exit(0)

def main():
    pass

if __name__ == "__main__":
    main()
    app = DomainsArmies()
    app.run()
