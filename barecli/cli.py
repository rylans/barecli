'''Barecli CLI'''

import click
import logging
logging.basicConfig(level=logging.DEBUG)

from .core import echo as _echo
from .core import count as _count
from .core import wc as _wc

@click.group()
@click.option('-d', '--debug', is_flag=True, default=False, help='Debug flag')
@click.pass_context
def cli(ctx, debug):
    '''Entry point of command line application v0.0.5'''
    ctx.obj = {}
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.argument('string')
@click.pass_context
def echo(ctx, string):
    '''Echo the string verbatim'''
    show(_echo(string), ctx)

@cli.command()
@click.argument('string')
@click.pass_context
def count(ctx, string):
    '''Count the number of letters in input string'''
    show(_count(string), ctx)

@cli.command()
@click.argument('string')
@click.option('-l', '--list', is_flag=True, default=False, help='List one word per line')
@click.pass_context
def wc(ctx, string, list):
    '''Count number of words in input string'''
    show(_wc(string, list), ctx)

def show(value, ctx):
    '''Echo the items to the console and log if debugging enabled'''
    debug = ctx.obj.get('DEBUG')
    if type(value) == type(list()):
        if len(value) == 0:
            _show('[]', debug)
        else:
            _show_list(value, debug)
    else:
        _show(value, debug)

def _show(item, debug):
    '''Show a single item (and log if debug is enabled)'''
    if debug:
        logger = logging.getLogger(__name__)
        logger.debug(item)
    click.echo(item)

def _show_list(items, debug):
    '''Show a list of items (and log if debugging is enabled)'''
    if debug:
        logger = logging.getLogger(__name__)
        logger.debug(items)
    for n, item in enumerate(items):
        indent = '  '
        if n >= 9:
            indent = ' '
        click.echo('%s%s. %s' % (indent, str(n+1), item))
