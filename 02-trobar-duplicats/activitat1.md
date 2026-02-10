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

**Per què aquesta funció és bona per l'exercici:**

1. **Cost O(n²)** - Té dos loops niats i usa `in` sobre una llista
2. **Comportament clar** - Fàcil d'entendre què fa i escriure tests
3. **Progressió natural** - Permet tres solucions:
   - **O(n²)**: La versió actual (legacy)
   - **O(n log n)**: Ordenar primer i després buscar consecutius iguals
   - **O(n)**: Usar un diccionari/set per comptar aparicions

**Tests que haurien d'escriure:**

- Llista buida
- Sense duplicats
- Tots duplicats
- Duplicats múltiples del mateix element
- Ordre dels duplicats retornats
- Llistes grans per mesurar performance

## Solució O(n log n)

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
    if not numbers:
        return []

    # Crear una llista de parells (valor, índex_original) per mantenir l'ordre
    indexed_numbers = [(num, idx) for idx, num in enumerate(numbers)]

    # Ordenar per valor (O(n log n))
    indexed_numbers.sort(key=lambda x: x[0])

    # Trobar duplicats comparant elements consecutius (O(n))
    duplicates_with_first_index = {}
    for i in range(len(indexed_numbers) - 1):
        current_val, current_idx = indexed_numbers[i]
        next_val, next_idx = indexed_numbers[i + 1]

        if current_val == next_val:
            if current_val not in duplicates_with_first_index:
                # Guardar el mínim índex on apareix per primera vegada
                duplicates_with_first_index[current_val] = min(current_idx, next_idx)

    # Ordenar els duplicats per l'ordre original d'aparició (O(k log k) on k <= n)
    result = sorted(duplicates_with_first_index.keys(),
                   key=lambda x: duplicates_with_first_index[x])

    return result
```

**Complexitat:**

- Ordenació: O(n log n)
- Recorregut per trobar consecutius: O(n)
- Ordenació final dels duplicats: O(k log k) on k ≤ n
- **Total: O(n log n)**

## Solució O(n)

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
    seen = {}  # Diccionari per comptar aparicions
    duplicates = []  # Llista per mantenir l'ordre d'aparició

    for num in numbers:
        if num in seen:
            # Si ja l'hem vist i encara no està a duplicates, l'afegim
            if seen[num] == 1:
                duplicates.append(num)
            seen[num] += 1
        else:
            seen[num] = 1

    return duplicates
```

**Complexitat:**

- Un sol recorregut de la llista: O(n)
- Operacions de diccionari (in, accés, increment): O(1) en promig
- **Total: O(n)**

**Clau de l'optimització:**

- Usem un diccionari per comptar aparicions en temps constant
- Afegim a `duplicates` només la primera vegada que detectem que un element és duplicat (quan `seen[num] == 1`)
- Això manté l'ordre d'aparició sense necessitat d'ordenacions addicionals

Aquesta és la solució òptima i passa exactament els mateixos tests que les versions anteriors!
