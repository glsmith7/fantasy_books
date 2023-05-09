import sql_wrapper_GLS as sql
import settings_GLS as s
import sys
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static, Placeholder, DataTable

# logging boilerplate
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class Test(Static):
    

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
       
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)

class MercenaryApp(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit_app","Quit app")
        ]

    def compose(self):
        yield Header()
        yield Test()
        yield Footer()
    
    def on_mount(self):
        pass

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit_app(self):
        sys.exit(0)

if __name__ == "__main__":
    app = MercenaryApp()
    app.run()
