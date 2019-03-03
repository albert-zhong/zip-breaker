from zipfile import ZipFile
import string
import csv


def crack(path, length):
    with ZipFile(path) as zf:

        chars = string.digits + string.ascii_letters  # Creates string of a-z, A-Z, 0-9
        special_chars = "!\"#$%&'()*+,-./:;?@[\]^_`{|}~"

        i = 0
        while i <= length:


        for char in letters_and_numbers:
            try:
                zf.extractall(pwd=bytes(char, "utf-8"))
                return char
            except RuntimeError:
                pass
        print("could not crack password")


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