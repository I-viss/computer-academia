def parse_to_integer(data):
    """
    @data: a string or float 
    @return: Integer data type

    This function is a parser, a feature use to parse string data type to integer and return the result
    >>> parse_to_integer('12')
    >>> 12 
    >>> str = '25'
    >>> type(str)
    >>> <class 'str'>
    >>> str = parse_to_integer(str)
    >>> type(str)
    >>> <class 'int'>
    >>> str 
    >>> 25
    """ 
    return int(data)

def parse_to_float(data):
    """
    @data: a string or a float
    @return: Float data type

    This function is a parser, a feature use to parse string data type to a float and return the result
    >>> parse_to_integer('12')
    >>> 12.0
    >>> str = '25'
    >>> type(str)
    >>> <class 'str'>
    >>> str = parse_to_integer(str)
    >>> type(str)
    >>> <class 'float'>
    >>> str
    >>> 25.0
    """ 
    return float(data)

def parse_to_string(number):
    """
    do the same thing we did above 
    """
    return str(number)

