from test import test
from matplotlib.pyplot import *

fileDizionario = open("Dizionario.txt", "r")

vocabolario = set()
for line in fileDizionario:
    line = line.replace('\n', '')
    vocabolario.add(line)

parolePresenti = ["bacio", "come", "esame", "domanda", "veramente", "caratteristico"]
paroleNonPresenti = ["bscho", "cmoe", "seamee", "donamda", "versmenta", "carayyerisyico"]

maxNGrams = 4

timeP, distanceP = (test(vocabolario, parolePresenti, maxNGrams))
timeNP, distanceNP = (test(vocabolario, paroleNonPresenti, maxNGrams))

print("timeP: " + str(timeP))
print("distanceP: " + str(distanceP))
print("timeNP: " + str(timeNP))
print("distanceNP: " + str(distanceNP))

x = [i for i in range(maxNGrams+1)]
yTimeInit = [timeP[i][0] for i in range(maxNGrams+1)]
yTimeP = [timeP[i][1] for i in range(maxNGrams+1)]
yTimeNP = [timeNP[i][1] for i in range(maxNGrams+1)]

print("Tempi di inizializzazione: " + str(yTimeInit))
print("Tempi medi di ricerca di parole presenti nel dizionario: " + str(yTimeP))
print("Tempi medi di ricerca di parole non presenti nel dizionario: " + str(yTimeNP))

figure(1)
bar(x, yTimeInit)
title("Tempi di inizializzazione")
xlabel("n-gram")
ylabel("tempo (s)")
show()

figure(2)
bar(x, yTimeP)
title("Tempi medi di ricerca di parole presenti nel dizionario")
xlabel("n-gram")
ylabel("tempo (s)")
show()

figure(3)
bar(x, yTimeNP)
title("Tempi medi di ricerca di parole non presenti nel dizionario")
xlabel("n-gram")
ylabel("tempo (s)")
show()
