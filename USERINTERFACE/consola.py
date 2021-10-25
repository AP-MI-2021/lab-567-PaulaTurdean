from DOMAIN.vanzare import to_string
from LOGIC.c_r_u_d import adauga_vanzare, sterge_vanzare, modifica_vanzare


def print_menu():
    print("1. Adaugare vanzare.")
    print("\t a. Afisare vanzari totale.")
    print("2. Stergere vanzare.")
    print("3. Modificare vanzare.")
    print("x. Iesire.")


def ui_adauga_vanzare(lista):
    id = input("Dati ID-ul: ")
    titlucarte = input("Dati titlul cartii: ")
    gencarte = input("Dati genul cartii: ")
    pret = float(input('Dati pretul cartii: '))
    tipreducere = input("Dati tipul de reducere (silver, gold, none): ")
    return adauga_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista)


def afisare_lista(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_sterge_vanzare(lista):
    id = input("Dati ID-ul vanzarii pe care vreti sa o stergeti: ")
    return sterge_vanzare(id, lista)


def ui_modifica_vanzare(lista):
    id = input("Dati ID-ul vanzarii pe care vreti sa o modificati: ")
    titlucarte = input("Dati noul titlu al cartii: ")
    gencarte = input("Dati noul gen al cartii: ")
    pret = float(input('Dati noul pret al cartii: '))
    tipreducere = input("Dati noul tip de reducere (silver, gold, none): ")
    return modifica_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            lista = ui_adauga_vanzare(lista)
        elif optiune == "a":
            afisare_lista(lista)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista)
            print("Lista a fost modificata. Element sters.")
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista)
        elif optiune == "x":
            print("Ati iesit din program!")
            break
        else:
            print("Optiune gresita! Reincercati: ")
