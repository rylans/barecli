'''Barecli CLI'''

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('string')
def echo(string):
    '''Echo the string verbatim'''
    click.echo(string)
