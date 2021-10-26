from DOMAIN.vanzare import get_id, get_titlu_carte, get_gen_carte, get_pret, get_tip_reducere
from LOGIC.c_r_u_d import adauga_vanzare, get_by_id, sterge_vanzare, modifica_vanzare


def test_adauga_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_titlu_carte(get_by_id("1", lista)) == "Carrie"
    assert get_gen_carte(get_by_id("1", lista)) == "Nuvela-Horror"
    assert get_pret(get_by_id("1", lista)) == 70
    assert get_tip_reducere(get_by_id("1", lista)) == "silver"


def test_get_by_id():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)

    assert get_by_id("2", lista) == ["2", "5 saptamani in balon", "Aventura", 49.9, "none"]
    assert get_by_id("3", lista) is None


def test_sterge_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)

    lista = sterge_vanzare("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    lista = sterge_vanzare("3", lista)

    assert len(lista) == 1
    assert get_by_id("2", lista) is not None


def test_modifica_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)

    lista = modifica_vanzare("1", "Gambitul damei", "Poveste istorica", 60.5, "silver", lista)

    vanzareupdatata = get_by_id("1", lista)
    assert get_id(vanzareupdatata) == "1"
    assert get_titlu_carte(vanzareupdatata) == "Gambitul damei"
    assert get_gen_carte(vanzareupdatata) == "Poveste istorica"
    assert get_pret(vanzareupdatata) == 60.5
    assert get_tip_reducere(vanzareupdatata) == "silver"

    vanzareneupdatata = get_by_id("2", lista)
    assert get_id(vanzareneupdatata) == "2"
    assert get_titlu_carte(vanzareneupdatata) == "5 saptamani in balon"
    assert get_gen_carte(vanzareneupdatata) == "Aventura"
    assert get_pret(vanzareneupdatata) == 49.9
    assert get_tip_reducere(vanzareneupdatata) == "none"
