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

def wc(input_string, list_flag=False):
    """Return the number of words in input string

    Examples
    --------

    >>> wc('hello there', False)
    '2'

    >>> wc('hello', False)
    '1'

    >>> wc('', False)
    '0'

    >>> wc('', True)
    []

    >>> wc('uno', True)
    ['uno']

    >>> wc('uno dos', True)
    ['uno', 'dos']
    """
    if list_flag:
        if input_string == '':
            return []
        else:
            return input_string.split(' ')
    if input_string == '':
        return str(0)
    return str(len(input_string.split(' ')))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
