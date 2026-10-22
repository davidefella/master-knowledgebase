# Capitolo 04: Natural Language Processing

**Lezioni:** SD-04 (1:47:06) e SD-05 (0:38:55), Dott.ssa Ida Mele, IASI-CNR
**Slide:** `4_NLP_SDA25.pdf` (64 pagine, quelle del video); versione Teams `4_NLP_SDA26.pdf` con le stesse 64 pagine e poche differenze, elencate in [divergenze](divergenze.md)
**Notebook:** `NLP_withNLTK_tutorial.ipynb`, `NLP_withSpacy_tutorial.ipynb`, dati `Natural_Language_Processing_Text.txt` (portale 2025; versioni 2026 su Teams, diff cella per cella nel file divergenze). Il codice del capitolo viene dal notebook 2025, quello mostrato a lezione; tutti i blocchi sono stati rieseguiti (copie eseguite in questa cartella).
**Riferimento:** capitolo 4 *Content: The What of Social Media* del libro [1] *Social Media Data Mining and Analytics* (Szabo, Polatkan, Boykin, Chalkiopoulos, Wiley 2019). Le slide coprono la parte iniziale del capitolo (feature dal testo, distribuzione dei termini, tf-idf); la seconda parte del capitolo del libro (similarità coseno, clustering gerarchico, popolarità dei topic, topic modeling) è materia del capitolo 05 della guida.
**Fonti 2026:** Teams 4 (06/10/2026, lezione live su NLP, 1:44), l'unica registrazione Teams 2026 con trascrizione italiana leggibile. Ripete quasi alla lettera SD-04 e la prima parte di SD-05: le poche aggiunte sono nei riquadri "Integrazione Teams 2026". Per il I livello programma e materiale sono quelli del 2025 (Teams 4 @ 0:02:44).

## Indice

