from solucions1 import *


def test_suma_parells():
    # Cas bàsic
    assert suma_parells([1, 2, 3, 4, 5]) == 6

    # Només senars
    assert suma_parells([1, 3, 5, 7]) == 0

    # Llista buida
    assert suma_parells([]) == 0

    # Només parells
    assert suma_parells([2, 4, 6, 8]) == 20

    # Amb números negatius
    assert suma_parells([-2, -1, 0, 1, 2]) == 0


def test_compta_vocals():
    # Cas bàsic
    assert compta_vocals("Hola món") == 2

    # Sense vocals
    assert compta_vocals("xyz") == 0

    # String buit
    assert compta_vocals("") == 0

    # Només vocals
    assert compta_vocals("aeiou") == 5

    # Majúscules i minúscules
    assert compta_vocals("AEIOUaeiou") == 10


def test_inverteix_diccionari():
    # Cas bàsic
    assert inverteix_diccionari({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    # Diccionari buit
    assert inverteix_diccionari({}) == {}

    # Valors duplicats (es queda amb l'últim)
    resultat = inverteix_diccionari({"a": 1, "b": 1})
    assert resultat == {1: "b"} or resultat == {1: "a"}

    # Un sol element
    assert inverteix_diccionari({"clau": 42}) == {42: "clau"}


def test_troba_maxim_minim():
    # Cas bàsic
    assert troba_maxim_minim([3.5, 1.2, 7.8, 2.1]) == (7.8, 1.2)

    # Un sol element
    assert troba_maxim_minim([5.0]) == (5.0, 5.0)

    # Amb números negatius
    assert troba_maxim_minim([-5, -1, -10, -3]) == (-1, -10)

    # Amb enters
    assert troba_maxim_minim([1.0, 2.0, 3.0]) == (3.0, 1.0)


def test_filtra_per_longitud():
    # Cas bàsic
    assert filtra_per_longitud(["hola", "a", "Python"], 3) == ["hola", "Python"]

    # Llista buida
    assert filtra_per_longitud([], 5) == []

    # Totes les paraules compleixen
    assert filtra_per_longitud(["casa", "arbre", "cotxe"], 3) == [
        "casa",
        "arbre",
        "cotxe",
    ]

    # Cap paraula compleix
    assert filtra_per_longitud(["a", "de", "el"], 5) == []

    # Longitud mínima 0
    assert filtra_per_longitud(["a", "bc", "def"], 0) == ["a", "bc", "def"]


def test_agrupa_per_paritat():
    # Cas bàsic
    assert agrupa_per_paritat([1, 2, 3, 4]) == {"parells": [2, 4], "senars": [1, 3]}

    # Només parells
    assert agrupa_per_paritat([2, 4, 6]) == {"parells": [2, 4, 6], "senars": []}

    # Només senars
    assert agrupa_per_paritat([1, 3, 5]) == {"parells": [], "senars": [1, 3, 5]}

    # Llista buida
    assert agrupa_per_paritat([]) == {"parells": [], "senars": []}

    # Amb negatius i zero
    assert agrupa_per_paritat([-2, -1, 0, 1, 2]) == {
        "parells": [-2, 0, 2],
        "senars": [-1, 1],
    }


def test_es_palindrom():
    # Palíndroms clàssics
    assert es_palindrom("ala") == True
    assert es_palindrom("radar") == True

    # Amb espais
    assert es_palindrom("Anar a Salas a Rana") == True

    # Amb majúscules
    assert es_palindrom("Ana") == True

    # No palíndrom
    assert es_palindrom("hola") == False

    # String buit
    assert es_palindrom("") == True

    # Un sol caràcter
    assert es_palindrom("a") == True


def test_fusiona_diccionaris():
    # Cas bàsic amb claus comunes
    assert fusiona_diccionaris({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {
        "a": 1,
        "b": 5,
        "c": 4,
    }

    # Sense claus comunes
    assert fusiona_diccionaris({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    # Primer diccionari buit
    assert fusiona_diccionaris({}, {"a": 1}) == {"a": 1}

    # Segon diccionari buit
    assert fusiona_diccionaris({"a": 1}, {}) == {"a": 1}

    # Ambdós buits
    assert fusiona_diccionaris({}, {}) == {}


def test_crea_parelles():
    # Cas bàsic
    assert crea_parelles([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]

    # Primera llista més curta
    assert crea_parelles([1, 2], ["a", "b", "c"]) == [(1, "a"), (2, "b")]

    # Segona llista més curta
    assert crea_parelles([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]

    # Llistes buides
    assert crea_parelles([], []) == []

    # Una llista buida
    assert crea_parelles([1, 2], []) == []


def test_compta_frequencia():
    # Cas bàsic
    assert compta_frequencia(["gat", "gos", "gat", "ocell"]) == {
        "gat": 2,
        "gos": 1,
        "ocell": 1,
    }

    # Llista buida
    assert compta_frequencia([]) == {}

    # Tots els elements iguals
    assert compta_frequencia(["a", "a", "a"]) == {"a": 3}

    # Tots diferents
    assert compta_frequencia(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}

    # Un sol element
    assert compta_frequencia(["hola"]) == {"hola": 1}
