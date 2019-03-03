from zipfile import BadZipFile
from zipfile import ZipFile
import string
import csv


def crack(path, lower_length, upper_length, special_chars=None):

    # Checking for exceptions
    if lower_length < 1 or upper_length < 1:
        raise Exception("Lower and upper length must be greater than 0")
    if lower_length > upper_length:
        raise Exception("Lower length must be equal or less than upper length")

    if special_chars is not None:
        chars = special_chars
    else:
        chars = string.digits + string.ascii_letters  # Creates string of a-z, A-Z, 0-9
        special_chars = "!\"#$%&'()*+,-./:;?@[\]^_`{|}~"

    passwords = set()  # Creates original password set with all chars, length = 1
    for char in chars:
        passwords.add(char)

    for i in range(1, lower_length):  # Creates new layers for lower_length bound
        passwords = new_layer(passwords, chars)

    for x in range(lower_length-1, upper_length):
        for password in passwords:
            try:
                with ZipFile(path) as zf:
                    zf.extractall(pwd=bytes(password, "utf-8"))
                    return password
            except RuntimeError:
                pass
            except BadZipFile:
                print("manually check: " + password)
                # For some reason there's a 1/256 chance of this error
                # https://stackoverflow.com/questions/54968252/python-throws-zipfile-badzipfile-bad-crc-32-only-when-i-pass-d-as-password
        passwords = new_layer(passwords, chars)
    print("could not crack password")


def new_layer(current_set, chars):
    new_set = set()
    for item in current_set:
        for char in chars:
            new_set.add(item + char)
    return new_set


def dict_crack(path, dict_path):  # Reads dictionary from a text file
    file = open(dict_path, "r")
    dictionary = file.read().splitlines()

    with ZipFile(path) as zf:
        for password in dictionary:
            try:
                zf.extractall(pwd=bytes(password, "utf-8"))
                return password
            except RuntimeError:
                pass
        print("could not crack password")


def get_firefox(path):  # returns a list of passwords from a Firefox exported passwords in CSV format
    pass_set = set()
    with open(path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            pass_set.add(row[2])
    return pass_set


def firefox_crack(path, firefox_path):  # Reads dictionary from Firefox CSV exported passwords
    dictionary = get_firefox(firefox_path)

    with ZipFile(path) as zf:
        for password in dictionary:
            try:
                zf.extractall(pwd=bytes(password, "utf-8"))
                return password
            except RuntimeError:
                pass
        print("could not crack password")