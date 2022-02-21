from itertools import permutations, product
import random, sys
import time
import math
import json 

def init(size, interactive):
    global all_permutations
    global all_pairs
    all_permutations = list(permutations(range(size)))
    all_pairs = list(product(range(size),repeat=2))
    if interactive:
        f = open('seasons/AYTO_DE_2021/candidates.json')
        global candidates_data
        candidates_data = json.load(f)
        print(candidates_data)
        for gender in candidates_data:
            for i in range(size):
                print("%s: " %str(i), candidates_data[gender][i][str(i)])

def evaluate(solution,guess):
    if len(guess) == len(solution):
        count = 0
        for x in range(len(solution)):
            if solution[x] == guess[x]:
                count += 1
        return count
    else: #Abfrage benötigt wenn wir nur das Ergebnis der truth booth haben und alle perms finden wollen, in denen dieses tupel (nicht) drin ist
         return 1 if solution[guess[0]] == guess[1] else 0

def remove_permutations(permutations, guess, number_matches):
    return [perm for perm in permutations if evaluate(perm, guess) == number_matches]

def remove_pair(possible_pairs, pair):
    poss_pairs = possible_pairs
    poss_pairs.remove(pair)
    return poss_pairs

def entropy_for_guess(guess, possible_permutations): #dauert viel zu lang.. für #poss_perms = 12800 dauerts ca 20 Minuten
    """
    calculates Shannon Entropy H for a specific guess as H = = -sum(p_k * log(p_k)
    where p_k is the probability that the guess has exactly k matches right:
    p_k = (number of still possible permutations that share exactly k elements with the guess) / (number of still possible permutations)
    
    """
    size = len(guess)
    H = 0 
    for k in range(size+1): #zero matches to 10 matches
        p_k = len([perm for perm in possible_permutations if evaluate(guess, perm) == k]) / len(possible_permutations)
        if p_k > 0: #TODO ist p_k = 0 möglich oder error?
            H += p_k * math.log((1 / p_k), 2)
    return H 

def entropy_for_truth_booth(possible_permutations, pair):
    "calculate Shannon Entropy H"
    size = len(possible_permutations[0])
    H = 0
    p = len([perm for perm in possible_permutations if perm[pair[0]] == pair[1]]) / len(possible_permutations)
    if p == 1:
        H += p * math.log((1 / p), 2) + (1-p)
        return H 
    elif p > 0: #TODO s.o.
        H += p * math.log((1 / p), 2) + (1-p) * math.log((1 / (1-p)), 2)
    return H

def get_truth_booth_candidate(possible_permutations, possible_pairs, roundnumber):
    if len(possible_permutations) == 1: #if only one option left id doesnt matter which pair we send to truth booth. but if len(possible_permutations) == 1, we get in entropy_for_truth_booth fct p = 1 and then a division by zero
        next_pair = possible_pairs[random.randint(0, len(possible_pairs)-1)]
        return next_pair
    if roundnumber == 1:
        return possible_pairs[random.randint(0, len(possible_pairs)-1)]
    else:
        next_pair = ()
        best_entropy = 0
        for pair in possible_pairs:
            if entropy_for_truth_booth(possible_permutations, pair) > best_entropy:
                next_pair = pair
                best_entropy = entropy_for_truth_booth(possible_permutations, pair)
        return next_pair

def get_guess_candidate(possible_permutations, roundnumber): #returns next guess
    size = len(possible_permutations[0])
    if roundnumber == 1:
        return possible_permutations[random.randint(0, len(possible_permutations)-1)]
    if len(possible_permutations) == 1: #nur noch eine Option über
        return possible_permutations[0]
    if len(possible_permutations) > RANDOM_THRESHOLD: #if computation takes too long
        return possible_permutations[random.randint(0, len(possible_permutations)-1)]
    else:
        next_guess = ()
        best_entropy = 0
        for guess_candidate in possible_permutations:
            if entropy_for_guess(guess_candidate, possible_permutations) > best_entropy:
                next_guess = guess_candidate
                best_entropy = entropy_for_guess(guess_candidate, possible_permutations)
        return next_guess

## Funktionen für interaktiven Modus

def GetKey(val): #TODO
   for key, value in candidates_data.items():
      if val == value:
         return key
      return "key doesn't exist"

def interactive_truthbooth():
    #input of truth booth pair
    print("Name of woman in truth booth:")
    woman_tb = str(input())
    for w in range(size):
        if candidates_data['women'][w][str(w)] == woman_tb:
            woman_tb_number = int(w)
            break
    print("Name of man in truth booth:")
    man_tb = str(input())
    for i in range(size):
        if candidates_data['men'][i][str(i)] == man_tb:
            man_tb_number = int(i)
            break
    cur_truth_booth_guess = (woman_tb_number, man_tb_number)
    return cur_truth_booth_guess

def interactive_evaluate_truthbooth(cur_truth_booth_guess):
    woman_number = cur_truth_booth_guess[0]
    man_number = cur_truth_booth_guess[1]
    woman = candidates_data['women'][str(woman_number)]
    man = candidates_data['men'][man_number]
    print("Are %s a match?" %str(woman, man), "(1/0)")
    evaluation = int(input())
    return evaluation

def interactive_guess():
    cur_guess = ()
    for i in candidates_data['women']:
        cur_woman = candidates_data['women'][i]
        print("who is %s match in matching night?" %str(cur_woman))
        cur_man = str(input())
        for j in candidates_data['men']:
            if candidates_data['men'][j] == cur_man:
                man_number = int(j)
                cur_guess_list = list(cur_guess)
                cur_guess_list.append(man_number)
                cur_guess = tuple(cur_guess_list)
                break
    return cur_guess


