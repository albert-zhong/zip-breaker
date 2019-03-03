from zipfile import ZipFile
import string
import csv


def crack(path, length):
    with ZipFile(path) as zf:
        chars = string.digits + string.ascii_letters  # Creates string of a-z, A-Z, 0-9
        special_chars = "!\"#$%&'()*+,-./:;?@[\]^_`{|}~"

        passwords = set()  # Creates original password set with all chars
        for char in chars:
            passwords.add(char)
        print(passwords)

        for x in range(1, length):
            for password in passwords:
                try:
                    zf.extractall(pwd=bytes(password, "utf-8"))
                    return password
                except RuntimeError:
                    pass
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