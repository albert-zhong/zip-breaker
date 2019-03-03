from zipfile import ZipFile

with ZipFile("p.zip") as zf:
    password = "D"
    try:
        zf.extractall(pwd=bytes(password, "utf-8"))
    except RuntimeError:
        print("wrong: " + password)
