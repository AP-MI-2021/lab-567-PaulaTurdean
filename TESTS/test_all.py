from TESTS.test_crud import test_adauga_vanzare, test_sterge_vanzare, test_modifica_vanzare
from TESTS.test_domain import test_vanzare


def run_all_tests():
    test_vanzare()
    test_adauga_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
