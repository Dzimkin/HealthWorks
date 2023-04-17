import random


def generate_name():
    name = ''
    for x in range(5):
        name += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ1234567890'))
    return name


def generate_source():
    source = ''
    for x in range(5):
        source += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ1234567890'))
    return source
