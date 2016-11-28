'''Generic test module'''

from barecli.core import echo
from barecli.core import count
from barecli.core import wc

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

def test_wc_zero():
    '''Verify that wc can return zero'''
    assert wc('') == '0'

def test_wc_one():
    '''Verify that wc can return one'''
    assert wc('example.') == '1'

def test_wc_two():
    '''Verifty that wc can return two'''
    assert wc('hey there!') == '2'
