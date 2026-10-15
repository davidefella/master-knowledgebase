# 03 - Cifratura per più destinatari, cifratura omomorfa, calcolo quantistico e post-quantum, certificati, autorità di certificazione, PKI gerarchica

*DI-03, registrazione Teams del 17/10/2025 (portale, a schermo "2025-10-17 16:07 UTC"), 1:57:53. Integrazioni da Teams 2 (22/09/2026, intera, 0:51:29) e Teams 3 (23/09/2026, da 0:00:05 a 0:58:48).*

> **Come leggere questo capitolo.** La lezione ha due metà. Nella prima (fino a *00:54:05*) il docente chiude la crittografia "teorica": cifratura per più destinatari, cifratura omomorfa in formule, calcolo quantistico, crittoanalisi quantistica, crittografia post-quantistica (PQC), QKD. Nella seconda entra nell'argomento proprio del corso, il **digital trust**: autenticità delle chiavi pubbliche, notai e terze parti fidate, certificati digitali, certification authority, PKI.
>
> **Cosa è fuori esame (detto dal docente).** Meccanica quantistica e calcolo quantistico (sezione 3: entanglement, qubit, porte quantistiche, quantum dot, investimenti) non saranno oggetto di domande (*DI-03 @ 00:13:37*; Teams 1 @ 1:02:46; DI-02 @ 01:47:08). Può invece esserci "qualche domanda sul **problema concreto alla base della crittografia post quantistica**" (Teams 1 @ 1:02:53): è riassunto nel riquadro della sezione 4. Dettagli in sezione 21.
>
> Il perimetro Teams di questo capitolo si ferma a Teams 3 @ 0:58:48, dove il docente passa al problema della validità nel tempo dei certificati (trust list, revoca, CRL): quella parte è nel capitolo 04.

## Indice

1. Cifratura per più destinatari: una sola chiave di contenuto
2. Cifratura omomorfa in formule
3. Calcolo quantistico: fenomeni e hardware (fuori esame)
4. Dal calcolo quantistico alla crittografia: tre discipline
5. Standard post-quantum: NIST FIPS 203, 204, 205 ed ETSI
6. Harvest now, decrypt later
7. La roadmap NIST
8. Quantum Key Distribution (QKD)
9. Nuovo nel 2026: migrazione ibrida e attacchi di downgrade
10. Digital trust: due problemi pratici ancora aperti
11. Dai testimoni ai notai al digital trust
12. La fiducia nell'era digitale: soggetto, CA, prestatore di servizi fiduciari
13. Il certificato digitale e le sue tre caratteristiche
14. Certificati a chiave pubblica e di attributo, contenuto e convalida
15. Certificati elettronici secondo eIDAS
16. Nomenclatura: certificati di CA, foglia, autofirmati, radice; CA tecniche e amministrative
17. Fidarsi di una CA: la tassonomia della fiducia
18. PKI: gerarchie e percorso di fiducia
19. Glossario
20. Punti incerti
21. Esame

## 1. Cifratura per più destinatari: una sola chiave di contenuto

*DI-03 @ 00:00:01-00:07:11*

La registrazione parte mentre il docente risponde a una domanda sulla cifratura verso più destinatari. Torna alla slide **"Asymmetric key wrapping"** (frame *00:00:07*, ripresa a *00:06:22*), già descritta nel capitolo 01 (sezione 12): plaintext cifrato con la chiave simmetrica $\kappa^{\text{sym}}$, chiave simmetrica cifrata con la chiave pubblica $\kappa^{\text{pub}}$ del destinatario, i due oggetti nella *cryptographic envelope*, il destinatario recupera $\kappa^{\text{sym}}$ con $\kappa^{\text{priv}}$. Testo a destra: "Given their secrecy requirements, *symmetric* and *private* keys are commonly referred to as ***secret* keys**, as opposed to *public* keys."

Il meccanismo, con i destinatari Paperino, Paperoga e Topolino (*DI-03 @ 00:00:33-00:03:49*):
1. se nel software di cifratura indico i destinatari, il software deve **già avere i loro certificati**, cioè le loro chiavi pubbliche;
2. il software genera **una sola** chiave simmetrica casuale, valida solo per quell'operazione; l'utente non la vede;
3. la chiave simmetrica cifra il file (il docente sceglie una JPEG "così evitiamo confusioni con la firma PAdES");
4. nella busta crittografica (il file **P7E**) vanno il file cifrato e **tre copie della stessa chiave simmetrica**, ciascuna cifrata con la chiave pubblica di un destinatario;
5. Paperino riconosce la copia cifrata per lui, la apre con la sua chiave privata e decifra il file; Paperoga ignora la copia di Paperino e usa la sua; lo stesso Topolino. Zio Paperone, che riceve il file, trova tre contenitori che non può aprire e quindi non può estrarre la chiave;
6. dopo l'uso il software **cancella la chiave simmetrica dalla memoria**: non è mai salvata in chiaro.

Il docente si autocorregge (*DI-03 @ 00:03:49*): spesso questi software aggiungono di default **una quarta copia** della chiave simmetrica cifrata con la chiave pubblica di chi ha generato il file, perché l'*owner* deve poterlo riaprire; la funzione si può disattivare.

A una domanda ("quindi creo un certificato?") risponde che il certificato si definisce più avanti nella stessa lezione, "se no confondiamo": per ora si parla solo di chiavi (*DI-03 @ 00:04:23*). Alla domanda se c'entri la **chiave di sessione**: "no, non c'entra nulla", se ne parlerà in una lezione successiva. La generazione della chiave non si fa a mano come su CyberChef: la fa il software nel back-end, ma è importante capirla per non pensare che si usi una chiave simmetrica per ogni destinatario (*DI-03 @ 00:04:57-00:05:28*).

In alcuni contesti, come il cinema, questa chiave si chiama **chiave di contenuto** (*content key*), perché riferita solo a quel contenuto. Se lo stesso JPEG viene ricifrato per Pluto, Iron Man e Capitan America, la chiave simmetrica è **rigenerata da capo**. Per questo un attaccante che collezionasse 80 invii cifrati dello stesso file, pur sapendo che dentro c'è lo stesso contenuto, troverebbe 80 chiavi diverse e non potrebbe risalire a una chiave unica con attacchi basati su più crittogrammi ("non-suffertex-attacchi" nella trascrizione, [?]); "ma è un discorso di secondo livello" (*DI-03 @ 00:05:59-00:07:11*).

> **Nota aggiunta:** il file P7E è un contenitore CMS/PKCS#7 di tipo *EnvelopedData*: per ogni destinatario contiene una struttura *RecipientInfo* con la chiave di contenuto cifrata per quel destinatario, più il contenuto cifrato una volta sola con la chiave simmetrica. La "copia per l'owner" è semplicemente un *RecipientInfo* in più. Il termine sfuggito nella trascrizione è plausibilmente un riferimento ad attacchi di tipo *known-ciphertext* o *known-plaintext*, ma non è udibile con certezza.

A *00:02:11* il docente dice che Paperino riconosce "un oggetto firmato con la sua chiave pubblica": è un lapsus per **cifrato** (con la chiave pubblica si cifra, non si firma).

## 2. Cifratura omomorfa in formule

*DI-03 @ 00:07:11-00:12:13*

Il docente ha preparato "una schermata per qualcuno che fosse un po' più avido di matematica" sulla cifratura omomorfa, già spiegata in modo semplice nella lezione precedente (capitolo 02): "questa è la slide più matematica che vedrete in tutto il corso, solo per soddisfare un po' di curiosità" (*DI-03 @ 00:07:42*).

Passando, scorre la slide **"The 3 states of data encryption"** (frame *00:07:12*, fonte "Safesforce website"): *at rest*, *in transit*, *in use*; "encryption at rest" su cartelle, computer, smartphone, server, database; "encryption in transit" in tre passi, "encrypt at the source… / …transmit encrypted… / …decrypt at the destination". Non commentata qui (è del capitolo 02).

**Slide "Homomorphic encryption"** (frame *00:00:03*, poi *00:07:19*). Schema: *User* con chiave pubblica $\kappa^{\text{pub}}_{\text{Hom}}$ → *Encrypted Query* → *Database* nel cloud; riquadro "Search the Database in Encrypted State, \*does not require user key to answer the query", "encryption *in use*"; *Encrypted Search Result* → *Decryption* con $\kappa^{\text{priv}}_{\text{Hom}}$ → *Search Result*. Testo:

> Homomorphic encryption allows data processing to be performed *directly on* encrypted data, without need for processors (e.g. remote third-party cloud services) to access any plaintexts.
>
> Mathematically, the encryption scheme commutes with mathematical and/or DB-query operators.

**Slide "Homomorphic encryption (…in math jargon)"** (frame *00:07:15*, leggibile a *00:11:59*). Formule della slide:

$$Y_{1,2,\dots,n} = f_{\text{enc}}\left(X_{1,2,\dots,n} \mid \kappa^{\text{pub}}_{\text{Hom}}\right) \qquad Z = R_{\text{ops}}(Y_1, Y_2, \dots, Y_n)$$

$$f^{-1}_{\text{enc}}\left(Z \mid \kappa^{\text{priv}}_{\text{Hom}}\right) = R_{\text{ops}}(X_1, X, \dots, X_n)$$

e nel riquadro tratteggiato:

$$\begin{cases} f^{-1}_{\text{enc}}\left(f_{\text{enc}}\left(\blacksquare \mid \kappa^{\text{pub}}_{\text{Hom}}\right) \mid \kappa^{\text{priv}}_{\text{Hom}}\right) \equiv \mathbb{1} \\ \{f_{\text{enc}} \mid R_{\text{ops}}\} \equiv \mathbb{0} \end{cases} \implies f^{-1}_{\text{enc}} \circ R_{\text{ops}} \circ f_{\text{enc}} \equiv R_{\text{ops}}$$

(Nella slide il secondo argomento a destra è scritto $X$ invece di $X_2$: refuso.)

Il commento (*DI-03 @ 00:07:42-00:12:13*):
- l'utente ha $n$ dati $X_1, \dots, X_n$ riservati da caricare nel cloud; li cifra con la propria chiave pubblica e ottiene $Y_1, \dots, Y_n$, che carica in un database;
- il gestore del servizio non ha la chiave privata, quindi non ha accesso ai dati, ma esegue per conto dell'utente un'operazione $R_{\text{ops}}$: una query ("estraimi tutti i dati che soddisfano queste caratteristiche", magari con il criterio a sua volta cifrato) o un calcolo matematico. Esempi: terabyte di dati geografici, sismici, sanitari (radiografie, TAC) che l'utente non ha la capacità di elaborare in casa;
- $R_{\text{ops}}$ deve essere **compatibile** con la tecnica omomorfa usata: "come si dice in analisi funzionale", l'operatore di cifratura **commuta** con l'operatore $R_{\text{ops}}$. Cifrare, applicare l'operazione sui dati cifrati e decifrare il risultato equivale ad applicare l'operazione sui dati in chiaro;
- il provider restituisce $Z$, che per lui è illeggibile (probabilmente non sa nemmeno quale operazione gli è stata chiesta); l'utente decifra $Z$ con la chiave privata e ottiene $R_{\text{ops}}(X_1, \dots, X_n)$;
- esistono molti algoritmi omomorfi e non tutti funzionano con tutte le operazioni: alcuni permettono solo **somme e moltiplicazioni** ("proprio degli omomorfismi nel senso dell'algebra"), altri permettono query. È un campo "assolutamente innovativo", in fervente aggiornamento.

> **Nota aggiunta:** la notazione $\{f_{\text{enc}} \mid R_{\text{ops}}\} \equiv \mathbb{0}$ si legge come un commutatore nullo, $[f_{\text{enc}}, R_{\text{ops}}] = 0$, cioè $f_{\text{enc}} \circ R_{\text{ops}} = R_{\text{ops}} \circ f_{\text{enc}}$. In pratica l'operazione eseguita sui crittogrammi è spesso un'operazione **diversa** da quella che si vuole ottenere sui dati in chiaro: in RSA "da manuale" (senza padding) il prodotto dei crittogrammi corrisponde al prodotto dei messaggi; in Paillier il prodotto dei crittogrammi corrisponde alla **somma** dei messaggi. Esempio verificato per esecuzione (Python): RSA con $p=61$, $q=53$, $n=3233$, $e=17$, $d=2753$; $E(6)=824$, $E(7)=2369$, $824 \cdot 2369 \bmod 3233 = 2557$, $D(2557)=42 = 6 \cdot 7$. Gli schemi che ammettono sia somme sia moltiplicazioni in numero arbitrario si chiamano *fully homomorphic* (FHE).

Fra *00:12:34* e *00:12:44* il docente scorre velocemente il mazzo di slide e passano per un istante slide di altre lezioni ("Authenticity - Digital Signing", "PAdES - PDF advanced digital signature", "JWE - encrypted JWT", una serie sulle Privacy Enhancing Technologies: "What is Privacy", "PETs", "Differential Privacy", "t-closeness", "Bibliography on PETs"). Non sono commentate qui.

## 3. Calcolo quantistico: fenomeni e hardware (fuori esame)

*DI-03 @ 00:12:13-00:23:16*

> **Fuori esame.** "Su un dettaglio non ci saranno domande su questa parte di calcolo e meccanica quantistica, ovviamente non ci saranno, non è argomento del corso, solo per soddisfare qualche curiosità" (*DI-03 @ 00:13:37*). Nel 2026: "non ci saranno domande di meccanica quantistica né di calcolo quantistico" (Teams 1 @ 1:02:46). In DI-02 sulle slide dell'hardware quantistico: "non guardate le slide, non saranno oggetto d'esame" (*DI-02 @ 01:47:08*). Questa sezione è quindi solo contesto.

Il docente riprende la lezione precedente: si dice "quantistico" perché i calcolatori quantistici usano fenomeni non descritti da equazioni classiche. La microelettronica moderna lavora già su scala molecolare, dove i fenomeni quantistici esistono, ma il comportamento dei calcolatori classici è ancora descritto da equazioni classiche; i calcolatori quantistici sfruttano invece fenomeni spiegabili **solo** con la meccanica quantistica (*DI-03 @ 00:12:46-00:13:37*).

**Slide "Semi-classical phenomena"** (frame *00:12:48*): "Classical Physics (**CP**) is still valid, as Quantum Mechanics (**QM**) equations converge (on the average/expected values) to their "classical" analogue, as long as larger-than-atomic length scales (i.e. relatively "low" energies) are considered." e "Some "*mesoscale*" quantum phenomena (e.g. atomic/molecular bonds and semiconductors, capstone for Chemistry and Electronics) can still be described by purely CP equations (e.g. Maxwell's, Thermodynamics, …) plus a few additional assumptions made in place of purely *quantum* effects. This is what the semi-classical approach consists of." Immagini: esperimento della doppia fenditura, funzioni d'onda.

**Slide "Introducing Quantum Mechanics"** (frame *00:13:30*): "QM postulates that, at microscopic scales (atomic and below), interactions of the measurement devices with the phenomena themselves are no longer negligible. This must be mathematically accounted for."

