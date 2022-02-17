from itertools import permutations, product
import random, sys
import time
import math

def init(size):
    global all_permutations
    global all_pairs
    all_permutations = list(permutations(range(size)))
    all_pairs = list(product(range(size),repeat=2))

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
    #TODO: unterschiedliche returns bei if Abfrage ein Problem?

def one_season(solution, should_print):
    if should_print:
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

        # Truth booth
        cur_truth_booth_guess = get_truth_booth_candidate(possible_permutations, possible_pairs, roundnumber) #TODO
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
            print("Number of permutations removed by Truth Booth: %s" % str(perm_before-len(possible_permutations))) # TODO: wenn match in truthbooth gefunden wird braucht das programm hier ewig, im anderen fall auch manchmal. Wieso? #wir behalten nur die permutationen bei denen perm(pairtuple[0])= pairtuple[1]
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
        seconds1 = time.time()
        cur_guess = get_guess_candidate(possible_permutations, roundnumber)
        if should_print:
            print('Guess: %s' % str(cur_guess))
            seconds2 = time.time()
            print("time needed to find guess (in seconds): %s" % str(seconds2-seconds1))
        prev_guesses.append(cur_guess)
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

def main(size):
    init(size)
    solution = all_permutations[random.randint(0,len(all_permutations)-1)]
    one_season(solution, True)

if __name__=='__main__':
    size = 10
    RANDOM_THRESHOLD = 150000
    main(size)



#TODO:
"""
1. Evaluate Kreuzmatrix erstellen um Wahrscheinlichkeitsverteilungen (sprich p_k für alle perms in possible_perms) schneller zu berechnen.
Idee: Matrix (10! x 10! groß) vorher berechnen. Wenn p_k für perm berechnet werden muss, muss nur noch in die Zeile von perm geschaut werden und die Anzahl der k in der Zeile gezählt.
Achtung: nur die k in der Zeile dürfen gezählt werden, die in einer Spalte von einer perm' sind, welche noch in poss_perms ist. Computational sinnvoll?
-> wenn perms aus possible_perms entfernt werden, auch aus Matrix löschen?
Nur Hälfte der Eintrage berechnen weil symmetrisch.

2. Projekt zu Github hochladen inkl. readme.md

3. Projekt automatisiert laufen lassen können
    (i) Resultate der einzelnen Läufe in Datei speichern
    (ii) x Läufe gleichzeitig starten können
"""