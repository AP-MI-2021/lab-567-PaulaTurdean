from DOMAIN.vanzare import get_gen_carte, get_pret
from LOGIC.c_r_u_d import adauga_vanzare, get_by_id, modifica_vanzare, sterge_vanzare
from USERINTERFACE.consola import undo, redo


def test_undo_redo():
    lista = []
    undolista = []
    redolista = []
    # adaugare element (1)
    undolista.append(lista)
    redolista.clear()
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    # adaugare element (2)
    undolista.append(lista)
    redolista.clear()
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    # adaugare element (3)
    undolista.append(lista)
    redolista.clear()
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    # VERIFICARI
    assert len(lista) == 3

    # 1 - adaugam un alt element
    undolista.append(lista)
    redolista.clear()
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    # VERIFICARI
    assert len(lista) == 4
    lista = undo(lista, undolista, redolista)
    assert len(lista) == 3
    assert get_by_id('4', lista) is None
    lista = redo(lista, undolista, redolista)
    assert len(lista) == 4
    assert get_by_id('4', lista) is not None

    # 2 - modificam un gen
    assert get_gen_carte(get_by_id('2', lista)) == "Aventura"
    undolista.append(lista)
    redolista.clear()
    lista = modifica_vanzare("2", "5 saptamani in balon", "Aventura--", 49.9, "none", lista)
    # VERIFICARI
    assert get_gen_carte(get_by_id('2', lista)) == "Aventura--"
    lista = undo(lista, undolista, redolista)
    assert get_gen_carte(get_by_id('2', lista)) == "Aventura"

    # 3 - stergem o vanzare si modificam un pret
    assert len(lista) == 4
    undolista.append(lista)
    redolista.clear()
    lista = sterge_vanzare("3", lista)
    # VERIFICARI
    assert len(lista) == 3
    assert get_by_id('3', lista) is None
    assert get_pret(get_by_id("2", lista)) == 49.9
    undolista.append(lista)
    redolista.clear()
    lista = modifica_vanzare("2", "5 saptamani in balon", "Aventura--", 55.8, "none", lista)
    assert get_pret(get_by_id("2", lista)) == 55.8
    lista = undo(lista, undolista, redolista)
    lista = undo(lista, undolista, redolista)
    # VERIFICARI
    assert len(lista) == 4
    assert get_by_id('3', lista) is not None
    assert get_pret(get_by_id("2", lista)) == 49.9
    lista = redo(lista, undolista, redolista)
    assert len(lista) == 3
    assert get_by_id('3', lista) is None











