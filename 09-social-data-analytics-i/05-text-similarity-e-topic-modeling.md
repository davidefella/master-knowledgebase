# Capitolo 05: Text Similarity

**Lezione:** SD-06, da 00:00:10 a 00:49:53 (la parte successiva, "Supervised Approaches", è nel capitolo 06), Dott.ssa Ida Mele, IASI-CNR
**Slide:** `5_TextSimilarity_SDA25.pdf` (39 pagine). La versione `5_TextSimilarity_SDA26.pdf` su Teams ha testo identico: cambia solo il logo del Dipartimento di Matematica e Fisica, rimosso dalle quattro slide di titolo
**Riferimento:** capitolo 4, *Content: The What of Social Media*, del libro [1] (Szabo, Polatkan, Boykin, Chalkiopoulos, *Social Media Data Mining and Analytics*, Wiley), sezioni da "Using Content Features to Identify Topics" (clustering sui post di Stack Exchange) a "Unsupervised Topic Modeling" (LDA)
**Fonti 2026:** nessuna integrazione Teams 2026 per questo capitolo. Il tutorial `topic_modeling_Gensim_BERTopic` su Teams è materiale del II livello: è citato solo in una nota (sez. 9)
**Codice:** la lezione non mostra codice e non c'è un notebook del I livello su questi temi. Tutti i blocchi di codice sono note aggiunte, eseguite con `verifica_sd05.py` (output in `verifica_sd05_output.txt`)

## Indice

