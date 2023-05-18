from django.shortcuts import render
import pymorphy2
from collections import Counter
from .utils import *
import string
from collections import Counter



def index(request):
    # form = PostForm(request.POST or None, files=request.FILES or None,)
    context = {}
    if request.method == 'POST':
        text = request.POST['text']
        context = {"text": text}
        words = text.split()
        context['words'] = words
        morph = pymorphy2.MorphAnalyzer()
        tags = tuple(morph.parse(word)[0].tag for word in words) #Кортеж извлеченных тэгов OpenCorpora

        numbsentences = number_of_sentences(text)
        context['numbsentences'] = numbsentences
        print(numbsentences)

        avgsentences = average_sentence_length(text)
        context['avgsentences'] = avgsentences

        text = delete_punctuation(text)

        words = text.split()
        tags = tuple(morph.parse(word)[0].tag for word in words)

        pos = tuple(tag.POS if tag.POS else '' for tag in tags) #Кортеж значений части речи
        context['pos'] = pos

        animacy = tuple(tag.animacy if tag.animacy else '' for tag in tags)
        context['animacy'] = animacy

        aspect = tuple(tag.aspect if tag.aspect else '' for tag in tags) #Кортеж значений вида
        context['aspect'] = aspect

        tense = tuple(tag.tense if tag.tense else '' for tag in tags)
        context['tense'] = tense

        case = tuple(tag.case if tag.case else '' for tag in tags) # Кортеж значений падежа
        context['case'] = case

        gender = tuple(tag.gender if tag.gender else '' for tag in tags) #Кортеж значений пола
        context['gender'] = gender

        mood = tuple(tag.mood if tag.mood else '' for tag in tags) #Кортеж значений наклонения
        context['mood'] = mood

        number = tuple(tag.number if tag.number else '' for tag in tags) #Кортеж значений числа
        context['number'] = number

        person = tuple(tag.person if tag.person else '' for tag in tags) #Кортеж значений лица
        context['person'] = person

        transitivity = tuple(tag.transitivity if tag.transitivity else '' for tag in tags) #Кортеж значений переходности
        context['transitivity'] = transitivity

        voice = tuple(tag.voice if tag.voice else '' for tag in tags) #Кортеж значений залога
        context['voice'] = voice

        letters = how_many_letters(text)
        context['letters'] = letters

        syllables = how_many_syllables(text)
        context['syllables'] = syllables

        lwords = long_words(text)
        context['lwords'] = lwords

        numbwords = number_of_words(text)
        context['numbwords'] = numbwords

        avgword = average_word_length(text)
        context['avgword'] = avgword

        wfrequency = frequency(text)
        context['wfrequency'] = wfrequency

        finduniquewords = find_unique_words(text)
        context['finduniquewords'] = finduniquewords

        numberuniquewords = number_of_unique_words(text)
        context['numberuniquewords'] = numberuniquewords

        freqlistSharov = frequency_list_match_Sharov(text)
        context['freqlistSharov'] = freqlistSharov

        freqlistRNC = frequency_list_RNC(text)
        context['freqlistRNC'] = freqlistRNC

        freqlistRNCnoaux = frequency_list_RNC_no_auxiliary(text)
        context['freqlistRNCnoaux'] = freqlistRNCnoaux

        freqlistnoauxSharov = frequency_list_match_Sharov_without_auxiliary_parts_of_speech(text)
        context['freqlistnoauxSharov'] = freqlistnoauxSharov

        freqlistShU = frequency_list_ShU(text)
        context['freqlistShU'] = freqlistShU

        freqlistShUnoaux = frequency_list_ShUnoaux(text)
        context['freqlistShUnoaux'] = freqlistShUnoaux

        lemma = lemmatize(text)
        context['lemma'] = lemma

        ttr1 = ttr(numberuniquewords, numbwords)
        context['ttr1'] = ttr1

        maas_ttr1 = maas_ttr(text)
        context['maas_ttr1'] = maas_ttr1

        mattr1 = mattr(text)
        context['mattr1'] = mattr1















    return render(request, 'index.html', context)

