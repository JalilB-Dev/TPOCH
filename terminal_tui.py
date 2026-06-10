import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
from datetime import datetime
from zoneinfo import ZoneInfo


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
            header_text, style="#d474ff", border_style="#d474ff", title="//Terminal World Clock", subtitle="//The Only Clock You Need"
        )
        self.Console.print(header_panel)

    def display_time(self, sorted_cities):
        layout = Layout()
        layout.split_row(
            Layout(name="L1"), Layout(name="L2"), Layout(
                name="R2"), Layout(name="R1")
        )
        layout["L1"].split_column(
            Layout(name="L1A"), Layout(name="L1B"), Layout(name="L1C"))
        layout["L2"].split_column(
            Layout(name="L2A"), Layout(name="L2B"), Layout(name="L2C"))
        layout["R1"].split_column(
            Layout(name="R1A"), Layout(name="R1B"), Layout(name="R1C"))
        layout["R2"].split_column(
            Layout(name="R2A"), Layout(name="R2B"), Layout(name="R2C"))

        for section, city in zip(layout["L1"].children + layout["L2"].children +
                                 layout["R1"].children +
                                 layout["R2"].children, sorted_cities
                                 ):

            time_text = Text(justify="center", style="#00ff41"
                             )
            current_time = datetime.now(ZoneInfo(city["timezone"])
                                        )
            line = f"{city['name']}: {current_time.strftime('%A, %B %d %I:%M %p %Z')}\n"
            time_text.append(line)
            time_panel = Panel(
                time_text, border_style="#d474ff")
            layout[section.name].update(time_panel)
        self.Console.print(layout)
