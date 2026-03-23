import argparse
import click

from rich.console import Console
from rich.panel import Panel

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

@click.command()
@click.argument("filename")
def main(filename):
    console = Console()
    content = read_file(filename)
    console.print(Panel(content, border_style="green", title=filename))

if __name__ == "__main__":
    main()
