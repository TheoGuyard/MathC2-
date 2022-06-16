def verificateur(sudoku):

    # Au début, on suppose que la grille est valide. On changera 'valid = False'
    # à partir du moment où on trouve la première erreur dans la grille. Si on
    # a encore 'valid = True' à la fin, alors la grille sera valide.
    valide = True   

    # Ensembles et variables utiles
    X0 = sudoku.X0      # Grille initiale
    X = sudoku.X        # Grille finale
    n = sudoku.n        # Taille de la grille
    b = sudoku.b        # Taille d'un bloc

    # 1 - Ensembles utiles
    I = range(n)        # Indices des lignes                                    /!\ on commence à 0 en python /!\
    J = range(n)        # Indices des colonnes                                  /!\ on commence à 0 en python /!\
    K = range(n)        # Valeurs possibles                                     /!\ on commence à 0 en python /!\
    IB = range(0, n, b) # Indices de ligne correspondant à un bloc valide       /!\ on commence à 0 en python /!\
    JB = range(0, n, b) # Indices de colonne correspondant à un bloc valide     /!\ on commence à 0 en python /!\

    # 2 - Vérification de la règle 'remplissage'
    for i in I:                                         # pour toute ligne i
        for j in J:                                     # pour toute colonne j
            if sum(X[i][j][k] for k in K) != 1:         # somme_sur_k ( X_ijk ) = 1
                print(f"La règle 'remplissage' n'est pas valide pour la case ({i+1},{j+1})")
                valide = False

    # 3 - Vérification de la règle 'ligne'
    for i in I:                                         # pour toute ligne i
        for k in K:                                     # pour toute valeur k
            if sum(X[i][j][k] for j in J) != 1:         # somme_sur_j ( X_ijk ) = 1
                print(f"La règle 'ligne' n'est pas valide pour la ligne {i+1} et la valeur {k+1}")
                valide = False

    # 4 - Vérification de la règle 'colonne'
    for j in J:                                         # pour toute colonne j
        for k in K:                                     # pour toute valeur k
            if sum(X[i][j][k] for i in I) != 1:         # somme_sur_i ( X_ijk ) = 1
                print(f"La règle 'colonne' n'est pas valide pour la colonne {j+1} et la valeur {k+1}")
                valide = False

    # 5 - Vérification de la règle 'bloc'
    for i in IB:                                    # pour toute ligne i
        for j in JB:                                # pour toute colonne j
            for k in K:                             # pour toute valeur k
                Ib = range(i, i + b)                # coordonnées de ligne du bloc
                Jb = range(j, j + b)                # coordonnées de colonne du bloc
                if sum(X[ib][jb][k] for ib in Ib for jb in Jb) != 1:    # somme_sur_i_dans_Ib_et_j_dans_Jb ( X_ijk ) = 1
                    print(f"La règle 'bloc' n'est pas valide pour le bloc B({i+1},{j+1}) et la valeur {k+1}")
                    valide = False
    
    # 6 - Vérification de la règle 'grille initiale'
    for i in I:                                         # pour toute ligne i
        for j in J:                                     # pour toute colone j
            for k in K:                             # pour toute valeur k
                if X0[i][j][k] == 1:
                    if not X[i][j][k] == 1:
                        print(f"La règle 'grille initiale' n'est pas valide pour la case ({i+1},{j+1})")
                        valide = False

    # 7 - Affichage des résultats
    if valide == True:            
        print("La grille est valide !")


    

    
