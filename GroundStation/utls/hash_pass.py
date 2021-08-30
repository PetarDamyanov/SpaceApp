import hashlib


def hash_password(password, salt):
    return hashlib.sha512((password + salt).encode()).hexdigest()