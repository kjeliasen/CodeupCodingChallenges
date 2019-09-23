
"""
    September 20, 2019
    Daily Code Workout

    We are at the grand canyon. Everyone shouts random things into the canyon to hear their echos.
    Make a function that will echo your phrase a random number of times. (max number of echos is 8)
    Have some fun with this one. Google grinch echo scene.

"""

import random


def shout_into_canyon(shouted_phrase):
    reverbs = random.randint(4,8)
    shouted_phrase = 'NO!' if shouted_phrase.lower() == 'is anybody out there?' else shouted_phrase
    lesser_phrase = ''.join([f'{char} ' for char in shouted_phrase])
    for reverb in range(reverbs):
        if reverb < reverbs / 4:
            print(f'!!{shouted_phrase.upper()}!!')
        elif reverb < 2 * reverbs / 4:
            print(f'{shouted_phrase.lower().capitalize()}!')
        elif reverb < 3 * reverbs / 4:
            print(f'{shouted_phrase.lower()}')
        else:
            print(lesser_phrase)

on_try = 1
echoing = True
no_phrases = ['is anybody out there?', 'can you hear me?', 'is anyone out there?']
print('We are at the grand canyon. Everyone shouts random things into the canyon to hear their echos.')
while echoing == True:
    use_else = '' if on_try == 1 else ' Else'
    on_try += 1
    shouted_phrase = input(f'Shout Something{use_else}: ')
    if len(shouted_phrase) == 0:
        echoing = False
    else:
        shout_into_canyon(shouted_phrase)