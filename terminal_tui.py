import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel


class TerminalTUI:
    def __init__(self):
        self.Console = Console()

    def display_header(self):
        ascii_header = pyfiglet.figlet_format(
            "TPOCH", font="slant"
        )
        header_text = Text(
            ascii_header, style="#00ff41", justify="center", no_wrap=True
        )
        header_panel = Panel(
            header_text, style="#d474ff", border_style="#d474ff")
        self.Console.print(header_panel
                           )