1. [Clustering e text similarity](#1-clustering-e-text-similarity)
2. [Clustering gerarchico agglomerativo](#2-clustering-gerarchico-agglomerativo)
3. [Document clustering e cosine similarity](#3-document-clustering-e-cosine-similarity)
4. [Dal testo ai cluster: step e problemi](#4-dal-testo-ai-cluster-step-e-problemi)
5. [Il dendrogramma](#5-il-dendrogramma)
6. [Esempio: Stack Exchange "Fiction & Fantasy"](#6-esempio-stack-exchange-fiction--fantasy)
7. [Popolarità dei topic e interessi degli utenti](#7-popolarità-dei-topic-e-interessi-degli-utenti)
8. [Topic extraction e limiti dello string matching](#8-topic-extraction-e-limiti-dello-string-matching)
9. [Statistical topic modeling](#9-statistical-topic-modeling)
10. [LDA: input, output e modello grafico](#10-lda-input-output-e-modello-grafico)
11. [LDA: processo generativo e inferenza](#11-lda-processo-generativo-e-inferenza)
12. [Tool e LDA per il clustering: soft e hard](#12-tool-e-lda-per-il-clustering-soft-e-hard)
13. [Riepilogo e compiti](#13-riepilogo-e-compiti)

---

## 1. Clustering e text similarity

*SD-06 @ 00:00:10*

È la lezione che chiude la parte di Natural Language Processing. Due blocchi:

| Blocco | Contenuto |
|---|---|
| Text similarity | document clustering, cosine similarity, clustering gerarchico, esempio con dati di Stack Exchange |
| Topic extraction e topic modeling | statistical topic modeling, Latent Dirichlet Allocation (LDA), clustering dei documenti con il topic modeling |

Il topic modeling estrae gli argomenti di una collezione in modo **completamente non supervisionato**, cioè senza etichettare i documenti, e permette anche di dividere i documenti in base ai topic trattati (SD-06 @ 00:01:28). Come sempre, le slide servono "come una sorta di indice" del capitolo 4 del libro [1]: alcune parti vanno approfondite, altre si possono solo "sorvolare".

*SD-06 @ 00:02:06*

- **Text similarity**: due documenti sono simili se trattano un argomento comune.
- **Clustering**: raggruppare elementi simili. Nell'esempio della slide gli elementi sono punti in uno spazio euclideo a due dimensioni: la loro "similarità" è esattamente la distanza, e più sono lontani meno sono simili.
- **Document clustering**: lo stesso in uno spazio multidimensionale in cui le dimensioni sono le parole e i punti sono i documenti. Si raggruppano i documenti che condividono parole, "cercando anche di sfruttare il contenuto semantico" (SD-06 @ 00:02:46).

---

## 2. Clustering gerarchico agglomerativo

*SD-06 @ 00:02:46*

Tipicamente si usa un clustering **gerarchico e agglomerativo**. L'algoritmo, nella slide e nel libro:

1. **Inizializzazione**: ogni elemento è un cluster a sé (*standalone* o *singleton cluster*); si calcolano le distanze fra tutte le coppie.
2. **Merging**: si trovano i due cluster più vicini e si uniscono. Nella figura, tre punti vicini formano il cluster A e due punti molto vicini il cluster B.
3. **Ridefinizione delle distanze**: per unire A e B in un cluster più grande serve una distanza fra cluster, ricavata dalle distanze fra tutte le coppie di elementi (SD-06 @ 00:03:58).
4. **Criterio di stop**: si ripetono i passi 2 e 3 finché resta un solo cluster, che raggruppa tutto e rappresenta il topic più generale.

| Linkage | Distanza fra due cluster | Nota della lezione |
|---|---|---|
| **Average** | media delle distanze fra tutte le coppie di elementi | "in genere fornisce buoni risultati" |
| **Single** | minimo delle distanze | |
| **Complete** | massimo delle distanze | |

L'esempio a voce (SD-06 @ 00:05:05): documenti su vari sport. All'inizio si uniscono gli sport simili, tennis con ping pong, calcio con rugby; il golf, "perché ha la pallina piccola", si unisce poi a tennis e ping pong; e così via fino al cluster "tutti gli sport".

> **Nota aggiunta:** l'esempio si riproduce con `scipy` su un corpus giocattolo di otto documenti (cinque sport, politica, affari esteri, religione), rappresentati con conteggi di parole e distanza coseno (sez. 3). Con average linkage le fusioni seguono la storia raccontata a lezione. I conteggi sono inventati: il risultato dimostra il meccanismo, non i dati del libro.

```python
# Nota aggiunta: clustering gerarchico su un corpus giocattolo (da verifica_sd05.py).
from sklearn.feature_extraction.text import CountVectorizer
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist

corpus = [
    "tennis racket ball court serve match",          # 0 tennis
    "ping pong table racket ball serve",             # 1 ping pong
    "golf ball club course hole",                    # 2 golf
    "soccer ball goal player match team",            # 3 calcio
    "rugby ball team player try match",              # 4 rugby
    "government election minister vote parliament",  # 5 politica
    "foreign minister embassy treaty government",    # 6 affari esteri
    "church pope christian faith prayer",            # 7 religione
]
X = CountVectorizer().fit_transform(corpus).toarray()
D = pdist(X, metric="cosine")          # distanze d = 1 - cos, forma condensata
Z = linkage(D, method="average")       # oppure "single", "complete"
print(Z)                               # N-1 = 7 righe: (cluster, cluster, altezza, dimensione)
```

Output, riformattato (average linkage):

```
passo 1: soccer + rugby        altezza 0.333
passo 2: tennis + pingpong     altezza 0.500
passo 3: politics + foreign    altezza 0.600
passo 4: {soccer,rugby} + {tennis,pingpong}   altezza 0.750
passo 5: golf + {4 sport}      altezza 0.817
passo 6: {politics,foreign} + {5 sport}       altezza 1.000
passo 7: religion + tutto il resto            altezza 1.000
```

Con single linkage il passo 4 avviene a 0.667 (minimo invece della media); con complete linkage il golf si unisce prima a tennis e ping pong (0.817) e solo dopo al calcio e al rugby (0.833). Le altezze crescono in modo monotono, come previsto dal libro. In `scikit-learn` lo stesso si ottiene con `AgglomerativeClustering(n_clusters=3, metric="cosine", linkage="average")`, che qui restituisce i cluster {5 sport}, {politics, foreign}, {religion}.

---

## 3. Document clustering e cosine similarity

*SD-06 @ 00:06:09*

Un cluster grande rappresenta un topic generale (sport), i cluster più piccoli i suoi sottotopic (calcio, tennis, golf, notizie sulle partite, squadre). Per trattare i documenti si usa la rappresentazione vettoriale vista nel capitolo 04: ogni documento diventa un vettore di score sulle parole.

- **Bag of words** (per esempio `CountVectorizer`): solo il conteggio delle occorrenze della parola nel documento.
- **TF-IDF**: la frequenza nel documento moltiplicata per l'IDF, che dice quanto il termine è discriminativo.

Prima va sempre fatto il **preprocessing** (caratteri speciali, stop word, stemming o lemmatizzazione): pulisce il testo e riduce la dimensionalità, altrimenti i vettori sono molto sparsi (SD-06 @ 00:06:39).

### Cosine similarity

*SD-06 @ 00:07:43*

Definizione semplice: due documenti sono tanto più simili quanto più i loro termini si sovrappongono. Esempio della slide: due post che contengono più volte "star" e "trek" parlano probabilmente della serie *Star Trek*.

Dati due documenti *u* e *v*, sia *u_t* il numero di occorrenze del termine *t* in *u* e *v_t* quello in *v*. La **cosine similarity** è il prodotto scalare dei due vettori normalizzati:

$$S(\mathbf{u},\mathbf{v}) = \frac{\sum_t u_t v_t}{\sqrt{\sum_t u_t^2}\,\sqrt{\sum_t v_t^2}} = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|} = \frac{\mathbf{u}}{\|\mathbf{u}\|}\cdot\frac{\mathbf{v}}{\|\mathbf{v}\|}$$

Il denominatore è il prodotto delle norme: per ciascun documento si sommano i quadrati dei valori e si prende la radice (SD-06 @ 00:08:49). In un corpus si ottiene una similarità per ogni coppia di documenti: con mille o duemila documenti, una matrice.

*SD-06 @ 00:09:21*

Si chiama "coseno" perché è il coseno dell'angolo fra i due vettori (figura della slide: doc 1 e doc 2 nel piano x1, x2, con l'angolo θ). Per il clustering serve una **distanza**:

$$d(\mathbf{u},\mathbf{v}) = 1 - S(\mathbf{u},\mathbf{v})$$

| Documenti | Cosine similarity | Distanza |
|---|---|---|
| molto simili | vicina a 1 | vicina a 0 |
| molto diversi | vicina a 0 | vicina a 1 |

Similarità 1 (distanza 0) si ha solo con un overlap completo, cioè documenti fatti delle stesse parole; in pratica i valori stanno fra 0 e 1 (SD-06 @ 00:09:51).

> **Nota aggiunta:** tre precisazioni.
> 1. Per vettori qualsiasi il coseno sta fra -1 e 1; sta fra 0 e 1 perché conteggi e pesi TF-IDF sono non negativi (lo dice anche il libro). Più precisamente, vale 1 quando i vettori sono **proporzionali**: un documento e la sua copia ripetuta due volte hanno similarità 1.
> 2. La slide dice che il coseno "è anche lo stesso che prendere il prodotto scalare u · v". Vale solo per vettori già normalizzati (ultima forma della formula); nel libro la frase si riferisce al numeratore. Sui conteggi grezzi il prodotto scalare non è limitato a [0, 1].
> 3. La slide chiama la cosine similarity "distance metric". È una similarità, e anche 1 - S non è una metrica in senso matematico, perché non rispetta la disuguaglianza triangolare. Al clustering agglomerativo basta comunque una dissimilarità.

```python
# Nota aggiunta: verifica numerica (da verifica_sd05.py).
import numpy as np
u = np.array([3, 2, 0, 1])     # conteggi di (star, trek, ring, ship) in u
v = np.array([2, 3, 0, 0])
s1 = (u * v).sum() / (np.sqrt((u**2).sum()) * np.sqrt((v**2).sum()))
s2 = u @ v / (np.linalg.norm(u) * np.linalg.norm(v))
s3 = (u / np.linalg.norm(u)) @ (v / np.linalg.norm(v))
print(round(s1, 4), round(s2, 4), round(s3, 4), u @ v, round(1 - s1, 4))
# 0.8895 0.8895 0.8895 12 0.1105   (le tre forme coincidono; u·v grezzo = 12)

# 1 - cos viola la disuguaglianza triangolare
d = lambda x, y: 1 - x @ y / (np.linalg.norm(x) * np.linalg.norm(y))
a, b, c = np.array([1, 0]), np.array([1, 1]), np.array([0, 1])
print(d(a, c), round(d(a, b) + d(b, c), 4))   # 1.0 0.5858
```

---

## 4. Dal testo ai cluster: step e problemi

*SD-06 @ 00:10:28*

Gli step da ricordare "ogni volta che dobbiamo fare un'operazione su dati testuali":

1. **Preprocessing**: tokenizzazione, pulizia, rimozione delle stop word, stemming o lemmatizzazione.
2. **Feature vector** per ogni documento: conteggi (`CountVectorizer`, bag of words) o TF-IDF.
3. **Cosine similarity** fra i vettori.
4. **Clustering agglomerativo** sulle distanze: i documenti vicini finiscono nello stesso cluster.

Due problemi (SD-06 @ 00:11:05):

| Problema | Soluzione | Spiegazione della lezione |
|---|---|---|
| Il vocabolario del corpus è enorme: vettori molto sparsi, con pochissime componenti non nulle | buon preprocessing per ridurre la dimensionalità | stemming e lemmatizzazione collassano le varianti al termine base (lo *stem*, "lo stelo", o la forma del dizionario); le stop word come *the, of, and* compaiono ovunque e non discriminano l'argomento |
| Alcune parole sono molto più frequenti di altre anche dopo il preprocessing | pesi diversi ai termini: **TF-IDF** | in una collezione di articoli scientifici *experiments, results, state of the art* compaiono quasi ovunque. La TF dice quanto il termine conta nel documento, l'IDF lo "sconta" se compare in molti documenti, rendendolo simile a una stop word (SD-06 @ 00:12:42) |

Gli esempi in slide, presi dal libro, sono *would, one, time*: le parole in cima alla lista di frequenza dei post di Stack Exchange dopo la rimozione delle stop word.

> **Nota aggiunta (dal libro, non detto a lezione):** nel dataset Science Fiction & Fantasy un singolo post ha circa 54 termini distinti, il vocabolario circa 116.000. Gli autori calcolano le similarità con R (`tm`, `Matrix`), con pesi TF-IDF e vettori normalizzati, e usano d = -S invece di 1 - S: con 1 - S la matrice delle distanze si riempirebbe di 1 e perderebbe la sparsità. Per il clustering conta solo l'ordine delle distanze, e alla fine sommano 1 alle altezze di merge per riportarle in [0, 1].

---

## 5. Il dendrogramma

*SD-06 @ 00:13:25*

Il clustering agglomerativo produce un **albero binario** (ogni nodo ha due figli), il **dendrogramma**:

- le **foglie** sono i singoli documenti;
- la **radice** è il topic più generale (nell'esempio iniziale, "sport");
- salendo, i cluster diventano più generali perché agglomerano topic sempre più diversi.

Con N documenti ci sono N - 1 fusioni, quindi N - 1 **merging heights**: le distanze a cui avviene ogni fusione, disegnate come linee orizzontali. La slide (dal libro) mostra un dendrogramma reale su asse verticale da 0,4 a 1,0 con la scritta "Going up we have more general clusters, while the leaves represent the documents".

Una linea verticale lunga sotto una fusione indica che i due cluster erano lontani anche dal vicino più prossimo. L'esempio a voce (SD-06 @ 00:14:48): unire politica e affari esteri avviene a distanza minore; unirli poi alla religione richiede una distanza maggiore, e ancora maggiore unirli allo sport.

> **Nota aggiunta:** nel corpus giocattolo della sez. 2, `linkage` restituisce 7 righe per 8 documenti, cioè N - 1 merging heights, e `scipy.cluster.hierarchy.dendrogram(Z, labels=..., no_plot=True)` ordina le foglie come `['religion', 'politics', 'foreign', 'golf', 'soccer', 'rugby', 'tennis', 'pingpong']`. Il disegno si ottiene togliendo `no_plot=True` (serve `matplotlib`).

---

## 6. Esempio: Stack Exchange "Fiction & Fantasy"

*SD-06 @ 00:15:30*

Applicando gli step precedenti (preprocessing, vettorizzazione bag of words o TF-IDF, clustering agglomerativo) alle domande della sezione *Science Fiction & Fantasy* di Stack Exchange, gli autori del libro isolano **tre cluster**, riconoscibili dalle word cloud dei termini più frequenti:

| Cluster | Topic | Termini nella word cloud (stemmati) |
|---|---|---|
| A | *Lord of the Rings* | ring, sauron, gandalf, hobbit, frodo, saruman, tolkien |
| B | *Star Trek* | enterpris, warp, borg, kirk, klingon, picard, ship, episod, vulcan |
| C | *story identification* | book, stori, rememb, read, alien, planet, human |

Le parole sono troncate perché è stato applicato lo stemming: "stori" è *story*, "rememb" è *remember*, ma restano riconoscibili (SD-06 @ 00:17:58).

Il cluster C non è un'opera ma un **tipo di domanda**: un utente ricorda la trama di un libro, di una serie o di un film ma non il titolo, la descrive e chiede agli altri se lo riconoscono. Gli esempi della lezione: "ho letto questo libro che trattava di viaggi nello spazio, ricordate il titolo?", oppure una serie con i personaggi delle favole ambientata ai giorni nostri (SD-06 @ 00:16:52).

> **Nota aggiunta (dal libro):** i tre cluster sono sottoalberi scelti a mano nella parte alta del dendrogramma, tagliato a distanza 0,9 (Figura 4.5 del libro, funzione `identify` di R). Il libro osserva che il cluster C è tenuto insieme non dall'argomento ma dall'**intento** degli utenti, e dalla mancanza di parole specifiche nel testo.

### Valutazione del clustering

*SD-06 @ 00:18:28*

Come si sa se i cluster sono corretti? Serve un'etichettatura.

| Valutazione | Come | Costo |
|---|---|---|
| **Manuale** | persone aprono i documenti di ogni cluster e controllano che trattino lo stesso argomento; si può campionare, per esempio 100 documenti per cluster, 300 in tutto | richiede molto tempo anche con il campionamento |
| **Automatica** | si usa un'altra fonte d'informazione come etichetta. Su Stack Exchange chi scrive la domanda le assegna dei **tag**, che sono "una buona approssimazione" degli argomenti e sono più puliti del testo | quasi nullo |

Ripetendo il clustering con le sole parole dei tag si ottengono di nuovo tre cluster: *lord-of-the-rings*, *star-trek*, *story-identification*. I tag concordano bene con i topic trovati sul testo (SD-06 @ 00:19:33). Una domanda può avere più tag: nel cluster Star Trek, oltre al tag dominante *star-trek*, compaiono tag minori come *star-wars*, *star-trek-voyager*, *star-trek-enterprise* e altri leggibili solo in parte nella slide (SD-06 @ 00:20:05).

---

## 7. Popolarità dei topic e interessi degli utenti

### Distribuzione dei tag

*SD-06 @ 00:20:05*

Quali topic interessano di più? Si possono estrarre i topic dal testo (topic modeling, sez. 9-12) oppure usare i tag. Il numero di volte che ogni tag compare, in un grafico log-log, segue chiaramente una **power law**: decrescita molto rapida e l'effetto di *fanning out* già visto nel capitolo 02.

> **Nota aggiunta (dal libro):** l'esponente stimato è circa -1,4 (didascalia della Figura 4.7). Il libro nota l'analogia con il capitolo 02: se si trattano i tag come utenti, il numero di volte che un tag è "attivo" ha la stessa distribuzione del numero di azioni di un utente. I tag più usati sono *story-identification*, *harry-potter*, *star-trek*, *star-wars*, *movie*, *lord-of-the-rings*.

### Popolarità dopo il clustering

*SD-06 @ 00:21:26*

Si possono rappresentare i risultati del clustering a **granularità diverse** tagliando il dendrogramma a una certa altezza (*cut height*): è il criterio di stop. Si contano poi i post di ogni ramo sotto il taglio. Il grafico della slide confronta tre tagli, 0,5, 0,7 e 0,9: tutte e tre le distribuzioni seguono una power law e hanno all'incirca la stessa forma.

> **Correzione:** a lezione (SD-06 @ 00:21:26-00:22:30) e nella slide *Topic Popularity after Clustering* la direzione è invertita: "se impostiamo 0.5 ci fermiamo a dei cluster piuttosto grandi", con 0,7 e 0,9 "andiamo sempre più in profondità", e "la distribuzione è più inclinata per i cluster più grandi". Il dendrogramma ha le **distanze** sull'asse verticale (foglie in basso, radice in alto vicino a 1). Tagliare a 0,5 significa fermarsi **in basso**, con molti cluster piccoli; tagliare a 0,9 significa fermarsi **in alto**, con pochi cluster grandi. Lo dice il libro: "As we go higher in the dendrogram (let the clustering proceed further), we start to see the distributions shift toward larger cluster sizes", con esponente che diventa "shallower". Lo conferma il grafico stesso: la serie a 0,5 (cerchi) parte da circa 10^4 rami di un solo post e non supera i 10 post per ramo; quella a 0,9 (rombi) arriva a oltre 100 post per ramo. Quindi la distribuzione più ripida è quella dei cluster **più piccoli** (taglio a 0,5).

```python
# Nota aggiunta: tagli del dendrogramma a altezze diverse, su 1500 documenti
# sintetici con 30 topic di popolarità long-tail (da verifica_sd05.py).
from scipy.cluster.hierarchy import fcluster
for h in [0.5, 0.7, 0.9]:
    lab = fcluster(Zs, t=h, criterion="distance")   # Zs = linkage average su distanze coseno
    ...
# cut 0.5: 446 cluster | singleton 135 | max size 32  | media 3.4
# cut 0.7:  60 cluster | singleton  11 | max size 639 | media 25.0
# cut 0.9:  25 cluster | singleton   1 | max size 799 | media 60.0
```

Più alto il taglio, meno cluster e più grandi. Sul corpus giocattolo della sez. 2: 6 cluster a 0,5, 5 a 0,7, 3 a 0,9.

### Interessi degli utenti

*SD-06 @ 00:22:30*

Quanto sono diversi gli interessi dei singoli utenti? La procedura della slide:

1. per ogni utente si ordinano le sue etichette di interesse (topic o tag) in ordine decrescente di frequenza;
2. si **normalizzano** i pesi in modo che sommino a 1 per ogni utente, così la metrica è la stessa a prescindere da quanto l'utente sia attivo;
3. si fa la media sugli utenti, rank per rank.

| Rank del tag | Frequenza relativa per utente |
|---|---|
| 1 | 52,1% |
| 2 | 25,8% |
| 3 | 11,0% |
| 4 | 4,2% |
| 5 | 2,1% |

La decrescita è molto rapida: dal 52,1% del primo rank al 2,1% del quinto.

> **Correzione:** a lezione (SD-06 @ 00:22:30) il 52,1% è letto come "il tag più popolare in assoluto è stato usato da più del 50% degli utenti", e il 2,1% come "il quinto tag più popolare è usato dal 2% degli utenti"; la slide scrive "The most popular tag is used by around 50% of the users". La tabella (Table 4.1 del libro) misura un'altra cosa: il rank è **per utente**, non globale. Il libro: "On average, the most frequently used tag appears in 52.1% of a user's posts, the second most frequent tag appears 25.8% of the time". Cioè: in media, il tag preferito di ciascun utente (diverso da utente a utente) copre il 52,1% dei suoi tag. Il dato dice che gli interessi individuali sono concentrati su pochi argomenti, non quanti utenti usano un certo tag.

```python
# Nota aggiunta: la procedura della Listing 4.6 del libro, in Python, su tre utenti inventati.
from collections import Counter, defaultdict
user_tags = {"ann": ["star-trek", "star-trek", "star-trek", "star-wars", "story-identification"],
             "bob": ["lord-of-the-rings", "lord-of-the-rings", "harry-potter"],
             "cid": ["story-identification"]}
by_rank = defaultdict(float)
for user, tags in user_tags.items():
    freqs = sorted((c / len(tags) for c in Counter(tags).values()), reverse=True)  # normalizza e ordina
    for r, f in enumerate(freqs, start=1):
        by_rank[r] += f
tot = sum(by_rank.values())
print({r: round(f / tot, 3) for r, f in sorted(by_rank.items())})
# ann [0.6, 0.2, 0.2], bob [0.667, 0.333], cid [1.0]  ->  {1: 0.756, 2: 0.178, 3: 0.067}
```

Il rank 1 è *star-trek* per ann, *lord-of-the-rings* per bob, *story-identification* per cid: la media al rank 1 non riguarda un tag specifico.

---

## 8. Topic extraction e limiti dello string matching

*SD-06 @ 00:23:37*

La **topic extraction** estrae informazione a **bassa dimensionalità**, il più possibile strutturata, da testo che è non strutturato e ad **alta dimensionalità**. Anche un testo breve come un tweet è un vettore lunghissimo: con il bag of words sul primo milione di parole inglesi, "Good morning!" è un vettore di un milione di componenti, tutte zero tranne "good" e "morning", che valgono 1 o il loro score TF-IDF (SD-06 @ 00:24:15).

```python
# Nota aggiunta: "Good morning!" come vettore sparso (da verifica_sd05.py).
import numpy as np
from scipy.sparse import csr_matrix
vec = csr_matrix((np.ones(2), ([0, 0], [4211, 15873])), shape=(1, 1_000_000))  # indici arbitrari
print(vec.shape[1], vec.nnz, vec.nnz / vec.shape[1])   # 1000000 2 2e-06
```

### Perché è difficile per una macchina

*SD-06 @ 00:24:46*

Per una persona convertire testo grezzo, scritto o parlato, in significato è relativamente semplice, perché associa un concetto alla parola e la disambigua con il contesto (tempo, mittente e altro). L'esempio già usato nel capitolo 04: "pesca" è scritta allo stesso modo come frutto e come azione, ma "io mangio la pesca" e "vado a pescare al lago" non lasciano dubbi. Anche le persone a volte sbagliano, se il contesto non basta o c'è sarcasmo e manca il tono di voce. Per un computer è molto più difficile: deve simulare la comprensione e intanto mappare il testo, non strutturato, in qualcosa di tabellare e numerico, come la matrice documento-termine (SD-06 @ 00:25:57).

La slide contrappone due schemi: *raw text → cervello umano → extracted meaning* e *raw text → topic modeling → extracted meaning*. L'obiettivo è far "imitare il cervello umano" alla macchina, trasformando milioni di parole in pochi temi: è un **mapping many-to-one**.

**Applicazioni** (SD-06 @ 00:26:45):

- **similarità basata sul contenuto**, quindi clustering di documenti sullo stesso argomento;
- **text classification**: su un grande sito di notizie o di blog, separare politica da cronaca. Lo può fare a mano il giornalista con un tag, come gli utenti di Stack Exchange; senza contributo umano, per esempio su uno stream di tweet, serve la classificazione;
- **text summarization**, che "ultimamente sta avendo molta attenzione" perché aiuta la generative AI a mostrare un riassunto invece di una lista di risultati di ricerca.

### String matching

*SD-06 @ 00:28:24*

Perché non basta lo **string matching**, cioè controllare se due parole sono scritte allo stesso modo? Per via dei sinonimi: un documento con "cat" e uno con "kitty" parlano dello stesso topic ma non vengono collegati.

L'esempio della slide:

- doc1: *"Today's soccer match was amazing!"*
- doc2: *"The right player could have scored that goal"*

Una persona risponde che sono simili, perché parlano entrambi di una partita di calcio. Un programma che usa lo string matching risponde di no: nessuna parola in comune, similarità 0. Bisogna trovare i **topic latenti** che rappresentano il significato comune, associando "soccer" e "match" del primo documento a "right player", "scored" e "goal" del secondo. La soluzione è il **topic modeling**, che apprende rappresentazioni tematiche a bassa dimensionalità (*topic*) del testo.

```python
# Nota aggiunta: l'esempio della slide con bag of words e cosine similarity (da verifica_sd05.py).
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs = ["Today's soccer match was amazing!",
        "The right player could have scored that goal"]
cv = CountVectorizer(stop_words="english")
X = cv.fit_transform(docs)
print(cv.get_feature_names_out().tolist())
# ['amazing', 'goal', 'match', 'player', 'right', 'scored', 'soccer', 'today']
print(cosine_similarity(X)[0, 1])   # 0.0
```

> **Nota aggiunta:** nel libro il secondo tweet è "The right **winger** could have scored that goal": "right winger" è l'ala destra, cioè una posizione in campo. La slide lo semplifica in "right player", che perde il riferimento al ruolo.

---

## 9. Statistical topic modeling

*SD-06 @ 00:30:06*

Lo **statistical topic modeling** scopre i topic in modo probabilistico in una grande collezione di documenti non etichettati, quindi in modo non supervisionato. Due assunzioni:

1. **ogni documento è un mix di topic**: una pagina Wikipedia sull'Italia ha sezioni di storia, geografia, religione, cultura (SD-06 @ 00:30:37);
2. **ogni topic è una distribuzione di probabilità sulle parole**: nei documenti di sport compaiono più spesso giocatore, match, partita, calcio, basket, baseball; in quelli di politica governo, elezioni, comizio.

Alla base c'è la **distributional hypothesis**: parole che compaiono in contesti simili hanno significato simile. La slide cita J.R. Firth, "a word is characterized by the company it keeps": la parola si riconosce "dalla sua cerchia di amicizie" (SD-06 @ 00:31:42).

La slide confronta l'umano (giusto livello di astrazione, cambio di contesto al volo) con la macchina, che può simulare la conoscenza umana ma incontra due sfide (SD-06 @ 00:32:18):

| Sfida | Esempio |
|---|---|
| **Sinonimia** | "cat" e "kitty" (gatto, micio) indicano lo stesso felino |
| **Polisemia** | "Turkey": l'animale in *this turkey is delicious*, il paese in *the new president of Turkey was elected* |

> **Nota aggiunta:** la formulazione più citata di Firth (1957) è "You shall know a word by the company it keeps". Non l'ho verificata su fonte primaria.

### Modello generativo

*SD-06 @ 00:33:05*

Un topic model è un **modello generativo**: specifica una procedura probabilistica con cui i documenti potrebbero essere generati, parola per parola. È una semplificazione: le parole compaiono in modo casuale e la loro **posizione non conta** (è un bag of words), mentre le persone tengono conto dell'ordine.

L'output è un insieme di topic, ognuno rappresentato da una distribuzione di probabilità sulle parole. Nel topic "politica" *election*, *parliament*, *minister* hanno probabilità alta rispetto a *smartphone* e *computer* (topic tech) o *soccer* e *tennis* (topic sport). Precisazione importante della lezione: approcci come LDA "molto spesso non rispondono con una label 'politica'", ma con **la lista delle parole più frequenti** nei documenti di quel topic. L'etichetta la dà l'analista (SD-06 @ 00:33:53).

### Modelli principali

*SD-06 @ 00:34:28*

| Modello | Autori | Idea |
|---|---|---|
| **pLSA**, probabilistic Latent Semantic Analysis | Hofmann, 1999 | il modello pionieristico |
| **LDA**, Latent Dirichlet Allocation | Blei et al., 2003 | versione avanzata di pLSA |
| **DTM**, Dynamic Topic Modeling | Blei & Lafferty, 2006 | applica LDA su finestre temporali per vedere come evolvono i topic |
| **BERTopic** | Grootendorst, 2022 | embedding BERT (Transformer) + una definizione *class-based* di TF-IDF |

L'esempio di DTM a voce (SD-06 @ 00:35:04): su una collezione di articoli di informatica, l'intelligenza artificiale un tempo era soprattutto robotica, oggi sempre più NLP, comprensione del linguaggio, chatbot e generative AI. BERTopic è più recente e, usando gli embedding, dà risultati migliori.

> **Nota aggiunta:** a voce BERTopic è contrapposto "alla semplice definizione di TF-IDF", ma la slide dice che BERTopic **usa** anch'esso una variante di TF-IDF: gli embedding servono a raggruppare i documenti, la *class-based TF-IDF* (c-TF-IDF) a estrarre le parole rappresentative di ogni gruppo.

> **Nota aggiunta (fuori perimetro I livello):** su Teams c'è il tutorial `Tutorials/topic_modeling_Gensim_BERTopic/` (`LDA_Gensim.ipynb`, `BERTopic.ipynb`, dataset `ACM_papers.tsv` con titoli e abstract ACM), materiale del II livello e non trattato in questa guida. Può servire a chi sceglie la traccia d'esame **#SDA3** (*Sentiment Analysis & Topic Extraction*), che chiede di usare "LDA, Gensim, BERTopic" per estrarre i topic dei documenti positivi e negativi (`0_General_Info_SDA26.pdf`). Il notebook Gensim copre preprocessing, dizionario Gensim, LDA con 3 topic, topic dominante per documento (hard clustering), scelta di k con la coherence `c_v` e visualizzazione con pyLDAvis.

---

## 10. LDA: input, output e modello grafico

### Input e output

*SD-06 @ 00:36:12*

"Noi lo utilizziamo come una riga di codice", ma bisogna capire come funziona.

- **Input**: la collezione di documenti, preprocessata, e il numero di topic **K**, scelto da noi o stimato, per esempio con una grid search. K grande dà molti topic specifici, K piccolo (per esempio 3) pochi topic generali (SD-06 @ 00:36:43).
- **Output**: K topic, dove un topic è una lista di parole rappresentative.

L'esempio della slide, con K = 3, ricavato da Mele da una collezione reale di notizie (SD-06 @ 00:37:56):

| Topic | Parole | Interpretazione |
|---|---|---|
| 1 | parliament, minister, democracy, elections, vote, referendum | politica |
| 2 | rain, weather, storm, people, flooding, county, water | disastro naturale: un'inondazione |
| 3 | shooting, bomb, victims, police, terrorism, isis, gun | cronaca: attentati terroristici |

All'epoca "si parlava molto di attacchi terroristici, di ISIS, e ci fu anche un'inondazione in India, se non ricordo male". La lista reale era più lunga.

### Modello grafico

*SD-06 @ 00:37:56*

LDA si rappresenta con un **modello grafico probabilistico**, che visualizza le dipendenze fra le entità e il processo generativo. I rettangoli sono la **plate notation**: in inferenza bayesiana indicano variabili replicate (SD-06 @ 00:38:37).

```
          [ β ]K                       nodi bianchi = variabili latenti
             \                         nodo grigio  = osservato
  α → θ → [ z → (w) ]N ]M              plate N: parole del documento
                                       plate M: documenti del corpus
                                       plate K: topic
```

| Simbolo | Significato |
|---|---|
| **M** | numero di documenti del corpus |
| **N** | numero di parole di ogni documento (la slide assume che tutti i documenti abbiano la stessa lunghezza) |
| **w** (grigio) | le parole osservate: l'unica cosa che il modello vede |
| **θ** | proporzioni dei topic nel documento (*per-document topic distribution*), latente |
| **z** | assegnazione di un topic a ogni posizione di parola, latente |
| **β** | i topic, cioè le distribuzioni sulle parole (*per-topic word distribution*), K in tutto, latenti |
| **α** | parametro fisso del modello |
| **K** | numero di topic, fissato da noi o stimato empiricamente |

Mele spiega l'assunzione di lunghezza uguale così: si prende il documento più lungo, per esempio mille parole, e si riempiono gli altri con "parole vuote" (SD-06 @ 00:38:37-00:39:07).

> **Correzione:** l'uguale lunghezza è solo una semplificazione di notazione della figura, e le implementazioni non riempiono i documenti con parole vuote. Nel modello di Blei et al. (2003) ogni documento ha la sua lunghezza N_d; `scikit-learn` e Gensim lavorano su conteggi bag of words, dove la lunghezza diversa non crea problemi. Un token di riempimento sarebbe anzi dannoso: comparirebbe moltissimo in tutti i documenti corti e finirebbe dentro i topic.

---

## 11. LDA: processo generativo e inferenza

### Il processo generativo con i secchielli

*SD-06 @ 00:39:40*

Le slide costruiscono il processo un passo alla volta, con dei secchielli di palline colorate.

**1. Topic bucket (θ, parametro α).** Ogni documento è un mix di topic. Esempio con tre topic al 50%, 30% e 20%, come la pagina Wikipedia di un paese: politica, geografia, religione [?]. La distribuzione si immagina come un secchiello di palline: 5 verdi (topic 1), 3 rosse (topic 2), 2 blu (topic 3). I topic più probabili hanno più palline (SD-06 @ 00:40:14).

**2. Word buckets (β).** Per ogni topic c'è un secchiello di parole, ciascuna replicata in proporzione alla probabilità di comparire in un documento di quel topic. Intuizione: se una parola rappresenta un topic, comparirà nei documenti di quel topic (SD-06 @ 00:40:46).

**3. Generazione.** Per ogni posizione *z* del documento (SD-06 @ 00:41:26):

1. si estrae una pallina dal topic bucket, per esempio verde (topic 1);
2. si va nel word bucket verde e si estrae una parola *w*;
3. la si scrive in quella posizione, e si passa alla successiva.

**4. Risultato.** Il documento generato non ha senso per una persona: è come una rappresentazione bag of words. Ha senso per la macchina, perché le parole rosse vi compaiono con una frequenza che dice che il topic rosso pesa il 30% (SD-06 @ 00:41:57).

> **Nota aggiunta:** in notazione standard (LDA "smoothed", come in figura con β dentro il plate K) il processo è:
> - per ogni topic k = 1..K: β_k ~ Dirichlet(η);
> - per ogni documento d: θ_d ~ Dirichlet(α);
> - per ogni posizione n del documento: z_{d,n} ~ Categorical(θ_d), poi w_{d,n} ~ Categorical(β_{z_{d,n}}).
>
> Il "Dirichlet" del nome è la distribuzione da cui si estraggono θ e β: una distribuzione su vettori di probabilità. Con α piccolo i documenti tendono a concentrarsi su pochi topic. Nel modello originale del 2003 β è invece una matrice di parametri, senza η.

### Inferenza

*SD-06 @ 00:42:31*

Il processo generativo serve a capire perché il modello funziona; nella realtà si fa il percorso inverso, l'**inferenza**: data la collezione e il numero di topic, si apprende il modello che descrive i topic. La slide *LDA: Inference* mette i due percorsi uno sopra l'altro:

| | Da | A |
|---|---|---|
| Processo generativo | distribuzione dei topic per documento e delle parole per topic | documenti |
| Inferenza (**Gibbs sampling**) | documenti (input del modello) | topic (output del modello): liste di parole con probabilità |

Per il topic politica si ottiene per esempio *government, election, president*; per sport *soccer, basketball, player, match*; per religione *christian, church, pope*.

La figura successiva viene dall'articolo di Blei et al. (SD-06 @ 00:43:04): un articolo di *Science* ("Seeking Life's Bare (Genetic) Necessities") con ogni parola colorata secondo il topic assegnato, l'istogramma delle proporzioni dei topic e quattro topic a sinistra, ciascuno con parole e probabilità (gene 0,04, dna 0,02, genetic 0,01; life, evolve, organism; brain, neuron, nerve; data, number, computer). LDA "non cerca di capire il significato semantico della frase", identifica le parole più rappresentative di ciascun topic.

> **Nota aggiunta (dal libro e dalla documentazione dei tool, verificata il 22/10/2026):** l'inferenza cerca la distribuzione a posteriori delle variabili latenti (θ, z, β) date le parole osservate. Il denominatore della formula di Bayes è intrattabile, quindi si usano metodi approssimati: campionamento MCMC, di cui il Gibbs sampling citato in slide è un caso, oppure **inferenza variazionale**. I due tool Python della slide successiva usano la seconda: `sklearn.decomposition.LatentDirichletAllocation` implementa "online variational Bayes" (default `learning_method='batch'`, priori di default 1/K) e `gensim.models.LdaModel` l'online LDA di Hoffman et al. (2010). Il libro usa invece il Gibbs sampler del pacchetto R `lda` (`lda.collapsed.gibbs.sampler`).

---

## 12. Tool e LDA per il clustering: soft e hard

### Tool

*SD-06 @ 00:43:34*

| Tool | Classe o modulo | Link della slide |
|---|---|---|
| **scikit-learn** | `sklearn.decomposition.LatentDirichletAllocation` | scikit-learn.org, pagina della classe |
| **Gensim** ("topic modeling for humans") | `gensim.models.ldamodel` | radimrehurek.com/gensim |
| **BERTopic** | basato su Transformer, risultati "anche migliori dei modelli più tradizionali" | maartengr.github.io/BERTopic |

Lo schema in slide: in input la collezione e K = 3, in output la distribuzione dei topic (una tabella di parole con probabilità per topic).

> **Nota aggiunta:** la lezione non mostra un esempio LDA eseguibile: i topic della slide K = 3 vengono da una collezione di notizie non fornita. L'esempio qui sotto riproduce l'idea su un corpus giocattolo di 11 frasi costruite con le parole della slide, più due documenti misti. **I topic dipendono dal seed** (`random_state`): cambiano numerazione e, sui documenti ambigui, anche le proporzioni. Su un corpus così piccolo e separato le tre liste si ritrovano comunque.

```python
# Nota aggiunta: LDA con scikit-learn su un corpus giocattolo (da verifica_sd05.py).
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

news = [
    "parliament minister election vote referendum democracy",
    "minister parliament vote election government",
    "referendum vote democracy parliament election",
    "rain storm flooding water weather river",
    "flooding water rain people storm country",
    "weather storm rain flooding people",
    "shooting bomb police victims terrorism",
    "police terrorism bomb attack victims gun",
    "bomb shooting police gun terrorism",
    "minister police terrorism parliament vote",   # doc 9: misto politica/cronaca
    "storm flooding minister government water",    # doc 10: misto disastro/politica
]
cv = CountVectorizer()
X = cv.fit_transform(news)                  # LDA lavora sui conteggi, non su TF-IDF
vocab = cv.get_feature_names_out()

lda = LatentDirichletAllocation(n_components=3, random_state=0, max_iter=200)
theta = lda.fit_transform(X)                # per-document topic distribution (righe sommano a 1)
for k, row in enumerate(lda.components_):   # pesi parola-topic (beta non normalizzato)
    print(k, [vocab[i] for i in row.argsort()[::-1][:5]])
```

Output reale con due seed:

| | `random_state=0` | `random_state=1` |
|---|---|---|
| topic 0 | storm, flooding, rain, water, people | vote, parliament, minister, election, referendum |
| topic 1 | terrorism, police, bomb, gun, victims | storm, flooding, rain, water, weather |
| topic 2 | vote, parliament, minister, election, referendum | terrorism, police, bomb, gun, victims |
| θ doc 9 | [0.06, 0.39, 0.56] | [0.56, 0.06, 0.39] |
| θ doc 10 | [0.87, 0.06, 0.07] | [0.38, 0.57, 0.06] |

Con il seed 1 il documento 10 risulta un mix disastro/politica, con il seed 0 quasi solo disastro.

### LDA per il clustering

*SD-06 @ 00:44:09*

Il topic modeling si usa anche per il **clustering dei documenti**. Con 3 topic lo spazio LDA ha tre dimensioni: la slide lo disegna come un triangolo con i topic ai vertici. LDA assegna a ogni documento la sua distribuzione dei topic, un'"impronta digitale" (*fingerprint*) che permette di confrontare i documenti. Un documento verde vicino al vertice "Topic 1" tratta quasi solo quel topic; i documenti arancioni stanno a cavallo fra topic 1 e 2, quelli fucsia fra 2 e 3; quelli grigi al centro "trattano un po' di tutto" (SD-06 @ 00:44:40).

| | Soft clustering | Hard clustering |
|---|---|---|
| Regola | un documento può appartenere a più cluster | un documento appartiene a un solo cluster |
| Pregio | più realistico: i documenti trattano spesso più topic (SD-06 @ 00:45:19) | più semplice |
| Come | si tengono tutti i topic sopra una certa probabilità | si usa una soglia, oppure si tiene il primo topic (*top-first topic*): il documento arancione va al topic a cui è più simile, anche se tratta in parte l'altro (SD-06 @ 00:46:07) |
| Quando | | "è una semplificazione, però dipende dal tipo di applicazione" |

```python
# Nota aggiunta: hard e soft clustering dalla matrice theta dell'esempio precedente.
import numpy as np
hard = theta.argmax(axis=1)                              # top-first topic
soft = [np.where(t >= 0.3)[0].tolist() for t in theta]   # soglia 0.3, scelta arbitraria
print(hard.tolist())
# seed 0: [2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 0]
print(soft)
# seed 0: [[2], [2], [2], [0], [0], [0], [1], [1], [1], [1, 2], [0]]
# seed 1: ... doc 9 -> [0, 2], doc 10 -> [0, 1]
```

Il documento 9 ("minister police terrorism parliament vote") finisce in due cluster con il soft clustering e nel solo cluster politica con l'hard clustering.

---

## 13. Riepilogo e compiti

*SD-06 @ 00:46:37*

- **Document clustering**: raggruppare documenti simili in base ai topic trattati.
- **Text similarity**: cosine similarity fra vettori di documenti; distanza d = 1 - S.
- **Clustering gerarchico** agglomerativo: si fondono via via i cluster più vicini fino alla radice. Il risultato è il **dendrogramma**, albero binario con i documenti come foglie e cluster sempre più generali salendo.
- **Esempio Stack Exchange "Fiction & Fantasy"**: tre cluster (*Lord of the Rings*, *Star Trek*, *story identification*), confermati dai tag. La popolarità dei topic segue una **power law** (*long-tailed*): pochi topic interessano a molti utenti, molti topic a una cerchia ristretta. *Story identification* era molto popolare.
- **Topic extraction** con il **topic modeling** statistico: **LDA** estrae i topic in modo automatico e non supervisionato, dati la collezione e il numero di topic; ogni topic è la lista delle parole più rappresentative.
- **Tool**: scikit-learn, Gensim, BERTopic.
- **Clustering con LDA**: **soft** se un documento può avere più label di topic, **hard** se ne ha una sola.

**Compiti** (slide *Homework*, SD-06 @ 00:49:22): finire di leggere il **capitolo 4**, *Content: The What of Social Media*, di *Social Media Data Mining and Analytics*, che tratta il contenuto condiviso dagli utenti, tipicamente testo.

Con questo si chiude la parte di Natural Language Processing (SD-06 @ 00:49:53). La lezione prosegue con la sentiment analysis supervisionata: capitolo 06.

---

## Glossario

| Termine | Significato nel corso |
|---|---|
| Text similarity | grado in cui due documenti trattano un argomento comune |
| Document clustering | raggruppamento di documenti simili |
| Singleton (standalone) cluster | cluster di un solo elemento, stato iniziale del clustering agglomerativo |
| Clustering gerarchico agglomerativo | fonde ripetutamente i due cluster più vicini fino a uno solo |
| Average / single / complete linkage | distanza fra cluster come media / minimo / massimo delle distanze fra coppie |
| Cosine similarity | prodotto scalare dei vettori normalizzati, coseno dell'angolo fra di essi |
| Distanza coseno | d = 1 - S |
| Dendrogramma | albero binario delle fusioni; foglie = documenti, altezze = distanze di fusione |
| Merging height | distanza a cui avviene una fusione; N - 1 per N documenti |
| Cut height | altezza a cui si taglia il dendrogramma per ottenere i cluster |
| Topic extraction | mappare testo ad alta dimensionalità in pochi temi (many-to-one) |
| String matching | confronto delle parole così come sono scritte |
| Topic | distribuzione di probabilità sulle parole; in output, lista delle parole più probabili |
| Distributional hypothesis | parole in contesti simili hanno significato simile |
| Sinonimia / polisemia | parole diverse con lo stesso significato / stessa parola con significati diversi |
| pLSA, LDA, DTM, BERTopic | modelli di topic modeling (Hofmann 1999, Blei et al. 2003, Blei & Lafferty 2006, Grootendorst 2022) |
| Plate notation | rettangoli che indicano variabili replicate nel modello grafico |
| θ (theta) | per-document topic distribution, parametro α |
| β (beta) | per-topic word distribution |
| z | topic assegnato a una posizione di parola |
| Gibbs sampling | metodo di campionamento usato per l'inferenza di LDA |
| Soft / hard clustering | un documento in più cluster / in un solo cluster |

## Punti incerti

- **SD-06 @ 00:40:14:** "al 50% che parlo di politica, al 30% di geografia e al **3%** di religione" (Whisper, confidenza buona). Con la slide (20%) e con le 2 palline blu dette subito dopo, è quasi certamente un lapsus o un errore di trascrizione per 20%. Ho scritto 20% con [?].
- **SD-06 @ 00:20:05:** "come Star Wars, Star Trek, Ing": i tag minori del cluster B sono leggibili solo in parte nella slide (*star-wars*, *star-trek-voyager*, *star-trek-enterprise*, uno illeggibile, forse *star-trek-tng*).
- **SD-06 @ 00:16:13:** "Remember, Remember, che sta per Remembery": la word cloud mostra il termine stemmato "rememb".
- **Slide K = 3, topic 2:** la slide scrive "county", la lezione legge "country". Probabile refuso nella slide: con *rain, flooding, people* è plausibile *country*, ma l'output reale di LDA potrebbe contenere davvero *county*.
- **Video contro PDF:** le slide del video sono una versione leggermente precedente dello stesso deck. Le differenze sono solo di forma: "It's called 'cosine'..." invece di "It is called 'cosine similarity'..."; nella slide *Computing Similarity* il video ha "removing stopwords, stemming, lemmatization" senza "for dimensionality reduction".
- **Termini corretti in silenzio dalla trascrizione:** LDE → LDA, "Latent Dirigely/Dirigere a Location" → Latent Dirichlet Allocation, "GIF sampling" → Gibbs sampling, "Hoffman" → Hofmann, "Bly" → Blei, "Probabilistic Lathe/Lethal Semantic Analysis" → pLSA, "ShakeItLearn" → scikit-learn, "Work Cloud"/"workload" → word cloud, "dendogramma" → dendrogramma, "vikmi" → victims, "aggromerativo" → agglomerativo.
- Segmenti a bassa confidenza: uno solo sopra soglia (-0.319, SD-06 @ 00:34:52, frase su LDA e pLSA), con i nomi storpiati ma il contenuto confermato dalla slide.

## Materiale usato

- Video: `video/SD-06.mp4`, trascrizione `out/SD-06/SD-06-trascrizione.md` fino a 00:49:53; frame `out/SD-06/frames/` da 00:00:10 a 00:49:37; `SD-06-ocr-indice.json` come indice
- Slide: `Materiale/Portale/estratti/5_TextSimilarity_SDA25.pdf`; confronto con `Materiale/Teams/estratti/Slides/5_TextSimilarity_SDA26.pdf`
- Libro: `Materiale/Portale/estratti/books/Social Media Data Mining and Analytics.pdf`, capitolo 4 (pp. 129-153)
- Teams (solo citato): `Materiale/Teams/estratti/Tutorials/topic_modeling_Gensim_BERTopic/`, `Slides/0_General_Info_SDA26.pdf` (traccia #SDA3)
- Verifica: `verifica_sd05.py`, `verifica_sd05_output.txt` (numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1)
