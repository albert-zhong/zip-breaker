import breaker
from string import ascii_lowercase


def main():
    top100 = "darkweb2017-top100.txt"
    top1000 = "darkweb2017-top1000.txt"
    top10000 = "darkweb2017-top10000.txt"

    print(breaker.crack("p.zip", 1, 1, ascii_lowercase))


if __name__ == "__main__":
    main()