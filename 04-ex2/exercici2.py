from typing import Callable


def valida_email(email: str) -> bool:
    """
    Valida si un string és un email vàlid.
    Ha de contenir exactament un @, almenys un caràcter abans i després del @,
    i almenys un punt després del @.
    Exemple: valida_email("usuari@domini.com") -> True
    Exemple: valida_email("usuari@domini") -> False
    """
    ...


def aplana_llista(llista: list[list[int]]) -> list[int]:
    """
    Converteix una llista de llistes en una llista plana.
    Exemple: aplana_llista([[1, 2], [3, 4, 5], [6]]) -> [1, 2, 3, 4, 5, 6]
    """
    ...


def troba_duplicats(llista: list[int]) -> set[int]:
    """
    Retorna un conjunt amb els elements que apareixen més d'una vegada.
    Exemple: troba_duplicats([1, 2, 3, 2, 4, 3, 5]) -> {2, 3}
    Exemple: troba_duplicats([1, 2, 3]) -> set()
    """
    ...


def ordena_per_frequencia(paraules: list[str]) -> list[tuple[str, int]]:
    """
    Retorna una llista de tuples (paraula, frequència) ordenada per frequència descendent.
    Si dues paraules tenen la mateixa frequència, s'ordenen alfabèticament.
    Exemple: ordena_per_frequencia(["gat", "gos", "gat", "ocell", "gos", "gat"])
             -> [("gat", 3), ("gos", 2), ("ocell", 1)]
    """
    ...


def transforma_text(text: str, transformacio: Callable[[str], str]) -> str:
    """
    Aplica una funció de transformació a cada paraula del text.
    Les paraules estan separades per espais.
    Exemple: transforma_text("hola món", str.upper) -> "HOLA MÓN"
    Exemple: transforma_text("hola món", lambda x: x[::-1]) -> "aloh nóm"
    """
    ...


def interseccio_diccionaris(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Retorna un diccionari amb les claus que apareixen en ambdós diccionaris.
    El valor és el menor dels dos valors.
    Exemple: interseccio_diccionaris({"a": 5, "b": 3, "c": 8}, {"b": 7, "c": 2, "d": 1})
             -> {"b": 3, "c": 2}
    """
    ...


def troba_subcadena_mes_llarga(s1: str, s2: str) -> str:
    """
    Troba la subcadena comuna més llarga entre dos strings.
    Si hi ha múltiples subcadenes de la mateixa longitud, retorna la primera.
    Exemple: troba_subcadena_mes_llarga("abcdef", "xbcde") -> "bcde"
    Exemple: troba_subcadena_mes_llarga("hola", "adeu") -> "a"
    """
    ...


def descodifica_run_length(text: str) -> str:
    """
    Descodifica un string codificat amb run-length encoding.
    Format: "3a2b1c" significa "aaabbc"
    Exemple: descodifica_run_length("3a2b1c") -> "aaabbc"
    Exemple: descodifica_run_length("1h4o2l1a") -> "hhoooola"
    """
    ...
