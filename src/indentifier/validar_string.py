import re
def verificar_string(string):
    if not re.match(r'^[A-Za-z]', string) or len(string) == 0:
        return False

    if re.search(r'[^a-zA-Z0-9]', string) is not None:
        return False

    if not (1 <= len(string) < 7):
        return False

    return True
