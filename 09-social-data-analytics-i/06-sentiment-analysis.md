# Capitolo 06: Sentiment Analysis

**Lezioni, in ordine logico:** SD-07 (1:14:14, intera), SD-06 da 00:49:53 alla fine (1:03:48; parte "Supervised Approaches"), SD-08 (1:21:15, intera). Dott.ssa Ida Mele, IASI-CNR
**Ordine:** nota ufficiale della docente (`important_note_about_videos.txt`): "La parte relativa a 'Supervised Approach' (a partire dal minuto 50 della lezione 6) è successiva alla lezione 7. Andrebbe seguita dopo la lezione 7 oppure subito prima della lezione 8 (prima di Naïve Bayes Classifier)". Nelle registrazioni la parte supervisionata comincia a SD-06 @ 00:49:53, subito dopo i compiti della lezione di NLP.
**Slide:** `6_Sentiment_Analysis_SDA25.pdf` (62 pagine). La versione `6_Sentiment_Analysis_SDA26.pdf` (Teams) ha le stesse 62 pagine, con differenze minime (vedi file divergenze).
**Riferimento:** Bing Liu, *Sentiment Analysis and Opinion Mining*, Morgan & Claypool, capitoli 1-4 (slide *Outline* e *Homework*). Il livello di aspetto (capitolo 5 del libro) compare nelle slide ma non è citato come lettura.
**Notebook:** `sentiment_mining/Sentiment_mining_Twitter.ipynb` e `Read_Clothing_Reviews.ipynb` (portale 2025); versioni 2026 su Teams in `Tutorials/sentiment_mining/`, più `Sentiment_mining_Twitter-sample.ipynb`. Tutti eseguiti per intero (sez. 15.10).
**Fonti 2026:** nessuna integrazione dalle registrazioni Teams. Il materiale "II level" (RoBERTa, deep learning per la sentiment analysis) è fuori perimetro.

## Indice