1. [Che cos'è il Natural Language Processing](#1-che-cosè-il-natural-language-processing)
2. [Perché è difficile: ambiguità e contesto](#2-perché-è-difficile-ambiguità-e-contesto)
3. [Approcci: basati su regole e statistici](#3-approcci-basati-su-regole-e-statistici)
4. [Componenti e sfide](#4-componenti-e-sfide)
5. [Strumenti: NLTK, spaCy e altri](#5-strumenti-nltk-spacy-e-altri)
6. [Contenuto generato dagli utenti e terminologia](#6-contenuto-generato-dagli-utenti-e-terminologia)
7. [Preprocessing I: tokenizzazione](#7-preprocessing-i-tokenizzazione)
8. [Preprocessing II: punteggiatura, stopword, frequenze, WordCloud](#8-preprocessing-ii-punteggiatura-stopword-frequenze-wordcloud)
9. [Preprocessing III: stemming e lemmatizzazione](#9-preprocessing-iii-stemming-e-lemmatizzazione)
10. [Part-of-Speech tagging](#10-part-of-speech-tagging)
11. [Chunking](#11-chunking)
12. [Named Entity Recognition](#12-named-entity-recognition)
13. [WordNet: significati, sinonimi, iponimi, similarità](#13-wordnet-significati-sinonimi-iponimi-similarità)
14. [Bag-of-words e CountVectorizer](#14-bag-of-words-e-countvectorizer)
15. [Distribuzione delle frequenze dei termini](#15-distribuzione-delle-frequenze-dei-termini)
16. [TF-IDF](#16-tf-idf)
17. [Il tutorial con spaCy](#17-il-tutorial-con-spacy)
18. [Riepilogo e compiti](#18-riepilogo-e-compiti)

---

## 1. Che cos'è il Natural Language Processing

*SD-04 @ 00:00:09*

Il **linguaggio naturale** è quello che gli umani usano per comunicare: l'italiano in cui parla Mele, l'inglese delle slide, lo spagnolo o il tedesco se si viaggia. Si dice "naturale" per distinguerlo dai linguaggi di programmazione come Python e Java (SD-04 @ 00:06:28). Il **text mining** invece non guarda al tipo di sequenza: si applica a bit, DNA, proteine come a parole; l'NLP si occupa specificamente di sequenze di parole usate dagli umani.

Perché serve: molto del contenuto condiviso dagli utenti è testo (post, status update, articoli di Wikipedia, ma anche tag e commenti sotto le immagini). Le macchine lavorano bene con dati **strutturati** (numeri, tabelle, fogli di calcolo), le persone comunicano con dati **non strutturati** (parole e frasi). L'NLP è l'insieme di tecniche che riduce questo divario: l'obiettivo è aiutare la macchina a "leggere" il testo **simulando** la capacità umana di comprenderlo.

La slide colloca l'NLP all'intersezione di tre aree: **informatica**, **intelligenza artificiale** (perché si usano tecniche di machine learning e deep learning, SD-04 @ 00:07:35) e **linguaggio umano**.

La lezione anticipa la pipeline che il capitolo seguirà (SD-04 @ 00:01:30):

1. **preprocessing**: tokenizzazione (spezzare il testo in parole), pulizia da caratteri speciali e da parole molto frequenti (stopword), **riduzione della dimensionalità** con stemming e lemmatizzazione, che riportano le parole a una forma base;
2. **analisi**: part-of-speech tagging (una sorta di analisi grammaticale), individuazione dei *noun chunk* (gruppi di parole che esprimono un unico concetto, come *beautiful young lady* o *natural language processing*), riconoscimento delle *named entity* (persone, luoghi, brand come Samsung, modelli di prodotto);
3. **rappresentazione**: il documento diventa un vettore di numeri, con il modello **bag-of-words** (conta quante volte compare ogni parola, ignorando la posizione) e con **TF-IDF**, che pesa anche quanto una parola è discriminativa nella collezione (SD-04 @ 00:04:12).

### Applicazioni

*SD-04 @ 00:08:12*

| Applicazione | Come la descrive la lezione |
|---|---|
| Text understanding | simulare la comprensione del testo: l'applicazione principale |
| Information extraction (IE) | recupero di informazioni da dati **strutturati** (knowledge graph, ontologie) o **semistrutturati** (pagine con metadati, come molte pagine di Wikipedia) |
| Information retrieval (IR) | recupero da **testo libero** (PDF, HTML): Google, Bing, Yandex |
| Question answering | chatbot: domanda in linguaggio naturale, risposta in linguaggio naturale |
| Conversational system | la domanda si pone a voce, a uno smartphone o a un home assistant come Amazon Alexa ("qual è il programma in televisione stasera?") |
| Speech recognition | la voce, un'onda sonora, viene trascritta e passata al sistema di question answering |
| Text summarization | il paragrafo conciso di ChatGPT, lo snippet generato dall'AI che Google mette sopra la lista dei risultati: sintesi da più fonti per chi va di fretta |
| Translation | il viaggio in un paesino della Malesia, lontano dalle città dove si parla inglese |
| Spelling correction, autocompletion | completano parole e ormai intere frasi nelle mail; devono fare un'analisi grammaticale (dopo un soggetto viene probabilmente un verbo) |
| Named entity recognition | sezione 12 |
| Sentiment analysis | testo che esprime o no un'opinione, positiva, negativa o neutra verso un'entità: capitolo 06 |

> **Integrazione Teams 2026:** fra le applicazioni Mele aggiorna gli esempi al 2026: gli assistenti vocali in casa e sul telefono ("quando passa il prossimo autobus per il centro") e il riassunto generato con AI generativa che Google mostra sopra i risultati, costruito su 3-4 fonti ritenute più autorevoli, al posto della sola lista di link ordinata per rilevanza. Lo collega alla *text summarization* e al successo degli LLM. Aggiunge anche il *text autocompletion* della tastiera (Teams 4 @ 0:07:30-0:09:50).

Sul confine fra IE e IR Mele fa l'esempio dei motori di ricerca: cercando un personaggio famoso compare a destra un riquadro con luogo e data di nascita, età e, per un attore, film, colleghi, coniuge, figli. Sono dati presi da un knowledge graph, quindi information extraction affiancata al classico retrieval (SD-04 @ 00:08:52).

---

## 2. Perché è difficile: ambiguità e contesto

*SD-04 @ 00:14:17*

L'NLP è un approccio **non deterministico**, basato su probabilità: la stessa parola cambia significato con il contesto e con l'interpretazione. Se fosse deterministico, lo stesso testo avrebbe sempre la stessa interpretazione, mentre ciò che va bene per una persona in un contesto può non andare bene per un'altra in un altro (slide *Motivation*).

**Pesca e pesca.** In italiano "pèsca" (frutto) e "pésca" (l'atto di pescare) si distinguono a voce, non per iscritto. Per un umano il contesto basta: "ieri ho mangiato una pesca ed era buonissima" contro "ieri mio zio è andato a pesca". Per la macchina è molto più difficile (SD-04 @ 00:14:53).

**Ambiguità anche per gli umani.** *I saw a man on a hill with a telescope*: senza virgole né altro contesto ha quattro interpretazioni ugualmente valide (SD-04 @ 00:15:34):

| | Dove sono io | Dove è l'uomo | Chi ha il telescopio |
|---|---|---|---|
| 1 | non specificato | sulla collina | io, lo guardo con il telescopio |
| 2 | non specificato | sulla collina | lui |
| 3 | sulla collina | non specificato | io |
| 4 | sulla collina | non specificato | lui |

**Can you help me with the can?** Il primo *can* è il verbo modale, il secondo è il nome "lattina". Per la macchina sono due sequenze di caratteri identiche: un confronto solo lessicale non le distingue. Il PoS tagging (sezione 10) le separa perché il primo precede un soggetto e il secondo segue un articolo (SD-04 @ 00:17:15).

> **Nota aggiunta:** l'esempio è stato verificato per esecuzione. Il tagger di spaCy (`en_core_web_sm` 3.8.0) assegna `MD` al primo *can* e `NN` al secondo; il tagger di default di NLTK (`nltk.pos_tag`, NLTK 3.10.4) li tagga **entrambi** `MD`, cioè sbaglia proprio il caso usato come esempio. Vedi `verifica_sd04.py`, sezione 2.

---

## 3. Approcci: basati su regole e statistici

*SD-04 @ 00:18:15*

**Rule-based NLP.** Usa regole di *common sense*: una temperatura da congelamento può uccidere, il caffè caldo versato sulla pelle può ustionare. Scrivere regole per tutte le parole di una lingua e per tutti i loro significati richiede moltissimi esperti e moltissimo tempo, e andrebbe rifatto per ogni dominio (una parola ha un significato in medicina e un altro in informatica) e per ogni lingua (SD-04 @ 00:18:53).

> **Integrazione Teams 2026:** sugli approcci statistici aggiunge che nelle reti neurali capire dov'è l'errore è "praticamente impossibile": per questo esiste un'area di ricerca, la *Explainable AI*, che studia perché un modello si comporta in un certo modo e perché è soggetto ad allucinazioni. E precisa che il modello non comprende il contesto: lo simula grazie alla capacità di rilevare pattern (Teams 4 @ 0:15:00 circa).

**Statistical NLP.** Si allenano modelli di machine learning o deep learning su grandi quantità di dati e il modello impara le regole da solo. Se ha visto abbastanza esempi e i parametri sono ben impostati, i risultati sono buoni: un PoS tagger riconosce che il primo *can* è un verbo e l'ultimo un nome. Una piccola *ground truth* etichettata serve a validare il modello, cioè a controllare che i valori predetti corrispondano alla realtà. Nella descrizione di Mele il training avviene su dati **non etichettati**: si scaricano tutti gli articoli di Wikipedia o moltissimi tweet, e lo sforzo si riduce a costruire il dataset (SD-04 @ 00:19:26).

> **Correzione:** la lezione presenta l'NLP statistico come apprendimento "completamente unsupervised". Non è sempre così. Molti modelli statistici classici sono **supervisionati**: il tagger usato da `nltk.pos_tag` è un perceptron addestrato su corpora annotati a mano con i tag (Penn Treebank), e anche i modelli `en_core_web_*` di spaCy sono addestrati su corpora annotati. L'addestramento su grandi quantità di testo non etichettato è tipico del pre-training dei modelli linguistici (word embedding, Transformer), che poi spesso si specializzano con dati etichettati.

La slide *Approach Comparison* (Figure 4: Rule-Based NLP vs. Statistical NLP):

| | Rule-based NLP | Statistical NLP |
|---|---|---|
| **Pro** | flessibile: si aggiungono o tolgono regole | scala facilmente |
| | facile da debuggare: si vede dove sta l'errore | impara da solo |
| | non richiede molto training | sviluppo rapido: basta cambiare collezione (Wikipedia italiana invece di quella inglese, documenti legali invece di un'enciclopedia) e riallenare |
| | comprensione del linguaggio | alta copertura |
| | alta precisione, ma solo se le regole sono di qualità | |
| **Contro** | servono sviluppatori esperti, affiancati da linguisti computazionali | servono grandi quantità di dati |
| | parsing lento: per ogni parola vanno verificate molte regole, e su un dataset enorme il tempo esplode | difficile da debuggare: una rete neurale è una scatola nera; nel machine learning si può lavorare sulle feature, nel deep learning dopo il fine-tuning non si capisce perché alcuni esempi funzionano e altri no |
| | copertura moderata: regole per l'italiano nel dominio informatico non valgono per altre lingue o per il dominio legale o medico | nessuna comprensione del contesto |

L'ultimo punto (SD-04 @ 00:24:49): i modelli probabilistici **simulano** la comprensione grazie alla co-occorrenza delle parole, ma non capiscono davvero il contenuto semantico; "non è che veramente la macchina capisce che *can* è la lattina". Lo stesso vale per il topic modeling (capitolo 05).

---

## 4. Componenti e sfide

*SD-04 @ 00:25:22*

| Componente | Che cosa fa | Esempio della lezione |
|---|---|---|
| 1. **Analisi lessicale** | divide il testo in paragrafi, frasi e parole e ne analizza la struttura | |
| 2. **Analisi sintattica** | analizza la grammatica e come le parole sono disposte e legate fra loro | |
| 3. **Analisi semantica** | (simula di) capire il significato esatto delle parole; verifica che la frase abbia senso | *play*: "giocare" in *I play soccer*, "suonare" in *I play guitar*, "interpretare" per un attore, "far girare" in *I play the CD*; come nome un'opera teatrale. *Hot ice-cream* non passa l'analisi |
| 4. **Discourse integration** (coreference resolution) | un pronome rimanda a qualcosa citato prima; il tool sostituisce il pronome con il nome | *John is a computer scientist. He works at Google.* → *he* = John |
| 5. **Analisi pragmatica** | interpreta la frase in base alla situazione | l'ossimoro *hot ice cream* in poesia; sarcasmo e comicità; un cartone animato in cui il gatto parla con il cane, o *Cars*, dove le macchine parlano |

Sulla coreference (SD-04 @ 00:28:28): un umano non ripete mai "John, John, John", per questo esistono i pronomi; la macchina però ha bisogno che vengano risolti per collegare le frasi.

> **Correzione:** la slide (2025 e 2026) e la lezione chiamano il quarto componente *Disclosure Integration*. Il termine corretto è ***Discourse** Integration*: l'integrazione del discorso, cioè il legame di una frase con quelle che la precedono.

### Le sfide

*SD-04 @ 00:30:11*

- trasformare il testo, dato non strutturato, in dato **strutturato** facile da processare;
- spezzare le frasi in token (**tokenizzazione**);
- costruire un **vocabolario** (o dizionario) con le parole più significative;
- **PoS tagging**: riconoscere nomi, verbi, pronomi;
- capire il contesto e risolvere l'ambiguità;
- estrarre il significato semantico, anche con l'aiuto del PoS tagging (il *can* verbo e il *can* nome);
- **named entity recognition**: *John* è una named entity.

---

## 5. Strumenti: NLTK, spaCy e altri

*SD-04 @ 00:31:56*

| | NLTK (Natural Language Toolkit) | spaCy |
|---|---|---|
| Link | https://www.nltk.org/ | https://spacy.io/ |
| Uso tipico | didattica e ricerca accademica, raramente in produzione | industria; Mele cita aziende come Meta che fanno ricerca su dati social |
| Funzionalità | tokenizzazione, PoS tagging, NER, classificazione, sentiment analysis, pacchetti per chatbot | tokenizzazione, PoS, NER, classificazione, sentiment analysis, dependency parsing, word vectors |
| Pro | molto conosciuto, molte lingue | veloce, facile da imparare e usare, training basato su reti neurali, molte lingue |
| Contro | ignora il contesto, lento, nessun modello neurale ("non usa modelli sofisticati come Hugging Face Transformers") | poco flessibile perché basato su pipeline predefinite (la funzione `nlp`); può richiedere molta memoria con modelli grandi |

> **Integrazione Teams 2026:** nel 2026 il corso estende l'NLP solo per il master di **II livello**: LDA con Gensim e i Transformer, in particolare BERT, oltre a NLTK e spaCy (Teams 4 @ 0:20:40 circa). Il materiale relativo (`7_DL_SDA26_II_level.pdf`, tutorial RoBERTa, LDA_Gensim, BERTopic) è fuori dal perimetro di questa guida.

Sulla flessibilità di spaCy (SD-04 @ 00:33:45): con una sola chiamata a funzione si ottiene una pipeline che pulisce e preprocessa il testo. Per questo è diventato popolare fra i linguisti computazionali non informatici, ma è poco adatto alla didattica e all'informatico "purista" che vorrebbe mettere mano alla pipeline.

Altri strumenti: **Gensim** (topic modeling), **TextBlob** (sentiment analysis), **Hugging Face Transformers** (modelli preallenati basati su Transformer) e, per Java, **Stanford CoreNLP**. "Se siete abituati a usare Java, questo tool vi potrà essere utile" (SD-04 @ 00:35:01).

> **Nota aggiunta:** l'affermazione che Meta usi spaCy non è stata verificata. Le versioni usate per rieseguire i tutorial sono NLTK 3.10.4, spaCy 3.8.16 con `en_core_web_sm` 3.8.0, scikit-learn 1.9.1, wordcloud 1.9.6, Python 3.13 (la docente usava Python 3.12.2 nel 2025 e 3.10.20 nel 2026).

---

## 6. Contenuto generato dagli utenti e terminologia

*SD-04 @ 00:35:01*

Dei tre ingredienti dei social media (capitolo 01: utenti, connessioni, contenuto generato dagli utenti) qui conta il terzo, che è tipicamente testo:

> **Integrazione Teams 2026:** a voce aggiunge che "il 90% del web è rappresentato da testo" (Teams 4 @ 0:21:30 circa), dato citato senza fonte. Il resto della sezione coincide con il 2025.

- status update (Facebook, X);
- review di prodotti e servizi (Amazon, Yelp);
- articoli di blog (LiveJournal);
- domande e risposte nei forum (Quora, Stack Exchange);
- commenti sotto foto (Instagram, Flickr) e video (YouTube).

Perché interessa a un data analyst (SD-04 @ 00:36:13), con le tre domande che sono anche quelle del capitolo 4 del libro:

1. **di che cosa parlano le persone?** Individuare i *trend emergenti*, per esempio dai tweet pubblicati oggi su X;
2. **come classificare gli argomenti?** Il *topic modeling* definisce l'argomento di un testo con un certo grado di accuratezza; essendo un modello probabilistico, può sbagliare;
3. **quanto sono popolari i topic e come sono legati fra loro?** Si quantifica la popolarità, si studiano le relazioni e la distribuzione delle frequenze.

**Esempio Stack Exchange** (SD-04 @ 00:37:21). Stack Exchange è una rete di siti di domande e risposte su temi diversi, nata come estensione di Stack Overflow, il forum dove i programmatori si scambiano soluzioni. Il post della slide (*What science fiction novels have well developed alien languages?*, dalla sezione Science Fiction & Fantasy) mostra la struttura di un contenuto generato dagli utenti:

| Campo | Significato |
|---|---|
| Title | la domanda |
| Post body text | il testo |
| Vote count | 16: voti degli utenti |
| Favorite count | 3: quante volte è stato salvato tra i preferiti |
| Tags | `novel`, `languages`: definiti a mano, dicono di che cosa tratta il testo senza leggerlo |
| Edit time | timestamp dell'ultima modifica: permette un'analisi temporale |
| Author | l'autore |

### Terminologia

*SD-04 @ 00:39:04*

| Termine | Definizione |
|---|---|
| **Corpus** | collezione di documenti: tutte le pagine di Wikipedia, tutti gli articoli di news |
| **Documento** | qualunque pezzo di testo: un post, un tweet, un articolo, una review |
| **Vocabolario / dizionario** | le parole estratte dai documenti (con tokenizzazione e stemming), quelle che riteniamo significative |
| **Stopword** | parole che portano poco significato e compaiono ovunque: *and*, *of*, *just*, *because*. Servono agli umani come connettori grammaticali; di solito si rimuovono nel preprocessing |

Fra le stopword Mele mette congiunzioni (*and*, *or*; in italiano *e*, *o*, *oppure*), preposizioni (*per*), spesso aggettivi poco informativi (*many*, *much*) e pronomi personali. I pronomi, però, vanno eliminati **dopo** la coreference resolution, altrimenti si perdono i collegamenti nella frase (SD-04 @ 00:40:48). La slide mostra una word cloud delle stopword inglesi, dove *of*, *to*, *in*, *that* sono le più grandi.

### Document-term matrix

*SD-04 @ 00:41:53*

Righe = documenti $D_1 \dots D_n$, colonne = termini $T_1 \dots T_t$; l'elemento $w_{ij}$ (nella figura: indice del termine, poi del documento) dice quante volte il termine $T_i$ compare nel documento $D_j$. Quindi $w_{21}$ è il numero di occorrenze di $T_2$ in $D_1$, $w_{22}$ quello di $T_2$ in $D_2$.

```
         T1    T2   ...  Tt
  D1    w11   w21   ...  wt1
  D2    w12   w22   ...  wt2
  ...
  Dn    w1n   w2n   ...  wtn
```

Si analizzano solo le frequenze, non le posizioni né le co-occorrenze. La matrice è molto **sparsa**: il vocabolario è grande e la maggior parte delle parole non compare nella maggior parte dei documenti.

> **Nota aggiunta:** in scikit-learn, che il capitolo usa nella sezione 14, la matrice ha la stessa orientazione (righe = documenti, colonne = termini) ed è restituita in formato sparso (`scipy.sparse`); `.toarray()` la converte in densa, cosa che su un corpus reale non conviene fare.

### Bag-of-words e step di un progetto sul testo

*SD-04 @ 00:42:53*

Il **bag-of-words** tratta un testo come una "busta" di parole con le rispettive frequenze: si perdono ordine, contesto e coesione grammaticale, si tiene traccia della frequenza. Come in ogni progetto data-driven (capitolo 01):

1. raccolta dei dati (API o dataset scaricato);
2. preprocessing: tokenizzazione; rimozione di punteggiatura, caratteri speciali e stopword; stemming o lemmatizzazione;
3. analisi: PoS tagging, NER;
4. conclusioni e visualizzazione.

---

## 7. Preprocessing I: tokenizzazione

*SD-04 @ 00:44:04*

Tokenizzazione e pulizia sono passi fondamentali: senza, i dati sono rumorosi (*noisy*) e l'analisi dà cattivi risultati. **Tokenizzare** significa dividere un documento in pezzi, frasi o parole. Sembra facile, per la macchina non lo è. L'esempio della slide, *Let's tokenize! Isn't this easy?* (fonte: blog FloydHub):

| Strategia | Token |
|---|---|
| sugli spazi | `Let's` `tokenize!` `Isn't` `this` `easy?` |
| sulla punteggiatura | `Let` `'` `s` `tokenize` `!` `Isn` `'` `t` `this` `easy` `?` |
| con regole (NLTK) | `Let` `'s` `tokenize` `!` `Is` `n't` `this` `easy` `?` |

Con gli spazi, *tokenize* e *tokenize!* finirebbero nel vocabolario come due parole diverse. La tokenizzazione basata su regole è la migliore: separa *Let* dalla contrazione *'s* e *Is* da *n't*. Le regole sono già implementate nei tool, "ci vengono gratis" (SD-04 @ 00:45:41).

> **Nota aggiunta:** riga "spazi" e riga "regole" verificate per esecuzione (`str.split()` e `nltk.word_tokenize`, `verifica_sd04.py` sezione 1); la riga "punteggiatura" è riportata dalla slide.

Esempio delle slide (non è nel notebook), con `word_tokenize` e con un tokenizer a espressione regolare (SD-04 @ 00:46:15):

```python
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer

example = "This is an example sentence! However, it isn't a very informative one"

print(word_tokenize(example, language='english'))
# ['This', 'is', 'an', 'example', 'sentence', '!', 'However', ',', 'it', 'is', "n't", 'a', 'very', 'informative', 'one']

tokenizer = RegexpTokenizer(r'\w+')
print(tokenizer.tokenize(example))
# ['This', 'is', 'an', 'example', 'sentence', 'However', 'it', 'isn', 't', 'a', 'very', 'informative', 'one']
```

`word_tokenize` va chiamata con la lingua. Mantiene virgola e punto esclamativo, perché la punteggiatura non è ancora stata rimossa. `RegexpTokenizer(r'\w+')` prende solo sequenze di caratteri "di parola" e scarta la punteggiatura, ma spezza *isn't* in `isn` e `t`. Mele preferisce il primo: la contrazione `n't` si risolve facilmente in un secondo passaggio, e almeno il verbo è separato. Con un'espressione regolare migliore anche il secondo può gestire *isn't*; in generale `word_tokenize`, disponibile per molte lingue, "fa molto bene" (SD-04 @ 00:48:01).

### Il tutorial NLTK: dati e setup

*SD-04 @ 00:53:07*

Il notebook è l'adattamento di un tutorial di Towards AI (link a Colab e GitHub nella prima cella). Mele usa Python 3.12, richiesto da altre librerie che usa; va bene qualunque Python 3. Consiglia di eseguire le prime celle (`pip install` di `nltk`, `matplotlib`, `wordcloud`), anche da terminale, per trovarsi tutto installato. Il file di testo si può scaricare con `wget`, se lo si ha, oppure prendere dal materiale del corso; in quel caso la cella va commentata (SD-04 @ 00:54:11).

```python
#Open the text file :
text_file = open("Natural_Language_Processing_Text.txt")

#Read the data :
text = text_file.read()

#Print the text:
print(text + "\n")

#Length of the text:
print ("Text Length: "+str(len(text))+"\n")

#Datatype of the data:
print ("Data Type: "+str(type(text))+"\n")
```

```
Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.

The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. [...]

Text Length: 675

Data Type: <class 'str'>
```

È un estratto della favola dei tre porcellini, 675 caratteri, di tipo stringa.

> **Nota aggiunta:** il file pesa 679 byte ma `len(text)` dà 675 perché contiene quattro `\r` (fine riga Windows) che `open()` in modalità testo converte. Verificato in `verifica_sd04.py`, sezione 7.

```python
import nltk

from nltk import sent_tokenize
from nltk import word_tokenize

nltk.download("popular")
```

`nltk.download("popular")` scarica la collezione dei pacchetti di dati più usati (stopword, WordNet, tagger, chunker...).

> **Nota aggiunta:** con NLTK 3.10.4 dietro un proxy HTTP, `nltk.download` rifiuta di scaricare e restituisce `False` a meno di impostare la variabile d'ambiente `NLTK_ALLOW_PROXIED_URLOPEN=1`: è quanto è servito per rieseguire il notebook nel container. Sul proprio portatile, senza proxy, la cella funziona così com'è.

### Sentence e word tokenization

*SD-04 @ 00:48:35*

```python
#Tokenize the text by sentences:
sentences = sent_tokenize(text)

#Print the sentences:
print(sentences)

#How many sentences?
print ("\nNumber of sentences: "+str(len(sentences))+"\n")
```

```
['Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them.', 'So when they were old enough, she sent them out into the world to seek their fortunes.', 'The first little pig was very lazy.', "He didn't want to work at all and he built his house out of straw.", [...] 'It looked like it could withstand the strongest winds.']

Number of sentences: 9
```

`sent_tokenize` restituisce una lista in cui ogni elemento è una frase; con `word_tokenize` ogni elemento è una parola.

```python
#Tokenize the text with words:
words = word_tokenize(text)

#Print words:
print (words)

#How many words?
print ("\nNumber of words: "+str(len(words))+"\n")
```

```
['Once', 'upon', 'a', 'time', 'there', 'was', 'an', 'old', 'mother', 'pig', 'who', 'had', 'three', 'little', 'pigs', 'and', 'not', 'enough', 'food', 'to', 'feed', 'them', '.', 'So', [...] 'He', 'did', "n't", 'want', [...] 'the', 'strongest', 'winds', '.']

Number of words: 144
```

I token sono 144, ancora con punteggiatura e stopword (SD-04 @ 00:55:20).

---

## 8. Preprocessing II: punteggiatura, stopword, frequenze, WordCloud

### Distribuzione delle frequenze sul testo grezzo

*SD-04 @ 00:55:59*

```python
#Import required libraries:
from nltk.probability import FreqDist

#Find the frequency:
fdist = FreqDist(words)

#Print 10 most frequent terms:
fdist.most_common(10)
```

```
[('.', 9), ('and', 7), ('little', 5), ('a', 4), ('was', 4), ('pig', 4), ('the', 4), ('house', 4), ('to', 3), ('out', 3)]
```

```python
#Plot the most frequent terms computed with fdist:

#Import required libraries:
import matplotlib.pyplot as plt

# setting the plot size
plt.figure(figsize=(6, 3))  

#plotting top-10 words
fdist.plot(10) 
```

Il grafico (asse x le parole, asse y i conteggi) mostra una discesa repentina che ricorda una **power law**, anche se con così poche parole, e sporche, "è quasi inutile dirlo" (SD-04 @ 00:56:29). I dati sono sporchi: in testa c'è il punto, seguito da stopword.

### Rimozione della punteggiatura

*SD-04 @ 00:49:44*

`str.isalpha()` restituisce `True` se la stringa contiene solo lettere: è il test usato per scartare i token con caratteri speciali (`, . : ; - / ' "`).

```python
#examples with "apple", "email@" and "..."

w1 = "apple"
if w1.isalpha():
    print(w1+" does not have special chars")
else:
    print(w1+" has special chars") 
    
w2 = "email@"
if w2.isalpha():
    print(w2+" does not have special chars")    
else:
    print(w2+" has special chars")    

w3 = "..."
if w3.isalpha():
    print(w3+" does not have special chars")    
else:
    print(w3+" has special chars")  
```

```
apple does not have special chars
email@ has special chars
... has special chars
```

In alternativa si usano le espressioni regolari (SD-04 @ 00:57:37):

```python
#Regular expressions can be used to remove special chars from a string 

import re

text_with_special_chars = "email@-:."

# Use re.sub() to replace special characters with an empty letter
#The regular expression [^\w\s] matches any character that is not a word character 
#(\w includes letters, digits, and underscores) or a whitespace character (\s)
#The ^ inside the square brackets negates the character class, meaning it matches any character that is not in the specified set

cleaned_text = re.sub(r'[^\w\s]', '', text_with_special_chars) 

# Print the cleaned string
print(cleaned_text)
```

```
email
```

`[^\w\s]` è la classe negata: qualunque carattere che non sia alfanumerico o underscore (`\w`) né spazio (`\s`). Sostituendolo con la stringa vuota, da `email@-:.` resta `email`.

Applicato al testo, con conversione in minuscolo per non avere *The* e *the* come parole distinte nel dizionario:

```python
#let's remove special chars from the example text 

#Empty list to store words:
words_no_punc = []

#Removing punctuation marks :
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

#Print the words without punctution marks :
print (words_no_punc)

#Length:
print ("\nLength (after removing spec chars): "+str(len(words_no_punc))+"\n")
```

```
['once', 'upon', 'a', 'time', 'there', 'was', 'an', 'old', 'mother', 'pig', [...] 'he', 'did', 'want', [...] 'the', 'strongest', 'winds']

Length (after removing spec chars): 132
```

Da 144 a 132 token. Il test `isalpha()` elimina anche `n't`, che contiene un apostrofo.

```python
#Frequency distribution:
fdist = FreqDist(words_no_punc)

fdist.most_common(10)
```

```
[('and', 7), ('the', 7), ('little', 5), ('a', 4), ('was', 4), ('pig', 4), ('he', 4), ('house', 4), ('to', 3), ('out', 3)]
```

Il punto è sparito; *and* e *the* hanno lo stesso conteggio, 7 (ora *The* e *the* sono la stessa parola). Ma sono stopword e vanno eliminate. *Little* compare 5 volte: la favola parla di *little pigs* (SD-04 @ 00:59:19).

> **Dal materiale ufficiale, non mostrato a lezione:** il notebook 2026 aggiunge, dopo la cella dell'espressione regolare, una cella che mostra `lower()` su `"Apple is a Company"` → `"apple is a company"`.

### Rimozione delle stopword

*SD-04 @ 00:50:59*

Ogni lingua ha la sua lista. La slide cita per l'italiano "io", "me", "mio", "tu", "te", "tuo", gli articoli "il", "lo", "la", "i", "gli", "le", "un", "uno", "una", poi "nessuno", "però", "per". NLTK fornisce le liste nel corpus `stopwords`; ne esistono altre, anche molto dettagliate, e si può usarne una propria (SD-04 @ 00:51:30).

```python
from nltk.corpus import stopwords

#List of stopwords
stopwords = stopwords.words("english")
print(stopwords)
```

```
['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', [...]]
```

> **Nota aggiunta:** la slide stampa `stop_words[:20]` e mostra `['i', 'me', 'my', 'myself', 'we', ...]`, l'ordine delle versioni più vecchie di NLTK. Nel notebook (2025 e 2026) e con NLTK 3.10.4 la lista è in ordine alfabetico e contiene 198 parole. Da notare anche che la cella riassegna `stopwords`: il nome del modulo importato viene sovrascritto dalla lista, quindi rieseguendo la cella una seconda volta si ottiene un `AttributeError`.

```python
#Empty list to store clean words:
clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

print(clean_words)

#Length:
print ("\nLength (after removing spec chars and stopwords): "+str(len(clean_words))+"\n")
```

```
['upon', 'time', 'old', 'mother', 'pig', 'three', 'little', 'pigs', 'enough', 'food', 'feed', 'old', 'enough', 'sent', 'world', 'seek', 'fortunes', [...] 'withstand', 'strongest', 'winds']

Length (after removing spec chars and stopwords): 65
```

Da 132 a 65 parole, tutte con contenuto semantico (SD-04 @ 01:00:25).

```python
#Frequency distribution :
fdist = FreqDist(clean_words)

fdist.most_common(10)
```

```
[('little', 5), ('pig', 4), ('house', 4), ('built', 3), ('old', 2), ('enough', 2), ('lazy', 2), ('worked', 2), ('day', 2), ('upon', 1)]
```

> **Nota aggiunta:** *pig* (4) e *pigs* restano parole distinte: è il problema che risolvono stemming e lemmatizzazione (sezione 9). *Three* resta in `clean_words` perché non è nella lista di NLTK; sarebbe invece eliminato con la lista di spaCy, che è molto più ampia (sezione 17).

### WordCloud

*SD-04 @ 00:52:34, tutorial @ 01:01:40*

Una word cloud dispone le parole a caso e le disegna tanto più grandi quanto più sono frequenti. "Fa molto scena" (SD-04 @ 01:00:58). Si genera con il pacchetto `wordcloud` e si mostra con `matplotlib.pyplot`:

```python
#Library to form wordcloud :
from wordcloud import WordCloud

#Library to plot the wordcloud :
import matplotlib.pyplot as plt

#Generating the wordcloud :
wordcloud = WordCloud().generate(text)

#Plot the wordcloud :
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud) 

#To remove the axis value :
plt.axis("off") 
plt.show()
```

Sul testo grezzo compaiono anche le stopword; sulla lista pulita la nuvola è più interessante. Le parole più grandi sono *little*, *pig*, *house*, *build*; le più piccole *bricks*, *sang*, *chimney* (slide WordCloud).

```python
#with clean text (without spec chars and stopwords)

#Library to form wordcloud :
from wordcloud import WordCloud

#Library to plot the wordcloud :
import matplotlib.pyplot as plt

clean_text=""
for clean_word in clean_words:
    clean_text = clean_text + " "+clean_word

#Generating the wordcloud :
wordcloud = WordCloud().generate(clean_text)

#Plot the wordcloud :
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud) 

#To remove the axis value :
plt.axis("off") 
plt.show()
```

> **Nota aggiunta:** `WordCloud().generate()` applica una propria lista di stopword di default (`wordcloud.STOPWORDS`) e accorpa i plurali in *s* (`normalize_plurals=True`), quindi anche la nuvola "grezza" non mostra *the* o *and*: verificato, sul testo grezzo le parole più pesanti sono *pig* e *little* (peso 1,0), poi *house* e *built*. La differenza fra le due nuvole è quindi minore di quanto suggerisca la lezione. La slide riporta *build*, ma nel testo la parola è *built*. La concatenazione `clean_text + " " + clean_word` in un ciclo equivale a `" ".join(clean_words)`, più idiomatico.

Riepilogo della pipeline (slide *Preprocessing: Example in Python*, SD-04 @ 00:52:00):

| Passo | Token | Esempio |
|---|---|---|
| testo | 675 caratteri | *Once upon a time there was an old mother pig...* |
| `word_tokenize` | 144 | `'Once', 'upon', 'a', 'time', ...` |
| `isalpha()` + `lower()` | 132 | `'once', 'upon', 'a', 'time', ...` |
| senza stopword | 65 | `'upon', 'time', 'old', 'mother', 'pig', ...` |

---

## 9. Preprocessing III: stemming e lemmatizzazione

### Stemming

*SD-04 @ 01:02:12*

Lo **stemming** riduce una parola al suo *stem* ("stelo"): collassa le varianti flesse su una radice, che non è detto sia una parola del vocabolario. Esempio della slide (Fox 2018): *consult*, *consultant*, *consulting*, *consultative*, *consultants* → *consult*. Il testo diventa meno leggibile per gli umani ma più confrontabile per la macchina.

Lo scopo è **ridurre la dimensionalità del vocabolario** senza perdere il significato: i plurali collassano sul singolare, le forme verbali sulla forma base. Ne guadagna la matrice documento-termine, che diventa meno sparsa (SD-04 @ 01:04:56).

Stemmer citati: **Porter**, **Snowball**, **Lancaster**. Porter e Snowball danno una buona approssimazione; altri approcci tagliano troppo presto (*overstemming*) e diventa difficile capire la parola originale. Lingue diverse hanno grammatiche diverse, quindi serve uno stemmer per lingua.

Esempi della slide: *changing*, *changed*, *change* → *chang*, che un correttore ortografico sottolineerebbe; *studying*, *studies*, *study* → *studi*, con la *i* al posto della *y* (SD-04 @ 01:03:52).

> **Correzione:** a SD-04 @ 01:03:22 la lezione dice che con lo stemming *I was, you were, I am, you are* collassano sul verbo *to be*. Lo stemming non può farlo, perché tronca suffissi e non conosce le forme irregolari: Porter dà `am`, `is`, `are`, `wa`, `were`. Ridurre *am, are, is* a *be* è compito della **lemmatizzazione** con `pos="v"` (sezione successiva), come dice correttamente la slide *Stemming vs. Lemmatization* ("am, are, is → be"). Verificato in `verifica_sd04.py`, sezione 8.

I due errori tipici:

| Errore | Che cosa succede | Esempio |
|---|---|---|
| **Overstemming** | si taglia troppo: parole con significati diversi finiscono sulla stessa radice | *university* e *universe* → *univers* (università e universo) |
| **Understemming** | si taglia troppo poco: parole che dovrebbero avere la stessa radice restano separate | *data*, *datas* → *data*, ma *datum* (la forma latina) → *datum* |

"Sono errori compiuti dagli stemmer, però non possiamo farci nulla" (SD-04 @ 01:06:03).

Il tutorial (SD-04 @ 01:27:20):

```python
#Import the stemming library PorterStemmer

from nltk.stem import PorterStemmer

porter = PorterStemmer()

#Word-list for stemming:
word_list = ["Study","Studying","Studies","Studied"]

for w in word_list:
    print(porter.stem(w))

print("\n********\n")

#Word-list for stemming :
word_list_2 = ["studies","leaves","decreases","plays"]

for w in word_list_2:
    print(porter.stem(w))
```

```
studi
studi
studi
studi

********

studi
leav
decreas
play
```

Lo stemming tratta tutto come verbo: *leaves* diventa *leav* (da *to leave*), mai *leaf*. *Play* resta corretto solo per caso: è stata tolta la *s* (SD-04 @ 01:08:52).

```python
#examples of overstamming and understamming

from nltk.stem import PorterStemmer

porter = PorterStemmer()

#Word-list for stemming:
word_list = ["Universe", "University", "Universities", "data", "datas", "datum"]

for w in word_list:
    print(porter.stem(w))
```

```
univers
univers
univers
data
data
datum
```

Con `SnowballStemmer("english")` il notebook ripete gli stessi due esempi e l'output è identico (SD-04 @ 01:28:55):

```python
#Import the stemming library SnowballStemmer

from nltk.stem import SnowballStemmer

snowball = SnowballStemmer("english")

#Word-list for stemming :
word_list = ["Study", "Studying", "Studies", "Studied"]

for w in word_list:
    print(snowball.stem(w))
```

```
studi
studi
studi
studi
```

Allora che differenza c'è? Snowball supporta molte lingue, anche meno diffuse e con regole complesse come l'ungherese o lo svedese (SD-04 @ 01:29:37):

```python
#Print languages supported:
SnowballStemmer.languages
```

```
('arabic', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish')
```

> **Nota aggiunta:** l'italiano è supportato (`SnowballStemmer("italian")`), utile per un progetto su testo italiano. La voce `'porter'` è l'algoritmo Porter originale esposto con l'interfaccia Snowball.

### Lemmatizzazione

*SD-04 @ 01:06:37*

La **lemmatizzazione** ha lo stesso obiettivo, ma invece di troncare cerca nel dizionario la forma base (il *lemma*), che è quindi una parola scritta correttamente. Soprattutto tiene conto del **PoS tag**, con quattro scelte: verbo (`v`), nome (`n`), aggettivo (`a`), avverbio (`r`). Così distingue *studies* terza persona di *to study* da *studies* plurale di *study*, lo studio di un medico o di un osteopata. Lo stemming non considera il contesto: è più veloce ma meno accurato.

```python
from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()
word_list = ["am", "is", "are", "was", "were"]

for w in word_list:
    print(lemma.lemmatize(w, pos="v"))
```

```
be
be
be
be
be
```

```python
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('change', pos="v")) #verb
print(lemmatizer.lemmatize('changes', pos="v"))
print(lemmatizer.lemmatize('changed', pos="v"))
print(lemmatizer.lemmatize('changing', pos="v"))
print(lemmatizer.lemmatize('changing', pos="n")) #noun
```

```
change
change
change
change
changing
```

Come nome *changing* resta invariato. Come si sa a priori se è nome o verbo? Non si sa: prima si applica il PoS tagger alla frase, poi si chiama il lemmatizer con il tag trovato. Esempio di Mele: *changing room*, il camerino, dove *changing* non è un verbo (SD-04 @ 01:31:27).

```python
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('studying', pos="v")) #verb
print(lemmatizer.lemmatize('studying', pos="n")) #noun
print(lemmatizer.lemmatize('studying', pos="a")) #adjective
print(lemmatizer.lemmatize('studying', pos="r")) #adverb   
#Note that the pos = "v|n|a|r" can be decided after sentence analysis (e.g., PoS tagging)
```

```
study
studying
studying
studying
```

Solo come verbo *studying* torna alla forma base; come nome, aggettivo (*studying room*) o avverbio resta invariato.

### Stemming contro lemmatizzazione

*SD-04 @ 01:07:48, tutorial @ 01:32:38*

| | Stemming | Lemmatizzazione |
|---|---|---|
| Metodo | tronca la parte finale, tiene quella iniziale | analisi morfologica con dizionari dettagliati |
| Risultato | può non essere una parola (*chang*, *studi*) | forma del dizionario (*change*, *study*) |
| Contesto / PoS | ignorato | considerato (`v`, `n`, `a`, `r`) |
| Velocità | più veloce | più lento, più accurato |
| Obiettivo comune | ridurre le forme flesse: *am, are, is* → *be*; *car, cars, car's, cars'* → *car* | |

```python
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer("english")

word_list = ["studies","leaves","decreases","plays"]

for w in word_list:
    print(snowball.stem(w))
```

```
studi
leav
decreas
play
```

```python
from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()
word_list = ["studies","leaves","decreases","plays"]

for w in word_list:
    print(lemma.lemmatize(w, "v"))
    
print("-----")   

word = "leaves"
print(lemma.lemmatize(word, "n")) #Note that the v and n can be decided after sentence analysis (e.g., PoS tagging)
```

```
study
leave
decrease
play
-----
leaf
```

> **Nota aggiunta:** la slide *Stemming vs. Lemmatization: Examples in Python* chiama `lemma.lemmatize(w)` **senza** `pos` e riporta *study, leaf (noun), decrease, play*: senza argomento il default è `pos="n"`, quindi *leaves* diventa *leaf*. Mele lo dice a voce: "di default lo tratta come un nome" (SD-04 @ 01:09:23). Verificato per esecuzione: `['study', 'leaf', 'decrease', 'play']`.

---

## 10. Part-of-Speech tagging

*SD-04 @ 01:10:35*

Il **PoS tagging** assegna a ogni parola la sua categoria grammaticale (nome, verbo, aggettivo, avverbio...) e aiuta sia l'analisi sintattica sia quella semantica: dare un significato specifico alla parola permette al programma di trattarla correttamente. Torna l'esempio *Can you help me with the can?*: il primo *can* è un verbo modale (lo si capisce perché è seguito da un soggetto), il secondo un nome (è preceduto da un articolo). Per il comportamento reale dei due tagger vedi la nota nella sezione 2.

I tag più frequenti (insieme del Penn Treebank, usato da NLTK):

| Tag | Categoria | Esempi della slide |
|---|---|---|
| CC | congiunzione coordinante | *and, or, but* |
| IN | preposizione | *at, in, on, above, behind* |
| DT | determinante (articoli, dimostrativi) | *the, a, an, this, that* |
| PRP | pronome personale | *I, you, he, they* |
| PRP$ | pronome possessivo | slide: *mine, yours, his, theirs* |
| RB / RBR / RBS | avverbio / comparativo / superlativo | *really, already* / *worse, less, better* / *worst, least, best* |
| JJ / JJR / JJS | aggettivo / comparativo / superlativo | *new, old, big, beautiful* / *newer, older, bigger* / *biggest, most* |
| NN / NNS | nome comune singolare / plurale | *year, table, pen* / *years, tables, pens* |
| NNP / NNPS | nome proprio singolare / plurale | *April, Africa, Mark* / *Americans, Indians* |
| PDT | predeterminante | *all, both, half* |
| POS | terminazione possessiva (genitivo sassone) | *Patrick's pen, Klaus' house* |
| MD | modale | *can, will, could, should* |
| VB | verbo, forma base | *be, play, stay* |
| VBD | passato | *was, were* |
| VBG | participio presente / gerundio | *staying* |
| VBN | participio passato | *taken* |
| VBZ | presente, terza persona singolare | *plays* |

Attenzione, sottolinea Mele (SD-04 @ 01:12:44): in **NNP** la *P* sta per *proper*, non per *plural*; il plurale è la *S* finale (NNS, NNPS). Le liste complete si trovano online.

> **Correzione:** secondo le linee guida del Penn Treebank, **PRP$** è il tag degli aggettivi possessivi che precedono un nome (*my, your, his, her, its, our, their*); i pronomi possessivi autonomi *mine, yours, theirs* sono taggati **PRP**. Gli esempi della slide (*mine, yours, his, theirs*) sono quindi quasi tutti PRP; *his* è ambiguo (PRP$ in *his pen*, PRP in *it's his*). Verificato: `nltk.pos_tag` assegna `PRP$` a *my* in *not my brother's*.

Il tutorial (SD-04 @ 01:33:53):

```python
#PoS tagging of a list of words:
tag = nltk.pos_tag(["studying", "study", "studied"])
print (tag)
```

```
[('studying', 'VBG'), ('study', 'NN'), ('studied', 'VBD')]
```

Senza contesto, *study* viene taggato come nome (la stanza, lo studio), di default.

```python
#PoS tagging in a sentence:

sentence = "A very beautiful young lady is walking on the beach"

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

for words in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)
    
tagged_words
```

```
[('A', 'DT'), ('very', 'RB'), ('beautiful', 'JJ'), ('young', 'JJ'), ('lady', 'NN'), ('is', 'VBZ'), ('walking', 'VBG'), ('on', 'IN'), ('the', 'DT'), ('beach', 'NN')]
```

*A* determinante, *very* avverbio, *beautiful* e *young* aggettivi, *lady* nome, *is* verbo alla terza persona, *walking* participio presente, *on* preposizione, *the* determinante, *beach* nome singolare (SD-04 @ 01:14:31).

> **Nota aggiunta:** il ciclo `for words in tokenized_words:` è superfluo: a ogni iterazione richiama `nltk.pos_tag` sull'intera lista e sovrascrive lo stesso risultato, quindi tagga la frase n volte. Basta `tagged_words = nltk.pos_tag(tokenized_words)`. Il notebook 2026 ha tolto il ciclo in tutte le celle, con lo stesso output. `pos_tag` va chiamato sulla frase intera e non parola per parola, perché il tagger usa il contesto.

Con contesto, *study* viene taggato correttamente (SD-04 @ 01:35:03):

```python
#PoS tagging example with the word study as a noun:

sentence = "Today I went to the doctor study"

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

for words in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)
    
tagged_words
```

```
[('Today', 'NN'), ('I', 'PRP'), ('went', 'VBD'), ('to', 'TO'), ('the', 'DT'), ('doctor', 'NN'), ('study', 'NN')]
```

```python
#PoS tagging example with the word study as a verb:

sentence = "Today I study English"

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

for words in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)
    
tagged_words
```

```
[('Today', 'NN'), ('I', 'PRP'), ('study', 'VBP'), ('English', 'JJ')]
```

Qui *study* è un verbo al presente (VBP: non terza persona singolare).

> **Nota aggiunta:** nello stesso output il tagger sbaglia due parole: *English* è taggato `JJ` (aggettivo) invece di `NNP`, e *Today* `NN` è accettabile ma discutibile. Un buon promemoria del fatto che il tagging è probabilistico.

---

## 11. Chunking

*SD-04 @ 01:15:12*

Il **chunking** estrae dal testo frasi significative, i *noun chunk* (o *noun phrase*): raggruppa le parole in blocchi più significativi delle parole singole. Prende in input le parole con i loro PoS tag e restituisce i chunk. Esempi: *date, of, birth* → *date of birth*; *country, of, origin* → *country of origin*; in *We watched a fantastic movie*, *We* è il soggetto, *watched* il verbo e *a fantastic movie* il complemento oggetto, un unico concetto.

L'approccio usa un'**espressione regolare sui tag** (grammar pattern):

```
NP : {<DT>?<RB>*<JJ>*<NN>}
```

Un determinante opzionale (`?`), zero o più avverbi (`*`), zero o più aggettivi, un nome. Con questa regola un nome da solo, un articolo e un nome, oppure articolo, avverbi, aggettivi e nome formano un noun chunk. Mele non entra nel dettaglio delle espressioni regolari, "piuttosto complesse", ma `?` (opzionalità) e `*` (ripetizione) vanno conosciuti (SD-04 @ 01:17:30).

```python
grammar = "NP : {<DT>?<RB>*<JJ>*<NN>} "

#import matplotlib.pyplot as plt

#Creating a parser :
parser = nltk.RegexpParser(grammar)


sentence = "A very beautiful young lady is walking on the beach"
tokenized_words = word_tokenize(sentence)

for words in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)
    
#print(tagged_words)

#Parsing text :
output = parser.parse(tagged_words)
print (output)

#To visualize :
output.draw()
```

```
(S
  (NP A/DT very/RB beautiful/JJ young/JJ lady/NN)
  is/VBZ
  walking/VBG
  on/IN
  (NP the/DT beach/NN))
```

Il risultato testuale è "alquanto incomprensibile per noi umani ma molto comprensibile per la macchina" (SD-04 @ 01:36:17): due chunk NP, *A very beautiful young lady* e *the beach*, ogni token con il suo tag. `output.draw()` apre una finestra con l'albero. **Bisogna chiudere quella finestra** prima di passare alla cella successiva, altrimenti il kernel resta occupato (il cerchietto grigio di Jupyter) (SD-04 @ 01:37:19).

> **Nota aggiunta:** a voce (SD-04 @ 01:16:20) Mele descrive tre chunk, il terzo "*is walking on*"; l'output della grammatica ne ha due: *is*, *walking*, *on* restano fuori da ogni NP. `draw()` richiede Tkinter: nel container usato per la verifica Tkinter non c'è e le tre celle con `draw()` falliscono con `ModuleNotFoundError: No module named 'tkinter'` **dopo** aver stampato l'output testuale, che coincide con il notebook. In ambienti senza interfaccia grafica (Colab, server) si può commentare `draw()` o, in Jupyter, visualizzare l'albero con `svgling` installato.

---

## 12. Named Entity Recognition

*SD-04 @ 01:18:08*

Una **named entity** è il nome proprio di una persona, di un luogo, di un'organizzazione, di un brand. La **NER** estrae automaticamente dal testo le entità e il loro tipo.

| Tipo | Esempio della slide |
|---|---|
| ORGANIZATION | WHO (World Health Organization) |
| PERSON | President Obama |
| LOCATION | Mount Everest |
| DATE | 2020-07-10 |
| TIME | 12:50 P.M. |
| MONEY | One Million Dollars |
| PERCENT | 98.24% |
| FACILITY | Washington Monument |
| GPE (geopolitical entity) | North West America |

Applicazioni: classificazione dei contenuti, riassunto dei curriculum, ottimizzazione degli algoritmi dei motori di ricerca, sistemi di raccomandazione (SD-04 @ 01:18:55).

Nel tutorial la NER si applica dopo tokenizzazione e PoS tagging, con `nltk.ne_chunk` (SD-04 @ 01:37:41):

```python
#Sentence for NER :
sentence = "Mr. Smith made a deal on a beach of Switzerland near WHO."
#sentence = "Mr. Smith made a deal on a beach of United States near Yosemite Park."

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

#PoS tagging :
for w in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)

print (tagged_words)
print()

#Named Entity Recognition :
N_E_R = nltk.ne_chunk(tagged_words, binary=False) #print the named-entity type
print(N_E_R)

#To visualize :
N_E_R.draw()
```

```
[('Mr.', 'NNP'), ('Smith', 'NNP'), ('made', 'VBD'), ('a', 'DT'), ('deal', 'NN'), ('on', 'IN'), ('a', 'DT'), ('beach', 'NN'), ('of', 'IN'), ('Switzerland', 'NNP'), ('near', 'IN'), ('WHO', 'NNP'), ('.', '.')]

(S
  (PERSON Mr./NNP)
  (PERSON Smith/NNP)
  made/VBD
  a/DT
  deal/NN
  on/IN
  a/DT
  beach/NN
  of/IN
  (GPE Switzerland/NNP)
  near/IN
  (ORGANIZATION WHO/NNP)
  ./.)
```

Con `binary=False` il chunker indica anche il tipo: *Mr.* e *Smith* persone, *Switzerland* entità geopolitica, *WHO* organizzazione.

A lezione (SD-04 @ 01:19:44, tratto recuperato con una seconda passata di trascrizione) la frase della slide è l'altra, quella commentata nel notebook: *Mr. Smith made a deal on a beach of the United States near Yosemite Park*. Con `pos_tag` e `ne_chunk` Mele mostra che *Mr.* e *Smith* sono nomi propri riconosciuti come persona e che *United States* forma un unico chunk [?].

A lezione Mele commenta la frase della Svizzera e attiva quella della slide (SD-04 @ 01:38:59): *United States* è riconosciuto come GPE, come *Switzerland*, e *Yosemite Park* come FACILITY. Il notebook ufficiale lascia attiva la frase della Svizzera; l'output della frase della slide, verificato rieseguendo la cella (ed è l'output del notebook 2026):

```
(S
  (PERSON Mr./NNP)
  (PERSON Smith/NNP)
  made/VBD
  [...]
  of/IN
  (GPE United/NNP States/NNPS)
  near/IN
  (FACILITY Yosemite/NNP Park/NNP)
  ./.)
```

*United States* è un nome proprio al plurale (NNP + NNPS).

> **Nota aggiunta:** con `binary=False` NLTK spezza *Mr. Smith* in due entità PERSON separate (*Mr.* e *Smith*), mentre con `binary=True` (sotto) le tiene in un'unica NE. La slide *NER: Example in Python* mostra lo stesso comportamento.

Con `binary=True` il chunker dice solo **se** un gruppo è una named entity, non il tipo (SD-04 @ 01:39:31):

```python
#Sentence for NER :
sentence = "Mr. Smith made a deal on a beach of United States near Yosemite Park."

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

#PoS tagging :
for w in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)

print (tagged_words)
print()

#Named Entity Recognition :
N_E_R = nltk.ne_chunk(tagged_words,binary=True) #print if it is a named-entity 

print(N_E_R)

#To visualize :
N_E_R.draw()
```

```
[('Mr.', 'NNP'), ('Smith', 'NNP'), ('made', 'VBD'), ('a', 'DT'), ('deal', 'NN'), ('on', 'IN'), ('a', 'DT'), ('beach', 'NN'), ('of', 'IN'), ('United', 'NNP'), ('States', 'NNPS'), ('near', 'IN'), ('Yosemite', 'NNP'), ('Park', 'NNP'), ('.', '.')]

(S
  (NE Mr./NNP Smith/NNP)
  made/VBD
  a/DT
  deal/NN
  on/IN
  a/DT
  beach/NN
  of/IN
  (NE United/NNP States/NNPS)
  near/IN
  (NE Yosemite/NNP Park/NNP)
  ./.)
```

Le NE sono *Mr. Smith*, *United States*, *Yosemite Park*. "Tipicamente però quando si applica la NER si vuole sapere anche il tipo" (SD-04 @ 01:40:01). L'albero serve agli umani; su un testo lungo la struttura viene passata a un parser per analisi successive.

> **Nota aggiunta:** nel notebook 2026 questa cella ha `binary=False` (il commento dice ancora "print if it is a named-entity") e stampa i tipi: l'esempio con `binary=True` non c'è più. Vedi divergenze.

---

## 13. WordNet: significati, sinonimi, iponimi, similarità

*SD-04 @ 01:21:07*

**WordNet** è un database lessicale della lingua inglese, incluso nei corpora di NLTK. Data una parola fornisce:

| Che cosa | *fun* | *natural* |
|---|---|---|
| significati | "activities that are enjoyable or amusing"; "verbal wit or mockery" | |
| esempi | "I do it for the fun of it"; "he is fun to have around" | |
| sinonimi | *merriment*, *playfulness*, ... | *raw*, *born*, *innate*, *lifelike*, ... |
| antonimi | `[]`: la lista può essere vuota | *unnatural*, *artificial*, *supernatural*, ... |

Per *fun* WordNet non ha contrari; un altro dizionario potrebbe averne (SD-04 @ 01:22:15).

L'unità di WordNet è il **synset**: un insieme di sinonimi che condividono un significato. Una parola ha più synset, uno per significato; il significato giusto si discrimina in base al contesto.

```python
#Import wordnet :
from nltk.corpus import wordnet

for words in wordnet.synsets("Fun"): 
    print(words)      
```

```
Synset('fun.n.01')
Synset('fun.n.02')
Synset('fun.n.03')
Synset('playfulness.n.02')
```

```python
#Word meaning with definitions :
for words in wordnet.synsets("Fun"): 
    print(words.name())
    print(words.definition())
    print(words.examples())
    
    for lemma in words.lemmas(): 
        print(lemma)
    print("\n")
```

```
fun.n.01
activities that are enjoyable or amusing
['I do it for the fun of it', 'he is fun to have around']
Lemma('fun.n.01.fun')
Lemma('fun.n.01.merriment')
Lemma('fun.n.01.playfulness')


fun.n.02
verbal wit or mockery (often at another's expense but not to be taken seriously)
['he became a figure of fun', 'he said it in sport']
Lemma('fun.n.02.fun')
Lemma('fun.n.02.play')
Lemma('fun.n.02.sport')


fun.n.03
violent and excited activity
['she asked for money and then the fun began', 'they began to fight like fun']
Lemma('fun.n.03.fun')


playfulness.n.02
a disposition to find (or make) causes for amusement
['her playfulness surprised me', 'he was fun to be with']
Lemma('playfulness.n.02.playfulness')
Lemma('playfulness.n.02.fun')
```

Il nome del synset ha la forma `parola.categoria.numero` (`n` = nome). Il terzo significato è un'attività violenta ed eccitata (SD-04 @ 01:41:46). Per avere solo i nomi dei lemmi, senza l'oggetto `Lemma(...)` che "potrebbe dare fastidio", si usa `lemma.name()`:

```python
#Get only the name of each lemma

for words in wordnet.synsets("Fun"): 
    for lemma in words.lemmas(): 
        print(lemma.name())
    print("\n")
```

```
fun
merriment
playfulness


fun
play
sport


fun


playfulness
fun
```

Lo stesso per *play* (SD-04 @ 01:42:21), che ha moltissimi synset: un dramma messo in scena da attori (*he wrote several plays but only one was produced on Broadway*), la rappresentazione teatrale, uno schema di gioco negli sport di squadra, un tentativo di ottenere qualcosa (*they made a futile play for power*), e altri. Il codice è quello di *fun* con `wordnet.synsets("Play")`; l'output è lungo e qui si omette.

### Sinonimi e antonimi

*SD-04 @ 01:43:33*

```python
#Finding synonyms and antonyms :

#Empty lists to store synonyms/antonynms : 
synonyms = []
antonyms = []

for words in wordnet.synsets('Natural'):
    for lemma in words.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
            
#Print lists :
print("Synonyms:")
print(synonyms)
print("\n")
print("Antonyms:")
print(antonyms)
```

```
Synonyms:
['natural', 'natural', 'cancel', 'natural', 'natural', 'natural', 'natural', 'natural', 'natural', 'natural', 'instinctive', 'natural', 'raw', 'rude', 'natural', 'natural', 'born', 'innate', 'lifelike', 'natural']


Antonyms:
['unnatural', 'artificial', 'supernatural', 'sharp']
```

*Natural* compare più volte perché WordNet restituisce i lemmi di ogni synset, e *natural* è lemma di quasi tutti. Fra gli antonimi *artificial* va da sé: un lago naturale contro un lago artificiale, scavato e riempito d'acqua (SD-04 @ 01:24:32).

> **Correzione:** a SD-04 @ 01:25:07 Mele interpreta l'antonimo *sharp* nel senso della moda (una persona molto ben vestita, chic, quindi "poco naturale"). In WordNet *sharp* viene dal synset `natural.a.05`, "(of a musical note) being neither raised nor lowered by one chromatic semitone": è il **bequadro** contro il **diesis**. Allo stesso modo *cancel* fra i sinonimi è il nome del segno di bequadro. Verificato in `verifica_sd04.py`, sezione 10.

> **Nota aggiunta:** la lista `synonyms` ha duplicati; per un uso reale conviene `set(synonyms)` o escludere la parola stessa.

### Iponimi e iperonimi

*SD-04 @ 01:22:50*

- **Iponimo**: parola con significato più specifico, che appartiene alla categoria espressa da una parola più generale. *Bird* è iponimo di *animal*, *robin* (pettirosso) è iponimo di *bird*.
- **Iperonimo**: parola con significato ampio, la categoria in cui ricadono parole più specifiche. *Animal* è iperonimo di *bird* e *dog*; *bird* è iperonimo di *robin* e *parrot* (pappagallo).

L'esempio a voce sono le posate: *posata* è iperonimo di forchetta, coltello, cucchiaio, che ne sono iponimi. Nella figura della slide *bird* e *dog* sono iponimi di *animal* e **co-iponimi** fra loro; a loro volta sono iperonimi di *robin*, *parrot* e di razze come *poodle* e *labrador* (Mele aggiunge husky e pastore tedesco). La stessa parola può quindi essere iponimo e iperonimo, a seconda del livello (SD-04 @ 01:23:59).

```python
word = wordnet.synsets("Bird")[0]

#Find more abstract terms:
print("Hypernyms of Bird")
print(word.hypernyms())
print("\n")
print("Hyponyms of Dove")
word = wordnet.synsets("Dove")[0]

#Find more specific terms:
word.hyponyms()
```

```
Hypernyms of Bird
[Synset('vertebrate.n.01')]


Hyponyms of Dove

[Synset('mourning_dove.n.01'), Synset('turtledove.n.02'), Synset('australian_turtledove.n.01')]
```

L'iperonimo di *bird* è *vertebrate*; gli iponimi di *dove* (colomba) sono tipi di colomba: *mourning dove*, *turtledove*, *Australian turtledove* (SD-04 @ 01:44:15).

### Similarità fra parole

*SD-04 @ 01:25:40, tutorial @ 01:45:31*

WordNet permette di calcolare la similarità fra synset. Il notebook usa la similarità di Wu-Palmer, una cella per coppia:

```python
#Similarity in words :
word1 = wordnet.synsets("ship","n")[0]

word2 = wordnet.synsets("boat","n")[0] 

#Check similarity :
print("ship vs boat: "+str(word1.wup_similarity(word2))+"\n")
```

```
ship vs boat: 0.9090909090909091
```

| Coppia | `wup_similarity` | Commento di Mele |
|---|---|---|
| ship / boat | 0,909 | nave e barca: mezzi di trasporto sull'acqua, trasportano persone, cose, animali |
| ship / bike | 0,696 | entrambi mezzi di trasporto, ma uno va per acqua e l'altro sulla terraferma; la bicicletta porta in genere una persona |
| dove / parrot | 0,8 | colomba e pappagallo, molto simili |
| dog / parrot | 0,75 | entrambi animali e vertebrati, anche se uno ha quattro zampe e l'altro vola |
| ship / parrot | 0,364 | un mezzo di trasporto contro un volatile |

Tutti i valori sono stati riottenuti identici rieseguendo il notebook.

> **Nota aggiunta:** la lezione non dà la formula. La similarità di Wu-Palmer è $\text{wup}(s_1, s_2) = \dfrac{2 \cdot \text{depth}(\text{LCS})}{\text{depth}(s_1) + \text{depth}(s_2)}$, dove LCS (*lowest common subsumer*) è l'iperonimo comune più specifico dei due synset nella gerarchia e la profondità si misura dalla radice. Vale in $(0, 1]$, e 1 solo per lo stesso synset. Per *ship* e *boat* l'LCS è `vessel.n.02`. Dipende dal synset scelto: `synsets("ship","n")[0]` prende il primo significato come nome, che non è detto sia quello voluto.

---

## 14. Bag-of-words e CountVectorizer

*SD-05 @ 00:00:09*

Dopo il preprocessing (pulizia, tokenizzazione, stopword) si costruiscono il vocabolario e i vettori. La slide riassume la pipeline: *Raw Text → Clean Text → Tokenize → Build Vocab → Generate Vectors*.

Il modello **bag-of-words** (BoW) scarta l'ordine delle occorrenze: un testo è l'insieme delle sue parole, ciascuna con il numero di volte che compare. È un metodo semplice per estrarre le feature essenziali dal testo grezzo, e le feature si usano per addestrare modelli di machine learning.

### L'esempio delle tre frasi

*SD-05 @ 00:00:42*

1. *Jim and Pam traveled by the bus*
2. *The train was late*
3. *The flight was full. Traveling by flight is expensive*

Primo passo, il conteggio per frase: nelle prime due tutte le parole compaiono una volta; nella terza *flight* compare due volte. Nell'esempio **non** si tolgono stopword e non si fa stemming, per semplicità. Nel mondo reale ci sono 100.000 documenti lunghi, e senza preprocessing *traveled* e *travel* sarebbero colonne diverse: la colonna *traveled* sarebbe zero quasi ovunque tranne dove compare esattamente quella forma. Collassando *traveling*, *traveled*, *travels* su *travel* si mantiene il contenuto semantico e si riduce la sparsità (SD-05 @ 00:02:13).

Secondo passo, l'aggregazione sulla collezione (SD-05 @ 00:03:17):

| Termine | Frequenza | | Termine | Frequenza |
|---|---|---|---|---|
| and | 1 | | late | 1 |
| bus | 1 | | pam | 1 |
| by | 2 | | the | 3 |
| expensive | 1 | | train | 1 |
| flight | 2 | | travelled | 1 |
| full | 1 | | travelling | 1 |
| is | 1 | | was | **2** |
| jim | 1 | | | |

*By* compare nella prima e nella terza frase, *flight* due volte nella terza, *the* in tutte e tre.

> **Correzione:** la tabella della slide 2025 riporta *was* = 1; *was* compare nella seconda e nella terza frase, quindi la frequenza è **2**. La slide 2026 è corretta. A voce (SD-05 @ 00:03:17) Mele dice che *by* compare "nella prima e nella seconda" frase: è nella prima e nella **terza**, come lei stessa dice poco dopo (SD-05 @ 00:04:21). Verificato per esecuzione: `verifica_sd04.py`, sezione 3.

Terzo passo, il modello finale: la **document-term matrix**, frasi sulle righe e termini sulle colonne (SD-05 @ 00:03:48).

| | and | bus | by | expensive | flight | full | is | jim | late | pam | the | train | travelled | travelling | was |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| S-2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| S-3 | 0 | 0 | 1 | 1 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |

Anche in un esempio così piccolo molti elementi sono zero: è la **sparsità**. Stopword removal e riduzione delle varianti (per esempio *was* e *is* ricondotti a *to be*) la riducono (SD-05 @ 00:04:55).

> **Nota aggiunta:** 26 celle su 45 sono zero, il 58%. Le frasi delle slide scrivono *traveled*/*Traveling* (inglese americano), il codice *travelled*/*Travelling* (britannico): le colonne della matrice sono quelle del codice.

### CountVectorizer

*SD-05 @ 00:05:29, tutorial @ 00:24:18*

In Python lo fa `CountVectorizer` di scikit-learn (`sklearn.feature_extraction.text`):

```python
#Import required libraries :
from sklearn.feature_extraction.text import CountVectorizer

#Text for analysis :
sentences = ["Jim and Pam travelled by the bus:",
             "The train was late",
             "The flight was full. Travelling by flight is expensive"]

#Create an object :
cv = CountVectorizer()

#Generating output for Bag of Words :
B_O_W = cv.fit_transform(sentences).toarray()

print("Total words with their index in model:")
print(cv.vocabulary_)
print("\n")

print("Features:")
print(cv.get_feature_names_out())
print("\n")

#Show the output :
print("Output:") #note that the vectors start with position 0
print(B_O_W)
```

```
Total words with their index in model:
{'jim': 7, 'and': 0, 'pam': 9, 'travelled': 12, 'by': 2, 'the': 10, 'bus': 1, 'train': 11, 'was': 14, 'late': 8, 'flight': 4, 'full': 5, 'travelling': 13, 'is': 6, 'expensive': 3}


Features:
['and' 'bus' 'by' 'expensive' 'flight' 'full' 'is' 'jim' 'late' 'pam'
 'the' 'train' 'travelled' 'travelling' 'was']


Output:
[[1 1 1 0 0 0 0 1 0 1 1 0 1 0 0]
 [0 0 0 0 0 0 0 0 1 0 1 1 0 0 1]
 [0 0 1 1 2 1 1 0 0 0 1 0 0 1 1]]
```

Come leggerlo (SD-05 @ 00:06:45):

- `vocabulary_` dà per ogni termine l'**indice di colonna**, contando da 0: *and* ha indice 0, *pam* 9 (compare nella prima frase), *the* 10 (colonna con tre 1, una volta per frase), *flight* 4 (colonna `0 0 2`: assente nelle prime due frasi, due volte nella terza);
- `get_feature_names_out()` dà le **feature**, cioè i termini del vocabolario nell'ordine delle colonne;
- ogni riga della matrice è un documento, ogni valore il conteggio.

> **Nota aggiunta:** il default di `CountVectorizer` converte in minuscolo (`lowercase=True`) e tokenizza con `token_pattern=r"(?u)\b\w\w+\b"`, cioè parole di almeno **due** caratteri: per questo i due punti di *bus:* e il punto di *full.* spariscono, e una parola di una lettera come *a* o *I* verrebbe scartata. Le colonne sono in ordine alfabetico. Il conteggio a mano (minuscolo, solo token alfabetici) coincide con la matrice di scikit-learn: `verifica_sd04.py`, sezione 3.

### Limiti del bag-of-words

*SD-05 @ 00:08:01*

1. **Significato semantico**: ignorando la posizione, ignora il contesto. In *Can you help me with the can?* il termine *can* ha frequenza 2 anche se i due significati sono diversi.
2. **Dimensione dei vettori**: con documenti grandi i vettori crescono, con problemi di tempo di calcolo e di scalabilità oltre che di sparsità.
3. **Preprocessing**: serve una pulizia accurata; stopword removal, stemming e lemmatizzazione aiutano, ma vanno fatti con cautela, perché "dati rumorosi portano a vettori rumorosi".
4. **Le parole sono tutte uguali**: conta solo la frequenza, non quanto la parola è discriminativa. Alcune parole non sono stopword, portano contenuto, ma compaiono in quasi tutti i documenti. In una collezione di articoli scientifici *research*, *experiment*, *result*, *state of the art* compaiono quasi ovunque e non aiutano a distinguere un articolo di fisica da uno di informatica o di medicina (SD-05 @ 00:09:37). Da qui TF-IDF.

---

## 15. Distribuzione delle frequenze dei termini

*SD-05 @ 00:11:44*

Per creare le feature si contano le frequenze delle parole. Se si guarda l'intero corpus si ottiene la **distribuzione delle frequenze dei termini**: quanto spesso compare ogni termine nei documenti? Le parole più frequenti tendono ad avere un significato meno specifico. Come per le stopword, conviene **ridurre il peso dei termini frequenti** e aumentare quello dei termini rari: le parole devono avere pesi che riflettono la loro importanza, da cui TF-IDF.

Esempio dal libro (sezione Fiction & Fantasy di Stack Exchange): dopo stopword removal e stemming, la distribuzione delle frequenze dei termini segue una **power law**, una distribuzione *highly skewed* con coda lunga. Una variante vicina è la **legge di Zipf**: se si ordinano le parole di un testo per frequenza, così che la più frequente abbia rango 1, la seconda rango 2 e così via, i loro conteggi sono inversamente proporzionali al rango (fino a un rango di circa 1000). Anche dopo aver tolto le stopword i termini in cima restano molto frequenti: non sono stopword, ma termini poco discriminativi per quel dominio (SD-05 @ 00:12:11).

> **Nota aggiunta:** la figura della slide (Figura 4.2 del libro) **non** è un grafico rango-frequenza: in ascissa c'è il numero di volte che un termine compare, in ordinata il numero di termini che compaiono quel numero di volte, entrambi in scala logaritmica. Tanti termini compaiono poche volte (in alto a sinistra), pochissimi compaiono moltissime volte (la coda a destra). La spiegazione a voce in termini di rango (SD-05 @ 00:12:46) descrive invece la legge di Zipf, che è la vista rango-frequenza dello stesso fenomeno. Il libro riporta per questa distribuzione un esponente di circa $-1{,}45$ (fit su assi doppio-logaritmici). In formule: Zipf dice $f(r) \propto r^{-s}$ con $s \approx 1$; una legge di Zipf con esponente $s$ corrisponde a una distribuzione dei conteggi $P(f) \propto f^{-(1+1/s)}$. Il libro nota anche che fra i dieci stem più frequenti compaiono *time* e *book*, per le idiosincrasie del forum di fantascienza.

---

## 16. TF-IDF

*SD-05 @ 00:10:38*

**TF-IDF** (*Term Frequency, Inverse Document Frequency*) è uno schema di pesatura usato in information retrieval e text summarization. Mette insieme due quantità:

- **TF** (term frequency): quante volte un termine compare **nel documento**. Un termine frequente nel documento è più importante di uno raro.
- **IDF** (inverse document frequency): quanto il termine è **discriminativo nella collezione**. Se un termine compare in molti documenti (stopword, verbi, aggettivi, avverbi frequenti, ma anche parole poco discriminative per il dominio) il suo peso va ridotto.

Esempio a voce (SD-05 @ 00:11:34): in una collezione di fiabe *principe*, *principessa*, *castello* compaiono quasi ovunque e sono poco discriminative; per distinguere una fiaba dall'altra servono altre parole.

La **document frequency** (DF) conta in quanti documenti compare il termine: in molti, il termine è simile a una stopword; in pochi, è rappresentativo di un topic. L'**IDF** è il suo inverso: grande se il termine compare in pochi documenti, piccolo se compare in molti. "Premia" i termini più discriminativi (SD-05 @ 00:20:57).

### Definizione formale

*SD-05 @ 00:21:27*

$$
\text{tf-idf}(t, d, D) = \text{tf}(t, d) \cdot \text{idf}(t, D) = \text{tf}(t, d) \cdot \log \frac{|D|}{|\{d \in D : t \in d\}|}
$$

- $\text{tf}(t, d)$: numero di volte che il termine $t$ compare nel documento (o frase) $d$; negli esempi viene diviso per la lunghezza del documento;
- $|D|$: numero di documenti (o frasi) del corpus;
- $|\{d \in D : t \in d\}|$: numero di documenti che contengono $t$.

Il rapporto $|D| / |\{d \in D : t \in d\}|$ **non è mai minore di 1**, quindi il logaritmo non è mai negativo: vale 0 se il termine compare in tutti i documenti.

> **Correzione:** a voce (SD-05 @ 00:23:08) Mele dice che "questo rapporto è sempre minore o uguale a 1, in modo tale che il logaritmo è sempre o 0 o maggiore di 0". È il contrario, come dice la slide: il numeratore è il totale dei documenti e il denominatore un loro sottoinsieme, quindi il rapporto è **maggiore o uguale a 1**; se fosse minore di 1 il logaritmo sarebbe negativo.

Perché il logaritmo (SD-05 @ 00:16:18): il TF si calcola su un singolo documento e dà numeri piccoli; il rapporto dell'IDF si calcola sulla collezione e può essere enorme. L'esempio della slide: 100 milioni di documenti, 10 contengono il termine, rapporto 10 milioni. Senza logaritmo l'IDF renderebbe il TF trascurabile; il logaritmo "smorza" i valori alti.

> **Nota aggiunta:** la slide scrive "log" senza base. Il valore $\log 2 = 0{,}693$ dell'esempio indica il **logaritmo naturale**, che è anche quello di scikit-learn. Con il logaritmo in base 10 si avrebbe $\log_{10} 2 = 0{,}301$: cambia la scala dei pesi, non l'ordinamento. Il libro [1] usa come tf il conteggio grezzo e nota che dividere per il numero di termini del documento è un'opzione; la definizione formale della slide parla di conteggio, gli esempi numerici dividono per la lunghezza.

### Esempio a mano

*SD-05 @ 00:14:32*

Due documenti, senza preprocessing:

- $d_1$ = *This is the first document* (5 parole)
- $d_2$ = *This document is the second document* (6 parole; *document* compare due volte)

**TF** = frequenza della parola nella frase / numero totale di parole della frase:

| Termine | TF in $d_1$ | TF in $d_2$ |
|---|---|---|
| this | 1/5 = 0,20 | 1/6 = 0,166 |
| is | 1/5 = 0,20 | 1/6 = 0,166 |
| the | 1/5 = 0,20 | 1/6 = 0,166 |
| first | 1/5 = 0,20 | 0 |
| document | 1/5 = 0,20 | 2/6 = 0,33 |
| second | 0 | 1/6 = 0,166 |

**IDF** = log(numero totale di frasi / numero di frasi che contengono la parola). Non dipende dal documento, è lo stesso per tutta la collezione (SD-05 @ 00:16:54):

| Termine | IDF |
|---|---|
| this, is, the, document | log(2/2) = log(1) = 0 |
| first, second | log(2/1) = log(2) = 0,693 |

**TF-IDF** = TF × IDF:

| Termine | TF-IDF in $d_1$ | TF-IDF in $d_2$ |
|---|---|---|
| this, is, the, document | 0 | 0 |
| first | 0,20 × 0,693 = **0,139** | 0 |
| second | 0 | 0,166 × 0,693 = **0,116** |

Tutti i termini presenti in entrambi i documenti si azzerano; restano solo *first* e *second*, gli unici discriminativi (SD-05 @ 00:19:04). In un caso reale il logaritmo esattamente 0 capita di rado, quasi solo per le stopword; ma se un termine compare in 99 documenti su 100 il rapporto è vicinissimo a 1 e il logaritmo vicinissimo a 0 (SD-05 @ 00:19:39).

> **Correzione:** la tabella della slide *Inverse Document Frequency: Example* scrive *first* = 0.20·log(2) = 0.13 e *second* = 0.166·log(2) = **0.13**. Con il logaritmo naturale i valori sono 0,1386 (arrotondato 0,14) e **0,1155** (0,12): *second* pesa meno di *first* perché $d_2$ è più lungo. Calcolato a mano e con scikit-learn in `verifica_sd04.py`, sezioni 4 e 5. A voce (SD-05 @ 00:17:57) Mele parla anche di "parole che hanno logaritmo pari a 1" intendendo log(2/2), cioè il logaritmo **di** 1, che vale 0: è un lapsus, la frase successiva lo chiarisce.

A voce (SD-05 @ 00:15:13, tratto recuperato con una seconda passata di trascrizione): per la term frequency si mette al numeratore il numero di volte in cui la parola compare nel documento, qui la frase, e si divide per la lunghezza del documento, cioè il numero totale di parole. La prima frase ha 5 parole, quindi ogni termine vale 1/5 = 0,20; la seconda ha 6 parole e i conteggi si dividono per 6 (*document*, che compare due volte, vale 2/6).

### TfidfVectorizer: perché i numeri non coincidono con la slide

*SD-05 @ 00:23:08, tutorial @ 00:26:00*

```python
#Import required libraries :
from sklearn.feature_extraction.text import TfidfVectorizer

#Sentences for analysis :
#sentences = ['This is the first document','This document is the second document']
sentences =["Jim and Pam travelled by the bus:",
             "The train was late",
             "The flight was full.Travelling by flight is expensive"]

#Create an object :
vectorizer = TfidfVectorizer(norm = None)

#Generating output for TF_IDF :
X = vectorizer.fit_transform(sentences).toarray()

print("Total words with their index in model:")
print(vectorizer.vocabulary_)
print("\n")

print("Features:")
print(vectorizer.get_feature_names_out())
print("\n")

#Show the output :
print("Output:")
print(X)
```

```
Total words with their index in model:
{'jim': 7, 'and': 0, 'pam': 9, 'travelled': 12, 'by': 2, 'the': 10, 'bus': 1, 'train': 11, 'was': 14, 'late': 8, 'flight': 4, 'full': 5, 'travelling': 13, 'is': 6, 'expensive': 3}


Features:
['and' 'bus' 'by' 'expensive' 'flight' 'full' 'is' 'jim' 'late' 'pam'
 'the' 'train' 'travelled' 'travelling' 'was']


Output:
[[1.69314718 1.69314718 1.28768207 0.         0.         0.
  0.         1.69314718 0.         1.69314718 1.         0.
  1.69314718 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         1.69314718 0.         1.         1.69314718
  0.         0.         1.28768207]
 [0.         0.         1.28768207 1.69314718 3.38629436 1.69314718
  1.69314718 0.         0.         0.         1.         0.
  0.         1.69314718 1.28768207]]
```

"Poco leggibile perché ci sono molte cifre dopo la virgola": 1,69 è il valore del termine con indice 0, *and* (SD-05 @ 00:23:45). Nel tutorial Mele mostra questa matrice sulle tre frasi e dice che si può eseguire anche sull'esempio delle slide (la riga commentata); il messaggio è che i termini presenti in molti documenti pesano meno, "quindi in generale è bene usare TF-IDF" (SD-05 @ 00:26:31).

La lezione non spiega perché *the*, presente in tutte e tre le frasi, valga 1 e non 0, né da dove venga 1,69. La ragione è che `TfidfVectorizer` **non implementa la formula della slide**:

> **Nota aggiunta: la formula di scikit-learn.** Con i parametri di default (`smooth_idf=True`, `sublinear_tf=False`, `norm='l2'`):
>
> $$\text{tf}(t,d) = \text{conteggio grezzo}, \qquad \text{idf}(t) = \ln\frac{1 + n}{1 + \text{df}(t)} + 1$$
>
> e alla fine ogni riga viene normalizzata a norma euclidea 1. Rispetto alla slide cambiano quattro cose:
>
> 1. il tf è il **conteggio**, non diviso per la lunghezza (per questo *flight* vale 2 × 1,693 = 3,386);
> 2. **smoothing**: +1 a numeratore e denominatore, come se esistesse un documento in più che contiene ogni termine una volta; evita divisioni per zero su termini nuovi in `transform`;
> 3. **+1 all'idf**: un termine presente in tutti i documenti non viene azzerato ma pesa 1 (per questo *the* vale 1);
> 4. **normalizzazione L2** delle righe, disattivata nel notebook con `norm=None`.
>
> Verifica sui valori del notebook ($n = 3$): df = 1 → $\ln(4/2) + 1 = 1{,}69314718$; df = 2 (*by*, *was*) → $\ln(4/3) + 1 = 1{,}28768207$; df = 3 (*the*) → $\ln(4/4) + 1 = 1$. Con `smooth_idf=False` si ha $\ln(n/\text{df}) + 1$, cioè l'idf della slide più 1.

Sull'esempio a due documenti delle slide (`verifica_sd04.py`, sezione 5):

| Configurazione | *first* in $d_1$ | *second* in $d_2$ | *this* in $d_1$ | *document* in $d_2$ |
|---|---|---|---|---|
| formula della slide (tf relativo × ln(N/df)) | 0,1386 | 0,1155 | 0 | 0 |
| `TfidfVectorizer()` default (smooth, L2) | 0,575 | 0,469 | 0,409 | 0,668 |
| `TfidfVectorizer(norm=None)` | 1,4055 | 1,4055 | 1 | 2 |
| `TfidfVectorizer(norm=None, smooth_idf=False)` | 1,6931 | 1,6931 | 1 | 2 |

Per riprodurre esattamente la slide con scikit-learn (verificato, dà 0,1386 e 0,1155):

```python
# Nota aggiunta: riproduce la formula della slide, non mostrato a lezione.
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

docs = ["This is the first document", "This document is the second document"]
C = CountVectorizer().fit_transform(docs).toarray()
idf = TfidfVectorizer(norm=None, smooth_idf=False).fit(docs).idf_   # ln(N/df) + 1
tfidf_slide = C / C.sum(axis=1, keepdims=True) * (idf - 1)            # tf relativo * ln(N/df)
print(tfidf_slide.round(4))
# [[0.     0.1386 0.     0.     0.     0.    ]
#  [0.     0.     0.     0.1155 0.     0.    ]]
```

Le differenze contano poco per l'uso tipico (similarità coseno, classificazione): l'idea, pesare di meno i termini diffusi in tutta la collezione, è la stessa, e con la normalizzazione L2 la lunghezza del documento si compensa comunque. Contano invece se si confrontano numeri calcolati a mano con quelli di una libreria, per esempio in un esercizio d'esame.

---

## 17. Il tutorial con spaCy

*SD-05 @ 00:30:01*

Il secondo tutorial fa più o meno le stesse cose con **spaCy**. Va installato insieme al modello inglese piccolo `en_core_web_sm` (*sm* = small):

```python
!python3 -m pip install --user spacy
!python3 -m spacy download en_core_web_sm
```

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

spaCy ha la sua lista di stopword, e il modulo `string` di Python fornisce i caratteri di punteggiatura, utili per ripulire il testo (SD-05 @ 00:30:43):

```python
from spacy.lang.en import stop_words

stop_words = stop_words.STOP_WORDS
print(stop_words)
```

```
{'few', 'say', 'just', 'also', 'noone', 'you', 'herein', 'though', "n't", 'as', [...]}
```

```python
from string import punctuation

punctuations = list(punctuation)
print(punctuations)
```

```
['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
```

> **Nota aggiunta:** `STOP_WORDS` è un `set`, quindi l'ordine di stampa cambia da un'esecuzione all'altra. La lista di spaCy (326 parole) è molto più ampia di quella di NLTK (198) e contiene parole come *made*, *three*, *full*, *call*: le due liste danno risultati di preprocessing diversi sullo stesso testo.

### Analisi dei token

*SD-05 @ 00:31:49*

`nlp(text)` esegue in un colpo solo una pipeline di NLP (tokenizzazione, lemmatizzazione, PoS tagging, dependency parsing, NER) e restituisce un oggetto `Doc`, che si scorre token per token:

```python
text = "Mr. Smith made a deal on a beach of Switzerland near WHO."

print("Input text: "+text)
print("\n")

doc = nlp(text) 

print("Token Analysis:\n")
for token in doc:
    print("Token: "+token.text)
    print("LEMMA: " + token.lemma_+", POS: "+token.pos_)
    if(token.is_sent_start):
        print("The sentence starts with "+ token.text)
    print("\n")
```

```
Token Analysis:

Token: Mr.
LEMMA: Mr., POS: PROPN
The sentence starts with Mr.

Token: Smith
LEMMA: Smith, POS: PROPN

Token: made
LEMMA: make, POS: VERB

Token: a
LEMMA: a, POS: DET

Token: deal
LEMMA: deal, POS: NOUN
[...]
Token: WHO
LEMMA: WHO, POS: PROPN

Token: .
LEMMA: ., POS: PUNCT
```

`token.text` è il token, `token.lemma_` la forma base, `token.pos_` il PoS tag, `token.is_sent_start` dice se il token apre una frase (solo *Mr.*). Solo *made* cambia forma (→ *make*); le altre parole sono già nella forma base. Il punto finale è riconosciuto come punteggiatura: con una rimozione preventiva della punteggiatura non ci sarebbe (SD-05 @ 00:33:57). Che "il lavoro sporco" lo faccia la funzione è un vantaggio per chi non è un programmatore esperto e uno svantaggio per chi vuole controllare la pipeline (SD-05 @ 00:32:20).

> **Nota aggiunta:** spaCy usa i tag universali (*Universal Dependencies*: PROPN, VERB, DET, NOUN, ADP, PUNCT) in `token.pos_`, e i tag Penn Treebank di NLTK (NNP, VBD...) in `token.tag_`.

```python
for token in doc:
    print(token.text+"\n is it a stopword? "+str(token.is_stop)+"\n does it have only alphab. chars? "+str(token.is_alpha)+"\n")
```

```
Mr.
 is it a stopword? False
 does it have only alphab. chars? False

Smith
 is it a stopword? False
 does it have only alphab. chars? True

made
 is it a stopword? True
 does it have only alphab. chars? True
[...]
WHO
 is it a stopword? True
 does it have only alphab. chars? True

.
 is it a stopword? False
 does it have only alphab. chars? False
```

*Made* è una stopword per spaCy, perché voce di *to make*, un verbo molto comune; lo sono anche *a*, *on*, *of*. `is_alpha` è falso solo per *Mr.* e per il punto (SD-05 @ 00:34:30).

> **Nota aggiunta:** anche *WHO* risulta stopword: il controllo di spaCy non distingue maiuscole e minuscole, e *who* pronome è nella lista. Rimuovere le stopword prima della NER cancellerebbe l'Organizzazione Mondiale della Sanità: un buon argomento per fare la NER sul testo non ancora ripulito.

### Noun chunk

*SD-05 @ 00:35:07*

spaCy trova i noun chunk da solo, con `doc.noun_chunks`. Il notebook definisce una funzione e poi ripete lo stesso codice inline:

```python
text = "Mr. Smith made a deal on a beach of Switzerland near WHO."
print("Input: "+text)
print("\n")

doc = nlp(text)  

print("**Chunk Analysis:**\n")
num_chunks = 0
for chunk in doc.noun_chunks:
    num_chunks = num_chunks + 1
    print("chunk text: "+chunk.text+"\nroot text: "+chunk.root.text+", root dep: "+ chunk.root.dep_+", root head: "+chunk.root.head.text+"\n\n")
num_chunks = len(list(doc.noun_chunks))
print("total number of chunks: "+str(num_chunks))
```

```
chunk text: Mr. Smith
root text: Smith, root dep: nsubj, root head: made

chunk text: a deal
root text: deal, root dep: dobj, root head: made

chunk text: a beach
root text: beach, root dep: pobj, root head: on

chunk text: Switzerland
root text: Switzerland, root dep: pobj, root head: of

chunk text: WHO
root text: WHO, root dep: pobj, root head: near

total number of chunks: 5
```

Per ogni chunk: il testo, la **radice** (la parola principale), la relazione di dipendenza della radice e la sua **testa**. *Mr. Smith* è il soggetto (`nsubj`) di *made*, *a deal* il complemento oggetto (`dobj`) di *made* (SD-05 @ 00:36:16). Cinque chunk in tutto.

> **Nota aggiunta:** `pobj` è l'oggetto di una preposizione (*a beach* dipende da *on*). Il contatore `num_chunks` viene calcolato due volte, con il ciclo e con `len(list(...))`; basta la seconda.

### NER con spaCy

*SD-05 @ 00:36:16*

```python
doc = nlp("Mr. Smith made a deal on a beach of Switzerland near WHO.")  

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_) #it prints the starting and ending index of the named-entity and the type

num_ents = len(doc.ents)
print("Tot. num. of recognized named entities: "+str(num_ents)+"\n") 
```

Output del notebook 2025, quello mostrato a lezione:

```
Smith 4 9 PERSON
Switzerland 36 47 GPE
WHO 53 56 ORG
Tot. num. of recognized named entities: 3
```

`doc.ents` contiene le entità; per ciascuna il testo, l'indice di carattere di inizio e di fine (contando da 0, fine esclusa) e il tipo. *Smith* va dal carattere 4 al 9 ed è una persona, *Switzerland* da 36 a 47 ed è una GPE, *WHO* un'organizzazione (SD-05 @ 00:36:56).

> **Nota aggiunta:** rieseguendo la cella con `en_core_web_sm` 3.8.0 *WHO* **non** viene riconosciuto: l'output ha 2 entità (*Smith*, *Switzerland*). Lo stesso succede nel notebook 2026 della docente. La NER di spaCy è un modello statistico e cambia fra versioni del modello; il notebook non fissa la versione. Da notare anche che spaCy dà *Smith* come PERSON, non *Mr. Smith*.

```python
doc = nlp("Mr. Smith made a deal on a beach of United States near Yosemite Park.")
          
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_) #it prints the starting and ending index of the named-entity and the type

num_ents = len(doc.ents)
print("Tot. num. of recognized named entities: "+str(num_ents)+"\n")
```

```
Smith 4 9 PERSON
United States 36 49 GPE
Yosemite Park 55 68 GPE
Tot. num. of recognized named entities: 3
```

Qui spaCy tagga *Yosemite Park* come GPE, mentre NLTK lo riconosceva come FACILITY: gli output dei due tool sono "un pochino diversi". spaCy è preferito in alcuni ambiti, NLTK ha altri vantaggi; la scelta del tool è libera (SD-05 @ 00:37:32).

> **Nota aggiunta:** nello schema di etichette di spaCy (OntoNotes) un parco come *Yosemite Park* sarebbe tipicamente LOC o FAC; GPE (paesi, città, stati) è un errore del modello piccolo. Con questo esempio entrambi i tool sbagliano qualcosa: NLTK spezza *Mr.* e *Smith*, spaCy etichetta il parco come entità geopolitica.

---

## 18. Riepilogo e compiti

*SD-05 @ 00:27:02*

- Il contenuto generato dagli utenti è spesso **testo in linguaggio naturale** (italiano, inglese, spagnolo...), dato non strutturato.
- L'**NLP** riduce il divario fra uomo e macchina nella comprensione del testo; sta all'intersezione di informatica, intelligenza artificiale e linguaggio umano. Per questo conta anche l'esperienza dei linguisti computazionali, che sviluppano i tool insieme agli informatici e li usano (SD-05 @ 00:27:37).
- **Preprocessing**, da fare con attenzione: tokenizzazione, rimozione di caratteri speciali e stopword, stemming e lemmatizzazione per ridurre la dimensionalità del vocabolario.
- **Analisi**: PoS tagging (aggettivo, avverbio, nome, verbo...), chunking (gruppi di parole che esprimono un concetto), NER (entità e tipo), analisi con WordNet.
- **Rappresentazione**: matrice documento-termine. Con il bag-of-words (`CountVectorizer`) i pesi sono i conteggi; con TF-IDF la frequenza del termine nel documento, divisa per la lunghezza, è moltiplicata per l'IDF, il logaritmo del numero di documenti diviso il numero di documenti che contengono il termine, che premia i termini discriminativi (SD-05 @ 00:29:20).

**Compiti** (slide *Homework*, SD-05 @ 00:38:05):

- leggere il capitolo 4 *Content: The What of Social Media* di *Social Media Data Mining and Analytics*, per la parte di NLP;
- ripetere i due tutorial: `NLP_withNLTK_tutorial.ipynb` (visto e approfondito a lezione) e `NLP_withSpacy_tutorial.ipynb` (messo a disposizione nel materiale del corso).

Nessuna indicazione su esame, progetto o dataset in SD-04 e SD-05.

> **Integrazione Teams 2026:** la lezione live si apre con chiarimenti sull'assignment (Teams 4 @ 0:00:03-0:02:00). Le proposte di progetto sono "per chi è poco creativo": chi ha già un proprio dataset, di lavoro o di un altro corso, contatta la docente, lo descrive insieme a ciò che vuole farci, e si concorda un progetto sui temi del corso. Oltre ai due dataset per il sentiment (tweet e review) ne fornisce uno di articoli scientifici per l'estrazione dei topic (`ACM_papers.tsv`). In chiusura (Teams 4 @ 1:42:34-1:43:57) ricorda che la parte "Supervised Approach" del video 6 va vista dopo la lezione 7, che le slide 2026 sono state solo un po' aggiornate ("piccole modifiche non cambiano": si può studiare anche sulla versione vecchia), e che il programma del I livello non cambia per non chiedere il doppio del lavoro a parità di crediti. Le lezioni live servono ad approfondire "anche in vista dell'assignment finale". Dettagli in `assessment.md`.

---

## Glossario

| Termine | Significato nel corso |
|---|---|
| NLP | tecniche per far "leggere" il linguaggio naturale alle macchine, simulandone la comprensione |
| Text mining | analisi di sequenze generiche (bit, DNA, parole); l'NLP si limita al linguaggio umano |
| Information extraction / retrieval | recupero da dati strutturati o semistrutturati / da testo libero |
| Rule-based / statistical NLP | regole scritte da esperti / modelli addestrati su grandi quantità di dati |
| Coreference resolution | sostituire un pronome con l'entità cui si riferisce (*he* → *John*) |
| Analisi pragmatica | interpretare una frase in base alla situazione (poesia, sarcasmo, cartoni animati) |
| Corpus | collezione di documenti |
| Documento | qualunque pezzo di testo (post, tweet, review) |
| Vocabolario / dizionario | insieme dei termini estratti e considerati significativi |
| Stopword | parola frequente e poco significativa, di solito rimossa |
| Token / tokenizzazione | unità di testo (frase, parola) / divisione del testo in token |
| Stemming | troncamento alla radice (*studies* → *studi*) |
| Over/understemming | radice comune per parole diverse (*universe/university*) / radici diverse per varianti della stessa parola (*data/datum*) |
| Lemmatizzazione | riduzione alla forma del dizionario, dipendente dal PoS (*leaves* → *leaf* o *leave*) |
| PoS tag | categoria grammaticale (NN, VB, JJ, ...; set Penn Treebank in NLTK) |
| Chunking / noun chunk | raggruppare parole in frasi nominali (*a very beautiful young lady*) |
| Named entity / NER | nome proprio di persona, luogo, organizzazione... / riconoscimento automatico e tipizzazione |
| GPE | geopolitical entity: paesi, città, stati |
| WordNet / synset | database lessicale inglese / insieme di sinonimi con un significato comune |
| Iponimo / iperonimo | parola più specifica / più generale (*robin* / *bird*) |
| Wu-Palmer similarity | similarità fra synset basata sulla profondità dell'antenato comune |
| Document-term matrix | righe = documenti, colonne = termini, valori = pesi |
| Sparsità | prevalenza di zeri nella matrice documento-termine |
| Bag-of-words | testo come insieme di parole con frequenze, senza ordine |
| Zipf's law | frequenza inversamente proporzionale al rango |
| TF / DF / IDF | frequenza nel documento / numero di documenti con il termine / log(N/DF) |
| TF-IDF | TF × IDF: peso alto per termini frequenti nel documento e rari nella collezione |

## Punti incerti

- **SD-05 @ 00:15:13-00:15:41:** recuperato con una seconda passata (`scripts/ritrascrivi_tratti.py`, 22/10/2026) e integrato nella sezione 16.
- **SD-04 @ 01:19:48-01:20:13:** recuperato con una seconda passata; la fine ("United States sono un nome proprio al...") resta parziale [?].
- **SD-04 @ 01:37:41-01:40:57:** segmenti a bassa confidenza (avg_logprob fino a -0,373) sulla demo NER; ricostruiti dai frame (`frame_01-39-32`, `frame_01-40-32`) e dal notebook.
- **SD-04 @ 01:16:20:** il terzo chunk "*is walking on*" descritto a voce non corrisponde all'output della grammatica (due NP): forse Mele indicava la parte fuori dai chunk.
- **SD-04 @ 00:32:37:** "Meta" come utente industriale di spaCy: detto a voce, non verificato.
- Termini corretti in silenzio dalla trascrizione: "spesi" = spaCy, "warnet"/"Wornet" = WordNet, "nementity"/"animentity" = named entity, "post-hugger"/"post hacker" = PoS tagger, "ShakeItLearn" = scikit-learn, "FrecDist" = FreqDist, "Analytics Hub" = NLTK, "zip flow" = Zipf's law, "Edile" = *a deal*, "U"/"The Who" = WHO, "ken" = *can*, "isalfa" = isalpha, "Josemite" = Yosemite, "Corefancy" = coreference.

## Materiale usato

- Video: `video/SD-04.mp4`, `video/SD-05.mp4` (portale); trascrizioni `out/SD-04/`, `out/SD-05/`; frame `frame_00-53-06`, `frame_01-36-52`, `frame_01-38-52`, `frame_01-39-32`, `frame_01-40-32` (SD-04), `frame_00-25-08`, `frame_00-25-59`, `frame_00-26-59` (SD-05)
- Slide: `Materiale/Portale/estratti/4_NLP_SDA25.pdf`; `Materiale/Teams/estratti/Slides/4_NLP_SDA26.pdf`
- Notebook e dati: `Materiale/Portale/estratti/NLP/` (2025), `Materiale/Teams/estratti/Tutorials/NLP/` (2026); copie eseguite in questa cartella (`*_2025.eseguito.ipynb`, `*_2026.eseguito.ipynb`)
- Verifiche: `verifica_sd04.py`, output in `verifica_sd04-output.txt`
- Libro [1], capitolo 4, pp. 123-134 (`Materiale/Portale/estratti/books/`)
- Teams 2026: Teams 4 **non letta** (browser integrato non disponibile durante la stesura)
