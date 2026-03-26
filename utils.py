import re

def valid_name(name):
    """
    only allows letters (regex)
    """

    pattern = r"^[a-Za-z]+$"

    if re.match(pattern, name):
        return True
    else:
        return False