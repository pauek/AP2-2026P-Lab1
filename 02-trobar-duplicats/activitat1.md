# Activitat 1

## Solució inicial O(n²)

```python
def find_duplicates(numbers):
    """
    Retorna una llista amb els elements que apareixen més d'una vegada.
    Els duplicats es retornen en l'ordre en què apareixen per primera vegada.

    Exemples:
    >>> find_duplicates([1, 2, 3, 2, 4, 1])
    [1, 2]
    >>> find_duplicates([5, 5, 5, 1, 2])
    [5]
    >>> find_duplicates([1, 2, 3])
    []
    """
    duplicates = []
    for i in range(len(numbers)):
        # Comprovar si l'element actual ja l'hem vist abans
        count = 0
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1

        # Si apareix més d'una vegada i no l'hem afegit ja
        if count > 1 and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

    return duplicates
```

La funció `find_duplicates` actual:
1. **Cost O(n²)** - Té dos loops niats i usa `in` sobre una llista
2. **Comportament clar** - Fàcil d'entendre què fa i escriure tests

Passos per millorar-la:
1. **O(n²)**: La versió actual (legacy)
2. **O(n log n)**: Ordenar primer i després buscar consecutius iguals
3. **O(n)**: Usar un diccionari/set per comptar aparicions

Però abans de començar escriurem el tests, per exemple:
- Llista buida
- Sense duplicats
- Tots duplicats
- Duplicats múltiples del mateix element
- Ordre dels duplicats retornats
- Llistes grans per mesurar performance

Un cop escrits, podem "optimitzar" la funció saben que no estem perdent la correctesa!
