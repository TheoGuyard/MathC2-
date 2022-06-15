import numpy as np
from math import sqrt
from pyomo.environ import *

CPLEX_PATH = "/Applications/CPLEX_Studio201/cplex/bin/x86-64_osx/cplex"

def solveur(sudoku):

    n = sudoku.n
    b = int(sqrt(n))
    X = sudoku.X
    
    # Instanciation du modèle
    model = ConcreteModel()

    # Ensembles
    I = list(range(1, n+1))
    J = list(range(1, n+1))
    K = list(range(1, n+1))

    # Variables
    model.x = Var(I, J, K, within=Binary)

    # Règle 'remplissage'
    model.remplissage = ConstraintList()
    for i in I:
        for j in J:
            model.remplissage.add(sum(model.x[i, j, k] for k in K) == 1)

    # Règle 'ligne'
    model.ligne = ConstraintList()
    for i in I:
        for k in K:
            model.ligne.add(sum(model.x[i, j, k] for j in J) == 1)
        
    # Règle 'colonne'
    model.colonne = ConstraintList()
    for j in J:
        for k in K:
            model.colonne.add(sum(model.x[i, j, k] for i in I) == 1)
        
    # Règle 'bloc'
    model.bloc = ConstraintList()
    for i in I:
        for j in J:
            if (i - 1) % b == (j - 1) % b == 0:
                Ib = range(i, i + b)
                Jb = range(j, j + b)
                for k in K:
                    model.bloc.add(sum(model.x[ib, jb, k] for ib in Ib for jb in Jb) == 1)
        
    # Règle 'grille initiale'
    model.grille_initiale = ConstraintList()
    for i in I:
        for j in J:
            if sum(X[i-1][j-1][k-1] for k in K) == 1:
                k_initial = [k for k in K if X[i-1][j-1][k-1] == 1][0]
                model.grille_initiale.add(model.x[i,j,k_initial] == 1)
        
    # Objectif
    model.Obj = Objective(expr = summation(model.x), sense=minimize)

    # Résolution 
    opt = SolverFactory('cplex', executable=CPLEX_PATH)
    res = opt.solve(model)

    # Récupération des valeurs
    for i in I:
        for j in J:
            for k in K:
                X[i-1][j-1][k-1] = model.x[i,j,k]()

    return res.solver.termination_condition == TerminationCondition.optimal