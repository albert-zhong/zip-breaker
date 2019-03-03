import breaker
from string import ascii_lowercase


def main():
    top100 = "darkweb/darkweb2017-top100.txt"
    top1000 = "darkweb/darkweb2017-top1000.txt"
    top10000 = "darkweb/darkweb2017-top10000.txt"

    print(breaker.crack("tests/p.zip", 1, 1, ascii_lowercase))


if __name__ == "__main__":
    main()