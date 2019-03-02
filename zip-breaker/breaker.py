from zipfile import ZipFile
import csv


def get_firefox(path):
    pass_set = set()
    with open(path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            pass_set.add(row[2])
    return pass_set


def get_dictionary():
    dictionary = dict()
    return dictionary


def crack(path):
    with ZipFile(path) as zf:
        zf.extractall(pwd=bytes("pass", "utf-8"))