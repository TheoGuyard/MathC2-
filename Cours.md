# MathC2+

## Intro

* But du stage : familiariser avec la logique propositionnelle qui nous sert à formaliser les maths via les sudokus

## Sudokus à la main

* 9x9 puis 4x4 pour généralisation à tout $n$ tel que $\sqrt{n}$ est entier
* Essayer de mettre des mots sur les décisions prises


## Écriture des règles en français
* Règle 'ligne' : Pour toute ligne et pour toute valeur autorisée, on doit avoir une unique case de cette ligne prenant cette valeur
* Règle 'colonne' : Pour toute colonne et pour toute valeur autorisée, on doit avoir une unique case de cette colonne prenant cette valeur
* Règle 'bloc' : Pour tout bloc de la grille et pour toute valeur autorisée, on doit avoir une unique case de ce bloc prenant cette valeur
* Règle 'remplissage' : Chaque case doit prendre une unique valeur (Contre exemple : Remplir la grille avec les 9 valeurs dans la diagonale avec multiples valeurs par case)
* Règle 'grille initiale' : Pour toute case initialement fixée à une certaine valeur, on veut que la case correspondante reste fixée à la même valeur

## Éléments de logique propositionnelle
* Ensemble : un objet qui contient une collection de choses, on note $I=\{\mathrm{truc}_1,\mathrm{truc}_2,\dots\}$. On peut aussi avoir des couples $C=\{(a,b), (c,d)\}$...
* $\forall$ : "quelque soit"
* $\exists$ : "il existe"
* $\in$ : "dans"
* $\sum_{i \in I} p_i$ : somme sur tous les $i$ dans l'ensemble $I$
* $\implies$ : "implique

## Quelques exemples
  * "Il existe un élément de $I$ égal à 1"
    $$\exist \ i \in I, \ i = 1$$
  * "Tous les éléments de $I$ sont égaux à 1"
    $$\forall \ i \in I, \ i = 1$$
  * "Tous les éléments de $I$ sauf un sont égaux à 1"
    $$\exist \ i \in I, \ \forall j \in I, \ i \neq 1, \ j \neq i, \ j=1$$
  * "Somme des éléments de $I$ égale à $1$"
    $$\sum_{i \in I} i = 1$$
  * "Somme des éléments de $P=\{p_1,\dots,p_n\}$ aves les indices dans $I$ égale à $1$"
    $$\sum_{i \in I} p_i = 1$$
  * "Pour chaque élément $J$ de $I$, somme des éléments de $J$ égale à $1$"
   $$\forall J \in I, \ \sum_{j \in J} j = 1$$
  * "Pour chaque élément $J$ de $I$, il existe un élément de $J$ égal à $1$"
    $$\forall J \in I, \ \exists j \in J, \ j = 1$$
  * "Pour chaque élément $i$ de $I$ et pour chaque élément $j$ de $J$, $i > j$"
    $$\forall i \in I, \ \forall j \in J, \ i > j$$
  * "Pour chaque élément $i$ de $I$ et pour chaque élément $j$ de $J$, si $i=1$, alors $j=1$"
    $$\forall i \in I, \ \forall j \in J, \ i=1 \implies j=1$$

## Notations utiles
* $n$ : taille de la grille
* $b = \sqrt{n}$ : taille d'un bloc 
* $I = \{1,\dots,n\}$ : ensembles des indices de ligne
* $J = \{1,\dots,n\}$ : ensembles des indices de colone
* $K = \{1,\dots,n\}$ : ensembles des valeurs de case possibles
* $B$ : bloc définit comme la collection des indices appartenant au bloc
* $B^*$ : l'ensemble des blocs de la grille
* $X^0$ : la grille initiale
    
## Écriture formelle des règles
* Codage de l'information d'une case : $x_{ijk} = 
  \begin{cases}
  1 \ \text{si} \ \mathrm{val}(i,j)=k \\
  0 \ \text{sinon}
  \end{cases} \quad \forall \ i \in I, \ j \in J, \ k \in K$
* Règle 'ligne' : $\forall \ i \in I, \ \forall k \in K, \sum_{j \in J} x_{ijk} = 1$
* Règle 'colonne' : $\forall \ j \in J, \ \forall k \in K, \sum_{i \in I} x_{ijk} = 1$
* Règle 'bloc' : $\forall \ B \in B^{\star}, \ \forall k \in K, \ \sum_{(i,j) \in B} x_{ijk} = 1$
* Règle 'remplissage' : $\forall \ i \in I, \ \forall \ j \in J$, $\sum_{k \in K} x_{ijk} = 1$
* Règle 'grille initiale' : $\forall \ i \in I, \ \forall j \in J, \ \forall k \in K, \ X^0_{ijk} = 1 \implies X_{ijk} = 1$

## Écriture d'un vérificateur de grille

* `verificateur.py`

## Écriture d'un solver de grille

* `solver.py`

## Parallèle avec le jeu des 8 dames

* Placer 8 dames sur un échiquier 8x8 sans qu'elles ne se prennent
* Même modèle mais notion de bloc différent et uniquement 2 chiffres possible par case (1 si dame est placée et 0 sinon)

## Parallèle avec la coloration de graphe

La résolution d'un sudoku peut être formalisée par le problème de la coloration de graphe. Le but, dans la version classique du jeu, est d'appliquer $n$ couleurs sur un graphe donné, à partir d'un coloriage partiel (la configuration initiale de la grille). Ce graphe possède $n^2$ sommets, un par cellule. Chacune des cases du sudoku peut être étiquetée avec un couple ordonné (x, y), où x et y sont des entiers compris entre 1 et $n$. Deux sommets distincts étiquetés par (x, y) et (x’, y’) sont reliés par une arête si et seulement si :
  * x = x’ (les deux cellules appartiennent à la même ligne) ou,
  * y = y’ (les deux cellules appartiennent à la même colonne) ou,
  * $\text{ceil}(\frac{x}{\sqrt{n}})=\text{ceil}(\frac{x'}{\sqrt{n}})$ et $\text{ceil}(\frac{y}{\sqrt{n}})=\text{ceil}(\frac{y'}{\sqrt{n}})$, ie, les deux cellules appartiennent à la même région).

La grille se complète en affectant un entier entre 1 et 9 pour chaque sommet, de façon que tous les sommets liés par une arête ne partagent pas le même entier.