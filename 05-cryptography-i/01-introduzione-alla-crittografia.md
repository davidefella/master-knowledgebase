# 01 - Introduzione alla crittografia

> Fonte Notion: https://app.notion.com/p/3e312abc808d81c880f8f848850428ab — ultima modifica 2026-09-22T13:31:05.645Z

**Docente:** Elia Onofri — Master in Data Analytics, Roma Tre, A.A. 2026
**Registrazione:** `CR-01`, durata 02:04:21
> Il docente chiama questa lezione «Introduzione alla Crittografia»: è pensata per dare una base comune a studenti con background eterogenei, non per formalizzare. Lui stesso avverte a `@ 01:11:56`: *«non voglio andare eccessivamente nel dettaglio di nessuna di queste tematiche, lo scopo non è quello di spaventarvi oggi»*.
## 1. Inquadramento del corso
### Il docente — `@ 00:01:19`
Laurea triennale in matematica, magistrale in computer science, dottorato in matematica per le applicazioni, tutti a Roma Tre. Professore a contratto a Roma Tre e ricercatore al CNR, Istituto per le Applicazioni del Calcolo.
Distingue tre ambiti: **matematica pura** (algebra, analisi), **applicata** (analisi numerica: «non si sporca eccessivamente le mani nel mondo reale»), e **per le applicazioni**, che formalizza problemi reali.
Ambiti di ricerca citati come spunti per la tesina (`@ 00:03:18`): teoria dei grafi, crittografia, bioinformatica, beni culturali, machine learning, security and privacy, simulazioni numeriche, ottimizzazione di flussi.
I due moduli (`@ 00:03:48`): **Crittografia I** — l'arte che studia i cifrari; **Crittografia Case Study** — l'overlay ingegneristico attorno alla sicurezza dei dati.
### Prerequisiti — `@ 00:04:31`
- Programmazione a livello generico: cos'è un linguaggio imperativo.
- Confidenza minima con Unix: comandi di base, cos'è una shell.
- Python suggerito ma non obbligatorio: strutture dati, I/O su file («leggere chiavi, scrivere chiavi»), test e debugging, `import`. **Nessuna libreria specifica richiesta.**
### Procedura d'esame — `@ 00:06:28` – `00:10:50`
Vedi la pagina **Assessment** per il dettaglio completo.
### Roadmap del modulo — `@ 00:10:50`
<table header-row="true">
<tr>
<td>Lezione</td>
<td>Contenuti annunciati</td>
</tr>
<tr>
<td>**1** (3h)</td>
<td>Storia, concetti base, attori, contesto, simmetrica vs asimmetrica, cenni di crittoanalisi</td>
</tr>
<tr>
<td>**2** (2h)</td>
<td>Vernam, Shannon e segretezza perfetta, stream cipher (LFSR, Salsa20), cifrari a blocchi (DES, AES), lightweight</td>
</tr>
<tr>
<td>**3** (3h)</td>
<td>Chiave pubblica, Diffie–Hellman, RSA, ElGamal, Paillier, Rabin, algebra modulare, curve ellittiche</td>
</tr>
<tr>
<td>**4**</td>
<td>Hash (Merkle–Damgård, spugna, SHA-3), MAC, firme digitali e aspetti legali, schemi di impegno da Lamport agli alberi di Merkle</td>
</tr>
</table>
Sul cifrario "perfetto" anticipa una tesi che attraversa tutto il corso (`@ 00:13:33`): *«un cifrario non può essere perfetto — per essere infallibile diventerebbe non pratico»*.
## 2. Che cos'è la crittografia
### Etimologia — `@ 00:16:50`
Dal greco *kryptós* (nascosto) + *graphía*: **l'arte di scrivere in maniera nascosta**.
### Crittografia contro steganografia — `@ 00:17:59`
- **Steganografia**: nascondere *l'esistenza* del messaggio. I persiani che tatuavano il messaggio sulla testa degli schiavi e aspettavano la ricrescita dei capelli. **Ma se lo avessero trovato, lo avrebbero letto.**
- **Crittografia**: risponde alla domanda «se il mio avversario cattura il mio messaggio, quel messaggio è inutile per il mio avversario».
### encode contro encrypt — `@ 00:26:20`
- **encrypt** = cifratura, codifica crittografica (**usa una chiave**);
- **encode** = trasformazione da una rappresentazione a un'altra **senza chiave**.
In italiano si dice «codifica» per entrambe, e questo genera confusione.
## 3. Crittografia antica
<table header-row="true">
<tr>
<td>Epoca</td>
<td>Evento</td>
</tr>
<tr>
<td>V sec. a.C.</td>
<td>Scitala spartana</td>
</tr>
<tr>
<td>I sec. a.C.</td>
<td>Cifrario di Cesare</td>
</tr>
<tr>
<td>1460 ca.</td>
<td>Alberti, *De Componendis Cifris* — nascita della crittografia moderna</td>
</tr>
<tr>
<td>II guerra mondiale</td>
<td>Macchina Enigma</td>
</tr>
<tr>
<td>dal 1975–76</td>
<td>Crittosistemi moderni: AES, RSA</td>
</tr>
</table>
### La scitala spartana — `@ 00:20:33`
Un bastone attorno al quale si arrotolava una striscia di pelle. Arrotolata su un bastone **del diametro corretto** le lettere si allineano; srotolata è priva di senso.
È un caso ibrido: crittografia perché nasconde la scrittura, steganografia perché serve un oggetto fisico. Ed è già più avanzato dell'Atbash, perché **il diametro del bastone funziona da chiave**.
### Il cifrario Atbash — `@ 00:22:32`
Usato nel Libro di Geremia, inizialmente per nascondere la parola "Babele". **Monoalfabetico**: prima lettera ↔ ultima (*alef* ↔ *tav*), da cui il nome. Sull'alfabeto latino: A→Z, B→Y, C→X.
Il limite è decisivo: **non ha alcuna variabile di sicurezza**. Noto il metodo, il messaggio è decifrato. Per questo il docente propone di chiamarlo **protocrittografia**.
### Il quadrato di Polibio — `@ 00:24:19`
Nasce non come metodo crittografico ma come **metodo di rappresentazione dell'informazione**: trasmettere un messaggio da un avamposto all'altro senza documento scritto.
Dalla slide: mappa ogni lettera su $`(i,j) \in \{1,\dots,5\}^2`$, griglia $`5\times5`$ per le 24 lettere greche, ogni coppia trasmessa con **segnali di torce**. Esempio: $`\kappa = (2,5)`$, 2 torce a sinistra e 5 a destra.
⚠️ **Divergenza.** A voce il docente dice che K è «la 14ª lettera dell'alfabeto»: è l'**11ª**. La coordinata $`(2,5)`$ della slide è però corretta.
**Eredità**: l'idea sopravvive come base dei **cifrari poligrafici** — lettera → coppia di simboli, **sistema digrafico**, che raddoppia il testo. Esempi: Playfair, ADFGX.
**Riferimento** dato dal docente: Simon Singh, *Codici e segreti*, da cui dichiara di aver tratto parte delle slide.
## 4. Il cifrario di Cesare
`@ 00:29:44`
Alfabeto in forma **circolare**, **shift fisso**: con $`+3`$, A→D, B→E, C→F.
$`\text{CIAO} \xrightarrow{\;k=3\;} \text{FLDR}`$
✅ *Verificato per esecuzione.*
La mappa è **biiettiva**. Per decifrare basta shiftare indietro di tre.
### Perché conta, e perché non basta — `@ 00:31:17`
Il docente lo difende dal giudizio di banalità: siamo nel I secolo a.C., «in cui già saper leggere era una sfida». Ed è più avanzato dell'Atbash perché ha **25 shift possibili** — ✅ *verificato: *$`26-1`$*, *$`k=0`$* lascia il testo invariato*.
Ma 25 è un numero che «una persona con tanta voglia di lavorare» può esaurire a mano. E resta **monoalfabetico**.
## 5. Dal monoalfabetico ai nomenclatori
Intorno all'anno 1000 compaiono i **cifrari per sostituzione**: schema arbitrario, anche un rimescolamento casuale.
L'Italia è centrale, spinta dalle **repubbliche marinare**.
**Nomenclatori** (`@ 00:34:26`): parole comuni sostituite da lettere, caratteri o numeri. **Gabriele Lavinde**, **1379**, forse il primo manuale di cifrari storicamente attendibile.
Perché funzionava (`@ 00:35:41`): nel medioevo esistono centinaia di metodi diversi, e **l'attaccante non sa quale sia stato usato**.
**Venezia** (`@ 00:36:20`): lettere del Doge **Michele Steno**, prima lettera cifrata conosciuta del **1411**. Spesso **non si cifrava l'intero messaggio, ma solo le parole importanti** — in una lettera per fissare un incontro, solo giorno, mese e ora.
**1530: primo ufficio crittografico di Stato**, sotto **Giovanni Soro**, nominato dal Consiglio dei Dieci.
**Francia** (`@ 00:36:56`): i **Rossignol** introducono nel **1640** le *Grandes Chiffres*, circa **11.000 gruppi**, usate da Luigi XIV e ritenute indecifrabili. Rotte «poco meno di 50 anni dopo». Il metodo resta in uso fino alla campagna di **Russia del 1812**.
**Cifrari polifonici** (`@ 00:39:40`): si cifra il suono, non il carattere. Doppio scopo: confondere **e accorciare** il messaggio.
### Il problema di fondo — `@ 00:39:03`
> «Se l'attaccante capisce il metodo di cifratura utilizzato, tutte queste cifre diventano inutilizzabili, perché sarà in grado di decifrare non solo il messaggio che ha intercettato, ma anche **tutti i messaggi futuri**.»
Da qui il problema della **distribuzione**, che nella crittografia contemporanea diventa il problema delle **chiavi**.
## 6. Alberti e la nascita della crittografia moderna
**Leon Battista Alberti** (1404–1472). Nel **1466** scrive il ***De Componendis Cifris***, pubblicato postumo, inedito fino al **1568**.
### Perché è uno spartiacque — `@ 00:42:30`
> **Un buon sistema crittografico è un sistema che, pur essendo noto all'avversario, resta indecifrabile.**
### Il disco cifrante — `@ 00:43:53`
Due **dischi concentrici** con due copie dell'alfabeto, eventualmente in ordine casuale. **Ogni rotazione produce un cifrario monoalfabetico diverso**: ruotandolo durante la cifratura si ottiene il **primo cifrario polialfabetico** della storia.
Il docente segnala che l'**Associazione Nazionale Italiana di Crittografia** si chiama *De Componendis Cifris*.
### Perché non ebbe successo subito — `@ 00:46:12`
**Troppo complesso per l'uso pratico**: bisognava ricordare le frasi chiave, ruotare il disco, e serviva l'oggetto fisico. Riscoperto solo nel **XX secolo**. Nonostante tutto, «per quasi 400 anni è rimasto considerato sicuro dai più».
### Altre figure
- **1499** — **Johannes Tritemio**, *Steganographia*: all'epoca l'arte di nascondere i messaggi era ritenuta magia, e il trattato è condito da una narrazione mistica di comunicazioni angeliche, ma contiene metodi reali.
- **Giovanni Battista Bellaso** — **il primo a introdurre il concetto di chiave**. La sicurezza deve essere **indipendente dalla conoscenza del modo in cui il sistema è costruito**, inclusi quelli che oggi chiameremmo i **vettori di inizializzazione**.
## 7. Il cifrario di Vigenère
Il docente lo colloca con precisione: dopo Cesare, **il secondo cifrario più importante prima di Enigma**. Ma precisa che è **una riedizione**: il *Traicté des chiffres* (**1586**) combina la *tabula recta* di **Tritemio** con il **concetto di chiave** di **Bellaso**.
> «Spesso nella cultura di massa si pensa al cifrario di Vigenère ma non si pensa a quelli che sono venuti prima, primo fra tutti Leon Battista Alberti.»
### L'esempio della slide — `@ 00:56:07`
<table header-row="true">
<tr>
<td></td>
<td>Sequenza</td>
</tr>
<tr>
<td>**Plaintext**</td>
<td>A T T A C K A T M I D N I G H T</td>
</tr>
<tr>
<td>**Keyword**</td>
<td>L E M O N L E M O N L E M O N L</td>
</tr>
<tr>
<td>**Ciphertext**</td>
<td>L X F O P V E F R N H R Y G U Z</td>
</tr>
</table>
$`A + L = L \qquad \text{(A è la lettera 0, L shifta di 11)}`$
🔴 **Divergenza grave — l'esempio della slide è sbagliato.** Il ciphertext è corretto solo per le prime 8 lettere:
```javascript
posizione     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
plaintext     A  T  T  A  C  K  A  T  M  I  D  N  I  G  H  T
chiave        L  E  M  O  N  L  E  M  O  N  L  E  M  O  N  L
corretto      L  X  F  O  P  V  E  F  A  V  O  R  U  U  U  E
slide         L  X  F  O  P  V  E  F  R  N  H  R  Y  G  U  Z
```
Il ciphertext della slide è quello dell'esempio canonico `ATTACKATDAWN` → `LXFOPVEFRNHR`: il plaintext è stato allungato senza ricalcolare il cifrato.
### Vantaggi e limiti
**Vantaggi**: la stessa lettera viene cifrata con lettere diverse; più difficile da rompere con l'analisi delle frequenze.
**Limiti**: **sensibilità all'allineamento** — persa una lettera, «tutto il significato diventa illeggibile»; ciphertext della **stessa lunghezza** del plaintext; **non compressivo**.
### La rottura: il test di Kasiski — `@ 00:59:08`
Si guadagnò il nome di ***le chiffre indéchiffrable***. Nel **1863** **Friedrich Kasiski** introduce il test, che il docente definisce «peraltro banale»:
> Si cercano **terne o quaterne di lettere che si ripetono** nel cifrato, si suppone che siano pezzi di parole cifrate nella stessa maniera, e da lì si calcola la **lunghezza della chiave**.
Il passaggio chiave: nota la lunghezza $`n`$, «invece di avere un cifrario polialfabetico ci ritroviamo con $`n`$ cifrari monoalfabetici».
### Il ponte verso Enigma — `@ 01:01:28`
«L'idea che sta dietro la macchina Enigma è molto simile, perché Enigma era un metodo **meccanizzato** per ruotare gli alfabeti in maniera pseudo-casuale attraverso dei rotori.»
## 8. Vista matematica: aritmetica modulare
### L'orologio — `@ 01:02:39`
Su un orologio a 12 ore, 9 + 5 non fa 14, fa 2. «Ogni volta che superiamo il numero 12, ripartiamo da 0.»
### Notazione — `@ 01:05:00`
- $`\mathbb{Z}`$ — gli interi;
- $`\mathbb{Z}_n`$ — le **classi resto modulo **$`n`$, fra $`0`$ e $`n-1`$;
- $`\mathbb{F}_2`$ — per $`n=2`$ si usa $`\mathbb{F}`$ per **campo**, perché 2 è primo.
**In **$`\mathbb{F}_2`$: la somma è lo **XOR**, la moltiplicazione è l'**AND**.
### Le lettere come $`\mathbb{Z}_{26}`$
A ↦ 0, B ↦ 1, …, Z ↦ 25. Cesare è già aritmetica modulare: cifrando X con $`+3`$ si arriva alla A, «che sarebbe la zeresima lettera», riducendo modulo 26.
### Annotazione scritta in diretta — `@ 01:08:39` – `01:09:12`
> Il docente scrive **a mano con il mouse** sopra la slide. **Questo contenuto non è nelle slide: sta solo nel video.**
$`\mathbb{Z}_N \qquad\qquad (\mathbb{F}_2,\; +,\; \times)`$
con sotto $`\oplus`$ e $`\wedge`$, e a destra la funzione di cifratura di Cesare:
$`f_K(x): \mathbb{Z}_{26} \longrightarrow \mathbb{Z}_{26}, \qquad x \longmapsto x + K \bmod 26`$
La slide riporta invece la forma generale $`y = x + v \bmod N`$.
### Interpretazione algebrica — `@ 01:09:44`
La struttura è un **gruppo commutativo**: chiusura, elemento neutro (la A, perché vale 0), inverso, associatività, commutatività.
## 9. I quattro obiettivi della crittografia
### Confidenzialità — `@ 01:12:28`
Il messaggio può essere letto solo dal destinatario autorizzato, e **resta segreto anche se il ciphertext trapela**.
Protegge nelle **tre fasi del dato**: in **trasmissione**, in **archiviazione**, **in elaborazione**. Ed è qui che il docente si ferma, perché è il punto più rilevante per un master in data analytics.
**L'esempio della cartella clinica** (`@ 01:17:24`) — il ponte fra crittografia e data science:
> Un sistema di IA classifica una cartella clinica. Non abbiamo la potenza per eseguirlo, Google sì, ma non vogliamo dargli la nostra cartella clinica. Allora la inviamo **cifrata**. Esistono tecniche per cui, a valle della valutazione sul cifrato, si ottiene una **risposta cifrata** che, decifrata, è equivalente a quella che si sarebbe ottenuta sul dato in chiaro.
È la **crittografia omomorfa**, annunciata come spoiler.
### Integrità — `@ 01:13:48`
Il messaggio **non può essere stato modificato**. L'avversario cattura il cavaliere, non riesce a leggere il messaggio, **ma può riscriverlo** e consegnarlo al posto suo.
Qui introduce tre cose insieme: l'attacco **man in the middle**, l'**integrità**, e il **sigillo di ceralacca** — che però garantisce anche l'autenticità.
Va garantita rispetto a **due** minacce: **attacco avversario** (tampering) e **errore accidentale** — «il codice Morse: batto punto linea punto invece di punto linea linea, lì ho commesso un errore e nessuno se ne può accorgere». Più il **replay attack**.
### Autenticità — `@ 01:15:27`
Garantisce **l'origine**. Previene gli **impersonation attack**. I canali alla base di internet **non la garantiscono**, e per questo richiedono sovrastrutture.
### Non ripudio — `@ 01:23:53`
Il mittente non deve poter negare. L'analogia è la **firma notarile**: posso contestare una firma autografa, ma non un atto firmato davanti a un notaio.
Esempio moderno: la **PEC** — «il server l'ha processata e si è fatto garante dell'identità».
## 10. Applicazioni
**Comunicazione sicura**: HTTPS, **VPN** («un tunnel end-to-end: il traffico viene oscurato e posso far finta di essere quel computer»), messaggistica end-to-end.
> Osservazione controcorrente su Telegram (`@ 01:31:58`): rispetto a WhatsApp, che ha protocolli più oscurati, **Telegram pubblica interamente i suoi protocolli**, pur usando un metodo proprio (MTProto). E il controesempio **Bridgefy**: messaggistica Bluetooth per zone di guerra, «aveva grossi bachi e ha messo a rischio diverse vite».
**Autenticazione**: password («peccato che oggigiorno non si ritenga più sufficiente»), **MFA** — **una cosa che conosco** e **una cosa che possiedo** —, **certificati digitali** e la **tripla stretta di mano**.
**Protezione dei dati**: at rest, in transit, in execution. Access control, *attribute-based encryption*.
**Commercio e criptovalute**: firma digitale, acquisti online, **double spending**, **smart contract** e il requisito aggiuntivo dell'**anonimato**.
## 11. Attori e modello di comunicazione
<table header-row="true">
<tr>
<td>Nome</td>
<td>Ruolo</td>
</tr>
<tr>
<td>**Alice** e **Bob**</td>
<td>Le due parti</td>
</tr>
<tr>
<td>**Eve**</td>
<td>*Evil*, fa l'**eavesdropper**</td>
</tr>
<tr>
<td>**Mallory**</td>
<td>*Malicious attacker*, può **alterare**</td>
</tr>
<tr>
<td>**Trent**</td>
<td>*Trusted party*</td>
</tr>
<tr>
<td>**Oscar**</td>
<td>L'*outsider* curioso</td>
</tr>
<tr>
<td>**Artù e Merlino**</td>
<td>Nelle prove a conoscenza zero</td>
</tr>
</table>
> Nota personale: «Io in realtà li uso al contrario, tipicamente uso Bob come mandante e Alice come ricevente».
### Il modello — `@ 01:43:23`
> «Tipicamente quando parliamo di crittografia ci vogliamo trasmettere i dati su un canale insicuro, altrimenti non avremmo bisogno di crittografia.»
Alice cifra con un **meccanismo che può essere arbitrariamente noto** e una **chiave**; Bob decifra con la stessa chiave (simmetrico) o una **chiave surrogata** (asimmetrico); Eve ascolta e può alterare.
## 12. Spazi e funzioni di cifratura
- **Plaintext** ($`M`$), **Ciphertext** ($`C`$), **Chiave** ($`K`$).
Osservazione: in Vigenère i tre spazi coincidono, ma **in generale non è così**.
### Il principio fondamentale — `@ 01:46:21`
> **La sicurezza di un crittosistema non deve essere basata sulla segretezza dell'algoritmo, ma sulla resistenza della chiave.**
> **Nota aggiunta:** è il principio di Kerckhoffs. Il docente ne enuncia il contenuto ma non lo nomina.
**L'esempio di Enigma**: i messaggi restarono sicuri **anche dopo** che gli alleati ebbero una copia della macchina. Il dettaglio storico: i codici erano stampati su **carta idrosolubile**, perché al primo segno di attacco i comandanti degli U-Boot potessero gettarli in acqua.
### Le funzioni — `@ 01:48:54`
$`E_k: \mathcal{M} \to \mathcal{C}, \qquad D_k(E_k(m)) = m`$
La mappa **non deve necessariamente essere biiettiva, ma deve essere invertibile**.
> «Questa è una formalizzazione matematica di un concetto banale: se prima cifro e poi decifro devo riottenere il messaggio.»
## 13. Simmetrica, asimmetrica, ibrida
### Simmetrica
**Stessa chiave**. Tutti i cifrari visti finora sono simmetrici. Problema: condividere la chiave richiede **un canale sicuro** in qualche momento.
**Analogia**: il **lucchetto a combinazione**. «Quello che lo rende sicuro è la conoscenza della combinazione. Uso la stessa combinazione per aprirlo e per chiuderlo.»
### Asimmetrica
**Chiave pubblica** per cifrare, **chiave privata** per decifrare. **Non serve un canale sicuro.** Problema: costo computazionale.
**Analogia**: la **coppia chiave-lucchetto**. Nella versione postale: «spedisco il mio lucchetto aperto, l'altra persona mette il messaggio nella scatola, la chiude col mio lucchetto e me la rimanda. **Solo io ho la chiave.**»
E il rovescio: lo stesso meccanismo si può usare **per dimostrare al mondo di possedere la chiave**.
<table header-row="true">
<tr>
<td>Feature</td>
<td>Symmetric</td>
<td>Asymmetric</td>
</tr>
<tr>
<td>Keys</td>
<td>Same key</td>
<td>Public/private key pair</td>
</tr>
<tr>
<td>Speed</td>
<td>Fast</td>
<td>Slower</td>
</tr>
<tr>
<td>Use Case</td>
<td>Bulk data encryption</td>
<td>Key exchange, signatures</td>
</tr>
<tr>
<td>Security</td>
<td>Key must remain secret</td>
<td>Public key can be shared</td>
</tr>
</table>
### Ibrida — `@ 01:57:32`
«**Tipicamente si utilizza la crittografia ibrida.**» Sull'esempio di **TLS**: accordo via **asimmetrica** → canale sicuro → **chiave di sessione simmetrica** → i dati veri cifrati con quella.
Il costo: due approcci, «quindi il doppio dei modi di essere rotti di uno solo».
⚠️ **Divergenza.** «la sicurezza incondizionata della crittografia **simmetrica**, ma anche la velocità della crittografia **simmetrica**»: la prima doveva essere *asimmetrica*.
## 14. Modelli di attacco
**La sicurezza perfetta non è realizzabile in pratica**, quindi va definita **rispetto a un rischio**:
- **un ordine all'esercito** — difficile da rompere *adesso*; «se l'avversario lo rompe dopodomani, non subisco danno»;
- **un documento secretato** — deve resistere a «30, 40, 50 anni di tentativi».
Conseguenza: bisogna **prevedere il futuro**, cioè quanto diventerà potente l'attaccante.
L'**adversarial model** comprende **potenza computazionale**, **capacità** (può cifrare, decifrare, ha accesso alla macchina) e **conoscenze**.
<table header-row="true">
<tr>
<td>Attack Type</td>
<td>Attacker's Capability</td>
</tr>
<tr>
<td>**COA**</td>
<td>Only ciphertexts are available</td>
</tr>
<tr>
<td>**KPA**</td>
<td>Some plaintext–ciphertext pairs are known</td>
</tr>
<tr>
<td>**CPA**</td>
<td>Attacker can encrypt chosen plaintexts</td>
</tr>
<tr>
<td>**CCA**</td>
<td>Attacker can decrypt chosen ciphertexts</td>
</tr>
</table>
Su **CPA**: è il caso classico in cui si conosce la **chiave pubblica** — «posso cifrare tutte le volte che voglio, ma non posso cifrare un messaggio che non conosco».
## Chiusura — `@ 02:03:22`
Il docente annuncia che carica le slide su Teams «senza le transizioni», e lascia una **sezione aggiuntiva sulla crittoanalisi** non ripresa a lezione: analisi delle frequenze e note sul test di Kasiski. Le ultime slide mostrate includono l'istogramma delle frequenze dell'inglese (E al 12,7%, T al 9,1%).
## Appendici
### Punti a bassa confidenza
L'audio è ottimo: **nessun segmento** sotto $`-0.6`$ su 988, e nessuno sotto $`-0.3`$. I punti seguenti sono marcati per **contenuto dubbio**.
<table header-row="true">
<tr>
<td>Timestamp</td>
<td>Punto</td>
<td>Dubbio</td>
</tr>
<tr>
<td>`@ 00:34:26`</td>
<td>«arcivescovo Pietro di Garcia»</td>
<td>Nome probabilmente distorto</td>
</tr>
<tr>
<td>`@ 00:41:48`</td>
<td>«Meister poi introduce…»</td>
<td>Nome non identificabile con certezza</td>
</tr>
<tr>
<td>`@ 00:51:23`</td>
<td>«200 — 208 frasi»</td>
<td>Il docente si corregge in diretta</td>
</tr>
<tr>
<td>`@ 00:53:33`</td>
<td>Lettera omessa nella tavola originale</td>
<td>Dice prima Z, poi H, poi ammette di non ricordare</td>
</tr>
</table>
### Divergenze
1. 🔴 `@ 00:56:07` — esempio di Vigenère: ciphertext sbagliato, appartiene a `ATTACKATDAWN`.
2. ⚠️ `@ 00:25:37` — «K è la 14ª lettera»: è l'11ª. La coordinata $`(2,5)`$ è corretta.
3. ⚠️ `@ 01:58:36` — «simmetrica» detto due volte al posto di «asimmetrica».
4. ℹ️ `@ 00:27:49` — l'avvertimento sulla prima impressione è attribuito a Erodoto a voce, a Polibio sulla slide.
### Materiale
157 frame estratti, 138 dopo deduplica, **94 slide logiche** dopo triage. Frame letti visivamente: `00:26:33`, `00:31:33`, `00:56:07`, `00:57:19`, `01:09:49`, `01:45:21`, `01:56:28`, `01:57:10`, `02:03:21`. Conti verificati: Cesare `CIAO`/$`k=3`$, Vigenère, coordinate di Polibio, spazio delle chiavi di Cesare.
