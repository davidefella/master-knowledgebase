# Capitolo 01: Introduzione a Social Data Analytics

**Lezione:** SD-01 (1:14:15), Dott.ssa Ida Mele, IASI-CNR (ida.mele@iasi.cnr.it)
**Slide:** `0_General_Info_SDA25.pdf`, `1_Introduction_SDA25.pdf` (versioni SDA26 su Teams: differenze solo di refusi, salvo `0_General_Info`, vedi sez. 1)
**Riferimento:** Introduzione del libro *Social Media Data Mining and Analytics* (Szabo, Polatkan, Boykin, Chalkiopoulos, Wiley)
**Fonti 2026:** delle registrazioni Teams è leggibile solo Teams 4 (le altre trascrizioni sono generate in inglese su parlato italiano). Le indicazioni della 2026 sono nei riquadri "Integrazione Teams 2026".

## Indice

1. [Il corso: programma, riferimenti, strumenti, idoneità](#1-il-corso-programma-riferimenti-strumenti-idoneità)
2. [Che cos'è Social Data Analytics](#2-che-cosè-social-data-analytics)
3. [Motivazioni: perché analizzare i dati social](#3-motivazioni-perché-analizzare-i-dati-social)
4. [Sfide: big data, MapReduce, le 5 V](#4-sfide-big-data-mapreduce-le-5-v)
5. [Social media: definizione e storia](#5-social-media-definizione-e-storia)
6. [Gli ingredienti dei social media ed esempi di piattaforme](#6-gli-ingredienti-dei-social-media-ed-esempi-di-piattaforme)
7. [Data analytics, data science e i "unicorni"](#7-data-analytics-data-science-e-gli-unicorni)
8. [Data mining contro data analytics](#8-data-mining-contro-data-analytics)
9. [Progetti data-driven: pattern, task e step](#9-progetti-data-driven-pattern-task-e-step)
10. [Riepilogo e compiti](#10-riepilogo-e-compiti)

---

## 1. Il corso: programma, riferimenti, strumenti, idoneità

*SD-01 @ 00:00:09*

Il corso vale 3 CFU per 15 ore. Il programma segue gli "ingredienti" delle piattaforme sociali:

| Blocco | Contenuto | Lezione (slide SDA26) | Capitolo della guida |
|---|---|---|---|
| Introduzione | definizione, motivazioni, sfide | Lecture 1 | 01 |
| Attività degli utenti | analisi delle azioni degli utenti | Lecture 2 | 02 |
| Reti sociali | grafi: nodi = utenti, archi = relazioni o interazioni | Lecture 3 | 03 |
| Natural Language Processing | analisi del testo in linguaggio naturale | Lectures 4, 5, 6 | 04, 05 |
| Sentiment analysis | sentiment classification | Lectures 7, 8 | 06 |
| Tutorial Python | NLP e sentiment analysis | trasversali | dentro i capitoli |

La sentiment analysis, detta anche *sentiment classification*, classifica un estratto di testo prima come *opinionated* o no, e poi, se esprime un'opinione, come positivo o negativo verso un prodotto o un servizio (SD-01 @ 00:02:24).

> **Integrazione Teams 2026:** nelle slide SDA26 il corso è da 3 CFU / 15 ore per il master di I livello e da 4 CFU / 20 ore per il II livello, che aggiunge "Deep Learning for NLP & SA with tutorials (only for MDA II level)" (slide `7_DL_SDA26_II_level.pdf`, lezioni Teams 8 e 9). Per il I livello Mele dichiara: "seguirò lo stesso programma dell'anno scorso, quindi il materiale è sempre quello e le lezioni sono sempre quelle" (Teams 4 @ 0:02:44). Questa guida copre il I livello.

### I due libri di riferimento

*SD-01 @ 00:03:13*

**[1] Szabo, Polatkan, Boykin, Chalkiopoulos, *Social Media Data Mining and Analytics*, Wiley.** Gli autori lavoravano nell'industria: è un libro con molti esempi pratici, poco teorico e orientato alle applicazioni. Si studiano l'Introduzione e i capitoli 1, 2 e 4, che rispondono a tre domande:

| Capitolo | Domanda | Oggetto | Capitolo della guida |
|---|---|---|---|
| 1 | *The Who of Social Media* | gli utenti e le loro azioni | 02 |
| 2 | *The How of Social Media* | come gli utenti sono connessi: graph mining su relazioni esplicite e implicite | 03 |
| 3 | *The When of Social Media* | analisi temporale (time series) delle azioni degli utenti | **saltato** |
| 4 | *The What of Social Media* | il contenuto testuale, analizzato con NLP | 04, 05 |

Il capitolo 3 è saltato anche negli anni precedenti, "per dare più spazio alla seconda parte del corso" (SD-01 @ 00:06:24).

Le relazioni **esplicite** nascono da una scelta dell'utente: chiedere l'amicizia (Facebook) o seguire qualcuno (X, Instagram). Le relazioni **implicite** nascono intorno a contenuti condivisi: su YouTube o Wikipedia un utente carica o scrive un contenuto, un altro lo commenta o lo modifica, e fra i due si crea un legame anche se non si sono mai incontrati. Anche questo legame si rappresenta come un arco in un grafo (SD-01 @ 00:05:13).

**[2] Bing Liu, *Sentiment Analysis and Opinion Mining*, Morgan & Claypool.** Liu ha studiato a lungo la sentiment analysis e ha scritto molte survey sullo stato dell'arte (SD-01 @ 00:07:30).

| Capitoli | Argomento |
|---|---|
| 1 e 2 | definizione del problema di sentiment analysis |
| 3 | *document-level* sentiment classification: il classificatore si applica a tutto il testo |
| 4 | *sentence-level* sentiment classification: si classificano le singole frasi, utile per testi più lunghi di un tweet, come le review |
| 5 | *feature/aspect-level*: un'opinione per ogni caratteristica del prodotto |

L'esempio del livello di aspetto è una macchina fotografica (SD-01 @ 00:09:16): l'opinione può essere molto positiva sulla qualità delle foto e sullo zoom, e meno positiva sulla compattezza e sul peso, quindi sulla praticità di trasporto. Una sola etichetta per tutta la review perderebbe questa distinzione.

> **Nota aggiunta:** la slide `0_General_Info` (2025 e 2026) elenca per Liu i capitoli 1-5, mentre a voce, in SD-08 @ 01:21:06, Mele rimanda ai "primi quattro capitoli". Il capitolo 5 compare nella slide e nell'esempio della macchina fotografica, ma la lezione di sentiment analysis non lo tratta in dettaglio: vedi capitolo 06.

Entrambi i libri sono nel materiale del corso (`books.zip` sul portale).

### Strumenti

*SD-01 @ 00:10:24*

I tutorial usano **Python 3** e **Jupyter Notebook**. Mele motiva la scelta del notebook: fra una cella di codice e l'altra si inserisce testo, e i suoi tutorial spiegano in una cella testuale cosa fa ogni cella di codice. Il vantaggio vale anche per chi sviluppa, perché un unico blocco di codice senza commenti diventa illeggibile anche per chi l'ha scritto. Per installare tutto insieme consiglia **Anaconda**, che lei stessa usa sul portatile.

### Idoneità

*SD-01 @ 00:11:49*

L'idoneità si ottiene con **un unico progetto** per i corsi del percorso *Social Data and Natural Language Processing*, che vale **9 crediti** complessivi: il corso di Mele, il corso di "Enrico" [?], il corso di NLP tenuto da un'azienda e il corso del prof. "Maielli" [?], che segue immediatamente l'ultima lezione di Mele. I progetti vengono presentati al termine dei corsi, forse già da "Maielli" a metà del suo corso.

> **Integrazione Teams 2026:** la slide `0_General_Info_SDA26.pdf` sostituisce la pagina "Exam" del 2025 con due pagine "Assignment" (tracce SDA1-SDA3, dati, modalità). I dettagli sono in `assessment.md` della guida. In Teams 4 @ 0:00:03 Mele precisa che le proposte sono "per chi è poco creativo": chi ha già un dataset proprio, di lavoro o di un altro corso, la contatta, lo descrive insieme a ciò che vuole farci, e si concorda il progetto.

---

## 2. Che cos'è Social Data Analytics

*SD-01 @ 00:12:42*

La lezione segue l'Introduzione del libro [1], in un ordine diverso: Mele ha invertito alcune parti "per essere più sintetica". Le slide vanno usate "come una sorta di indice" per decidere quali parti del capitolo approfondire e quali leggere superficialmente (SD-01 @ 00:13:36). Lo dice di tutte le slide del corso.

**Definizione.** Social Data Analytics è *data analytics applicata ai dati dei social media*. L'obiettivo, citato dal libro, è "analyzing raw data to understand how social media services are used": analizzare i dati grezzi per capire come gli utenti usano i servizi delle piattaforme.

La definizione apre due domande, che organizzano il resto della lezione:

```
                 Social Data Analytics
                /                     \
        Social Media              Data Analytics
  - cos'è una piattaforma social?    - cos'è la data analytics?
  - quando e perché si è diffusa?    - perché è importante?
  - come la usano gli utenti?        - perché i data scientist sono "unicorni"?
  - perché i suoi dati valgono?      - task e step dei progetti data-driven
```

### Da dove vengono i dati

*SD-01 @ 00:14:46*

| Provenienza | Esempi | Accesso |
|---|---|---|
| **Pubblici**: condivisi dagli utenti sul web | commenti sotto un video YouTube, status update su un profilo Facebook pubblico, foto, video, podcast | scaricabili, anche con API (librerie per Java, Python ecc.), con restrizioni della piattaforma |
| **Nei log**: file molto grandi delle aziende | visualizzazioni, like, reazioni, rating, review, connessioni, relazioni, interazioni | interni all'azienda, a volte anonimizzati con un ID numerico; alcuni pubblicati su siti di dataset, altri custoditi "gelosamente" perché servono alla profilazione |

Esempi di restrizioni citati a voce (SD-01 @ 00:15:16): con le API di Facebook si scaricano solo i post visibili al proprio profilo (pubblici, amici, eventualmente amici degli amici se l'hanno consentito); per X "in passato" c'era un limite al numero di tweet scaricabili al giorno.

> **Nota aggiunta (fatti esterni, verificati il 22/10/2026 su fonti secondarie):** le condizioni sono più restrittive di quanto suggerisce la lezione. Per X, l'accesso gratuito in lettura è finito di fatto nel febbraio 2023; dal 2026 gli sviluppatori nuovi pagano a consumo (circa 0,005 $ per post letto, ricerca solo sugli ultimi 7 giorni), mentre i piani Basic e Pro restano solo per chi li aveva già ([postproxy.dev](https://www.postproxy.dev/blog/x-api-pricing-2026/), fornitore con interesse commerciale: le cifre vanno confermate sulla documentazione di X). Per Facebook, dopo il caso Cambridge Analytica (2018) la Graph API non permette più di leggere liberamente i post degli utenti: serve il loro consenso esplicito tramite app approvata. Questa seconda informazione non l'ho ricontrollata. Conseguenza pratica per i progetti: si lavora su dataset già pubblicati, come quelli del corso o di Kaggle.

### Tre tipi di dati

*SD-01 @ 00:18:05*

| Tipo | Esempi | Note dalla lezione |
|---|---|---|
| **Non strutturati** | testo: post, status update, commenti, review, tag delle foto | gran parte del contenuto online è testo |
| **Semi-strutturati** | informazioni del profilo: genere, fascia d'età, località, lavoro, interessi | gestibili per categorie (fasce d'età), ma un campo libero come gli interessi ("pasticceria" invece del tag predefinito "cooking") degenera in testo |
| **Strutturati** | archi di un grafo: amicizia, following/follower, gruppi | anche utenti senza connessione esplicita formano gruppi se hanno condiviso contenuti simili o commentato gli stessi post |

> **Nota aggiunta:** la classificazione è quella del libro e del corso. Da un punto di vista database, "strutturati" qui significa rappresentabili come relazioni (coppie utente-utente, appartenenza a gruppi), cioè tabelle di archi.

---

## 3. Motivazioni: perché analizzare i dati social

*SD-01 @ 00:20:26*

L'idea è estrarre **pattern di comportamento** degli utenti e, se possibile, **predirne il comportamento futuro**. I dati grezzi sembrano inutili; aggregati e analizzati diventano una fonte d'informazione per:

- supportare i processi decisionali;
- scopi di business;
- **guadagnare**, soprattutto con il *targeted advertisement*, cioè annunci mirati a un piccolo gruppo di utenti o a un singolo utente grazie alla profilazione.

Aziende, imprese ed enti analizzano i dati social per fare ricerca, migliorare i servizi, fare marketing e pubblicità. Le piattaforme social e i motori di ricerca (Google, Bing) sono gratuiti per l'utente e "vivono grazie agli annunci" (SD-01 @ 00:21:12).

### Il fine "nobile" e quello economico

*SD-01 @ 00:21:54*

Migliorare il servizio e aumentare i ricavi vanno nella stessa direzione: se raccomando contenuti che l'utente trova interessanti (news, i video "laterali" di YouTube), l'utente torna e resta di più sulla piattaforma, e più tempo passa più annunci vede. È la *user engagement* richiamata nel riepilogo (SD-01 @ 01:12:07).

Mele descrive il modello di remunerazione degli annunci con cifre puramente illustrative: l'inserzionista paga per la visualizzazione, di più per il click, ancora di più per una transazione conclusa. Con 5 centesimi a visualizzazione, 10 a click e 100 a transazione, alla piattaforma conviene anche la sola visualizzazione se i numeri sono grandi, perché il ricavo è 5 centesimi moltiplicato per milioni di visualizzazioni. Da qui i siti con molti pop-up, a volte ingannevoli: si crede di chiudere il pop-up e si viene rediretti (SD-01 @ 00:23:36).

> **Nota aggiunta:** nel gergo pubblicitario i tre modelli si chiamano CPM (costo per mille impressioni), CPC (costo per click) e CPA (costo per acquisizione/azione). La lezione non usa questi termini.

### Profilazione: il telefono "che ascolta"

*SD-01 @ 00:24:10*

La slide mostra un meme (scena della serie *Friends*, "My phone when I say I want to buy something": le icone di YouTube, Instagram, Facebook e Google origliano alla porta). Mele cita la convinzione diffusa che le app usino il microfono per profilare, e la definisce "un discorso un po' complottista", senza escluderlo. Propone una spiegazione più semplice: la ricerca fatta sul PC con Chrome viene memorizzata nei cookie e il profilo sincronizzato fra dispositivi la porta anche sul telefono. Racconta di aver visto per mesi annunci di lavatrici dopo averne comprata una in negozio, perché aveva confrontato i modelli online.

Contromisure citate: disabilitare i cookie, cancellare periodicamente la cronologia, usare motori di ricerca che non profilano, come DuckDuckGo (SD-01 @ 00:26:25).

---

## 4. Sfide: big data, MapReduce, le 5 V

*SD-01 @ 00:27:15*

### Scala e scalabilità

Più dati si hanno, migliori sono i risultati: si parla di gigabyte o terabyte. È il campo della **Big Data Analytics**, il cui problema principale è la **scalabilità**. Un personal computer, magari vecchio e con poca RAM e poco disco, non gestisce file di questa dimensione. I dati grezzi poi non sono aggregati: un record ripete le informazioni dell'utente per ogni singola azione, e solo l'aggregazione riduce le dimensioni (SD-01 @ 00:27:48).

### Dal supercomputer ai cluster di commodity hardware

*SD-01 @ 00:28:25*

L'evoluzione raccontata da Mele:

1. **Supercomputer.** Le aziende compravano un server molto potente. Il difetto è il *single point of failure*: se il server si guasta il servizio si ferma, e ripararlo o sostituirlo costa.
2. **Cluster di commodity hardware.** Molti server economici, con disco e RAM modesti, collegati in una rete interna. I dati vengono suddivisi fra i nodi ed elaborati in modo **distribuito e parallelo**, con **replica** dei dati: se un nodo si guasta, si usa la copia su un altro nodo. Il difetto è che servono programmatori esperti e ben pagati, perché occorre gestire a mano la comunicazione fra nodi, i risultati parziali e la loro aggregazione.
3. **MapReduce.** Il paradigma rende semplice la programmazione distribuita: il programmatore scrive solo una funzione *map* e una funzione *reduce*, senza pensare alla comunicazione fra nodi. Il **map** divide i dati e svolge piccole operazioni su ciascuna parte; il **reduce** aggrega i risultati parziali nel risultato finale (SD-01 @ 00:30:47). Un nodo guasto si sostituisce rapidamente con hardware economico, senza interrompere il servizio grazie alla replica.

> **Nota aggiunta:** MapReduce è stato descritto da Google (Dean e Ghemawat, 2004); l'implementazione open source più diffusa è Hadoop. La descrizione della lezione è semplificata: fra map e reduce c'è una fase di *shuffle* che raggruppa per chiave le coppie (chiave, valore) emesse dai mapper, e ogni reducer riceve tutte le coppie di una stessa chiave. Esempio canonico, il conteggio delle parole:

```python
# Nota aggiunta: simulazione locale di MapReduce (word count), non mostrata a lezione.
from collections import defaultdict

documenti = ["social data analytics", "data analytics applied to social media data"]

# map: ogni documento emette coppie (parola, 1)
coppie = [(parola, 1) for doc in documenti for parola in doc.split()]

# shuffle: raggruppa per chiave
gruppi = defaultdict(list)
for parola, uno in coppie:
    gruppi[parola].append(uno)

# reduce: aggrega i valori di ogni chiave
conteggi = {parola: sum(valori) for parola, valori in gruppi.items()}
print(conteggi)
# {'social': 2, 'data': 3, 'analytics': 2, 'applied': 1, 'to': 1, 'media': 1}
```

### Le 5 V dei big data

*SD-01 @ 00:31:38*

| V | Significato | Esempio della lezione |
|---|---|---|
| **Volume** | grandi quantità di dati | GB, TB |
| **Variety** | tipi e fonti diversi | strutturati (archi di un grafo), non strutturati (testo) |
| **Velocity** | il contenuto cambia rapidamente | stream di news, stream di tweet |
| **Value** | come ricavare valore dai dati | grezzi non valgono nulla, aggregati e analizzati valgono molto |
| **Veracity** | ci si può fidare? le conclusioni reggono in scenari simili? | un comportamento osservato su Instagram vale anche su X, che ha lo stesso meccanismo following/follower? |

---

## 5. Social media: definizione e storia

*SD-01 @ 00:33:52*

Una piattaforma di social media permette alle persone di **connettersi e condividere informazioni**. Le tappe raccontate:

- **Bulletin board system** (anni '80): bacheche digitali, diffuse anche nelle università. Erano la versione online della bacheca fisica ("cerco stanza vicino al campus", "vendo il motorino"). Lo studente dell'Ohio che va a Stanford può cercare casa senza viaggiare. Sono i primi esempi di piattaforme sociali.
- **Web 2.0**: prima, da una parte chi sapeva scrivere HTML e PHP o forniva contenuti (giornalisti) e creava le pagine, dall'altra gli utenti ordinari che le leggevano. Con il Web 2.0 l'utente diventa anche autore. I blog permettono di pubblicare testo e immagini senza conoscere l'HTML; poi arrivano Facebook e Twitter, oggi X, nato come sito di *microblogging* con update brevi, "al massimo 140 caratteri, se non erro" (SD-01 @ 00:37:28).
- **Ogni servizio diventa sociale**: e-commerce con rating e review (Amazon, eBay), dove gli utenti votano anche l'utilità delle review altrui; dizionari online con forum (WordReference), dove madrelingua e non madrelingua discutono l'uso di una parola in contesti diversi.
- **Dispositivi mobili**: lo smartphone è "internet in your pocket". Prima si scattavano le foto in vacanza, le si scaricava sul PC a casa e se ne condividevano poche; oggi si pubblica in tempo reale. Mele cita i casi di furti in appartamenti di persone che pubblicavano foto dalle Maldive, e l'uso delle app da parte di persone anziane, prima poco tecnologiche.

> **Nota aggiunta:** il limite di 140 caratteri di Twitter è stato portato a 280 nel novembre 2017; oggi gli abbonati a X Premium possono pubblicare post molto più lunghi.

Il punto che distingue una piattaforma social da un sito di notizie, aziendale o istituzionale: **esiste grazie agli utenti**. Senza gli utenti, Facebook o Instagram sarebbero "contenitori vuoti", perché sono gli utenti a fornire i contenuti (SD-01 @ 00:41:15).

### Che cosa permettono

*SD-01 @ 00:41:47*

- Essere connessi globalmente: con familiari, amici, colleghi, ovunque (social network, ma anche chat come WhatsApp); per le aziende, con i clienti (piattaforme di rating sui siti di e-commerce).
- **Social network** (Facebook, X): fatti di **connessioni sociali**, su cui si condividono contenuti, foto, video, file multimediali, news.
- **Piattaforme di content sharing** (Wikipedia, YouTube): fatte di **interazioni sociali intorno al contenuto condiviso**.

La slide raccoglie le categorie in una mappa intorno a "Social Media": microblogging, weblog, network, chat, forum, community, bookmarking, podcast, wiki, video, rating, pictures.

Esempi meno ovvi citati a voce (SD-01 @ 00:44:44): il **bookmarking** (Pinterest: salvo un'immagine per me, ma anche per condividerla) e i **forum di domande e risposte** (Quora, Yahoo Answers), che collegano chi segue gli stessi argomenti o interagisce intorno a una domanda.

---

## 6. Gli ingredienti dei social media ed esempi di piattaforme

*SD-01 @ 00:45:14*

Si parla di social media quando ci sono tre ingredienti:

1. **Utenti**: l'ingrediente principale, senza il quale c'è un contenitore vuoto.
2. **Contenuto generato dagli utenti** (*user-generated content*): dati non strutturati, tipicamente testo in linguaggio naturale. Articoli di blog, status update, post, tweet, review e commenti, domande e risposte nei forum. Le review non riguardano solo prodotti ma anche servizi: un albergo su Booking (personale gentile e pulizia ottima, vista sul palazzo di fronte deludente), un ristorante (buon rapporto qualità-prezzo, servizio lento o scortese).
3. **Connessioni fra utenti**:
   - di amicizia (Facebook);
   - di following-follower (Instagram, X);
   - **implicite**, basate sulle interazioni, per esempio utenti che hanno contribuito allo stesso articolo di Wikipedia.

Questi tre ingredienti sono anche la mappa del corso: gli utenti nel capitolo 02, le connessioni nel capitolo 03, il contenuto nei capitoli 04-06.

### Esempi

*SD-01 @ 00:47:31*

| Piattaforma | Relazione | Caratteristica |
|---|---|---|
| **Facebook** | amicizia, nata **bidirezionale**: la richiesta va confermata, altrimenti si vedono solo le informazioni pubbliche (oggi in alcuni casi si può anche solo "seguire") | aggiornamenti da amici, parenti, conoscenti, anche lontani |
| **X** (ex Twitter) | following, **non necessariamente reciproco** | profili molto seguiti (attori, cantanti, politici); chi segui compare nella tua timeline ("se seguo Lady Gaga vedrò i post di Lady Gaga"), insieme a contenuti suggeriti dalla piattaforma |
| **LinkedIn** | professionale | mette in contatto chi cerca lavoro e le aziende che cercano competenze |
| **Wikipedia, YouTube, Flickr** | implicita, intorno al contenuto | la rete sociale è un *facilitatore* per co-creare o fruire il contenuto: si collegano persone che non si conoscono ma hanno interessi simili |

Differenza chiave: su Facebook si collegano persone che si conoscono, sulle piattaforme di content sharing persone che condividono interessi.

---

## 7. Data analytics, data science e gli "unicorni"

*SD-01 @ 00:49:44*

**Data analytics** è un *umbrella concept*: un "grande ombrello" che raccoglie le tecniche usate per estrarre informazioni e insight dai dati grezzi. Definizione: *la scienza di analizzare dati grezzi per trarne conclusioni*.

Mele usa come sinonimi data analytics, data mining e data science, pur riconoscendo che alcuni autori li distinguono (sezione 8). Due specializzazioni:

- **Predictive analytics**: il focus è sulla predizione del comportamento futuro degli utenti, per esempio per raccomandare video, news, prodotti o servizi.
- **Big data analytics**: il focus è sui dataset su larga scala, quindi sul problema della scalabilità (supercomputer o MapReduce, sezione 4).

**Perché è importante.** I dati sono "il nuovo petrolio" (slide: *Data is the new oil*) perché si convertono in denaro. Vengono dal web, dalla domotica, dai videogiochi: tutto ciò che permette di capire gli interessi degli utenti e di profilarli. Con gli strumenti giusti e abbastanza potenza di calcolo i dati diventano insight utili ai processi decisionali, al business, al marketing (SD-01 @ 00:52:00).

### Data science: tre competenze

*SD-01 @ 00:53:11*

La slide riporta un diagramma di Venn a tre insiemi (fonte: S. Palmer, *Data Science for the C-Suite*, 2015): **conoscenza del dominio** (giallo), **matematica** (blu), **informatica** (verde). Le intersezioni a due a due e il centro:

| Intersezione | Risultato | Cosa manca, secondo la lezione |
|---|---|---|
| Dominio + matematica | *Statistical research* | l'informatica: senza saper programmare non si applica la statistica su larga scala. Era la situazione pre-web: statistici che analizzavano questionari cartacei con la calcolatrice, per esempio sui clienti di un supermercato (i giovani comprano pizza surgelata, i meno giovani integratori, da cui coupon personalizzati) |
| Dominio + informatica | *Data processing* | la parte statistica e di machine learning |
| Matematica + informatica | *Machine learning* | l'esperto di dominio che interpreta i risultati |
| Tutte e tre | **Data science** | nulla |

L'esempio personale di Mele (SD-01 @ 00:56:04): lei conosce matematica e informatica e ha sempre analizzato testo e grafi dei social. Se le chiedessero di predire la predisposizione a tumori da sequenze di DNA "non saprebbe da dove iniziare" senza un esperto di bioinformatica che la guidi.

Chi copre tutte e tre le aree è raro: per questo la stampa chiama i data scientist **"unicorni"**, e per questo sono ben pagati.

---

## 8. Data mining contro data analytics

*SD-01 @ 00:57:51*

| | Data mining | Data analytics |
|---|---|---|
| Definizione | *knowledge discovery from data* | può essere esplorativa, descrittiva o predittiva |
| Obiettivo | estrarre e scoprire pattern significativi | estrarre modelli e spiegazioni, proporre ipotesi |
| Ruolo | il *data miner* fornisce evidenza a supporto di un'ipotesi data | il *data analyst* / *data scientist* scopre "the how and the why" |
| Organizzazione, secondo alcuni autori | un singolo specialista con uno strumento raccoglie, analizza e riporta al cliente | un team di specialisti valuta i dati, trova pattern, trae conclusioni |

Gli esempi della lezione, entrambi su un log di e-commerce:

- **Data miner**, compito ben definito: "scoprimi se le casalinghe di mezza età preferiscono questo prodotto di skin care o quest'altro". Prende i dati, li pre-processa, fa un'analisi statistica e risponde sì o no (SD-01 @ 00:58:37).
- **Data analyst**, compito aperto: "cosa scopri da questo log?". Pulisce i dati, fa clustering e trova, per esempio, che lo sport si compra fra i 20 e i 40 anni, la tecnologia e le poltrone fra i 50 e i 70, gli sport acquatici al Sud e lo sci al Nord. Poi presenta i dati aggregati con una visualizzazione e ne spiega il perché: i giovani del Nord hanno modo di sciare (SD-01 @ 00:59:50).

Mele usa comunque i termini in modo intercambiabile: nella ricerca si è affermato prima "data mining", poi sostituito da "data analytics", e secondo lei "bisogna porsi delle domande anche se si fa data mining". In entrambi i casi si tratta di un **progetto guidato dai dati** (SD-01 @ 01:01:07).

---

## 9. Progetti data-driven: pattern, task e step

*SD-01 @ 01:02:21*

### Obiettivo e qualità dei pattern

L'obiettivo è "getting insights and draw conclusions from raw data", cioè **trovare pattern**: comportamenti che si ripetono per uno stesso utente o per gruppi di utenti. La domanda chiave è "che cosa ci dice il pattern?", perché **l'interpretazione** è decisiva. Il rischio è scoprire pattern privi di significato.

Un pattern deve essere:

| Proprietà | Significato | Esempio della lezione |
|---|---|---|
| **Valid** | regge su dati nuovi con una certa sicurezza | |
| **Useful** | si può agire sui risultati | raccomandazione: a chi compra un latte detergente per pelli grasse e miste si consiglia una crema per lo stesso tipo di pelle; a chi compra una tenda, materassini e un fornelletto a bombola |
| **Unexpected** | non ovvio | "chi compra lo snowboard d'inverno compra il costume d'estate" è ovvio, ma si può sfruttare a stagione giusta: tavola da surf e costume a chi ha comprato lo snowboard |
| **Understandable** | interpretabile da un umano | il lavoro del data analyst è visualizzare e **raccontare una storia** dietro i dati a chi ha commissionato l'analisi |

La slide cita: "Data is like garbage. You'd better know what you are going to do with it before you collect it.", attribuita a Mark Twain. Mele la collega alla raccolta differenziata: se separo vetro, plastica e carta posso riciclare e perfino guadagnare, se mescolo tutto inquino e non ricavo nulla. Allo stesso modo, il data scientist spesso riceve dati grezzi senza poterli scegliere, e il **pre-processing** è la "prima scrematura" che rende possibile trovare pattern (SD-01 @ 01:05:10).

> **Nota aggiunta:** l'attribuzione a Mark Twain, morto nel 1910, è diffusa online ma non risulta documentata in nessuna sua opera; va presa come citazione apocrifa. Non l'ho verificata su una fonte primaria.

### Due tipi di task

*SD-01 @ 01:07:20*

La slide mostra la sequenza *Data → Sorted → Arranged → Presented visually → Explained with a story* (mattoncini prima ammucchiati, poi ordinati per colore, poi in un istogramma, infine costruiti in una casa).

| Task | Obiettivo | Esempio |
|---|---|---|
| **Descrittivo** | trovare pattern interpretabili che descrivono i dati | **clustering**: sulle transazioni di un e-commerce emergono fasce d'età e aree geografiche con acquisti diversi |
| **Predittivo** | usare alcune variabili per predire valori sconosciuti o futuri di altre | **sistemi di raccomandazione**: a chi compra un giallo di un autore si consigliano altri libri dello stesso autore o altri gialli. Più il data scientist è bravo, più la raccomandazione è inattesa |

### Gli step

*SD-01 @ 01:08:25*

Mele la definisce "una slide molto importante": i tutorial del corso seguiranno questi passi.

1. **Raccolta dei dati**
   - dataset o dump già disponibili online (es. **Kaggle**, con dataset di ogni ambito, dal medico al social);
   - **API** per scaricare i dati, se il dataset non esiste o se servono dati recenti;
   - **web scraper**, cioè codice che simula i click di un utente per scaricare le pagine, se non ci sono API.
2. **(Pre)processing**
   - estrarre i dati e produrre un file in un formato comodo per il proprio codice;
   - rimuovere rumore e ridondanza: per esempio, il record dell'utente ripetuto per ogni azione;
   - **bilanciare le classi**, se serve. Esempio di sentiment classification: con molti esempi positivi e pochissimi negativi il classificatore "si comporta bene" solo perché predice quasi sempre "positivo" (SD-01 @ 01:10:36).
3. **Analisi**: statistica e matematica, machine learning, deep learning. Il deep learning si sta affermando perché, con molti dati, l'addestramento di una rete neurale dà buoni risultati su vari task predittivi.
4. **Conclusioni**: aggregazione dei risultati, visualizzazione e, se serve, predizione.

> **Nota aggiunta:** l'esempio sul bilanciamento si quantifica facilmente. Con 95 esempi positivi e 5 negativi, un classificatore che risponde sempre "positivo" ha accuracy 95/100 = 0,95 e recall sulla classe negativa pari a 0. Per questo, nel capitolo 06, oltre all'accuracy si guardano precision, recall e F1 per classe.

```python
# Nota aggiunta: verifica numerica dell'esempio, non mostrata a lezione.
y_true = ["pos"] * 95 + ["neg"] * 5
y_pred = ["pos"] * 100                     # classificatore banale
accuracy = sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)
recall_neg = sum(t == p == "neg" for t, p in zip(y_true, y_pred)) / y_true.count("neg")
print(accuracy, recall_neg)                # 0.95 0.0
```

---

## 10. Riepilogo e compiti

*SD-01 @ 01:11:37*

- **Social data analytics** = data analytics applicata ai dati dei social media. È richiesta per migliorare i servizi e per aumentare l'engagement, quindi l'esposizione alla pubblicità mirata. La sfida principale è la scala.
- **Social media**: piattaforme che esistono grazie agli utenti. Tre ingredienti: utenti, contenuto generato dagli utenti, connessioni esplicite o implicite. Due famiglie: social network (Facebook, Instagram) e content sharing (YouTube, Wikipedia).
- **Data analytics**: all'intersezione di dominio, matematica e informatica. Obiettivo: scoprire pattern e, se serve, predire.
- **Progetti data-driven**: task descrittivi (clustering) o predittivi (raccomandazione), stessi step: raccolta, pulizia e processing, analisi, conclusioni e visualizzazione.

**Compiti** (slide *Homework*):

- installare Python 3 (python.org) e Jupyter Notebook (jupyter.org);
- leggere la *beginner guide* di Jupyter Notebook;
- leggere l'**Introduzione** di *Social Media Data Mining and Analytics*.

---

## Glossario

| Termine | Significato nel corso |
|---|---|
| Social Data Analytics | data analytics applicata ai dati dei social media |
| User-generated content | contenuto prodotto dagli utenti, tipicamente testo non strutturato |
| Relazione esplicita | connessione voluta dall'utente: amicizia, following |
| Relazione implicita | connessione nata da interazioni intorno a un contenuto (es. co-editing su Wikipedia) |
| Targeted advertisement | pubblicità mirata grazie alla profilazione |
| Big Data Analytics | analytics su dataset su larga scala, con problemi di scalabilità |
| Commodity hardware | server economici di base, usati in cluster |
| MapReduce | paradigma di calcolo distribuito: map (operazioni parziali), reduce (aggregazione) |
| 5 V | Volume, Variety, Velocity, Value, Veracity |
| Umbrella concept | concetto ombrello che raccoglie più tecniche |
| Predictive analytics | analytics focalizzata sulla predizione |
| Data miner / data analyst | specialista con compito definito / analista con compito esplorativo, spesso in team |
| Task descrittivo / predittivo | trovare pattern interpretabili (clustering) / predire valori futuri (raccomandazione) |
| Kaggle | sito che pubblica dataset di vario tipo |
| Web scraper | codice che simula la navigazione per scaricare pagine |

## Punti incerti

- **SD-01 @ 00:12:04-00:12:30:** i nomi dei docenti degli altri corsi del percorso: "professor Maielli" / "Maieli" e "Enrico" [?]. Da confermare con il calendario del master.
- **SD-01 @ 00:03:57:** "Zabbo" nella trascrizione è Gabor **Szabo**, primo autore del libro (confermato dalla slide SDA26).
- Segmenti a bassa confidenza: uno solo sopra soglia (-0.309, SD-01 @ 00:33:52), senza conseguenze sul contenuto.

## Materiale usato

- Video: `video/SD-01.mp4` (portale, `Mele-Lesson-1_low.mp4`)
- Slide: `Materiale/Portale/estratti/0_General_Info_SDA25.pdf`, `1_Introduction_SDA25.pdf`; `Materiale/Teams/estratti/Slides/0_General_Info_SDA26.pdf`, `1_Introduction_SDA26.pdf`
- Teams 2026: Teams 4 (trascrizione letta in pagina, non salvata)
- Libri: `Materiale/Portale/estratti/books/`
