from itertools import permutations, product
import random, sys
import time
import math
import json 
from pathlib import Path

def init(size, interactive):
    global all_permutations
    global all_pairs
    all_permutations = list(permutations(range(size)))
    all_pairs = list(product(range(size),repeat=2))
    if interactive:
        f = open(candidates_file) #TODO: praktischer machen
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
    if pair in poss_pairs:
        poss_pairs.remove(pair)
    else:
        print("%s ist schon kein mögliches Pärchen mehr."%str(pair))
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
    if len(possible_permutations) == 1: #if only one option left it doesnt matter which pair we send to truth booth. but if len(possible_permutations) == 1, we get in entropy_for_truth_booth fct p = 1 and then a division by zero
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

def get_guess_candidate(possible_permutations, roundnumber): #returns next guess from set of **still valid** guesses
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
    print("Is the truth booth being sold? (1/0)")
    is_sold = int(input())
    if is_sold == 0:
        woman_tb_number = -1
        while woman_tb_number == -1:
            print("Name of woman in truth booth:")
            woman_tb = str(input())
            for w in range(size):
                if candidates_data['women'][w][str(w)] == woman_tb:
                    woman_tb_number = int(w)
                    break
            if woman_tb_number == -1:
                print("%s is not a candidate." %woman_tb, "Try again.")
        man_tb_number = -1
        while man_tb_number == -1:
            print("Name of man in truth booth:")
            man_tb = str(input())
            for m in range(size):
                if candidates_data['men'][m][str(m)] == man_tb:
                    man_tb_number = int(m)
                    break
            if man_tb_number == -1:
                print("%s is not a candidate." %man_tb, "Try again.")
        cur_truth_booth_guess = (woman_tb_number, man_tb_number)
    else:
        cur_truth_booth_guess = (-1,-1)
    return cur_truth_booth_guess

def interactive_evaluate_truthbooth(cur_truth_booth_guess):
    if cur_truth_booth_guess == (-1,-1):
        evaluation = -1
    else:
        woman_number = cur_truth_booth_guess[0]
        man_number = cur_truth_booth_guess[1]
        woman = candidates_data['women'][woman_number][str(woman_number)]
        man = candidates_data['men'][man_number][str(man_number)]
        print("Are", woman, "and", man, "a match?", "(1/0)")
        evaluation = int(input())
    return evaluation

def interactive_guess():
    cur_guess = ()
    already_paired_men = []
    for i in range(size):
        cur_woman = candidates_data['women'][i][str(i)]
        man_number = -1
        while man_number == -1:
            h = 0
            print("who is %s's match in matching night?" %str(cur_woman))
            cur_man = str(input())
            for j in range(size):
                if candidates_data['men'][j][str(j)] == cur_man:
                    if int(j) in already_paired_men:
                        print("%s is already paired." %cur_man, "Try again.")
                        h -= 1
                        break
                    else:
                        man_number = int(j)
                        cur_guess_list = list(cur_guess)
                        cur_guess_list.append(man_number)
                        already_paired_men.append(man_number)
                        cur_guess = tuple(cur_guess_list)
                        break
            if man_number == -1 and h == 0:
                print("%s is not a candidate." %cur_man, "Try again.")
    return cur_guess


def interactive_evaluate_matchingnight(cur_guess, possible_permutations, roundnumber):
    if cur_guess not in possible_permutations:
        print("%s is not a possible solution." %str(cur_guess))
    print("How many matches in matching night?")
    evaluation = int(input())
    # print("Save Matching night week %d" %roundnumber, "in %s ? (1/0)" %str(save_file) ) #TODO
    # save = int(input())
    # if save == 1:
    #     g = open(save_file, "w")
    #     weekly_data = json.load(g)
    #     weekly_data['matchingnight'][roundnumber][str(roundnumber)] = cur_guess
    #     json.dump(weekly_data, save_file)
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
    #weekly_data = {} #TODO
    prev_truth_booth_guesses = []
    while True:
        roundnumber += 1
        if should_print:
            print('\n Round %d' % roundnumber)
            print('Num of possibilities: %d' % len(possible_permutations))
            print('Num of possible pairs: %d' % len(possible_pairs))
        if interactive:
            # Truth booth
            cur_truth_booth_guess = interactive_truthbooth() 
            prev_truth_booth_guesses.append(cur_truth_booth_guess)
            evaluation = interactive_evaluate_truthbooth(cur_truth_booth_guess)
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
            elif evaluation == 0:
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
        elif evaluation == -1:
            print("Truth booth was sold. No permutations removed.")
        else: 
            possible_pairs = remove_pair(possible_pairs, cur_truth_booth_guess)
            perm_before = len(possible_permutations)
            possible_permutations = remove_permutations(possible_permutations, cur_truth_booth_guess, 0)
            print("Number of permutations removed by Truth Booth: %s" % str(perm_before-len(possible_permutations)))
        #Matching Night
        if interactive:
            cur_guess = interactive_guess() 
        else:
            start = time.time()
            cur_guess = get_guess_candidate(possible_permutations, roundnumber)
        if should_print:
            print('Guess: %s' % str(cur_guess))
            end = time.time()
            if not interactive:
                print("time needed to find guess (in seconds): %s" % str(end-start))
        prev_guesses.append(cur_guess)
        if interactive:
            number_of_matches = interactive_evaluate_matchingnight(cur_guess, possible_permutations, roundnumber) #TODO: roundnumber als Parameter in Funktion nötig?
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
    #only relevant for interactive mode:
    data_folder = Path("data/seasons/AYTO_DE_2021/")
    candidates_file = data_folder / "candidates.json"
    #save_file = data_folder / "weekly_data.json" #TODO
    main(size, interactive)