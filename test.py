from timeit import default_timer as timer

import sys

from editdistance import distance
from editdistance import ngrams


def findWord(parola, insieme):
    if parola in insieme:
        return 0, parola
    minDistance = sys.maxsize
    nearWord = None
    for word in insieme:
        d = distance(parola, word)
        if minDistance > d:
            minDistance = d
            nearWord = word
    return minDistance, nearWord


def createDictionary(vocabolario, n):
    dict = {}
    for parola in vocabolario:
        nGrammi = ngrams(parola, n)
        for nGramma in nGrammi:
            if nGramma in dict:
                dict[nGramma].add(parola)
            else:
                dict[nGramma] = {parola}
    return dict


def createSet(parola, dict, n):
    sottoInsieme = set()
    nGrammi = ngrams(parola, n)
    for nGramma in nGrammi:
        if nGramma in dict:
            sottoInsieme = sottoInsieme.union(dict[nGramma])
    return sottoInsieme


def test(vocabolario, parole, maxNGram):

    tempi = []
    distanze = []

    decimalDigits = 4

    # eseguo il test sul vocabolario intero
    allDicTime = 0
    distanze.append([])
    for parola in parole:
        start = timer()
        d, word = findWord(parola, vocabolario)
        end = timer()
        allDicTime += (end-start)
        distanze[0].append(d)
    allDicTime /= len(parole)
    allDicTime = round(allDicTime, decimalDigits)
    tempi.append([0, allDicTime])

    # eseguo il test per ogni sotto-vocabolario ottenuto con gli nGrammi
    for n in range(1, maxNGram+1):
        nGramTime = 0
        distanze.append([])

        #inizializzo e misuro il tempo
        start = timer()
        dict = createDictionary(vocabolario, n)
        end = timer()
        initTime = round((end-start), decimalDigits)

        for parola in parole:
            # cerco la parola e misuro tempo e distanza
            start = timer()
            miniVocabolario = createSet(parola, dict, n)
            d, word = findWord(parola, miniVocabolario)
            end = timer()
            nGramTime += (end-start)
            distanze[-1].append(d)
        nGramTime /= len(parole)
        nGramTime = round(nGramTime, decimalDigits)
        tempi.append([initTime, nGramTime])

    return tempi, distanze
