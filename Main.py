# TURDEAN PAULA-FLORINA cod: 7903 => 1 + 7903 % 4 = 1 + 3 = PROBLEMA 4
"""
Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:
4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID.
O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
4.2. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
4.3. Modificarea genului pentru un titlu dat.
4.4. Determinarea prețului minim pentru fiecare gen.
4.5. Ordonarea vânzărilor crescător după preț.
4.6. Afișarea numărului de titluri distincte pentru fiecare gen.
4.7. Undo.
"""
from LOGIC.c_r_u_d import adauga_vanzare
from TESTS.test_all import run_all_tests
from USERINTERFACE.consola import run_program


def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare("1", "Carrie", "Nuvela-Horror", 70, "silver", lista)
    lista = adauga_vanzare("2", "5 saptamani in balon", "Aventura", 49.9, "none", lista)
    lista = adauga_vanzare("3", "Tata sarac tata bogat", "Economie", 80, "gold", lista)
    lista = adauga_vanzare("4", "Cum sa iti reinventezi viata?", "Psihologie", 104.99, "gold", lista)
    lista = adauga_vanzare("5", "Game of Thrones", "S.F. mitologic", 100, "none", lista)
    lista = adauga_vanzare("6", "Ocolul pamantului in 80 de zile", "Aventura", 55.6, "silver", lista)
    lista = adauga_vanzare("7", "Arta manipularii", "Psihologie", 95.0, "none", lista)
    lista = adauga_vanzare("8", "5 saptamani in balon", "Aventura", 39.9, "silver", lista)
    run_program(lista)


main()
