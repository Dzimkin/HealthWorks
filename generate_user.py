import random


def generate_name():
    name = ''
    for x in range(5):
        name += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return name


def generate_source():
    source = ''
    for x in range(5):
        source += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return source


def generate_date():
    date = '0'
    for x in range(1):
        date += random.choice(list('123456789'))
        date += "/0"
    for x in range(1):
        date += random.choice(list('123456789'))
        date += "/2022"
    return date


def generate_program():
    program = ''
    for x in range(5):
        program += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return program


def generate_number():
    number = '(123) 456-'
    for x in range(4):
        number += random.choice(list('1234567890'))
    return number
