# Ricerca su sottoinsiemi individuati da N-grammi

Si vuole analizzare l'utilità dell'utilizzo di N-grammi nella ricerca di parole in un lessico vicine ad una query (in termini di EditDistance). In particolare, si usano gli N-grammi per ridurre lo spazio di ricerca e di conseguenza cercare di ridurre il tempo impiegato.

## Esperimento 
Si usano dei dizionari per associare ad ogni N-gram, la lista di parole che lo contegono. Data una query, si cerca la parola più vicina ad essa nel sottoinsieme dato dall'unione delle parole associate agli N-grammi della query.

Si confronta la ricerca esaustiva con le ricerche basate su bigrammi, trigrammi e 4-grammi. 
Si creano 3 grafici, nei quali si riporta:

+ tempo di inizializzazione del metodo di ricerca
+ tempo medio di ricerca di parole presenti nel lessico
+ tempo medio di ricerca di parole non presenti nel lessico

Per eseguire l'esperimento:

`python3 exp.py`