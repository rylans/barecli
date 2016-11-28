'''Barecli CLI'''

import click

from .core import echo as _echo
from .core import count as _count
from .core import wc as _wc

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

@cli.command()
@click.argument('string')
def wc(string):
    '''Count number of words in input string'''
    click.echo(_wc(string))