def interactive_evaluate_matchingnight(cur_guess):
    print("How many matches in matching night?")
    evaluation = int(input())
    return evaluation


def one_season(solution, should_print, interactive):
    if should_print and not interactive:
        print("solution: ", solution)
    size = len(solution)
    cur_guess = None
    cur_truth_booth_guess = None
    possible_permutations = all_permutations
    possible_pairs = all_pairs
    roundnumber = 0
    prev_guesses = []
    prev_truth_booth_guesses = []
    while True:
        roundnumber += 1
        if should_print:
            print('\n Round %d' % roundnumber)
            print('Num of possibilities: %d' % len(possible_permutations))
            print('Num of possible pairs: %d' % len(possible_pairs))
        if interactive:
            # Truth booth
            cur_truth_booth_guess = interactive_truthbooth() #TODO: Eingabe Truth Booth Pärchen
            prev_truth_booth_guesses.append(cur_truth_booth_guess)
            evaluation = interactive_evaluate_truthbooth(cur_truth_booth_guess) #TODO: sagen ob wahr oder falsch
        else:
            # Truth booth
            cur_truth_booth_guess = get_truth_booth_candidate(possible_permutations, possible_pairs, roundnumber) 
            prev_truth_booth_guesses.append(cur_truth_booth_guess)
            if should_print:
                print('Guess for truth booth: %s' % str(cur_truth_booth_guess))
            evaluation = evaluate(solution, cur_truth_booth_guess)
        if should_print:
            print('Evaluation of Truth Booth:')
            if evaluation == 1: 
                print("Truth Booth found a match")
            else:
                print("Truth Booth did not find a match")
        if evaluation == 1:
            perm_before = len(possible_permutations)
            possible_permutations = remove_permutations(possible_permutations, cur_truth_booth_guess, 1)
            print("Number of permutations removed by Truth Booth: %s" % str(perm_before-len(possible_permutations))) 
            for k in range(size):
                if k != cur_truth_booth_guess[1] and (cur_truth_booth_guess[0], k) in possible_pairs:
                    possible_pairs = remove_pair(possible_pairs, (cur_truth_booth_guess[0], k))
                if k != cur_truth_booth_guess[0] and (k, cur_truth_booth_guess[1]) in possible_pairs:
                    possible_pairs = remove_pair(possible_pairs, (k, cur_truth_booth_guess[1]))
        else: 
            possible_pairs = remove_pair(possible_pairs, cur_truth_booth_guess)
            perm_before = len(possible_permutations)
            possible_permutations = remove_permutations(possible_permutations, cur_truth_booth_guess, 0)
            print("Number of permutations removed by Truth Booth: %s" % str(perm_before-len(possible_permutations)))
        #Matching Night
        start = time.time()
        if interactive:
            cur_guess = interactive_guess() #TODO: Matching night Eingabe guess
        else:
            cur_guess = get_guess_candidate(possible_permutations, roundnumber)
        if should_print:
            print('Guess: %s' % str(cur_guess))
            end = time.time()
            if not interactive:
                print("time needed to find guess (in seconds): %s" % str(end-start))
        prev_guesses.append(cur_guess)
        if interactive:
            number_of_matches = interactive_evaluate_matchingnight() #TODO Matching night Eingabe #matchings
        else:
            number_of_matches = evaluate(solution, cur_guess)
        if should_print:
            print('Guess had %s matches' % str(number_of_matches))
        if number_of_matches == 0: #Blackout Sonderfall
            for k in range(len(cur_guess)):
                possible_pairs.remove((k,cur_guess[k]))
        if number_of_matches == size:
            if should_print:
                print('Found %s in %d guesses' % (str(cur_guess), roundnumber))
            else:
                return roundnumber
            break #einziges Abbruchkriterium wenn Lösung gefunden wurde
        perm_before = len(possible_permutations)
        possible_permutations = remove_permutations(possible_permutations, cur_guess, number_of_matches)
        print("Number of permutations removed by Matching Night: %s" % str(perm_before-len(possible_permutations)))

def main(size, interactive):
    init(size, interactive)
    solution = all_permutations[random.randint(0,len(all_permutations)-1)]
    one_season(solution, output, interactive)

if __name__=='__main__':
    size = 10
    RANDOM_THRESHOLD = 150000
    output = True
    interactive = True
    main(size, interactive)




#TODO:
"""
1. Evaluate Kreuzmatrix erstellen um Wahrscheinlichkeitsverteilungen (sprich p_k für alle perms in possible_perms) schneller zu berechnen.
Idee: Matrix (10! x 10! groß) vorher berechnen. Wenn p_k für perm berechnet werden muss, muss nur noch in die Zeile von perm geschaut werden und die Anzahl der k in der Zeile gezählt.
Damit kriegt man in jeder Zeile eine Wahrscheinlichkeitsverteilung die man einfach an entropy funktion geben kann: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
Achtung: nur die k in der Zeile dürfen gezählt werden, die in einer Spalte von einer perm' sind, welche noch in poss_perms ist. Computational sinnvoll?
-> wenn perms aus possible_perms entfernt werden, auch aus Matrix löschen?
Nur Hälfte der Eintrage berechnen weil symmetrisch.

2. Projekt zu Github hochladen inkl. readme.md

3. Projekt automatisiert laufen lassen können
    (i) Resultate der einzelnen Läufe in Datei speichern
    (ii) x Läufe gleichzeitig starten können
"""