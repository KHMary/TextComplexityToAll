import string
from collections import Counter
import pymorphy2
import math


def how_many_letters(example):
    count = 0
    for l in 'аеиоуюяйцкнгшщзхфвпрлджчсмтб':
        count += example.count(l)
    return count

def how_many_syllables(example):
    count = 0
    for vowel in 'аеиоуюя':
        count += example.count(vowel)
    return count

def long_words(example):
    example = example.lower()
    text_update = example.split()
    list = []
    for words in text_update:
        b = 0
        for l in words:
            b += 1 if l in 'аоэиуыеёюя' else 0
        if b >= 3:
            list.append(words)
    return len(list)

def number_of_sentences(example):
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    return n_dots

def number_of_words(example):
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    return words

def average_sentence_length(example):
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    if n_dots:
        average_length = words/n_dots
    else:
        return None
    return round(average_length, 2)

def delete_punctuation(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
        example.strip()
    return example

def average_word_length(example):
    words = example.split()
    average = sum(len(word) for word in words) / len(words)
    return round(average, 2)

def frequency(example):
    example = example.lower()
    a = dict(Counter(example.split()))
    return a

def find_unique_words(example):
    unique_words = {}
    for key in example.split():
        unique_words[key] = unique_words.setdefault(key, 0) +1
    return list(filter(lambda x: unique_words[x] == 1, unique_words))

def number_of_unique_words(example):
    unique_words = {}
    for key in example.split():
        unique_words[key] = unique_words.setdefault(key, 0) + 1
    return len(list(filter(lambda x: unique_words[x] == 1, unique_words)))

def frequency_list_match_Sharov(example):
    with open('frequencySharov.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def frequency_list_RNC(example):
    with open('RNC.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def frequency_list_RNC_no_auxiliary(example):
    with open('RNC_no_auxiliary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def frequency_list_match_Sharov_without_auxiliary_parts_of_speech(example):
    with open('FrequencySharov_no_auxiliary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def frequency_list_ShU(example):
    with open('Sharoff_Umanskaya_CoreVocabulary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def frequency_list_ShUnoaux(example):
    with open('Sharoff_Umanskaya_CV_no_auxiliary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read().strip().split(', ')
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1

def lemmatize(example):
    morph = pymorphy2.MorphAnalyzer()
    words = example.split() # разбиваем текст на слова
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res

def ttr(unique_words, words):
    type_token_ratio = unique_words / words

    return round(type_token_ratio, 2)

def maas_ttr(example):
    ntokens = len(example)
    ntypes = len(set(example))

    return round((math.log10(ntokens) - math.log10(ntypes)) / math.pow(math.log10(ntokens), 2), 2)

def mattr(example, window_length=50):
    if len(example) < (window_length + 1):
        ma_ttr = (len(set(example)) / len(example))
    else:
        sum_ttr = 0
        denom = 0
        for x in range(len(example)):
            small_text = example[x:(x + window_length)]
            if len(small_text) < window_length:
                break
            denom += 1
            sum_ttr += (len(set(small_text)) / float(window_length))
            ma_ttr = (sum_ttr / denom)

    return round(ma_ttr, 2)
