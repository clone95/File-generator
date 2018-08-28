menu = "Insert extension of the file:\n "


def main():
    ext = input(menu)
    nome = ""
    while nome != "end":
        nome = input("FILENAME:\n\n")
        file = open("%s.%s" % (nome, ext), "w+")
        file.close()


main()
