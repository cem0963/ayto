# Are You The One solver using Shannon Entropy


## some explanations  for *ayto_solver_entropy.py*

To start the program, you have to declare some parameters in:


if __name__=='__main__':

    size = 10
    RANDOM_THRESHOLD = 10000
    output = True
    interactive = False
    main(size, interactive)

- *size* = number of pairs (in AYTO size = 10)
- *output* = option to get outputs for each round involving 
    - number of possible solutions left
    - number of possible pairs left
    - chosen guesses for truth booth and matching night
    - number of possibilities removed by each
- *random_threshold* is the threshold for the number of possible solutions left from which on the Shannon Entropy is calculated in order to select the next matching night guess
    - for my setup (Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz   2.11 GHz, 16GB RAM) a good threshold was 10000. At 10000 possibilities left it took approx. 20 minutes to calculate the entropy for each possible guess left
    - if there are more than *random_threshold* possibilities left, the program takes a random guess from the set of still valid guesses for matching night
    - Entropy for Truthbooth guess is **always** calculated
- *interactive mode* offers the possibility to type in the guesses for each round yourself so that you can keep track while watching a season of AYTO
    - for that you need a file *candidates.json* (and of course the correct file path)
    - make sure you type in the names correct, otherwise you get an error


## some explanations  for *ayto_solver_entropy precalc eval matrix.py*
**work in progress**

Idea: calculate evaluation matrix beforehand in order to speed up entropy calculation

### Precalculate evaluation matrix in *generate_evaluation_matrix.py*
Some experiments of calculating evaluation matrix on my system:
size  | #permutations  | time  | storage
------ | ------ | -------- | --------
6  | 720 | 0,45 sek   | 2 mb
7  | 5040 | 21 sek   | 99 mb
8  | 40320 | 26,9 min   | 6,05 gb




# TODO:
1. Evaluate Kreuzmatrix erstellen um Wahrscheinlichkeitsverteilungen (sprich p_k für alle perms in possible_perms) schneller zu berechnen.
Idee: Wenn p_k für perm berechnet werden muss, muss nur noch in die Zeile von perm geschaut werden und die Anzahl der k in der Zeile gezählt.
Damit kriegt man in jeder Zeile eine Wahrscheinlichkeitsverteilung die man einfach an entropy funktion geben kann: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
Achtung: nur die k in der Zeile dürfen gezählt werden, die in einer Spalte von einer perm' sind, welche noch in poss_perms ist. Computational sinnvoll?
-> wenn perms aus possible_perms entfernt werden, auch aus Matrix löschen?
Nur Hälfte der Eintrage berechnen weil symmetrisch.

2. Projekt automatisiert laufen lassen können

    (i) Resultate der einzelnen Läufe in Datei speichern

    (ii) x Läufe gleichzeitig starten können

3. Monte-Carlo-Simulation mit und ohne entropy um vergleichen zu können

*To switch between views, press Ctrl+Shift+V in the editor.*