**Slide "Quantum Entanglement"** (frame completo *00:17:35*):

> Entanglement happens whenever two or more quantum systems (e.g. two *qubits*) interact with each other. Their wavefunctions are linear combinations of *pure* states, like $\varphi(\mathbf{r}_A, t_A) \otimes \psi(\mathbf{r}_B, t_B) \equiv |A\rangle|B\rangle \neq |B\rangle|A\rangle$.
>
> However, the overall system $A \otimes B$ will not generally be in such a pure state, but rather in an **entangled** state, which may exhibit non-trivial quantum features and may be formalized by the following wavefunction / ket:
> $\Psi(\mathbf{r}_A, \mathbf{r}_B; t) \equiv |A, B\rangle \neq |A\rangle|B\rangle \equiv \varphi(\mathbf{r}_A, t) \otimes \psi(\mathbf{r}_B, t)$ (and, classically, $t_A \equiv t_B = t$).
>
> A gross analogy for quantum entanglement (and their tensor algebra) may be integer-number decompositions. For example, the number 37, which is a prime number (i.e. it is divisible by 1 and by itself only), can also be decomposed in a polynomial ring $\mathbb{Z}[x]$ (linear combination) as $37 = 22 + 15 = 11 \cdot 2 + 5 \cdot 3$, in two mutually coprime numbers (none of which is a prime number), yet neither 11, nor 5, nor 3, nor 2 divide 37.
>
> The same number may also be decomposed (measured) as $37 = 33 + 4 = 11 \cdot 3 + 2 \cdot 2$, which is yet a different way of observing the same ("entangled") number.
>
> Entangled states carry information within their wavefunction that can be extracted with several independent observations. For example, when observed/measured in a "former way" (e.g. from subsystem $A$'s point of view) and thus collapsed into an eigenstate of the overall system, it is still observable in a "latter way" (e.g. from subsystem $B$'s point of view), which collapses it into another eigenstate, whence it can yet be measured in the "former way", producing a different result.

Il commento a voce (*DI-03 @ 00:14:09-00:17:44*): in meccanica classica due palle su un biliardo (la rossa e la bianca, "per usare il gergo della goriziana") si descrivono come indipendenti che ogni tanto si scontrano; in meccanica quantistica sono delocalizzate su tutto il biliardo e lo stato del sistema non è il semplice accostamento dei due stati. L'analogia aritmetica: 37 è primo, ma si può scomporre in somme in modi diversi, ciascuno con divisori primi diversi che non dividono 37; questa molteplicità di "letture" è l'analogo del **entangled state** (stato ingarbugliato). Un insieme di qubit, poiché ciascuno non è mai solo 0 o solo 1, rappresenta una distribuzione di numeri, e questo permette di **accelerare** una serie di operazioni matematiche.

Verifica per esecuzione (Python) dell'esempio numerico: 37 è primo; $22 + 15 = 37$ con $22 = 2 \cdot 11$, $15 = 3 \cdot 5$, $\gcd(22, 15) = 1$, nessuno dei due è primo; $33 + 4 = 37$ con $33 = 3 \cdot 11$, $4 = 2 \cdot 2$, $\gcd(33, 4) = 1$, nessuno dei due è primo; nessuno dei fattori 2, 3, 5, 11 divide 37; $11 \cdot 2 + 5 \cdot 3 = 37$ e $11 \cdot 3 + 2 \cdot 2 = 37$. Tutto corretto.

Le slide sull'hardware scorrono rapidamente (*00:18:17-00:18:31*), senza commento puntuale:
- **"Qubits"** (*00:18:22*): "Qubits are quantum **2-states** systems which information equivalent to one "classical" bit can be represented within. Since 1990's many physical systems have been researched and prototyped for qubits: NMR, either solid- or liquid-state; nitrogen valence centres in diamonds; photonic devices (e.g. used in QKD); superconducting *transmons*; *anyons* (Majorana, Ising, Fibonacci); topological qubits (still highly experimental); ion traps; …". Sfera di Bloch, sovrapposizione $\frac{|0\rangle + |1\rangle}{\sqrt{2}}$, misura.
- **"Quantum dots and quantum wires"** (*00:18:24*): implementazioni ancora soggette a **errori**, quindi servono *quantum error correcting codes* (QECC, "e.g. Shor's"); servono qubit migliori per "intrappolarli" *at rest* (quantum dot) e *in transit* (quantum wire) e per l'aritmetica di base (porte quantistiche); i calcolatori quantistici che eseguono algoritmi classici devono curarsi solo degli errori di ampiezza ($\sim|\psi|$), quelli che eseguono algoritmi quantistici anche degli errori di fase ($\sim \arg\psi$).
- **"From quantum gates to quantum computing"** (*00:18:29*): porte quantistiche come operazioni reversibili (unitarie); porte universali; "Some mathematical problems that are exponentially "hard" to solve (i.e. *non-polynomial*, **NP**) with classical computers, may be reduced to sub-exponential (**BQP**) complexity on QCs". Tabella di porte con matrici: Pauli X (NOT), Hadamard, T, T aggiunta, phase-shift S, S aggiunta, Feynman (CNOT).
- **""Quantum" effort (and spending) worldwide"** (*00:18:31*): mappa degli investimenti pubblici (fonte qureca.com, 2023), "Global Quantum Efforts \$38.6b (estimate)".

> **Correzione:** nella slide "From quantum gates to quantum computing" la sigla **NP** è sciolta come "non-polynomial". NP significa *nondeterministic polynomial time*: problemi le cui soluzioni si **verificano** in tempo polinomiale. La fattorizzazione e il logaritmo discreto non sono nemmeno ritenuti NP-completi; BQP è la classe dei problemi risolvibili in tempo polinomiale (con errore limitato) da un calcolatore quantistico.

**Slide "QC: where are we at it?"** (frame *00:22:46*):
- governi e coalizioni spingono il QC: USA e Cina dall'inizio; 2020, prima comunicazione quantistica internazionale al G-20; progetti UE *Euro-QCI*, *QSAFE*, *OQTAVO*;
- progetti accademici: MIT, Yale, Chicago; in Italia ASI, CNR, PoliMi, Roma, L'Aquila, Napoli, Padova, Trieste, Banca d'Italia;
- "*Provable security* (1984): QC provides unbreakable security, *if implemented right*. In fact, it is **based on the Physics** laws (…as long as they're not disproven)";
- problemi pratici: i calcolatori quantistici attuali elaborano numeri piccoli (~100 bit); gli errori aumentano i costi; ecosistema frammentato, rischio di *vendor lock-in*; per le telecomunicazioni quantistiche, i *quantum repeaters* sulle lunghe distanze diventano nodi fidati che aumentano la superficie d'attacco ("entanglement swapping" come contromisura in ricerca); "the whole schema must be secured".

Il commento (*DI-03 @ 00:19:02-00:23:16*): grandi investimenti nel mondo e in Europa; "anche il mio datore di lavoro ha dei progetti". Oggi i calcolatori quantistici che funzionano bene lavorano con **poche decine di bit**, lontani dai 256 bit dell'AES e "infinitamente lontani" dai 2048-4096 bit di RSA, almeno stando ai dati pubblici; cosa facciano gli Stati nel segreto militare non lo sappiamo. Le aziende private più avanti pongono un rischio di **lock-in** analogo al cloud (tre giganti, due grandi, gli altri piccoli). È difficile perché un calcolatore deve dare risultati esatti sempre ("nessuno comprerebbe una calcolatrice degli anni 80 che sbaglia una divisione ogni mille") e il comportamento statistico su scala atomica produce errori; le tecniche di correzione rendono i circuiti più complessi, costosi, a temperature bassissime o superconduttivi: lo "smartphone quantistico" è lontano.

> **Nota aggiunta:** la slide dice "~100 bit", il docente "poche decine di bit". Per i qubit fisici le macchine pubbliche superano il centinaio (e alcune il migliaio), ma i qubit **logici** corretti dagli errori sono ancora pochissimi: è a questi che si riferisce il discorso sulla capacità di calcolo utile.

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 3 (entanglement)*

- Nel 2026 il docente riprende l'entanglement come fenomeno sfruttato dalla QKD: con due fotoni di uno stesso messaggio in fibra, lo stato non è solo la combinazione degli stati classici (polarizzazione orizzontale o verticale di ciascuno) ma comprende stati ingarbugliati che, misurati in un modo, collassano in uno stato noto e, rimisurati in un altro modo, danno risultati "non previsti". (Teams 2 @ 0:00:12-0:01:54)
- Ripete l'analogia del 37 ($22 + 15$, $33 + 4$) definendola "numerologia", da prendere "senza nessuna pretesa di esattezza o di attinenza col mondo fisico": serve a mostrare che bisogna ragionare in modo controintuitivo. (Teams 2 @ 0:01:54-0:03:56)

## 4. Dal calcolo quantistico alla crittografia: tre discipline

*DI-03 @ 00:18:32 e 00:23:16-00:33:54*

Il collegamento con la crittografia (*DI-03 @ 00:18:32*): **tutta** la crittografia si basa su problemi matematici facili da calcolare in un verso per chi cifra e difficili da invertire senza le chiavi.

**Slide "Quantum: from Computing to Cryptography"** (frame completo *00:34:00*; costruzione progressiva da *00:26:26*):

> 1. **Quantum Crypto-analysis**: implementation of QC algorithms capable of **defeating** current "classical" cryptographic algorithms.
>    - Shor's factorization and discrete log-finding algorithms can beat **public-key** cryptography (RSA, ECC);
>    - Grover's search algorithm can provably beat **symmetric** cryptography (AES);
>    - Hashes (and, to a certain extent, symmetric keys) may still resist current quantum crypto-analysis (as long as key lengths are increased).
> 2. **Post-quantum / quantum-safe Cryptography (PQC)**: the implementation of ciphers capable of resisting quantum crypto-analysis. Currently, a fundamental requisite for PQC is that ciphers are **computable by classical computers** as well (e.g. near-to-market software, IoT, smart devices, …).
> 3. **Quantum Key Distribution (QKD)**: applications of Quantum Communication channels to detect *whether* transmitted secrets (e.g. secret keys) have been eavesdropped *in transit* by a TA / man-in-the-middle (**MitM**). QKD exploits inherent quantum phenomena like quantum **entanglement**.

(Nella slide i due punti dopo i titoli sono trattini lunghi, resi qui con due punti.) Vignetta in stile pop art: "OH ALICE… YOU'RE THE ONE FOR ME" / "BUT BOB… IN A QUANTUM WORLD HOW CAN WE BE SURE?", con "$\psi^+$ or $\psi^-$?".

**1. Crittoanalisi quantistica** (*DI-03 @ 00:23:16-00:26:40*): algoritmi quantistici, eseguibili da calcolatori quantistici, che battono gli algoritmi classici. Teoremi "neanche recenti" dimostrano che RSA, alcune curve ellittiche, "persino alcuni algoritmi simmetrici, persino alcune funzioni di hash" possono essere battuti riducendo una complessità **esponenziale** a una **polinomiale**. In soldoni: con complessità esponenziale, allungando la chiave rendo impossibile all'avversario stare al passo anche raddoppiando la velocità del calcolatore; con complessità polinomiale, un calcolatore abbastanza veloce raggiunge comunque la chiave allungata. Sono gli algoritmi di **Shor** (chiave pubblica) e **Grover** (simmetrica).

