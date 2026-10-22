# Capitolo 02: Analisi dell'attività degli utenti

**Lezione:** SD-02 (1:05:08), Dott.ssa Ida Mele, IASI-CNR (ida.mele@iasi.cnr.it)
**Slide:** `2_User_Activity_SDA25.pdf` (41 pagine, quelle del video). La versione `2_User_Activity_SDA26.pdf` (42 pagine) aggiunge una pagina sui bot di Wikipedia (sez. 4) e corregge tre refusi.
**Riferimento:** capitolo 1, *Users: The Who of Social Media*, del libro [1] *Social Media Data Mining and Analytics* (Szabo, Polatkan, Boykin, Chalkiopoulos, Wiley 2019), usato qui solo per verificare grafici e numeri.
**Fonti 2026:** nessuna integrazione dalle registrazioni Teams. Nessun notebook per questa lezione.

## Indice

1. [Perché monitorare gli utenti](#1-perché-monitorare-gli-utenti)
2. [Azioni e finestre temporali](#2-azioni-e-finestre-temporali)
3. [I due casi di studio: Wikipedia e X](#3-i-due-casi-di-studio-wikipedia-e-x)
4. [Wikipedia: istogramma, media e mediana](#4-wikipedia-istogramma-media-e-mediana)
5. [Il grafico log-log e il fanning out](#5-il-grafico-log-log-e-il-fanning-out)
6. [La legge di potenza](#6-la-legge-di-potenza)
7. [Ranking degli utenti, bot e regola 80/20](#7-ranking-degli-utenti-bot-e-regola-8020)
8. [PDF e confronto fra periodi: i coefficienti C21 e C31](#8-pdf-e-confronto-fra-periodi-i-coefficienti-c21-e-c31)
9. [Burst activity e il modello r2 = R12 · r1](#9-burst-activity-e-il-modello-r2--r12--r1)
10. [Gli utenti meno attivi: la CDF](#10-gli-utenti-meno-attivi-la-cdf)
11. [Gli utenti più attivi: la CCDF](#11-gli-utenti-più-attivi-la-ccdf)
12. [User activity su X](#12-user-activity-su-x)
13. [Riepilogo e compiti](#13-riepilogo-e-compiti)

---

## 1. Perché monitorare gli utenti

*SD-02 @ 00:01:52*

Gli utenti sono l'ingrediente principale di una piattaforma sociale (capitolo 01): pubblicano contenuti, comunicano con i commenti e tengono il servizio "vivo e in crescita". Senza di loro Facebook o Instagram sarebbero contenitori vuoti. Il data analyst studia il loro comportamento per migliorare il servizio e aumentare la **user engagement**: un utente soddisfatto torna volentieri, uno insoddisfatto rischia di cancellare l'account.

Le domande tipiche, raggruppate come nella slide *Social Media Users*:

| Area | Domande |
|---|---|
| **User engagement** | quanti utenti ci sono e quanto sono attivi? Perché si iscrivono, perché se ne vanno? Il servizio piace? Se no, perché, e come migliorarlo? |
| **Comportamento tipico** | qual è l'attività complessiva di chi usa il servizio? Ci sono somiglianze fra utenti diversi, o per lo stesso utente su piattaforme diverse? |
| **Analisi temporale e predizione** | come evolve l'uso nel tempo? Si può predire? |
| **Networking degli utenti** | che aspetto hanno le reti degli utenti? Gli utenti più coinvolti formano reti di tipo diverso? |

Esempi a voce:

- **Abbandono** (SD-02 @ 00:03:23): YouTube raccomanda video estranei ai nostri interessi, dopo il primo video lasciamo la piattaforma e passiamo a un'altra. Capire cosa è successo quando un utente se ne va permette di correggere il servizio.
- **Comportamento fra piattaforme** (SD-02 @ 00:04:28): lo possono studiare soprattutto le big company con molti servizi, come Meta, proprietaria sia di Facebook sia di WhatsApp.
- **Analisi temporale** (SD-02 @ 00:05:01): esiste, ma nel corso non si tratta la *time series analysis* (il capitolo 3 del libro è saltato, vedi capitolo 01).
- **Networking** (SD-02 @ 00:05:38): su X e Instagram celebrity e influencer, molto attivi, tendono a seguirsi a vicenda, come le persone che lavorano in televisione. Formano una **clique**, una rete molto interconnessa. Le reti si vedono nel capitolo 03.

---

## 2. Azioni e finestre temporali

*SD-02 @ 00:05:57*

Prima di misurare l'attività bisogna fissare due cose.

**1. L'azione da analizzare.** Scrivere un post su Facebook, lasciare un commento sotto una foto di Instagram, condividere una foto, creare o rimuovere un link. Esempio a voce: quando chiedo l'amicizia e viene accettata creo un link, quando tolgo l'amicizia lo rimuovo. L'ipotesi di partenza è che **alcuni utenti siano più attivi di altri**.

**2. Il campionamento della finestra temporale** (SD-02 @ 00:06:36). Un dataset reale non è infinito: se ho dieci anni di dati e ne voglio analizzare una parte, come la scelgo? La slide mostra due scenari su un asse del tempo:

```
(a)  ──█────██───█──███────────▶   finestre casuali, non consecutive
(b)  ────███████████──────────▶    un intervallo continuo e chiuso   (preferito)
                              time
```

Con lo scenario (a) la "fotografia" può non essere veritiera: un utente molto attivo nelle finestre prese può essere poco attivo negli spazi vuoti, o viceversa. Meglio (b): periodi consecutivi o almeno vicini. Una piccola interruzione è tollerabile: se monitoro lo stream di X e perdo la connessione per un paio d'ore, l'importante è recuperare. Se invece perdo un paio di giorni, un'analisi sulle notizie risulta falsata, perché in due giorni escono moltissime notizie (SD-02 @ 00:07:46).

Nella finestra scelta (una settimana, un mese, un anno, secondo l'analisi) si misura la **frequenza d'uso**: quante volte l'utente è stato attivo nell'intervallo, per esempio quanti post ha scritto su Facebook.

> **Nota aggiunta:** il libro [1] dà anche il motivo per preferire intervalli brevi e continui: il comportamento degli utenti può cambiare nel tempo (i nuovi iscritti possono avere caratteristiche diverse dai vecchi), quindi conviene campionare in un intervallo il più breve possibile.

### Più osservo, più vedo

*SD-02 @ 00:08:53*

Seconda osservazione, "abbastanza banale ma importante": più dati osservo, più utenti catturo, e più attivi mi appaiono. L'esempio di Mele è una stazione di una città di provincia (non Roma Termini): in un minuto vedo al massimo uno o due treni, in un'ora molti di più, in un giorno centinaia. Allo stesso modo, una finestra più lunga cattura anche gli utenti mediamente attivi, e quelli molto attivi risultano ancora più attivi. Questa osservazione torna nella sezione 8, dove si scopre che la crescita **non è proporzionale** alla lunghezza della finestra.

---

## 3. I due casi di studio: Wikipedia e X

*SD-02 @ 00:09:46*

Gli esempi sono quelli del capitolo 1 del libro [1].

**Wikipedia** è un'enciclopedia online e di solito non la si associa ai social media, perché manca la connessione esplicita fra utenti: su Facebook chiedo l'amicizia e si crea un arco fra il mio nodo e quello dell'amico, su X seguo qualcuno per mia volontà. Su Wikipedia no. Però è un contenitore che resterebbe vuoto senza i volontari che, con il software *wiki*, creano e modificano gli articoli e li aggiornano in base agli eventi: è una **piattaforma di content sharing** che vive grazie agli utenti, quindi una piattaforma sociale. Le connessioni nascono implicitamente: se modifico un articolo già modificato da un altro utente, fra noi si crea un legame, se non altro di interessi simili (SD-02 @ 00:11:37).

| | Wikipedia | X (ex Twitter) |
|---|---|---|
| Tipo | enciclopedia, content sharing | microblogging |
| Dati | dump XML della Wikipedia inglese, da pre-processare | API per scaricare i dati |
| Domanda | quante volte un utente modifica un articolo in ogni periodo? | quante volte un utente pubblica o ripubblica (*retweet*) in un periodo? |

Su X Mele precisa (SD-02 @ 00:13:57) che userà spesso "Twitter" e "tweet" invece di "X" e "post", perché i dati del libro sono di qualche anno fa, quando la piattaforma si chiamava ancora Twitter.

> **Nota aggiunta (verificata il 22/10/2026):** l'acquisizione di Twitter da parte di Elon Musk si è chiusa a fine ottobre 2022; il rebranding in X è del luglio 2023 ([Wikipedia, *Twitter under Elon Musk*](https://en.wikipedia.org/wiki/Twitter_under_Elon_Musk); [Daily Illini, 24/07/2023](https://dailyillini.com/news-stories/2023/07/24/twitter-rebrands-as-x/)).

---

## 4. Wikipedia: istogramma, media e mediana

*SD-02 @ 00:14:27*

Il compito è **aggregare gli utenti in base alla frequenza delle loro modifiche**. I quattro step del capitolo 01 diventano:

1. **Raccolta dati**: il dump della Wikipedia inglese, un grande file XML.
2. **Pre-processing**: si estraggono i campi necessari in un file più piccolo e pulito in formato **TSV** (*tab-separated values*):
   - nome della pagina modificata;
   - *namespace* della pagina, cioè il "tipo" di pagina, quello che compare nel link (`https://en.wikipedia.org/wiki/Wikipedia:Namespace`);
   - ID della pagina;
   - ID della revisione;
   - **timestamp** della revisione: data (anno, mese, giorno) e ora (ore, minuti, secondi) esatte, "time" più "stamp", il timbro;
   - ID dell'utente che ha modificato;
   - nome dell'account;
   - indirizzo IP (solo per gli editor anonimi).
3. **Analisi**: contare quante volte ogni utente ha modificato una pagina.
4. **Visualizzazione**: un istogramma, "la parte più importante, quella decisiva" (SD-02 @ 00:15:38).

> **Nota aggiunta:** il libro [1] spiega come si fa il pre-processing di un XML così grande (circa 54 GB compressi a inizio 2018): con un parser **SAX**, che legge il file a eventi in un solo passaggio, e non con un parser **DOM**, che caricherebbe l'intero albero in memoria. Il conteggio per periodo è poi un semplice ciclo sul TSV che incrementa `user_frequencies[user_id][range_id]` se il timestamp cade nell'intervallo (Listing 1.1 del libro, in Python 2). Il libro considera solo gli utenti registrati, escludendo l'ID vuoto e l'ID 0.

### L'istogramma di gennaio 2013

*SD-02 @ 00:15:38*

**Grafico (slide 8):** istogramma a barre nere. Asse x: *Number of revisions made*, da 1 a 20. Asse y: *Number of users in period*, fino a circa 50.000. La prima barra (1 revisione) supera di poco 50.000 utenti, la seconda è circa 22.000, la terza circa 12.000, poi le barre scendono fino a quasi zero verso 20. Una freccia rossa sottolinea la discesa.

- L'asse x è **troncato a 20** per leggibilità. Alcuni utenti fanno molte più modifiche, ma non sono umani: sono **bot**, agenti automatici per la manutenzione di Wikipedia (*bookkeeping*, sistemare link che non puntano a nulla). "Già 20 in un mese verosimilmente si tratta di un bot" (SD-02 @ 00:16:54).
- Il numero di utenti **decresce molto rapidamente** al crescere delle revisioni, ma in modo regolare: è una *smooth function*.
- **Media circa 30, mediana 2.** Nella mediana i valori si ordinano (tutti gli utenti con 1 modifica, poi con 2, e così via, fino ai bot) e si prende quello centrale: ha fatto solo 2 modifiche, quindi a sinistra ci sono tantissimi utenti con una o due modifiche e a destra pochissimi. Gli **outlier** con moltissime modifiche spostano la media ma quasi non toccano la mediana.

Regola pratica (SD-02 @ 00:18:38): quando media e mediana differiscono molto, l'istogramma avrà con ogni probabilità questa decrescita rapida e si parla di distribuzione **highly skewed** o **long tail**, a coda lunga.

> **Correzione:** a voce (SD-02 @ 00:16:14) e nella slide 8 ("Few users made ~1K edits in 1 month") i bot fanno "circa 1000" modifiche al mese. La tabella della slide 14, presa dal libro, dà per gennaio 2013 80.003 modifiche a ClueBot NG, 79.357 a EmausBot e 63.136 ad Addbot, e il libro parla di "tens of thousands of edits in just 1 month". Circa 1000 è l'ordine di grandezza in cui, nel grafico log-log, restano pochi utenti per valore (sez. 5); i bot più attivi ne fanno decine di migliaia.

> **Slide SDA26, non mostrata nel video:** la versione 2026 aggiunge una pagina *Wikipedia "bots"*. I bot sono script o programmi per compiti ripetitivi e ad alto volume, che usano la MediaWiki API.
> - **Editing bots**, che modificano le pagine: anti-vandalismo (individuano e annullano svuotamenti, spam, modifiche malevole: *ClueBot NG*); manutenzione (citazioni mancanti, link rotti, formattazione dei template: *Citation bot*, *InternetArchiveBot*); amministrazione e tagging (tag delle pagine di discussione per i WikiProject, archiviazione di vecchie discussioni, blocco di IP sospetti).
> - **Non-editing bots**, che analizzano senza modificare: *data miner* che estraggono informazioni strutturate e statistiche; identificatori di violazioni di copyright e vandalismo sottile, con euristiche e confronti con fonti esterne.
> - Il codice gira fuori da Wikipedia, su Wikimedia Cloud Services (es. Toolforge), con account interni e approvati.
> - Il *Bot Approvals Group* (BAG) nega di solito i bot di spam, di invio massivo di newsletter, inviti o avvisi su centinaia di pagine di discussione, e di riscrittura automatica degli articoli con l'AI generativa (LLM).

---

## 5. Il grafico log-log e il fanning out

*SD-02 @ 00:19:23*

Si applica la scala logaritmica a **entrambi** gli assi: è il **log-log plot**, il modo compatto di rappresentare le distribuzioni a coda lunga. Permette di mettere nello stesso grafico tre finestre: gennaio, gennaio-febbraio, gennaio-marzo 2013.

**Grafico (slide 9):** asse x *Number of revisions made* da 10⁰ a 10⁴, asse y *Number of users in period* da 10⁰ a oltre 10⁵. Legenda *Period*: cerchio = Jan, quadrato = Jan-Feb, rombo = Jan-Mar. Le tre serie scendono quasi in linea retta (freccia rossa) e, oltre circa 10², si allargano in una nuvola di punti densa che arriva fino a 10⁴ sul fondo dell'asse y. Mele ammette che "c'è poca differenza tra questi simboli": sono le immagini del libro. La curva più in alto è quella dei tre mesi.

Che cosa si legge:

- **Differenze a sinistra, quasi nulle a destra.** Con un mese si osservano meno utenti con 1 revisione che con due o tre mesi: è l'esempio del treno. Sulla destra, dove stanno gli utenti più attivi, le tre curve quasi coincidono (SD-02 @ 00:20:11).
- **Tutti i dati.** A differenza dell'istogramma, non serve troncare: si vedono sia gli utenti con 1, 2, 10 revisioni, sia i bot con migliaia.
- **"Stepping decades".** In base 10, un passo a destra o in alto moltiplica il valore per 10.
- **Rette quasi parallele.** Le tre funzioni seguono, in modo approssimato, rette in scala log-log.
- **Fanning out** ("effetto a ventaglio"): all'estremo destro i valori di y si allargano. Secondo la slide, è la zona degli utenti più attivi, per esempio i bot.

**Istogramma contro log-log** (slide 10, SD-02 @ 00:21:51): l'istogramma mostra un solo mese e un intervallo limitato (fino a 20); il log-log confronta tre finestre di lunghezza diversa con tutti gli utenti. Conclusione della slide: la distribuzione è a coda lunga e il **numero di utenti U con r revisioni segue una power law**.

> **Nota aggiunta:** il libro [1] dà due spiegazioni che la lezione non riporta.
> - **Perché le rette sono "parallele".** Una differenza costante sull'asse logaritmico, ln y₁ − ln y₂ = c, equivale a un rapporto costante y₁/y₂ = eᶜ. Le tre curve sono quindi la stessa funzione moltiplicata per costanti diverse: è l'idea dei coefficienti C21 e C31 della sezione 8.
> - **Perché c'è il fanning out.** È un effetto statistico: verso 1000 revisioni ci sono meno di 10 utenti per valore di r, e con campioni così piccoli il conteggio oscilla molto intorno al valore atteso. Il rimedio proposto è il **binning logaritmico** (sez. 12). Il ventaglio sta dove stanno i bot perché lì ci sono pochi utenti, non perché i bot si comportino in modo particolare.

---

## 6. La legge di potenza

*SD-02 @ 00:22:45*

**Definizione (slide 12):** "una relazione funzionale fra due quantità, in cui una variazione relativa di una quantità produce una variazione relativa proporzionale dell'altra, indipendentemente dalla loro dimensione iniziale: una quantità varia come una potenza dell'altra".

Per Wikipedia, il numero di utenti U che hanno fatto r revisioni segue, "in larga misura", la legge

$$U(r) = K\, r^{\gamma}$$

con γ costante (l'esponente) e K fattore di scala. Mele aggiunge che "ci sono dei software che permettono di identificare il valore di γ" (SD-02 @ 00:23:20).

Applicando il logaritmo naturale a entrambi i membri:

$$\ln U(r) = \ln\left(K r^{\gamma}\right) \;\Rightarrow\; \ln U(r) = \gamma \ln r + \ln K$$

Poiché K e γ sono costanti, **ln U(r) è una funzione lineare di ln r**: in scala log-log la power law è una retta con pendenza γ e intercetta ln K. Per una distribuzione che decresce, γ è negativo.

> **Correzione:** a voce (SD-02 @ 00:24:26) Mele dice che c'è "una relazione lineare tra il numero di utenti che fanno le modifiche e il numero di modifiche". La relazione lineare è fra i **logaritmi**, ln U(r) e ln r, come nella slide. Fra U e r la relazione è di potenza.

> **Nota aggiunta:** la frase "variazione relativa proporzionale indipendente dalla dimensione iniziale" si traduce così: U(c·r) = K cᵞ rᵞ = cᵞ · U(r). Moltiplicare r per c moltiplica U per cᵞ, qualunque sia r. È la *scale invariance* della power law, la stessa proprietà che il libro usa per dimostrare che la distribuzione delle revisioni deve essere una power law (vedi la nota della sezione 9).

### Esempio: stimare γ con un fit in log-log

> **Nota aggiunta, non mostrata a lezione:** la lezione dice a parole che γ si ricava con un software. Il modo più diretto, coerente con la relazione lineare appena vista, è una regressione lineare di ln U(r) su ln r. L'esempio usa dati sintetici generati con esponente noto (1,87, il valore che il libro ricava per Wikipedia, vedi nota successiva) e lo stesso numero di utenti attivi di gennaio 2013. Il codice è estratto da `verifica_sd02.py`, eseguito con Python 3 e NumPy 2.5.

```python
# Nota aggiunta: fit di una power law in log-log su dati sintetici, non mostrato a lezione.
import numpy as np

rng = np.random.default_rng(42)
N, alpha = 134_804, 1.87            # stessi ordini di grandezza di Wikipedia, gennaio 2013
edits = rng.zipf(alpha, size=N)     # P(r) proporzionale a r^-alpha, r = 1, 2, ...
print(f"media = {edits.mean():.1f}, mediana = {np.median(edits):.0f}, max = {edits.max()}")
r, U = np.unique(edits, return_counts=True)   # U(r): numero di utenti con r edit

# 1) regressione lineare di ln U(r) su ln r, solo sulla "testa" (r <= 50)
testa = r <= 50
g_testa, lnK = np.polyfit(np.log(r[testa]), np.log(U[testa]), 1)
print(f"OLS su r<=50:        gamma = {g_testa:.3f}, K = {np.exp(lnK):.0f}")

# 2) stessa regressione su tutti i punti: la coda rumorosa ("fanning out") distorce la stima
g_tutto, _ = np.polyfit(np.log(r), np.log(U), 1)
print(f"OLS su tutti i punti: gamma = {g_tutto:.3f}  (distorta dalla coda)")

# 3) binning logaritmico: bucket di ampiezza crescente, conteggio diviso per l'ampiezza
bordi = np.unique(np.floor(np.logspace(0, np.log10(edits.max() + 1), 30)).astype(int))
cont, _ = np.histogram(edits, bins=bordi)
largh = np.diff(bordi)
centro = np.sqrt(bordi[:-1] * (bordi[1:] - 1).clip(min=bordi[:-1]))
ok = cont > 0
g_bin, _ = np.polyfit(np.log(centro[ok]), np.log(cont[ok] / largh[ok]), 1)
print(f"OLS con binning log: gamma = {g_bin:.3f}")
```

Output:

```
media = 22.8, mediana = 1, max = 293388
OLS su r<=50:        gamma = -1.874, K = 76342
OLS su tutti i punti: gamma = -0.781  (distorta dalla coda)
OLS con binning log: gamma = -1.849
```

Tre cose da notare:

- Anche i dati sintetici mostrano lo scarto media/mediana della sezione 4 (22,8 contro 1): basta una power law con γ ≈ −1,87.
- La regressione su **tutti** i punti sbaglia di molto (−0,78): nella coda ogni valore di r ha 1 o 2 utenti, ln U vale 0 o ln 2 per centinaia di punti, e la retta si appiattisce. È il fanning out della sezione 5 tradotto in numeri.
- Restringendo il fit alla testa, o aggregando la coda con bucket logaritmici, si torna vicino a −1,87.

La regressione in log-log è didattica. Per stime serie si usa la massima verosimiglianza con scelta del valore minimo da cui vale la legge (Clauset, Shalizi, Newman, *Power-law distributions in empirical data*, SIAM Review 2009; in Python il pacchetto `powerlaw`). Riferimento non verificato in questa sessione.

> **Nota aggiunta:** il libro [1] non stima γ con un fit, lo **deduce** da due osservazioni sperimentali (sezioni 8 e 9): la PDF non dipende dalla finestra, e chi fa r₁ modifiche nel periodo 1 ne fa in media R21·r₁ nel periodo 2. Ne segue γ = −(1 + ln(U₂/U₁) / ln R21). Con U₁ = 134.804 utenti attivi a gennaio, U₂ = 219.604 a gennaio-febbraio e R21 = 1,75 (pendenza del fit della sezione 9), il libro ottiene γ ≈ −1,87. Verifica:

```python
# Nota aggiunta: esponente gamma dai numeri del libro [1], p. 20.
import numpy as np
U1, U2, R21 = 134_804, 219_604, 1.75
print(f"C21 = U2/U1 = {U2 / U1:.3f}")
print(f"gamma = {-(1 + np.log(U2 / U1) / np.log(R21)):.3f}")
# C21 = U2/U1 = 1.629
# gamma = -1.872
```

---

## 7. Ranking degli utenti, bot e regola 80/20

*SD-02 @ 00:24:26*

### Ranking

Si ordinano gli utenti per numero di attività in modo che i **più attivi stiano all'inizio** del vettore e i meno attivi alla fine. In pratica (SD-02 @ 00:25:03): un file con ID utente e numero di modifiche, ordinato sulla seconda colonna in modo decrescente. La posizione nel vettore è il **rank** dell'utente. Le domande: che percentuale delle azioni viene dagli utenti più attivi? E dai meno attivi?

**Grafico (slide 13):** asse x *Most active user rank* in scala log, da 10⁰ a oltre 10⁵; asse y *Fraction of all edits up to this rank*, da 0 a 1. La curva parte poco sopra 0 al rank 1, sale lentamente fino a circa 0,25 intorno a 10², poi rapidamente fino a circa 0,85 verso 10⁴, e arriva a 1 a poco più di 10⁵.

Lettura della slide: gli utenti più attivi sono pochi, "vicini all'1%", e stanno a sinistra (rank alto, cioè posizioni iniziali); gli inattivi sono "quasi il 100%" e stanno a destra. Mele collega questo alla mediana di 2 (SD-02 @ 00:26:07).

> **Nota aggiunta:** la curva è una **somma cumulativa**: il valore in corrispondenza del rank k è la frazione di tutte le modifiche fatte dai k utenti più attivi. La slide dice "increasing activities", ma l'ordinamento è decrescente (prima il più attivo); a voce Mele parla una volta di "posizione 1" e una volta di "posizione 0, rank 0": nel libro il primo utente ha rank 1. Dalla curva, secondo il libro: i primi 10 utenti fanno circa il 12% delle modifiche, i primi 100 circa il 29%, cioè lo 0,07% dei 134,8 mila utenti attivi fa quasi un terzo delle modifiche.

### I bot di Wikipedia

*SD-02 @ 00:26:07*

Nella slide 14 la stessa curva ha un cerchio blu sul rank 1, accanto a una tabella:

| Account | Modifiche nel periodo 1 (gennaio 2013) | Secondi medi fra due modifiche |
|---|---|---|
| ClueBot NG | 80.003 | 33 |
| EmausBot | 79.357 | 34 |
| Addbot | 63.136 | 42 |

I primi tre del ranking sono bot: moltissime modifiche e "molto ravvicinate tra di loro". **10 utenti sono responsabili di circa il 12% di tutte le modifiche**, verosimilmente bot (SD-02 @ 00:26:39).

> **Nota aggiunta:** la terza colonna si ricava dalla seconda: gennaio ha 31 × 86.400 = 2.678.400 secondi; 2.678.400 / 80.003 = 33,5 s, / 79.357 = 33,8 s, / 63.136 = 42,4 s (eseguito in `verifica_sd02.py`). Il libro aggiunge che, togliendo i bot noti, i primi 10 utenti scendono al 6% delle modifiche e i primi 100 al 18%: meno, ma comunque una quota enorme per così pochi utenti.

### Principio di Pareto (regola 80/20)

*SD-02 @ 00:27:18*

L'economista italiano **Vilfredo Pareto** osservò nel 1906 che l'**80% delle terre** apparteneva al **20% della popolazione**. Generalizzando: in molti fenomeni una piccola frazione dei partecipanti (20%) è responsabile della maggior parte delle azioni (80%).

| | Studio di Pareto | Social media |
|---|---|---|
| Partecipanti | proprietari terrieri | utenti |
| Azioni | possedere terra | pubblicare, seguire, modificare |

**Grafico (slide 15, fonte Wikipedia, User:Husky, pubblico dominio):** una curva che scende ripidissima e poi si appiattisce verso destra. L'area a sinistra, in verde, è il 20% circa che domina; l'area a destra, in giallo, è la **lunga coda**.

Sui social (SD-02 @ 00:28:52): influencer e celebrity postano molto per tenere aggiornati i fan e, pur essendo pochi, contribuiscono molto; su Wikipedia lo stesso ruolo lo hanno i bot. In generale c'è un **forte sbilanciamento**: pochi utenti molto attivi, moltissimi poco attivi (chi modifica una pagina una o due volte, chi ha pochi follower).

> **Nota aggiunta:** il libro [1] precisa che 80 e 20 non devono sommare a 100, perché si riferiscono a entità diverse (conseguenze e cause); la forma generale è la "regola p/q", con p vicino a 1 e q vicino a 0.

### Code lunghe ovunque

*SD-02 @ 00:29:29*

Si osservano distribuzioni a coda lunga nella vita reale (reddito, ricchezza, popolarità) e sui social (prodotti, canzoni e film popolari, tag nel bookmarking, influencer, follower su X).

**Grafico "Example of Popular Songs" (slide 16, fonte: Anderson 2006, p. 25):** download (asse y, fino a 180.000 con l'asse spezzato) contro titoli ordinati per popolarità (asse x, anch'esso spezzato: 25.000, 50.000, 100.000, poi 900.000). Una linea verticale a 25.000 separa la zona verde, "Songs available at Wal-Mart and Rhapsody", dalla zona gialla, "Songs available only at Rhapsody", etichettata *Long tail*. A voce (SD-02 @ 00:30:06): poche canzoni, circa 25.000, hanno moltissimi download, fino a un picco di 180.000; la grande maggioranza ne ha pochi.

**Grafico "Example of Influencer" (slide 16, fonte crowdmedia.com):** *The Long Tail Model*, popolarità/prezzo contro influencer. A sinistra la testa (*HEAD*, verde: *Celebrities, Macro-influencers*), poi in arancione i *Mid-tier influencers*, poi la *LONG TAIL* gialla dei *Micro-influencers*. Gli esempi a voce:

| Livello | Chi è | Esempio della lezione |
|---|---|---|
| Celebrity, macro-influencer | influencer di professione, con entrate importanti; pochi, molto popolari | Lady Gaga, Rihanna, Ferragni |
| Mid-tier | popolari in un ambito specifico | un professore di Stanford che tiene corsi, molto seguito in informatica |
| Micro-influencer | utenti ordinari, seguiti da amici e conoscenti | |

---

## 8. PDF e confronto fra periodi: i coefficienti C21 e C31

*SD-02 @ 00:31:13*

Domanda: **la distribuzione cambia se considero periodi più lunghi?**

### Probability Density Function

Si **normalizza l'istogramma**: si divide il numero di utenti che hanno fatto n modifiche per il numero totale di utenti attivi nella finestra. Si ottiene la **Probability Density Function (PDF)**, "da non confondere con l'estensione del file" (SD-02 @ 00:31:43):

$$P(\text{edits} = n) = \frac{U(\text{edits} = n)}{\sum_{i=1}^{\infty} U(\text{edits} = i)}$$

- U(edits = n): numero di utenti che hanno fatto esattamente n modifiche;
- il denominatore è il totale degli utenti attivi nel periodo;
- P è la *likelihood*, la verosimiglianza che un utente preso a caso abbia fatto n modifiche nel periodo.

> **Correzione:** a voce (SD-02 @ 00:32:14) la somma al denominatore va "per i da 1 a 1000". Nella slide e nel libro va da 1 a **∞**: conta tutti gli utenti attivi, compresi i bot con decine di migliaia di modifiche (sez. 4). In pratica la somma si ferma al massimo osservato.

> **Nota aggiunta:** il libro [1] osserva che, essendo r discreto, il nome corretto sarebbe *probability mass function*; il corso, come il libro, usa PDF. Il grafico della PDF ha la stessa forma dell'istogramma, con l'asse y riscalato di una costante.

### PDF per periodo

*SD-02 @ 00:32:50*

Per ciascuna finestra p (p = 1 gennaio, p = 2 gennaio-febbraio, p = 3 gennaio-marzo):

$$P_p(r) = \frac{U_p(r)}{\sum_{i} U_p(i)}$$

con Uₚ(r) numero di utenti che hanno fatto esattamente r modifiche nel periodo p; il denominatore è il numero di utenti attivi nel periodo p. Pₚ(r) è la probabilità che un utente scelto a caso abbia fatto r modifiche nel periodo p.

**Grafici (slide 19 e 21):**

| Grafico | Assi | Che cosa mostra |
|---|---|---|
| *Normalized functions (from 1 to 3 months)* | x: revisioni da 1 a 20; y: *Number of users in period* fino a oltre 90.000 | tre curve con lo stesso andamento, a quote diverse: il primo punto vale circa 50.000 per Jan, 80.000 per Jan-Feb, 110.000 per Jan-Mar |
| *Normalized functions for each time period* | x: revisioni da 1 a 20; y: *Fraction of users in period* da 0 a circa 0,35 | le tre curve si sovrappongono quasi del tutto, da circa 0,35 a r = 1 fino a quasi 0 |

Nel primo grafico, con più mesi si osservano più dati e la curva è più alta, ma **la forma non cambia** (SD-02 @ 00:33:28). Nel secondo, dividendo ciascuna curva per il numero di utenti attivi nel *suo* periodo, le tre curve diventano praticamente una: "nessuna differenza tranne il primo punto".

> **Nota aggiunta:** il primo dei due grafici, nonostante il titolo "Normalized functions", ha sull'asse y numeri assoluti di utenti (fino a 110.000 circa), non frazioni: è la versione non normalizzata, cioè la Figure 1.3 del libro. La normalizzazione vera è nel secondo grafico (Figure 1.4).

**Conclusione** (SD-02 @ 00:35:20): **la PDF dell'attività degli utenti non dipende dalla finestra temporale.** Mele aggiunge due avvertenze: dipende dal tipo di dati, non vale sempre; e per Wikipedia un mese basta, mentre "un giorno o un paio di giorni probabilmente non sarebbe stato sufficiente".

> **Nota aggiunta:** il libro misura la somiglianza: l'errore quadratico medio relativo dei tre punti rispetto alla loro media sta fra il 6 e l'8% per r da 1 a 10.

### L'ipotesi e i coefficienti C_ij

*SD-02 @ 00:36:29*

Ipotesi: per ogni r le frazioni di utenti sono uguali nei tre periodi.

$$\frac{U_1(r)}{\sum_{i=1}^{\infty} U_1(i)} = \frac{U_2(r)}{\sum_{i=1}^{\infty} U_2(i)} = \frac{U_3(r)}{\sum_{i=1}^{\infty} U_3(i)}$$

Si definiscono i rapporti fra utenti attivi, **C_ij = utenti attivi nel periodo i / utenti attivi nel periodo j**:

$$C_{21} = \frac{\sum_{i=1}^{\infty} U_2(i)}{\sum_{i=1}^{\infty} U_1(i)} \qquad C_{31} = \frac{\sum_{i=1}^{\infty} U_3(i)}{\sum_{i=1}^{\infty} U_1(i)}$$

Dall'ipotesi segue che si può calcolare il numero di utenti con r modifiche in un periodo lungo a partire da quello del periodo 1 (SD-02 @ 00:37:43):

$$U_2(r) = C_{21}\, U_1(r) \qquad U_3(r) = C_{31}\, U_1(r)$$

Seconda ipotesi: **C_p1 non dipende da r**. Per verificarla lo si misura per ogni r:

$$C_{p1}(r) = \frac{U_p(r)}{U_1(r)}, \qquad p = 2, 3$$

> **Nota aggiunta:** nella slide 23 la frase "computing the num. of active users in period i knowing the num. of active users in period i (e.g., 1)" ha un refuso: il secondo indice è j. Il passaggio dall'ipotesi alla formula è immediato: se U₂(r)/ΣU₂ = U₁(r)/ΣU₁, allora U₂(r) = (ΣU₂/ΣU₁)·U₁(r) = C21·U₁(r).

### C21(r) e C31(r) misurati

*SD-02 @ 00:38:45*

**Grafico (slide 24):** asse x *Number of revisions made* da 0 a 50, asse y *Ratio of the number of users* da 1,0 a 3,0. Legenda *Ratio to Period 1*: linea nera *Of Period 2*, linea grigia *Of Period 3*. La nera oscilla intorno a 1,6-1,7, la grigia intorno a 2,2-2,4. Una linea rossa tratteggiata verticale marca uno *Spike* poco oltre r = 40, dove la grigia sale a circa 2,7 e la nera a circa 1,8.

Le due curve sono spostate, perché in una ci sono più dati, ma hanno **comportamento simile**: anche lo spike cade più o meno alla stessa ascissa, "intorno alle 40 revisioni". Conclusione: **C21(r) e C31(r) sono circa costanti, indipendenti dal numero di revisioni**.

### La crescita non è proporzionale

*SD-02 @ 00:39:59*

Allargando la finestra osservo più utenti, e più attivi. Ma in proporzione alla durata? **No.** Stime dal grafico:

| Rapporto | Dagli utenti attivi | Dai giorni | Mesi ideali da 30 giorni |
|---|---|---|---|
| periodo 2 / periodo 1 | C21 = U₂(r)/U₁(r) ≈ **1,6** | (31 + 28) / 31 ≈ **1,9** | 60 / 30 = 2 |
| periodo 3 / periodo 1 | C31 = U₃(r)/U₁(r) ≈ **2,2** | (31 + 28 + 31) / 31 ≈ **2,9** | 90 / 30 = 3 |

Non è sfortuna dovuta a febbraio: anche con mesi ideali da 30 giorni i rapporti sarebbero 2 e 3, lontani da 1,6 e 2,2 (SD-02 @ 00:41:09). Il messaggio (SD-02 @ 00:42:21): l'osservazione banale "periodi più lunghi, più utenti e più azioni" resta vera, ma **non si può assumere una crescita proporzionale**. Se in un giorno osservo 100 utenti, in due giorni non ne osserverò necessariamente 200.

```python
# Verifica dei rapporti (eseguita in verifica_sd02.py)
print(f"{(31 + 28) / 31:.3f}  {(31 + 28 + 31) / 31:.3f}")   # 1.903  2.903
print(f"{60 / 30:.1f}  {90 / 30:.1f}")                      # 2.0  3.0
print(f"{219_604 / 134_804:.3f}")                           # 1.629: C21 dai totali del libro
```

> **Nota aggiunta:** il libro dà C31 ≈ 2,2-2,3 e i totali U₁ = 134.804, U₂ = 219.604, da cui C21 = 1,629. Il motivo intuitivo per cui la crescita è meno che proporzionale: molti utenti attivi a febbraio lo erano già a gennaio, quindi allungare la finestra aggiunge giorni ma solo in parte utenti nuovi.

---

## 9. Burst activity e il modello r2 = R12 · r1

*SD-02 @ 00:42:21*

**Burst activity**: utenti molto attivi in periodi di tempo brevi. Spesso i burst hanno una **stagionalità**, per esempio annuale.

Esempi (SD-02 @ 00:42:58):

- **Query log** dei motori di ricerca. Un query log è un file simile al dump di Wikipedia: per ogni record l'ID anonimo dell'utente, la query, il timestamp, l'eventuale risultato cliccato con la sua posizione nel ranking e il link. Lo studiano i ricercatori delle grandi aziende (Google, Yahoo) per capire il comportamento di ricerca, migliorare il ranking, fare *query recommendation*. Alcune query arrivano a burst: per un **evento esterno improvviso** (terremoto in Giappone → "Japan earthquake") o per un **evento periodico** (la cerimonia degli Oscar → "Oscar ceremony", ogni anno nello stesso periodo).
- **E-commerce**: sciarpe e cappotti si vendono in inverno, costumi e teli mare in estate, ma dipende dall'emisfero: in Australia, nello stesso periodo, si vendono di più gli articoli estivi.

Un picco nelle vendite di un prodotto o nelle query su un argomento è una burst activity.

### Il numero medio di modifiche in un periodo più lungo

*SD-02 @ 00:44:47*

Domanda: **come cambia il numero di modifiche di un utente se cambia la lunghezza della finestra?** Per ogni valore r₁ si prendono tutti gli utenti che nel periodo 1 hanno fatto esattamente r₁ modifiche e si calcola la media delle loro modifiche nel periodo 2:

$$\bar{r}_2(r_1) = \frac{\sum_{i=1}^{N} I(r_{i,1} = r_1)\, r_{i,2}}{\sum_{i=1}^{N} I(r_{i,1} = r_1)}$$

| Simbolo | Significato |
|---|---|
| N | numero totale di utenti |
| r_{i,1}, r_{i,2} | modifiche dell'utente i nel periodo 1 e nel periodo 2 |
| I(·) | **funzione indicatrice**: vale 1 se l'argomento è vero, 0 altrimenti |
| numeratore | somma delle modifiche nel periodo 2 (gennaio-febbraio) degli utenti che a gennaio ne hanno fatte esattamente r₁ |
| denominatore | numero di utenti che a gennaio hanno fatto r₁ modifiche |
| r̄₂(r₁) | numero medio di modifiche nel periodo 2 per quegli utenti |

L'esempio a voce (SD-02 @ 00:47:04): fisso r₁ = 6, considero solo chi a gennaio ne ha fatte 6 e conto quante ne ha fatte in gennaio-febbraio, che possono essere 6 o di più; divido per il numero di quegli utenti.

> **Nota aggiunta:** siccome i periodi 2 e 3 contengono gennaio, r_{i,2} ≥ r_{i,1} sempre: "the edits made in those two periods are never fewer than the edits of Jan" (slide 30). A voce Mele dice "potrebbero averne fatte di meno": vale per il solo febbraio, non per gennaio-febbraio.

**Grafico (slide 30):** asse x *Revisions in Period 1* da 0 a 100, asse y *Average edits in Period 2 & 3* da 0 a 300. Quadrati vuoti (*In Period 2*) e punti neri (*In Period 3*), ciascuno con una retta di fit. La retta del periodo 2 arriva a circa 170 per r₁ = 100, quella del periodo 3 a circa 250; i punti del periodo 3 sono più dispersi.

**Conclusione** (SD-02 @ 00:48:51): le modifiche di un utente in due periodi di lunghezza diversa sono **linearmente proporzionali**. Un buon modello, **in media**, è

$$r_2 = R_{12}\, r_1$$

Chi fa r₁ revisioni nel periodo 1 ne farà in media r₂ nel periodo 2, proporzionale a r₁ con costante R12.

> **Nota aggiunta:** il libro scrive la costante R21 (dal periodo 1 al 2) e ne stima la pendenza in **1,75**, minore del rapporto dei giorni (1,9). Il libro inoltre usa la parola *burst* solo per l'eccezione: assume che ogni utente abbia un tasso di attività suo, circa costante su finestre abbastanza lunghe, e cita i burst come periodi brevi in cui l'utente è più attivo del solito (rimandando al capitolo 4 del libro, non in programma). La formula di r̄₂(r₁) misura la proporzionalità media, non i burst; la slide la presenta sotto il titolo "Burst Activity".

> **Nota aggiunta:** dalle due osservazioni (PDF indipendente dalla finestra, sezione 8; r₂ = R21·r₁, questa sezione) il libro deduce che U₁(r) deve soddisfare un'equazione del tipo A·g(x) = g(B·x), e con il teorema di Euler sulle funzioni omogenee ricava che l'unica soluzione è g(x) = K·xᵞ: la power law della sezione 6 non è solo osservata, è una conseguenza dei due fatti.

Esempio su utenti simulati, per vedere la formula all'opera:

```python
# Nota aggiunta: r2_bar(r1) su utenti simulati (continua dal blocco della sez. 6, stesso rng).
# Ogni utente ha un tasso personale di edit al giorno (distribuzione a coda lunga),
# i conteggi nei periodi sono Poisson. Periodo 2 = gennaio + febbraio (sovrapposto al periodo 1).
M = 300_000
tasso = 0.02 * (rng.pareto(0.9, size=M) + 1)
gen = rng.poisson(tasso * 31)
feb = rng.poisson(tasso * 28)
p1, p2 = gen, gen + feb
print(f"utenti attivi: periodo 1 = {np.count_nonzero(p1)}, periodo 2 = {np.count_nonzero(p2)}, "
      f"rapporto = {np.count_nonzero(p2) / np.count_nonzero(p1):.3f}  (rapporto dei giorni = 1.903)")
# r2_bar(r1) = sum_i I(r_i1 = r1) r_i2 / sum_i I(r_i1 = r1)
r1_vals = np.arange(1, 101)
r2_bar = np.array([p2[p1 == k].mean() for k in r1_vals])
R21_sim = np.polyfit(r1_vals, r2_bar, 1)[0]
print(f"r2_bar(r1) per r1 = 1, 10, 50, 100: {np.round(r2_bar[[0, 9, 49, 99]], 1)}")
print(f"pendenza R21 stimata = {R21_sim:.3f}  (tassi costanti: atteso 59/31 = 1.903; Wikipedia: 1.75)")
```

Output:

```
utenti attivi: periodo 1 = 225015, periodo 2 = 268254, rapporto = 1.192  (rapporto dei giorni = 1.903)
r2_bar(r1) per r1 = 1, 10, 50, 100: [  2.1  18.2  93.5 192.8]
pendenza R21 stimata = 1.903  (tassi costanti: atteso 59/31 = 1.903; Wikipedia: 1.75)
```

`p2[p1 == k].mean()` è esattamente la formula: la maschera booleana `p1 == k` è la funzione indicatrice. Con tassi individuali costanti la pendenza coincide con il rapporto dei giorni; che su Wikipedia sia 1,75 indica che l'attività degli utenti non è costante nel tempo. Il simulatore riproduce anche il fatto della sezione 8: il numero di utenti attivi cresce molto meno della durata (1,19 contro 1,9), perché gran parte degli utenti di febbraio era già attiva a gennaio. Il modello è giocattolo e i suoi parametri sono scelti a mano: non riproduce i numeri di Wikipedia.

---

## 10. Gli utenti meno attivi: la CDF

*SD-02 @ 00:49:28*

La **Cumulative Distribution Function (CDF)** dà la probabilità che la variabile aleatoria (il numero di modifiche) non superi una soglia ρ (*threshold*): la frazione di utenti che hanno fatto **al più ρ** modifiche nel periodo.

$$CDF(\rho) = P(r \le \rho) = \frac{1}{U} \sum_{i=1}^{\rho} U(i)$$

con U numero totale di utenti attivi e U(i) numero di utenti con i modifiche.

**Grafico (slide 33):** asse x *Number of revisions made* in **scala log** da 10⁰ a 10⁴; asse y *Fraction of users w/no more edits*, lineare, da 0,4 a 1,0. La curva parte da 0,4 a 10⁰ (crocetta verde), sale ripida (freccia rossa) fino a circa 0,85 a 10¹ (asterisco blu), arriva quasi a 1 a 10² (crocetta magenta) e resta piatta fino a 10⁴. Il log sull'asse x serve perché i valori vanno da 1 a 10.000: in scala lineare non si vedrebbe la salita iniziale.

Lettura (SD-02 @ 00:50:35):

| Soglia ρ | CDF | Significato |
|---|---|---|
| 1 | ≈ 40% | quasi metà degli utenti di gennaio ha fatto **una sola** modifica |
| 10 | ≈ 85% | la grande maggioranza ne ha fatte al più 10 |
| 100, 1000, 10.000 | ≈ 100% | quasi nessuno supera 100: chi lo fa è un bot |

È lo strumento per i **least active users**.

> **Correzione:** a voce (SD-02 @ 00:51:07) la quota di utenti con al più 100 modifiche è "99,9%". Nel grafico la crocetta magenta a 10² è a circa 0,97, e la slide successiva dice che "meno del 5%" supera 100 revisioni: la CDF a 100 è quindi fra 0,95 e 0,97 circa, non 0,999. "Circa il 100%" della slide è un arrotondamento.

> **Nota aggiunta:** c'è una piccola incongruenza fra due grafici del libro: nella PDF normalizzata (sez. 8) il punto r = 1 vale circa 0,35, mentre la CDF a ρ = 1, che dovrebbe coincidere, vale 0,40. Non incide sulle conclusioni.

---

## 11. Gli utenti più attivi: la CCDF

*SD-02 @ 00:52:20*

Gli utenti più attivi sono di solito i più interessanti: su Wikipedia "abbiamo svelato l'arcano", sono bot, ma su Instagram o X sono gli influencer, che portano le entrate maggiori alla piattaforma. Stanno nella **coda** della distribuzione e si studiano con la **Complementary Cumulative Distribution Function (CCDF)**, detta anche *tail distribution*: la frazione di utenti con **più di ρ** modifiche.

$$CCDF(\rho) = P(r > \rho) = \frac{1}{U} \sum_{i=\rho+1}^{\infty} U(i) = 1 - CDF(\rho)$$

Esempio a voce: con ρ = 100 si contano gli utenti con 101, 102, ... modifiche. CDF e CCDF sono complementari: sommate danno 1.

**Grafici (slide 35):**

| Grafico | Assi | Lettura |
|---|---|---|
| sinistra, x in scala log | x: revisioni da 10⁰ a 10⁴; y: *The edits/user tail distribution* da 0 a 0,6 | parte da circa 0,6 (= 1 − 0,4) e scende; asterisco viola a 10¹ ≈ 0,15; crocetta magenta a 10² ≈ 0,04; poi quasi 0 |
| destra, log-log | x: revisioni da 10⁰ a 10⁴; y da 10⁰ a 10⁻⁴ | quasi una retta fino a una linea tratteggiata rossa a 10^2,5; oltre, la discesa è più ripida (freccia rossa) |

- Circa il **15%** degli utenti ha **più di 10** revisioni in un mese.
- **Meno del 5%** ne ha **più di 100**: sono tantissime per un mese, si tratta dei bot.
- Con il log anche sull'asse y la decrescita appare rapida e diventa **ancora più rapida oltre 10^2,5 ≈ 316** revisioni.

**Risultato teorico (slide 35):** se la PDF dell'attività segue una power law con esponente γ, **anche la coda segue una power law, con esponente γ + 1**. Secondo Mele è un fatto che si osserva spesso nelle reti sociali, e su Wikipedia è "ancora più evidente" perché i bot, con tantissime modifiche, si distinguono molto dagli utenti meno attivi (SD-02 @ 00:55:08). Segue un esempio a voce di cui la trascrizione conserva solo la fine: "[?] ... moltissimi amici e sono nella coda. Mentre la stragrande maggioranza ne hanno un numero medio o comunque in basso" (SD-02 @ 00:55:50-00:56:12).

> **Nota aggiunta:** il perché di γ + 1. Il libro approssima la somma della coda con un integrale: con P(r) = A·rᵞ,
> CCDF(ρ) ≈ ∫_ρ^∞ A zᵞ dz = A/(−(γ+1)) · ρ^(γ+1),
> che converge solo se γ < −1. Con γ ≈ −1,87 la coda ha esponente ≈ −0,87: in log-log la CCDF è **meno ripida** della PDF, perché integrare "alza" l'esponente di 1. Il libro spiega anche il gomito a 10^2,5: è un *finite size effect*, una **cutoff** dovuta al fatto di osservare una finestra finita; con il periodo 3, circa tre volte più lungo, il gomito si sposta verso 10³. Il vantaggio pratico della CCDF è che, sommando, liscia la coda rumorosa della PDF (il fanning out).

Verifica sui dati sintetici della sezione 6:

```python
# Nota aggiunta: CDF, CCDF ed esponente della coda (continua dal blocco della sez. 6).
cdf = np.cumsum(U) / N               # P(r <= rho) per rho = r
ccdf = 1 - cdf                       # P(r > rho)
for rho in (1, 10, 100):
    i = np.searchsorted(r, rho, side="right") - 1
    print(f"rho={rho:3d}: CDF = {cdf[i]:.3f}, CCDF = {ccdf[i]:.3f}, somma = {cdf[i] + ccdf[i]:.1f}")
sel = (r >= 2) & (r <= 200) & (ccdf > 0)
g_coda, _ = np.polyfit(np.log(r[sel]), np.log(ccdf[sel]), 1)
print(f"pendenza della CCDF in log-log = {g_coda:.3f}  (atteso gamma+1 = {1 - alpha:.2f})")
```

Output:

```
rho=  1: CDF = 0.560, CCDF = 0.440, somma = 1.0
rho= 10: CDF = 0.917, CCDF = 0.083, somma = 1.0
rho=100: CDF = 0.988, CCDF = 0.012, somma = 1.0
pendenza della CCDF in log-log = -0.846  (atteso gamma+1 = -0.87)
```

La pendenza misurata (−0,85) è vicina a γ + 1 = −0,87. I valori di CDF non coincidono con quelli di Wikipedia (56% contro 40% a ρ = 1): i dati sintetici sono una power law pura con esponente scelto a mano, quelli reali no, e l'esempio serve solo a mostrare il calcolo e la relazione γ + 1.

---

## 12. User activity su X

*SD-02 @ 00:56:12*

Twitter divenne famoso per i **messaggi brevi**: 140 caratteri, poi 280 (dal 2017, slide 37). Rispetto ai blog, con articoli da leggere in minuti o mezz'ora, i tweet si leggevano subito e, se interessanti, si **retweetavano**: un utente poteva scrivere qualcosa di originale o ripubblicare contenuti altrui. Così le notizie si diffondevano molto in fretta: tsunami, terremoti, attacchi terroristici venivano riportati su Twitter prima che dalle grandi testate (SD-02 @ 00:57:06). Se seguo un utente, vedo i suoi tweet nella mia *timeline* e posso retweetarli ai miei follower.

Domanda: **le conclusioni di Wikipedia valgono anche per X?** Di solito i trend su larga scala sono simili fra piattaforme, ma a volte i pattern scoperti non si trasferiscono.

| Step | Su X |
|---|---|
| Dati | tweet pubblicati dagli utenti, scaricati con l'API di Twitter tramite il modulo Python **tweepy** |
| Analisi | numero di post pubblicati (tweet o retweet) da ogni utente in un periodo, l'analogo delle modifiche di Wikipedia |
| Finestre | settimane invece di mesi, perché all'epoca gli utenti pubblicavano moltissimo: 1 settimana (1-7 agosto), 2 settimane (1-14 agosto), "3 settimane" (1-28 agosto) [vedi Punti incerti] |
| Visualizzazione | PDF: utenti (y) che hanno pubblicato un certo numero di post (x) nelle tre finestre |

**Grafico (slide 38):** log-log, asse x *Number of Tweets* da 10⁰ a 10⁴, asse y *Number of users in period* da 10⁻² a 10⁻⁸ circa. Legenda *Period*: 8/1-8/7, 8/1-8/14, 8/1-8/28. Le tre curve si sovrappongono a sinistra e si separano solo oltre circa 10³, dove scendono in modo sempre più ripido; la curva della finestra più lunga resta più in alto. I punti sono più radi e regolarmente spaziati che nel grafico di Wikipedia.

### X contro Wikipedia

*SD-02 @ 00:59:45*

**Grafico (slide 39):** affiancati, a sinistra il grafico di X appena descritto, a destra il log-log di Wikipedia della sezione 5.

- Su X le tre PDF **non si sovrappongono** nella parte alta della scala dei tweet.
- In log-log la relazione fra numero di tweet e numero di utenti **non è lineare**: le curve di X sono concave, piegano verso il basso. Quindi le distribuzioni **non seguono esattamente una power law**. A voce (SD-02 @ 01:00:15): su Wikipedia c'è la decrescita rapida e rettilinea, su X "questa decrescita non la vediamo".
- Conclusione: il modello di Wikipedia **approssima** quello di X, ma non è identico. Allungando la finestra si vedono più utenti molto attivi e l'estremo alto della distribuzione si sposta verso l'alto.

> **Nota aggiunta:** l'asse y del grafico di X dice "Number of users in period" ma i valori sono minori di 1 (fino a 10⁻⁸): è una PDF normalizzata. I punti radi ed equidistanti dipendono dal **binning logaritmico** che il libro usa per questo grafico: bucket la cui ampiezza cresce di un fattore costante (equidistanti in scala log), con il conteggio di ogni bucket diviso per la sua ampiezza. Così la coda, dove ci sono pochi utenti per valore, non diventa un ventaglio di rumore e si possono stimare probabilità anche molto piccole. In R: `buckets = exp(seq(log(from), log(to), length.out=bucket.count + 1))`; l'equivalente NumPy è nel terzo fit della sezione 6. Il libro collega anche la non sovrapposizione al fallimento della power law: la stabilità della PDF nel tempo era una delle due premesse da cui la power law discende (sez. 9).

### Dove il modello regge

*SD-02 @ 01:00:49*

**Grafico (slide 40):** asse x *Tweets in Period 1* da 0 a 100, asse y *Average Tweets in Period 2 & 3* da 0 a 400. Due nuvole di punti quasi perfettamente rettilinee: *In Period 2* arriva a circa 200 per 100 tweet nel periodo 1, *In Period 3* a circa 400.

Il confronto r̄₂(r₁) della sezione 9 funziona anche qui: **il numero medio di tweet nei periodi 2 e 3 di chi ne pubblica q nel periodo 1 è un multiplo costante di q**. La conclusione tratta per Wikipedia vale anche per X, nonostante dati diversi e finestre più brevi (settimane invece di mesi).

> **Nota aggiunta:** il libro precisa che anche qui il modello vale "quasi": guardando da vicino i dati hanno un po' di curvatura e i primi punti non crescono in modo strettamente monotono. Aggiunge che i limiti imposti dalla piattaforma cambiano il comportamento osservabile: se un social network impone un massimo di connessioni, nessuno lo supererà. Per descrizioni accurate i modelli vanno raffinati piattaforma per piattaforma.

---

## 13. Riepilogo e compiti

*SD-02 @ 01:01:58*

- Il **numero di utenti cala bruscamente** al crescere del numero di azioni: molti utenti fanno poche azioni, parecchi ne fanno abbastanza, pochissimi ne fanno tantissime. Su Wikipedia i pochissimi sono i bot.
- Il conteggio delle attività in una finestra segue una **power law**: U(r) = K·rᵞ, retta in scala log-log.
- **PDF**: le distribuzioni dei vari periodi appartengono alla stessa famiglia e sono scalate l'una rispetto all'altra; una volta normalizzate, qualunque finestra si scelga, la funzione è la stessa.
- Periodi più lunghi mostrano più azioni da più utenti, ma **non un numero proporzionalmente maggiore** di utenti attivi (C21 ≈ 1,6 contro 1,9 dei giorni; C31 ≈ 2,2 contro 2,9).
- Le azioni di un utente in due periodi di lunghezza diversa sono **linearmente proporzionali** (r₂ = R12·r₁), su Wikipedia e su X.
- Una piccola frazione di utenti molto attivi può **influenzare fortemente la media**: per studiarli ci si concentra sulla coda, con la **CCDF**; la **CDF** serve per gli utenti meno attivi.
- Un modello che descrive bene una piattaforma **non vale necessariamente per un'altra** (Wikipedia contro X): può valere per alcuni aspetti e non per altri, e va adattato.

Il tratto SD-02 @ 01:02:34-01:03:12, saltato dalla prima trascrizione e recuperato con una seconda passata, aggiunge a voce: il contatore di attività (per esempio le modifiche alle pagine di Wikipedia) segue una power law; normalizzata, la PDF è la stessa qualunque periodo si prenda, uno, due o tre mesi; da qui le due osservazioni, che alcuni utenti sono più attivi di altri e che, cambiando periodo, il comportamento resta lo stesso.

**Compiti** (slide *Homework*, SD-02 @ 01:04:47): leggere il **capitolo 1**, *Users: The Who of Social Media*, del libro [1], con più attenzione alle parti viste a lezione. Il capitolo contiene anche argomenti non trattati, come la derivazione della power law, il binning logaritmico e il modello della frazione di attività degli utenti più attivi (Figure 1.13), su cui le note aggiunte di questo capitolo danno solo un'idea.

---

## Glossario

| Termine | Significato nel corso |
|---|---|
| User engagement | quanto l'utente è coinvolto nell'uso del servizio |
| Clique | gruppo di utenti tutti collegati fra loro (es. celebrity che si seguono a vicenda) |
| Finestra temporale | intervallo in cui si contano le azioni; preferibile continuo e chiuso |
| Frequenza d'uso | numero di volte in cui un utente è attivo nella finestra |
| Dump | grande file con l'esportazione di una base dati (es. revisioni di Wikipedia, XML) |
| TSV | *tab-separated values*, testo con campi separati da tabulazione |
| Timestamp | data e ora esatte di un evento |
| Namespace | "tipo" di pagina di Wikipedia (articolo, pagina utente, aiuto, ...) |
| Bot | account automatico che esegue modifiche ripetitive (manutenzione, anti-vandalismo) |
| Highly skewed / long-tail distribution | distribuzione molto asimmetrica: tanti valori piccoli, pochi valori enormi; segnale: media molto maggiore della mediana |
| Log-log plot | grafico con scala logaritmica su entrambi gli assi |
| Fanning out | allargamento a ventaglio dei punti all'estremo destro del log-log |
| Power law | U(r) = K·rᵞ; in log-log è una retta di pendenza γ |
| Rank | posizione di un utente nella lista ordinata per attività decrescente |
| Principio di Pareto, regola 80/20 | una piccola frazione dei partecipanti produce la maggior parte delle azioni |
| Macro, mid-tier, micro-influencer | livelli di popolarità, dalla testa alla coda della distribuzione |
| PDF | *probability density function*: istogramma normalizzato, P(r) = U(r)/ΣU(i) |
| C_ij | rapporto fra utenti attivi nel periodo i e nel periodo j |
| Burst activity | attività molto intensa in un periodo breve, spesso stagionale |
| Query log | registro delle ricerche: utente anonimo, query, timestamp, clic e posizione |
| Funzione indicatrice I(·) | vale 1 se la condizione è vera, 0 altrimenti |
| R12 (R21 nel libro) | costante di proporzionalità fra le azioni di un utente in due periodi |
| CDF | P(r ≤ ρ): frazione di utenti con al più ρ azioni; per i meno attivi |
| CCDF, tail distribution | P(r > ρ) = 1 − CDF(ρ): frazione con più di ρ azioni; per i più attivi |
| tweepy | libreria Python per l'API di Twitter usata nel libro |
| Binning logaritmico | bucket di ampiezza crescente in progressione geometrica (nota aggiunta) |

## Punti incerti

- **SD-02 @ 00:55:50-00:56:08:** anche la seconda passata di trascrizione restituisce solo "E... moltissimi amici e sono nella coda": il tratto è in gran parte pausa o parlato non intelligibile [?]. Probabilmente un esempio di utente molto connesso che sta nella coda della distribuzione.
- **SD-02 @ 01:02:39-01:03:07:** recuperato con una seconda passata (`scripts/ritrascrivi_tratti.py`, 22/10/2026); integrato nel riepilogo.
- **Finestre di X:** la slide dice "3 weeks (Aug. 1 to 28)" e la legenda del grafico "8/1-8/28", ma dal 1° al 28 agosto ci sono 28 giorni, cioè 4 settimane. Il libro parla di "three-week period" ma il suo codice scarica gli ultimi 28 giorni. Nel grafico della slide 40 le pendenze sono circa 2 (periodo 2) e 4 (periodo 3), coerenti con 2 e 4 settimane. È probabile che il periodo 3 sia di 4 settimane, ma non è verificabile.
- **SD-02 @ 00:39:26:** "gennaio, febbraio e maggio": lapsus per marzo, corretto nel testo.
- **SD-02 @ 00:26:39:** "club bot ng, mouse bot, ad bot" nella trascrizione = ClueBot NG, EmausBot, Addbot (dalla slide).
- **SD-02 @ 00:16:14 e slide 8:** "~1K edits" per i bot, in contrasto con la tabella della slide 14; trattato come Correzione (sez. 4).
- Segmenti a bassa confidenza: solo i due di SD-02 @ 00:56:08-00:56:12 (−0,33), adiacenti al primo vuoto.

## Materiale usato

- Video: `video/SD-02.mp4`; trascrizione `out/SD-02/SD-02-trascrizione.md`, segmenti `SD-02.json`, `SD-02-bassa-confidenza.json`, frame `out/SD-02/frames/` (controllati 00:55:39 e 01:01:37)
- Slide: `Materiale/Portale/estratti/2_User_Activity_SDA25.pdf` (tutte le 41 pagine renderizzate e guardate); `Materiale/Teams/estratti/Slides/2_User_Activity_SDA26.pdf` (confronto testuale, pagina 11 renderizzata)
- Libro [1]: `Materiale/Portale/estratti/books/Social Media Data Mining and Analytics.pdf`, capitolo 1 (pp. 1-40)
- Script di verifica: `out/lezione-02/verifica_sd02.py`, output in `verifica_sd02_output.txt`
