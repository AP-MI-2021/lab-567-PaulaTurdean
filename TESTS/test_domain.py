from DOMAIN.vanzare import creeaza_vanzare, get_id, get_titlu_carte, get_gen_carte, get_pret, get_tip_reducere


def test_vanzare():
    vanzare = creeaza_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver")
    assert get_id(vanzare) == "1"
    assert get_titlu_carte(vanzare) == "Carrie"
    assert get_gen_carte(vanzare) == "Nuvela-Horror"
    assert get_pret(vanzare) == 70
    assert get_tip_reducere(vanzare) == "silver"
