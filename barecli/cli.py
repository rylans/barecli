'''Barecli CLI'''

import click

from .core import echo as _echo
from .core import count as _count

@click.group()
def cli():
    '''Entry point of command line application v0.0.5'''
    pass

@cli.command()
@click.argument('string')
def echo(string):
    '''Echo the string verbatim'''
    click.echo(_echo(string))

@cli.command()
@click.argument('string')
def count(string):
    '''Count the number of letters in input string'''
    click.echo(_count(string))
