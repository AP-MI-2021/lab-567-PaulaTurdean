def creeaza_vanzare(id, titlucarte, gencarte, pret, tipreducere):
    """
    Creeaza un dictionare ce reprezinta o VANZARE.
    :param id: Un string reprezentativ (ex.: 1, 2, 3, ...).
    :param titlucarte: Un string.
    :param gencarte: Un string.
    :param pret: Un numar rational (float).
    :param tipreducere: Un string ales din : NONE, SILVER sau GOLD.
    :return: Returneaza un dictionare ce reprezinta o vanzare.
    """
    return[
        id,
        titlucarte,
        gencarte,
        pret,
        tipreducere
    ]


def get_id(vanzare):
    """
    Preia ID-ul unei vanzari.
    :param vanzare: Dictionarul ce contine o vanzare.
    :return: Returneaza ID-ul vanzarii.
    """
    return vanzare[0]


def get_titlu_carte(vanzare):
    """
    Preia titlul cartii vandute.
    :param vanzare: Dictionarul ce contine o vanzare.
    :return: Returneaza titlul cartii vandute.
    """
    return vanzare[1]


def get_gen_carte(vanzare):
    """
    Preia genul cartii vandute.
    :param vanzare: Dictionarul ce contine o vanzare.
    :return: Returneaza genul cartii vandute.
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Preia pretul vanzarii.
    :param vanzare: Dictionarul ce contine o vanzare.
    :return: Returneaza pretul vanzarii.
    """
    return vanzare[3]


def get_tip_reducere(vanzare):
    """
    Preia tipul reducerii aplicate pe costul vanzarii
    :param vanzare:
    :return:
    """
    return vanzare[4]


def to_string(vanzare):
    return "Id: {}, Titlu carte: {}, Gen carte: {}, Pret: {}, Tip reducere: {}".format(
        get_id(vanzare),
        get_titlu_carte(vanzare),
        get_gen_carte(vanzare),
        get_pret(vanzare),
        get_tip_reducere(vanzare)
    )
