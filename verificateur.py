import numpy as np

def verificateur(sudoku, sudoku_0=None):

    valide = True
    
    X = sudoku.X    # Grille du sudoku
    n = sudoku.n    # Taille de la grille
    b = sudoku.b    # Taille d'un carré
    I = range(n)    # Indices des lignes    /!\ on commence à 0 en python /!\
    J = range(n)    # Indices des colonnes  /!\ on commence à 0 en python /!\
    K = range(n)    # Valeurs possibles     /!\ on commence à 0 en python /!\

    # Vérification de la règle 'remplissage'
    for i in I:                                         # pour toute ligne i
        for j in J:                                     # pour toute colone j
            regle = np.sum(X[i, j, k] for k in K) == 1  # somme sur k des x_{ijk} = 1
            if not regle:     
                print(f"La grille ne vérifie pas la règle 'remplissage' pour la case ({i},{j})")
                valide = False

    # Vérification de la règle 'ligne'
    for i in I:                                         # pour toute ligne i
        for k in K:                                     # pour toute value k
            regle = np.sum(X[i, j, k] for j in J) == 1  # somme sur j des X_ijk = 1
            if not regle:     
                print(f"La grille ne vérifie pas la règle 'ligne' pour la valeur {k+1} sur la ligne {i+1}")
                valide = False

    # Vérification de la règle 'colone'
    for j in J:                                         # pour toute clone j
        for k in K:                                     # pour toute value k
            regle = np.sum(X[i, j, k] for i in I) == 1  # somme sur i des X_ijk = 1
            if not regle:     
                print(f"La grille ne vérifie pas la règle 'colone' pour la valeur {k+1} sur la colonne {j+1}")
                valide = False

    # Vérification de la règle 'bloc'
    for i in I:
        for j in J:
            # Point de repère d'un bloc : coin supérieur gauche. Le bloc est 
            # valide si ce point de repère à des coordonnées multiples de b.
            if i % b == 0 and j % b == 0: 
                for k in K:  
                    Ib = range(i, i+b)  # lignes du bloc
                    Jb = range(j, j+b)  # colones du bloc
                    regle = np.sum(sudoku.X[ib, jb, k] for ib in Ib for jb in Jb) == 1
                    if not regle:
                        print(f"La grille ne vérifie pas la règle 'bloc' pour la valeur {k+1} sur le bloc ({i+1},{j+1})")
                        valide = False

    # Vérification de la règle 'grille initiale'
    if sudoku_0:
        X0 = sudoku_0.X
        for i in I:                                             # pour toute ligne i
            for j in J:                                         # pour toute colone j
                if np.sum(X0[i, j, :] == 1):                    # si la case était initialement remplie
                    regle = np.all(X[i, j, :] == X0[i, j, :])   # on veut X_ijk = X0_ijk
                    if not regle:     
                        print(f"La grille ne vérifie pas la règle 'grille initiale' pour la case ({i},{j})")
                        valide = False

    if valide:            
        print("La grille est valide !")