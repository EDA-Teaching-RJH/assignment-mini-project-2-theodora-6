import re

def valid_name(name):
    """
    only allows letters (regex)
    """

    if not isinstance(name, str):
        return False
    
    return bool(re.match(r"^[A-Za-z]+$", name))