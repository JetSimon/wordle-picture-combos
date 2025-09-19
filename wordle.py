from tqdm import tqdm
import itertools

def get_line(guess, answer, valid_letters, lookup):
    key = (guess, answer)
    if key in lookup:
        return lookup[key]

    line = []
    for i in range(len(guess)):
        letter = guess[i]
        if letter == answer[i]:
            line.append(2)
        elif letter in valid_letters:
            line.append(1)
        else:
            line.append(0)
    
    lookup[key] = line
    return line


def can_make_target_from_answer(answer, target, words, lookup):
    valid_letters = set(list(answer))
    guesses = []
    for target_line in target:
        guesses_before = len(guesses)
        for guess in words:
            resulting_line = get_line(guess, answer, valid_letters, lookup)
            if resulting_line == target_line:
                guesses.append(guess)
                break
        if len(guesses) == guesses_before:
            return False
    return True

def get_answer():
    lookup = {}
    words_file = open("./words.txt")
    words = [line.strip() for line in words_file.readlines()]
    words_file.close()

    total = 2**(25)

    target = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

    with tqdm(total=total) as pbar:
        for seq in itertools.product([0,1], repeat=5*5):
            for i in range(5*5):
                target[i // 5][i % 5] = seq[i]
            
            made_it = False
            for answer in words:
                if can_make_target_from_answer(answer, target, words, lookup):
                    made_it = True
                    break
            if not made_it:
                return False
            pbar.update(1)

    return True

possible = get_answer()

if not possible:
    print("Not possible!")