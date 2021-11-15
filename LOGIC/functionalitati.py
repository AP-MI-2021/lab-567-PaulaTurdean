from DOMAIN.vanzare import get_tip_reducere, get_pret, creeaza_vanzare, get_id, get_titlu_carte, get_gen_carte
from LOGIC.c_r_u_d import get_by_titlu


def aplicare_reduceri(lista):
    """
    Aplica reducerile corespunzatoare pentru fiecare vanzare. (silver = 5%, gold = 10%, none = 0%)
    :param lista: Lista vanzarilor.
    :return: Returneaza lista vanzarilor cu reducerile aplicate.
    """
    # FOLOSIM METODA PRIN CARE CREAM O LISTA NOUA
    listanoua = []
    for vanzare in lista:
        if get_tip_reducere(vanzare) == "silver":
            pretmodificat = get_pret(vanzare) - ((get_pret(vanzare) * 5) / 100)
            vanzarenoua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu_carte(vanzare),
                get_gen_carte(vanzare),
                pretmodificat,
                get_tip_reducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        elif get_tip_reducere(vanzare) == "gold":
            pretmodificat = get_pret(vanzare) - ((get_pret(vanzare) * 10) / 100)
            vanzarenoua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu_carte(vanzare),
                get_gen_carte(vanzare),
                pretmodificat,
                get_tip_reducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)

    return listanoua


def modificare_gen_carte_dupa_titlu(titlu, genmodificat, lista):
    """
    Modifica genul unei carti/vanzari dupa titlul cautat.
    :param titlu: Titlul introdus de la tastatura.
    :param genmodificat: genul cartii modificat.
    :param lista: lista de carti.
    :return: Returneaza lista cu genurile modificate dupa titlul introdus initial.
    """
    if get_by_titlu(titlu, lista) is None:
        print(ValueError("Titlul dat nu exista in lista de vanzari!"))
        return lista
    else:
        listanoua = []
        for vanzare in lista:
            if get_titlu_carte(vanzare) == titlu:
                vanzare_noua = creeaza_vanzare(
                    get_id(vanzare),
                    get_titlu_carte(vanzare),
                    genmodificat,
                    get_pret(vanzare),
                    get_tip_reducere(vanzare)
                )
                listanoua.append(vanzare_noua)
            else:
                listanoua.append(vanzare)
        return listanoua


def pret_minim_dupa_gen(lista):
    """
    Creeaza un dictionar care contine pretul minim pentru fiecare gen din lista de vanzari.
    Cheia: genul, Valoarea: pretul.
    :param lista: Lista de carti/vanzari
    :return: Returneaza in dictionar care contine pretul minim pentru fiecare gen din lista.
    """
    rezultat = {}
    for vanzare in lista:
        gen = get_gen_carte(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def ordonare_cresc_dupa_pret(lista):
    """
    Ordoneaza lista crescator dupa pret (de la cel mai mic la cel mai mare pret)
    :param lista: Lista de vanzari
    :return: Returneaza lista ordonata crescator dupa pretul vanzarilor.
    """
    return sorted(lista, key=lambda vanzare: get_pret(vanzare))


def afisare_nr_titluri_distincte_dupa_gen(lista):
    """
    Creeaza un dictionar cu numarul de titluri distincte pentru fiecare gen.
    Cheia: genul, Valoare: Numarul de titluri.
    :param lista: Lista de carti.
    :return: Returneaza un dictionar cu numarul de titluri distincte pentru fiecare gen.
    """
    rezultat = {}
    listatitluri = []
    for vanzare in lista:
        gen = get_gen_carte(vanzare)
        titlu = get_titlu_carte(vanzare)
        if gen in rezultat:
            if titlu not in listatitluri:
                listatitluri.append(titlu)
                rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1
            listatitluri.append(titlu)
    return rezultat
