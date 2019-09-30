import pandas as pd
print('\033[2J')
###############################################################################
###############################################################################
###############################################################################
print(
'''Take the word EASY: Its first three letters — E, A and S — are the fifth, 
first, and nineteenth letters, respectively, in the alphabet. If you add 5, 1, 
and 19, you get 25, which is the value of the alphabetical position of Y, the 
last letter of EASY.

Can you think of a common five-letter word that works in the opposite way — 
in which the value of the alphabetical positions of its last four letters add 
up to the value of the alphabetical position of its first letter?

NPR Sunday Puzzle for 2016-04-03'''
)


def get_sample_words():
    with open('/usr/share/dict/words') as f:
        words = f.read().split('\n')
    return words

def find_npr_puzzle_words(words):
    words5plus = [word for word in words if len(word) == 5]  
    word_chart = pd.DataFrame({'word':words5plus})  
    word_chart['char_beg'] = word_chart.word.apply(lambda x: str(x)[0].lower())
    word_chart['chars_end'] = word_chart.word.apply(lambda x: str(x)[-4:].lower())
    word_chart['val_beg'] = word_chart.char_beg.apply(lambda x: ord(x)-96)
    word_chart['val_end'] = word_chart.chars_end.apply(lambda x: sum([ord(xc)-96 for xc in x]))
    word_chart['val_match'] = word_chart.val_beg == word_chart.val_end
    return word_chart.word[word_chart.val_match]

got_words = find_npr_puzzle_words(get_sample_words())
print(got_words)