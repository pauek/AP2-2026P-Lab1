def suma_parells(numeros: list[int]) -> int:
    """
    Retorna la suma de tots els números parells de la llista.
    Exemple: suma_parells([1, 2, 3, 4, 5]) -> 6
    """
    pass


def compta_vocals(text: str) -> int:
    """
    Compta el nombre de vocals (a, e, i, o, u) en un text.
    No distingeix entre majúscules i minúscules.
    Exemple: compta_vocals("Hola món") -> 3
    """
    pass


def inverteix_diccionari(d: dict[str, int]) -> dict[int, str]:
    """
    Inverteix les claus i valors d'un diccionari.
    Si hi ha valors duplicats, es queda amb l'última clau.
    Exemple: inverteix_diccionari({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    pass


def troba_maxim_minim(numeros: list[float]) -> tuple[float, float]:
    """
    Retorna una tupla amb el valor màxim i mínim de la llista.
    Exemple: troba_maxim_minim([3.5, 1.2, 7.8, 2.1]) -> (7.8, 1.2)
    """
    pass


def filtra_per_longitud(paraules: list[str], longitud_minima: int) -> list[str]:
    """
    Retorna només les paraules que tenen una longitud >= longitud_minima.
    Exemple: filtra_per_longitud(["hola", "a", "Python"], 3) -> ["hola", "Python"]
    """
    pass


def agrupa_per_paritat(numeros: list[int]) -> dict[str, list[int]]:
    """
    Agrupa els números en parells i senars.
    Retorna un diccionari amb claus "parells" i "senars".
    Exemple: agrupa_per_paritat([1, 2, 3, 4]) -> {"parells": [2, 4], "senars": [1, 3]}
    """
    pass


def es_palindrom(text: str) -> bool:
    """
    Verifica si un text és un palíndrom (es llegeix igual d'esquerra a dreta).
    Ignora espais i majúscules.
    Exemple: es_palindrom("Anar a Salas a Rana") -> True
    """
    pass


def fusiona_diccionaris(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Fusiona dos diccionaris sumant els valors de les claus comunes.
    Exemple: fusiona_diccionaris({"a": 1, "b": 2}, {"b": 3, "c": 4})
             -> {"a": 1, "b": 5, "c": 4}
    """
    pass


def crea_parelles(llista1: list[int], llista2: list[str]) -> list[tuple[int, str]]:
    """
    Crea parelles dels elements de dues llistes.
    Si les llistes tenen longituds diferents, s'atura a la més curta.
    Exemple: crea_parelles([1, 2, 3], ["a", "b"]) -> [(1, "a"), (2, "b")]
    """
    pass


def compta_frequencia(paraules: list[str]) -> dict[str, int]:
    """
    Compta quantes vegades apareix cada paraula a la llista.
    Exemple: compta_frequencia(["gat", "gos", "gat", "ocell"])
             -> {"gat": 2, "gos": 1, "ocell": 1}
    """
    pass
