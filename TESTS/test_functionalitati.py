from DOMAIN.vanzare import get_pret, get_gen_carte, get_id
from LOGIC.c_r_u_d import adauga_vanzare, get_by_id
from LOGIC.functionalitati import aplicare_reduceri, modificare_gen_carte_dupa_titlu, pret_minim_dupa_gen, \
    ordonare_cresc_dupa_pret, afisare_nr_titluri_distincte_dupa_gen


def test_aplicare_reduceri():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    lista = adauga_vanzare("5", "Game of Thornes", "S.F. mitologic", 100, "none", lista)

    lista = aplicare_reduceri(lista)

    assert get_pret(get_by_id("1", lista)) == 66.5
    assert get_pret(get_by_id("2", lista)) == 49.9
    assert get_pret(get_by_id("3", lista)) == 72.0


def test_modificare_gen_carte_dupa_titlu():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    lista = adauga_vanzare("5", "Game of Thrones", "S.F. mitologic", 100, "none", lista)

    titlu = "Carrie"
    gen_modificat = "Horror Psihologic"
    lista = modificare_gen_carte_dupa_titlu(titlu, gen_modificat, lista)

    assert get_gen_carte(get_by_id("1", lista)) == gen_modificat
    assert get_gen_carte(get_by_id("3", lista)) == "Economie"

    titlu = "Game of Thrones"
    gen_modificat = "S.F."

    lista = modificare_gen_carte_dupa_titlu(titlu, gen_modificat, lista)

    assert get_gen_carte(get_by_id("5", lista)) == gen_modificat


def test_pret_minim_dupa_gen():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    lista = adauga_vanzare("5", "Game of Thrones", "S.F. mitologic", 100, "none", lista)
    lista = adauga_vanzare("6", "Ocolul pamantului in 80 de zile", "Aventura", 55.6, "silver", lista)
    lista = adauga_vanzare("7", "Arta manipularii", "Psihologie", 95.0, "none", lista)

    auxiliar = pret_minim_dupa_gen(lista)

    assert len(auxiliar) == 5
    assert auxiliar["Aventura"] == 49.9
    assert auxiliar["Psihologie"] == 95


def test_ordonare_crescatoare_dupa_pret():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)

    ordonat = ordonare_cresc_dupa_pret(lista)

    assert get_id(ordonat[0]) == "2"
    assert get_id(ordonat[1]) == "1"
    assert get_id(ordonat[2]) == "3"


def test_afisare_nr_titluri_distincte_dupa_gen():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    lista = adauga_vanzare("5", "Game of Thrones", "S.F. mitologic", 100, "none", lista)
    lista = adauga_vanzare("6", "Ocolul pamantului in 80 de zile", "Aventura", 55.6, "silver", lista)
    lista = adauga_vanzare("7", "5 saptamani in balon", "Aventura", 39.9, "silver", lista)

    auxiliar = afisare_nr_titluri_distincte_dupa_gen(lista)

    assert len(auxiliar) == 5
    assert auxiliar["Aventura"] == 2
