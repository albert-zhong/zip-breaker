import breaker


def main():
    top100 = "darkweb2017-top100.txt"
    top1000 = "darkweb2017-top1000.txt"
    top10000 = "darkweb2017-top10000.txt"

    print(breaker.dict_crack("password.zip", top100))


if __name__ == "__main__":
    main()