Conseguenza: delle due ipotesi su cui poggia tutta la crittografia teorica vista finora (funziona finché l'algoritmo è robusto; funziona finché le chiavi segrete restano a chi le deve avere) la prima "sta cominciando a frantumarsi". "Quella fiducia che vi sto costruendo nel corso, ve lo devo dire, oggi è pesantemente minata da questo fatto": è il primo motivo per cui si parla di calcolo quantistico in un corso di digital trust (*DI-03 @ 00:25:33-00:26:40*).

> **Correzione:** l'algoritmo di **Grover** non porta la ricerca della chiave da esponenziale a polinomiale: dà un vantaggio **quadratico**, da $2^k$ a circa $2^{k/2}$ operazioni, che resta esponenziale. Per questo basta raddoppiare la lunghezza della chiave simmetrica (AES-128 → AES-256) e la slide stessa dice che hash e chiavi simmetriche "may still resist… as long as key lengths are increased". La riduzione da (sub)esponenziale a polinomiale vale per **Shor**, cioè per fattorizzazione e logaritmo discreto (RSA, curve ellittiche).

**2. Crittografia post-quantistica o quantum-safe** (*DI-03 @ 00:26:40-00:29:48*): poiché molti algoritmi classici saranno potenzialmente battuti da chi avrà calcolatori quantistici abbastanza potenti, servono **nuovi problemi matematici** con due caratteristiche:
1. **non essere battibili da calcolatori quantistici**: devono stare in una categoria di calcoli che un calcolatore quantistico non può eseguire più velocemente, cioè non può sfruttare l'entanglement per abbattere il tempo di un attacco a forza bruta; devono essere "dimostrabilmente resistenti". Un calcolatore abbastanza potente ci arriverà sempre, ma il tempo deve essere proiettato così lontano che "si farà prima a essere quanto-agili" e cambiare di nuovo algoritmo;
2. "ed è qui che spesso le persone si confondono": gli algoritmi post-quantum **non devono essere eseguiti da calcolatori quantistici**. Shor e Grover li può eseguire con successo solo un calcolatore quantistico; un algoritmo quantum-safe "lo deve poter eseguire il calcolatore di mia nonna", lo smartphone, la smart card, la carta d'identità, la carta di pagamento, perché deve essere usabile **oggi**. Sono "algoritmi assolutamente classici" basati su un problema matematico non (dimostrabilmente) abbattibile da un calcolatore quantistico.

**3. Distribuzione quantistica delle chiavi** (*DI-03 @ 00:29:48-00:33:54*): vedi sezione 8.

Riepilogo del docente (*DI-03 @ 00:33:16*): la prima e la terza disciplina sfruttano fenomeni quantistici (serve un calcolatore quantistico per la crittoanalisi, un canale quantistico, satellitare o in fibra, per la QKD); la seconda no, è un algoritmo classico che si usa su dispositivi classici di oggi **per difendersi** da calcolatori quantistici.

> **Il problema concreto alla base della post-quantum (possibile domanda d'esame).** Ricostruito con le parole del docente (*DI-03 @ 00:18:32, 00:24:26-00:29:48, 00:39:06-00:40:12*; Teams 1 @ 1:22:20-1:23:27; Teams 2 @ 0:21:36-0:29:39):
> - tutta la crittografia poggia su problemi matematici **facili in un verso e difficili da invertire** senza la chiave, e funziona **finché l'algoritmo è robusto**;
> - per la crittografia **a chiave pubblica** (RSA: fattorizzazione; curve ellittiche: logaritmo discreto) è dimostrato (Shor) che un calcolatore quantistico abbastanza grande risolve il problema inverso in tempo **polinomiale**: allungare la chiave "può darci qualche anno in più, ma non potrà risolvere il problema", bisogna **cambiare algoritmo**;
> - per **simmetrica e hash** (Grover) basta, per ora, **allungare** chiavi e digest (AES-256, SHA-2/SHA-3 a 256 o 512 bit);
> - servono quindi algoritmi basati su **problemi matematici diversi** (reticoli, hash, codici…) che siano resistenti alla crittoanalisi quantistica ma **eseguibili oggi su calcolatori classici**, fino alle smart card;
> - l'urgenza è data dall'attacco **harvest now, decrypt later** (sezione 6): i dati rubati oggi, protetti da crittografia classica, saranno attaccabili quando l'avversario avrà il calcolatore quantistico, quindi la migrazione (cripto-agilità) va completata **prima**;
> - la migrazione è difficile soprattutto dove l'algoritmo è "nel silicio" (smart card, POS, gate): nei chip che fanno RSA "non c'è la microelettronica" per fare un calcolo diverso, bisogna sostituire carte e lettori.

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 4 (le tre accezioni di crittografia quantistica)*

- Nel 2026 il docente ribadisce le tre accezioni: **crittoanalisi quantistica**, un algoritmo quantistico eseguibile solo da un computer quantistico per battere un algoritmo classico; **crittografia post-quantistica o quantum-safe**, un algoritmo tipicamente classico, eseguito su smartphone, laptop, software o servizio web, che resiste (o almeno in teoria può resistere) alla crittoanalisi quantistica; **QKD**. (Teams 2 @ 0:03:56-0:05:45)

## 5. Standard post-quantum: NIST FIPS 203, 204, 205 ed ETSI

*DI-03 @ 00:33:54-00:36:43*

**Slide "Quantum-safe algorithms"** (frame completo *00:36:14*):

> **FIPS 203, 204, 205**: `https://csrc.nist.gov/projects/post-quantum-cryptography/`
>
> First international standards on PQC for encryption and digital signing. Based on 4 rounds of peer-review, which started in year 2017 by an initial submission of 69 proposed algorithms:
> - CRYSTALS **KYBER** (FIPS 203): module-lattice-based encryption
> - CRYSTALS-**Dilithium** (FIPS 204): module-lattice-based signing
> - **SPHINCS+** (FIPS 205): stateless hash-based signing
>
> IETF *Quantum Internet Research Group*
>
> ITU-T *Focus Group on Quantum … for Networks*
>
> ETSI *TR 106-619*: `https://www.etsi.org/deliver/etsi_tr/103600_103699/103619`
>
> European standard for guiding a *non-emergency* migration of IT systems towards quantum-safe schemes, in 3 phases: inventory compilation; planning; migration. For some assets, a *hybrid* migration (suboptimal) may be chosen, where the system supports both legacy and PQC.

A destra, uno schema dei candidati: *encryption (1 scheme)*: lattice-based (Crystals-Kyber in evidenza, FrodoKEM, NTRU, NTRU Prime, SABER; LAC, NewHope, Round5, Three Bears barrati), code-based (Classic McEliece, BIKE, HQC; NTS-KEM, LEDAcrypt, Rollo, RQC barrati), isogeny-based (SIKE); *signing (2 schemes)*: lattice-based (Crystals-Dilithium, FALCON; qTesla barrato), symmetric/hash-based (SPHINCS+, Picnic), multivariate-based (GeMSS, Rainbow; LUOV, MQDSS barrati).

Il commento (*DI-03 @ 00:33:54-00:36:43*): il problema è così sentito che nel 2017 il **NIST** (organo di standardizzazione tecnologica americano, ma di fatto internazionale per crittografia e sicurezza, già citato nel corso di Cybersecurity) ha fatto una *open call*, nello spirito degli algoritmi pubblici sottoposti per anni a peer review (guida [Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/README.md), capitolo 07, sezione 14). Sono stati proposti 69 algoritmi da tutto il mondo; nel 2024 ne sono stati selezionati tre, diventati gli standard **FIPS 203, 204 e 205**. Il primo [nome non udibile, nella slide Kyber] è un algoritmo di cifratura basato su un problema "matematico reticolare" (*lattice*, reticolo, una struttura algebrica); il secondo, **Dilithium**, è di firma digitale, anch'esso su reticoli; **SPHINCS+** è un altro algoritmo di firma "basato però su un'altra tipologia". Altri candidati scartati in prima analisi vengono rivisti e potrebbero diventare seconde scelte, perché non tutti gli algoritmi sono implementabili in tutti i casi: probabilmente ci saranno altri standard. Anche l'Europa, con l'**ETSI**, ha prodotto uno standard per guidare le organizzazioni verso una "criptoagilità quantistica", descrivendo i passi per prepararsi alla transizione.

> **Nota aggiunta (verificata):** i tre standard sono stati pubblicati dal NIST il 13 agosto 2024 con nomi definitivi diversi da quelli colloquiali: **FIPS 203 ML-KEM** (*Module-Lattice-Based Key-Encapsulation Mechanism*, da Kyber), **FIPS 204 ML-DSA** (*Module-Lattice-Based Digital Signature Algorithm*, da Dilithium), **FIPS 205 SLH-DSA** (*Stateless Hash-Based Digital Signature Algorithm*, da SPHINCS+). ML-KEM non è un cifrario "di cifratura" generico ma un **meccanismo di incapsulamento di chiave** (KEM): serve a stabilire una chiave simmetrica, esattamente il ruolo del key wrapping della sezione 1. La call NIST è del dicembre 2016, con scadenza delle proposte a novembre 2017; i 69 candidati sono quelli ammessi al primo round.

> **Correzione:** nella slide il documento ETSI è indicato come "TR 106-619", ma il link della slide stessa punta a **ETSI TR 103 619** (*Migration strategies and recommendations to Quantum Safe schemes*, 2020), che è il documento corretto.

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 5 (standard NIST ed ETSI)*

- Nel 2026 il docente parla di **quattro** standard, **FIPS 203, 204, 205 e 206**, con i nomi definitivi in grassetto viola nella slide (ML-KEM, ML-DSA, SLH-DSA, FN-DSA) al posto di quelli colloquiali (Kyber, Dilithium, SPHINCS+, Falcon): "nel 2024 sono stati pubblicati i primi tre e l'ultimo è uscito quest'anno". (Teams 2 @ 0:05:45-0:06:54)
- Come si seleziona un cifrario: pubblicato e "messo alla mercé" della comunità dei ricercatori, attaccato per anni, irrobustito sia matematicamente sia nell'implementazione, perché conta la robustezza dell'intero **schema**, non del solo algoritmo; il responso viene da università e imprese che dovranno usarlo e venderlo. Altri candidati in valutazione, probabilmente nuovi standard "intorno al 2027". (Teams 2 @ 0:06:54-0:08:20)
- ML-KEM è un algoritmo di **key encapsulation**, cioè a chiave pubblica per incapsulare chiavi simmetriche; ML-DSA e SLH-DSA sono di firma e usano due modelli matematici diversi fra loro e diversi da fattorizzazione (RSA) e logaritmo discreto su curve ellittiche. (Teams 2 @ 0:08:20-0:09:04)
- **FIPS 206** (FN-DSA): firma digitale scelta perché produce firme **più piccole** di ML-DSA, che genera firme "lunghe diversi kilobyte": tollerabile su computer e smartphone, non su smart card, SIM, dispositivi IoT o contactless alimentati via radio. (Teams 2 @ 0:09:04-0:10:23)
- ETSI: la norma (citata a voce come "ETSI 106 619") guida la strategia di migrazione: **inventario**, **pianificazione**, **migrazione**, con una fase intermedia **ibrida** (algoritmi classici e post-quantistici insieme) prima di abbandonare del tutto i classici. (Teams 2 @ 0:10:27-0:11:18)

> **Correzione:** FN-DSA (Falcon) non è "basato su un'altra metodologia matematica": è anch'esso **su reticoli** (reticoli NTRU), come ML-DSA; la differenza è la dimensione molto minore di firme e chiavi. Sulla data: a quanto risulta dalle fonti consultate, la bozza di FIPS 206 è stata inviata ad approvazione nell'agosto 2025 e la versione finale era attesa fra fine 2026 e inizio 2027; che sia "uscito quest'anno" (2026) non sono riuscito a verificarlo.

## 6. Harvest now, decrypt later

*DI-03 @ 00:36:43-00:52:29*

**Slide "Harvest-now-decrypt-later attack!"** (frame completo *00:43:34*):

> - According to Research community, symmetric algorithms and crypto hash functions shall start to be vulnerable around **2026**. Increasing keys'/digests' lengths *may* still counter that.
> - Public-key crypto may be vulnerable around **2029**. Increasing key lengths shall not work.
>
> Transitioning to PQC is a crypto-agility process that organisations need to complete before their relevant TAs can get quantum crypto-analytic capabilities (*Mosca's law*).

Sotto, una linea del tempo (fonte "BIS website"): "1994: Recognition that a functional quantum computer could break current cryptography"; "Today: Data are exposed to "harvest now, decrypt later" attacks"; "Standardisation process of post-quantum cryptography"; "Migration to post-quantum cryptography"; "Availability of a quantum computer"; "Data are protected".

**Cripto-agilità, ora concreta** (*DI-03 @ 00:36:43-00:42:56*). La cripto-agilità (capitolo 01, sezione 3) è "proprio il punto in cui ci troviamo noi oggi". Secondo il docente le ricerche dicono che, dato il trend tecnologico, "entro l'anno prossimo" (il 2026) i primi algoritmi **simmetrici e di hash** potrebbero diventare vulnerabili (risalire alla chiave simmetrica, oppure trovare un documento diverso che collide con l'hash: "quell'hash non è di quel documento… ti ho trovato quest'altro documento che ha lo stesso hash"); entro il **2029** anche i primi algoritmi **a chiave pubblica**. Differenza:
- per simmetrica e hash, **allungare** le chiavi (abbandonare AES-128, "oggi molto diffusa") e gli hash (512 bit) sposta in avanti il problema "quasi con lo stesso hardware e software di oggi";
- per la chiave pubblica, intorno al 2029-2030, l'allungamento potrebbe non bastare: un avversario con un calcolatore quantistico abbastanza potente in pochi anni ne avrebbe uno capace anche con la chiave allungata. Va **cambiato l'algoritmo**: "ecco perché dei tre standard NIST ben due sono standard di firma digitale".

Anche allungare una chiave "non è questione da poco". Nel software basta dire alla libreria (Bouncy Castle o altra) di allungare la chiave: fa gli stessi calcoli ma ci mette 3, 4, 6 volte di più, e se la navigazione diventa 3-6 volte più lenta perché la cifratura del canale TLS è più pesante è già un problema (rimando alle VPN del corso di Cybersecurity). Ma su smart card, carta d'identità, carta di pagamento, token USB, app sullo smartphone, chip dei POS, tarati per costare il meno possibile, potrei non avere abbastanza bit; e soprattutto "nei chip delle smart card che oggi lavorano con RSA non c'è la logica booleana, non c'è la microelettronica" per un calcolo diverso dalla fattorizzazione: bisogna buttare carte, POS, lettori e gate e distribuirne di nuovi. È l'esempio di cripto-agilità della lezione precedente, "solo che questa volta vi sto descrivendo una minaccia concreta… prossima" (*DI-03 @ 00:40:12-00:42:56*).

**L'attacco** (*DI-03 @ 00:42:56-00:51:50*). Pianificare con calma ("la minaccia è tra quattro o cinque anni, mi metto piano piano") significa avere già perso, per l'attacco **Harvest Now, Decrypt Later** (o *Crack Now, Decrypt Later*). Un avversario che oggi non ha un calcolatore quantistico (ammesso che sia vero: ci basiamo su dati pubblici, e cosa fa un attore statuale nei suoi laboratori militari "noi non lo sapremo mai finché non sarà troppo tardi"; scenari improbabili ma non escludibili nel contesto geopolitico attuale) si procura oggi:
- file cifrati che oggi non può decifrare;
- documenti firmati di cui non può falsificare la firma, né alterare il contenuto senza invalidarla, perché non può ricavare la chiave privata;
- documenti protetti da un hash di cui non trova collisioni.

Valgono "i tre mantra" di sicurezza teorica: l'hash è sicuro se trovare una collisione costa troppo; simmetrica e asimmetrica sono robuste se all'avversario costa troppo risalire alla chiave segreta (simmetrica o privata). L'avversario conserva i dati ("se li mette al pizzo, come si dice a Roma", "sotto ghiaccio") e quando avrà il calcolatore quantistico decifrerà, falsificherà firme o contenuti. Il punto è se quei dati avranno **ancora valore** in quel momento.

Esempio (*DI-03 @ 00:49:01-00:51:16*), "chiaramente una provocazione", la ricetta di un segreto industriale (il docente usa la Coca-Cola, poi dice "non nomino più un'azienda commerciale"): oggi l'avversario la ruba cifrata con AES-256 e non può usarla; fra quattro anni, con un calcolatore quantistico, estrae la chiave e la legge. Nel frattempo l'azienda si è adeguata al NIST e ha ricifrato la ricetta con Kyber: se l'avversario rientra fra quattro anni trova solo la versione quantum-safe e non riesce a romperla, "ma non gli serve", perché ha la copia rubata oggi e la ricetta non è cambiata. "È un attacco che verte sulla nostra vulnerabilità oggi per presentarci uno sfruttamento domani": l'exploit avverrà fra $n$ anni, ma la vulnerabilità c'è oggi, e ripararla domani non protegge i dati già rubati. "Ecco perché è così essenziale proteggersi oggi e migrare il prima possibile ad algoritmi quantum safe" (*DI-03 @ 00:52:29*).

> **Nota aggiunta:** le date della slide (2026 per simmetrica e hash, 2029 per la chiave pubblica) sono previsioni del docente e della fonte citata, non un consenso: Grover dà solo un vantaggio quadratico ed è difficilmente parallelizzabile, e il NIST continua a considerare AES-128 adeguato anche in ottica post-quantum (è il riferimento della categoria di sicurezza 1 dei FIPS 203-205). Nello stesso esempio il docente fa "bucare" AES-256, che però è proprio la destinazione raccomandata dalla roadmap della sezione 7: va letto come provocazione. La "**Mosca's law**" è la disuguaglianza di Michele Mosca: se $x$ è il tempo per cui i dati devono restare sicuri, $y$ il tempo per migrare e $z$ il tempo prima che esista un calcolatore quantistico rilevante, c'è un problema quando $x + y > z$. Il 1994 della linea del tempo è l'anno dell'algoritmo di Shor.

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 6 (harvest now, decrypt later)*

- Se non si parla di intelligenza artificiale si parla di crittografia post-quantistica: un tempo era il primo argomento, i recenti fatti sull'IA l'hanno portato "al secondo, alla moda", ma questo non significa che la minaccia sia al secondo posto. (Teams 2 @ 0:20:56-0:21:36)
- Detto così sembrerebbe un rischio del futuro. Il docente aggiunge che non servono 2048 qubit per battere RSA-2048: "un algoritmo quantistico che gira su un calcolatore quantistico di pochissime centinaia di qubit" potrebbe farlo in tempi ragionevoli. Il problema è che gli avversari si stanno **già procurando i dati**. (Teams 2 @ 0:21:36-0:23:17)
- L'attacco "non è nato col calcolo quantistico": è una strategia che esiste da quando esiste la crittografia nell'informatica ("arraffa ora, decifrerai dopo"). (Teams 2 @ 0:23:17-0:23:50)
- Condizione di successo esplicitata: l'attacco futuro conviene se, **al netto di quanto l'avversario avrà speso** per il calcolatore quantistico, rompere quei dati produce ancora valore per lui e impatto sull'organizzazione. Scenario "ottimista": anche se quando l'attore statuale avrà il calcolatore i difensori avranno completato la migrazione, la copia rubata oggi resta vulnerabile. (Teams 2 @ 0:24:56-0:28:43)
- Chi vende soluzioni di migrazione dice "è già troppo tardi" e "in realtà non sbaglia": ci sono molti leak noti, da fonti OSINT e "closint", di dati cifrati e firmati per cui oggi non c'è evidenza di sfruttamento ma che domani potrebbero essere attaccati. (Teams 2 @ 0:28:43-0:29:39)

> **Nota aggiunta:** la stima delle "pochissime centinaia di qubit" va precisata: le stime pubbliche più recenti per fattorizzare RSA-2048 (Gidney, 2025) parlano di circa un milione di qubit **fisici** rumorosi, corrispondenti a circa un migliaio e mezzo di qubit **logici** corretti dagli errori, per meno di una settimana di calcolo. L'ordine di grandezza in qubit logici è comunque molto inferiore ai 2048 bit della chiave, che è il punto del docente.

## 7. La roadmap NIST

*DI-03 @ 00:52:29-00:53:35*

**Slide "NIST PQC roadmap"** (frame *00:53:33*). Cinque riquadri con le migrazioni:
- **Hashing**: MD4, SHA-1 → SHA-2 256, SHA-2 512, SHA-3 256, SHA-3 512;
- **Symmetric encryption**: AES128 → AES256;
- **Key Exchange**: ECDH, RSA KE → ML-KEM (Kyber); "Under consideration: BIKE, HQC, McEliece";
- **Public-key encryption**: RSA OAEP → ML-KEM (Kyber);
- **Digital signing**: ECDSA, Ed25519, RSA PSS, RSA PKCS#1 1.5 → ML-DSA (Dilithium), SLH-DSS (Sphincs+); "new additional round: Inc CROSS, SQiSign, HAWK, PERK, Mayo".

A sinistra: "NIST proposed timeline: **2030** All existing public-key & 128-bit symmetric/hashing methods to be deprecated. To be removed from FIPS by **2035**."

Il commento: il NIST ha prospettato i cambiamenti per firma, cifratura a chiave pubblica, scambio delle chiavi, cifratura simmetrica e hashing. Per l'hash non serve ancora un algoritmo post-quantum: basta passare a 256 o 512 bit; per la simmetrica, per il momento, da AES-128 ad AES-256; per cifratura a chiave pubblica e firma serve **cambiare algoritmo** (Dilithium, SPHINCS+), con un problema di cripto-agilità particolarmente rilevante perché si basano su aritmetiche totalmente diverse (*DI-03 @ 00:52:29-00:53:35*).

> **Correzione:** nella slide "SLH-DSS" va letto **SLH-DSA** (FIPS 205).

> **Nota aggiunta (verificata su fonte secondaria):** la "NIST proposed timeline" corrisponde alla bozza **NIST IR 8547** (dicembre 2024, *initial public draft*): gli algoritmi a chiave pubblica quantum-vulnerabili con sicurezza a 112 bit (per esempio RSA-2048) diventano *deprecated* dopo il 2030 e **tutti** quelli quantum-vulnerabili (RSA, ECDSA, EdDSA, ECDH) *disallowed* dopo il 2035. La bozza non depreca AES-128 né SHA-256: la dicitura "128-bit symmetric/hashing methods to be deprecated" della slide non trova riscontro nella fonte NIST che ho potuto consultare. Il NIST la chiama "proposta" e non "imposizione".

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 7 (roadmap NIST)*

- Il docente legge la timeline come obbligo per le aziende americane: entro il 2030 tutte le chiavi pubbliche esistenti e gli algoritmi simmetrici e di hash a 128 bit deprecati, entro il 2035 rimossi dagli standard. Obiettivo: una fase ibrida che parta possibilmente **prima del 2030** e si concluda **entro il 2035**. (Teams 2 @ 0:29:39-0:30:23)
- Ripete le migrazioni della slide: MD5 e SHA-1, "già oggi non sicuri", verso SHA-2 e SHA-3 a 256 e 512 bit; AES-128 → AES-256; scambio e incapsulamento di chiavi (curve ellittiche, RSA) → ML-KEM "o altri algoritmi che potrebbero essere standardizzati entro il prossimo anno"; firme (curve ellittiche, RSA, Ed25519, "usato in moltissimi tipi di criptovalute") → ML-DSA, FN-DSA, SLH-DSA o altri in valutazione. (Teams 2 @ 0:30:23-0:31:44)
- Chi ha il calcolo quantistico: per svariati anni non avremo uno smartphone quantistico; i calcolatori saranno di grandi atenei, grandi progetti (in Europa ce ne sono tre), grandi aziende come IBM, e forse di comparti difesa di cui non sappiamo. Gli errori di fase fanno esplodere i costi perché accanto a ogni qubit rumoroso va costruito un sistema che riduce il rumore: oggi, secondo la ricerca pubblicata, circa un centinaio di qubit; "ogni tanto si legge su Internet che è già stato battuto, poi si scopre che non è vero… c'è parecchia hype e parecchia fuffa". (Teams 2 @ 0:31:44-0:33:59)

## 8. Quantum Key Distribution (QKD)

*DI-03 @ 00:29:48-00:33:54 e 00:53:35*

Nella panoramica (*DI-03 @ 00:29:48-00:33:54*), "di questo ne parleremo poco, perché c'è poco tempo": la QKD riguarda canali di comunicazione realizzati con fenomeni quantistici, come la propagazione della luce, e dà una garanzia in più: **sapere se qualcuno ha spiato** l'informazione. Come per la chiave pubblica, questi metodi elaborano pochissimi qubit alla volta, quindi sono adatti a piccole quantità di dati come le **chiavi**. Si usa la QKD per scambiare una chiave simmetrica: Alice e Bob, insieme e con un metodo statistico, verificano se qualche fotone è stato alterato, perché un'osservazione di Eva avrebbe fatto collassare lo stato quantistico di alcuni fotoni. Se c'è la prova che qualcuno l'ha vista, la chiave si butta e se ne scambia un'altra, finché non si ha la dimostrazione che Eva non l'ha presa; a quel punto si usa l'algoritmo simmetrico. È la soluzione al problema classico della simmetrica (scambiare la chiave su un canale sicuro), con una dimostrazione "non più tecnica ma fisico-matematica". Canali: satelliti o fibre ottiche.

**Slide "Quantum Key Distribution (QKD)"** (frame *00:53:49*, mostrata solo di passaggio: "sulla quantum key distribution… credo di avervi detto abbastanza, quindi non mi dilungo", *DI-03 @ 00:53:35*). Testo:

> QKD allows to confidentially communicate a small secret, e.g. a secret key, across a quantum communication channel so that, in the event of a MitM attack, Alice and Bob acknowledge "*eavesdropping* by *Eve*" because of that has likely collapsed the entangled state of the transmitted qubits. In such a case, Alice and Bob can eventually drop the secret without even starting to use it (for key wrapping).
>
> Alice sends Bob a message whose qubits encode both the secret to be exchanged and additional random data. Bob communicates some plaintext to Alice after having received all the information. Failure to match the two indicates eavesdropping may have happened, altering the sent qubits' originally prepared *singlet* states.

Schema: Alice e Bob con QRNG, canale quantistico, canale pubblico, Eve nel mezzo, rivelatori rettilineo e diagonale con PBS e rotatore; codifica della polarizzazione (0° e 45° = 0, 90° e 135° = 1). Tabella:

| | | | | | | |
|---|---|---|---|---|---|---|
| Alice random bits | 0 | 1 | 1 | 1 | 1 | 0 |
| Bob's bit values | 1 | 1 | 0 | 1 | 0 | 0 |
| Bob tells Alice the chosen basis | Rect. | Diag. | Diag. | Diag. | Diag. | Rect. |
| Alice tells Bob the bits to keep | | ☺ | | ☺ | | ☺ |
| Shared sifted key | - | 1 | - | 1 | - | 0 |

Verifica per esecuzione (Python) della tabella: con le basi di Alice ricavate dai simboli dei fotoni inviati (diagonale, diagonale, rettilinea, diagonale, rettilinea, rettilinea) e quelle di Bob, le basi coincidono nelle posizioni 2, 4 e 6; lì i bit di Bob coincidono con quelli di Alice e la chiave setacciata è 1, 1, 0, come nella slide. Nota di lettura: la legenda in alto a destra (135° = 1, 45° = 0) è invertita rispetto alla tabellina di Alice (↗ = 1, ↖ = 0); la tabella è coerente con la seconda.

### Integrazione Teams 2026 (lezioni 2 e 3 2026)

*Sezione 8 (QKD): nel 2026 il docente la spiega per esteso*

- Rischio pratico: sulle lunghe distanze (centinaia o migliaia di km, oggi "praticamente non praticabile") alcune aziende propongono di mettere un **amplificatore** a metà strada. Ma è un ragionamento classico: un amplificatore classico in un canale quantistico diventa un punto attaccabile con un classico uomo nel mezzo. La forza della sicurezza quantistica è di essere "dimostrabile dalla fisica, un teorema del 1984": sicura non finché qualcuno trova un algoritmo che la batte, ma "fintanto che sono sicure le leggi della fisica". (Teams 2 @ 0:33:59-0:35:57)
- Il docente descrive una versione "molto molto semplice", la **BB84** degli anni '80, base di metodi più complessi che richiederebbero meccanica quantistica e ottica avanzata. Canali: fibre ottiche non amplificate di diverse decine di km, le stesse delle dorsali Internet e "sotto i marciapiedi delle nostre città", con trasduttori a singolo fotone e bande lontanissime dai Gbit/s; oppure satelliti a bassa quota (qualche decina di km). (Teams 2 @ 0:36:02-0:38:46)
- Il procedimento come lo racconta: Alice e Bob hanno un canale quantistico e uno classico (intercettabile); Alice invia fotoni, alcuni con il segreto e altri preparati apposta che non ne fanno parte; Alice comunica a Bob sul canale classico come orientare i polarizzatori; Bob misura, facendo collassare i qubit in bit, e invia ad Alice in chiaro un campione dei bit misurati; se le discordanze superano una **soglia**, o il canale era troppo disturbato o c'era Eva, e il segreto si scarta; sotto soglia, Alice indica a Bob le posizioni dei bit che compongono il segreto. (Teams 2 @ 0:38:46-0:45:22)
- Perché funziona: osservare un fotone significa interagire con esso (colpirlo con un altro fotone o farlo incidere su materia), quindi alterarlo; Eva può reimmettere un fotone "sintetico", e Bob può misurare per caso lo stesso valore (probabilità "non bassa"), ma ripetuto su molti fotoni di controllo l'effetto statistico emerge. Anche conoscere una parte della chiave è grave: se Eva conosce 100 bit di una chiave AES-256, la forza bruta si riduce ai 156 bit restanti (verificato: $256 - 100 = 156$). (Teams 2 @ 0:47:49-0:50:57)
- La QKD serve a scambiare chiavi simmetriche da usare poi con cifratura classica: Alice genera la chiave, non la usa, la invia via BB84; se sopra soglia la cancella e Bob non la userà mai. (Teams 2 @ 0:45:22-0:47:49)
- Su domanda di uno studente (probabilità che un attacco man-in-the-middle riesca in una QKD), Teams 3 si apre con un'**inversione dell'onere della prova**: in un attacco classico possiamo sapere che l'attaccante *poteva* esfiltrare dati senza prova che l'abbia fatto; con la QKD, se le discordanze superano la soglia Alice e Bob non sono certi che ci sia stata Eva (potrebbe essere un disaccoppiamento del canale), ma se restano sotto soglia sono **certi che nessuno** si è interposto. La QKD dà la *provable security* non dell'esfiltrazione ma della sua **assenza**. (Teams 3 @ 0:00:05-0:03:09)

> **Correzione:** nel protocollo **BB84** Alice **non** comunica in anticipo a Bob le basi di misura: se lo facesse sul canale classico intercettabile, Eva le conoscerebbe e potrebbe misurare senza disturbare i fotoni. Bob sceglie le basi **a caso**; **dopo** la misura Alice e Bob confrontano pubblicamente le basi (non i bit) e tengono solo le posizioni in cui coincidono (*sifting*), poi sacrificano un campione di bit per stimare il tasso d'errore. È esattamente ciò che mostra la tabella della slide 2025 ("BOB tells ALICE the chosen basis", "ALICE tells BOB the bits to keep"). Inoltre BB84 è un protocollo *prepare-and-measure* con singoli fotoni e **non usa entanglement**; i protocolli basati su coppie entangled sono di altra famiglia (E91, BBM92). Infine il 1984 è l'anno del protocollo di Bennett e Brassard; le dimostrazioni di sicurezza incondizionata sono successive (fine anni '90 e 2000).

## 9. Nuovo nel 2026: migrazione ibrida e attacchi di downgrade

*Contenuto di Teams 2 senza corrispondente in DI-03.*

### Integrazione Teams 2026 (lezione 2 2026)

*Sezione 9 (cripto-agilità post-quantum in pratica)*

- **Il caso fisico.** Ripresa delle carte: pianificare quando i chip non sono più sicuri, emettere da una certa data carte nuove, ridistribuire POS e varchi doganali in grado di leggerle e dismettere i vecchi algoritmi solo quando la distribuzione fisica è completa; la data di scadenza dell'ultima carta vecchia garantisce che anche chi per pigrizia non l'ha cambiata non sia più un vettore d'ingresso. (Teams 2 @ 0:11:18-0:13:52)
- **Il caso senza vincoli fisici.** Bisogna poter **ricifrare o rifirmare** i dati passati con i nuovi algoritmi senza invalidare la **catena di custodia**, e assicurarsi che tutte le controparti supportino gli algoritmi nuovi. Esempio: in cloud SaaS "clicco un bottone", di notte il fornitore migra tutto e la mattina sono quantum-safe; la seconda controparte è a posto, la terza "non legge più niente" perché nella sua pipeline c'è un prodotto più vecchio che "gli farebbe marameo". (Teams 2 @ 0:13:52-0:15:32)
- **Inventario.** Si scopre il problema tardi, dopo aver avviato un processo irreversibile, perché l'**inventario** non era completo: componenti trattati come scatole nere. Esempio: il software di fatturazione elettronica in cloud, aggiornato ogni settimana, smette di funzionare perché il fornitore ha un vecchio storage che non supporta la nuova crittografia e non può più apporre i sigilli elettronici. Opzioni: restare classici, restare ibridi, cambiare fornitore o aspettarlo, finendo "al ricasco" della cripto-agilità del peggior fornitore della filiera. (Teams 2 @ 0:15:32-0:17:13)
- **Ibrido.** Una pipeline ibrida supporta algoritmi classici e post-quantistici e usa quello supportato dalla controparte. Consente di aggiornare gradualmente senza bloccare la produzione, testando i prodotti man mano; solo quando tutta la pipeline, tutti i fornitori e gli stakeholder supportano la PQC si disabilitano gli algoritmi classici e si **revocano i certificati classici**. (Teams 2 @ 0:17:13-0:19:10)
- **Il rischio: l'ibrido che diventa permanente.** "È proprio il rischio che l'ibrido diventi permanente": la crittografia ibrida non è pensata come transizione a lungo termine né definitiva. Finché c'è crittografia classica nella catena si è vulnerabili come all'inizio, perché l'avversario con un calcolatore quantistico passerà dalla parte classica con un **downgrade attack**, cioè forzerà un sistema che supporta entrambi i mondi a usare l'algoritmo meno sicuro. Ci si potrà dire al sicuro solo a migrazione quantum-safe completata. (Teams 2 @ 0:17:29-0:20:53)

> **Nota aggiunta:** nei protocolli reali (per esempio lo scambio di chiavi ibrido X25519 + ML-KEM già in uso in TLS 1.3) "ibrido" ha spesso anche un secondo significato: combinare **insieme** un algoritmo classico e uno post-quantistico, così che l'attaccante debba romperli entrambi. In quel caso l'ibrido protegge anche da un eventuale difetto del nuovo algoritmo; il rischio di downgrade descritto dal docente riguarda la **negoziazione**, quando un sistema accetta di ripiegare sul solo algoritmo classico.

## 10. Digital trust: due problemi pratici ancora aperti

*DI-03 @ 00:54:05-00:58:07*

**Slide di sezione "Digital Trust"** (*00:55:10*). Il docente annuncia: "adesso abbiamo tutte le basi teoriche per trattare l'argomento di oggi, cioè l'argomento di questo insegnamento, che è il digital trust e poi da lì andremo sulle identità digitali".

Ricapitola: la crittografia presidia anche integrità e soprattutto autenticità (origine del dato), da cui le firme digitali; tutti gli algoritmi (hash, simmetrica, chiave pubblica e le firme che li combinano) funzionano **finché l'algoritmo è robusto** (e il calcolo quantistico ne è un caso concreto di minaccia) e **finché le chiavi segrete restano segrete**: la simmetrica condivisa solo fra chi deve averla, la privata solo dal titolare. "Se questo assunto muore, crolla tutto il castello della teoria". Serve la **crittografia applicata**: ci sono due problemi non ancora risolti senza i quali non si può usare realmente la crittografia (*DI-03 @ 00:54:37-00:55:45*).

**Slide "Two yet unravelled practical issues"** (frame *00:56:51*, unico punto visibile): "1. Can we really **trust** the authenticity of **public keys**? Rephrasing: *Is Alice's public key really Alice's?*". Il secondo punto non compare in nessun frame.

Il primo problema (*DI-03 @ 00:55:45-00:58:07*): in tutti gli schemi Bob usa "la chiave pubblica di Alice" per verificare che il messaggio sia di Alice, "bellissimo, ma chi gli ha detto che la chiave pubblica di Alice è di Alice?". Carl, l'avversario, attacca il repository pubblico da cui Bob prende le chiavi e scrive sotto il nome di Alice la propria chiave pubblica. Da quel momento:
- chi cifra documenti riservati per Alice li cifra in realtà per Carl, che li legge con la sua chiave privata;
- Carl può firmare qualunque documento o contratto "nel nome di Alice" e tutti, convalidando con la chiave che credono di Alice, crederanno che l'abbia firmato lei.

"Questo la crittografia non ci aiuta, non ci spiega come fare": è un **problema di fiducia**.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 10 (autenticità delle chiavi pubbliche)*

- Nel 2026 il docente riformula l'assioma della convalida: "poiché il documento risulta firmato con una chiave privata che non conosco, ma usando questa chiave pubblica dimostro che è stato cifrato con la chiave privata corrispondente, siccome quella chiave pubblica è di Alice deduco che solo Alice può averlo firmato". Questo ragionamento "fa acqua dal punto di vista pratico in almeno due punti", il primo dei quali è proprio l'appartenenza della chiave pubblica. Carl può anche "travestirsi digitalmente" da Alice e passarti la sua chiave su un canale non sicuro. (Teams 3 @ 0:03:15-0:06:23)
- Lo stesso vale per le **identità digitali**: davanti ho un account, un indirizzo email con scritto Mario Rossi e la sua foto, post che "sembrano Mario Rossi", ma non sono certo che sia lui; mi affido a uno **schema di identificazione elettronica** certificato da un terzo che l'ha identificato a monte. Le due tematiche del corso sono i **servizi fiduciari** e le **identità digitali**, entrambe realizzate con crittografia a chiave pubblica "pratica, reale, applicata": oltre a chiavi ben custodite e algoritmi robusti servono schemi di firma e cifratura che garantiscano la catena della fiducia, tipicamente tramite un terzo soggetto. (Teams 3 @ 0:08:35-0:09:58)

## 11. Dai testimoni ai notai al digital trust

*DI-03 @ 00:58:07-01:04:31*

**Slide "From witnesses, to notaries, to Digital Trust"** (frame completo *01:03:51*):

> - Since ancient times, when people from different villages had to come to agreements (e.g. marriage), they used to call on somebody from a *third*, independent village, who was either **trust**ed directly by both individuals, or by two trusted representatives of theirs, each from either village, so that he would witness that the agreement had, in fact, been settled.
> - In Merovingian Italy (ca. V-VIII century A.D.), trust relationships related to feudal matters became so complex that Lombards scaled up a solution, so that what were an issue to many would become an opportunity to a few: notaries were born. Their task was, under a compensation, *to note down facts* (e.g. signing a deed) making them official, effective, and/or binding *by law*. Notaries' guilds were instituted. Nobody, not even foreigners, was able to **repudiate** facts that had been such *noted down*.
> - In cyberspace, *digital trust* is a matter of IT systems acknowledging the integrity and authenticity of other electronic data/systems (also of those which they are communicating with for the first time) and that their digital counterparts can*not* repudiate. It is also a matter of electronically identifying the legal and natural persons that *may* correspond to those digital evidences (e.g. by means of a digital identity or *persona*), so that actions deriving from the process have a mutually accepted legal value enabling online transactions (e.g. business).

Immagine: un logo "NOTARIUS LEX" con bilancia e libro.

Il commento (*DI-03 @ 00:58:07-01:04:31*): l'esempio dei matrimoni fra Montecchi e Capuleti: si chiamava un terzo indipendente, magari "il cugino di mio zio" sposato con un parente dell'altra famiglia, di cui entrambe le parti si fidavano; se il terzo diceva che il matrimonio era avvenuto, era avvenuto. Nel Medioevo i Lombardi trasformarono il problema in un'opportunità commerciale: "perché non farlo per soldi?", e nacquero i **notai**, persone che per legge erano fidate *super partes*: un fatto annotato da loro aveva valore di legge e nessuno poteva **ripudiarlo**. È il primo **servizio fiduciario**: due parti che non si conoscono si affidano a un terzo di cui entrambe si fidano, perché lo pagano (i servizi fiduciari digitali sono in larga parte a pagamento) o perché c'è una legge che lo dice (il notaio è un pubblico ufficiale iscritto a un ordine con un codice deontologico).

Nel digitale funziona allo stesso modo ed è essenziale perché facciamo affari con controparti che non conosciamo. Esempio: un acquisto da 7 euro su una piattaforma polacca, venditore canadese, merce partita dalla Cina, spedizioniere di un altro paese, dogana: "li ho pagati tutti, mi sono di tutti fidato", e lo faccio "perché c'è un digital trust sotto". Fiducia significa saper **identificare** le persone, così che se commettono un reato si possano perseguire. Il docente cita il **Digital Markets Act** e il **Digital Services Act**, regolamenti europei che, come il GDPR, si applicano anche a soggetti esteri che operano in Europa e impongono fra l'altro una rappresentanza legale o una sede nell'UE: "banalmente ti mando la Guardia di Finanza". Per farlo devo identificarti digitalmente: sapere che dietro il marketplace c'è un'azienda con sede legale in Irlanda, Lussemburgo o Olanda e rivolgermi all'autorità giudiziaria di quel paese. "Però sto divagando" (*DI-03 @ 01:02:05-01:04:31*).

> **Nota aggiunta:** la descrizione dei due regolamenti è approssimativa. Il **DSA** (Reg. UE 2022/2065) riguarda i servizi intermediari e impone a quelli non stabiliti nell'UE di nominare un **rappresentante legale** in uno Stato membro (art. 13). Il **DMA** (Reg. UE 2022/1925) riguarda i grandi *gatekeeper* delle piattaforme e la concorrenza, non in generale gli operatori che vendono online.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 11 (dai testimoni ai notai)*

- Stessa analogia del matrimonio fra villaggi ostili e dei notai lombardi "nel basso Medioevo". Termine nuovo: i soggetti che si fidano di ciò che il terzo ha annotato sono le **parti facenti affidamento sulla certificazione**, in inglese ***relying parties***, i "quarti soggetti" che non possono ripudiare perché, se si fidano del soggetto centrale, devono fidarsi di ciò che ha annotato. (Teams 3 @ 0:06:27-0:08:35)

## 12. La fiducia nell'era digitale: soggetto, CA, prestatore di servizi fiduciari

*DI-03 @ 01:04:31-01:09:47*

**Slide "Trust in the digital age"** (frame completo *01:09:24*):

> - To make Cryptography actually work, public keys need be bound to a **subject**: either a natural person, a legal person, or an IT system (e.g. a server, a software, a website, …).
> - To trust such a binding in the first place, I need to trust that subject can keep the corresponding private key private. As a matter of fact, when different alien parties are involved (like in internet-age communities spread worldwide), this may hardly be achieved with high confidence.
> - If that's not the case, then I need a **certification authority** (**CA**) that I *digitally trust*, i.e. whose public CA key I can trust is solely bound to. To trust the subject in this case, it's enough for the CA to **issue** a (public-key) **certificate** stating, *notarying*, the binding between the subject and its public key.
> - We introduced two things: CAs and public-key certificates. To actually work, we need much more: one or more CAs and the digital certificates they issue, i.e. a **public key infrastructure** (**PKI**). … But let's go step by step.

Fumetti: "e.g., Alice", "e.g., Big Company Ltd.", "e.g.: my iPhone, www.mydomain.com, …". (Nel terzo punto, "notarying" è fra trattini lunghi nella slide, resi qui con virgole.)

Il commento (*DI-03 @ 01:04:31-01:09:47*):
- serve sapere con certezza a chi appartengono le chiavi pubbliche, cioè identificare il **titolare** della chiave pubblica: nel gergo dei certificati il **soggetto** (*subject*); nella normativa AgID si chiama **titolare del certificato** (il docente dice di aver contribuito a quella normativa);
- il soggetto può essere una **persona fisica** (Alice Bianchi, nata a Terni, codice fiscale…), una **persona giuridica** (Alice SRL, sede a Poggio Mirteto, partita IVA…) o un **sistema tecnologico** (un sito web, un nome macchina, il server di posta, il database, il NAS);
- con milioni di soggetti (tutti i siti visitati in una giornata, ciascuno con una chiave pubblica, e le chiavi di sessione di cui chiedeva lo studente a inizio lezione arriveranno più avanti) non posso fidarmi di ciascuno in senso tradizionale: devo fidarmi di una **terza parte**, un **fornitore di servizi fiduciari** (*Trust Service Provider*), che nel gergo dei certificati si chiama **Certification Authority (CA)**;
- uso dei termini: "trust service provider" (prestatore di servizi fiduciari) quando si intende l'accezione amministrativa e organizzativa, tipicamente un'azienda che lo fa di mestiere dietro compenso; "certification authority" per la componente tecnologica; si trova anche "CA amministrativa" per l'azienda;
- funzionamento: Alice va dal TSP e chiede "una prova opponibile a terzi" da mandare a Bob, che non la conosce: "se non ti fidi di me, che è normale, ti devi fidare della Certification Authority". Se Bob si fida della CA, quando la CA emette un certificato che dice "questa è la chiave pubblica di Alice" non è più Alice a sostenerlo, è la CA, "il notaio della situazione".

Avvertenza (*DI-03 @ 01:09:14*): in Italia e in Europa esiste anche un servizio fiduciario chiamato **notaio digitale** (*digital notary*): è un altro servizio. Il docente usa "notaio" solo come analogia, "però non vi sto descrivendo il servizio di notaio digitale e né lo farò nel corso".

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 12 (soggetto e CA)*

- Esempi del soggetto nel 2026: per una persona fisica bisogna distinguere Alice Verdi nata nel '72 a Vigevano da quella nata nel '98 a Bogotà; per una persona giuridica Alice SRL registrata in Italia da quella registrata a Malta da un attore della minaccia; per un sistema, il sito su cui inserisco le credenziali (richiamo a phishing e *typosquatting*): anche un dominio scritto correttamente potrebbe non essere autentico, serve "un livello di trust ancora superiore". (Teams 3 @ 0:09:58-0:11:26)
- "Sarebbe un corto circuito" se fosse il soggetto stesso a garantire la propria chiave: "non puoi dirmelo tu stesso, me lo dice il notaio digitale, tra virgolette". Di nuovo la distinzione: in Italia il servizio di **notariato digitale** assolve in digitale ai compiti che per legge spettano ai notai e lo svolgono i notai, mentre una CA "fa un altro mestiere". Il compito della CA è certificare che la chiave pubblica di Alice è di Alice tramite **certificati a chiave pubblica**; quando dietro il rilascio c'è un insieme di CA si parla di **PKI**, "l'argomento che ci assorbirà nella lezione di oggi". (Teams 3 @ 0:11:26-0:13:53)

## 13. Il certificato digitale e le sue tre caratteristiche

*DI-03 @ 01:09:47-01:21:47*

**Slide "Digital (and electronic) certificates"** (frame *01:16:10*, ripresa a *01:32:32*):

> A digital certificate is an 'electronic document' (according to **eIDAS Regulation**; in some contexts even a '*documento informatico*', according to Italian CAD) that:
> 1. is encoded in a pre-agreed format/syntax, e.g. ITU-T **X.509** = RFC-5280 standard;
> 2. it binds a property $\mathcal{P}$ to the identifiable data of a personality, the certificate's **subject**;
> 3. it is digitally signed by (i.e. its digest is encrypted via the private key of) a "certification authority", the certificate's **issuer**.
>
> Digital certificates always include their digital signature (otherwise, we talk about *pre-certificates*).
>
> X.509 taxonomy has 2 types of *digital* certificates:
> - **public-key** cert, binding a public key $\kappa^{\text{pub}}_{\text{subj}}$ to a **subject**;
> - **attribute** cert, binding an attribute $\mathcal{A}$ to its **holder**.
>
> **eIDAS Regulation** has 3 types of *electronic* certificates (+ **qualified** variants, which we'll see later): they are *electronic attestations*, respectively *linking*:
> - c. for e-signatures: e-signing by **signatory** natural person, confirming at least name & pseudonym;
> - c. for e-seals: e-sealing by a legal person (**seal creator**), confirming at least its legal name;
> - web-auth. c. (**WAC**): website to a natural/legal person subject & allowing anyone to authenticate it.

(Nella slide i punti 1-3 sono separati dalle spiegazioni con trattini lunghi, resi qui con virgole.) Al centro lo schema del contenuto: *public key / attribute(s)*, *Issuer DN*, *Subject DN / Holder DN*, *issuing CA's digital signature*; ai lati un certificato con chiave (verde) e uno con attributi, ciascuno con il tempietto blu (la CA) e l'icona del soggetto.

Il docente insiste sulla terminologia: anche "esimi colleghi informatici" usano la parola impropriamente; dire "ti passo la chiave e sta nel certificato" è "altamente improprio… il modo migliore per non capire come funzionano i certificati" (*DI-03 @ 01:10:25*). Un certificato è "un file, né più né meno" con tre caratteristiche.

**1. Un formato standard riconoscibile da tutti** (*DI-03 @ 01:10:56-01:17:26*). Il formato usato nel "95%" dei certificati al mondo (stima sua) è **X.509**, standard dell'**ITU** (Unione Internazionale delle Telecomunicazioni) della fine degli anni '80, ancora vivo e aggiornato; è stato reso pubblico in un RFC, la **RFC 5280**, "talmente importante che lo cito come numero". Ogni pagamento o visita a un sito comporta lo scambio di **almeno due** certificati X.509; una pagina con 84 immagini da 20 fornitori diversi comporta almeno due certificati per ciascuna fonte; un pagamento con carta ne coinvolge almeno tre (quello nella carta, quello nel POS, quello del circuito: Visa, Mastercard, American Express). I documenti d'identità elettronici letti dai gate o dai lettori delle forze dell'ordine usano invece un altro formato, il **CVC** (*card verifiable certificate*, certificato verificabile in carta), "il restante 4,99%".

Il formato deve essere unico perché se non lo so leggere tutto ciò che contiene non ha valore; e l'applicazione deve **onorare** tutto ciò che c'è scritto. Caso vissuto dal docente: uno standard di autenticazione solido (SAML) implementato con la libreria open source più usata al mondo, gratuita, disponibile in tutti i linguaggi, che però non rende obbligatoria la verifica dei certificati in certi casi, perché programmata senza *security by design*. Se un certificato è revocato o scaduto la libreria non lo dice, e l'avversario sfrutta la vulnerabilità. "La risposta non può essere: ma quella è la libreria più usata al mondo. È una libreria insicura". Saper leggere il formato significa **fare ciò che lo standard dice** (rimando alla sicurezza applicativa della guida Cybersecurity).

**2. Lega una proprietà ai dati identificabili di un soggetto** (*DI-03 @ 01:17:26-01:19:35*). Non ad "Alice Rossi", di cui in Italia ce ne sono centinaia, ma ad Alice Rossi con codice fiscale RSSLCI82… H501: dati associati a un'identità. Le norme AgID dicono per esempio che nel certificato di firma elettronica qualificata deve esserci almeno il codice fiscale (o, in mancanza, altri dati previsti da uno standard europeo). Per una persona giuridica non basta "ACME" ("di società che si chiamano ACME, i cartoni del Coyote ce lo insegnano, ce ne sono tantissime"): servono SRL, sede, partita IVA, codice fiscale, numero di registro imprese; per una pubblica amministrazione italiana il **codice IPA**; per una macchina un nome unico almeno nel contesto organizzativo. Sono i dati **distintivi**: il **DN**, *Distinguished Name*, che distingue l'Alice Rossi di Vigevano da quella di Torino.

**3. È firmato digitalmente** (*DI-03 @ 01:19:35-01:21:47*). "Non esiste un certificato digitale senza firma digitale oppure la cui firma digitale non sia valida": "il certificato non era firmato" è una frase senza senso; al massimo la firma può essere scaduta. Nel mondo dei certificati per siti web esistono i **precertificati**, creati "a metà" e trasferiti senza firma per esigenze tecniche legittime, che non servono a nulla finché non vi si appone la firma. La firma è dell'**emettitore** (*issuer*): emettendo il certificato si assume la responsabilità, tecnica, amministrativa o giuridica, di ciò che c'è scritto, compresi i dati personali del soggetto, il che presuppone averlo **identificato** prima (allo sportello o davanti alla telecamera di un laptop).

> **Nota aggiunta:** X.509 è stato pubblicato per la prima volta nel 1988. La RFC 5280 (2008) non è la "pubblicazione" dello standard ITU ma il suo **profilo per Internet** (PKIX): definisce quali campi ed estensioni usare per certificati e CRL in Internet. Il docente lo precisa nel 2026 ("versione legata alle sole caratteristiche Internet"). I **precertificati** nominati sono quelli della *Certificate Transparency* (RFC 6962): la CA li registra nei log pubblici prima di emettere il certificato finale. Il caso di libreria SAML senza nome è un racconto del docente: non è identificabile dalla lezione.

> **Correzione:** i passaporti elettronici **usano X.509**: i certificati del firmatario del documento (*Document Signer*) e della CA nazionale (*CSCA*), con cui si fa l'autenticazione passiva dei dati del chip, sono X.509 secondo ICAO Doc 9303; i **CVC** si usano per l'*Extended Access Control*, cioè per autenticare il **terminale** che vuole leggere i dati protetti (impronte). Lo dice indirettamente lo stesso docente alla fine della lezione ("i profili dei certificati 509 dei passaporti elettronici del formato ICAO", *DI-03 @ 01:51:36*).

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 13 (il certificato digitale)*

- Un certificato è un "piccolo file" di pochissimi kilobyte, salvo i certificati post-quantum, che per la dimensione delle chiavi pubbliche possono arrivare a "qualche centinaio di kilobyte". (Teams 3 @ 0:14:13-0:14:43)
- Analogia del formato: come un'immagine JPEG data a un'applicazione che legge solo GIF. La raccomandazione ITU X.509 "è a pagamento", ma se ne trova una versione "stripped down", legata alle sole caratteristiche Internet, nella RFC 5280, "lo standard di riferimento". I certificati X.509 sono il 99% di quelli in informatica e quasi la totalità in Internet; l'unica tipologia diversa che il docente conosce è il CVC dei documenti d'identità e passaporti, "più light", perché X.509 sarebbe troppo complesso da verificare dentro il microchip. Ogni navigazione o transazione comporta la verifica di "una catena di 3, 4, 5, 6 certificati". (Teams 3 @ 0:14:43-0:17:20)

> **Nota aggiunta:** le dimensioni post-quantum standardizzate sono grandi ma non "centinaia di kilobyte": una chiave pubblica ML-DSA va da 1312 a 2592 byte e una firma da 2420 a 4627 byte; le firme SLH-DSA arrivano a circa 50 KB nelle varianti più grandi. Un certificato con ML-DSA pesa quindi qualche kilobyte o decina di kilobyte. Le centinaia di kilobyte riguardano chiavi come quelle di Classic McEliece, non standardizzate dal NIST. Le Raccomandazioni ITU-T in vigore, X.509 compresa, sono scaricabili gratuitamente dal sito dell'ITU.

## 14. Certificati a chiave pubblica e di attributo, contenuto e convalida

*DI-03 @ 01:21:47-01:31:56*

Nella tassonomia X.509 ci sono solo **due tipi** di certificati, secondo la proprietà asserita (*DI-03 @ 01:21:47*):
- **certificato a chiave pubblica**: quando qualcuno dice "mandami il certificato", 99 volte su 100 intende questo. Risolve il problema pratico della sezione 10: se mi fido di chi l'ha firmato, mi fido che quella sia la chiave pubblica di Alice. Una chiave pubblica "in chiaro", passata da qualcuno che l'ha avuta da un altro di cui si fida, che l'ha avuta da un altro ancora, non basta: "non c'è un digital trust a priori", l'unico modo è che la chiave sia contenuta in un certificato emesso da una CA (il "tempietto blu") di cui mi fido (*DI-03 @ 01:22:20-01:24:22*);
- **certificato di attributo**: il titolare si chiama ***holder***, possessore dell'attributo. In italiano si dice sempre **titolare** in entrambi i casi; X.509, "un po' vetusto", distingue *subject* (titolare di una chiave pubblica) e *holder* (titolare di qualunque altra cosa, gli **attributi**). "Non li vedremo quasi mai durante questo corso"; quando il docente dirà "certificato digitale" intenderà quello a chiave pubblica (*DI-03 @ 01:24:50-01:25:27*).

Fra *01:24:22* e *01:24:51* la trascrizione ha un buco di circa 30 secondi: l'inizio della definizione del certificato di attributo non è stato trascritto ([?]).

**Le quattro cose in un certificato** (*DI-03 @ 01:25:27-01:29:15*), valide anche per formati diversi da X.509 come i CVC:
1. la **chiave pubblica** del soggetto (o gli **attributi**, se è un certificato di attributo);
2. il **nome distintivo dell'emettitore** (*issuer*): Aruba, Banca d'Italia, un provider francese, DocuSign; per un'azienda anche la partita IVA internazionale, a volte sede legale, indirizzo, email e perfino un logo (esiste uno standard per includere il logo dell'emettitore o l'URL da cui recuperarlo);
3. il **nome distintivo del titolare** (*subject DN*): Alice, Rossi, codice fiscale, eventualmente luogo di nascita. I certificati nella **CIE** contengono nome, cognome, codice fiscale e data di nascita, non le altre informazioni stampate sulla carta;
4. la **firma digitale dell'emettitore**, la più importante: l'impronta crittografica (per esempio SHA-256) del **precertificato**, cioè di tutto il certificato compilato senza la firma (che contiene "scritti nella pietra" emettitore, titolare e chiave pubblica), cifrata con la **chiave privata della CA**. Apposta sul precertificato, lo trasforma in certificato.

**La convalida** (*DI-03 @ 01:29:15-01:31:56*):
1. estraggo dal certificato la firma digitale;
2. leggo l'**issuer DN** e deduco quale CA l'ha firmato;
3. decido se mi fido di quella CA; se sì, recupero la **chiave pubblica della CA**;
4. con questa decifro la firma ed estraggo l'hash;
5. calcolo indipendentemente l'hash del precertificato (il certificato senza firma);
6. se i due hash coincidono il certificato è valido, e mi fido che la chiave pubblica contenuta sia del titolare.

Se Carl sostituisce nel certificato la propria chiave pubblica, la firma resta quella della CA ma l'hash del contenuto cambia: convalidando "mi accorgerò subito che o la firma è invalida o il certificato è invalido. Non mi interessa sapere quale delle due… Boom! Rifiuto qualunque operazione si basi sulla chiave pubblica di Alice". "Carl non può fare un cavolo" (*DI-03 @ 01:30:53-01:31:56*). Per sostituire la chiave dovrebbe falsificare la firma della CA.

> **Nota aggiunta:** "hash cifrato con la chiave privata" è il modello didattico usato in tutto il corso e corrisponde bene a RSA (PKCS#1 v1.5, con padding). Per ECDSA, EdDSA o ML-DSA la firma non è una "cifratura dell'hash" ma un oggetto matematico diverso, verificato con un algoritmo di verifica dedicato; il ragionamento sulla convalida (chi ha la chiave pubblica della CA può verificare, solo chi ha la privata può produrre) resta identico.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 14 (tipi, contenuto e convalida dei certificati)*

- Esempio nuovo di certificato di attributo: un certificato che attesta che "quell'Alice lì e non altre" ha i capelli biondi. Hanno un uso potenzialmente più ampio di quelli a chiave pubblica, ma sono sempre accoppiati a un certificato a chiave pubblica e, nell'esperienza del docente, "non si sono quasi del tutto diffusi"; ipotesi personale: potrebbero trovare "una seconda giovinezza" nei **wallet** dell'identità digitale. (Teams 3 @ 0:18:22-0:19:39)
- Contenuto: la chiave pubblica "che sia RSA 2048, che sia ML-KEM, che sia secp256k1" è la cosa più importante; nel DN del titolare in Italia tipicamente il codice fiscale, la partita IVA o il codice della PA. Senza una firma **tecnicamente valida** non posso essere certo né dell'integrità del certificato né che l'abbia emesso quella CA e non un'altra "di cui magari non mi fido, persino una CA malevola". (Teams 3 @ 0:20:15-0:22:38)
- Per convalidare una firma su un documento devo **anche** prendere la chiave pubblica usata, recuperarla da un certificato e convalidare la firma di quel certificato, "prima o dopo a seconda degli standard che seguo", per accertare l'associazione fra l'asserito firmatario e la sua chiave pubblica. (Teams 3 @ 0:22:16-0:22:53)

## 15. Certificati elettronici secondo eIDAS

*DI-03 @ 01:31:56-01:33:02*

Piccola nomenclatura (parte bassa della slide della sezione 13): la normativa europea usa il termine **certificato elettronico**. Sembra un sinonimo, ma è una **definizione giuridica**: un certificato digitale usato per compiti specifici, cioè firme elettroniche (che "non sono esattamente le firme digitali"), **sigilli elettronici** ("una cosa diversa, ne parleremo tra un po'") e certificati di autenticazione di siti web, che il docente chiama "WAC, Web Access Certificates". Quando si riferirà alle sole caratteristiche tecniche (X.509 e gli altri pochi formati) dirà **certificato digitale** (*DI-03 @ 01:31:56-01:33:02*). Il docente inizia un parallelo con i film, poi si interrompe: "ah no, non ve l'ho detto… ve lo diremo più avanti".

> **Correzione:** nel Regolamento eIDAS la terza categoria è il **certificato di autenticazione di siti web** (*certificate for website authentication*; nella variante qualificata **QWAC**, *Qualified Website Authentication Certificate*), non "Web Access Certificate".

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 15 (certificati elettronici eIDAS)*

- Nel 2026 il docente spiega i tre tipi: i certificati elettronici eIDAS sono un **sottoinsieme** dei certificati digitali, definito non dalle caratteristiche tecniche ma da **cosa** si certifica. Se la chiave pubblica appartiene a una **persona fisica** e i metadati del certificato dicono che la chiave privata è idonea a **firmare**, è un **certificato di firma elettronica**: serve a esprimere la volontà di sottoscrivere un documento. Se appartiene a una **persona giuridica** e serve ad asserire integrità e origine dei documenti, rendendoli riferibili a quella persona, è un **certificato di sigillo elettronico**. Tecnicamente sono sempre certificati X.509. (Teams 3 @ 0:22:53-0:25:11)
- Il terzo tipo, il **certificato di autenticazione di sito web**, serve a stabilire se un sito è riferibile davvero a una persona fisica o giuridica responsabile: se google.com afferisce realmente a Google LLC, del gruppo Alphabet, o è un sito fraudolento. (Teams 3 @ 0:25:11-0:25:52)

## 16. Nomenclatura: certificati di CA, foglia, autofirmati, radice; CA tecniche e amministrative

*DI-03 @ 01:33:02-01:37:32*

**Slide "Certification authorities"** (frame *01:37:06*):

> - A certificate issued to a CA is called a **CA certificate**; otherwise, it is called a **leaf certificate**.
> - A certificate issued by a CA to itself (possibly with different key pairs) is **self-issued**; when the CA (private) key to sign it is associated to the certificate's public key itself, it is a **self-signed certificate**.
> - A self-signed CA certificate is called a **root** (CA) **certificate**.
> - A *technical* CA is the software (e.g. *openssl*, *EJBCA*, …) and/or hardware (e.g. HSM, smartcard, …) component that generates / **signs** *digital* certificates to subjects;
> - An *administrative* CA is the (usually "legal") entity, an **electronic trust service provider** (**eTSP**) according to the **eIDAS Regulation**, providing the electronic *trust service* of *electronic* certificates' **issuance**, by means of technical CA(s).
>
> An administrative CA may own/manage several technical CAs (which self-issue certificates to one another) and, vice versa, a technical CA may provision certificates for multiple administrative CAs.
>
> There is, in general, an ecosystem of eTSPs / administrative CAs out there. The business is the **digital trust** itself, and those who framed first are today very profitable, yet not much known, companies.

(Nella slide l'inciso sull'eTSP è fra trattini lunghi, reso qui con virgole.)

Il commento (*DI-03 @ 01:33:02-01:37:32*):
- un certificato emesso da una CA per la chiave pubblica di **un'altra CA** si chiama in italiano, dagli anni '90, **certificato di certificazione**; in inglese *CA certificate*; altrimenti è un certificato **finale**, *end user* o **foglia**;
- se la CA firma con la propria chiave privata il certificato della chiave pubblica della **stessa coppia** è un certificato ***self-signed***, **autofirmato**; in altri casi si parla di **certificato radice**. "Foglia" e "radice" fanno intuire che i certificati sono organizzati in **gerarchie**, argomento finale della lezione;
- **CA tecnica**: il software o l'hardware che materialmente firma i certificati. Se uso OpenSSL, quella è la mia CA tecnica, magari su un laptop con software non aggiornato e una password debolissima (il proprio nome e cognome): chiunque potrebbe entrare e sostituire la chiave privata. "Come CA tecnica funziona bene… tutto il resto lascia un po' a desiderare";
- **CA amministrativa**: un'entità legale che lo fa per business e "dovrebbe, ma non è detto" adottare misure di cybersicurezza importanti. Esempio: ACME SRL con sette CA tecniche (America, Asia, due in Europa, Africa, Australia) per non costringere tutti a chiamare l'America nei fusi orari americani; oppure una CA amministrativa che usa la CA tecnica di un'altra CA amministrativa e rivende i certificati (un subappalto). Le due definizioni sono "molto grigie", senza corrispondenza uno a uno: c'è un **ecosistema** di Trust Service Provider, "il tessuto nel quale si materializza il concetto di digital trust".

> **Nota aggiunta:** in RFC 5280 un certificato è *self-issued* quando emettitore e soggetto coincidono (stesso DN), anche se la chiave che firma è diversa da quella certificata (tipico dei rinnovi di chiave della CA, *key rollover*); è *self-signed* quando è self-issued **e** la firma si verifica con la chiave pubblica contenuta nel certificato stesso. Il docente nel 2026 dice che la differenza è "un dettaglio davvero troppo tecnico" ai fini del corso.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 16 (nomenclatura delle CA)*

- La coppia di chiavi della CA si chiama in italiano **chiavi di certificazione**, in inglese *CA keys*; poiché le CA sono associate a soggetti giuridici, si può dire che **sigillano elettronicamente** i certificati che emettono. I certificati foglia sono "il prodotto finale dell'attività di certificazione"; quelli che garantiscono a ritroso l'autenticità delle chiavi di certificazione si chiamano **certificati intermedi**. (Teams 3 @ 0:25:52-0:26:59)
- *Self-issued* e *self-signed*: c'è una differenza, "ma non entro nei dettagli… ai fini di questo corso è un dettaglio davvero troppo tecnico"; normalmente si dice *self-signed*. Esempio tipico di self-signed: il certificato radice, "nella radice del trust". (Teams 3 @ 0:26:59-0:27:47)
- OpenSSL è "forse il software open source più famoso al mondo" per farsi una CA in casa; ne esistono versioni installabili sullo smartphone, con cui trasformare in CA tecnica "persino il vostro braccialetto di fitness". Le CA amministrative sono **fornitori di servizi fiduciari elettronici** nella tassonomia europea; possono gestire più CA tecniche in parallelo o in serie, oppure affittare CA tecniche in cloud. Avere una CA in casa "non mi dà nessuna certezza" che mi possa fidare: Carl può presentarsi come Alice e ottenere una coppia di chiavi con scritto "Alice" se nessuno verifica la sua identità; "ci deve essere qualcos'altro", altrimenti gli avversari gestirebbero CA malevole "e non ci sarebbe digital trust in Internet". (Teams 3 @ 0:27:47-0:31:04)

## 17. Fidarsi di una CA: la tassonomia della fiducia

*DI-03 @ 01:37:32-01:54:31*

**Slide "Trust taxonomy"** (frame *01:54:24*):

> A CA has at least one asymmetric key pair $\left(\kappa^{\text{pub}}_{\text{CA}}, \kappa^{\text{priv}}_{\text{CA}}\right)$ which is used to issue (i.e. digitally sign) certificates. Those two keys, individually or as a key pair, are thus called **CA keys**/key-pair.
>
> A digital **trust** relationship between two personalities is a relation, directed from Alice to Bob (and read «*Alice trusts Bob*»), such that:
> - Alice, acting as a CA, issues either:
>   - a public-key certificate towards Bob's public key ($\kappa^{\text{pub}}_{\text{Bob}}$), or
>   - an attribute certificate for an attribute $\mathcal{A}$ that Alice acknowledges Bob being the *holder* of;
> - 3rd parties will trust $\kappa^{\text{pub}}_{\text{Bob}}$ being Bob's public key [Bob holding attribute $\mathcal{A}$] *if* they trust Alice can:
>   1. keep its own CA private key ($\kappa^{\text{priv}}_{\text{CA}}$) private;
>   2. identify any subjects to whom it issues public-key or attribute certificates\*;
>   3. confirm whether any information stated\* in its issued certificates is true, accurate and current (e.g. by means of certificate **validation**).
>
> \* From a governance standpoint, eTSPs may be trusted for issuing **only** specific types of certificates, which are constrained for defined purposes. E.g. I can trust a private company issuing digital certificates to employees' badges, granting them entry into its own premises. Yet, no border controls or airport security would ever accept such eID's to grant borders' crossing, as they may neither want to trust the issuing company, nor be able to reliably validate the certificates issued by that private subject.

In alto a destra: Alice (chiavi gialla e viola) → "trusts" → Bob (chiavi verde e rossa, attributo $\mathcal{A}$), con i due certificati emessi a Bob.

Il commento: le CA lavorano firmando certificati; fidarsi di un certificato significa fidarsi della firma che porta, cioè che la chiave pubblica della CA (gialla), con cui si convalidano tutti i certificati che emette, sia di quella CA (una CA tecnica ha la sua; un'azienda con quattro CA tecniche ne ha quattro) (*DI-03 @ 01:37:32-01:38:35*). Fidarsi della CA significa fidarsi di **tre cose**, "una tecnica e due tipicamente di tipo amministrativo" (*DI-03 @ 01:38:35*).

**1. Che la CA mantenga privata la propria chiave privata** (la viola) (*DI-03 @ 01:39:06-01:44:33*), con misure di sicurezza logiche, fisiche e amministrative (rimando alla guida Cybersecurity). L'attacco alla CA è "enorme": chi ruba la chiave privata (attacco alla riservatezza) o la sostituisce con la propria (attacco all'integrità) può emettere certificati a nome della CA, e tutti quelli che si fidano della CA li prendono per buoni. "È l'attacco peggiore che può capitare a una CA", ed è successo molte volte. Due casi pubblici:
- **DigiNotar** ("mi pare che era olandese, forse era belga"): rubate le chiavi private di CA, la ditta, il cui business era proprio il digital trust, è fallita; incidente del 2011 ("mi pare"), "noto negli annali"; c'erano anche documenti d'identità emessi da alcuni governi basati su certificati comprati da DigiNotar;
- **Nvidia**: rubate le chiavi con cui firmava i driver, che i sistemi operativi accettano come fidati; l'attore le ha usate (benché i certificati fossero scaduti, "ma su questo poi ci arriviamo") per **firmare malware**, che si è installato in sistemi che un malware non firmato non l'avrebbero mai accettato.

A *01:40:42* la connessione si interrompe per circa trenta secondi e il docente riprende la frase.

**2. Che la CA sappia identificare i soggetti** (*DI-03 @ 01:44:33-01:47:16*). Alice chiede un certificato: "chi sei? Fammi vedere un documento", di una nazionalità che la CA sa convalidare; una CA neozelandese davanti a una carta italiana dice "rivolgiti a qualcun altro". Da qui il regolamento **eIDAS**: finché hai un documento valido in Europa, se una CA non sa identificarti (un documento bulgaro in Francia) ti rivolgi all'autorità del tuo paese, "detto in due soldi". Per un'azienda: verifica dell'iscrizione al registro imprese, codice fiscale, partita IVA; identità di chi ha **potere di firma** (*power of attorney*), verificabile in Italia alla Camera di Commercio; oppure documento firmato dall'amministratore che delega un dipendente, più il suo documento d'identità e la fotocopia di quello dell'amministratore (il docente cita "la legge 445 del 2000"). La CA incrocia i dati secondo i criteri che la legge le impone, diversi in Italia, Francia, Stati Uniti, Russia.

**3. Che le informazioni siano vere, accurate e attuali, e che la chiave del titolare resti privata** (*DI-03 @ 01:47:16-01:50:26*). Tipicamente la CA consegna lei la chiave privata in un dispositivo, software o hardware, da cui si estrae solo dimostrando di essere il titolare (PIN, password, impronta), o in **busta chiusa** con il codice di sblocco a parte (carte di pagamento, carta d'identità). Ma soprattutto deve avere sistemi per **revocare** il certificato se la chiave è smarrita, rubata o sospettata di furto, e per **riemettere** il certificato se i dati personali cambiano. "È un mestiere complicato": la CA open source sul laptop, anche se usa lo stesso software del TSP a pagamento di alto livello, non ha gli stessi presidi di sicurezza fisica, tecnica e organizzativa di chi lo fa per mestiere, come i notai.

**Governance: non tutte le CA possono emettere certificati di qualunque tipo** (*DI-03 @ 01:50:26-01:54:31*). Tecnicamente tutti i certificati X.509 sono uguali, ma c'è un aspetto di governance (l'asterisco della slide). Esempio del badge: l'azienda dà al consulente un badge con certificato che apre il tornello finché lavora lì; ma passato al gate dell'aeroporto non funziona, perché il gate non si fida digitalmente della CA dell'azienda, che non è un'autorità di frontiera. Si possono scaricare da Internet i profili X.509 dei passaporti ICAO e crearsi una CA che emette certificati tecnicamente identici, ma il gate si fida solo delle autorità autorizzate per legge. Il gate ha l'elenco dei certificati di **tutti i paesi membri ICAO**: quando passa un passaporto lituano ci sono due certificati, quello nel passaporto e quello dell'autorità lituana che emette i passaporti (in Italia, dice il docente, "il Ministero della Giustizia, mi pare" per i passaporti e il Ministero dell'Interno per le carte d'identità). "Il problema del digital trust è un problema di fiducia che si sposta": da fidarmi di Alice a fidarmi della CA.

> **Correzione:** il furto alla DigiNotar (paesi Bassi, 2011, fallita nel settembre 2011) riguardava la **chiave privata** di CA; a *01:41:43* il docente dice per lapsus "gli hanno rubato la chiave pubblica di CA". I passaporti italiani **non** sono di competenza del Ministero della Giustizia: sono rilasciati dalle Questure (Ministero dell'Interno) e, all'estero, dalle rappresentanze diplomatico-consolari. La norma citata è il **D.P.R. 445/2000** (Testo unico sulla documentazione amministrativa), non una legge.

> **Nota aggiunta:** il caso Nvidia è del 2022 (gruppo Lapsus$): furono diffusi certificati di firma del codice scaduti, comunque accettati da Windows per la firma dei driver in certe condizioni. Il "dopo WannaCry" detto dal docente a proposito di DigiNotar non è un riferimento cronologico (WannaCry è del 2017).

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 17 (fidarsi di una CA)*

- La relazione di trust si realizza tecnicamente fra due soggetti: la CA con le sue chiavi di certificazione (gialla e viola) firma il certificato foglia del soggetto finale. Terze parti che **non conoscono Bob** e non possono fidarsi che lui custodisca la sua chiave rossa si fidano invece della CA. (Teams 3 @ 0:31:04-0:33:03)
- Identificazione, esempi 2026: Bob si presenta con la patente indonesiana a una CA europea che non sa verificarla: "dammi un documento che io so convalidare… presentati con un'identità digitale che io sappia riconoscere". Per Bob SRL, Bob Inc., Bob SA: dati societari, registro nazionale, documento che attesta il potere di richiedere il **certificato di sigillo elettronico** (amministratore delegato, direttore finanziario, rappresentante legale o un delegato con documento firmato dal board, firma verificabile alla Camera di Commercio). Per www.bob.com, oltre all'identificazione del richiedente, si verifica nel **DNS** che il dominio sia registrato a nome di Bob. (Teams 3 @ 0:33:03-0:35:57)
- Terza proprietà: le informazioni devono restare vere **nel tempo**; se Bob perde la chiave privata o ha evidenza che qualcuno la conosce ("sicuramente se ha usato QKD"), Alice deve **revocare** il certificato: c'è un processo di vigilanza di cui la CA è responsabile. (Teams 3 @ 0:35:57-0:37:13)
- Governance: il badge aziendale (stesso standard tecnico BSI dei documenti di viaggio, certificato tecnicamente valido) apre il gate del magazzino a un fornitore ma non il gate dell'area d'imbarco, "perché Alice SRL non è il governo italiano"; in alcuni aeroporti italiani oggi si passa il gate anche con la CIE. Aggiunta 2026: anche lo **scopo** conta, un certificato per cifrare è diverso da uno per firmare o da uno per attestare l'identità, anche se tutti X.509 e firmati dalla stessa CA: quello per firmare "non dovrebbe essere ammesso" per verificare un documento cifrato, "ma di questo ne parleremo più avanti". (Teams 3 @ 0:37:13-0:40:08)

## 18. PKI: gerarchie e percorso di fiducia

*DI-03 @ 01:54:31-01:57:53*

**Slide "Public Key Infrastructure"** (frame *01:56:41*): "A **public key infrastructure** (**PKI**) is a *directed graph* whose nodes are CAs and whose links are digital trust relations." Tre topologie: ***Hierarchical* PKI** (in rosso: *Root CA* → due *intermediate sub-CA* e una *leaf sub-CA*; ciascuna intermedia → una *leaf sub-CA*); ***(full) Mesh* PKI** (in verde: cinque CA collegate tutte con tutte in entrambe le direzioni); ***Ring* (mesh) PKI** (in blu: cinque CA in un anello orientato).

Il commento, "l'ultima slide della giornata" (*DI-03 @ 01:54:31-01:57:10*): il problema della fiducia è **gerarchico** e "non lo risolvo mai completamente" (se ne riparlerà). Se mi fido di una CA devo fidarmi della sua chiave pubblica (la gialla), che non può essere scritta da qualche parte dove Carl potrebbe cambiarla: tipicamente sta in un **certificato di CA** emesso da un'altra CA. Per fidarmi di una CA foglia mi devo fidare di una **CA intermedia**, la cui chiave sta in un certificato firmato da un'altra CA, e così via per molti livelli: si crea una **gerarchia** di CA. Questi grafi o alberi si chiamano **infrastrutture a chiave pubblica** (PKI). Le più semplici e più usate sono ad **albero** con una **CA radice** che ha un **certificato radice** autofirmato: se mi fido della radice, mi fido in cascata di tutte le intermedie fino alle foglie e ai certificati che emettono. "Questo è lo scenario più semplice col quale termino la lezione di oggi."

In chiusura: si riprenderà non la settimana successiva (il docente è assente) ma quella dopo, "per le lezioni finali" (*DI-03 @ 01:57:10*).

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 18 (PKI e trust path): nel 2026 il docente va molto oltre la slide*

- Analogia del matrimonio "a catena": sposo e sposa senza un testimone comune portano ciascuno un parente (CA intermedie) che conosce un terzo soggetto, il quale garantisce per entrambi i parenti: fiducia **indiretta**. Nella PKI gerarchica la CA superiore firma con la propria chiave privata il certificato della CA sottostante (per esempio la radice, con il suo certificato autofirmato, certifica che la CA intermedia userà la propria chiave per firmare i certificati finali). Si crea un **percorso fiduciario**, ***trust path***, dalla radice al certificato finale; esiste anche il percorso brevissimo con un solo livello di CA. (Teams 3 @ 0:40:15-0:42:31)
- Topologie: la più usata in pratica è la **gerarchica**, che ricalca le deleghe di poteri di rappresentanza (la fiducia si trasmette dall'alto in basso). Alla radice della fiducia, nel back-end, si trovano spesso PKI **a rete** (*mesh*): ad anello (ogni CA si fida di una sola e l'ultima della prima), a doppio anello, complete; servono dove la sicurezza della radice va garantita a un livello superiore. Le CA intermedie di solito firmano solo certificati di altre CA, a volte anche certificati foglia. La radice della fiducia è l'**ancora fiduciaria** (*trust anchor*), tipicamente una CA radice con certificato autofirmato. (Teams 3 @ 0:42:31-0:45:34)
- **Bridge CA** (nuovo 2026): se non mi fido della root CA in cima alla catena, non posso fidarmi di nulla di ciò che emette. Esempio: Paola e Francesca portano al matrimonio la "root CA" del loro ordine ecclesiastico, ma la relying party che deve attestare il matrimonio professa un'altra fede e non se ne fida. Le root CA dei due ordini possono fare un **accordo bilaterale** e creare una **CA ponte**, che consente a chi si fida della root viola di fidarsi anche dei certificati della root rossa e viceversa: "l'analogo digitale dell'accordo bilaterale di fiducia tra due paesi stranieri", tipicamente tramite i ministeri degli Esteri. (Teams 3 @ 0:45:39-0:48:10)
- **Convalida della catena** (nuovo 2026): arriva un contratto firmato da Alice. Convalido la firma (hash del documento, decifratura dell'hash dalla firma con la chiave pubblica di Alice presa dal suo certificato, confronto) e so che è tecnicamente valida; ma mi fido che la chiave sia di Alice solo se il suo **certificato di firma elettronica** ha a sua volta una firma valida. Leggo quale CA l'ha emesso, recupero la chiave pubblica della CA da un certificato di certificazione, verifico il **sigillo elettronico** della CA sul certificato, e così via **a ritroso** finché non arrivo a una CA, "non necessariamente la CA radice", di cui mi fido **assiomaticamente**, tipicamente rappresentata da un certificato radice. "Esattamente come nel mondo reale… alla fine devo arrivare a una persona della quale mi fido ciecamente". Se non è così intervengono "altri meccanismi di fiducia che vedremo più tardi". (Teams 3 @ 0:48:17-0:52:07)
- **Il mercato del digital trust** (nuovo 2026): dietro "CA" c'è quasi sempre un'intera PKI, magari con CA giuridicamente diverse. Esempi noti: **Microsoft** firma tutto il software che rilascia e Windows rifiuta aggiornamenti non firmati ("l'incidente CrowdStrike insegna"), **Apple**, **Symantec** ("un tempo la creatrice del Norton Antivirus", oggi gestisce una delle PKI più famose). La maggior parte dei colossi che fanno da CA radice in Internet sono **americani**, con nomi che il pubblico non conosce perché lavorano **B2B**, innestati negli strati profondi della PKI; c'è "anche qualche piccolo italiano". Nella lezione successiva un esempio concreto su un sito web. (Teams 3 @ 0:52:15-0:55:56)
- **RA e VA** (nuovo 2026): i dati nel DN del certificato (in Italia nome, cognome e codice fiscale o, in mancanza, l'identificativo di un documento valido in Europa o di un passaporto; per le persone giuridiche ragione sociale e codice fiscale, partita IVA o VAT number, o il codice **IPA** registrato sul sito di AgID per le PA; per i sistemi tecnici il nome del sito web) li verifica la **Registration Authority (RA)**, il *front-end* della PKI a cui si rivolge l'utente e che spesso chiede il pagamento. La **Validation Authority (VA)** è invece il servizio fornito alle **relying parties** per verificare online se un certificato rilasciato oggi è ancora valido domani. (Teams 3 @ 0:55:56-0:58:48)

> **Nota aggiunta:** il docente nel 2026 dice che nella PKI la fiducia passa "in maniera spesso intransitiva" (Teams 3 @ 0:42:57) e subito dopo che nelle gerarchie "si trasmette transitivamente": la seconda è la lettura corretta per il modello gerarchico (se mi fido della radice mi fido di ciò che certifica in cascata), mentre nelle reti di CA e con i bridge la fiducia può essere vincolata (per esempio con le estensioni *name constraints* e *policy constraints* di X.509) e quindi non sempre transitiva. Symantec ha venduto il proprio business di certificati a DigiCert nel 2017.

## 19. Glossario

| Termine | Significato nel corso |
|---|---|
| Chiave di contenuto (*content key*) | Chiave simmetrica casuale generata per un solo contenuto e cifrata per ciascun destinatario |
| Busta crittografica, P7E | Contenitore con contenuto cifrato e copie della chiave di contenuto cifrate per i destinatari |
| Cifratura omomorfa | Cifratura che commuta con certe operazioni: calcolo sui dati cifrati, risultato decifrato uguale al calcolo sui dati in chiaro |
| Entanglement (stato ingarbugliato) | Stato di più sistemi quantistici non riducibile alla combinazione degli stati singoli (fuori esame) |
| Qubit | Sistema quantistico a due stati, base del calcolo quantistico (fuori esame) |
| Crittoanalisi quantistica | Algoritmi quantistici (Shor, Grover) che battono algoritmi classici |
| PQC, crittografia quantum-safe | Algoritmi classici, eseguibili su dispositivi di oggi, resistenti alla crittoanalisi quantistica |
| QKD | Distribuzione quantistica delle chiavi: rileva se una chiave è stata osservata in transito |
| BB84 | Protocollo QKD di Bennett e Brassard (1984) |
| ML-KEM, ML-DSA, SLH-DSA, FN-DSA | Nomi definitivi di Kyber (FIPS 203), Dilithium (FIPS 204), SPHINCS+ (FIPS 205), Falcon (FIPS 206) |
| Harvest now, decrypt later | Furto oggi di dati protetti da crittografia classica per romperli quando sarà disponibile un calcolatore quantistico |
| Mosca's law | Bisogna migrare prima che tempo di migrazione più durata di sicurezza dei dati superi l'arrivo del calcolatore quantistico |
| Migrazione ibrida | Fase in cui la pipeline supporta algoritmi classici e post-quantistici |
| Downgrade attack | Forzare un sistema che supporta più algoritmi a usare il meno sicuro |
| Digital trust | Riconoscimento di integrità, autenticità e non ripudio di dati e sistemi, con identificazione delle persone corrispondenti |
| Relying party | Parte che fa affidamento sulla certificazione |
| Soggetto, titolare (*subject*) | Persona fisica, giuridica o sistema a cui il certificato lega la chiave pubblica |
| Holder | Titolare di un attributo in un certificato di attributo |
| Certification Authority (CA) | Terza parte fidata che emette e firma certificati |
| Trust Service Provider (TSP, eTSP) | Prestatore di servizi fiduciari, la CA in senso amministrativo |
| Notaio digitale | Servizio fiduciario distinto, svolto dai notai; non trattato nel corso |
| Certificato digitale | File in formato standard che lega una proprietà ai dati distintivi di un soggetto, firmato da una CA |
| X.509, RFC 5280 | Standard ITU dei certificati e suo profilo per Internet |
| CVC | *Card verifiable certificate*, certificato verificabile dentro il chip |
| DN | *Distinguished Name*, dati distintivi di emettitore e titolare |
| Precertificato | Certificato compilato ma senza firma; non utilizzabile |
| Certificato elettronico | Definizione giuridica eIDAS: certificati di firma elettronica, di sigillo elettronico, di autenticazione di siti web |
| Certificato di certificazione (*CA certificate*) | Certificato emesso a una CA |
| Certificato foglia | Certificato finale emesso a un soggetto non CA |
| Certificato intermedio | Certificato di una CA intermedia in una catena |
| Certificato autofirmato, radice | Firmato con la chiave privata della stessa coppia; quello della CA radice |
| CA tecnica / amministrativa | Software o hardware che firma / entità legale che fornisce il servizio |
| Chiavi di certificazione (*CA keys*) | Coppia di chiavi con cui la CA firma i certificati |
| PKI | Grafo orientato di CA e relazioni di fiducia: gerarchica, mesh, ad anello |
| Trust path, ancora fiduciaria | Percorso dalla radice al certificato finale; CA di cui ci si fida assiomaticamente |
| Bridge CA | CA ponte che collega due PKI con un accordo di fiducia reciproca |
| RA, VA | Registration Authority (identificazione, front-end); Validation Authority (verifica della validità nel tempo) |

## 20. Punti incerti

- *DI-03 @ 00:05:59*: il tipo di attacco nominato ("non-suffertex-attacchi" nella trascrizione) non è udibile con certezza: [?].
- *DI-03 @ 00:34:57*: il nome colloquiale del primo standard (FIPS 203) è caduto dalla trascrizione; dalla slide è Kyber.
- *DI-03 @ 00:13:27-00:13:37*: circa 10 secondi non trascritti, subito prima della frase sulle domande d'esame.
- *DI-03 @ 01:24:22-01:24:51*: circa 30 secondi non trascritti (inizio della definizione del certificato di attributo).
- La slide "Two yet unravelled practical issues" mostra solo il primo punto: il secondo problema pratico non compare in nessun frame e il docente non lo enuncia esplicitamente in DI-03.
- Il primo frame della slide "Digital (and electronic) certificates" è a *01:16:10*, mentre il docente inizia a parlarne a *01:09:47*: il frame precedente (*01:09:24*) è ancora "Trust in the digital age"; è probabile che la slide sia apparsa prima ma il frame non sia stato estratto.
- Il caso della libreria SAML insicura (*DI-03 @ 01:15:11*) è raccontato senza nomi: non identificabile.
- FIPS 206: la pubblicazione definitiva nel 2026 dichiarata in Teams 2 non è verificata.
- Teams 3 @ 0:35:36: "il namex" nella trascrizione Teams, probabilmente *name server* o registro dei nomi a dominio: [?].

## 21. Esame

Frasi del docente su cosa sarà o non sarà chiesto, rilevanti per questo capitolo:

- *DI-03 @ 00:13:37*: "su un dettaglio non ci saranno domande su questa parte di calcolo e meccanica quantistica, ovviamente non ci saranno, non è argomento del corso, solo per soddisfare qualche curiosità". Riguarda la sezione 3.
- Teams 1 @ 1:02:46-1:03:13 (2026, citato per completezza; la sezione è del capitolo 02): "non ci saranno domande di meccanica quantistica né di calcolo quantistico. All'esame al massimo potrebbe esserci qualche domanda sul **problema concreto alla base della crittografia post quantistica**"; le introduzioni di meccanica, elettronica e calcolo quantistico "servono solo a dare un piccolo background del perché il problema si pone oggi". Il problema concreto, come lo spiega il docente, è riassunto nel riquadro della sezione 4: Shor rende polinomiale la rottura della crittografia a chiave pubblica (allungare le chiavi non basta, va cambiato algoritmo), Grover impone di allungare chiavi simmetriche e hash, servono algoritmi su problemi matematici nuovi eseguibili su dispositivi classici, e l'harvest now, decrypt later rende la migrazione urgente già oggi.
- *DI-02 @ 01:47:08* (capitolo 02, citato per completezza): sulle slide dell'hardware quantistico, "non guardate le slide, non saranno oggetto d'esame".
- *DI-03 @ 00:07:42*: la slide matematica sulla cifratura omomorfa è "la slide più matematica che vedrete in tutto il corso, solo per soddisfare un po' di curiosità" (non è un'esclusione esplicita dall'esame, ma indica che le formule sono un approfondimento).
- *DI-03 @ 01:09:14*: il servizio fiduciario di **notaio digitale** non viene descritto "e né lo farò nel corso".
- *DI-03 @ 01:25:27*: i certificati di attributo "non li vedremo quasi mai durante questo corso".
- Teams 3 @ 0:27:21: la differenza fra *self-issued* e *self-signed* è, "ai fini di questo corso, un dettaglio davvero troppo tecnico".
- Teams 3 @ 0:00:21: sulla QKD, "questo non è un corso di fisica".

Nessun'altra indicazione d'esame in DI-03, in Teams 2 o nella parte di Teams 3 di questo capitolo. Per il quadro completo vedi la pagina [Assessment](assessment.md).
