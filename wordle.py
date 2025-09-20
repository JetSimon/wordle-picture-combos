from tqdm import tqdm
import itertools
import random

def get_line(guess, answer, valid_letters):
    line = []
    for i in range(len(guess)):
        letter = guess[i]
        if letter == answer[i]:
            line.append(2)
        elif letter in valid_letters:
            line.append(1)
        else:
            line.append(0)
    return line


def can_make_target_from_answer(answer, target, words):
    valid_letters = set(list(answer))

    for guess in words:
        resulting_line = get_line(guess, answer, valid_letters)
        if resulting_line == target:
            #print(resulting_line, target)
            return True
    return False
    

def get_answer():

    words_file = open("./words.txt")
    words = [line.strip() for line in words_file.readlines()]
    random.shuffle(words)
    words_file.close()

    possible_with = []

    for answer in tqdm(words):
        made_it = True
        for seq in itertools.product([0,1], repeat=5):
            target = list(seq)
            if not can_make_target_from_answer(answer, target, words):
                #print(answer,"cannot make",target)
                made_it = False
                break

        if made_it:
            possible_with.append(answer)

    return possible_with

possible = get_answer()

words_file = open("./words.txt")
words = [line.strip() for line in words_file.readlines()]
if len(possible) > 0:
    print("Possible with", len(possible),"out of",len(words),"words")
else:
    print("Not possible!")