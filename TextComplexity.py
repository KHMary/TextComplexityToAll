import string
from collections import Counter
import pymorphy2
import math


def lower(self):
    return self.lower()


def count(self):
    return self.count()


def how_many_letters(example):
    c = 0
    example1 = example.lower()
    for l in 'аеиоуюяйцкнгшщзхфвпрлджчсмтб':
        c += example1.count(l)
    return c


def how_many_syllables(example):
    c = 0
    example1 = example.lower
    for vowel in 'аеиоуюя':
        c += example1.count(vowel)
    return c


def number_of_words(example):
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    return words


def long_words(example):
    example1 = example.lower()
    text_update = example1.split()
    list = []
    for words in text_update:
        b = 0
        for l in words:
            b += 1 if l in 'аоэиуыеёюя' else 0
            if b >= 3:
                list.append(words)
        length = len(list)
        return length


def number_of_sentences(example):  
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    return n_dots


def average_sentence_length(example):   
    text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
    words = len(text_dots.split())
    n_dots = text_dots.count('.')
    average_length = words / n_dots
    return round(average_length, 2)


def average_word_length(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
        example.strip()

    def avg():
        words = example.split()
        return round(sum(len(word) for word in words) / len(words), 2)
    return avg()


def frequency(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
    example.strip()
    example = example.lower()
    a = dict(Counter(example.split()))
    return a


def find_unique_words(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
    example.strip()
    example1 = example.lower()
    unique_words = {}
    for key in example1.split():
        unique_words[key] = unique_words.setdefault(key, 0) + 1
    return list(filter(lambda x: unique_words[x] == 1, unique_words))


def lemmatize(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
    example.strip()
    morph = pymorphy2.MorphAnalyzer()
    words = example.split()
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)

    return res


def number_of_unique_words(example):
    for p in example:
        if p in string.punctuation:
            example = example.replace(p, '')
        example.strip()
        unique_words = {}
        for key in example.split():
            unique_words[key] = unique_words.setdefault(key, 0) + 1
        return len(list(filter(lambda x: unique_words[x] == 1, unique_words)))


def frequency_list_match_sharov(example):
    with open('frequencySharov.txt', mode='r', encoding='UTF-8') as l:
        list = l.read()
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1


def frequency_list_match_sharov_without_auxiliary_parts_of_speech(example):
    with open('FrequencySharov_no_auxiliary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read()
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1


def frequency_list_match_russian_national_corpus(example):
    with open('RNC.txt', mode='r', encoding='UTF-8') as l:
        list = l.read()
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)
    return length_words, words_1


def frequency_list_match_russian_national_corpus_no_auxiliary(example):
    with open('RNC_no_auxiliary.txt', mode='r', encoding='UTF-8') as l:
        list = l.read()
        freq = set(example.split())
        words_1 = [f'{word} == {example.count(word)}' for word in freq if word in list]
        length_words = len(words_1)

    return length_words, words_1


def ttr(unique_words, words):
    type_token_ratio = unique_words / words

    return round(type_token_ratio, 2)


def maas_ttr(example):
    ntokens = len(example)
    ntypes = len(set(example))

    return (math.log10(ntokens) - math.log10(ntypes)) / math.pow(math.log10(ntokens), 2)


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

    return mattr

