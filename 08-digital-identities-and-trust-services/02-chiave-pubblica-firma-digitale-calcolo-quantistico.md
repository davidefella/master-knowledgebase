# 02 - Usi della chiave pubblica, CyberChef AES e RSA, key wrapping, stati della cifratura, cifratura omomorfa, firma digitale, formati di firma, introduzione al calcolo quantistico

*DI-02, registrazione Teams del 15/10/2025 (portale), 1:54:57; parlato fino a 1:54:55. Integrazioni da Teams 1 (21/09/2026, da 0:29:34 alla fine).*

> **Come leggere questo capitolo.** I primi 50 minuti di DI-02 rispiegano a voce le slide che in DI-01 erano scorse **senza audio** (RSA, curve ellittiche, casi d'uso della chiave pubblica, riservatezza+autenticità, svantaggi della simmetrica, key wrapping). Il testo di quelle slide è già trascritto nel **capitolo 01, sezione 12**, insieme alle integrazioni di Teams 1 fino a 0:29:34: qui si rimanda e si scrive per esteso solo il commento a voce del 2025. Da 0:49:51 il materiale è nuovo: stati della cifratura, cifratura omomorfa, firma digitale, PAdES e JSON, calcolo quantistico. Il docente dichiara due volte che la firma digitale è "il concetto logico più difficile dell'intero corso" (sezione 9).

## Indice

1. Ripresa: RSA e curve ellittiche
2. I due usi della chiave pubblica: riservatezza e autenticità
3. Laboratorio: AES e RSA con CyberChef
4. Riservatezza e autenticità insieme; il costo della chiave pubblica
5. Svantaggi della crittografia simmetrica
6. Key wrapping
7. I tre stati della cifratura
8. Cifratura in uso: la cifratura omomorfa
9. Firma digitale
10. Firma digitale e firma autografa
11. Firme sui PDF: PAdES e signature wrapping attack
12. Firma e cifratura di JSON: JWT, JWS, JWE, JAdES
13. Introduzione al calcolo quantistico
14. Crittografia quantistica: le tre accezioni (solo Teams 2026)
15. Glossario
16. Punti incerti
17. Esame

## 1. Ripresa: RSA e curve ellittiche

*DI-02 @ 00:00:02-00:05:13*

Il docente riparte da "la scorsa volta dovremmo essere arrivati a parlare della crittografia RSA" e chiede conferma in chat che le slide siano visibili. Slide **"RSA cryptography"** (*DI-02 @ 00:00:02*) ed **"Elliptic Curve Cryptography (ECC)"** (*00:00:24*, *00:04:54*): testo e immagini nel capitolo 01, sezioni 11 e 12.

**RSA** (*DI-02 @ 00:00:42*). Anche dispositivi molto semplici come le smart card sanno **moltiplicare** numeri interi, anche enormi. Dalla chiave privata (i due primi) si ottiene moltiplicandoli un numero ancora più grande: la chiave pubblica. L'asimmetria sta qui: moltiplicare è computazionalmente banale, **fattorizzare** un intero enorme è molto complesso per i calcolatori classici, anche sapendo a priori che i fattori sono solo due. La chiave privata RSA "è costituita di fatto" dai due primi, "in realtà non è proprio così ma non entro nei dettagli tecnici"; le proprietà dell'**algebra modulare** consentono elevamenti a potenza che, fatti in un verso, si invertono con l'altra chiave della coppia (*00:02:24*).

Esempio piccolo (*DI-02 @ 00:05:43*): $33 = 3 \cdot 11$ è banale da fattorizzare; se la "chiave pubblica 33" fosse lunga migliaia di bit, trovare anche uno solo dei due fattori (l'altro segue per divisione) sarebbe computazionalmente difficile. Convenzione per il resto del corso: con RSA, "chiave privata" = i due fattori primi, "chiave pubblica" = il loro prodotto. Verifica per esecuzione: $33 = 3 \cdot 11$.

> **Correzione:** a *00:00:42* il docente dice che il prodotto di due numeri "da 100 cifre ciascuno" ha "decine di migliaia di cifre". Il prodotto di due numeri di 100 cifre ha 199 o 200 cifre (le cifre si sommano, non si moltiplicano). Verificato per esecuzione: due primi casuali di 100 cifre danno un prodotto di 200 cifre.

> **Nota aggiunta:** la precisazione del docente ("non è proprio così") è corretta: in RSA la pubblica è $(N, e)$ e la privata l'esponente $d$ con $e \cdot d \equiv 1 \pmod{\varphi(N)}$; $p$ e $q$ servono a calcolare $d$. Dettagli nel capitolo 01, sezione 11.

**Curve ellittiche** (*DI-02 @ 00:02:53-00:05:13*). L'argomento è "estremamente specialistico" e il docente rimanda al corso di crittografia del master. La ECC si basa sulla risoluzione di **equazioni polinomiali** di grado piccolo (due variabili, polinomio di terzo grado), non nei reali ma nell'**algebra modulare**: si cercano solo soluzioni intere $(x, y)$. Formalmente è lo stesso problema, ma computazionalmente è molto diverso e appartiene alla teoria dei numeri e alla geometria algebrica, soprattutto quando il polinomio e il modulo primo $p$ (in verde nella slide) sono scelti in modo adeguato. Non tutti i polinomi vanno bene: si usano **curve specifiche**. I bit della chiave danno informazioni sui coefficienti del polinomio "in maniera un po' più complessa".

> **Nota aggiunta:** la sicurezza ECC poggia sul logaritmo discreto su curva ellittica (dato $Q = kG$, trovare lo scalare $k$): la chiave privata è $k$, la pubblica il punto $Q$; i coefficienti $a, b$ e il primo $p$ sono parametri pubblici della curva, non la chiave. Vedi la nota nel capitolo 01, sezione 12.

## 2. I due usi della chiave pubblica: riservatezza e autenticità

*DI-02 @ 00:05:13-00:16:31*

**Slide "Basic use cases of asymmetric ciphers"** (*DI-02 @ 00:08:09-00:16:10*): testo e schema nel capitolo 01, sezione 12. In DI-02 la versione a schermo ha le etichette delle chiavi: a sinistra $\kappa^{\text{pub}}_{\text{Alice}}$ (verde, "Alice's public key") per cifrare e $\kappa^{\text{priv}}_{\text{Alice}}$ (rossa) per decifrare, sotto "Confidentiality (+ some integrity)"; a destra $\kappa^{\text{priv}}_{\text{Bob}}$ per cifrare e $\kappa^{\text{pub}}_{\text{Bob}}$ per decifrare, sotto "Authenticity (+ some integrity)".

**Le ipotesi.** Bob deve mandare ad Alice "ci vediamo domani sera alle 8.30 al cinema tal dei tali". Ciascuno ha una coppia di chiavi. Le chiavi pubbliche si devono supporre **note a chiunque**, anche a Carl, l'attore della minaccia, l'uomo nel mezzo; le private le hanno solo i titolari. "La crittografia a chiave pubblica funziona, è bellissima, fintanto che le chiavi private rimangono private": il docente dice che lo ripeterà varie volte (*DI-02 @ 00:07:21*).

**Riservatezza** (*DI-02 @ 00:07:54*). Bob cifra con la **pubblica di Alice** e invia su un canale non sicuro. L'intercettazione in inglese è *eavesdropping*, da cui il nome **Eve/Eva** per l'attrice della minaccia che intercetta (la "donna nel mezzo"). Poiché l'unico modo di decifrare è la privata di Alice, Eva non può leggere: è un **sillogismo**, valido finché nessuno salvo Alice conosce la sua privata (*00:09:19*).

**"Un po' di integrità"** (*DI-02 @ 00:09:50*). Se Eva altera il crittogramma, secondo i libri di teoria dei numeri Alice decifrerebbe comunque qualcosa, ma di inintelligibile, perché l'algebra modulare darebbe numeri sbagliati. Nella pratica gli algoritmi hanno "fattori di controllo a doppia mandata": il software di decifratura dà un **errore** ("chiave sbagliata"), e Alice sa che il messaggio è stato alterato oppure non era cifrato per lei.

**Autenticità** (*DI-02 @ 00:11:29*). Bob cifra con la **propria privata**; Alice decifra con la **pubblica di Bob**. Il docente segnala che nella slide il crittogramma `6EB69570 08E03CE4` è identico nei due schemi, ma "chiaramente il risultato sarà diverso perché le due chiavi sono diverse": con RSA la pubblica di Alice è un numero, la privata di Bob sono due numeri, il processo è completamente diverso (*00:11:44*; lo stesso rilievo è in Teams 1, capitolo 01, sezione 12).

Qui non c'è riservatezza: chiunque intercetti decifra con la pubblica di Bob. "Qual è lo scopo di mandare un messaggio cifrato che chiunque può decifrare? Questo è il primo passaggio logico veramente importante da capire" (*DI-02 @ 00:13:11*). Lo scopo non è la riservatezza ma **accertarsi che il messaggio provenga da Bob**. Se Eva altera il messaggio (per mandare Alice altrove o impedirle di leggere l'ora), Alice decifrando con la pubblica di Bob ottiene un errore: o la chiave usata per cifrare non era la privata di Bob, quindi il messaggio non viene da Bob, o il messaggio è stato alterato in transito. In entrambi i casi il messaggio **non è autentico**: perdita di autenticità (non proviene da Bob) e, se alterato, anche di integrità (*00:15:22-00:16:31*). "Questi sono i due casi basilari della crittografia a chiave pubblica."

## 3. Laboratorio: AES e RSA con CyberChef

*DI-02 @ 00:16:31-00:31:37*

Il docente rimanda in chat il link a **CyberChef** del GCHQ (`gchq.github.io/CyberChef`) e invita a "giocarci". La volta scorsa lo ha usato per gli hash (capitolo 01, sezione 7), ora per la cifratura.

### AES-128 in modalità CBC

Ricetta **AES Encrypt** (*DI-02 @ 00:17:43-00:22:55*):
- prima prova con chiave `deadbee` (7 cifre esadecimali): CyberChef risponde "Invalid key length: 3 bytes. The following algorithms will be used based on the size of the key: 16 bytes = AES-128, 24 bytes = AES-192, 32 bytes = AES-256" (*00:18:25*); il docente corregge a voce: la chiave "deve essere 16 byte";
- chiave `deadbeefdeadbeefdeadbeefdeadbeef` (HEX, "la parola dead beef ripetuta quattro volte"), IV `00000000000000000000000000000000` (HEX; prima prova con `00000`: "Invalid IV length; got 3 bytes and expected 16 bytes", *00:19:25*), **Mode CBC**, Input Raw, Output Hex.

Il **vettore di inizializzazione** (IV) è messo a zero "per semplicità"; il docente rimanda al corso di crittografia, precisando che "in realtà è fondamentale per la sicurezza di una crittografia simmetrica" (*DI-02 @ 00:19:36*).

Input `Benvenuti al corso di Digita Identities and Trust Services!` (59 caratteri) → output (*DI-02 @ 00:21:25*):

```
ea60f3ae1386558cecf4fedd38f5185448b6896905b5a8d7ef160e42e03442ff
93d7fd9aee10bd380af0060ed6de108e14b477ed446228f699cb6cbf3f201d2c
```

**Differenza rispetto all'hash** (*DI-02 @ 00:20:14*). Con un hash, cambiare un bit in qualunque posizione cambia l'intera impronta (il *mixing* ripetuto decine di volte). Con AES-CBC, cambiando un carattere verso metà del testo il crittogramma cambia **solo da quel punto in poi**; cambiando il primo carattere (una B in 8) cambia tutto; cambiando solo l'ultimo (punto esclamativo invece di punto) cambia solo la parte finale. Motivo: ogni blocco è cifrato e poi "il blocco precedente è usato come nuovo vettore di inizializzazione per i blocchi successivi" (*00:21:16*).

Decifratura (*DI-02 @ 00:21:48-00:22:55*): nuova scheda, **AES Decrypt**, stessa chiave, stesso IV, Input Hex, Output Raw; incollando il crittogramma si riottiene `Benvenuti al corso di Digita Identities and Trust Services!` (*00:22:48*). Il docente simula le due estremità: Alice cifra, Bob decifra perché Alice gli ha comunicato "in un modo sicuro" algoritmo (AES a 128 bit), IV nullo e chiave.

Verifica per esecuzione (Python, `cryptography`, AES-128-CBC con padding PKCS#7): il crittogramma letto a schermo coincide carattere per carattere con quello calcolato. Verificato anche il comportamento descritto: con l'ultimo carattere cambiato in `.` i primi 48 byte (tre blocchi) restano `ea60…108e` identici e cambia solo l'ultimo blocco; con il primo carattere cambiato in `8`, o con `Corso` maiuscolo (posizione 14, sempre nel primo blocco), cambia tutto il crittogramma.

> **Nota aggiunta:** il "cambia da quel punto in poi" vale a granularità di **blocco** (16 byte per AES): si altera il blocco che contiene il carattere modificato e tutti i successivi, perché in CBC $C_i = E_K(P_i \oplus C_{i-1})$ con $C_0 = IV$. Un IV fisso (qui zero) rende la cifratura deterministica: stesso testo, stesso crittogramma, e prefissi uguali producono blocchi iniziali uguali; per questo nella pratica l'IV deve essere casuale e diverso per ogni messaggio. CBC inoltre non protegge l'integrità: oggi si preferiscono modalità autenticate come GCM.

### RSA-OAEP a 2048 bit

*DI-02 @ 00:22:55-00:31:04*

Dopo un falso avvio ("sto usando AES Encrypt, ecco perché non mi tornava", *00:23:48*), il docente procede:
1. **Generate RSA Key Pair**, RSA Key Length 2048, Output Format PEM (*00:25:32*). Escono due blocchi in **Base64** ("per gli informatici, rappresentazione in base 64 di una stringa binaria"): il primo è la chiave pubblica (`-----BEGIN PUBLIC KEY-----`), il secondo, "molto più grande", la privata (`-----BEGIN RSA PRIVATE KEY-----`), più grande perché "contiene molti più parametri". La coppia simula quella generata da Alice.
2. **RSA Encrypt** con la pubblica di Alice, Encryption Scheme **RSA-OAEP** (*00:26:37*). Messaggio di Bob: `Ciao Alice, ci vediamo domani alle 8.30 al Cinema Taldeitali, via Lo sai tu.` / `Non vedo l'ora,` / `Bob`. L'output è binario (a schermo caratteri non stampabili; CyberChef mostra una raffica di avvisi sul separatore di riga).
3. **RSA Decrypt** con la privata di Alice, RSA-OAEP, Message Digest Algorithm SHA-1: senza chiave l'output è "Please enter a private key." (*00:28:10*); incollata la privata, "boom, Alice decifra il messaggio" (*00:27:50*, frame *00:31:10*: input di 256 caratteri, output il messaggio di Bob).
4. Cambiando un singolo carattere del crittogramma (Eva che altera), il software **avvisa che la decifratura non è possibile** (*00:28:25*).

Verifica per esecuzione (Python): la chiave generata a schermo non è riproducibile, quindi ho rifatto l'esperimento con una coppia RSA-2048 nuova. Con RSA-OAEP/SHA-1 il messaggio (97 byte) cifrato dà un crittogramma di **256 byte** (come i 256 caratteri dell'input a schermo); la privata giusta lo decifra; un solo bit alterato nel crittogramma, o una privata diversa, producono `Decryption failed`. Due cifrature dello stesso messaggio danno crittogrammi diversi (OAEP è randomizzato).

> **Nota aggiunta:** il blocco `RSA PRIVATE KEY` (formato PKCS#1) contiene, oltre a $N$ ed $e$, l'esponente privato $d$, i primi $p$ e $q$ e tre valori ausiliari per il calcolo veloce (CRT): per questo è circa quattro volte più lungo della pubblica (nella prova: 1675 contro 426 caratteri PEM). Con OAEP/SHA-1 e chiave da 2048 bit si cifrano al massimo $256 - 2 \cdot 20 - 2 = 214$ byte: è il motivo pratico per cui RSA si usa su dati piccoli (sezioni 4 e 6).

### Perché il digitale "si ferma"

*DI-02 @ 00:28:56-00:31:04*

L'errore non è necessariamente malevolo: un canale radio o satellitare può degradarsi per rumore, banda insufficiente, interferenze. Il software digitale **non continua a processare** il dato, altrimenti restituirebbe un blocco senza senso. Analogia (di *encoding*, non di cifratura): la TV analogica decodificava sempre il segnale, anche quando non c'era, e si vedeva il "riso bianco e nero"; il digitale terrestre, quando il segnale è sotto una certa qualità, smette di decodificare: "c'è solo il canale che vedete e il canale che non vedete". Lo stesso accade cambiando un bit del crittogramma.

Chiusura: domande benvenute "relativamente a queste funzioni di CyberChef", "chiaramente questo non è un corso di CyberChef" (*DI-02 @ 00:31:04*).

## 4. Riservatezza e autenticità insieme; il costo della chiave pubblica

*DI-02 @ 00:31:37-00:37:21*

**Slide "Asymmetric for confidentiality and authenticity"** (*DI-02 @ 00:32:00*, *00:37:00*): testo nel capitolo 01, sezione 12. In DI-02 il titolo porta anche la notazione delle coppie $(\kappa_{\text{Bob}}, \kappa_{\text{Alice}})$.

Si possono usare le due modalità insieme: cifrare prima con la privata del mittente e poi con la pubblica del destinatario, o viceversa; il docente non entra in quale ordine sia "più sicuro, più efficace, più performante". A destinazione si decifra due volte, nell'ordine giusto, e si ottiene un messaggio **riservato e autentico** (*DI-02 @ 00:32:10*).

> **Nota aggiunta:** come già osservato nel capitolo 01, sezione 12, lo schema della slide ("Combine keys" → segreto condiviso) è un accordo di chiave alla Diffie-Hellman, mentre il commento a voce descrive la doppia cifratura.

**Il problema della performance** (*DI-02 @ 00:32:49*). La chiave pubblica sembrerebbe superare la simmetrica (che offre solo riservatezza), ma a **parità di robustezza crittografica** la simmetrica è sempre computazionalmente più semplice, anche per chi si difende. Se si vuole che l'avversario abbia bisogno, per esempio, di "47 anni" di calcolo, l'algoritmo a chiave pubblica di robustezza corrispondente costa molto di più anche a chi cifra. Per questo, per la riservatezza, si preferisce dove possibile la simmetrica.

Esempio "vuoto per pieno" (*DI-02 @ 00:35:11*): se AES-256 impiega 10 secondi su certi dati, cifrare gli stessi dati con robustezza equivalente con "RSA 2048, che più o meno corrisponde ad AES-256", probabilmente "non mi basterebbero settimane di calcoli". Per questo è impensabile cifrare grandi dati a chiave pubblica su dispositivi poco potenti (smartphone economici, smart card, i vecchi token RSA per l'e-banking). La chiave pubblica, per la riservatezza, cifra **piccoli dati**, da pochi byte a poche centinaia di byte al massimo: tipicamente **chiavi simmetriche** (*00:36:21-00:36:53*).

> **Correzione:** RSA-2048 non equivale ad AES-256: secondo NIST SP 800-57 parte 1 offre circa 112 bit di sicurezza (AES-128 ≈ RSA-3072, AES-256 ≈ RSA-15360). Stesso errore di Teams 1 @ 0:13:14, già corretto nel capitolo 01, sezione 12. Le "settimane di calcoli" sono un'iperbole didattica: nella pratica RSA non si usa affatto per cifrare grandi dati (vedi il limite di 214 byte della sezione 3), proprio per i motivi che il docente spiega.

## 5. Svantaggi della crittografia simmetrica

*DI-02 @ 00:37:21-00:44:34*

**Slide "Disadvantages of symmetric cryptography"** (*DI-02 @ 00:37:19-00:44:19*): testo nel capitolo 01, sezione 12 (formula $N(N-1)/2$, ~5000 chiavi per 100 utenti, ~0,5M per 1000; documenti da ricifrare per ogni coppia mittente-destinatario).

Commento a voce:
- **Contesto data science** (*DI-02 @ 00:37:30*): non comunicano solo persone, ma dispositivi (telecamere, sensori di temperatura, pressione, luce) che inviano in tempo reale a una centrale che fa previsioni meteo da milioni di sensori; o un'azienda in cui tutti devono poter scambiare dati con tutti.
- **Lo scambio della chiave** (*00:38:33*): la simmetrica è segreta ma **condivisa**, quindi Alice e Bob devono aver trovato un canale sicuro per scambiarla, diverso da quello del messaggio cifrato. "Ancora nel 2025" si vedono file cifrati inviati per email con la password nel testo, o in una seconda email (chi accede alla casella legge entrambe), o via SMS ("gli SMS si possono leggere in chiaro"). In azienda si può ridurre il problema distribuendo la chiave nel badge all'assunzione; con persone di organizzazioni diverse nel mondo diventa complesso.
- **La combinatoria** (*00:40:51*): il rosso scambia dati con giallo e verde, altri con blu, viola e celeste, altri uno a uno: serve una chiave per ogni coppia. Il docente dice "n quadro" e poi precisa "n per n meno uno mezzi". Per 1000 utenti mezzo milione di chiavi, "diverse centinaia di megabyte solo di chiavi", figurarsi su uno smartphone: "abbiamo trasformato un problema di riservatezza in un problema di gestione molto più complesso" (*00:41:54-00:42:25*).
- **Ricifratura**: lo stesso dato per giallo, celeste e viola va cifrato tre volte con tre chiavi diverse; il vantaggio di velocità della simmetrica si perde (*00:42:56*).
- **La soluzione a chiave pubblica** (*00:43:27*): ognuno ha la propria coppia, tiene la privata e dà a tutti la pubblica; invece di un numero di chiavi che va col quadrato, ciascuno memorizza $n + 1$ chiavi (le $n$ pubbliche, compresa la propria, più la propria privata).

Verifica per esecuzione: $N(N-1)/2$ = 15 per i 6 computer della figura, 4950 per 100, 499500 per 1000.

> **Nota aggiunta:** le "diverse centinaia di megabyte" per mezzo milione di chiavi sono una sovrastima se si conta il solo materiale crittografico: $499500 \times 32$ byte (AES-256) ≈ 16 MB, e ogni utente ne custodisce comunque solo $N-1 = 999$. Il punto del docente (la gestione cresce col quadrato) resta valido.

## 6. Key wrapping

*DI-02 @ 00:44:34-00:50:23*

**Slide "Asymmetric key wrapping"** (*DI-02 @ 00:45:46-00:49:59*, costruita per passi): testo e schema nel capitolo 01, sezione 12. Il docente la chiama **key wrapping**, "avvolgimento della chiave" (la trascrizione automatica rende "key-dropping", "key mapping").

Il procedimento a voce (*DI-02 @ 00:44:34-00:49:20*), con l'esempio del **cinema** (anticipato, verrà ripreso più avanti nel corso): ogni volta che ci si siede in una sala cinematografica avviene esattamente questo; il file del film è di gigabyte se non terabyte, impossibile da cifrare a chiave pubblica in tempi ragionevoli.
1. Alice conosce la **pubblica del destinatario** Bob.
2. Genera dal nulla una **chiave simmetrica** $\kappa^{\text{sym}}$ (come la `deadbeef…` del laboratorio, ma con un algoritmo **pseudo-casuale**: ripetendo si ottiene sempre una chiave diversa).
3. Cifra il contenuto con l'algoritmo simmetrico: poco tempo e poche risorse.
4. Cifra con la pubblica di Bob **solo la chiave simmetrica**.
5. **Butta** la chiave simmetrica in chiaro, la cancella dalla memoria.
6. Invia il contenuto cifrato (grande, ma cifrato a basso costo) e il contenitore con la chiave cifrata (piccolo: "qualche centinaio di bit" per le curve ellittiche, qualche migliaio per RSA, alcuni algoritmi post-quantum "qualche decina di migliaia di bit"), di solito uniti in una **busta crittografica**: un unico file gigante, in gran parte contenuto cifrato, con il contenitore della chiave in testa o in coda.
7. Bob decifra con la propria privata la chiave simmetrica, poi con essa tutto il film.

La chiave simmetrica è stata generata una sola volta per quel solo contenuto e poi buttata: l'unico a poterla estrarre è Bob. È "il meglio dei due mondi": velocità della simmetrica, facilità di distribuzione e gestione delle chiavi della pubblica (*DI-02 @ 00:49:20*).

"Capire questo meccanismo significa capire gran parte della crittografia. Il prossimo scalino lo vedremo con la firma digitale, e poi i passaggi logicamente complessi finiscono qui in tutto il corso" (*DI-02 @ 00:49:52*).

> **Nota aggiunta:** le dimensioni citate a voce sono quelle dell'oggetto a chiave pubblica, non della chiave simmetrica avvolta (128-256 bit). Per esempio un crittogramma RSA-2048 è di 2048 bit qualunque sia la chiave AES dentro; con ML-KEM-768 (FIPS 203) il crittogramma è di 1088 byte (8704 bit). Nella terminologia moderna lo schema è un **KEM/DEM** (*key/data encapsulation mechanism*); in Teams 1 il docente usa infatti "key encapsulation" (capitolo 01, sezione 12).

## 7. I tre stati della cifratura

*DI-02 @ 00:50:23-00:53:41*

**Slide "The 3 states of data encryption"** (*DI-02 @ 00:49:51*, *00:53:12*). Tre cerchi: **AT REST** (cartella), **IN TRANSIT** (frecce), **IN USE** (persona alla scrivania). Riquadro "encryption *at rest*": lucchetto con chiave su cartella, PC, smartphone, server, database. Riquadro "encryption *in transit*": 1 "encrypt at the source…", 2 "…transmit encrypted…", 3 "…decrypt at the destination". Fonte: "Safesforce website" (sic).

**In transito** (*DI-02 @ 00:50:23*). Tutto ciò che si è visto finora (simmetrica, chiave pubblica, key wrapping) è cifratura in transito, in tre passi: il mittente cifra; trasferisce il dato cifrato e, se serve, la chiave (in modo che dipende dallo schema: simmetrico, a chiave pubblica o "ibrido" come il key wrapping); il destinatario decifra. Mittente e destinatario **mantengono una copia in chiaro**: la cifratura serve solo ad attraversare un canale tendenzialmente non sicuro, perché chi intercetta (Eva) non possa conoscere o alterare il messaggio.

**A riposo** (*DI-02 @ 00:51:58*). Si è "destinatari di se stessi": si cifra per conservare il dato cifrato su un server, uno storage, un repository pubblico, tenendo la chiave. Chi accede allo storage trova un dato cifrato e, senza la chiave di decifratura (la stessa se simmetrica, l'altra della coppia se a chiave pubblica: "in questo stato è irrilevante"), non può leggerlo. Esempio: l'attacco **Evil Maid** (la "cameriera cattiva" che accede al laptop e estrae il contenuto del disco): se il disco è cifrato e lei non ha la password, non è matematicamente impossibile, ma dovrà fare una crittoanalisi.

**In uso** (*DI-02 @ 00:53:41*): il terzo stato, sezione 8.

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 7 (stati della cifratura)*

- Il docente sottolinea che questa parte è "molto importante per chi è un data scientist: capire come la crittografia si applica rispetto ai dati". (Teams 1 @ 0:30:22)
- **Il key wrapping vale in entrambi gli stati**: la busta crittografica è stata descritta come un file, ma può essere anche un **pacchetto di rete**; quindi la key encapsulation è un metodo sia di cifratura in transito sia a riposo. (Teams 1 @ 0:31:38-0:32:03)
- Cifratura a riposo, definizione 2026: cifrare il dato scrivendolo tipicamente come file cifrato, **eliminare la copia in chiaro**, lasciare nel file system, nel database, nell'object storage o su una pagina pubblicata solo la copia cifrata; anche se esfiltrato, l'attore della minaccia dovrebbe poi decifrarlo. (Teams 1 @ 0:32:03-0:32:55)
- **Stati in serie**: un file cifrato a riposo può essere ulteriormente cifrato in transito; il ricevente toglie la cifratura in transito, ma resta un file cifrato a riposo da decifrare prima dell'uso. (Teams 1 @ 0:32:58-0:33:24)

## 8. Cifratura in uso: la cifratura omomorfa

*DI-02 @ 00:53:41-01:02:28*

La **cifratura in uso** ha come esempio più semplice la famiglia degli algoritmi **omomorfi**, dal gergo algebrico; si basa su algoritmi completamente diversi, "di cui non parleremo in questo corso, o meglio, di cui parleremo se c'è tempo alla fine, perché devo arrivare prima a parlare di identità digitali" (*DI-02 @ 00:53:41-00:54:16*).

**Il problema** (*DI-02 @ 00:54:16-00:57:33*), "e qui veniamo proprio all'utilizzo nell'ambito dei dati". Si vuole usare un sistema cloud per l'analisi dei dati, ma i dati sono riservati, coperti da brevetto, proprietà intellettuale, NDA ("nominate voi il presidio di sicurezza amministrativa", con rimando al corso di Cybersecurity) che impedisce di memorizzarli in chiaro su un cloud magari di un'altra nazionalità, o di cui non si controllano le policy di memorizzazione, riservatezza o privacy. Esempi: cartelle cliniche dei pazienti di un grande studio clinico internazionale (dati personali e sensibili, anche se negli studi clinici i nomi vengono comunque rimossi), un brevetto, un algoritmo segreto, "la ricetta della Coca-Cola" su cui calcolare la stabilità di una molecola al variare di temperatura e pressione o la conservazione di un farmaco. Se si memorizzano i dati cifrati a riposo, il cloud non può calcolarci sopra; dare la chiave al gestore "è come se avessi caricato i dati in chiaro", e se la compliance vietava il chiaro vieta anche di dare la chiave. Restano due alternative cattive: riscaricare e calcolare offline (allora tanto valeva non usare il cloud) o non poterlo fare affatto perché il laptop non ha la capacità di calcolo.

**La soluzione** (*DI-02 @ 00:58:08*). Terminologia: nei convegni si sente "cifratura omomorfica", ma la traduzione corretta è **omomorfa**, perché lavora per omomorfismi. Il dato è cifrato "come" con una chiave simmetrica o pubblica, ma sul dato cifrato esiste un insieme di operazioni matematiche (gli omomorfismi) eseguibili **"alla cieca"** senza che chi calcola possa decifrare. Per la statistica è perfetto: "quasi sempre si riduce all'algebra lineare", medie, somme, varianze, polinomi quadratici; raramente funzioni non lineari (*00:59:17*). Somme, moltiplicazioni, divisioni, elevazioni al quadrato sono, con certi algoritmi omomorfi, eseguibili sul cifrato; il risultato resta cifrato e solo chi ha la chiave lo decifra.

In termini algebrici (*DI-02 @ 01:00:49*): gli operatori di calcolo "commutano" con gli operatori di cifratura ("per chi conosce la meccanica quantistica"); cifratura, poi calcoli sul cifrato, poi decifratura dà lo stesso risultato del calcolo sul chiaro. "Il servizio terzo non vede gli addendi, li somma e non vede la somma." È il **terzo stato** della crittografia.

**Slide "Homomorphic encryption"** (*DI-02 @ 01:01:48*). Schema: *User* con chiave $\kappa^{\text{pub}}_{\text{Hom}}$ → *Encrypted Query* → *Database* (cloud); riquadro "Search the Database in Encrypted State, \*does not require user key to answer the query", "encryption *in use*"; *Encrypted Search Result* → *Decryption* con $\kappa^{\text{priv}}_{\text{Hom}}$ → *Search Result* all'utente. Testo: "Homomorphic encryption allows data processing to be performed *directly on* encrypted data, without need for processors (e.g. remote third-party cloud services) to access any plaintexts."

Verifica per esecuzione (Python, aggiunta mia): con lo schema di **Paillier** (libreria `phe`, chiave da 2048 bit) ho cifrato quattro valori (37,5; 41,2; 39,8; 36,9), sommato i crittogrammi e moltiplicato per $1/4$ senza mai decifrare: decifrando si ottengono somma 155,4 e media 38,85, uguali al calcolo in chiaro. Con RSA "da manuale" (senza padding) $\text{Dec}(\text{Enc}(12) \cdot \text{Enc}(7) \bmod N) = 84$: RSA è omomorfo rispetto al prodotto.

> **Nota aggiunta:** esistono schemi **parzialmente** omomorfi (Paillier: solo somme e prodotti per costanti in chiaro; RSA ed ElGamal: solo prodotti) e **completamente** omomorfi (FHE, dal lavoro di Gentry del 2009: somme e prodotti arbitrari, quindi qualunque circuito, a costi computazionali ancora molto alti; CKKS è lo schema usato per l'aritmetica approssimata, statistica e machine learning). Le funzioni non lineari si ottengono approssimandole con polinomi. Lo schema della slide usa una coppia di chiavi, coerente con il commento del 2026; esistono anche varianti simmetriche.

Chiusura: "oggi finiremo alle 8, sempre per recuperare sia la lezione fatta, sia parte di quella lezione che non è stata registrata ieri, sia per la lezione in meno che faremo" (*DI-02 @ 01:02:28*; vedi Punti incerti).

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 8 (cifratura in uso e omomorfa)*

- Nel 2026 la cifratura in uso è presentata "a scopo di cultura generale", come "uno dei campi di ricerca crittografici più fertili oggigiorno", che però "esulerebbe da molte trattazioni che dobbiamo fare". La cifratura omomorfa è **uno** degli esempi, "non l'unico". (Teams 1 @ 0:33:30-0:34:05)
- Descrizione 2026: coppia di chiavi asimmetriche con algoritmo omomorfo; dato memorizzato in un database o storage cloud non più sotto il proprio stretto controllo, che magari non soddisfa i requisiti di cybersicurezza, cyber resilienza e soprattutto privacy (rimando alla triade "dell'altro corso"). (Teams 1 @ 0:34:05-0:34:53)
- Argomento nuovo nel 2026: oggi non si possono lavorare grandi quantità di dati senza grandi infrastrutture, che si affittano in cloud (macchine virtuali con decine o centinaia di CPU/GPU in parallelo; con l'intelligenza artificiale i servizi cloud sono "gli unici ad avere quelle capacità di calcolo"). Senza cifratura in uso si sarebbe costretti a fare tutto in casa, spesso impossibile per motivi economici (spesa operativa o in conto capitale). (Teams 1 @ 0:35:02-0:36:58)
- Formulazione 2026 dell'omomorfismo: con ogni algoritmo omomorfo "viene gratis" un insieme di operazioni; la somma o il prodotto dei dati cifrati, una volta decifrati, equivale alla somma o al prodotto dei dati in chiaro ("legge di invarianza"); il risultato si decifra con la stessa privata del dato originale. (Teams 1 @ 0:37:09-0:38:13)
- Il docente aggiunge che le operazioni statistiche, "anche le più complicate e non lineari", alla fine si svolgono con operazioni di algebra lineare sul dato cifrato. (Teams 1 @ 0:38:26-0:38:41) Vedi la nota sopra: le non linearità si approssimano.
- Ogni algoritmo omomorfo ammette solo certe operazioni: per questo esistono molte tipologie di cifratura omomorfa e, più in generale, molti algoritmi di cifratura in uso che rispondono a domande diverse. (Teams 1 @ 0:39:04-0:39:36)

## 9. Firma digitale

*DI-02 @ 01:02:28-01:19:19*

**Perché serve** (*DI-02 @ 01:02:28*). Finora: crittografia per l'integrità (hash) e per la riservatezza; la chiave pubblica può dare anche autenticità, ma "da sola è poco pratica": bisognerebbe cifrare l'intero messaggio (magari diversi megabyte, computazionalmente proibitivo) e decifrarlo ogni volta che si accede al dato, anche senza voler verificarne l'autenticità. Da qui un altro uso della chiave pubblica: la **firma digitale** (*digital signing*).

**Slide "Authenticity – Digital Signing"** (*DI-02 @ 01:04:10*, costruita per passi fino a *01:16:10*). Testo:
- "To **sign**, Alice processes original data with her own private key, $\kappa^{\text{priv}}_{\text{Alice}}$, to obtain a digital signature $S$. Data and signature may be either **detached** *from* or **enveloped** *one into* another."
- "To **validate** the signature $S$, Bob processes *both* the original data *and* the signature with Alice's public key, $\kappa^{\text{pub}}_{\text{Alice}}$, and gets a Boolean response (TRUE/FALSE)."

Legenda: *digital signature* (blocco `1110100101`), *original data (unsigned)*, *signed data (envelope)*. Schema: *Signer* con la privata produce $S$; dati e firma passano per *Network*, separati o in busta; il *Verifier* con la pubblica di Alice ottiene TRUE o FALSE.

**La firma** (*DI-02 @ 01:04:02-01:06:49*). Alice deve firmare un documento (un contratto, o un messaggio per Bob) e vuole che Bob sia certo che viene da lei: l'autenticità è la capacità di garantire l'**origine del dato**. Alice **non cifra il messaggio** (impiegherebbe troppo): sceglie un algoritmo di hash, calcola il **digest** e cifra con la propria privata **solo il digest**, un dato piccolo (256 bit con SHA-256, 512 con SHA-512). Definizione:

> La **firma digitale** di un messaggio è l'impronta crittografica di quel messaggio cifrata con la chiave privata del titolare (*DI-02 @ 01:05:42*).

È una manciata di bit, "della stessa dimensione di un'impronta crittografica, poco più grande", relativamente semplice da generare.

**Il trasporto** (*DI-02 @ 01:06:49-01:11:32*). Il messaggio viaggia **in chiaro**: non interessa la riservatezza. Un contratto pubblico non deve essere riservato, deve dimostrare chi l'ha firmato; "come dice il diritto italiano ma anche di molti paesi", la firma deve esprimere la **volontà del firmatario** di sottoscrivere, una prova giuridico-legale. Restando sui dati: Bob deve essere certo che il messaggio viene da Alice e non è stato alterato, né per caso (canale rumoroso) né da qualcuno che gli tende un tranello ("ci vediamo alle 6 del mattino tra 18 giorni in questo covo segreto di spie"). Carl, l'uomo nel mezzo ("stavolta voglio essere gender neutral"), può intercettare, cambiare e inoltrare sia messaggio sia firma. Messaggio e firma $S$:
- possono viaggiare insieme in una **busta crittografica** (un file che contiene il messaggio in chiaro e la sua firma): è "la modalità preferita in quasi tutti i contesti";
- oppure separati: Bob potrebbe già avere il documento (il contratto che l'operatore telefonico ha mandato da firmare) e Alice gli rimanda **solo la firma**.

**La convalida** (*DI-02 @ 01:11:32-01:15:34*). Alice e Bob hanno concordato prima, anche in chiaro, l'**algoritmo di firma**, cioè la combinazione di un algoritmo di hash e di un algoritmo a chiave pubblica; quest'ultimo è dettato dal tipo di chiave ("se ti do una chiave a curva ellittica secp256k1, quello è l'algoritmo"). Bob:
1. calcola **indipendentemente** l'hash del documento con l'algoritmo concordato;
2. decifra $S$ con la **pubblica di Alice**: solo quella funziona, "se uso una qualunque altra chiave pubblica mi dà errore", come visto in CyberChef; ottiene l'hash calcolato da Alice;
3. confronta: se i due hash sono **identici bit a bit**, Bob è ragionevolmente certo che la firma è di Alice (solo lei ha la privata) e che riguarda **proprio quel messaggio** (un messaggio diverso avrebbe dato un hash diverso, quindi una firma diversa).

"Questo è il concetto logico più difficile da capire dell'intero corso. Capito questo processo abbiamo tutte le basi per capire che cos'è il digital trust e da lì che cos'è l'identità digitale" (*DI-02 @ 01:15:34-01:16:07*).

**Slide "Digital signatures"** (*DI-02 @ 01:16:16*, *01:19:16*). Intestazione "FIPS 186-5: *Digital Signature Standard*", `https://csrc.nist.gov/pubs/fips/186-5/final`. A sinistra: Alice, "Hello Bob!" → *Sign* con *Alice's private key* (rossa) → "Hello Bob!" con firma `BE459576 785039E8`; Bob → *Verify* con *Alice's public key* (verde) → "Hello Bob!". A destra:

> **Digital signing** is a **technical** procedure, whereby an entity (legal/natural person; a hardware/software system or service, a website, …), called **digital signer**, has a *signing key-pair* $(\kappa^{\text{pub}}, \kappa^{\text{priv}})$ with which it shall:
> 1. *hash* the plaintext (pre-agreed hash function);
> 2. *encrypt* the above digest via its *private* key $\kappa^{\text{priv}}$, which is allegedly only known to, and usable by, the signer.
>
> A **digital signature** is the **message's encrypted digest**.
>
> To **digitally trust** the message, any third parties shall:
> 1. *decrypt* the digital signature via the ***alleged*** signer's public key $\kappa^{\text{pub}}$, thus getting another digest $h_1$;
> 2. *re-hash* the original unsigned message to get a digest $h_2$;
> 3. *compare* the two digests $h_1$ (from 1.) and $h_2$ (2.).
>
> If $h_1 \neq h_2$ *either* message *and* digital signature have been modified (or a hash collision has occurred) **!!**

Commento (*DI-02 @ 01:16:07-01:19:31*): lo standard NIST "è stato rivisto di recente". Nel corso "firma digitale" indica **solo** il processo tecnico di cifrare un'impronta con una chiave privata, il cui titolare è il firmatario; per fidarsi si decifra con la pubblica dell'**asserito** titolare. Se Carl cambia anche un solo bit del messaggio o della firma, Bob vede che qualcosa è stato alterato, ma **non sa cosa** né chi ha firmato, "e non è importante": la convalida dà una **risposta oracolare**, vero o falso, e Bob è "un semplice giudice": la prova è buona, la accetta; non è buona, la scarta. Il firmatario può essere una persona fisica ("Alice, … via … 12", [?]) o un sistema: `alice.edu.nz`, un'università neozelandese che firma i messaggi agli studenti, o che invia al computer del ministero dell'istruzione gli esiti degli esami, che deve fidarsi che i voti non siano stati alterati da un hacker.

> **Correzione:** l'ultima riga della slide è imprecisa in due punti. (1) Se $h_1 \neq h_2$ è stato modificato il messaggio **o** la firma (o entrambi), oppure si è usata la pubblica sbagliata: il docente stesso lo dice a voce ("o la chiave o il messaggio", *01:17:50*). (2) Una **collisione** non spiega $h_1 \neq h_2$: spiega il caso opposto, un falso positivo, cioè $h_1 = h_2$ con un documento diverso da quello firmato. Il docente lo dice correttamente a *01:15:34* ("a meno di collisioni").

Verifica per esecuzione (Python, RSA-2048 con SHA-256 e padding PKCS#1 v1.5, chiave generata per la prova): la firma di `Hello Bob!` è lunga 256 byte; "decifrandola" con la pubblica ($s^e \bmod N$) si ottiene un blocco che termina con lo SHA-256 di `Hello Bob!` preceduto dall'identificativo dell'algoritmo (`3031300d060960864801650304020105000420`): $h_1 = h_2$. La verifica dà TRUE su `Hello Bob!` e FALSE su `Hello Bob?`. Il valore `BE459576 785039E8` della slide è illustrativo.

> **Nota aggiunta:** "cifrare il digest con la privata" è la descrizione esatta per **RSA** (PKCS#1 v1.5, dove il digest è imbustato con l'identificativo dell'algoritmo, come nella verifica sopra). Per ECDSA ed EdDSA (inclusa secp256k1, citata dal docente) non c'è alcuna "cifratura": la firma è una coppia di numeri $(r, s)$ calcolata da digest, privata e un nonce, e la verifica è un'equazione sulla curva che restituisce vero o falso, senza "estrarre" $h_1$. Il modello "hash, poi cifra con la privata" resta il modo giusto per ragionare sul *chi* e sul *cosa*, ed è quello che il docente userà in tutto il corso. FIPS 186-5 è stato pubblicato il 3 febbraio 2023 (verificato: annuncio NIST e Federal Register del 03/02/2023) e ha aggiunto EdDSA e tolto DSA per le nuove firme.

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 9 (firma digitale)*

- **Alice è un soggetto virtuale**: nella letteratura crittografica può essere una persona fisica, una persona giuridica o un sistema informatico; "a questo livello di discussione non ci interessa sapere cos'è o chi è". Deve dimostrare a terzi che dati prodotti da lei, o dei quali è *accountable*, sono autentici, per esempio un contratto firmato da qualcuno che lavora per "la Alice SRL". (Teams 1 @ 0:39:51-0:41:12)
- **Legame con il digital trust**: nel cyberspazio i soggetti probabilmente non si sono mai incontrati, o se si sono incontrati non sono sicuri di interagire davvero fra loro; la capacità di realizzare l'autenticità "è alla base del digital trust". (Teams 1 @ 0:41:12-0:41:49)
- **Dimensione della firma**, dato nuovo del 2026: che si usi RSA 2048, 4096, 8192 o una curva ellittica da 521 bit, la firma è lunga "poche decine, al massimo poche centinaia di byte", a prescindere dalla lunghezza del messaggio, salvo alcuni algoritmi *quantum safe* che generano firme "piuttosto lunghe". (Teams 1 @ 0:44:17-0:44:45) Verifica per esecuzione: RSA-2048 dà firme di 256 byte (RSA-8192: 1024 byte); ECDSA su P-521 con SHA-512 dà 139 byte in codifica DER.
- **Metadati della firma**: la prima cosa che Bob fa è leggere nei metadati quale algoritmo di firma è stato usato, per esempio "RSA 256 con chiave lunga 2048" [?: verosimilmente RSA con SHA-256]. (Teams 1 @ 0:45:39-0:46:10)
- **Esiti della verifica, caso per caso**: se è alterata la firma, il software probabilmente va in errore già alla decifratura; altrimenti l'hash estratto non corrisponde. Se è alterato il documento, Bob recupera sì l'impronta originale, ma quella ricalcolata è diversa. Negativo anche se Bob usa la pubblica sbagliata. In ogni caso "quella non è la firma di Alice, oppure Alice non ha firmato quel documento". (Teams 1 @ 0:48:49-0:51:34)
- **Doppia garanzia**: con la firma si ottiene autenticità e "in maniera molto più robusta" anche integrità; documento e firma possono restare per anni in uno storage non fidato. (Teams 1 @ 0:47:51-0:48:16)
- **Algoritmo e schema**: un algoritmo di firma è "in soldoni" la coppia hash + cifratura a chiave pubblica, ma conta l'intero ciclo di vita del documento firmato e delle chiavi; FIPS 186-5, "il documento più importante sulle firme digitali a livello internazionale, anche se di fatto è uno standard americano", descrive anche la gestione delle chiavi, cioè uno schema crittografico ad alto livello. (Teams 1 @ 0:51:38-0:52:33)
- "Il 90% del digital trust si comprende se si comprende a cosa serve la firma digitale e come funziona." (Teams 1 @ 0:52:46)
- Nel 2026 il docente presenta la firma come "il concetto forse più difficile di tutto il corso". (Teams 1 @ 0:39:39)

## 10. Firma digitale e firma autografa

*DI-02 @ 01:19:19-01:28:56*

**Slide "Digital *vs* handwritten signatures"** (*DI-02 @ 01:19:19*, *01:28:23*). A sinistra lo schema documento → # → `1110100101` → chiave rossa → `1110100101`; a destra due firme autografe (la seconda "Mario Rossi"). Testo:

| Digital signature | Handwritten signature |
|---|---|
| *It cryptographically links a key-pair to a document.* | *It is about inking a glyph on a piece of paper.* |
| It is a unique binary payload to each and every signed document. | The same signer is supposed to replicate it as close as possible on every document he/she undersigns. |
| It covers the whole document: it changes whenever any bit of the document is changed/tampered with. | Technically it only "covers" the parts of the document the ink was laid on: other contract parts may change. |
| It cannot be associated to a different document\*, i.e. it cannot be forged by almost any means\* but using the signer's own private key. | It may be copied (e.g. forged or printed) by a forger, thus pretending that a different document/contract had been signed. |
| As any digital data, it may be cloned indefinitely. | Its quality degrades at each successive analogic copy. |
| A predefined technical process is set to validate it (to be described later along with *digital trust* elements). | In doubt, a graphologist may be consulted by justice, evidence usually leading to an inconsistent outcome. |

Riga centrale: "The signer may still be tricked, or coerced, into signing an incorrect document!". In basso a sinistra: "Subject to **private key** / hash-**collision** (\*) **attacks**."; a destra: "The signing process may be recorded and replayed." Chiusura: "The real strength of digital signatures is, thus, within the effectively adopted **signature scheme**."

Commento (*DI-02 @ 01:20:00-01:28:56*):
- La firma digitale lega "in maniera biunivoca" una coppia di chiavi a **quel** messaggio: cambiando un bit della chiave o del messaggio si altera tutta la firma, quindi è facile verificare sia un'alterazione sia una chiave diversa da quella del firmatario.
- La firma su carta copre solo il pezzo di foglio con l'inchiostro. Esempio: "ti do un milione di euro, firmato Walter Arrighetti", qualcuno aggiunge due zeri con abilità e il lettore crede che l'importo sia cento volte maggiore. Per questo i contratti si fanno in **doppia copia**, si **siglano** o firmano tutte le pagine, in alcuni processi si firma su **filigrana**: processi aggiuntivi (*01:21:13-01:22:32*).
- Nessun essere umano fa due firme uguali, mentre la firma digitale con la stessa chiave sullo stesso dato è **sempre identica bit a bit** (*01:22:56*).
- L'autografa si può ritagliare e copiare. Il docente racconta di documenti "con firma digitale" che erano file Word con lo **scan** o la foto della firma a penna incollata come immagine ("si vedeva pure il bordo giallognolo"): chiunque la può estrarre e incollare altrove; "ovviamente non è una firma autografa, è una firma elettronica, più avanti" (*01:23:03-01:24:05*). La firma digitale invece è **unica per messaggio**.
- Finché non si sa risalire alla privata o trovare una **collisione** (un altro documento con la stessa impronta, per sostenere che Alice ha firmato quello), il legame firmatario-documento è molto più forte; con hash robusti la collisione "non è praticamente possibile" (*01:24:35-01:25:42*).
- La firma digitale è **opponibile**, in alcuni casi con **pieno valore legale** (si vedrà parlando di digital trust). Sembrerebbe sempre migliore dell'autografa, con due sole debolezze (*01:25:42-01:28:56*):
  1. una **nuova**, che l'autografa non ha: l'**attacco crittografico**, cioè risalire alla privata e firmare qualunque cosa al posto del titolare, oppure un **attacco a collisione di hash**;
  2. la **stessa del mondo fisico**: ingannare, ricattare o forzare il firmatario. Pistola alla tempia ("metti il PIN e firma"), foglio scambiato mentre il firmatario si gira, **carta carbone** con sotto un altro contratto. Due categorie: **inganno** (il firmatario non si accorge) e **coercizione** (ricatto, corruzione, tortura: sa ma non ha scelta).
  - "Poi c'è una terza tipologia, va bene, questa per il momento la saltiamo" (*01:28:24*): verosimilmente il "recorded and replayed" della slide, non commentato.

> **Nota aggiunta:** "sempre identica bit a bit" vale per gli schemi **deterministici**: RSA PKCS#1 v1.5 (verificato: due firme dello stesso messaggio con la stessa chiave coincidono), EdDSA, ECDSA deterministico (RFC 6979). Con RSA-PSS ed ECDSA randomizzato due firme dello stesso documento sono diverse (verificato per ECDSA P-521: due firme diverse, entrambe valide). Ciò che resta vero in ogni caso è il punto del docente: una firma valida per un documento non è valida per nessun altro.

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 10 (firma digitale e autografa)*

- Il processo si chiama firma digitale perché ha "moltissime similitudini con la firma analogica", ma è più robusto. (Teams 1 @ 0:54:14-0:54:32)
- **Il punto principale nel 2026**: l'autografo **non dipende dal documento**; anche se il firmatario lo replicasse perfettamente, sarebbe lo stesso su dieci documenti diversi, e questo rende efficaci gli attacchi di copiatura. Il docente aggiunge che nessun firmatario ripete mai lo stesso autografo e che l'autografo si può falsificare, "come qualunque perito in tribunale direbbe". Le firme scansionate incollate in calce ai Word: "l'ho visto fare tante volte a delle segretarie per i loro capi". (Teams 1 @ 0:54:36-0:56:44)
- **Collisioni**: solo due documenti che collidono produrrebbero la stessa firma; anche in quel caso, "in pratica impossibile", la firma sarebbe comunque fatta con la propria privata. (Teams 1 @ 0:57:00-0:58:03)
- **Le due ipotesi** da cui dipende la superiorità della firma digitale: (1) l'algoritmo di firma è robusto (sia l'hash sia la cifratura a chiave pubblica); (2) la privata è sotto il **controllo esclusivo** del firmatario, il **sole control** visto nel corso di Cybersecurity (per le chiavi simmetriche: controllo esclusivo dei soli mittente e destinatario). Come verificare queste ipotesi nel concreto si vedrà più avanti. (Teams 1 @ 0:58:22-0:59:57)
- **Esempio di inganno digitale**: un'applicazione di firma opaca mostra l'immagine JPEG di un contratto con il proprio IBAN, ma calcola l'impronta di un altro contratto con l'IBAN dell'hacker; è l'equivalente della carta carbone. La coercizione "funziona sia che in mano io abbia la penna, sia la tastiera". (Teams 1 @ 1:00:14-1:01:21)
- **Schema di firma digitale sicuro**: robustezza dell'algoritmo e controllo esclusivo della privata si realizzano progettando uno schema, che descrive non solo gli algoritmi ma le procedure che garantiscono che la privata sia solo nella disponibilità del firmatario e che della pubblica si possa accertare la **titolarità**. "La robustezza dello schema di firma è un criterio molto più ampio della robustezza del solo algoritmo." (Teams 1 @ 1:01:25-1:02:13) È la riga finale della slide.

## 11. Firme sui PDF: PAdES e signature wrapping attack

*DI-02 @ 01:28:56-01:35:16*

Il laboratorio sulle firme PDF è rinviato: prima bisogna parlare di **Certification Authority**, "forse già nella prossima lezione, se non nella prossima, in quella dopo" (*DI-02 @ 01:31:48*).

**PAdES** (*DI-02 @ 01:28:56*). Le firme sui PDF fatte con certi requisiti di sicurezza imposti in Europa costituiscono uno standard chiamato **PAdES** e danno una sicurezza molto elevata. Firmando un PDF si può (opzionale, ma si fa di solito) aggiungere un **elemento visivo** nel punto previsto dal contratto, "firmato da Walter Arrighetti": utile nella gestione documentale e bello da vedere, ma **non è la prova crittografica**. Il PDF fa da **busta crittografica di se stesso**: dentro c'è la firma vera e propria. In un visore tecnico della struttura interna si vede un campo `/Sig` (tutti i campi tecnici PDF iniziano con `/`), con metadati come nome del firmatario, luogo, data, e soprattutto `/Contents`, il valore della firma digitale. Acrobat mostra la firma in una finestra di proprietà; esistono anche software integrati per Mac, Linux e Windows. PAdES consente **più firmatari** e mostra la versione del documento **come l'ha vista ciascuno**, perché il PDF è nato per simulare fedelmente i processi cartacei (*01:30:42-01:32:20*).

**Slide "PAdES – PDF advanced digital signature"** (*DI-02 @ 01:31:54*). A sinistra la struttura di un PDF firmato: *PDF CONTENT*, *SIGNATURE DICTIONARY*, *BYTE RANGE*, *CONTENTS*, *CERTIFICATE*, *SIGNED MESSAGE DIGEST*, *DOCUMENT TIMESTAMP*, *VALIDATION VALUES*, *DOCUMENT TIMESTAMP*, *EOF*, con le parentesi dei livelli *PDF Signature*, *PAdES B-Level*, *PAdES T-Level*, *PAdES LT-Level*, *PAdES LTA-Level*. Al centro l'albero degli oggetti di `test (35).pdf`: `/AcroForm`, campo `Signature1`, dizionario `/Sig` con `/Filter: /Adobe.PPKLite`, `/SubFilter: /ETSI.CAdES.…`, `/Name: My Name`, `/ContactInfo: info@eideasy.com`, `/Location: At my desk`, `/Reason: Signed in test app`, `/M: D:20210215161719+00'00'`, `/Contents`, `/ByteRange: [0, 9247, 47137, 794]`, e `/DSS` con `/Certs`. A destra lo schema degli aggiornamenti incrementali: *Original version* + *signature 1* + `%%EOF`, *Changes for version 2* + *signature 2* + `%%EOF`, *Changes for version 3* + *signature 3* + `%%EOF`, ciascuna firma "applies to these bytes". In basso a destra la finestra "Signature Properties" di Acrobat: "Signature is VALID, signed by GemBoxECDsa521 <info@gemboxsoftware.com>", ora di firma 2020/05/08 13:57:12 +02'00', "The document has not been modified since this signature was applied", "The signer's identity is valid", timestamp incorporato, "The path from the signer's certificate to an issuer's certificate was successfully built", "The signer's certificate is valid and has not been revoked".

> **Nota aggiunta:** `/ByteRange` elenca le due porzioni del file coperte dalla firma (tutto tranne lo spazio riservato a `/Contents`, che contiene la firma stessa): qui byte 0-9246 e 47137-47930. I livelli B, T, LT, LTA aggiungono rispettivamente: firma di base; marca temporale; dati di convalida (certificati, stato di revoca) per la verifica a lungo termine; marche temporali di archivio. PAdES è lo standard ETSI EN 319 142. I livelli e i certificati saranno ripresi nei capitoli su PKI e servizi fiduciari.

**Il cappello del "sicurista"** (*DI-02 @ 01:32:20-01:35:16*). Proprio per abilitare queste caratteristiche *paper-like*, il PDF è un formato molto complesso, "e tutte le volte che nell'informatica abbiamo parecchia complessità abbiamo parecchie strategie di attacco". Esistono diverse TTP sui PDF, in particolare il **signature wrapping attack**: si modifica un PDF aggiungendo una firma ulteriore fatta ad arte, e un lettore vulnerabile mostra il documento come correttamente firmato anche se modificato dopo la firma. Il docente non entra nei dettagli e mette il link a un sito che lo descrive. Con versioni **aggiornate** dei programmi PDF, per firmare e per verificare, si è immuni: le versioni recenti di Acrobat avvisano che il file potrebbe aver subito l'attacco. Software non aggiornati, "soprattutto software open source" scritti "non pensando con la mente del sicurista", potrebbero non fare tutti i controlli e dichiarare valida una firma su un file alterato.

**Slide "PDF signature wrapping attack"** (*DI-02 @ 01:34:37*, *01:38:52*), `https://pdf-insecurity.org/`. In alto: un *Certifier* firma un contratto PDF ("Transfer to: Name: Honest Corp., IBAN: US12 3456 7890, Amount: 100$") consentendo modifiche successive ("Further changes are allowed"); l'*Attacker* fa "Evil but allowed changes" e la *Victim* riceve "Name: Evil Corp., IBAN: US66 6666 6666, Amount: 100.000$" con il sigillo ancora valido. In basso la struttura di due file `%PDF-2.0`: l'oggetto `4 0 obj` compare due volte ("Sign the document to get a reward!" e "You are fired. Get out immediately"), uno come *Shadowed Document*; la *Digital Signature* (`6 0 obj (/Sig)`) copre la versione innocua, mentre un `xref`/`trailer` aggiunto in coda (in rosso, *Referencing Shadowed Content*) fa mostrare la versione malevola; le due finestre del lettore dicono entrambe "Signed and all signatures are valid".

> **Nota aggiunta:** la figura in basso è, nella terminologia di pdf-insecurity.org (Ruhr-Universität Bochum), uno **shadow attack** (la slide stessa usa "Shadowed Document"), mentre il contratto Honest/Evil Corp. in alto illustra l'abuso delle modifiche consentite su documenti certificati. Il *signature wrapping* in senso stretto (ACM CCS 2019) sposta la `/ByteRange` per far coprire alla firma i byte originali mentre il lettore interpreta contenuto inserito altrove. Sono famiglie di attacchi diverse sullo stesso principio: ciò che la firma copre non coincide con ciò che il lettore mostra.

## 12. Firma e cifratura di JSON: JWT, JWS, JWE, JAdES

*DI-02 @ 01:35:16-01:39:04*

A voce (*DI-02 @ 01:35:16*): chi fa data science conosce **JSON**, formato molto usato nel web, nello sviluppo software e nella data science per rappresentare dati "non strutturati"; i dati vengono codificati in **Base64** per trasferirli comodamente online. JSON ha uno standard di firma e di cifratura.

**Slide "…a digression about JSON Web Token (JWT)"** (*DI-02 @ 01:28:45*). A sinistra un token con le parti colorate: *JWT header* `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`, *JWT payload* `eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ`, poi segnaposto `B64chunkNo3`, `B64chunkNo4…`. A destra: *JOSE header* `{"typ":"JWT", "cty":"..."}`; *payload*: "Any payload (e.g. document in any file format) can be converted in to a JWT payload, not necessarily native JSON data."; "third / fourth / fifth optional chunk of a JWT". Testo: "**JSON** is a very popular format for representing (esp.) unstructured data. It is derived from JavaScript (JS) syntax but is very similar to that of other programming/scripting languages (e.g. Python). It's used in NoSQL databases as well (e.g. MongoDB). A **JSON Web Token** (JWT) is a base-64 encoding of JSON data for either **encryption** (JWE) *and* **signing** (JWS), as well as **selective-disclosure** (SD-JWT) and **key-binding** JWTs (KB-JWT)."

**JWS** (*DI-02 @ 01:36:23*). Il JSON firmato (il docente lo scioglie "JSON Web Token Signature") appende in coda al token Base64 (il JWT) un altro blocco Base64 con la firma: in grigio il contenuto, in cima un piccolo campo verde (un *wrapper*, un'intestazione) che dice "quello che segue è un JSON firmato con questo algoritmo", e in coda un blocco blu con la firma.

**Slide "JWS – digitally signed JWT"** (*DI-02 @ 01:35:22*). Token in tre parti: *JWT header*, *JWT payload*, *JWS signature* `SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`. *JOSE header*: `{"alg":"ES256", "typ":"JOSE", "iss":"Alice", "iat":21243431.33, "kid":`$\kappa^{\text{pub}}$`, "x5c":`[icona di certificato]`, "crit":["iat","alg","kid","x5c"]}`. *Payload*: `{"iss": "https://vc.vrs.digital.go.jp/issuer", "nbf": 1648956149.461584, // ~= 2022-04-03, "vc": {"type": ["https://smarthealth.cards#health-card",...], "credentialSubject": {"fhirVersion": "4.0.1", "fhirBundle": {...`; *JWT signature* `1110100101`. Schema: `BASE64URL-ENCODE(UTF8(JOSE Header))` . `BASE64URL-ENCODE(JWS Payload)` . `BASE64URL-ENCODE(JWS Signature)`. Testo: "Both JWE and JWS have a JWT compact serialization and a JSON compact serialization flavours. The former (shown here) is adopted because of interoperability, complexity and, ultimately, security reasons, although the latter is more feature-reach [sic] for both JWE and JWS. **JAdES** flavour, however, re-introduces many features still using JWT compact serialization." (Nella slide l'inciso è separato da un trattino lungo, reso qui con una virgola.)

Verifica per esecuzione (Python): il token delle slide è l'esempio standard di jwt.io. L'header decodifica in `{"alg":"HS256","typ":"JWT"}`, il payload in `{"sub":"1234567890","name":"John Doe","iat":1516239022}` (iat = 18/01/2018 01:30:22 UTC); la terza parte è l'HMAC-SHA256 con il segreto di esempio `your-256-bit-secret` (ricalcolato, coincide). Il valore `nbf` 1648956149,461584 corrisponde al 03/04/2022 03:22:29 UTC, come annotato nella slide.

> **Nota aggiunta:** tre precisazioni. (1) Il nome dello standard è **JSON Web Signature** (RFC 7515); JWE è **JSON Web Encryption** (RFC 7516), JWT (RFC 7519) è il formato dei *claim* che può essere protetto con JWS o JWE. (2) Gli header JOSE mostrati nei riquadri (`ES256`, firma ECDSA) sono illustrativi e non corrispondono al token a sinistra, che è `HS256`: un **MAC** con chiave simmetrica condivisa, che garantisce integrità e origine fra chi conosce il segreto ma **non** è una firma digitale nel senso del corso. (3) Le serializzazioni standard si chiamano *Compact Serialization* e *JSON Serialization* (la seconda non è "compact"). La codifica è **Base64url**, senza padding. JSON è più propriamente un formato per dati **semi-strutturati**.

**JWE** (*DI-02 @ 01:37:24*). Con modalità analoga si può cifrare un pacchetto JSON e trasferirlo senza che chi lo intercetta lo conosca; il docente non entra nei dettagli, "mi interessa relativamente di meno". Lo standard "è anche carino perché consente di scegliere alcune parti del JSON cifrandole e alcune lasciandole in chiaro"; si possono combinare firma e cifratura.

**Slide "JWE – encrypted JWT"** (*DI-02 @ 01:35:28*). Cinque parti: `BASE64URL-ENCODE(UTF8(JOSE Header))` . `(JWE Encrypted Key)` . `(Initialization Vector)` . `(Ciphertext)` . `(Authentication Tag)`. Header: `{"typ":"JWT", "cty":"...","kid":"...", "enc":"A256GCM", "alg":"RSA-OAEP"}`. Testo:
- "the payload is encrypted with a content encryption key (CEK) whose symmetric algorithm is specified in the `enc` element of the JOSE header;"
- "the CEK is encrypted with the JWE token recipient's public key (whose asymmetric algorithm is specified in the `alg` element of the JOSE header) and stored, key-wrapped, in its chunk."
- "There is currently none standard to both encrypt and sign the same data storing into a single JWT flavour, therefore the payload is usually: 1. digitally signed into a JWS; 2. the whole JWS is encrypted into a JWE."

Schema: JWS (Header . Payload . Signature) → encrypt → BASE64URL → JWE (Header . Encrypted Key . Vector . Payload . Tag).

> **Nota aggiunta:** il JWE è esattamente il **key wrapping** della sezione 6: CEK simmetrica (AES-256-GCM) per il contenuto, cifrata con la pubblica del destinatario (RSA-OAEP). Il docente a voce dice che JWE permette di cifrare solo alcune parti del JSON lasciandone altre in chiaro: lo standard JWE cifra l'intero payload; la divulgazione selettiva di singoli campi è invece lo scopo di **SD-JWT**, citato nella slide e ripreso nel corso parlando di wallet e credenziali verificabili.

**JAdES** (*DI-02 @ 01:38:01*). Esiste uno standard europeo di firma JSON con caratteristiche più avanzate, **JAdES**, "l'analogo del PAdES per la firma PDF". Non tutte le firme PDF sono PAdES: lo sono quelle conformi a questo standard europeo; firmando con Acrobat senza specificare altro, di default si fanno firme PAdES, ma un documento generato da software non europeo molto probabilmente non lo è. JAdES è ancora poco diffuso perché è il più recente della famiglia, usato in ambito europeo; il docente dice di aver "avuto il privilegio di poter contribuire al disegno di questo standard" (*01:38:32-01:39:04*).

**Slide "JAdES – JSON advanced digital signature"** (*DI-02 @ 01:35:33*, *01:37:59*). Stesso token; *JOSE header*: `{"alg":"ES256", "typ":"JOSE", "iat":21243431.33, "x5t#o":{"properties":{"digAlg":"…", "digVal":"…"}}, "kid":`$\kappa^{\text{pub}}$`, "srCms":{…}, "sigPl":{…}, "etsiU":{…}, "crit":["iat","alg","x5t#o","srCms","sigPl"]}`; payload della *smart health card* giapponese (paziente "DAN YAMAMOTO", `birthDate` "xxxx-xx-xx", risorsa "Immunization" con `occurrenceDateTime` "2021-08-10", `vaccineCode`…). Testo: "**JAdES** introduces several new claims to a JWS' JOSE header to provide the same flexibility and trust level of CAdES, XAdES and PAdES for advanced electronic signatures and seals. It also extends JWS functionalities, namely: **multiple** signatures; [un-]signed payload and header (**coverage**); **detached** signature."

> **Nota aggiunta:** JAdES è ETSI TS 119 182-1, prima versione V1.1.1 del marzo 2021 (verificato sul sito ETSI). CAdES (CMS), XAdES (XML) e PAdES (PDF) sono gli altri formati AdES; nel corso torneranno con i servizi fiduciari eIDAS. Non ho verificato in fonti esterne il contributo del docente allo standard.

### Integrazione Teams 2026

*Sezioni 11-12 (PAdES, JSON)*

- Nel 2026 PAdES, i formati AdES e la firma JSON non sono trattati in Teams 1: compaiono in Teams 6 (formati di firma, da circa 0:44) e Teams 8 (SD-JWT), di competenza di altri capitoli. Nessuna integrazione qui.

## 13. Introduzione al calcolo quantistico

*DI-02 @ 01:39:04-01:54:55*

**Capitolo saltato** (*DI-02 @ 01:39:04*): "per il momento salto questo capitolo perché vorrei parlarvene solo se ci sarà tempo". La slide di sezione che compare subito dopo (*01:39:09*) è **"Privacy Enhancing Technologies and anonymisation"**: è questo il capitolo saltato, non JAdES (vedi file divergenze).

**Slide di sezione "Introduction to Quantum Cryptography"** (*DI-02 @ 01:39:41*). Il docente vorrebbe parlare approfonditamente del background fisico-matematico, ma "esulerebbe dagli scopi di un corso di crittografia per la data science"; oggi una piccola introduzione, "dovrò essere per forza di cose impreciso", "non posso fare alle 8 di sera una lezione di meccanica quantistica".

**Bit classico** (*DI-02 @ 01:40:07*). Finora i dati crittografici sono rappresentati con bit 0/1. La microelettronica funziona con fenomeni quantistici (semiconduttori) ma su scale tali da essere descritti bene con approssimazioni classiche: a seconda che la corrente scorra o no, che un cristallo o una molecola sia polarizzata in un modo o nell'altro, che lo spin di una particella o di un fotone sia in un verso o nell'altro, si dice con "quasi assoluta certezza", deterministicamente, se il bit vale 0 o 1. Due bit valgono 00, 01, 10, 11 e "rappresentano i numeri 1, 2, 3, 4"; tre bit danno $2^3$ combinazioni.

> **Correzione:** 00, 01, 10, 11 rappresentano 0, 1, 2, 3 (quattro valori, ma a partire da 0).

**Qubit** (*DI-02 @ 01:41:42-01:43:59*). Gli informatici che si occupano di calcolo e crittografia quantistica lavorano con quantità astratte e non hanno necessariamente basi di meccanica quantistica. L'unità è il **bit quantistico**, **qubit**: un sistema a due stati come il bit classico, ma gli stati non sono determinati in modo assoluto; si trova in una **sovrapposizione** "statistica" di entrambi finché non viene **misurato/osservato**. Può valere 0 o 1 a seconda di come viene generato dal circuito e soprattutto di come viene misurato. L'osservazione può essere di Bob che riceve il qubit preparato da Alice (leggendolo lo altera e "decide" lo stato, anche se dipende da come Alice l'ha preparato) oppure di **Eva** che lo intercetta e, leggendolo, ne fissa lo stato definitivo.

**Slide "Qubits"** (*DI-02 @ 01:44:04*, *01:45:04*, *01:48:01*, *01:53:47*). Testo: "Qubits are *quantum* **2-states** systems which information equivalent to one "classical" bit can be represented within. Since 1990's many physical systems have been researched and prototyped for qubits: NMR, either solid- or liquid-state; nitrogen valence centres in diamonds; photonic devices (e.g. used in QKD); superconducting *transmons*; *anyons* (Majorana, Ising, Fibonacci); topological qubits (still highly experimental); ion traps; …". Figure: *Classical Bit* (binary system: 0 OR 1); *quantum bit "qubit"* (arbitrarily manipulable two-state quantum system) come sfera con $|0\rangle$ e $|1\rangle$ ai poli, "SUPERPOSITION: Overlay of different states", "MEASURING: Clear definition of the state", lo stato $\frac{|0\rangle + |1\rangle}{\sqrt{2}}$; circuito di un transmon; nanofilo InSb con quasiparticella di Majorana; schema di qubit ad anyoni (memoria, *braiding*, misura per *fusion*).

**Realizzazioni** (*DI-02 @ 01:43:59-01:47:08*). I qubit non sono solo astratti: funzionano con modelli fisici in cui i comportamenti quantistici non sono più approssimabili come classici. Oggi ci sono "una mezza dozzina" di tecniche realistiche (elencate nella slide, "non ve le elenco perché non servono ai fini di questo corso"). Il docente ricorda che già quando era studente negli anni '90 si parlava di qubit e di **quantum dot**, oggetti allora teorici; oggi esistono piccoli calcolatori quantistici. Si costruiscono dispositivi che contengono qubit, **fili quantistici** che trasportano qubit (anche fra punti dello stesso processore), canali a lunga distanza in **fibra ottica** "che oggi riescono a raggiungere le distanze di alcune decine di chilometri", e **quantum gate**, analoghi quantistici di diodi e transistor. La difficoltà: se non controllati, i fenomeni quantistici perdono **coerenza**; se fra due transistor che producono due addendi e il punto in cui si fa l'OR qualcosa va storto "in quei nanometri", il calcolo è sbagliato. L'**errore quantistico** è stato per vent'anni il problema principale; oggi si sa come mitigarlo, ma non in economia di scala.

**Slide "Quantum dots and quantum wires"** (*DI-02 @ 01:47:13*). Testo: "Qubits implementations are still deeply subject to **errors**, therefore quantum error correcting codes (**QECC**s, e.g. Shor's) must be used as mitigation strategy. Better qubit implementations are needed, especially to: "trap" qubits, both *at-rest* (quantum dots) and *in-transit* (quantum wires); perform basic arithmetic (quantum **gate**s). Quantum computers running classical algorithms need only to be concerned about *amplitude*/bit ($\sim |\psi|$) errors; those running quantum algorithms, instead, must also be concerned on *phase* errors ($\sim \arg \psi$)." Figure: un chip con bonding, strati InAs/GaAs con quantum dot piramidali, un dispositivo a "2D electron gas" con *quantum dot*, *sensor quantum dot*, *reservoirs*.

> **Correzione:** a *01:44:30* il docente descrive i quantum dot come "porte logiche che funzionavano su bit quantistici". Secondo la sua stessa slide i quantum dot **intrappolano** i qubit "a riposo"; le operazioni sono dei quantum gate.

**"Non guardate le slide"** (*DI-02 @ 01:47:28*): "non guardate le slide, non saranno oggetto d'esame, vi devo dare alcune basi minime per capire cos'è il calcolo quantistico". Le tecniche richiedono circuiti complessi, fotonici o superconduttivi, difficili da integrare: "siamo abbastanza vicini da usare calcolatori quantistici per calcoli concreti in ambito industriale, ma ancora molto lontani da averne uno nelle tasche dei jeans". Per calcoli significativi servono numeri di "qualche migliaio di cifre", spese enormi e macchinari giganti in laboratorio (*01:47:40-01:48:45*).

**Slide "From quantum gates to quantum computing"** (*DI-02 @ 01:47:21*, *01:48:09*). Testo: "Quantum gates realize reversible (*unitary*) qubit operations; they are the building blocks for QCs. *Universal* quantum gates can approximately realize any unitary operator on qubits. Due to quantum properties (and thanks to QECCs), quantum computers may be able to compute qubits at faster rates than classical ones can, on classical bits. Some mathematical problems that are exponentially "hard" to solve (i.e. *non-polynomial*, **NP**) with classical computers, may be reduced to sub-exponential (**BQP**) complexity on QCs." Figura di un circuito fotonico (*Quantum source*, *State preparing*, *Quantum gate*, *State tomography*) e dettagli di Hadamard, *Phase z gate* e CNOT a progettazione inversa. Tabella *quantum gates*:

| Porta | Matrice |
|---|---|
| Pauli's (NOT) $X$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| Hadamard $H$ | $\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ |
| "T" | $\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$ |
| "adjoint T" $T^\dagger$ | $\begin{pmatrix}1&0\\0&e^{-i\pi/4}\end{pmatrix}$ |
| phase-shift (1-param) $S$ | $\begin{pmatrix}1&0\\0&i\end{pmatrix}$ |
| adjoint phase-shift $S^\dagger$ | $\begin{pmatrix}1&0\\0&-i\end{pmatrix}$ |
| Feynman (CNOT) | $\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$ |

(Nella slide $S$ è detta "phase-shift (1-param)", ma la matrice mostrata è la porta $S$ fissa, cioè lo sfasamento di $\pi/2$; l'aggiunto è scritto $T^t$, $S^t$.)

**Slide ""Quantum" effort (and spending) worldwide"** (*DI-02 @ 01:48:18*, *01:50:04*). Testo: "Quantum Computing and Communications (QC) is a set of technologies employing quantum phenomena to: **run algorithms** that are barely **computable**, if at all, by "classic" computers; safeguard not just information **integrity**, but also **detection** of unwanted access (in Quantum Mechanics terms: *observed*)." Mappa con le spese (fonte `https://qureca.com/overview-of-quantum-initiatives-worldwide-2023/`): "Global Quantum Efforts \$38.6b (estimate)"; fra le altre China \$15b, United Kingdom £3.5b = \$4.3b, US National Quantum Initiative \$3.75b, Germany 3b € = \$3.3b, South Korea \$2.35b, France \$2.2b, Russia \$1.45b, European Quantum Flagship 1b € = \$1.1b, Canada \$1.1b, Netherlands \$1b.

Commento (*DI-02 @ 01:48:45-01:50:23*): "slide del 2023"; sono cifre ricavate da dati pubblici, mentre la spesa militare e di sicurezza è tipicamente segreta. Ci sono *big spender* e *huge spender*, primi Stati Uniti e Cina: la Cina avrebbe speso 15 miliardi di dollari "a fronte degli Stati Uniti che ne hanno spesi circa 3,5, il Regno Unito 4,5, la Germania 3,3", ma anche gli Stati più piccoli non hanno speso poco.

**Il parallelismo quantistico** (*DI-02 @ 01:50:23-01:52:58*). Il docente cerca una slide che manca ("mi sa che mi manca una slide, non l'ho messa… ve la farò trovare alla prossima lezione"; le slide sul post-quantum scorrono per pochi secondi, sotto) e ne parla a voce: un qubit è sovrapposizione di due risultati; con due qubit il numero "può valere sia 1 che 2 che 3 che 4" insieme. Se si è bravi a preparare i qubit iniziali, cioè la distribuzione di probabilità sui loro valori, la **funzione d'onda** "che contiene in sé tutte le proprietà statistiche di questa variabile casuale che è un qubit", e a calcolare senza introdurre errori, a parità di numero di bit il calcolatore quantistico **fa più calcoli in parallelo**, con un fattore di parallelizzazione irraggiungibile da un calcolatore classico anche fra diversi anni.

**Conseguenza per la crittografia** (*DI-02 @ 01:52:58-01:54:40*). "Entro in un campo che non è neanche più la mia zona di comfort… non è qualcosa che ho tecnicamente studiato." Secondo gli esperti si possono realizzare algoritmi per problemi "di tipo non polinomiale", che richiederebbero un tempo esponenziale nel numero di bit: problemi crittografici che, aumentando i bit, diventavano impossibili da rompere al passo del progresso tecnologico. Con il calcolatore quantistico "aumentare il numero di bit può non diventare più l'unico modo per difendermi, per alzare quella famosa asticella". Nella prossima lezione: come funzionano gli algoritmi quantistici in ambito crittografico, come i calcolatori quantistici possono rompere "molti, non tutti" gli algoritmi classici presentati come robusti. Fine della lezione con la richiesta di domande.

> **Correzione:** l'affermazione (a voce e nella slide) che i calcolatori quantistici rendano risolvibili i problemi "non polinomiali (NP)" è imprecisa. Non si ritiene che i calcolatori quantistici risolvano in tempo polinomiale i problemi NP-completi. Shor risolve in tempo polinomiale **fattorizzazione** e **logaritmo discreto** (quindi RSA e curve ellittiche), problemi in NP ma non ritenuti NP-completi e per i quali non è noto un algoritmo classico polinomiale; BQP è la classe dei problemi risolvibili in tempo **polinomiale** (non "sub-esponenziale") da un calcolatore quantistico con errore limitato. Per hash e cifrari simmetrici Grover dà solo un vantaggio quadratico, compensabile raddoppiando le chiavi.

> **Nota aggiunta:** "sovrapposizione statistica" e "fa tutti i calcoli in parallelo" sono semplificazioni dichiarate dal docente. Lo stato di un qubit è $\alpha|0\rangle + \beta|1\rangle$ con ampiezze **complesse** ($|\alpha|^2 + |\beta|^2 = 1$), non una miscela statistica: le ampiezze possono **interferire**, ed è l'interferenza, non il semplice parallelismo, che gli algoritmi quantistici sfruttano; una misura restituisce un solo risultato. Sulle distanze in fibra: la QKD in fibra ha superato i 1000 km nel 2023 (twin-field QKD, USTC, Liu et al., *Phys. Rev. Lett.*), ben oltre le "alcune decine di chilometri" citate, anche se a tassi di chiave molto bassi.

**Slide scorse in pochi secondi** (*DI-02 @ 01:50:20-01:50:35*), mentre il docente cerca la slide mancante: "Quantum: from Computing to Cryptography" (sezione); "Quantum-safe algorithms" (FIPS 203, 204, 205, `https://csrc.nist.gov/projects/post-quantum-cryptography/`: "First international standards on PQC for encryption and digital signing. Based on 4 rounds of peer-review, which started in year 2017 by an initial submission of 69 proposed algorithms:", elenco non ancora comparso); "Harvest-now-decrypt-later attack!" ("According to Research community, symmetric algorithms and crypto hash functions shall start to be vulnerable around **2026**. Increasing keys'/digests' lengths *may* still counter that. Public-key crypto may be vulnerable around **2029**. Increasing key lengths shall not work. Transitioning to PQC is a crypto-agility process that organisations need to complete before their relevant TAs can get quantum crypto-analytic capabilities (*Mosca's law*)", con la timeline da 1994 a "Today", fonte BIS website); "NIST PQC roadmap" ("NIST proposed timeline: **2030** All existing public-key & 128-bit symmetric/hashing methods to be deprecated. To be removed from FIPS by **2035**."). Non commentate in DI-02: sono il contenuto della lezione successiva.

## 14. Crittografia quantistica: le tre accezioni (solo Teams 2026)

*Contenuto del 2026 senza corrispondente in DI-02: nel 2025 il docente si ferma all'introduzione al calcolo quantistico e rinvia alla lezione successiva.*

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 14 (fisica quantistica, qubit, crittografia quantistica)*

- **Esame**: "Vi dico subito che non ci saranno domande di meccanica quantistica né di calcolo quantistico. All'esame al massimo potrebbe esserci qualche domanda sul problema concreto alla base della crittografia post quantistica"; le introduzioni di meccanica, elettronica e calcolo quantistico servono solo a spiegare "perché il problema si pone oggi". (Teams 1 @ 1:02:46-1:03:15)
- **Classico e quantistico**: la fisica classica studia oggetti macroscopici (dalla grande molecola in su); quando le dimensioni sono confrontabili con gli atomi, o le energie sono molto alte (acceleratori, cosmologia quantistica di stelle e buchi neri), dominano gli effetti quantistici, che convergono ai fenomeni classici al ridursi delle energie e al crescere delle scale: "tutto il mondo si comporta in maniera quantistica", quello che osserviamo è classico per buona approssimazione. (Teams 1 @ 1:03:15-1:05:24)
- **L'osservazione altera il sistema**: analogia del pulviscolo in una stanza buia illuminato da una lama di luce: osservandolo con la luce lo si riscalda e se ne aumenta il moto browniano. Per particelle molto piccole si devono usare fotoni con momento angolare, magnetico, spin confrontabili, quindi l'osservazione le altera: nelle equazioni bisogna includere anche come si osserva il fenomeno ("principio di determinazione di Heisenberg", sic). Per questo le grandezze si descrivono con **funzioni d'onda** $\psi$ complesse, ampiezze di probabilità. (Teams 1 @ 1:05:24-1:09:49)
- **Qubit 2026**: una particella confinata per rappresentare un bit, se è abbastanza piccola da interagire con la materia (o fare *tunneling*), non vale più solo 0 o 1 ma una **combinazione lineare a coefficienti complessi** di 0 e 1. Ricordo personale: da studente di ingegneria al terzo anno il docente fece una tesina sui quantum dot. Servono porte logiche, "cavi", una microelettronica che misura fotone per fotone, elettrone per elettrone o plasmone per plasmone; quantum dot per memorizzare un qubit, *quantum wire* per trasportarlo (ripresi nella QKD). (Teams 1 @ 1:09:54-1:13:29)
- **Rumore**: come nell'elettronica tradizionale, ma oltre al rumore d'**ampiezza** c'è un rumore di **fase** sui coefficienti complessi; è il problema più grave per arrivare a centinaia e poi migliaia di qubit, e i metodi per ridurlo sono "estremamente costosi". (Teams 1 @ 1:13:29-1:15:07)
- **Spesa e sovranità**: il diagramma "risale ad alcuni anni fa"; la spesa non è solo commerciale ma **strategica**: chi domina il settore resta sovrano e "detta le leggi", come nella generazione precedente con il cloud e oggi con l'intelligenza artificiale. Le cifre sono pubbliche e non aggiornate: parte della spesa può essere classificata come militare. (Teams 1 @ 1:15:07-1:16:14, 1:19:46-1:20:27)
- **Le tre accezioni di "crittografia quantistica"** (Teams 1 @ 1:16:14-1:26:29):
  1. **Crittoanalisi quantistica**: usare calcolatori quantistici per risolvere i problemi matematici alla base della crittografia classica e batterla: derivare una privata da una pubblica, trovare una chiave simmetrica, generare una collisione o invertire un hash. Questi problemi sono tutti risolvibili, ma con algoritmi robusti sono **antieconomici** per l'avversario; i calcolatori quantistici (anche grazie all'**entanglement**, rinviato alla lezione successiva) sembrano in grado di battere la crittografia basata su **logaritmi discreti** molto più velocemente di qualunque calcolatore classico presente o vicino, trasformando un problema non polinomiale in uno polinomiale.
  2. **Crittografia post-quantistica** (*quantum safe*): cifrari resistenti alla crittoanalisi quantistica, che però devono girare **oggi**, su software e microelettronica **classici** ("idealmente il mio smartphone"), per proteggere oggi dati che domani (e "purtroppo non solo domani") potrebbero essere attaccati. Per Shor e Grover "non basta aumentare la lunghezza delle chiavi": allungare RSA "può darci qualche anno in più, ma non potrà risolvere il problema"; andranno sostituiti RSA e le curve ellittiche; "sembra che l'unico algoritmo che potrebbe resistere allungando la chiave è AES", "ancora da vedere".
  3. **QKD**, distribuzione quantistica delle chiavi: un canale di comunicazione quantistico (aria, fibra ottica) che non rende il dato riservato, ma permette alle due estremità di **sapere se è stato intercettato**. Si può continuare a usare un algoritmo classico abbastanza robusto, con la certezza, "dimostrata dalla fisica", che la chiave segreta (simmetrica fra Alice e Bob, o privata generata da altri per Alice) non è stata osservata; se qualcuno l'ha osservata e quindi inevitabilmente alterata, la si scarta e se ne genera un'altra. Approfondimento nella lezione successiva.

> **Correzione:** a Teams 1 @ 1:23:27 il docente dice "AES di cifratura asimmetrica": AES è un cifrario **simmetrico** (lapsus o errore di trascrizione). Shor e Grover hanno ideato **algoritmi**, non teoremi (Teams 1 @ 1:22:35). Il principio è di **indeterminazione** di Heisenberg (Teams 1 @ 1:08:36; possibile errore di trascrizione).

> **Nota aggiunta:** l'affermazione 2026 che allungare le chiavi RSA "dà qualche anno in più" va intesa in senso di costo ingegneristico: l'algoritmo di Shor è polinomiale nella lunghezza della chiave (risorse che crescono circa col cubo dei bit), quindi raddoppiare la chiave aumenta il costo dell'attacco solo di un fattore costante, mentre per il difensore il costo cresce allo stesso modo. Per AES e hash Grover dimezza i bit di sicurezza: AES-256 conserva circa 128 bit, per questo è considerato resistente.

## 15. Glossario

| Termine | Significato nel corso |
|---|---|
| Eve / Eva, *eavesdropping* | L'attrice della minaccia che intercetta il canale; Carl è l'uomo nel mezzo |
| AES-CBC | Cifratura a blocchi in cui ogni blocco cifrato fa da IV al successivo; una modifica altera il blocco e i successivi |
| Vettore di inizializzazione (IV) | Parametro della cifratura simmetrica, "fondamentale per la sicurezza"; nel laboratorio posto a zero per semplicità |
| RSA-OAEP | Schema di cifratura RSA con padding randomizzato, usato nel laboratorio CyberChef |
| PEM | Rappresentazione in Base64 delle chiavi (`BEGIN PUBLIC KEY`, `BEGIN RSA PRIVATE KEY`) |
| Key wrapping (key encapsulation) | Contenuto cifrato con chiave simmetrica effimera, cifrata con la pubblica del destinatario |
| Busta crittografica | Contenitore unico: contenuto cifrato + chiave cifrata, oppure documento in chiaro + firma |
| Cifratura in transito | Cifrare per attraversare un canale non sicuro; mittente e destinatario tengono il chiaro |
| Cifratura a riposo | Cifrare per conservare; si elimina la copia in chiaro |
| Cifratura in uso | Elaborare dati senza decifrarli; esempio principale la cifratura omomorfa |
| Cifratura omomorfa | Schema in cui certe operazioni sui crittogrammi corrispondono a operazioni sui dati in chiaro |
| Evil Maid | Attacco con accesso fisico al dispositivo incustodito; mitigato dalla cifratura del disco |
| Firma digitale | Impronta crittografica del dato cifrata con la chiave privata del firmatario |
| Convalida (verifica) | Decifrare la firma con la pubblica dell'asserito firmatario, ricalcolare l'hash, confrontare: esito vero/falso |
| Firma *detached* / *enveloped* | Firma separata dal documento / imbustata con esso |
| Algoritmo di firma | Combinazione di un hash e di un algoritmo a chiave pubblica |
| Schema di firma | Algoritmi più procedure che garantiscono controllo esclusivo della privata e titolarità della pubblica |
| Sole control | Controllo esclusivo della chiave privata da parte del titolare |
| FIPS 186-5 | Digital Signature Standard del NIST (2023) |
| PAdES | Formato europeo di firma avanzata per PDF (livelli B, T, LT, LTA) |
| `/Sig`, `/Contents`, `/ByteRange` | Campi del PDF firmato: dizionario di firma, valore della firma, byte coperti |
| Signature wrapping attack | Attacco ai lettori PDF vulnerabili che mostrano come valido un PDF modificato dopo la firma |
| JWT, JWS, JWE | JSON Web Token; JSON Web Signature (firmato); JSON Web Encryption (cifrato) |
| JOSE header | Intestazione JSON di JWS/JWE con algoritmo (`alg`, `enc`), chiave (`kid`), certificati (`x5c`) |
| CEK | Content Encryption Key: la chiave simmetrica di un JWE |
| SD-JWT, KB-JWT | JWT a divulgazione selettiva; JWT con legame a una chiave |
| JAdES | Formato europeo di firma avanzata per JSON (ETSI TS 119 182-1) |
| Qubit | Sistema quantistico a due stati in sovrapposizione finché non misurato |
| Quantum dot, quantum wire | Dispositivi che intrappolano un qubit (a riposo) o lo trasportano (in transito) |
| Quantum gate | Operazione unitaria (reversibile) sui qubit: X, H, T, S, CNOT |
| QECC | Codici di correzione d'errore quantistici |
| Crittoanalisi quantistica | Uso di calcolatori quantistici per rompere la crittografia classica |
| Crittografia post-quantistica (quantum safe) | Algoritmi classici resistenti alla crittoanalisi quantistica |
| QKD | Distribuzione quantistica delle chiavi: rileva le intercettazioni |

## 16. Punti incerti

- *DI-02 @ 01:02:28*: "recuperare sia la lezione fatta, sia parte di quella lezione che non è stata registrata ieri, sia per la lezione in meno". DI-01 è del 07/10/2025, DI-02 del 15/10/2025: "ieri" (14/10) farebbe pensare a una lezione **non registrata**; ma potrebbe riferirsi alla parte senza audio di DI-01. Non risolvibile dalle fonti disponibili.
- *DI-02 @ 01:19:31*: esempio di firmatario persona fisica, trascritto "Alice Bengasi Milano via Rodengo 12": [?].
- *DI-02 @ 01:26:44*: "hai firmato il suo documento con l'ISO" [?] (verosimilmente "il documento che collide").
- *DI-02 @ 01:28:24*: la "terza tipologia" di attacco saltata non è nominata; l'associazione con "recorded and replayed" della slide è una mia ipotesi.
- *DI-02 @ 01:31:48*: il laboratorio sulle firme PDF è promesso per "la prossima lezione o quella dopo": da verificare nei capitoli successivi.
- Teams 1 @ 0:46:06: "firma RSA 256 con chiave lunga 2048": [?], verosimilmente RSA con SHA-256.
- Il messaggio RSA a schermo risulta di 98 caratteri nel contatore di output di CyberChef e 97 nel contatore di posizione dell'input; nella mia prova il testo letto è di 97 byte. Differenza di un carattere (probabile a capo finale), irrilevante.
- La slide mancante sul parallelismo quantistico (*DI-02 @ 01:50:23*) non compare in DI-02.

## 17. Esame

Frasi del docente su esame e perimetro, in ordine:

- *DI-02 @ 00:31:04*: domande benvenute sulle funzioni di CyberChef viste, ma "questo non è un corso di CyberChef" (come in DI-01 @ 00:50:44).
- *DI-02 @ 00:49:52*: "capire questo meccanismo [key wrapping] significa capire gran parte della crittografia; il prossimo scalino lo vedremo con la firma digitale, e poi i passaggi logicamente complessi finiscono qui in tutto il corso".
- *DI-02 @ 00:54:16*: cifratura omomorfa "di cui non parleremo in questo corso, o meglio, di cui parleremo se c'è tempo alla fine".
- *DI-02 @ 01:13:11* e *01:15:34*: la firma digitale come "primo passaggio logico veramente importante" e "il concetto logico più difficile da capire dell'intero corso"; base per capire digital trust e identità digitale.
- *DI-02 @ 01:39:04*: capitolo "Privacy Enhancing Technologies and anonymisation" saltato, "solo se ci sarà tempo".
- *DI-02 @ 01:39:36*: background fisico-matematico del quantistico fuori dagli scopi del corso.
- *DI-02 @ 01:44:30*: le tecniche di realizzazione dei qubit "non servono ai fini di questo corso".
- ***DI-02 @ 01:47:28***: "**non guardate le slide, non saranno oggetto d'esame**": slide sull'hardware quantistico (qubit, quantum dot, quantum gate).
- **Teams 1 @ 1:02:46** (2026): "**non ci saranno domande di meccanica quantistica né di calcolo quantistico. All'esame al massimo potrebbe esserci qualche domanda sul problema concreto alla base della crittografia post quantistica**". Unico riferimento esplicito all'esame nelle lezioni Teams 2026; conferma e precisa l'esclusione del 2025.
- Teams 1 @ 0:33:30 (2026): cifratura in uso "a scopo di cultura generale".
- Teams 1 @ 0:52:46 (2026): "il 90% del digital trust si comprende se si comprende a cosa serve la firma digitale e come funziona".

Nessuna indicazione su modalità, data o formato d'esame. Per il quadro completo vedi la pagina [Assessment](assessment.md).
