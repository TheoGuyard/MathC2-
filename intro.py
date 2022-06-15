# --- Base --- #

# Cette ligne est un commentaire, python ne s'en préoccupera pas !

x = 1               # Affectation à la variable 'x' la valeur 1
x = True            # Affectation à la variable 'x' la valeur True (ou 'Vrai')
x = False           # Affectation à la variable 'x' la valeur False (ou 'Faux')
print(x)            # Affichage de la valeur de la variable 'x'
print("bonjour")    # Affichage du texte 'bonjour'

# --- Opérations --- #
a = 1
b = 2
c = a + b   # Addition
d = a * b   # Multiplication
e = a / b   # Division
f = a // b  # Division euclidienne
g = a % b   # Reste de la division euclidienne


# --- Tableau de valeurs --- #

I = range(3)        # Ensemble {0, 1, 2} 
J = range(1, 5)     # Ensemble {1, 2, 3, 4} 
x = [i for i in I]  # Affectation à la variable 'x' le tableau [0, 1, 2]
l = len(x)          # Taille du tableau x, ici on a l = 3
s = sum(x)          # Somme des éléments du tableau x, ici on a s = 3
print(x, l, s)      # Affichage du tableau x et des valeurs l et s
x = [               # Tableau en 2 dimensions de taille 3x3
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
x12 = x[1][2]       # Affectation à la variable x12 la valeur de la case à 
                    # la ligne numéro 1 et la colonne numéro 2 de x
                    # /!\ En python les indices commencent à 0 /!\
S = sum(x[i][j] for i in range(3) for j in range(3))    # Somme des éléments du tableau x


# --- Boucles --- #

for i in range(3):      # Pour tout i dans {0, 1, 2}
    print(i)            #       Afficher i

x = 0                   # Initialisation de x à 0
for i in range(3):      # Pour tout i dans {0, 1, 2}
    x = x + i           #       Ajouter i à x


# --- Conditions logiques --- #

x = 10                  # Initialisation de x à 10
if x % 2 == 0:          # Si x est divisible par 2, alors
    print("Pair")       #   Afficher 'pair'
else:                   # Sinon
    print("Impair")     #   Afficher 'impair'