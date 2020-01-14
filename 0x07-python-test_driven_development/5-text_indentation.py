#!/usr/bin/python3
"""
5-text_indentation: module to indent a text
"""


def text_indentation(text):
    """
    text_indentation: function that prints a text with 2 new lines after each
                      of these characters: ., ? and :
    @text: text to indent
    Errors: if text not a string raise
    return: no one
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    if len(text) == 0:
        raise TypeError("text must be a string")
    sw = 0
    text = text.rstrip()
    text = text.lstrip()
    for j, i in enumerate(text):
        if i == '.' or i == '?' or i == ':':
            print(i, end="")
            print("\n")
            sw = 1
        elif sw == 1:
            if len(text) > j:
                if text[j] == ' ':
                    continue
                else:
                    print(i, end="")
                    sw = 0
        else:
            print(i, end="")
