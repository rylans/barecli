'''Source application core'''

def echo(input_string):
    """Return input string verbatim

    Examples
    --------

    >>> echo('hello')
    'hello'
    """
    return input_string

def count(input_string):
    """Return number of letters in input string

    Examples
    --------

    >>> count('hello')
    '5'

    >>> count('')
    '0'
    """
    return str(len(input_string))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
