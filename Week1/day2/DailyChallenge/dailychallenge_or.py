import re

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# Lecture colonne par colonne
texte = ""
cols = len(matrix[0])

for c in range(cols):
    for r in range(len(matrix)):
        texte += matrix[r][c]

# Remplacement des symboles entre lettres par un espace
message = re.sub(r'(?<=[A-Za-z])[^A-Za-z]+(?=[A-Za-z])', ' ', texte)

# Conserver uniquement lettres et espaces
message = ''.join(ch for ch in message if ch.isalpha() or ch == ' ')

print(message)