1. [Che cos'è la sentiment analysis](#1-che-cosè-la-sentiment-analysis)
2. [Motivazioni e prime sfide](#2-motivazioni-e-prime-sfide)
3. [Approcci, dati e aree applicative](#3-approcci-dati-e-aree-applicative)
4. [L'opinione e la sua definizione formale](#4-lopinione-e-la-sua-definizione-formale)
5. [Fatti contro opinioni, tipi di opinione](#5-fatti-contro-opinioni-tipi-di-opinione)
6. [Sentiment classification: soggettività e polarità](#6-sentiment-classification-soggettività-e-polarità)
7. [Granularità: documento, frase, feature](#7-granularità-documento-frase-feature)
8. [Gli step di un progetto e la consegna dei risultati](#8-gli-step-di-un-progetto-e-la-consegna-dei-risultati)
9. [Approcci e feature: la mappa](#9-approcci-e-feature-la-mappa)
10. [Approcci non supervisionati](#10-approcci-non-supervisionati)
11. [Approcci supervisionati](#11-approcci-supervisionati)
12. [Naive Bayes](#12-naive-bayes)
13. [Valutazione: confusion matrix, precision, recall, F1, micro e macro, ROC e AUC](#13-valutazione-confusion-matrix-precision-recall-f1-micro-e-macro-roc-e-auc)
14. [Regressione](#14-regressione)
15. [Tutorial: sentiment mining su Twitter](#15-tutorial-sentiment-mining-su-twitter)
16. [Il progetto: tre proposte e il dataset delle review](#16-il-progetto-tre-proposte-e-il-dataset-delle-review)
17. [Le sfide della sentiment classification](#17-le-sfide-della-sentiment-classification)
18. [Riepilogo e compiti](#18-riepilogo-e-compiti)

---

## 1. Che cos'è la sentiment analysis

*SD-07 @ 00:00:10*

La lezione segue i capitoli 1-4 del libro di Liu, "il secondo pdf che vi ho messo a disposizione". Mele precisa che non vanno studiati i quattro capitoli interi, ma "solo le parti riportate nelle slide", da usare come indice (SD-07 @ 00:02:31).

**Definizione.** La sentiment analysis è l'area di ricerca che analizza il contenuto condiviso dagli utenti, soprattutto testo, per trovarvi espressioni che identificano un'opinione (*opinionated text*).

**Sinonimi e gerarchie** (SD-07 @ 00:03:07). Si parla di *sentiment analysis*, *sentiment mining*, *opinion mining*, *opinion extraction*, *subjectivity analysis*, *emotion analysis* (più specifica), *review mining* (applicata alle review). Nel corso sentiment analysis e opinion mining sono usati come sinonimi, ma alcuni autori distinguono:

| Termine | Rapporto, per alcuni autori |
|---|---|
| Opinion mining / opinion extraction | classe più ampia: prima ci si chiede se il testo esprime un'opinione |
| Sentiment analysis / sentiment mining | sottocampo: se c'è un'opinione, se ne determina la polarità (positiva, negativa, eventualmente neutra) |
| Review mining | opinion mining applicato alle review, il contenuto più interessante per il marketing |

**La definizione di Liu** (SD-07 @ 00:04:48): "the field of study that analyzes people's opinions, sentiments, evaluations, appraisals, attitudes, and emotions towards entities such as products, services, organizations, individuals, issues, events, topics, and their attributes". Gli esempi della lezione per ogni tipo di entità: un prodotto (smartphone, forno a microonde, una bevanda), un servizio (ristorante, albergo), un'organizzazione, un individuo (personaggi famosi, politici), un dibattito o un evento. Per un'alluvione si può esprimere tristezza per le vittime, ma anche sconcerto e rabbia verso il governo se i canali non erano stati puliti. Infine gli **attributi** dell'entità: di una macchina fotografica si possono giudicare in modo diverso la qualità d'immagine e la facilità d'uso (SD-07 @ 00:06:13).

### Perché è un'area popolare e come si esprime il sentiment

*SD-07 @ 00:06:44*

La slide elenca tre ragioni: molte applicazioni commerciali (marketing), problemi di ricerca aperti (per esempio per i sistemi di raccomandazione), un enorme volume di dati *opinionated* prodotto dagli utenti del Web 2.0, che non sono più solo fruitori ma anche autori. Esempio a voce: dopo che la batteria di uno smartphone era esplosa in aereo, i commenti del tipo "non comprerò mai quel brand" hanno avuto ripercussioni negative sul produttore.

Il sentiment è "a feeling towards something/somebody" e si esprime in molte forme (SD-07 @ 00:08:24):

| Forma | Esempio | Uso nel corso |
|---|---|---|
| testo | aggettivi come *good*, *bad*, *terrible*, *fantastic* | feature principale |
| like / dislike | pollice su o giù, se la piattaforma li prevede | feature aggiuntiva |
| rating a stelle | ★★★☆☆ | **label automatiche** quando mancano etichette manuali (sez. 11.1) |
| emoticon | faccina con occhi a stella: positiva; le altre due della slide: negative | feature, ma attenzione al sarcasmo |

Sul rating la lezione anticipa il punto chiave degli approcci supervisionati: servono etichette per allenare e per valutare il classificatore; se l'etichettatura manuale costa troppo, il rating fornisce un'approssimazione automatica (SD-07 @ 00:09:25).

### Tecniche coinvolte

*SD-07 @ 00:10:35*

| Area | Ruolo nella sentiment analysis |
|---|---|
| Machine learning | classificazione di tweet, post, review in positivo/negativo |
| NLP | preprocessing, tokenizzazione, vettorizzazione, *named entity recognition* (a quale prodotto o celebrità si riferisce il sentiment) |
| Information retrieval | *opinion retrieval* e *opinion question answering*: non tutti i tweet sull'alluvione, ma solo quelli che esprimono un sentiment negativo, per tristezza o per rabbia verso chi non ha fatto manutenzione |
| Topic modeling | a quale argomento è associato il sentiment |

"Non si usa solo il tool che identifica i contenuti positivi o negativi, c'è molto altro" (SD-07 @ 00:12:28).

---

## 2. Motivazioni e prime sfide

*SD-07 @ 00:13:05*

La sentiment analysis incide su tutte le aree influenzate dalle opinioni: management, economia, scienze politiche e sociali. Nel prendere una decisione si tiene conto di cosa pensano gli altri. Le domande della slide e gli esempi a voce:

- *Which school should I apply?* "School" in americano è anche l'università: chi finisce il liceo chiede ad amici più grandi se è meglio la Sapienza o Tor Vergata, giurisprudenza o scienze politiche; oggi lo chiede in un forum di domande e risposte (SD-07 @ 00:13:38).
- *Whom should I vote for?* Per l'elezione del sindaco una volta si chiedeva al vicino; oggi si guardano i profili social dei candidati e come vengono recepite le loro azioni (SD-07 @ 00:14:55).
- *Which car should I buy?*, *Which restaurant should I go?*: anche per scelte banali (ristorante, hotel, film) si chiede un consiglio.

| | Prima del Web | Dopo il Web |
|---|---|---|
| Fonti | amici, parenti, conoscenti, *customer reports* | blog (Technorati), social network (X, Facebook), e-commerce (Amazon, eBay), forum (Quora), news feed (Google, Reuters) |

**Sfide** (SD-07 @ 00:16:19): troppa informazione, opinioni contrastanti e difficili da analizzare anche per un tool automatico, spam e fake review. Servono quindi sistemi automatici.

- **Sarcasmo** (SD-07 @ 00:16:53): "fantastico, il mio iPhone che tanto amavo si è rotto". *Fantastico*, *amavo*, *piaceva* hanno polarità positiva, mentre "si è rotto" descrive un fatto estremamente negativo senza usare parole negative.
- **Fake review** (SD-07 @ 00:17:26): i tool di generative AI imitano sempre meglio la scrittura umana. Mele ricorda un lavoro presentato a una conferenza: le fake review tendono a essere brevi e generiche. Un cliente reale scrive "la stanza era comoda e spaziosa, la pulizia efficiente, ma la vista non era un granché, avremmo preferito il mare"; una fake review di un concorrente scrive "servizio scadente", punto. Altro indizio: molte review con timestamp ravvicinati. Chi produce fake review però impara a evitare questi errori, in una rincorsa continua con i sistemi di rilevamento (SD-07 @ 00:19:39).

---

## 3. Approcci, dati e aree applicative

*SD-07 @ 00:20:09*

La slide riporta uno schema (fonte: Patil, Chaudhari, Bhavsar, Pawar, *A review on sentiment analysis in psychomedical diagnosis*): sentiment analysis **usa le tecniche** del machine learning e **usa le feature** del natural language processing; ML e NLP sono entrambi sottodomini dell'intelligenza artificiale. "Tutto rientra nel grande cappello dell'intelligenza artificiale."

### Approcci

*SD-07 @ 00:20:48*

- **Non supervisionato**: non servono dati etichettati.
- **Supervisionato**: servono dati etichettati (questo contenuto ha sentiment positivo, quest'altro negativo). L'etichetta ideale è manuale, fatta da esperti; molti dataset online sono già etichettati a mano, "come quello che utilizzeremo per il tutorial" (SD-07 @ 00:21:23). Altrimenti si etichetta un campione o si ricavano le label da altre feature come il rating.

A voce la soglia del rating è detta in due modi: "almeno tre stelline" positive (SD-07 @ 00:09:25) e "più di 3 su 5" positive (SD-07 @ 00:21:55). Lo schema preciso è nella slide degli approcci supervisionati (sez. 11.1).

**Problemi NLP che ritornano** (SD-07 @ 00:22:31):

| Problema | Esempio della lezione |
|---|---|
| Coreference resolution | "I bought a new iPhone, I simply love it": *it* è l'iPhone |
| Negation handling | "I watched the movie and I didn't like it": *like* è positivo, ma *did not* inverte la polarità |
| Word-sense disambiguation | due entità con lo stesso nome: senza disambiguare si attribuisce un sentiment negativo alla persona sbagliata |

La slide SDA26 aggiunge in questo elenco la sigla WSD e la NER.

**Un problema NLP "ristretto", ma non troppo** (SD-07 @ 00:23:34). La sentiment analysis può sembrare più semplice di altri problemi NLP: non serve capire tutta la semantica, basta stabilire la polarità e il suo target (*only sentiment detection*). Spesso però si vogliono sia il sentiment sia l'argomento: con il topic modeling (LDA) si trovano i topic con sentiment positivo e quelli con sentiment negativo (*sentiment & topic detection*).

### Dati

*SD-07 @ 00:24:41*

| Fonte | Caratteristiche secondo la lezione |
|---|---|
| Web (dati esterni): tweet, status update, commenti alle foto, review | tantissimi, rumorosi e sporchi, serve un preprocessing accurato; permettono confronti fra piattaforme (opinioni su uno smartphone su Twitter contro review sui siti di e-commerce) |
| Dati interni: feedback dei clienti via email, call center, survey | meno numerosi ma più puliti. Prima del Web i supermercati facevano compilare all'ingresso questionari di una decina di domande |

Per tipo di testo (SD-07 @ 00:26:25):

| Tipo | Difficoltà | Motivo |
|---|---|---|
| **Review** | le più facili | brevi, vanno al punto: chi ha comprato una fotocamera parla della fotocamera, chi ha comprato dei pantaloni dice se sono comodi e se il tessuto piace |
| **Tweet** | brevi ma difficili | slang fuori vocabolario (*terrific* usato come "fantastico"), *elongation* (*wooow*, *cooool*), emoticon che aiutano o ingannano ("perfetto, mi si è ancora rotto l'iPhone" con faccina sorridente: è sarcasmo) |
| **Discussioni nei forum** | le più difficili | lunghe, gli utenti interagiscono e litigano: gli insulti fra utenti in disaccordo verrebbero attribuiti all'evento discusso |

### Aree applicative

*SD-07 @ 00:29:23*

Prodotti di consumo, servizi finanziari, sanità, eventi sociali, elezioni. Esempi della lezione:

- **Sanità** negli Stati Uniti: ogni ospedale è a sé e i pazienti pagano, quindi l'opinione dei pazienti conta per la visibilità dell'ospedale.
- **Politica** (*public opinion tracking*, *influence analysis*): gruppi di data analyst lavorano per un politico per capire cosa vorrebbero sentirsi dire gli indecisi (SD-07 @ 00:30:49).
- **Marketing research**: analisi delle review, *marketing intelligence*, *brand tracking*.
- **Advertisement placement**: annunci mirati; se un utente esprime un'opinione negativa su un prodotto, il concorrente può proporgli il suo (SD-07 @ 00:31:58).

---

## 4. L'opinione e la sua definizione formale

*SD-07 @ 00:32:27*

Un'opinione ha:

| Componente | Significato |
|---|---|
| **Target** | tipicamente un'entità: persona, prodotto, servizio |
| **Sentiment** | detto anche *orientation* o *polarity*: positivo, negativo o neutro, verso l'entità o una sua caratteristica |
| **Opinion holder** | chi possiede l'opinione, in generale l'autore del testo |
| **Timestamp** | a volte solo la data, a volte data e ora |

### L'esempio di John Smith

*SD-07 @ 00:33:18*

Review postata da John Smith il 10 settembre 2011: "(1) I bought a canon g12 camera six months ago. (2) I simply love it, (3) the picture quality is amazing, (4) the battery life is also long. (5) However, my wife thinks it is too heavy for her."

| Frase | Opinionated? | Target | Polarità | Holder |
|---|---|---|---|---|
| (1) | no, è un fatto | | | |
| (2) | sì | la fotocamera nel suo insieme | positiva, "strong positive" | John Smith |
| (3) | sì | qualità delle foto | positiva | John Smith |
| (4) | sì | durata della batteria | positiva | John Smith |
| (5) | sì | peso | negativa | **la moglie di John** |

Il timestamp serve per l'**opinion trending**: le opinioni cambiano nel tempo, perché lo stesso autore può scrivere più tardi che la fotocamera si è rotta fuori garanzia, o perché, aggregando, si osservano review di utenti diversi in momenti diversi (SD-07 @ 00:35:05).

### La quintupla

*SD-07 @ 00:35:38*

Un'opinione (regolare) è la quintupla **(e<sub>i</sub>, a<sub>ij</sub>, s<sub>ijkl</sub>, h<sub>k</sub>, t<sub>l</sub>)**:

| Simbolo | Significato | Tecnica per estrarlo (slide) |
|---|---|---|
| e<sub>i</sub> | entità target | named entity recognition ed extraction |
| a<sub>ij</sub> | aspetto (feature) j dell'entità e<sub>i</sub> | information extraction |
| s<sub>ijkl</sub> | sentiment dell'holder h<sub>k</sub>, al tempo t<sub>l</sub>, sull'aspetto a<sub>ij</sub> dell'entità e<sub>i</sub> | sentiment mining |
| h<sub>k</sub> | opinion holder (l'utente, che può riportare l'opinione di altri, come John con la moglie) | |
| t<sub>l</sub> | quando l'opinione è espressa | time analysis |

Non sempre servono tutte e cinque le componenti: a volte bastano entità, sentiment e holder, se non interessano gli aspetti e non si fa opinion trending (SD-07 @ 00:36:44). Il punto della definizione è trasformare testo non strutturato in **dati strutturati**: la quintupla è come uno schema di database, ogni opinione estratta diventa una riga di una tabella o di un CSV.

> **Nota aggiunta:** per un ingegnere la lettura naturale è relazionale. L'esempio di John Smith diventa una tabella `opinion(entity, aspect, sentiment, holder, time)` con quattro righe: (Canon G12, GENERAL, +, John Smith, 2011-09-10), (Canon G12, picture quality, +, John Smith, 2011-09-10), (Canon G12, battery life, +, John Smith, 2011-09-10), (Canon G12, weight, -, John's wife, 2011-09-10). Liu (par. 2.1.1) arriva alla quintupla partendo da una quadrupla (g, s, h, t) e scomponendo il target g in entità e aspetto; usa GENERAL come aspetto quando l'opinione riguarda l'entità nel suo insieme.

---

## 5. Fatti contro opinioni, tipi di opinione

*SD-07 @ 00:37:47*

| | Esempi della slide |
|---|---|
| **Fatti: oggettivi** | "Apple released the new iPhone." "This car has 4 wheels." "Coke and Pepsi are soft drinks." |
| **Opinioni: soggettive** | "I love my new iPhone. It's fantastic!" "This car is great!" "Coke tastes better than Pepsi." |

Due eccezioni importanti:

- **Frasi oggettive con un'opinione implicita.** "I bought the mattress a week ago and a valley has formed": descrive un fatto, ma ha un'implicazione negativa, il materasso si è rovinato in una settimana e chi legge non lo comprerà. "I bought a camera that fits in a pocket": oggettiva, implicazione positiva, la fotocamera è compatta (SD-07 @ 00:39:00).
- **Frasi soggettive senza opinione.** "I think it is raining now": soggettiva ("penso"), ma non esprime un'opinione su nulla (SD-07 @ 00:39:35).

### Tipi di opinione

*SD-07 @ 00:40:08*

| Coppia | Definizione | Esempio | Cosa è più facile |
|---|---|---|---|
| **Regular** | sentiment su un'entità o un aspetto | "Coke tastes very good!" | più facile da rilevare e processare |
| **Comparative** | confronta entità su aspetti condivisi | "Coke tastes better than Pepsi." | più informativa, ma un tool fatica a capire a quale entità va l'aggettivo positivo senza un'analisi grammaticale: qui lo dice la posizione |
| **Direct** | opinione espressa direttamente su entità o aspetto | "Nikon picture quality is great." | più facile |
| **Indirect** | opinione espressa attraverso gli effetti su altre entità | "My Nikon camera fits in a pocket." | |
| **Explicit** | frase soggettiva che dà un'opinione regolare o comparativa | "Coke tastes great.", "Coke tastes better than Pepsi." | più facile da rilevare e classificare |
| **Implicit** | frase oggettiva che implica un'opinione: un fatto desiderabile o indesiderabile | il materasso; "The battery life of Nokia phones is longer than Samsung phones." | |

L'ultimo esempio è "molto difficile" perché somma due difficoltà: è implicita (descrive un fatto) ed è comparativa (Nokia contro Samsung) (SD-07 @ 00:42:54).

---

## 6. Sentiment classification: soggettività e polarità

*SD-07 @ 00:43:25*

La sentiment classification ha due passi:

1. **Subjectivity classification**: il testo esprime un'opinione o no? (soggettivo contro oggettivo, *opinionated* contro *not opinionated*)
2. **Orientation (polarity) detection**: se è opinionated, l'opinione è positiva (+), negativa (-) o neutra (0)?

| Classificazione | Esempi della slide |
|---|---|
| soggettività | "A car has four wheels." (not opinionated) / "It's a good car." (opinionated); "iPhone is Apple product." / "I like my new iPhone." |
| polarità, 2 classi | "It's a good car." (+) / "It's a bad car." (-) |
| polarità, 3 classi | come sopra, più "It's a car." (0) |

Tecniche: non supervisionate (lessico, pattern) o supervisionate (classificatori, nel corso Naive Bayes) (SD-07 @ 00:50:03).

### Che cosa cambia rispetto alla topic classification

*SD-07 @ 00:43:52*

Nella classificazione per topic (per esempio con LDA) contano le keyword dell'argomento (*sport*, *politics*). Nella sentiment classification contano le parole che esprimono polarità: *great*, *excellent*, *horrible*, *bad*, *cool*. Ne seguono regole di pulizia opposte a quelle viste per il topic modeling:

| Elemento | Topic modeling / frequenze | Sentiment classification |
|---|---|---|
| stopword | rimosse | **conservate**: molti aggettivi e la negazione *not* sono stopword |
| negazioni | rimosse come stopword | fondamentali (*negation handling*): "I do not like Pepsi" è negativo |
| caratteri speciali | rimossi | conservati: `!` enfatizza l'aggettivo, `:` `(` `)` compongono le emoticon ("My Nokia phone is awesome! :)") |

**Euristiche** (SD-07 @ 00:46:07): occorrenze delle parole, pattern di frase e punteggiatura, POS tag su unigrammi o n-grammi, stile dell'autore, popolarità delle pagine (feature basate sui link). Sugli **n-grammi** (bigrammi n = 2, trigrammi n = 3) Mele insiste: trattando le parole una alla volta si perde il *not*, a gruppi di due o tre la negazione resta attaccata alla parola che modifica. Lo stesso per gli intensificatori: "This book is very interesting", "This lecture is so boring": *very* e *so* rafforzano la polarità di *interesting* e *boring* e conviene portarli avanti insieme. Conta anche lo stile: l'autore di una review su un e-commerce scrive diversamente dall'autore di un tweet pieno di slang (SD-07 @ 00:47:13).

---

## 7. Granularità: documento, frase, feature

*SD-07 @ 00:47:54*

### Document level

*SD-07 @ 00:50:38*

Due passi: (1) il documento intero esprime un'opinione? (2) se sì, è positivo o negativo (o neutro, con tre classi)?

**Assunzione:** il documento è un'unità d'informazione, tratta un solo topic e contiene un'opinione di un solo utente. "Non sempre è vero": regge per testi brevi come tweet e status update, non per le review, dove ogni frase può cambiare opinione e aspetto, e dove possono comparire più autori (la moglie di John) (SD-07 @ 00:51:28).

Due tipi di task:

| Task | Output | Nel corso |
|---|---|---|
| Sentiment classification | sentiment complessivo del documento (positivo/negativo) | sì, tipicamente a due classi |
| Regression | valore numerico in un range, per esempio il rating 1-5 | solo citata (sez. 14) |

### Sentence level

*SD-07 @ 00:52:37*

Si decide per ogni frase se è opinionated e con quale polarità. Esempio della slide: "I bought a motorola phone two weeks ago. Everything was good initially. The voice was clear and the battery life was long, although it is a bit bulky. Then, it stopped working yesterday." La prima frase è un fatto; le altre esprimono sentiment espliciti o impliciti; una frase senza opinione si considera di solito neutra.

Due assunzioni deboli:

- **Una frase contiene una sola opinione**: falso per "The voice was clear and the battery life was long, although it is a bit bulky", che esprime tre opinioni su tre feature (voce chiara, batteria lunga, ma ingombrante) separate da virgole invece che da punti (SD-07 @ 00:53:41).
- **Le frasi oggettive non esprimono sentiment**: "Then, it stopped working yesterday" è oggettiva ma implica un sentiment negativo, perché descrive un fatto indesiderabile su un telefono comprato due settimane prima. La classificazione oggettivo/soggettivo da sola non basta.

### Feature (aspect) level

*SD-07 @ 00:54:44*

La forma più dettagliata: per ogni frase, un sentiment per ogni caratteristica dell'entità. Esempio di frase *compound and complex*: "The picture quality of this camera is amazing and so is the battery life, but the viewfinder is too small for such a great camera".

| Target | Polarità |
|---|---|
| picture quality | positiva |
| battery life | positiva |
| viewfinder | negativa |
| la fotocamera nel suo insieme | positiva ("such a great camera") |

L'idea della *feature-level* (o *aspect-level*) classification è che un'opinione sia una coppia (sentiment, target), dove il target è una feature specifica dell'entità.

---

## 8. Gli step di un progetto e la consegna dei risultati

*SD-07 @ 00:55:54*

| Step | Contenuto |
|---|---|
| **Data collection** | dataset già etichettato, oppure download via API da social (X, Instagram, Facebook), forum (Quora), e-commerce (Amazon). Il contesto conta: slang, forme *elongated* (wow, cool con la o ripetuta) e forme abbreviate, "che sono l'opposto" |
| **Data analysis: text cleaning** | eliminare il contenuto non testuale irrilevante, ma con attenzione: la punteggiatura (`!`) e le emoticon testuali (`:)` `:(` `:O` `:/`) servono; le stopword vanno mantenute, perché *good* e *bad* sono cruciali. "Dobbiamo mantenere il testo il più possibile uguale all'originale" (SD-07 @ 00:57:02) |
| **Data analysis: sentiment analysis** | si individuano e trattengono le frasi soggettive |
| **Indexing** | il testo opinionated si raggruppa in due (positivo, negativo) o tre classi (con il neutro) |

### Consegna dei risultati

*SD-07 @ 00:58:11*

L'obiettivo è convertire dati non strutturati in informazione: si aggregano le opinioni di molte persone verso un'entità o i suoi aspetti, per frequenza, e si visualizzano.

- **Sommario qualitativo**: strutturato o breve testo che riporta i risultati fondamentali.
- **Sommario quantitativo**, più frequente: "il 20% delle persone è positivo verso il prodotto", con istogrammi. La slide sottolinea che il 20% di positivi è molto diverso dall'80%. A voce Mele aggiunge che, per sottolineare il lato positivo, invece di scrivere che all'80% il prodotto non è piaciuto si scrive che il 20% si è dimostrato favorevole: "è comunque una percentuale bassa" (SD-07 @ 00:59:24).

**Autori contro lettori** (SD-07 @ 00:59:54): un'opinione va guardata da due prospettive.

- "The housing price has gone down, which is bad for the economy": negativo per chi vende, buona notizia per chi compra.
- "I am so happy that Google share price shot up today": chi ieri ha venduto in perdita non sarà contento, chi ha comprato è d'accordo con l'autore.

"C'è sempre il rovescio della medaglia."

---

## 9. Approcci e feature: la mappa

*SD-07 @ 01:00:27*

| Approcci | | Feature | |
|---|---|---|---|
| **Non supervisionati** | basati sul lessico; pattern sintattici; pattern sintattici + lessico | **Sintattiche** | POS tag |
| **Supervisionati** | classificatori allenati su dati etichettati: SVM, Naive Bayes | **Semantiche** | significato delle parole |
| **Semi-supervisionati** (ibridi) | lessico + classificatori | **Link-based** | molti link entranti: utente popolare, affidabile |
| | | **Stilistiche** | stili diversi fra uomini e donne; i giovani usano più slang degli anziani |
| | | **Semantiche + sintattiche** | combinarle dà risultati migliori |
| | | **Testo** | BoW o TF-IDF: la feature fondamentale |

Sulle feature link-based l'esempio è l'antispam: un account nuovo che scrive una recensione negativa potrebbe essere una fake review del concorrente, un utente con molti link entranti è più affidabile (SD-07 @ 01:01:49). Sulle stilistiche: studi mostrano che si può predire il genere dell'autore di un post anche senza guardare lo username (SD-07 @ 01:02:22).

---

## 10. Approcci non supervisionati

*SD-07 @ 01:03:34*

### 10.1 Feature sintattiche

*SD-07 @ 01:03:34*

Alcuni pattern sono forti indicatori di sentiment:

| Pattern | Esempio | Sentiment |
|---|---|---|
| POS + punteggiatura: aggettivo positivo + `!` | "This book is great!" | positivo |
| n-gram aggettivo + nome | "This is an interesting book" | positivo |
| | "This is a boring book" | negativo |
| trigramma con intensificatore | "this is a very interesting book" (a voce) | ancora più positivo |

I **modifier** cambiano il sentiment (*not*: "This book is not that great!" passa da positivo a negativo) o ne modificano l'intensità (*very*, *mostly*: "I found this book very interesting") (SD-07 @ 01:04:47).

### 10.2 Feature semantiche

*SD-07 @ 01:04:47*

Catturano il significato delle parole, con approcci manuali, semiautomatici o completamente automatici.

- **PMI (Pointwise Mutual Information)**, misura di associazione della teoria dell'informazione: una frase ha orientamento positivo se è associata a *excellent*, *good*, *nice* piuttosto che a *poor*, *horrible*, *terrible*. Limite citato: non tiene conto dello slang, come *terrific* usato dai giovani per "fantastico" (SD-07 @ 01:05:57).
- **Appraisal groups**: parole e frasi classificate a mano in classi di valutazione (per esempio *deny*, *endorse*, *affirm*); richiede sforzo umano.

### 10.3 Le due famiglie

*SD-07 @ 01:06:29*

Gli approcci non supervisionati non richiedono label sui dati, ma l'analista definisce un dizionario di parole d'opinione o dei pattern di POS. Sono semplici ma non sempre efficaci, perché dipendono dal dominio.

| Famiglia | Base |
|---|---|
| **Lexicon-based** | dizionari predefiniti di parole positive e negative |
| **Syntactic-pattern** | pattern sintattici definiti su POS tag, che probabilmente esprimono opinioni |

### 10.4 Approccio basato sul lessico

*SD-07 @ 01:07:09*

Usa l'orientamento semantico di parole o frasi: un dizionario di *opinion words*, costruibile partendo da parole "seme" positive e negative e aggiungendo sinonimi e contrari, per esempio da WordNet. Parola positiva: score > 0; negativa: score < 0. Gli score possono esprimere un'intensità o essere binari (-1, +1). L'algoritmo trova nel testo le parole del dizionario e somma i loro score. Approcci più sofisticati applicano regole per negazioni e modificatori; vanno considerate anche le *contrary words* (*but*, *however*) che cambiano la polarità. Il limite pratico: i dizionari sono definiti a mano e, per arricchirli, si dovrebbero cercare i sinonimi di ogni parola (SD-07 @ 01:07:43).

Il dizionario della slide:

| Key | Value |
|---|---|
| like | +2 |
| good | +1 |
| worst | -3 |
| best | +5 |
| terrible | -1.5 |

**Esempio** (SD-07 @ 01:08:19): "I did not like the movie because of its terrible plot, but the actors are the best".

| Variante | Calcolo | Esito |
|---|---|---|
| somma semplice | +2 (like) - 1.5 (terrible) + 5 (best) = **+5.5** | positivo: **sbagliato** |
| con negation detection (*not like* → -2) | -2 - 1.5 + 5 = +1.5 | ancora positivo: *best* pesa troppo |
| con negazione e *terrible* = -5 (ipotesi a voce) | -2 - 5 + 5 = -2 | negativo: corretto |

Mele chiude: questi approcci "trovano il tempo che trovano", perché i pesi sono decisi a mano. "Perché dare a *terrible* solo -1,5 e non -5?" (SD-07 @ 01:09:00). Le tre somme sono verificate in `verifica_sd06.py` (sezione 1) con una negation detection ingenua, finestra di tre parole.

**Limiti** (SD-07 @ 01:09:44):

| Limite | Esempio |
|---|---|
| negazioni e contrary words difficili | l'esempio sopra |
| stesse parole, significato diverso nel contesto | "The movie plot was unpredictable!" positivo (molti colpi di scena); "The steering of the car is unpredictable" negativo (lo sterzo non è affidabile) |
| parole di sentiment senza sentiment | domanda: "Can you tell me which Sony camera is good?"; condizionale: "If I can find a good camera in the shop, I will buy it". Entrambe contengono *good*, nessuna esprime un'opinione su una fotocamera |
| sarcasmo | "What a great car! It stopped working in two days": anche per un umano è difficile senza vedere la faccia o sentire l'inflessione. Raro nelle review, comune nei tweet e nelle discussioni politiche nei forum |

> **Nota aggiunta:** ho passato le frasi delle slide a VADER e TextBlob, i due tool del tutorial (`verifica_sd06.py`, sezione 9). Sull'esempio del film VADER dà compound +0,636 (positivo, stesso errore del lessico della slide), TextBlob polarity 0,0. Sulla frase sarcastica dell'auto VADER dà +0,541 e TextBlob polarity 1,0: entrambi sbagliano. Sulla domanda sul telefono Nokia VADER dà +0,440 e TextBlob 0,7: entrambi vedono un'opinione positiva. Sul materasso, opinione implicita, tutti e due danno 0. I limiti della slide si riproducono tali e quali sui tool reali.

### 10.5 Approccio a pattern sintattici (Turney)

*SD-07 @ 01:11:51*

I pattern che indicano un sentiment si decidono a mano (per esempio aggettivo + nome). La slide riporta la tabella 3.2 di Liu:

| # | Prima parola | Seconda parola | Terza parola (non estratta) |
|---|---|---|---|
| 1 | JJ | NN o NNS | qualsiasi |
| 2 | RB, RBR o RBS | JJ | né NN né NNS |
| 3 | JJ | JJ | né NN né NNS |
| 4 | NN o NNS | JJ | né NN né NNS |
| 5 | RB, RBR o RBS | VB, VBD, VBN o VBG | qualsiasi |

(JJ aggettivo, NN/NNS nome singolare/plurale, RB/RBR/RBS avverbio/comparativo/superlativo, VB* verbo.) In "This piano produces beautiful sounds" si estrae "beautiful sounds" (JJ + NNS, pattern 1) e gli si associa un sentiment positivo. Aggettivi e avverbi esprimono spesso opinioni; nomi e verbi fanno da **contesto**, perché lo stesso aggettivo cambia polarità: *unpredictable steering* contro *unpredictable plot* (SD-07 @ 01:12:24).

> **Nota aggiunta:** il passo 1 l'ho eseguito con il POS tagger di NLTK (`verifica_sd06.py`, sezione 2): "This piano produces beautiful sounds" → `[('beautiful sounds', 'pattern 1')]`; "This is a very interesting book" → solo "interesting book" (pattern 1), perché *very interesting* è RB + JJ ma la terza parola, *book*, è un nome e il pattern 2 lo esclude. "The movie plot was unpredictable" non produce nulla: *unpredictable* è a fine frase, senza una seconda parola. La slide (e la tabella) sono in questo senso più restrittive di quanto suggerisce l'esempio a voce sul trigramma.

**Algoritmo** (SD-07 @ 01:12:58). Mele lo presenta "brevemente, perché non utilizzeremo nessuno di questi approcci unsupervised":

1. si estraggono i bigrammi i cui POS tag rispettano la tabella;
2. si stima la *sentiment orientation* (SO) di ogni frase estratta con la PMI:

   PMI(term<sub>1</sub>, term<sub>2</sub>) = log<sub>2</sub> [ Pr(term<sub>1</sub> ∧ term<sub>2</sub>) / ( Pr(term<sub>1</sub>) · Pr(term<sub>2</sub>) ) ]

   Il numeratore è la probabilità di co-occorrenza effettiva, il denominatore quella attesa se i due termini fossero statisticamente indipendenti; le probabilità si stimano spesso con il numero di *hit* di un motore di ricerca. Poi

   SO(phrase) = PMI(phrase, "excellent") - PMI(phrase, "poor")

3. si calcola la **SO media** di tutte le frasi della review: positiva → review positiva, altrimenti negativa.

Il risultato "dipende molto dalla scelta delle parole *excellent*, *poor*" (SD-07 @ 01:13:35).

> **Nota aggiunta:** in Liu (par. 3.2) la SO si riscrive solo con i conteggi, perché le probabilità marginali si semplificano: SO(phrase) = log<sub>2</sub> [ hits(phrase NEAR "excellent") · hits("poor") / ( hits(phrase NEAR "poor") · hits("excellent") ) ]. Turney usava l'operatore NEAR di AltaVista (entro dieci parole). Esempio numerico con conteggi **inventati** (N = 10<sup>6</sup> documenti, hits("excellent") = 20.000, hits("poor") = 25.000), verificato in `verifica_sd06.py`, sezione 3:
>
> | Frase | NEAR excellent | NEAR poor | SO |
> |---|---|---|---|
> | beautiful sounds | 300 | 60 | +2,6439 |
> | unpredictable plot | 90 | 40 | +1,4919 |
> | small viewfinder | 30 | 70 | -0,9005 |
>
> SO media = +1,0784 → review positiva. La SO calcolata come differenza di PMI e con la formula a soli conteggi coincide, come atteso. Liu riporta per il metodo accuratezze dall'84% (review di automobili) al 66% (review di film).

---

## 11. Approcci supervisionati

*SD-06 @ 00:49:53*

> Questa parte è registrata in coda a SD-06, ma va letta qui, dopo SD-07 (nota della docente).

### 11.1 Dati etichettati

*SD-06 @ 00:49:53*

Servono label per allenare il modello. Anche l'approccio non supervisionato aveva una parte manuale (il lessico), ma si applicava a dati senza etichette. Qui ogni tweet o review deve avere una label (SD-06 @ 00:50:36):

- **due classi** (positivo, negativo): il caso tipico;
- **tre classi** (positivo, negativo, neutro).

Le label ideali le assegnano etichettatori umani che leggono tweet, review, discussioni: costoso in tempo, ma il Web offre molti dataset già etichettati, anche con lo sforzo congiunto di più gruppi di ricerca. Se non ci sono, per le review si usano gli score del rating (1-5 stelle) (SD-06 @ 00:51:44):

| Schema | Negativo | Neutro | Positivo | Effetto |
|---|---|---|---|---|
| 3 classi | 1-2 | 3 | 4-5 | |
| 2 classi, *leaning to negative* | 1-3 | | 4-5 | più esempi negativi |
| 2 classi, *leaning to positive* | 1-2 | | 3-5 | più esempi positivi |

"Questa è qualcosa che decidiamo noi", e lo si rivede nell'ultima parte del tutorial (SD-06 @ 00:52:50), cioè nel dataset delle review di abbigliamento (sez. 16).

### 11.2 Il modello

*SD-06 @ 00:53:26*

La sentiment classification è un problema di **text classification**, ma con un peso molto maggiore alle parole d'opinione (*good*, *great*, *terrible*, *horrible*, *bad*). La pulizia del testo è diversa da quella per topic mining e similarità tra documenti:

| Regola | Motivo, con esempio |
|---|---|
| tenere la punteggiatura | "it is great" contro "it is great!" |
| attenzione a stemming e lemmatizzazione | comparativi e superlativi collassano: *better*, *best* diventano *good* |
| non rimuovere le stopword | molte parole di sentiment sono aggettivi e avverbi comuni; contano anche nomi (*rubbish*, *junk*, *crap*) e verbi comuni (*hate*, *like*, *love*) |

Metodi tipici: **Naive Bayes** e **SVM**; l'esempio del corso è Naive Bayes (SD-06 @ 00:55:05).

Feature, decise dal data analyst:

- **binarie**: presenza o assenza di un aggettivo positivo (*good*) o negativo (*horrible*), di un nome, di un numero cardinale;
- **estratte dal testo**, "quelle che ci interessano di più": termini e frequenze.

### 11.3 Feature testuali

*SD-06 @ 00:55:40*

| Feature | Dettaglio dalla lezione |
|---|---|
| **termini e frequenze** | unigrammi e n-grammi, tipicamente n = 2 o 3 (si può salire a 4-5, ma di rado) per catturare aggettivo + nome o avverbio + aggettivo + nome. "It's a very interesting book": unigrammi *very*, *interesting*, *book*; bigramma *interesting book*; trigramma *very interesting book*, ognuno come termine con la sua frequenza |
| **POS tag** | gli aggettivi sono indicatori importanti di opinione |
| **parole e frasi di sentiment** | *good*, *wonderful* positivi; *bad*, *terrible* negativi. Anche espressioni: "it costs someone an arm and a leg" = costa moltissimo, sentiment negativo anche se il prodotto è di qualità (SD-06 @ 00:57:23) |
| **sentiment shifter** | negazioni, la classe più importante ("I don't like this camera" è negativo nonostante *like*); avverbi contrari: "I like my new phone, although it is a bit bulky", "I love this restaurant for the food, however the service is terrible", cioè probabilmente non ci torno perché il cameriere è scortese (SD-06 @ 00:58:31) |
| **dipendenza dal dominio** | su X: hashtag, emoticon, punteggiatura, contrazioni, slang anche fuori dizionario, *elongated words* (*woooow*, *coooool*, *aweeesome*) per enfatizzare |

### 11.4 Workflow di classificazione

*SD-06 @ 00:59:53*

```
                 ┌── training set ──> sviluppo del modello (feature + label)
   Dati ── split ┤
                 └── test set ──────> valutazione (label nascoste, poi confronto con la ground truth)
                                        accuracy, precision, recall, confusion matrix
```

1. dividere i dati in training e test set;
2. scegliere un modello;
3. allenarlo sul training set, mostrandogli feature **e** label;
4. sul test set mascherare le label, far predire il modello e confrontare le predizioni con la **ground truth**, le label degli etichettatori umani.

Nei problemi reali si usano **tre** insiemi: training, **validation** (per il tuning degli iperparametri ed evitare l'overfitting) e test. Nel corso basta lo split in due, con la parte più grande al training: tipicamente 80/20 o 70/30 (SD-06 @ 01:01:36).

### 11.5 Tool

*SD-06 @ 01:02:14*

| Libreria | Uso |
|---|---|
| **NLTK** | `SentimentIntensityAnalyzer`, che restituisce `polarity_scores` per una frase (link: nltk.org/howto/sentiment.html) |
| **TextBlob** e **spaCy-TextBlob** | TextBlob stima *subjectivity* (la frase è opinionated?) e *polarity*; un componente di pipeline lo integra in spaCy |
| **scikit-learn** | vettorizzazione dei documenti, classificatori (Naive Bayes), metriche (accuracy, precision, recall, confusion matrix) |

> **Nota aggiunta (verificata su documentazione):** in TextBlob la polarity sta in [-1, 1] e la subjectivity in [0, 1]. Il `SentimentIntensityAnalyzer` di NLTK implementa VADER (*Valence Aware Dictionary and sEntiment Reasoner*), un analizzatore a lessico e regole pensato per i social media, come dice anche il commento nel notebook; il suo `compound` è normalizzato in [-1, 1].

---

## 12. Naive Bayes

*SD-08 @ 00:00:09*

Naive Bayes è una tecnica di classificazione statistica basata sul **teorema di Bayes**:

P(A|B) = P(B|A) · P(A) / P(B)

Nella forma della slide, con ipotesi h e dati D:

P(h|D) = P(D|h) · P(h) / P(D)

| Termine | Nome nella slide | Significato |
|---|---|---|
| P(h) | prior probability di h | probabilità che l'ipotesi sia vera, indipendentemente dai dati |
| P(D) | prior probability | probabilità dei dati, indipendentemente dall'ipotesi |
| P(h\|D) | posterior probability di h dato D | probabilità dell'ipotesi conoscendo i dati: è ciò che si vuole |
| P(D\|h) | "posterior probability di D dato h" | probabilità dei dati se l'ipotesi è vera |

Conoscendo P(D|h), P(h) e P(D), "con un calcolo numerico" si ottiene la posterior dell'ipotesi (SD-08 @ 00:03:02).

> **Correzione:** P(D|h) nella terminologia standard si chiama **likelihood** (verosimiglianza), non probabilità a posteriori, e P(D) è l'**evidence** (probabilità marginale dei dati). La sola posterior della formula è P(h|D). La slide e la lezione (SD-08 @ 00:00:39 e @ 00:03:02) chiamano "posterior" anche P(D|h).

**Perché "naive"** (SD-08 @ 00:00:39). È semplice, accurato, affidabile e soprattutto veloce anche su dataset grandi. "Naive" per l'assunzione di **class-conditional independence**: l'effetto di una feature sulla classe è indipendente dalle altre feature. È una semplificazione voluta, falsa nella realtà, che rende il calcolo semplice e veloce e "tuttavia dà buoni risultati". L'esempio è la richiesta di un mutuo: reddito, debiti precedenti, storia delle transazioni, età, salute, luogo di residenza vengono trattati come indipendenti, mentre età e salute sono collegate (un giovane si riprende più facilmente da una malattia) e uno stipendio alto con molti debiti e molti acquisti rende la banca più restia (SD-08 @ 00:01:17).

> **Nota aggiunta:** la lezione non scrive la regola di decisione. Per un documento d con parole w<sub>1</sub>...w<sub>n</sub> l'assunzione naive dà P(d|c) = Π<sub>i</sub> P(w<sub>i</sub>|c), quindi si sceglie la classe c che massimizza log P(c) + Σ<sub>i</sub> log P(w<sub>i</sub>|c); P(d) è uguale per tutte le classi e si ignora. Nel **Multinomial NB** del tutorial P(w|c) = (conteggio di w nei documenti di c + α) / (totale parole di c + α·|V|), con α = 1 (smoothing di Laplace, il default di scikit-learn) per non azzerare il prodotto con una parola mai vista in una classe. Verifica in `verifica_sd06.py` (sezione 4), su sei frasi costruite con gli esempi delle slide ("it's a good car" +, "it's a bad car" -, "i do not like this camera" -, ...): per "a good camera but bad battery" il calcolo a mano dà P(neg) = 0,7262, P(pos) = 0,2738, identico a `MultinomialNB(alpha=1.0).predict_proba`, predizione *neg*.

---

## 13. Valutazione: confusion matrix, precision, recall, F1, micro e macro, ROC e AUC

*SD-08 @ 00:03:33*

### 13.1 Confusion matrix

*SD-08 @ 00:03:33*

|  | **Real: Positive** | **Real: Negative** |
|---|---|---|
| **Predicted: Positive** | True Positive (TP) | False Positive (FP) |
| **Predicted: Negative** | False Negative (FN) | True Negative (TN) |

- **TP**: predetti positivi, positivi nella ground truth; **FP**: predetti positivi, in realtà negativi;
- **TN**: predetti negativi, negativi; **FN**: predetti negativi, in realtà positivi.

Sulla diagonale le predizioni corrette (verde nella slide), fuori diagonale gli errori (rosso). Con n classi la matrice è n × n, sempre con le predizioni corrette sulla diagonale (SD-08 @ 00:04:44). Nella slide le righe sono le label predette e le colonne quelle reali.

### 13.2 Metriche

*SD-08 @ 00:04:44*

| Metrica | Formula | Lettura |
|---|---|---|
| **Precision** | TP / (TP + FP) | la riga dei predetti positivi; P = 1 ⇔ FP = 0, tutto ciò che è predetto positivo lo è davvero |
| **Recall** | TP / (TP + FN) | la colonna dei positivi reali; R = 1 ⇔ FN = 0, il modello trova tutti i positivi |
| **Accuracy** | (TP + TN) / (TP + FP + FN + TN) | ingannevole se le classi sono sbilanciate |
| **F-score** | 2·P·R / (P + R) | media armonica di P e R, in [0, 1], più vicino a 1 è meglio |

La precision va calcolata anche per la classe negativa: TN / (TN + FN), "sempre la riga" (SD-08 @ 00:05:15).

### 13.3 Media su più classi: macro e micro

*SD-08 @ 00:07:24*

**Con due classi**: si calcolano P<sub>pos</sub>, R<sub>pos</sub>, P<sub>neg</sub>, R<sub>neg</sub>, poi

- P<sub>avg</sub> = (P<sub>pos</sub> + P<sub>neg</sub>) / 2, R<sub>avg</sub> = (R<sub>pos</sub> + R<sub>neg</sub>) / 2
- F<sub>avg</sub> = 2·P<sub>avg</sub>·R<sub>avg</sub> / (P<sub>avg</sub> + R<sub>avg</sub>)

Questa è la **macro average**: ogni classe pesa uguale. Se le classi non sono bilanciate è fuorviante; meglio la **micro average**, che somma i contributi delle singole classi prima di dividere (SD-08 @ 00:07:56):

- P<sub>micro</sub> = ΣTP<sub>i</sub> / Σ(TP<sub>i</sub> + FP<sub>i</sub>)
- R<sub>micro</sub> = ΣTP<sub>i</sub> / Σ(TP<sub>i</sub> + FN<sub>i</sub>)
- F<sub>micro</sub> = 2·P<sub>micro</sub>·R<sub>micro</sub> / (P<sub>micro</sub> + R<sub>micro</sub>)

**Esempio a quattro classi della slide** (SD-08 @ 00:09:11):

| Classe | TP | FP | Precision |
|---|---|---|---|
| A | 1 | 1 | 0,5 |
| B | 10 | 90 | 0,1 |
| C | 1 | 1 | 0,5 |
| D | 1 | 1 | 0,5 |

- macro: (0,5 + 0,1 + 0,5 + 0,5) / 4 = **0,4** ("mi sembra di aver fatto molto bene");
- micro: (1 + 10 + 1 + 1) / (2 + 100 + 2 + 2) = 13 / 106 = **0,123**, "molto più veritiera" perché in linea con la classe dominante B.

Verificato in `verifica_sd06.py` (sezione 6) sia a mano sia con `precision_score(average="macro"/"micro")` di scikit-learn, ricostruendo etichette coerenti con la tabella: 0,4 e 0,1226.

> **Nota aggiunta:** due precisazioni utili quando si legge l'output di scikit-learn. (1) Il `classification_report` riporta come *macro avg* dell'F1 la **media degli F1 per classe**, non l'F calcolato da P<sub>avg</sub> e R<sub>avg</sub> come nella slide: in generale i due numeri differiscono. Nel tutorial coincidono (0,764137) solo perché per ciascuna classe P e R sono quasi uguali. (2) In un problema multiclasse con una sola label per esempio, micro precision, micro recall e micro F1 sono tutti uguali all'accuracy, perché ogni FP di una classe è un FN di un'altra. scikit-learn mostra infatti solo la riga *accuracy* e non una riga *micro avg*. La terza media del report, *weighted avg*, pesa ogni classe per il suo *support* (numero di esempi reali).

**Esempio a due classi dal tutorial** (`verifica_sd06.py`, sezione 5), con la confusion matrix del notebook (TN = 6411, FP = 2320, FN = 2321, TP = 8946, classe 1 = positiva):

| | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| classe 0 (neg) | 6411/8732 = 0,7342 | 6411/8731 = 0,7343 | 0,7342 | 8731 |
| classe 1 (pos) | 8946/11266 = 0,7941 | 8946/11267 = 0,7940 | 0,7940 | 11267 |
| macro avg | 0,7641 | 0,7641 | 0,7641 | |
| weighted avg | 0,7679 | 0,7679 | 0,7679 | |
| accuracy | | | 0,7679 | 19998 |

### 13.4 ROC e AUC

*SD-08 @ 00:11:06*

La **ROC curve** (*Receiver Operating Characteristic*) mostra le prestazioni di un classificatore a tutte le soglie di classificazione. Sugli assi:

- x: **False Positive Rate** (1 - specificity) = FP / (FP + TN);
- y: **True Positive Rate** (sensitivity, simile alla recall) = TP / (TP + FN).

Il classificatore perfetto sta nell'angolo TPR = 1, FPR = 0; non esiste, perché ogni predizione comporta errori, ma più la curva è alta meglio è. La diagonale è il classificatore casuale: stare "abbondantemente sopra" significa comportarsi bene. L'**AUC** (*Area Under the ROC Curve*) riassume la curva: più è grande, migliore è il classificatore (SD-08 @ 00:12:17).

> **Correzione:** la slide dice che l'AUC fornisce una misura aggregata "across all possible classifiers"; è aggregata su **tutte le possibili soglie di classificazione** dello stesso classificatore, come dice correttamente la prima riga della stessa slide.

> **Nota aggiunta:** per costruire la curva il classificatore deve dare uno **score**, non solo una label: nel tutorial è `predict_proba(X_test)[:, 1]`, la probabilità della classe positiva. Ogni soglia sullo score produce una coppia (FPR, TPR). L'AUC ha una lettura probabilistica: è la probabilità che un esempio positivo preso a caso abbia score più alto di un negativo preso a caso. Esempio su otto score inventati (`verifica_sd06.py`, sezione 7): AUC = 0,875, uguale alla frazione di coppie (positivo, negativo) ordinate correttamente (0,875).

---

## 14. Regressione

*SD-08 @ 00:12:30*

Mele la presenta "solo per sapere cos'è": è simile alla classificazione, ma predice **valori numerici** invece di label, per esempio il numero di stelle di una review (1-5).

Tecniche (slide): SVM regression; SVM multiclasse con strategia *one-vs-all* (OVA); *metric labeling*, un metodo di meta-learning. Per predire il rating di **ogni aspetto** di un prodotto, l'approccio semplice è la regressione standard, che però non sfrutta le dipendenze fra i giudizi dell'utente sui diversi aspetti; includerle migliora le predizioni. Il corso si concentra sulla classificazione (SD-08 @ 00:13:20).

---

## 15. Tutorial: sentiment mining su Twitter

*SD-08 @ 00:13:52*

Il notebook `Sentiment_mining_Twitter.ipynb` è diviso in tre parti: (1) **sentiment classification** con Naive Bayes, (2) **sentiment analysis** con tool già pronti (NLTK/VADER e TextBlob), (3) **text analysis** (distribuzione delle parole, word cloud, LDA). Ognuna ispira una proposta di progetto (sez. 16). Il tutorial è ispirato al progetto GitHub di Gunjan933 (`twitter-sentiment-analysis`); il dataset viene dalla competizione Kaggle `twitter-sentiment-analysis2`. Mele lo esegue dal vivo in JupyterLab (ambiente conda base, Python 3.13.5).

### 15.1 Setup e dati

*SD-08 @ 00:13:52*

Serve Python 3, la versione minore "non importa" (lei ha la 3.13); se una libreria non funziona si fa upgrade o downgrade. Le installazioni sono commentate nel notebook perché lei le aveva già fatte: `seaborn` per la visualizzazione, `textblob` per la sentiment analysis; NLTK dovrebbe esserci già dal tutorial di NLP.

```python
#!python3 -m pip install --user seaborn
#!python3 -m pip install --user textblob
#!python3 -m pip install --user scipy==1.12

import numpy as np
import pandas as pd
import json, nltk
import matplotlib.pyplot as plt

nltk.download('wordnet')

import seaborn as sns

%matplotlib inline
```

Il file `datasets/Twitter_train.csv` (CSV separato da virgole) non è in UTF-8, quindi va dichiarato l'encoding (SD-08 @ 00:14:58):

```python
total_data = pd.read_csv("datasets/Twitter_train.csv", encoding="ISO-8859-1")

pd.set_option("display.max_colwidth", None)   # mostra le celle senza troncarle
total_data.head()

tweet = total_data.columns.values[2]
sentiment = total_data.columns.values[1]
```

Tre colonne: `ItemID`, `Sentiment` (0 negativo, 1 positivo), `Tweet`. Mele ricorda che "in informatica si conta sempre da zero": la colonna 2 è il testo, la 1 il sentiment (SD-08 @ 00:15:33).

> **Nota aggiunta:** le due variabili `tweet` e `sentiment` contengono i **nomi** delle colonne (`'Tweet'` e `'Sentiment'`), non i dati: servono poi come chiavi, per esempio `total_data[tweet]`. La versione 2026 del notebook elimina questa indirezione e scrive direttamente `total_data['Tweet']` e `total_data['Sentiment']` (sez. 15.10).

### 15.2 Preprocessing

*SD-08 @ 00:16:05*

Passi elencati nel notebook (Step 1): minuscole; rimozione degli username (`@...`); rimozione degli URL; analisi delle emoji; risoluzione delle contrazioni (*can't* → *can not*, *won't* → *will not*); rimozione di punteggiatura, numeri e caratteri speciali; ripetizioni di più di due lettere ridotte a due (*wooooooow* → *woow*); rimozione degli spazi extra; tokenizzazione; opzionali stopword removal e stemming o lemmatizzazione.

**Contrazioni.** Il file `assets/contractions.json` contiene un dizionario già pronto: *ain't* → "am not / are not" (molto usata nello slang), *aren't* → "are not / am not", *can't* → "cannot", *'cause* → "because"... (SD-08 @ 00:16:40).

```python
with open('assets/contractions.json', 'r') as f:
    contractions_dict = json.load(f)
contractions = contractions_dict['contractions']
```

**Emoticon.** Con le espressioni regolari (viste nel tutorial NLP) le sequenze di caratteri speciali che formano una faccina si sostituiscono con una label: sorriso, sorpresa, risata, amore, occhiolino → `positiveemoji`; tristezza e pianto → `negetiveemoji` (sic) (SD-08 @ 00:17:50).

```python
def emoji(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :') , :O
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|:o|:O|:0)', ' positiveemoji ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' positiveemoji ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' positiveemoji ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-; , @-)
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;|@-\))', ' positiveemoji ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:, :-/ , :-|
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:|:-/|:-\|)', ' negetiveemoji ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' negetiveemoji ', tweet)
    return tweet
```

**La funzione di preprocessing** (SD-08 @ 00:19:27):

```python
import re #for using regular expressions

def process_tweet(tweet):
    tweet = tweet.lower()                                             # Lowercases the string
    tweet = re.sub(r'@[^\s]+', '', tweet)                             # Removes usernames (mentions or replies)
    tweet = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', ' ', tweet)  # Remove URLs
    tweet = re.sub(r'\d+', " ", str(tweet))                           # Removes all digits
    tweet = re.sub(r'&quot;'," ", tweet)                              # Remove (&quot;)
    tweet = emoji(tweet)                                              # Replaces Emojis (see function above)
    tweet = re.sub(r'\b[a-zA-Z]\b', "", str(tweet))                   # Removes all single characters

    #simple tokenization using split()
    for word in tweet.split():
        if word.lower() in contractions:
            tweet = tweet.replace(word, contractions[word.lower()])   # Replaces contractions (see list above)
    tweet = re.sub(r'[^\w\s]', " ", str(tweet))                       # Removes all remaining special chars
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)    # Convert more than 2 letter repetitions to 2 letter (e.g., cooool --> cool)
    tweet = re.sub(r'\s+', " ", str(tweet))      # Replaces extra spaces with a single space
    return tweet
```

La sequenza spiegata a voce:

1. minuscole; via gli username (sostituiti con stringa vuota: in Twitter gli utenti si rispondono o si menzionano spesso) e gli URL (sostituiti con uno spazio); via le cifre (`\d`) e le virgolette HTML (SD-08 @ 00:19:27);
2. **solo a questo punto** si chiama `emoji()`: username e URL sono spariti, ma i caratteri speciali delle faccine (due punti, parentesi, la D, l'apostrofo del pianto) ci sono ancora (SD-08 @ 00:20:35);
3. via le lettere rimaste isolate dopo le sostituzioni;
4. contrazioni sostituite con la forma piena tramite il dizionario; vanno trattate **prima** di togliere i caratteri speciali, perché contengono l'apostrofo (SD-08 @ 00:21:41);
5. via i caratteri speciali rimasti;
6. le ripetizioni di una lettera ridotte a due. Due e non una perché in inglese le doppie sono frequenti (*cool*, *deep*). È una regex "molto semplice e basilare" che può sbagliare; un'alternativa più sofisticata è cercare la parola nel dizionario, una sorta di spelling correction (SD-08 @ 00:22:14);
7. gli spazi multipli, prodotti dalle sostituzioni precedenti, ridotti a uno.

Applicazione a tutta la colonna, con il risultato in una colonna nuova per il confronto (SD-08 @ 00:23:53):

```python
total_data['processed_tweet'] = np.vectorize(process_tweet)(total_data[tweet])

total_data.head(10)
```

Commento all'output (SD-08 @ 00:24:24):

| Originale | `processed_tweet` | Osservazione a voce |
|---|---|---|
| is so sad for my APL friend............. | is so sad for my apl friend | minuscole, via i puntini |
| I missed the New Moon trailer... | missed the new moon trailer | |
| omg its already 7:30 :O | omg its already positiveemoji | faccina sorpresa → `positiveemoji`, cifre eliminate |
| i think mi bf is cheating on me!!! T_T | think mi bf is cheating on me t_t | `T_T` (occhi con le lacrime) non è nella lista: si potrebbe aggiungere alla regex del pianto come `negetiveemoji`, visto che il testo dice "penso che il mio fidanzato mi tradisca" |
| Juuuuuuuuuuuuuuuuussssst Chillin!! | juusst chillin | *elongation* ridotta a due lettere per gruppo: ancora scritta male, ma accorciata |

> **Nota aggiunta (verificata per esecuzione, `verifica_sd06.py` sezione 8):** l'ordine dei passi in `process_tweet` fa perdere proprio due segnali che la lezione dice di conservare.
> 1. **Le negazioni contratte spariscono.** La regex `\b[a-zA-Z]\b` (lettere isolate) gira prima delle contrazioni e, siccome l'apostrofo non è un carattere di parola, isola e cancella la *t* di *don't*, *can't*, *didn't*. Le contrazioni non vengono più riconosciute e la *n't* si perde: `"I don't like Pepsi :("` → `' don like pepsi negetiveemoji '`, `"I can't wait!! :D"` → `' can wait '`. Lo si vede anche nell'output del notebook: "I've been" diventa "ve been".
> 2. **Le faccine con lettere maiuscole non vengono riconosciute.** `lower()` gira prima di `emoji()`, ma le regex della risata cercano `D` e `X` maiuscole: `:D` diventa `:d`, non corrisponde, e i suoi caratteri vengono poi cancellati; `XD` diventa `xd` e resta come parola. `:O` funziona solo perché la regex include anche `:o`.
>
> Una correzione minima è chiamare `emoji()` prima di `lower()` e risolvere le contrazioni prima di eliminare le lettere singole. Non l'ho applicata ai risultati del capitolo, che restano quelli del notebook ufficiale.

### 15.3 Stopword, stemming, lemmatizzazione (opzionali)

*SD-08 @ 00:25:31*

Per la sentiment analysis questi passi non servono, anzi danneggiano: *good*, *bad*, *hate*, *like*, *love* sono stopword o parole comuni ma portano sentiment. Mele li mostra comunque perché la terza parte del tutorial analizza le frequenze delle parole e lì servono.

Le stopword di NLTK per l'inglese "erano un po' pochine"; il notebook usa in alternativa una lista più ricca scaricata da Kaggle, in `assets/stopwords_fromKaggle.txt`: "più sono le stopword e più sarà pulito il dataset" (SD-08 @ 00:26:35).

```python
#from nltk.corpus import stopwords
#stopwords = stopwords.words("english")

stopwords = []
with open('assets/stopwords_fromKaggle.txt', 'r') as f:
    for line in f:
        stopwords.append(line.strip())

def stopwords_removal(tweet):
    cleaned_tweet = ""
    for w in tweet.split():
        if w not in stopwords:
            cleaned_tweet = cleaned_tweet +" "+w
    clean_tweet = re.sub(r' +', ' ', cleaned_tweet)#remove extra spaces (if any)
    return clean_tweet

processed_tweet = total_data.columns.values[3]
total_data['clean_tweet'] = np.vectorize(stopwords_removal)(total_data[processed_tweet])
```

Nell'output spariscono parole come *is*, *so*; "omg its already positiveemoji" diventa "omg positiveemoji". Mele fa notare che *its* sparisce anche quando è usato al posto di *it's*: molti madrelingua lo scrivono così, slang grammaticalmente sbagliato (SD-08 @ 00:28:17). Si possono anche saltare le colonne intermedie; servono solo per vedere i passaggi.

**Stemming** con lo Snowball stemmer (SD-08 @ 00:28:48):

```python
from nltk.stem import SnowballStemmer

def tweet_stemmer(tweet):
    snowball = SnowballStemmer("english")
    stemmed_tweet = ""
    for w in tweet.split():
        stemmed_tweet = stemmed_tweet +" "+snowball.stem(w)
    return stemmed_tweet

clean_tweet = total_data.columns.values[4]
total_data['clean_stemmed_tweet'] = np.vectorize(tweet_stemmer)(total_data[clean_tweet])
```

*missed* → *miss*, *cheating* → *cheat*, *worry* → *worri*: lo stemming tronca e spesso produce forme non grammaticali. *chillin*, scritto male, non viene ricondotto a *chill* (SD-08 @ 00:29:26).

**Lemmatizzazione** con il WordNet lemmatizer (SD-08 @ 00:30:07):

```python
from nltk import WordNetLemmatizer

def tweet_lemmatizer(tweet):
    lemma = WordNetLemmatizer()
    lemmatized_tweet = ""
    for w in tweet.split():
        lemmatized_tweet = lemmatized_tweet+" "+lemma.lemmatize(w, pos='v')
    return lemmatized_tweet

clean_tweet = total_data.columns.values[4]
total_data['clean_lemmatized_tweet'] = np.vectorize(tweet_lemmatizer)(total_data[clean_tweet])
```

Rispetto allo stemming, *worry* resta *worry*: si torna a una forma base del vocabolario. Stopword removal, stemming e lemmatizzazione servono per la *dimensionality reduction* del vocabolario quando si cercano le parole più rappresentative dei topic, non per la sentiment classification (SD-08 @ 00:31:19).

> **Nota aggiunta:** il lemmatizer è chiamato con `pos='v'`, cioè tratta ogni parola come verbo: *missed* → *miss*, ma un nome plurale come *friends* resta *friends*. Per la lemmatizzazione corretta di nomi e aggettivi servirebbe il POS tag di ogni parola.

### 15.4 Vettorizzazione

*SD-08 @ 00:31:51*

Per la classificazione si usa la colonna `processed_tweet` (99.989 tweet), **senza** stopword removal né normalizzazione.

```python
tweets = total_data['processed_tweet']
print(len(tweets))        # 99989
```

Le feature testuali vanno mappate in una **document-term matrix**. Con `CountVectorizer` si conta quante volte ogni termine appare nel documento, come nel tutorial NLP; "nel caso di sentiment analysis è anche quello che dà migliori risultati". Qui su unigrammi **e bigrammi** (SD-08 @ 00:32:23):

```python
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer(ngram_range=(1,2))    # Unigrams (single words) and Bigrams (two consecutive words)
final_vectorized_data = count_vectorizer.fit_transform(tweets)

print(final_vectorized_data.toarray())
print(type(final_vectorized_data))
# <class 'scipy.sparse._csr.csr_matrix'>
```

"Come vediamo la matrice è molto sparsa." L'alternativa è **TF-IDF**, che pesa anche la rarità del termine nella collezione (un termine presente in quasi tutti i documenti è poco rappresentativo), qui con n-grammi da 1 a 3 (SD-08 @ 00:33:24):

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tf_idf_vectorizer = TfidfVectorizer(use_idf = True, ngram_range=(1,3)) #from 1 to 3 consecutive words
final_vectorized_data_TFIDF = tf_idf_vectorizer.fit_transform(tweets)

print(final_vectorized_data_TFIDF.toarray())
print(type(final_vectorized_data_TFIDF))
```

> **Nota aggiunta (esito anomalo in esecuzione):** `final_vectorized_data` ha forma 99.989 × 455.577 (verificata). `toarray()` chiede una matrice **densa** di 99.989 × 455.577 int64, circa 339 GiB: nel container Linux la cella fallisce con `MemoryError: Unable to allocate 339. GiB`, e la cella TF-IDF con gli n-grammi fino a 3 chiede ancora di più. Sul Mac della docente la stampa funziona, presumibilmente perché macOS concede memoria virtuale in modo lazy e `print` legge solo gli angoli della matrice; su Linux con le impostazioni di default, o su Windows, non è garantito. Per vedere la matrice basta `print(final_vectorized_data.shape, final_vectorized_data.nnz)` o `final_vectorized_data[:3].toarray()`. Per eseguire il notebook ho sostituito solo queste due stampe; il resto è invariato.

### 15.5 Split, training, predizione

*SD-08 @ 00:34:01*

Lo split "viene praticamente gratis" con scikit-learn. `test_size=0.2` dà 80% training, 20% test; restituisce quattro oggetti: `X_train` (feature di training), `X_test` (feature di test), `y_train` (label visibili in training), `y_test` (label nascoste, per verificare le predizioni) (SD-08 @ 00:34:37).

```python
from sklearn.model_selection import train_test_split

#with CountVectorizer
X_train, X_test, y_train, y_test = train_test_split(final_vectorized_data, total_data[sentiment],
                                                    test_size=0.2, random_state=69)

#test set's size is 20% of the whole dataset
#random_state: Controls the shuffling applied to the data before applying the split

#with TFIDF
#X_train, X_test, y_train, y_test = train_test_split(final_vectorized_data_TFIDF, total_data[sentiment],
#                                                    test_size=0.2, random_state=69)

print("X_train_shape: ", X_train.shape)   # (79991, 455577)
print("X_test_shape: ", X_test.shape)     # (19998, 455577)
print("y_train_shape: ", y_train.shape)   # (79991,)
print("y_test_shape: ", y_test.shape)     # (19998,)
```

Si può commentare la riga con il CountVectorizer e usare TF-IDF; Mele lascia la prima perché i risultati commentati sono stati ottenuti così (SD-08 @ 00:35:41).

**Perché lo shuffling** (`random_state=69`, SD-08 @ 00:36:14). Non sappiamo come è ordinato un dataset scaricato. Se è ordinato per label, il primo 80% potrebbe contenere quasi tutti i positivi e il test solo negativi; con quattro classi, gli esempi della classe 4 potrebbero finire quasi tutti nel test, e il classificatore "naturalmente non può fare bene". Anche un ordinamento per timestamp è rischioso: un evento tragico produce un blocco di tweet negativi che finirebbe tutto in un solo insieme. Con lo shuffling lo split non dipende dall'ordinamento.

> **Nota aggiunta:** `train_test_split` mescola di default (`shuffle=True`); `random_state` fissa il seme, così lo split è riproducibile. Per mantenere le stesse proporzioni di classe nei due insiemi esiste anche `stratify=y`, non usato nel notebook.

**Training e predizione** con il **Multinomial Naive Bayes**. Il notebook elenca tre varianti di classificatori bayesiani in scikit-learn (Bernoulli, Gaussian, Multinomial); il multinomiale è quello adatto a feature di conteggio (SD-08 @ 00:38:05):

```python
from sklearn.naive_bayes import MultinomialNB  # Naive Bayes Classifier

model_naive = MultinomialNB().fit(X_train, y_train)
predicted_naive = model_naive.predict(X_test)
```

`fit` allena il modello su feature e label di training; `predict` predice le label dalle feature di test.

### 15.6 Valutazione

*SD-08 @ 00:39:14*

```python
from sklearn.metrics import confusion_matrix

plt.figure(dpi=75)
mat = confusion_matrix(y_test, predicted_naive)
sns.heatmap(mat.T, annot=True, fmt='d', cbar=False)

plt.title('Confusion Matrix for Naive Bayes')
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.savefig("assets/confusion_matrix.png")
plt.show()
```

La heatmap (trasposta, con le predizioni sulle righe come nella slide):

| | true 0 | true 1 |
|---|---|---|
| **predicted 0** | 6411 | 2321 |
| **predicted 1** | 2320 | 8946 |

6411 negativi e 8946 positivi predetti correttamente sulla diagonale; 2320 negativi predetti positivi; 2321 positivi predetti negativi (SD-08 @ 00:39:44).

Mele aggiunge che gli errori andrebbero guardati uno per uno: a volte ha più ragione il classificatore dell'etichettatore umano. Ricorda un dataset di tweet sulla morte di un politico americano che si era comportato bene soprattutto con le classi più povere: tweet con *mourning*, *crying* erano negativi per il classificatore, ma l'etichettatore umano li aveva interpretati come positivi per il politico, ricordato bene (SD-08 @ 00:40:44).

```python
from sklearn.metrics import accuracy_score

score_naive = accuracy_score(predicted_naive, y_test)
print("\nAccuracy with Naive-bayes:", score_naive, "\n")
# Accuracy with Naive-bayes: 0.7679267926792679

from sklearn.metrics import classification_report
print(classification_report(y_test, predicted_naive))
```

```
              precision    recall  f1-score   support

           0       0.73      0.73      0.73      8731
           1       0.79      0.79      0.79     11267

    accuracy                           0.77     19998
   macro avg       0.76      0.76      0.76     19998
weighted avg       0.77      0.77      0.77     19998
```

"Possiamo ritenerci soddisfatti": accuracy 0,76 (detta così a voce, SD-08 @ 00:41:52; a schermo 0,7679). Il report dà precision e recall per classe, accuracy, macro average e **weighted average**, la media pesata per il *support*, cioè il numero di esempi di ogni classe: qui ci sono più positivi che negativi (SD-08 @ 00:42:30).

> **Nota aggiunta:** `accuracy_score(predicted_naive, y_test)` passa gli argomenti nell'ordine inverso rispetto alla firma `accuracy_score(y_true, y_pred)`. Per l'accuracy è indifferente (è simmetrica); per precision e recall no, e infatti `classification_report` è chiamato nell'ordine giusto.

**ROC e AUC** (SD-08 @ 00:43:06):

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

# calculate the fpr and tpr for all thresholds of the classification
probs = model_naive.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = roc_curve(y_test, preds)
roc_auc = auc(fpr, tpr) #area under the curve
plt.figure(dpi=100) # to plot high quality graph
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.ylabel('True Positive Rate', color='g')
plt.xlabel('False Positive Rate', color='r')
plt.savefig("assets/ROC_curve.png")
plt.show()
```

La curva sta sopra quella del classificatore casuale (tratteggio rosso), AUC = 0,84, "che non è male".

### 15.7 Il confronto dell'autore del tutorial

*SD-08 @ 00:43:40*

L'autore originale ha confrontato vettorizzatori (Count contro TF-IDF), normalizzazioni (nessuna, stemming, lemmatizzazione) e stopword removal. La tabella del notebook, in ordine di accuracy:

| Normalizzazione | Stopword removal | Vectorizer | Accuracy |
|---|---|---|---|
| None | No | Count | 0,7601 |
| Lemmatizing | No | Count | 0,7570 |
| Stemming | No | Count | 0,7550 |
| Lemmatizing | Yes | Count | 0,7484 |
| None | No | Tf-Idf | 0,7481 |
| Stemming | Yes | Count | 0,7478 |
| Lemmatizing | Yes | Tf-Idf | 0,7456 |
| Stemming | No | Tf-Idf | 0,7436 |
| Lemmatizing | No | Tf-Idf | 0,7404 |
| Stemming | Yes | Tf-Idf | 0,7384 |

La combinazione migliore per questi dati: **nessuna normalizzazione, nessuna stopword removal, CountVectorizer, unigrammi e bigrammi**. Per altri tipi di analisi (similarità tra documenti, topic modeling) conviene invece rimuovere stopword e lemmatizzare. Mele non ha provato tutte le combinazioni e invita a farlo (SD-08 @ 00:44:51).

**Confronto dei risultati** (SD-08 @ 00:44:51). L'autore aveva ottenuto **0,7601**, la docente **0,7679**: "ci sta che ci sono piccole variazioni perché sono comunque metodi probabilistici, però in grandi linee fino alla seconda cifra decimale sono corretti". La mia esecuzione nel container dà ancora **0,7679** (sez. 15.10).

> **Nota aggiunta:** la trascrizione dice "l'autore aveva ottenuto 0 76 01, a noi invece 0 76 e 79": sono 0,7601 (prima riga della tabella) e 0,7679 (output a schermo), non "0,76 contro 0,79". La differenza non dipende dalla natura probabilistica di Naive Bayes: con `random_state` fisso, MultinomialNB e CountVectorizer sono deterministici, e infatti la mia esecuzione riproduce 0,7679 alla quarta cifra. Le cause plausibili sono il preprocessing modificato rispetto all'originale e uno split diverso (seme, proporzione). Il notebook 2026 aggiunge "Leaderboard Highest: 0.79249", il miglior punteggio della competizione Kaggle da cui viene il dataset: è probabilmente lo 0,79 che compare nei riassunti della lezione, ma a voce non è citato.

### 15.8 Parte 2: sentiment analysis con NLTK (VADER) e TextBlob

*SD-08 @ 00:45:25*

Qui non si allena nulla: si usano tool già pronti e si confrontano con la ground truth.

**Statistiche del dataset** (SD-08 @ 00:45:59):

```python
num_positive_labels_GT = (total_data[sentiment] == 1).sum()
num_negative_labels_GT = (total_data[sentiment] == 0).sum()
# Num. tweets labeled as positive: 56457
# Num. tweets labeled as negative: 43532
```

Circa 56% positivi e 44% negativi, mostrati anche con un diagramma a torta (`plt.pie`, 56,46% e 43,54%).

> **Nota aggiunta:** a voce le percentuali sono "circa il 56%" e "circa il 43%": 43.532 / 99.989 = 43,54%.

**VADER con soglie su pos, neg, neu** (SD-08 @ 00:46:32). Il `SentimentIntensityAnalyzer` di `nltk.sentiment` lavora con il lessico **VADER**, che associa alle parole un sentiment positivo o negativo. `polarity_scores` restituisce quattro valori: `pos`, `neg`, `neu`, `compound`.

```python
from nltk.sentiment import SentimentIntensityAnalyzer

#download the VADER lexicon
nltk.download('vader_lexicon')

## Sentiment Analysis with NLTK SentimentIntensityAnalyzer using positive, negative, and neutral score
def sentiment_analysis_withNLTK_pos_neg_neu(text):
    sia = SentimentIntensityAnalyzer()
    #SentimentIntensityAnalyzer (sia) returns sentiment_score in the form pos="" neg="" neu="" and compound=""
    sentiment_score = sia.polarity_scores(text)

    if sentiment_score['pos'] >= 0.5:  #Positive Sentiment
         return "positive"
    elif sentiment_score['neg'] >= 0.5:  #Negative Sentiment
        return "negative"
    elif sentiment_score['neu'] >= 0.5:  #Neutral Sentiment
        return "neutral"

total_data['predicted_SIA1'] = total_data['processed_tweet'].apply(sentiment_analysis_withNLTK_pos_neg_neu)
```

Non tutti i tweet ricevono un'etichetta: se nessuna delle tre condizioni è vera la funzione non restituisce nulla (`None`). "È una nostra scelta usare una soglia" (SD-08 @ 00:48:12).

| `predicted_SIA1` | Tweet | Esempi a schermo |
|---|---|---|
| neutral | 80.811 | "missed the new moon trailer", "think mi bf is cheating on me t_t" |
| positive | 11.456 | "must think about positive", "ok thats it you win", "but proud", "congrats to helio though" |
| negative | 2.758 | "very sad about iran", "hate leysh ar", "miss earl", "im sick cough cough" |
| non etichettati | 4.964 | totale etichettati 95.025 su 99.989 |

A schermo la cella dei negativi mostra un `NameError: name 'total_data' is not defined` (output rimasto da una sessione precedente, con kernel riavviato); Mele dice "devo ricalcolare, vabbè dopo lo faccio" e passa oltre (SD-08 @ 00:49:48). Nel notebook distribuito la cella ha l'output corretto, 2.758. Gran parte dei tweet finisce fra i neutri.

**VADER con il compound** (SD-08 @ 00:50:20). Il `compound` è "una media"; con due soglie scelte da lei ("voi potete sceglierla diversamente") ogni tweet riceve un'etichetta, perché il caso residuo va in *neutral*:

```python
## Sentiment Analysis with NLTK SentimentIntensityAnalyzer using compound scores
def sentiment_analysis_withNLTK_compound(text):
    sia = SentimentIntensityAnalyzer()
    #sia returns a sentiment score
    sentiment_score = sia.polarity_scores(text)

    if sentiment_score['compound'] > 0.5:  #Positive Sentiment
        return 'positive'
    elif sentiment_score['compound'] < -0.01:  #Negative Sentiment
        return 'negative'
    else:
         return 'neutral' #Neutral Sentiment

total_data['predicted_SIA2'] = total_data['processed_tweet'].apply(sentiment_analysis_withNLTK_compound)
```

| `predicted_SIA2` | Tweet |
|---|---|
| neutral | 48.447 |
| positive | 28.864 |
| negative | 22.678 |

Fra i positivi *positive*, *win*, *celebrate*; fra i negativi *sad*, *missed*, *sick*, e il tweet "think mi bf is cheating on me t_t" ora è riconosciuto come negativo (SD-08 @ 00:52:04).

> **Nota aggiunta (verificata sul README di VADER):** le soglie raccomandate dagli autori di VADER sono compound ≥ 0,05 positivo, compound ≤ -0,05 negativo, neutro in mezzo. Le soglie del notebook (> 0,5 e < -0,01) sono asimmetriche: spostano molti tweet debolmente positivi nei neutri e quasi tutti quelli debolmente negativi nei negativi.

**TextBlob: soggettività e polarità** (SD-08 @ 00:52:35). TextBlob dice anche se la frase è soggettiva, cioè opinionated:

```python
from textblob import TextBlob

def sentiment_analysis_with_textblob(text):
    text_blob = TextBlob(text)
    #text is opinionated or not opinionated
    subjectivity = text_blob.subjectivity
    #if text opinionated --> polarity is negative or positive
    polarity = text_blob.polarity

    if (subjectivity > 0.5) and (polarity > 0.5):
         return 'positive'
    elif (subjectivity > 0.5) and (polarity <= 0.5):
         return 'negative'
    else:
         return 'neutral'

total_data['predicted_TB'] = total_data['processed_tweet'].apply(sentiment_analysis_with_textblob)
```

Logica: subjectivity > 0,5 → opinionated; allora polarity > 0,5 → positivo, altrimenti negativo; se non è opinionated → neutro (SD-08 @ 00:53:14). Le colonne sono affiancate solo per confronto: chi usa il compound calcola solo `predicted_SIA2`.

| `predicted_TB` | Tweet |
|---|---|
| neutral | 58.701 |
| negative | 30.707 |
| positive | 10.581 |

Fra i positivi *great*, *proud*, *friendly*; fra i negativi *sad*, *sucked*, ma anche "must think about positive": Mele ipotizza che sia finito fra i negativi "per pochissimo", per una delle due condizioni (SD-08 @ 00:54:25).

> **Nota aggiunta (verificata per esecuzione, `verifica_sd06.py` sezione 9):** il caso "must think about positive" non è un margine sottile ma un effetto della regola. TextBlob dà subjectivity 0,545 (> 0,5, quindi opinionated) e polarity 0,227: positiva, ma ≤ 0,5, quindi la funzione la etichetta **negativa**. La polarity di TextBlob va da -1 a 1: la condizione `polarity <= 0.5` mette fra i negativi tutto ciò che è opinionated e non fortemente positivo, compresa la polarity 0 e quella debolmente positiva. Questo spiega i 30.707 negativi. Una regola simmetrica sarebbe `polarity > 0` positivo e `polarity < 0` negativo.

**Confronto con la ground truth** (SD-08 @ 00:55:28). Le label 0/1 vengono mappate su `'negative'`/`'positive'` e si contano le corrispondenze:

```python
print("How many labels are correcly predicted as negative sentiment?\n")
mapping = {0: 'negative'}
matching_count_SIA1 = (total_data['Sentiment'].map(mapping) == total_data['predicted_SIA1']).sum()
print("SIA1 vs GT: "+str(matching_count_SIA1))
# ... stesso schema per SIA2, TB e per mapping = {1: 'positive'}
```

| Tool | Negativi corretti (su 43.532) | Positivi corretti (su 56.457) |
|---|---|---|
| SIA1 (pos/neg/neu ≥ 0,5) | 2.337 | 9.808 |
| SIA2 (compound) | **16.742** | **22.028** |
| TextBlob | 15.581 | 8.377 |

SIA2 fa più predizioni corrette in entrambe le classi. Il confronto però è sbilanciato: la ground truth ha due classi, i tool ne producono tre, e tutti i neutri contano come errori. Mele invita a modificare le condizioni, per esempio con TextBlob "se subjectivity > 0 e polarity > 0,5 ritorno positivo, altrimenti negativo", per avere due classi: "non dobbiamo implementare grandi cose, viene tutto fatto dal tool per fortuna" (SD-08 @ 00:56:31).

### 15.9 Parte 3: text analysis

*SD-08 @ 00:57:39*

Qui servono stopword removal e stemming (*dimensionality reduction* del vocabolario): si lavora su `clean_stemmed_tweet`, separando i tweet per label della ground truth e tokenizzando con `word_tokenize` di NLTK.

```python
from nltk.tokenize import word_tokenize

def tokenize_text(tweet):
    tokens = []
    toks = word_tokenize(tweet)
    tokens.extend(toks)
    return tokens

original_positive_tokens = total_data[total_data['Sentiment'] == 1]['clean_stemmed_tweet'].apply(tokenize_text)
original_negative_tokens = total_data[total_data['Sentiment'] == 0]['clean_stemmed_tweet'].apply(tokenize_text)
```

Il risultato sono liste di token puliti; lo stemming non sempre funziona (*chillin*, scritto male, resta tale) (SD-08 @ 00:58:50). Le frequenze si calcolano con `nltk.FreqDist`:

```python
tokens = []
for positive_token in original_positive_tokens:
    tokens.extend(positive_token)

positive_freq = nltk.FreqDist(tokens)
positive_freq.most_common(20)
```

| # | Positivi | Negativi |
|---|---|---|
| 1 | love 4183 | lol 2092 |
| 2 | lol 3318 | day 1911 |
| 3 | day 2543 | sad 1711 |
| 4 | haha 1996 | time 1602 |
| 5 | time 1984 | feel 1523 |
| 6 | amp 1821 | amp 1342 |
| 7 | hope 1669 | love 1339 |
| 8 | yeah 1321 | hope 1275 |
| 9 | hey 1290 | na 1181 |
| 10 | twitter 1283 | bad 1149 |

Fra i positivi *love*, *lol*, *happi*, *awesom*; c'è anche *tweet*, molto frequente ma non rimosso dalle stopword. Fra i negativi *sad*, *suck*, *miss*, *hate*, ma anche *lol*, frequente in entrambe le classi (SD-08 @ 00:59:24, @ 01:00:33).

> **Nota aggiunta:** *amp* è il residuo dell'entità HTML `&amp;` (il carattere &): il preprocessing rimuove `&quot;` ma non `&amp;`, e dopo la rimozione dei caratteri speciali resta la parola *amp*. *na* viene probabilmente da *gonna*/*wanna* spezzati dal tokenizer di NLTK (*gon na*, *wan na*).

La distribuzione delle frequenze si disegna anche in scala log-log: il solito andamento *highly skewed* e la power law già viste nelle lezioni precedenti; poi la **word cloud** (`wordcloud.WordCloud`), dove le parole più frequenti appaiono più grandi (SD-08 @ 00:59:58).

```python
y_val = [x[1] for x in positive_freq.most_common()]

import math
y_final = []
for i, k, z, t in zip(y_val[0::4], y_val[1::4], y_val[2::4], y_val[3::4]):
    y_final.append(math.log(i + k + z + t))
x_val = [math.log(i + 1) for i in range(len(y_final))]
plt.plot(x_val, y_final)

from wordcloud import WordCloud
all_tokens = original_positive_tokens.apply(' '.join)
all_words = ' '.join(all_tokens)
wordcloud_positive = WordCloud().generate(all_words)
plt.imshow(wordcloud_positive, interpolation="bilinear")
```

> **Nota aggiunta:** il log-log plot del notebook somma le frequenze a gruppi di quattro ranghi consecutivi prima del logaritmo (gli `zip` con passo 4): è un modo di ridurre il rumore della coda, non un log-log "puro" rango contro frequenza.

**Topic extraction con LDA** (SD-08 @ 01:01:06). Sui tweet, brevi, "non è che funziona benissimo", ma è possibile. Si usa `LatentDirichletAllocation` di `sklearn.decomposition`, cinque topic, stopword inglesi, sull'intero testo `clean_stemmed_tweet` (non sui token):

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def get_lda_topics(tweets, n_components=5, stop_words='english'):
    #Vectorization
    tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=0.85, min_df=3, ngram_range=(1, 2))
    X = tfidf_vectorizer.fit_transform(tweets)

    # LDA model
    lda_model = LatentDirichletAllocation(n_components=n_components, random_state=42, learning_method='online')
    lda_model.fit(X)

    #Most relevant keywords per topic
    topics = []
    for idx, topic in enumerate(lda_model.components_):
        topic_keywords = [tfidf_vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics.append(topic_keywords)
    return topics

original_positive_tweets = total_data[total_data['Sentiment'] == 1]['clean_stemmed_tweet']
original_negative_tweets = total_data[total_data['Sentiment'] == 0]['clean_stemmed_tweet']
positive_topics = get_lda_topics(original_positive_tweets)
negative_topics = get_lda_topics(original_negative_tweets)
twt_topics = get_lda_topics(total_data['clean_stemmed_tweet'])   # senza tener conto della label
```

Esempi di keyword (ultime dieci per peso, quindi la più rilevante è l'ultima): topic positivo 3 "guess, congrat, birthday, hahaha, girl, ya, day, yeah, happi, hey"; topic negativo 2 "weekend, rain, start, peopl, sick, talk, poor, bad, day, suck". Spesso si combinano sentiment analysis e topicality: quali argomenti sono trattati nei tweet a maggioranza positivi e quali in quelli a maggioranza negativi (SD-08 @ 01:02:55).

> **Nota aggiunta:** LDA è un modello generativo su **conteggi** di parole; applicarlo a una matrice TF-IDF, come fa il notebook 2025, è una pratica diffusa ma non coerente con il modello. Il notebook 2026 aggiunge infatti la riga alternativa con `CountVectorizer` (commentata). Le keyword stampate sono in ordine crescente di peso, per via di `argsort()[-10:]`.

### 15.10 Esecuzione e versioni 2026 a confronto

*Non mostrato a lezione: verifiche e diff sul materiale.*

**Esecuzione.** Ho eseguito per intero, nel container (Python 3.13.16, pandas 3.0.5, scikit-learn 1.9.1, NLTK 3.10.4, TextBlob 0.20.1), le due versioni del notebook Twitter, il notebook *sample* 2026 e il notebook delle review (2025 e 2026). Risultati:

Tutti gli output numerici del notebook 2025 si riproducono **identici**: shape (79.991 e 19.998 righe, 455.577 feature), confusion matrix (6411, 2320, 2321, 8946), accuracy 0,7679267926792679, classification report, AUC 0,84, i conteggi di SIA1, SIA2 e TextBlob, i confronti con la ground truth, le frequenze delle parole e perfino le keyword LDA (che ha `random_state=42`). Le sole differenze sono di ambiente: il `dtype` delle Series di testo stampato come `str` invece di `object` (pandas 3) e le due stampe `toarray()` sostituite (sez. 15.4). La matrice TF-IDF con n-grammi 1-3 ha 1.195.654 colonne (3.050.991 valori non nulli), quella del CountVectorizer 455.577 (2.112.992 non nulli).

**Diff 2025/2026 del notebook Twitter.** Codice e output sono gli stessi; cambiano:

| Punto | 2025 (portale) | 2026 (Teams) |
|---|---|---|
| kernel | Python 3.13.5 | Python 3.10.20 |
| riferimenti alle colonne | `tweet = total_data.columns.values[2]`, `sentiment = ...[1]`, poi `columns.values[3]`, `[4]` | nomi espliciti: `total_data['Tweet']`, `['processed_tweet']`, `['clean_tweet']`, `['Sentiment']` |
| struttura | "Step 1: Preprocessing" come titolo di primo livello | sezione "Sentiment Classification with Naive Bayes" con Step 1-3 sotto |
| salvataggio | assente | nuova cella "Saving clean data for other tutorials": `total_data.to_csv("datasets/Twitter_train_clean.tsv", sep="\t", encoding="ISO-8859-1")` |
| commento della regex delle ripetizioni | | aggiunto "ALTERNATIVE: more sophisticated approaches for spelling correction" |
| conclusioni | "Naive Bayes model : 0.76" | aggiunto "Leaderboard Highest : 0.79249" |
| LDA | titolo "LDA", `tfidf_vectorizer` | titolo "Topicality with LDA", variabile `vectorizer`, alternativa `CountVectorizer` commentata |

**`Twitter_train_clean.tsv`** (23 MB, solo 2026) è il dataframe dopo il preprocessing, con le colonne `ItemID`, `Sentiment`, `Tweet`, `processed_tweet`, `clean_tweet`, `clean_stemmed_tweet`, `clean_lemmatized_tweet` più l'indice salvato come `Unnamed: 0`. Eseguendo il notebook 2026 il file si rigenera **identico** a quello distribuito (99.989 righe, 8 colonne, confronto cella per cella).

**`Sentiment_mining_Twitter-sample.ipynb`** (solo 2026) legge il TSV pulito da `../sentiment_mining/datasets/`, ne estrae un campione di 10.000 tweet (`data.sample(n=10000, random_state=42)`) e ripete solo la classificazione: CountVectorizer (1,2) con 75.856 feature, split 8.000/2.000 con `random_state=69`, MultinomialNB. Risultati nel file: accuracy 0,733, F1 0,70 (neg) e 0,76 (pos), AUC "greater than 0.80". Serve evidentemente a chi ha poca memoria o vuole iterazioni rapide. Rieseguito (le celle del notebook come script, perché sotto nbclient il kernel moriva per cause d'ambiente): stessi numeri del file, 75.856 feature, confusion matrix [[615, 256], [278, 851]], accuracy 0,733, F1 0,70 e 0,76, AUC 0,8013. Rispetto al dataset intero (accuracy 0,7679) il campione da 10.000 tweet perde circa 3,5 punti.

**`Read_Clothing_Reviews.ipynb`**: identico nelle due versioni (cambia solo il kernel); vedi sez. 16.

---

## 16. Il progetto: tre proposte e il dataset delle review

*SD-08 @ 00:45:25*

Già dopo la parte di classificazione Mele anticipa: "un progetto è ispirato a questa prima parte del tutorial" (SD-08 @ 00:45:25). Alla fine del tutorial (SD-08 @ 01:03:26) precisa:

- **Tre proposte di progetto**, "ognuna ispirata a una di queste sezioni" del tutorial: (1) sentiment classification, (2) sentiment analysis con i tool, (3) text analysis (frequenze e topic).
- **Dati**: il **dataset Twitter** visto nel tutorial.
- **Alternativa**: chi vuole usare altri dati trova nella directory `datasets` un secondo dataset, le **review di un sito che vende abbigliamento**. Non ha label positive/negative ma il **rating**, quindi va fatto "un lavoro su questa colonna di rating per tradurre questo score in una label che indica il sentiment" (SD-08 @ 01:03:56).
- **La conversione**, "come vi avevo fatto vedere in una slide" (sez. 11.1): si suddivide il range 1-5, **positivo se il rating è 4 o 5, neutro se è 3, negativo tutti gli altri** ("quelli che hanno 0 o 1 o 2", SD-08 @ 01:04:31).
- Come leggere il dataset e fare la conversione è nel notebook `Read_Clothing_Reviews.ipynb`, "sempre messo a disposizione nel materiale del corso": chi decide di lavorare con le review e non con i tweet "può da qui in poi continuare con il suo progetto di fine corso" (SD-08 @ 01:04:58).
- Dataset, stopword e contrazioni del tutorial "ve le metto a disposizione su Teams" (SD-08 @ 00:43:40).
- Spunti dati a voce durante il tutorial, utili come estensioni: provare le combinazioni della tabella dell'autore (normalizzazione, stopword, Count/TF-IDF) che lei non ha provato (SD-08 @ 00:44:51); modificare le soglie di VADER e TextBlob, anche per ridurre a due classi e rendere il confronto con la ground truth equo (SD-08 @ 00:57:06); aggiungere faccine mancanti come `T_T` alla regex (SD-08 @ 00:25:00).

### Il notebook delle review

*SD-08 @ 01:03:56*

```python
import pandas as pd

df = pd.read_csv('datasets/Clothing_review.csv')
df.head()

#Drop unnecessary columns
df = df.drop(['Title', 'Positive Feedback Count', 'Unnamed: 0', ], axis=1)
df.dropna(inplace=True)

df['Polarity_Rating'] = df['Rating'].apply(lambda x: 'Positive' if x > 3 else('Neutral' if x == 3  else 'Negative'))

df_temp = df[['Review Text', 'Polarity_Rating']]
df_temp.head()

len(df_temp)     # 22628
```

Colonne originali: `Unnamed: 0`, `Clothing ID`, `Age`, `Title`, `Review Text`, `Rating`, `Recommended IND`, `Positive Feedback Count`, `Division Name`, `Department Name`, `Class Name`. Il notebook elimina titolo, conteggio dei feedback positivi e indice, poi le righe con valori mancanti.

Statistiche che ho calcolato sul file (non nel notebook):

| | Valore |
|---|---|
| righe originali | 23.486 |
| `Review Text` mancanti | 845; `Division/Department/Class Name` mancanti: 14 |
| righe dopo `dropna` | 22.628 |
| rating 1 / 2 / 3 / 4 / 5 (file intero) | 842 / 1.565 / 2.871 / 5.077 / 13.131 |
| Positive / Neutral / Negative (dopo `dropna`) | 17.435 (77,05%) / 2.823 (12,48%) / 2.370 (10,47%) |

> **Nota aggiunta:** il dataset è molto sbilanciato verso il positivo (77%), più del Twitter dataset (56%). Per un classificatore conviene guardare F1 per classe e macro average, non solo l'accuracy (sez. 13), e valutare il bilanciamento delle classi già citato nel capitolo 01. La colonna `Recommended IND` (il cliente raccomanda il prodotto, 0/1) è un'altra possibile label binaria. Per colonne e numero di righe il file coincide con il dataset pubblico *Women's E-Commerce Clothing Reviews* (Kaggle, utente nicapotato; replicato su OpenML con 23.486 righe e rating da 1 a 5); il notebook non dichiara la fonte.

> **Correzione:** a voce gli esempi negativi sono "quelli che hanno 0 o 1 o 2" (SD-08 @ 01:04:31): nel dataset il rating va da 1 a 5, non esistono rating 0. La regola del notebook (`x > 3` positivo, `x == 3` neutro, altrimenti negativo) è comunque corretta.

> **Nota aggiunta (materiale 2026, non registrazione):** la slide `0_General_Info_SDA26.pdf` mette per iscritto le tre proposte come #SDA1 *Sentiment Classification* (rappresentazioni diverse, BoW contro TF-IDF, e classificatori diversi, Naive Bayes, SVM, alberi di decisione, deep learning, con confronto dei risultati), #SDA2 *Sentiment Analysis* (tool come TextBlob e NLTK SentimentIntensityAnalyzer, verifica con la ground truth, vocabolario di termini positivi e negativi e loro distribuzione), #SDA3 *Sentiment Analysis & Topic Extraction* (parole più discriminanti, topic modeling con LDA, Gensim o BERTopic, clustering per sentiment e topic). Dati ammessi: il dataset Twitter del tutorial, il dataset delle review di abbigliamento, oppure un dataset etichettato dal Web (per esempio Kaggle); se il progetto è supervisionato e i dati vengono dal Web senza label, serve l'etichettatura manuale. Dettagli in `assessment.md` della guida.

---

## 17. Le sfide della sentiment classification

*SD-08 @ 01:05:08*

| Sfida | Causa |
|---|---|
| Cross-domain classification | il classificatore dipende dal dominio dei dati di training |
| Cross-language classification | il classificatore dipende dalla lingua |
| Frasi difficili | condizionali, domande, sarcasmo, frasi composte (→ classificazione a livello di aspetto) |

### 17.1 Cross-domain

*SD-08 @ 01:05:39*

La classificazione è molto sensibile al dominio dei dati di training. Un classificatore allenato sui tweet non si comporta bene sulle review: su X ci sono elongated words, slang, emoticon, che nelle review mancano. Ma anche fra review: allenato su review di libri, sbaglia molto di più su review di tecnologia, che contengono termini mai visti. E la stessa parola cambia polarità con il dominio: *unpredictable* è positivo per la trama di un film, di una sitcom o di un libro, negativo per lo sterzo di un'auto o per uno smartphone che "non risponde bene ai comandi, si sta rompendo" (SD-08 @ 01:06:57).

Serve **domain adaptation** o **transfer learning**. Il dominio con i dati etichettati è il *source domain*, quello nuovo il *target domain*. Due opzioni:

- nessun dato etichettato del target: l'ideale, ma molto difficile;
- una piccola quantità di dati etichettati del target per aggiustare il training del classificatore sorgente: ciò che si fa in genere, con risultati "sicuramente migliori" (SD-08 @ 01:07:32).

### 17.2 Cross-language

*SD-08 @ 01:08:25*

Le aziende vogliono confrontare le opinioni sui loro prodotti in paesi diversi. Molti tool sono sviluppati per l'inglese; alcune lingue popolari sono supportate (tedesco, spagnolo; a voce anche italiano e francese), altre no: lingue rare parlate da popolazioni ristrette (il **tanema** delle Isole Salomone, l'**ongota** dell'Etiopia), ma anche lingue parlate da molte persone e poco rappresentate sul Web, perché i parlanti online usano l'inglese e mancano esempi testuali per allenare i modelli.

- Se esiste un **lessico** per la lingua (per esempio italiano o cinese), si classifica il documento originale con un approccio basato sul lessico.
- Se il lessico manca o è povero, si usa la **traduzione automatica** verso la lingua sorgente e il tool già allenato su di essa.

Con **source language** = lingua popolare con dati etichettati, lessici di soggettività e tool (inglese, tedesco) e **target language** = lingua povera di dati e tool (swahili, tanema), tre strategie (SD-08 @ 01:10:02):

| # | Strategia |
|---|---|
| 1 | tradurre le frasi dal target alla lingua sorgente e classificarle con il classificatore della lingua sorgente |
| 2 | tradurre il corpus di training dalla lingua sorgente al target e riaddestrare un classificatore *corpus-based* nella lingua target |
| 3 | tradurre un lessico di sentiment o di soggettività dalla lingua sorgente al target e costruire un classificatore basato sul lessico nel target |

La scelta dipende dai dati disponibili; "in genere la prima strategia funziona abbastanza bene" (SD-08 @ 01:11:14).

### 17.3 Frasi condizionali

*SD-08 @ 01:11:14*

Descrivono implicazioni o situazioni ipotetiche e le loro conseguenze; hanno due clausole, condizione e conseguenza. Le parole di sentiment non distinguono una frase opinionated da una che non lo è:

- "If someone makes a reliable car, I will buy it.": *reliable* è positivo, ma la frase non esprime sentiment verso nessuna auto o marca. È un'ipotesi: vorrei che un genio della meccanica producesse un'auto che non si rompe mai.
- "If your Nokia phone is not good, buy this Samsung phone": sembra comparativa (Samsung meglio di Nokia), ma è ipotetica: è positiva sul Samsung, non esprime un'opinione sul Nokia, perché non sappiamo se l'altro utente abbia davvero un Nokia che non funziona (SD-08 @ 01:12:19).

Frasi di tipo diverso vanno analizzate in modo diverso: un metodo per le frasi non condizionali può non funzionare per le condizionali. Contro una soluzione unica (*one-technique-fit-all*) si preferisce **divide-and-conquer**: prima si classificano le frasi in condizionali e non condizionali (approcci supervisionati con feature linguistiche e POS tag delle parole di sentiment), poi si applica la sentiment classification classica alle seconde e un addestramento diverso alle prime. Le condizionali però sono poche, e l'addestramento è difficile (SD-08 @ 01:12:49).

> **Nota aggiunta:** VADER e TextBlob, sulla frase dell'auto affidabile, danno entrambi 0 (`verifica_sd06.py`, sezione 9): qui, per una volta, il lessico non sbaglia, perché *reliable* non ha peso nei loro dizionari.

### 17.4 Domande

*SD-08 @ 01:13:19*

"Can anyone tell me where I can find a good Nokia phone?": contiene *good*, ma non è opinionated, perché chiede un'informazione. Non basta però dire "punto interrogativo, quindi non opinionated": "Can anyone tell me how to fix this lousy Nokia phone?" è una domanda che esprime un'opinione negativa implicita, il telefono è *lousy*, si è rotto. "Per questo tipo di problema non c'è ancora una soluzione" (SD-08 @ 01:14:47).

### 17.5 Sarcasmo

*SD-08 @ 01:14:47*

Forma sofisticata di linguaggio, in cui si dice o si scrive il contrario di ciò che si intende; studiata in linguistica, psicologia, scienze cognitive. È uno dei problemi più difficili perché **inverte la polarità**: "What a great car! It stopped working in two days" verrebbe classificata positiva per *great* e il punto esclamativo, mentre la seconda frase, un fatto non opinionated, rivela un giudizio negativo. Raro nelle review di prodotti, molto frequente nei tweet (politica) e nelle discussioni dei forum.

Approcci: supervisionati (SVM, regressione logistica). Feature: unigrammi e feature da dizionario, più interiezioni (*ah*, *oh*, *yeah*), punteggiatura (`!`, `?`), emoticon, slang, @username di menzioni e risposte. Esempio a voce: in un botta e risposta su un politico, a un'affermazione positiva un altro utente risponde "sì, come no": formalmente un'affermazione, in realtà una presa in giro (SD-08 @ 01:16:26).

> **Nota aggiunta:** le feature della slide vengono dal lavoro di González-Ibáñez, Muresan e Wacholder (2011) su Twitter, citato da Liu (par. 4.4): con SVM e regressione logistica, nella classificazione a tre vie (sarcastico, positivo, negativo), la migliore accuracy era solo del 57%.

### 17.6 Frasi composte

*SD-08 @ 01:16:59*

Un'opinione positiva sull'entità non implica un'opinione positiva su tutti i suoi aspetti. "This camera is great! I could take amazing pictures, but the battery life is short":

| Aspetto | Polarità |
|---|---|
| generale: la fotocamera | positiva |
| qualità delle foto | positiva |
| durata della batteria | negativa |

Serve la **feature-level** (o *aspect-based*) sentiment analysis: scoprire gli aspetti e il sentiment su ciascuno. Ma resta aperta la domanda sull'etichetta complessiva: conta di più l'aspetto generale o la batteria, visto che a un certo punto la fotocamera si è spenta e l'utente non ha più potuto fare foto? "Rimane anche questo un problema aperto" (SD-08 @ 01:17:35).

---

## 18. Riepilogo e compiti

*SD-08 @ 01:18:30*

- **Sentiment analysis** (opinion mining): area di ricerca popolare con molti domini applicativi, dal marketing all'opinion tracking.
- **Opinione**: quintupla (entità, aspetto, sentiment, holder, tempo); fatti contro opinioni; tipi regular/comparative, direct/indirect, explicit/implicit.
- **Sentiment classification**, due sottoproblemi: subjectivity classification (opinionated o no) e orientation detection (positivo, negativo, neutro); a livello di documento, frase o aspetto.
- **Approcci**: non supervisionati (lessico, pattern sintattici con PMI/SO); supervisionati (Naive Bayes) con workflow preprocessing, split train/test, classificazione, valutazione.
- **Valutazione**: confusion matrix, precision, recall, accuracy, F-score, macro e micro average, ROC e AUC.
- **Sfide**: cross-domain, cross-language, condizionali, domande, sarcasmo, frasi composte.

**Compiti** (slide *Homework*; a voce SD-08 @ 01:20:58):

- leggere i capitoli 1, 2, 3 e 4 di *Sentiment Analysis and Opinion Mining* (le parti indicate dalle slide);
- ripetere il tutorial `Sentiment_mining_Twitter.ipynb`.

---

## Glossario

| Termine | Significato nel corso |
|---|---|
| Sentiment analysis / opinion mining | analisi delle opinioni espresse nel testo verso entità e loro attributi |
| Opinionated text | testo che esprime un'opinione (soggettivo) |
| Subjectivity classification | classificare un testo come oggettivo o soggettivo |
| Polarity / orientation detection | classificare un testo soggettivo come positivo, negativo o neutro |
| Opinion holder | chi esprime l'opinione |
| Quintupla (e, a, s, h, t) | entità, aspetto, sentiment, holder, tempo |
| Opinion trending | evoluzione delle opinioni nel tempo |
| Regular / comparative | opinione su un'entità / confronto fra entità |
| Direct / indirect | opinione espressa direttamente / attraverso gli effetti su altre entità |
| Explicit / implicit | frase soggettiva / frase oggettiva che implica un'opinione |
| Document / sentence / feature (aspect) level | granularità della classificazione |
| Sentiment shifter | espressione che cambia la polarità: negazioni, avverbi contrari (*although*, *however*) |
| Elongated word | parola allungata per enfasi (*wooow*) |
| Lexicon-based | approccio con dizionario di parole con score di sentiment |
| PMI | log2 del rapporto fra co-occorrenza osservata e attesa sotto indipendenza |
| SO (sentiment orientation) | PMI con *excellent* meno PMI con *poor* |
| Appraisal groups | classi di valutazione assegnate a mano a parole e frasi |
| Ground truth | label assegnate da etichettatori umani, usate per valutare |
| Class-conditional independence | assunzione "naive": feature indipendenti data la classe |
| Prior / posterior | P(h) / P(h\|D) |
| Precision / recall / F-score | TP/(TP+FP) / TP/(TP+FN) / media armonica |
| Macro / micro / weighted average | media delle metriche per classe / metrica sui conteggi aggregati / media pesata per support |
| Support | numero di esempi reali di una classe |
| ROC / AUC | curva TPR contro FPR al variare della soglia / area sotto la curva |
| Domain adaptation / transfer learning | adattare un classificatore dal dominio sorgente al target |
| VADER | lessico e regole per il sentiment sui social, usato dal `SentimentIntensityAnalyzer` di NLTK |
| Compound | score aggregato di VADER in [-1, 1] |

## Punti incerti

- **SD-08 @ 00:05:48:** la trascrizione dice per la recall "true positive diviso i false negative": quasi certamente "diviso true positive più false negative", come nella slide. Trattato come errore di trascrizione, non come errore della docente.
- **SD-08 @ 00:44:51:** "l'autore aveva ottenuto 0 76 01, a noi invece 0 76 e 79" interpretato come 0,7601 e 0,7679, confrontando con la tabella del notebook e l'output a schermo (frame 00:42:04). La lettura "0,76 contro 0,79" non trova riscontro.
- **SD-08 @ 00:25:00:** "viene scritta in questo modo già con 22 s" [?]: probabilmente "con due u e due s", riferito a *juusst* (frame 00:24:28).
- **SD-08 @ 00:40:44:** il politico americano scomparso del dataset di tweet non è nominato [?].
- **SD-08 @ 01:13:27:** bassa confidenza Whisper ("ne ha nevante lmi where i can find the good occhia phone"): ricostruito dalla slide come "Can anyone tell me where I can find a good Nokia phone?".
- **SD-08 @ 00:55:18:** bassa confidenza sui conteggi di TextBlob ("58.700 ... 30.000 circa negativa e per 10.000 positiva"): coerente con il notebook (58.701, 30.707, 10.581).
- **SD-07 @ 01:13:35:** "la frase e l'associo eccellente ... con una parola negativa, ad esempio, pur": *pur* è *poor*.
- **SD-07 @ 00:09:25 e @ 00:21:55:** due soglie diverse per trasformare il rating in label positiva ("almeno tre" e "più di tre"); la slide 37 dà gli schemi completi.
- **Inizio della parte supervisionata:** la nota della docente dice "dal minuto 50"; nella trascrizione la frase di passaggio è a SD-06 @ 00:49:53 e la slide-titolo "Supervised Approaches" compare nel frame 00:50:01.
- **Slide nel video contro PDF:** alcune slide registrate hanno un testo leggermente diverso dal PDF SDA25 (per esempio "Subjectivity Analysis / Polarity Detection" in SD-07 @ 00:48:34 contro "Subjectivity Classification / Orientation (Polarity) Detection" nel PDF). Contenuto equivalente.
- Trascrizioni corrette in silenzio: "Naif Bayes", "life pace", "nice bass" = Naive Bayes; "ShakeItLearn", "sciacchi turno" = scikit-learn; "Spacy" = spaCy; "Wornet" = WordNet; "lde" = LDA; "auke", "hawk" = AUC; "rock" = ROC; "cargo" = Kaggle; "Text Blog" = TextBlob; "demented recognition" = named entity recognition; "point-to-multiple information" = pointwise mutual information.

## Materiale usato

- Video e trascrizioni: `out/SD-07/`, `out/SD-06/` (da 00:49:53), `out/SD-08/` (trascrizioni, segmenti a bassa confidenza, frame e indice OCR)
- Nota sull'ordine: `Materiale/Portale/estratti/important_note_about_videos.txt`
- Slide: `Materiale/Portale/estratti/6_Sentiment_Analysis_SDA25.pdf`; `Materiale/Teams/estratti/Slides/6_Sentiment_Analysis_SDA26.pdf`; `0_General_Info_SDA26.pdf` (solo la pagina *Assignment: Proposals*)
- Notebook e dati: `Materiale/Portale/estratti/sentiment_mining/` (`Sentiment_mining_Twitter.ipynb`, `Read_Clothing_Reviews.ipynb`, `assets/`, `datasets/`); `Materiale/Teams/estratti/Tutorials/sentiment_mining/` (stessi più `Sentiment_mining_Twitter-sample.ipynb` e `datasets/Twitter_train_clean.tsv`)
- Libro: `Materiale/Portale/estratti/books/SentimentAnalysis-and-OpinionMining.pdf` (cap. 1-4; par. 2.1.1, 3.2, 3.5, 4.4)
- Verifiche: `verifica_sd06.py` e `verifica_sd06_output.txt` in questa cartella; notebook 2026 eseguito `Sentiment_mining_Twitter_2026.eseguito.ipynb` (la copia eseguita del 2025 non è stata conservata; output identici)
- Fonti esterne: README di vaderSentiment (soglie del compound); OpenML, dataset 43673 (*Women's Clothing E-Commerce*)
