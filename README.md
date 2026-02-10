# Instal·lació de `mise`, `python`, `uv`, i VSCode

## Instal·lar Visual Studio Code

Anar a [la web de VSCode](https://code.visualstudio.com) i descarregar-lo i
instal·lar-lo.

## Instal·lar 'mise' (https://mise.jdx.dev/)

```bash
curl https://mise.run | sh      # Executar en un terminal
```

## Instal·lar Python amb mise

```bash
mise use python                 # agafa la última
mise use python@3.13            # per una versió concreta
```

Un cop instal·lat està bé comprovar que tot va bé.

```bash
$ python
Python 3.14.3 (main, Feb  3 2026, 22:52:18) [Clang 21.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Instal·lar UV amb mise

```bash
mise use uv
```

I ho comprovem:

```bash
$ uv
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

Commands:
  auth     Manage authentication
  run      Run a command or script
  init     Create a new project
  ...
```

# Ús de Python a VSCode

## Extensions necessàries

Cal instal·lar 6 extensions de VSCode (totes de Microsoft):

- Python
- Python Debugger
- Mypy Type Checker
- Pylance
- Black Formatter
- Python Environments

## Preparar una carpeta per treballar

Un "Virtual Environment" (`venv`) és una carpeta que té:

1. Una versió de Python concreta (si en tenim és d'una).
2. Una sèrie de llibreries que necessitem pel projecte.

```bash
uv venv    # Crea un Virtual Environment
```

Per activar un Virtual Environment:

```bash
source .venv/bin/activate
```

Això posa un prefix en el "prompt" del shell, entre parèntesis:

```
(ProjecteAP2) $
```

Si esteu a VSCode, amb una carpeta oberta, i la carpeta `.venv` està en el
directori arrel, llavors l'obrir un terminal, es nota que s'activa el `.venv`
perquè surt el prefix esmentat. Això és molt útil perquè haver-ho d'escriure
cada cop és feixuc i al final acabes per no fer-ho.

## Instal·lar paquets a la carpeta

```bash
uv install <nom-del-paquet>
```

Per exemple:

```bash
uv install yogi   # Per llegir l'entrada en els problemes del Jutge
uv install pytest pytest-cov # Per poder fer servir testing
```

# Testing

El testing és una tècnica d'autocomprovació del codi que escrivim. En essència,
fem un programa que executa el codi d'interès i comprova que en certs cassos de
prova, els resultats siguin els esperats.

A Python hi ha dos paquets relacionats amb el testing que són `pytest` i
`pytest-cov`. Aquest últim el que mira és si els tests cobreixen totes les
instruccions del nostre programa, és a dir, hi ha tests que fan passar el
programa per totes les branques possibles.

## Escriure tests

Els tests s'organitzen per fitxers. Pel fitxer `abcde.py`, cal tenir un fitxer
`test_abcde.py`, és a dir, cal posar un prefix `test_` al nom del fitxer que es
vol testar.

Dins del fitxer `test_<nom>.py` posarem funcions també amb el prefix `test_`
(les altres poden ser auxiliars d'aquestes), i cadascuna és un test individual.
A més, normalment el que farem també és importar les funcions del fitxer
original que volem posar a prova.

A dins d'una funció de test, cal cridar a `assert` amb una comprovació:

```python
def test_addition():
    assert 2 + 2 == 4

def test_length():
    assert len([1, 2, 3]) == 3
```

Si qualsevol d'aquestes expressions és `False`, llavors el test serà negatiu i
podrem mirar després què passa.

Si el que volem és comprovar que una funció retorna una excepció, cal posar:

```python
def test_cannot_parse_a_word():
    with pytest.raises(Exception):
        a = int("xyz")  # Trying to convert "xyz" to an int throws ValueError
```

## Testing amb VSCode

A VSCode, hi ha un botó a la barra d'activitats (a l'esquerra, amb botons
grans), que té un símbol de matràs d'Erlenmeyer. Si no surt, es pot clicar amb
el botó dret i buscar "Testing" i activar-lo. El botó surt quan les extensions
indicades anteriorment estan correctament instal·lades.

1. El primer pas és configurar el _testing_ en Python. Donat que hi ha dos
   sistemes, la pregunta que ens farà VSCode és si fem servir _no sé què_ o
   `pytest`. Si has estat atent al text sabràs quina opció escollir 😋.

2. Després apareix una llista dels tests trobats (amb carpetes, fitxers i
   funcions) i es poden executar individualment o en grups.

3. A més, els tests es poden executar també en mode "coverage", que comprova
   quines línies de codi s'han cobert, i ens dóna resultats en %. Quan
   s'executen en mode "coverage" és interessant clicar el fitxer en l'informe de
   "coverage" i mirar quines línies no s'han cobert i pensar tests que ho facin.
