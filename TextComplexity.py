import string
from collections import Counter
import pymorphy2


class TextComplexityToAll:

    def __init__(self, example):
        self.example = example

    def how_many_letters(example):
        count = 0
        example = example.lower()
        for l in 'аеиоуюяйцкнгшщзхфвпрлджчсмтб':
            count += example.count(l)
        return count

    def how_many_syllables(example):
        count = 0
        example = example.lower
        for vowel in 'аеиоуюя':
            count += example.count(vowel)
        return count

    def number_of_words(example):
        text_dots = example.replace('?', '.').replace('!', '.').replace('...', '.')
        words = len(text_dots.split())
        n_dots = text_dots.count('.')

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
          length = len(list)

           return length
        return words, long_words(example), f"{round((long_words(example) / words) * 100)}%"

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
        example = example.lower()
        unique_words = {}
        for key in example.split():
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
