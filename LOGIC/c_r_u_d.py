from DOMAIN.vanzare import creeaza_vanzare, get_id


def adauga_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    """
     Adauga o vanzare in lista de vanzari.
    :param id: Un string reprezentativ (ex.: 1, 2, 3, ...).
    :param titlucarte: Un string.
    :param gencarte: Un string.
    :param pret: Un numar rational (float).
    :param tipreducere: Un string ales din : NONE, SILVER sau GOLD.
    :return: Returneaza lista de vanzari.
    """
    vanzare = creeaza_vanzare(id, titlucarte, gencarte, pret, tipreducere)
    return lista + [vanzare]


def get_by_id(id, lista):
    """
    Gaseste o vanzare dupa ID-ul dat.
    :param id: Un string.
    :param lista: Lista de vanzari.
    :return: Returneaza vanzarea cu ID-ul dat din lista (sau None daca aceasta nu exista).
    """
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None


def sterge_vanzare(id, lista):
    """
    Sterge o vanzare cu ID-ul dat din lista.
    :param id: ID-ul vanzarii care se va sterge.
    :param lista: Lista de vanzari.
    :return: Returneaza o lista de vanzari fara elementul cu ID-ul dat.
    """
    return [vanzare for vanzare in lista if get_id(vanzare) != id]


def modifica_vanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    """
    Modifica vanzarea cu ID-ul dat.
    :param id: ID-ul prajiturii ce trebuie modificata.
    :param titlucarte: Titlul nou.
    :param gencarte: Genul nou.
    :param pret: Pretul nou.
    :param tipreducere: Tipul nou de reducere.
    :param lista: Lista de vanzari
    :return: O lista de vanzari modificata.
    """
    listanoua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzarenoua = creeaza_vanzare(id, titlucarte, gencarte, pret, tipreducere)
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua
