from solucions2 import *


def test_valida_email():
    # Emails vàlids
    assert valida_email("usuari@domini.com") == True
    assert valida_email("nom.cognom@empresa.cat") == True
    assert valida_email("a@b.c") == True

    # Sense @
    assert valida_email("usuaridomini.com") == False

    # Múltiples @
    assert valida_email("usuari@@domini.com") == False
    assert valida_email("us@uari@domini.com") == False

    # Sense contingut abans del @
    assert valida_email("@domini.com") == False

    # Sense contingut després del @
    assert valida_email("usuari@") == False

    # Sense punt després del @
    assert valida_email("usuari@domini") == False

    # Punt al final sense domini
    assert valida_email("usuari@domini.") == False


def test_aplana_llista():
    # Cas bàsic
    assert aplana_llista([[1, 2], [3, 4, 5], [6]]) == [1, 2, 3, 4, 5, 6]

    # Llista buida
    assert aplana_llista([]) == []

    # Sublistes buides
    assert aplana_llista([[], [], []]) == []

    # Una sola sublista
    assert aplana_llista([[1, 2, 3]]) == [1, 2, 3]

    # Mescla de sublistes buides i plenes
    assert aplana_llista([[1], [], [2, 3], [], [4]]) == [1, 2, 3, 4]


def test_troba_duplicats():
    # Cas bàsic
    assert troba_duplicats([1, 2, 3, 2, 4, 3, 5]) == {2, 3}

    # Sense duplicats
    assert troba_duplicats([1, 2, 3]) == set()

    # Llista buida
    assert troba_duplicats([]) == set()

    # Tots duplicats
    assert troba_duplicats([1, 1, 1, 1]) == {1}

    # Múltiples duplicats
    assert troba_duplicats([1, 1, 2, 2, 3, 3]) == {1, 2, 3}

    # Amb negatius
    assert troba_duplicats([-1, -1, 0, 1, 1]) == {-1, 1}


def test_ordena_per_frequencia():
    # Cas bàsic
    assert ordena_per_frequencia(["gat", "gos", "gat", "ocell", "gos", "gat"]) == [
        ("gat", 3),
        ("gos", 2),
        ("ocell", 1),
    ]

    # Mateixa frequència (ordre alfabètic)
    assert ordena_per_frequencia(["b", "a", "c"]) == [("a", 1), ("b", 1), ("c", 1)]

    # Llista buida
    assert ordena_per_frequencia([]) == []

    # Una sola paraula
    assert ordena_per_frequencia(["hola"]) == [("hola", 1)]

    # Totes iguals
    assert ordena_per_frequencia(["a", "a", "a"]) == [("a", 3)]

    # Mescla de frequències
    assert ordena_per_frequencia(["x", "y", "x", "z", "y", "x"]) == [
        ("x", 3),
        ("y", 2),
        ("z", 1),
    ]


def test_transforma_text():
    # Majúscules
    assert transforma_text("hola món", str.upper) == "HOLA MÓN"

    # Invertir paraules
    assert transforma_text("hola món", lambda x: x[::-1]) == "aloh nóm"

    # Text buit
    assert transforma_text("", str.upper) == ""

    # Una paraula
    assert transforma_text("Python", str.lower) == "python"

    # Capitalitzar
    assert transforma_text("hola món python", str.capitalize) == "Hola Món Python"

    # Funció personalitzada
    assert transforma_text("ab cd ef", lambda x: x[0]) == "a c e"


def test_interseccio_diccionaris():
    # Cas bàsic
    assert interseccio_diccionaris(
        {"a": 5, "b": 3, "c": 8}, {"b": 7, "c": 2, "d": 1}
    ) == {"b": 3, "c": 2}

    # Sense intersecció
    assert interseccio_diccionaris({"a": 1}, {"b": 2}) == {}

    # Diccionaris buits
    assert interseccio_diccionaris({}, {}) == {}
    assert interseccio_diccionaris({"a": 1}, {}) == {}

    # Total intersecció
    assert interseccio_diccionaris({"a": 5, "b": 3}, {"a": 2, "b": 7}) == {
        "a": 2,
        "b": 3,
    }

    # Una clau en comú
    assert interseccio_diccionaris({"a": 10, "b": 5}, {"a": 3, "c": 8}) == {"a": 3}


def test_troba_subcadena_mes_llarga():
    # Cas bàsic
    assert troba_subcadena_mes_llarga("abcdef", "xbcde") == "bcde"

    # Un sol caràcter
    assert troba_subcadena_mes_llarga("hola", "adeu") == "a"

    # Strings iguals
    assert troba_subcadena_mes_llarga("test", "test") == "test"

    # Sense coincidències
    assert troba_subcadena_mes_llarga("abc", "xyz") == ""

    # String buit
    assert troba_subcadena_mes_llarga("", "test") == ""
    assert troba_subcadena_mes_llarga("test", "") == ""

    # Subcadena al principi
    assert troba_subcadena_mes_llarga("abcxyz", "abcdef") == "abc"

    # Subcadena al final
    assert troba_subcadena_mes_llarga("xyzabc", "defabc") == "abc"


def test_descodifica_run_length():
    # Cas bàsic
    assert descodifica_run_length("3a2b1c") == "aaabbc"

    # Exemple 2
    assert descodifica_run_length("1h4o2l1a") == "hoooolla"

    # Un sol caràcter
    assert descodifica_run_length("5x") == "xxxxx"

    # String buit
    assert descodifica_run_length("") == ""

    # Números més grans
    assert descodifica_run_length("10a") == "aaaaaaaaaa"

    # Múltiples caràcters
    assert descodifica_run_length("2a3b1c2d") == "aabbbcdd"
