import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""

    """
     v------ This.... -----------v
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()
     v------ ...is the same as this -----------v

    # requests.get(.API_URL).__enter__().json()
    """

    data = wikipedia.random_page()
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
