from DOMAIN.vanzare import to_string
from LOGIC.c_r_u_d import adauga_vanzare, sterge_vanzare, modifica_vanzare
from LOGIC.functionalitati import aplicare_reduceri, modificare_gen_carte_dupa_titlu, pret_minim_dupa_gen, \
    ordonare_cresc_dupa_pret, afisare_nr_titluri_distincte_dupa_gen

# FUNCTIONALITATI
def ui_adauga_vanzare(lista,undolista, redolista):
    try:
        id = input("Dati ID-ul: ")
        titlucarte = input("Dati titlul cartii: ")
        gencarte = input("Dati genul cartii: ")
        pret = float(input('Dati pretul cartii: '))
        tipreducere = input("Dati tipul de reducere (silver, gold, none): ")
        if tipreducere != "none" and tipreducere != "silver" and tipreducere != "gold":
            raise ValueError("!!! Tipul de reducere nu este acceptat. Trebuie sa fie silver, gold sau none !!!")
        undolista.append(lista)
        redolista.clear()
        return adauga_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def afisare_lista(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_sterge_vanzare(lista, undolista, redolista):
    try:
        id = input("Dati ID-ul vanzarii pe care vreti sa o stergeti: ")
        undolista.append(lista)
        redolista.clear()
        return sterge_vanzare(id, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def ui_modifica_vanzare(lista, undolista, redolista):
    try:
        id = input("Dati ID-ul vanzarii pe care vreti sa o modificati: ")
        titlucarte = input("Dati noul titlu al cartii: ")
        gencarte = input("Dati noul gen al cartii: ")
        pret = float(input('Dati noul pret al cartii: '))
        tipreducere = input("Dati noul tip de reducere (silver, gold, none): ")
        if tipreducere != "none" and tipreducere != "silver" and tipreducere != "gold":
            raise ValueError("!!! Tipul de reducere nu este acceptat. Trebuie sa fie silver, gold sau none !!!")
        undolista.append(lista)
        redolista.clear()
        return modifica_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def ui_aplicare_reduceri(lista, undolista, redolista):
    undolista.append(lista)
    redolista.clear()
    return aplicare_reduceri(lista)


def ui_modificare_gen_dupa_titlu(lista, undolista, redolista):
    titlu = input("Introduceti titlul pentru care urmeaza sa efectuati modificarea:")
    genmodificat = input("Introduceti genul modificat:")
    undolista.append(lista)
    redolista.clear()
    return modificare_gen_carte_dupa_titlu(titlu, genmodificat, lista)


def ui_pret_minim_dupa_gen(lista):
    rezultat = pret_minim_dupa_gen(lista)
    for gen in rezultat:
        print("Pretul minim pentru genul {} este {}".format(gen, rezultat[gen]))


def ui_ordonare_cresc_dupa_pret(lista):
    afisare_lista(ordonare_cresc_dupa_pret(lista))


def ui_afisare_nr_titluri_distincte_dupa_gen(lista):
    rezultat = afisare_nr_titluri_distincte_dupa_gen(lista)
    for gen in rezultat:
        print("Pentru genul {} exista {} titluri distincte".format(gen, rezultat[gen]))


def undo(lista, undo_lista, redo_lista):
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    return lista


def redo(lista, undo_lista, redo_lista):
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    return lista


# MENIU
def print_menu_simplu():
    print("\t \t MENIU ")
    print("1. Adaugare vanzare.")
    print("\t a. Afisare vanzari totale.")
    print("2. Stergere vanzare.")
    print("3. Modificare vanzare.")
    print("4. Aplicare reduceri.")
    print("5. Modificare gen al unei vanzari cu titlul dat.")
    print("6. Afisare pret minim pentru fiecare gen")
    print("7. Ordonare vanzari (crescator) in functie de pret.")
    print("8. Afisare numar de titluri distincte pentru fiecare gen")
    print("+ Alte optiuni:")
    print("\t u.Undo")
    print("\t r.Redo")
    print("\t s.Schimba interfata. ")
    print("x. Iesire.")


def print_menu_2():
    print("\t \t MENIU ")
    print("add = Adaugare vanzare")
    print("delete = Stergere vanzare")
    print("show = Afisare vanzari")
    print("change = Schimba interfata")
    print("stop = Oprire program")


def run_menu_simplu(lista):
    undolista = []
    redolista = []
    while True:
        print_menu_simplu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            lista = ui_adauga_vanzare(lista, undolista, redolista)
        elif optiune == "a":
            afisare_lista(lista)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista, undolista, redolista)
            print("Lista a fost modificata. Element sters.")
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista, undolista, redolista)
        elif optiune == "4":
            lista = ui_aplicare_reduceri(lista, undolista, redolista)
        elif optiune == "5":
            lista = ui_modificare_gen_dupa_titlu(lista, undolista, redolista)
        elif optiune == "6":
            ui_pret_minim_dupa_gen(lista)
        elif optiune == "7":
            ui_ordonare_cresc_dupa_pret(lista)
        elif optiune == "8":
            ui_afisare_nr_titluri_distincte_dupa_gen(lista)
        elif optiune == "u":
            if len(undolista) > 0:
                lista = undo(lista, undolista, redolista)
            else:
                print("!!! Nu se mai poate face UNDO !!!")
        elif optiune == "r":
            if len(redolista) > 0:
                lista = redo(lista, undolista, redolista)
            else:
                print("!!! Nu se mai poate face REDO !!!")
        elif optiune == "s":
            run_menu_2(lista)
        elif optiune == "x":
            print("Ati iesit din consola! \n")
            break
        else:
            print("Optiune gresita! Reincercati: ")


def run_menu_2(lista):
    print_menu_2()
    breaker = 1
    while True:
        comanda_linie = input("Introduceti comenzile dorite separate prin \';\': ")
        comanda_linie = comanda_linie.split(';')
        for comanda in comanda_linie:
            comanda = comanda.split(',')
            if comanda[0] == "add":
                if len(comanda) == 6:
                    try:
                        id = comanda[1]
                        titlu = comanda[2]
                        gen = comanda[3]
                        pret = float(comanda[4])
                        reducere = comanda[5]
                        lista = adauga_vanzare(id, titlu, gen, pret, reducere, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print("Eroare: !!! Numar de parametrii invalid !!!")
            elif comanda[0] == "show":
                afisare_lista(lista)
            elif comanda[0] == "delete":
                if len(comanda) == 2:
                    try:
                        id = comanda[1]
                        lista = sterge_vanzare(id, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print("Eroare: !!! Numar de parametrii invalid !!!")
            elif comanda[0] == "change":
                run_menu_simplu(lista)
                breaker = 0
            elif comanda[0] == "stop":
                print("Ati iesit din consola! \n")
                breaker = 0
                break
            else:
                print("!!! Comanda este gresita !!! Reincercati.")
        if breaker == 0:
            break


def run_program(lista):
    while True:
        print("\t \t MENIU ")
        print("1.Consola simpla.")
        print("2.Consola liniara.")
        print("x.Iesire")
        optiune_meniu = input("Alegeti interfata/meniul dorit(a):")
        if optiune_meniu == "1":
            run_menu_simplu(lista)
        elif optiune_meniu == "2":
            run_menu_2(lista)
        elif optiune_meniu == "x":
            print("Ati iesit din program! \n")
            break
        else:
            print("!!! Optiunea introdusa nu exista. Reincercati !!!")
