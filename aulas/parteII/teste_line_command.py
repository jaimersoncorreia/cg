import sys
def main():
    lista = sys.argv
    lista.__delitem__(0)
    print()
    if lista:
        for l in lista:
            print(l)
    else:
        print("Nada foi inserido")


if __name__ == "__main__":
    main()