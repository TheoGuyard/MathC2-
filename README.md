# MathC2+

* But du sujet : Utiliser les sudokus pour faire une introduction aux quantificateurs logiques et à la programmation. L'objectif est de formaliser les règles du sudoku et de coder un vérificateur de grille et un solver si il y a assez de temps.

## I - Mise en contexte

### 1) Résolution de sudokus

* Faire résoudre des sudokus 9x9
* Faire également résoudre des sudokus 4x4 pour montrer qu'on peut généraliser à tout sudoku de taille NxN
* Faire expliquer les décision prises pour mettre des chiffres dans des cases


### 2) Écriture des règles de sudoku en français
* Règle 'ligne' : Pour toute ligne et pour toute valeur autorisée, on doit avoir une unique case de cette ligne prenant cette valeur.
* Règle 'colonne' : Pour toute colonne et pour toute valeur autorisée, on doit avoir une unique case de cette colonne prenant cette valeur.
* Règle 'bloc' : Pour tout bloc de la grille et pour toute valeur autorisée, on doit avoir une unique case de ce bloc prenant cette valeur.
* Règle 'remplissage' : Chaque case doit prendre une unique valeur.
* Règle 'grille initiale' : Pour toute case initialement fixée à une certaine valeur, on veut que la case correspondante reste fixée à la même valeur.

## II - Formalisation des règles

### 1) Éléments de logique propositionnelle
* Ensemble : un truc qui contient une collection de trucs, on note $I=\{\mathrm{truc}_1,\mathrm{truc}_2,\dots\}$. Les trucs peuvent aussi être des ensembles.
* $\forall$ : "quelque soit"
* $\exists$ : "il existe"
* $\in$ : "dans"
* $\sum_{i \in I} ...$ : "somme sur tous les $i$ dans l'ensemble $I$"
* $\implies$ : "implique"

### 2) Quelques exemples
  * "Il existe un élément de $I$ égal à 1"
    $$\exists \ i \in I, \ i = 1$$
  * "Tous les éléments de $I$ sont égaux à 1"
    $$\forall \ i \in I, \ i = 1$$
  * "Tous les éléments de $I$ sauf un sont égaux à 1"
    $$\exists \ i \in I, \ i \neq 1, \ \forall j \in I, \ j \neq i, \ j=1$$
  * "Somme des éléments de $I$ égale à $1$"
    $$\sum_{i \in I} i = 1$$
  * "Somme des éléments de $P=\{p_1,\dots,p_n\}$ aves les indices dans $I$ égale à $1$"
    $$\sum_{i \in I} p_i = 1$$
  * "Pour chaque élément $J$ de $I$, somme des éléments de $J$ égale à $1$"
   $$\forall J \in I, \ \sum_{j \in J} j = 1$$
  * "Pour chaque élément $J$ de $I$, il existe un élément de $J$ égal à $1$"
    $$\forall J \in I, \ \exists j \in J, \ j = 1$$
  * "Pour chaque élément $i$ de $I$ et pour chaque élément $j$ de $J$, $i > j$"
    $$\forall i \in I, \ \forall j \in J, \ i > j \quad \text{ou} \quad \min_{i \in I} i > \max_{j \in J} j$$
  * "Pour chaque élément $p$ de $P$ (indicé par I) et pour chaque élément $q$ de $Q$ (indicé par I), si $p_i=1$, alors $q_i=1$"
    $$\forall i \in I, \ p_i=1 \implies p_i=1$$

### 3) Notations utiles
* $n$ : taille de la grille
* $b = \sqrt{n}$ : taille d'un bloc 
* $I = \{1,\dots,n\}$ : ensembles des indices de ligne
* $J = \{1,\dots,n\}$ : ensembles des indices de colone
* $K = \{1,\dots,n\}$ : ensembles des valeurs de case possibles
* $B$ : bloc définit comme la collection des indices appartenant au bloc
* $B^*$ : l'ensemble des blocs de la grille
* $X^0$ : la grille initiale
    
### 4) Écriture formelle des règles
* Codage de l'information d'une case : $x_{ijk} = 1 \ \text{si} \ \mathrm{valeur}(i,j)=k \ \text{et} \ 0 \ \text{sinon}, \quad \forall \ i \in I, \ j \in J, \ k \in K$
* Règle 'ligne' : $\forall \ i \in I, \ \forall k \in K, \sum_{j \in J} x_{ijk} = 1$
* Règle 'colonne' : $\forall \ j \in J, \ \forall k \in K, \sum_{i \in I} x_{ijk} = 1$
* Règle 'bloc' : $\forall \ B \in B^{\star}, \ \forall k \in K, \ \sum_{(i,j) \in B} x_{ijk} = 1$
* Règle 'remplissage' : $\forall \ i \in I, \ \forall \ j \in J, \sum_{k \in K} x_{ijk} = 1$
* Règle 'grille initiale' : $\forall \ i \in I, \ \forall j \in J, \ \forall k \in K, \ X^0_{ijk} = 1 \implies X_{ijk} = 1$

## III - Écriture d'un vérificateur de grille

* `verificateur.py`
