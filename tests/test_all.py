'''Generic test module'''

from barecli.core import echo
from barecli.core import count

def test_echo_word():
    '''Verify that word is echo'd verbatim'''
    assert echo('Hello') == 'Hello'

def test_echo_empty():
    '''Test that empty string is echo'd properly'''
    assert echo('') == ''

def test_count_word():
    '''Verify that word of four letters can be counted'''
    assert count('What') == '4'

def test_count_empty():
    '''Verify that the empty string is counted correctly'''
    assert count('') == '0'
