from TESTS.test_crud import test_adauga_vanzare, test_sterge_vanzare, test_modifica_vanzare, test_get_by_id
from TESTS.test_domain import test_vanzare
from TESTS.test_functionalitati import test_aplicare_reduceri, test_modificare_gen_carte_dupa_titlu, \
    test_pret_minim_dupa_gen, test_ordonare_crescatoare_dupa_pret, test_afisare_nr_titluri_distincte_dupa_gen
from TESTS.test_undo_redo import test_undo_redo


def run_all_tests():
    test_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_get_by_id()
    test_aplicare_reduceri()
    test_modificare_gen_carte_dupa_titlu()
    test_pret_minim_dupa_gen()
    test_ordonare_crescatoare_dupa_pret()
    test_afisare_nr_titluri_distincte_dupa_gen()
    test_undo_redo()


