import string


def maiusculas(a_string):
    uppers = ""
    for c in a_string:
        if c in string.ascii_uppercase:
            uppers = uppers + c
    return uppers
