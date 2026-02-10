from typing import Callable


def valida_email(email: str) -> bool:
    """
    Valida si un string és un email vàlid.
    Ha de contenir exactament un @, almenys un caràcter abans i després del @,
    i almenys un punt després del @.
    Exemple: valida_email("usuari@domini.com") -> True
    Exemple: valida_email("usuari@domini") -> False
    """
    if email.count("@") != 1:
        return False

    parts = email.split("@")
    if len(parts[0]) == 0 or len(parts[1]) == 0:
        return False

    if "." not in parts[1]:
        return False

    # Verificar que hi ha contingut després del punt
    domini_parts = parts[1].split(".")
    if any(len(part) == 0 for part in domini_parts):
        return False

    return True


def aplana_llista(llista: list[list[int]]) -> list[int]:
    """
    Converteix una llista de llistes en una llista plana.
    Exemple: aplana_llista([[1, 2], [3, 4, 5], [6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultat = list[int]()
    for sublista in llista:
        resultat.extend(sublista)
    return resultat
    # Alternativa amb list comprehension:
    # return [element for sublista in llista for element in sublista]


def troba_duplicats(llista: list[int]) -> set[int]:
    """
    Retorna un conjunt amb els elements que apareixen més d'una vegada.
    Exemple: troba_duplicats([1, 2, 3, 2, 4, 3, 5]) -> {2, 3}
    Exemple: troba_duplicats([1, 2, 3]) -> set()
    """
    vistos: set[int] = set()
    duplicats: set[int] = set()

    for element in llista:
        if element in vistos:
            duplicats.add(element)
        else:
            vistos.add(element)

    return duplicats


def ordena_per_frequencia(paraules: list[str]) -> list[tuple[str, int]]:
    """
    Retorna una llista de tuples (paraula, frequència) ordenada per frequència descendent.
    Si dues paraules tenen la mateixa frequència, s'ordenen alfabèticament.
    Exemple: ordena_per_frequencia(["gat", "gos", "gat", "ocell", "gos", "gat"])
             -> [("gat", 3), ("gos", 2), ("ocell", 1)]
    """
    # Comptar frequències
    frequencia: dict[str, int] = {}
    for paraula in paraules:
        frequencia[paraula] = frequencia.get(paraula, 0) + 1

    # Ordenar per frequència (descendent) i després alfabèticament
    resultat = sorted(frequencia.items(), key=lambda x: (-x[1], x[0]))
    return resultat


def transforma_text(text: str, transformacio: Callable[[str], str]) -> str:
    """
    Aplica una funció de transformació a cada paraula del text.
    Les paraules estan separades per espais.
    Exemple: transforma_text("hola món", str.upper) -> "HOLA MÓN"
    Exemple: transforma_text("hola món", lambda x: x[::-1]) -> "aloh nóm"
    """
    paraules = text.split()
    paraules_transformades = [transformacio(paraula) for paraula in paraules]
    return " ".join(paraules_transformades)


def interseccio_diccionaris(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Retorna un diccionari amb les claus que apareixen en ambdós diccionaris.
    El valor és el menor dels dos valors.
    Exemple: interseccio_diccionaris({"a": 5, "b": 3, "c": 8}, {"b": 7, "c": 2, "d": 1})
             -> {"b": 3, "c": 2}
    """
    resultat: dict[str, int] = {}
    for clau in d1:
        if clau in d2:
            resultat[clau] = min(d1[clau], d2[clau])
    return resultat


def troba_subcadena_mes_llarga(s1: str, s2: str) -> str:
    """
    Troba la subcadena comuna més llarga entre dos strings.
    Si hi ha múltiples subcadenes de la mateixa longitud, retorna la primera.
    Exemple: troba_subcadena_mes_llarga("abcdef", "xbcde") -> "bcde"
    Exemple: troba_subcadena_mes_llarga("hola", "adeu") -> "a"
    """
    if not s1 or not s2:
        return ""

    longitud_maxima = 0
    subcadena_maxima = ""

    for i in range(len(s1)):
        for j in range(len(s2)):
            longitud = 0
            while (
                i + longitud < len(s1)
                and j + longitud < len(s2)
                and s1[i + longitud] == s2[j + longitud]
            ):
                longitud += 1

            if longitud > longitud_maxima:
                longitud_maxima = longitud
                subcadena_maxima = s1[i : i + longitud]

    return subcadena_maxima


def descodifica_run_length(text: str) -> str:
    """
    Descodifica un string codificat amb run-length encoding.
    Format: "3a2b1c" significa "aaabbc"
    Exemple: descodifica_run_length("3a2b1c") -> "aaabbc"
    Exemple: descodifica_run_length("1h4o2l1a") -> "hhoooola"
    """
    resultat: list[str] = []
    i = 0

    while i < len(text):
        # Llegir el número
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1

        if num_str and i < len(text):
            count = int(num_str)
            char = text[i]
            resultat.append(char * count)
            i += 1

    return "".join(resultat)
