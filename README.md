# Are You The One solver using Shannon Entropy


## some explanations  for *ayto_solver_entropy.py*

The idea is to choose each guess (truth booth or matching night) as the one with the highest entropy of all guesses which are still valid at this point. This means non-valid guesses are excluded even though they might have a higher entropy, i.e. more information.

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
    - the deposited solution is irrelevant in the interactive mode because no query with the solution is happening


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
1. Evaluate Kreuzmatrix erstellen um Wahrscheinlichkeitsverteilungen (sprich p_k f??r alle perms in possible_perms) schneller zu berechnen.
Idee: Wenn p_k f??r perm berechnet werden muss, muss nur noch in die Zeile von perm geschaut werden und die Anzahl der k in der Zeile gez??hlt.
Damit kriegt man in jeder Zeile eine Wahrscheinlichkeitsverteilung die man einfach an entropy funktion geben kann: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
Achtung: nur die k in der Zeile d??rfen gez??hlt werden, die in einer Spalte von einer perm' sind, welche noch in poss_perms ist. Computational sinnvoll?
-> wenn perms aus possible_perms entfernt werden, auch aus Matrix l??schen?
Nur H??lfte der Eintrage berechnen weil symmetrisch.

2. unterschiedliche Strategien f??r Entropy, nicht nur  den Kandidaten mit h??chster expected Info. zB weitere Strategie: m??glichst wenig guesses, d.h. ab bestimmtem Punkt den wahrscheinlichsten Guess nehmen statt den mit h??chster expected info

2. im interactive mode die option geben in jeder runde den wahrscheinlichsten Tipp auszugeben

2. Projekt automatisiert laufen lassen k??nnen

    (i) Resultate der einzelnen L??ufe in Datei speichern

    (ii) x L??ufe gleichzeitig starten k??nnen

3. Monte-Carlo-Simulation mit und ohne entropy um vergleichen zu k??nnen

4. Im interactive mode die M??glichkeit geben bisherige Runden zu speichern, damit man nicht immer alles von der ersten Runde eingeben muss

5. M??glichkeit die solution selbst einzugeben

6. Speichern der Wochenst??nde im interactive mode

8. error catching bei Eingaben



*To switch between views, press Ctrl+Shift+V in the editor.*
