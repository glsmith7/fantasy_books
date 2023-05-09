
import sql_wrapper_GLS as sql
import settings_GLS as s
import sys
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static, Placeholder, DataTable


table_data = sql.query_database(table_name="MercenaryTableRealms")

for row in table_data:
    print (row)
    

