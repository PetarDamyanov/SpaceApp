from random import randint
from django.db.models.query import QuerySet
from user_satellite.models import User

chars = [
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '$', '_', '*', '.'
]


def create_salt():
    s = ''
    for letter in range(0, 4):
        s += str(chars[randint(0, len(chars) - 1)])
    if s not in User.objects.filter(salt=s):
        return s
    else:
        create_salt()