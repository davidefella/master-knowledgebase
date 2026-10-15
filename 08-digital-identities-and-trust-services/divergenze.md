# Divergenze

Errori, imprecisioni e differenze fra fonti, capitolo per capitolo. Le voci **Correzione** sono certe; le **Nota** sono precisazioni o semplificazioni. Ogni correzione compare anche nel capitolo, nel punto in cui il docente la dice.

## Capitolo 01

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 01. Le voci "Correzione" sono certe; le "Nota" sono precisazioni o semplificazioni.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| DI-01 @ 01:06:51 | Primi elencati come "1, 2 che è l'unico primo pari, 3…" | 1 non è primo | Correzione |
| DI-01 @ 01:08:27 | "trovare i divisori non banali di un numero primo" | Un primo non ha divisori non banali: il problema è fattorizzare il composto $N = p \cdot q$ | Correzione |
| Slide RSA (DI-01 @ 01:08:21) | "The private key is one of $N = p \cdot q$'s prime factors" | La privata è l'esponente $d$ (derivabile da $p$, $q$); la pubblica è $(N, e)$. La slide dice "loosely speaking" | Nota |
| Teams 1 @ 0:13:14 | RSA-2048 ≈ AES-256 | Secondo NIST SP 800-57: RSA-2048 ≈ 112 bit, AES-128 ≈ RSA-3072, AES-256 ≈ RSA-15360 | Correzione |
| Slide casi d'uso (DI-01 @ 01:14:34) | Stesso crittogramma `6EB69570 08E03CE4` nei due schemi | Refuso: con chiavi diverse i crittogrammi differiscono (lo dice il docente in Teams 1 @ 0:07:55) | Correzione (del docente) |
| Slide "Asymmetric for confidentiality and authenticity" (DI-01 @ 01:28:00) | Schema "Combine keys" → segreto condiviso | È un accordo di chiave (Diffie-Hellman/ECDH); il commento 2026 descrive invece la doppia cifratura | Nota |
| Slide ECC (DI-01 @ 01:13:17) | $a, b \in \mathbb{N}$ "usually very large integers" | $a, b \in \mathbb{F}_p$, non necessariamente grandi (secp256k1: $a=0$, $b=7$) | Nota |
| Slide salting (DI-01 @ 00:45:46) | nonce = «a secret number used once» | Il sale non è segreto (la slide stessa lo precisa subito dopo); nonce = *number used once* | Nota |
| DI-01 @ 00:38:43 | Il sistema trasferisce al verificatore solo l'impronta della password | Di norma la password viaggia in TLS e l'hash si calcola sul server; per le password si usano KDF lente con sale (bcrypt, scrypt, Argon2) | Nota |
| DI-01 @ 00:27:49-00:32:28 | Tre caratteristiche: lunghezza fissa, non invertibilità, collisioni difficili dato un messaggio | Proprietà standard: preimmagine, seconda preimmagine, collisioni; quella descritta è la seconda preimmagine | Nota |
| Slide crypto-agility (DI-01 @ 00:24:20) | Hash e cifratura "shall be broken" dai computer quantistici | Vale per RSA/ECC (Shor); hash lunghi e AES-256 restano robusti (Grover, vantaggio quadratico) | Nota |

### Fonti e anomalie

- **DI-01 01:09:08-01:47:42: audio assente** (silenzio digitale a -91 dB) con slide che avanzano. Contenuto ricostruito da frame, DI-02 (2025) e Teams 1 (2026).
- Trascrizione automatica: "Rives, Adelman" per Rivest, Adleman; "Digital Identity Central Service" per Digital Identities and Trust Services; "architettografia", "credito agilità" per crittografia e cripto-agilità; "drogana" per dogana; "i cao" per ICAO.

### Differenze 2025 / 2026

- Nel 2026 la lezione 1 non ripete hash, simmetrica, RSA ed ECC (già fatti in Cybersecurity, lezione 7 Teams 2026) e parte dai casi d'uso della chiave pubblica.
- Nel 2026 il docente spiega a voce key encapsulation e svantaggi della simmetrica, che nel 2025 cadono nella parte senza audio.


## Capitolo 02

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 02. Le voci "Correzione" sono certe; le "Nota" sono precisazioni o semplificazioni.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| DI-02 @ 00:00:42 | Il prodotto di due numeri da 100 cifre ha "decine di migliaia di cifre" | Ha 199 o 200 cifre (verificato per esecuzione) | Correzione |
| DI-02 @ 00:35:51 | RSA-2048 "più o meno corrisponde" ad AES-256 | NIST SP 800-57: RSA-2048 ≈ 112 bit; AES-256 ≈ RSA-15360 (stesso errore di Teams 1 @ 0:13:14, capitolo 01) | Correzione |
| Slide "Digital signatures" (DI-02 @ 01:16:16) | "If $h_1 \neq h_2$ either message and digital signature have been modified (or a hash collision has occurred)" | Modificato il messaggio **o** la firma (o usata la pubblica sbagliata); una collisione spiega un falso $h_1 = h_2$, non $h_1 \neq h_2$ | Correzione |
| DI-02 @ 01:41:42 | 00, 01, 10, 11 "rappresentano i numeri 1, 2, 3, 4" | Rappresentano 0, 1, 2, 3 | Correzione |
| DI-02 @ 01:44:30 | Quantum dot = "porte logiche su bit quantistici" | Secondo la slide stessa i quantum dot intrappolano i qubit; le operazioni sono i quantum gate | Correzione |
| DI-02 @ 01:52:58 e slide "From quantum gates…" | I QC riducono problemi "non polinomiali (NP)" a complessità "sub-esponenziale (BQP)" | Non si ritiene che i QC risolvano i problemi NP-completi; Shor risolve in tempo polinomiale fattorizzazione e log discreto; BQP = tempo polinomiale quantistico | Correzione |
| Teams 1 @ 1:23:27 | "AES di cifratura asimmetrica" | AES è simmetrico (lapsus o trascrizione) | Correzione |
| Teams 1 @ 1:22:35 | "teorema di Shor e teorema di Grover" | Sono algoritmi | Correzione |
| Teams 1 @ 1:08:36 | "principio di determinazione di Heisenberg" | Principio di indeterminazione (probabile errore di trascrizione) | Correzione |
| controlli-iniziali.md, sezione Esame | "DI-02 @ 01:39:11: JAdES, capitolo saltato solo se ci sarà tempo" | La slide di sezione subito dopo (DI-02 @ 01:39:09) è "Privacy Enhancing Technologies and anonymisation": il capitolo saltato è quello sulle PET; JAdES è stato trattato | Correzione (del nostro indice) |
| DI-02 @ 00:44:34 e Teams 1 | "Key wrapping" / "key encapsulation" usati come sinonimi | Concetto identico; nella terminologia moderna KEM/DEM | Nota |
| DI-02 @ 00:47:40 | La chiave cifrata è "qualche centinaio di bit" (ECC), "qualche migliaio" (RSA), "decine di migliaia" (PQC) | Sono le dimensioni dell'oggetto a chiave pubblica, non della chiave simmetrica avvolta (128-256 bit) | Nota |
| DI-02 @ 00:41:54 | Mezzo milione di chiavi = "diverse centinaia di megabyte" | $499500 \times 32$ B ≈ 16 MB; ogni utente ne tiene 999 | Nota |
| DI-02 @ 00:19:36 | IV nullo "per semplicità" | Con IV fisso la cifratura CBC è deterministica; l'IV va casuale; CBC non dà integrità (meglio GCM) | Nota |
| DI-02 @ 01:05:42 e slide | Firma = "digest cifrato con la privata" | Esatto per RSA PKCS#1 v1.5; ECDSA/EdDSA non cifrano, la verifica è un'equazione booleana | Nota |
| DI-02 @ 01:22:56 | Stessa chiave + stesso dato = firma sempre identica bit a bit | Vero per schemi deterministici (RSA v1.5, EdDSA, ECDSA RFC 6979); falso per RSA-PSS ed ECDSA randomizzato (verificato) | Nota |
| DI-02 @ 01:36:23 | JWS = "JSON Web Token Signature" | JSON Web Signature (RFC 7515); JWE RFC 7516; JWT RFC 7519 | Nota |
| Slide JWT/JWS/JAdES (DI-02 @ 01:28:45-01:37:59) | Token di esempio con header JOSE `ES256` | Il token è l'esempio jwt.io: header `HS256` (HMAC, non firma digitale), segreto `your-256-bit-secret` (verificato) | Nota |
| Slide JWS (DI-02 @ 01:35:22) | "JWT compact serialization and a JSON compact serialization" | JWS/JWE *Compact Serialization* e *JSON Serialization* | Nota |
| DI-02 @ 01:37:24 | JWE consente di cifrare solo alcune parti del JSON | JWE cifra l'intero payload; la divulgazione selettiva è SD-JWT | Nota |
| Slide "PDF signature wrapping attack" | Figura etichettata come signature wrapping | La figura in basso è uno *shadow attack* (pdf-insecurity.org); il signature wrapping in senso stretto manipola `/ByteRange` | Nota |
| DI-02 @ 01:45:33 | Fibre ottiche per qubit fino a "alcune decine di chilometri" | TF-QKD oltre 1000 km di fibra nel 2023 (USTC) | Nota |
| DI-02 @ 01:42:13 | Qubit in "sovrapposizione statistica" | Sovrapposizione di ampiezze complesse, non miscela statistica; conta l'interferenza | Nota |
| DI-02 @ 01:49:50 | USA "circa 3,5", Regno Unito "4,5" miliardi | La slide riporta US \$3.75b e UK \$4.3b | Nota |
| Slide "From quantum gates…" | "phase-shift (1-param)" con matrice $\mathrm{diag}(1, i)$; aggiunti scritti $T^t$, $S^t$ | La matrice è la porta $S$ fissa ($\pi/2$); l'aggiunto si scrive $T^\dagger$, $S^\dagger$ | Nota |
| Teams 1 @ 0:38:26 | Anche le operazioni statistiche non lineari si fanno con algebra lineare sul cifrato | In FHE le non linearità si approssimano con polinomi; gli schemi parziali supportano solo somma o prodotto | Nota |

### Fonti e anomalie

- **DI-02 0:00-0:50**: rispiega a voce le slide della parte senza audio di DI-01 (capitolo 01, sezione 12); qui solo il commento, il testo delle slide è nel capitolo 01.
- **DI-02 @ 01:02:28**: "parte di quella lezione che non è stata registrata ieri": possibile lezione del 14/10/2025 non registrata, oppure riferimento alla parte senza audio di DI-01. Da segnalare nei controlli iniziali.
- **DI-02 @ 01:50:20-01:50:35**: quattro slide sul post-quantum scorrono in pochi secondi mentre il docente cerca una slide mancante; non commentate.
- Trascrizione automatica: "criptografia/trittografia/tettografia/cartografia" per crittografia; "AS256", "AS encrypt" per AES; "key-dropping", "key mapping", "Symmetry Key Mapping" per key wrapping; "Arrichetti" per Arrighetti; "Agrobat", "acrobato" per Acrobat; "PADES", "padres" per PAdES; "JADES", "già adesso" per JAdES; "JV" per JWE; "ropper" per wrapper; "Signature Rocking Attack" per signature wrapping attack; "Cinematal dei Tali", "Tante Itali" per "Taldeitali"; "polisi" per policy; "clittografiche" per crittografiche; "rsi encrypt" per RSA Encrypt; "mi self digest" [?].
- Trascrizione Teams 1: "QPD" per QKD; "trappolo quantistico" per calcolo quantistico [?]; "quantum White" per quantum wire; "shore" per Shor; "Delicious, Sphinx" (Teams 2) per Dilithium, SPHINCS+.

### Differenze 2025 / 2026

- Nel 2026 il laboratorio CyberChef su AES e RSA non c'è in Teams 1.
- Nel 2026 il docente insiste sul fatto che il key wrapping vale sia in transito sia a riposo (busta = file o pacchetto di rete) e sugli stati in serie; nel 2025 non lo dice.
- Nel 2026 la cifratura in uso è motivata anche con il cloud e l'IA (capacità di calcolo affittata) ed è presentata "a scopo di cultura generale"; nel 2025 con brevetti, studi clinici e la "ricetta della Coca-Cola".
- Nel 2026 la firma digitale è collegata esplicitamente al digital trust, alle due ipotesi (algoritmo robusto, *sole control* della privata) e allo **schema** di firma; nel 2025 lo schema compare solo come riga finale della slide.
- Nel 2026 PAdES, JWT/JWS/JWE, JAdES e signature wrapping non sono in Teams 1 (formati di firma in Teams 6, SD-JWT in Teams 8).
- Nel 2026 la lezione 1 arriva alle tre accezioni di crittografia quantistica (crittoanalisi quantistica, PQC, QKD) e dà l'unica indicazione d'esame del corso; nel 2025 DI-02 si ferma al parallelismo quantistico.


## Capitolo 03

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 03. Le voci "Correzione" sono certe; le "Nota" sono precisazioni, semplificazioni o affermazioni non verificabili.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| DI-03 @ 00:02:11 | Paperino trova un oggetto "firmato con la sua chiave pubblica" | Cifrato (con la chiave pubblica si cifra) | Correzione (lapsus) |
| Slide omomorfa (DI-03 @ 00:11:59) | $R_{\text{ops}}(X_1, X, \dots, X_n)$ | $R_{\text{ops}}(X_1, X_2, \dots, X_n)$ | Correzione (refuso) |
| Slide omomorfa / DI-03 @ 00:10:32 | Cifratura che "commuta" con lo stesso operatore | Spesso sui crittogrammi si applica un'operazione diversa (Paillier: prodotto dei crittogrammi = somma dei messaggi) | Nota |
| Slide "From quantum gates to quantum computing" (DI-03 @ 00:18:29) | NP = "non-polynomial" | NP = *nondeterministic polynomial time* | Correzione |
| DI-03 @ 00:23:56-00:25:00 | Shor e Grover portano la complessità da esponenziale a polinomiale | Vale per Shor; Grover dà un vantaggio quadratico ($2^{k/2}$), resta esponenziale | Correzione |
| Slide "Quantum-safe algorithms" (DI-03 @ 00:36:14) | "ETSI TR 106-619" | ETSI TR 103 619 (lo dice il link stesso della slide) | Correzione |
| Slide "Quantum-safe algorithms" | Kyber come "encryption" | ML-KEM è un meccanismo di incapsulamento di chiave (KEM) | Nota |
| DI-03 @ 00:34:27 | Open call NIST "nel 2017" | Call del dicembre 2016, scadenza proposte novembre 2017, 69 candidati al primo round | Nota |
| Slide HNDL (DI-03 @ 00:43:34) e DI-03 @ 00:37:15 | Simmetrica e hash vulnerabili "around 2026" | Previsione non condivisa: il NIST considera AES-128 adeguato anche post-quantum (categoria 1) | Nota |
| DI-03 @ 00:49:01 | Esempio in cui un calcolatore quantistico "buca" AES-256 | AES-256 è la destinazione raccomandata dalla roadmap; esempio da leggere come provocazione | Nota |
| Slide "NIST PQC roadmap" (DI-03 @ 00:53:33) | "SLH-DSS (Sphincs+)" | SLH-DSA (FIPS 205) | Correzione |
| Slide roadmap e Teams 2 @ 0:29:39 | Dal 2030 deprecati anche simmetrici e hash a 128 bit; il NIST "ha imposto" | Bozza NIST IR 8547 (dic. 2024): deprecati dopo il 2030 gli algoritmi a chiave pubblica a 112 bit, disallowed dopo il 2035 tutti quelli quantum-vulnerabili; AES-128 e SHA-256 non deprecati; è una proposta | Nota (verificata su fonte secondaria) |
| Teams 2 @ 0:09:04 | FIPS 206 basato "su un'altra metodologia matematica" | FN-DSA (Falcon) è anch'esso su reticoli (NTRU) | Correzione |
| Teams 2 @ 0:06:34 | FIPS 206 "uscito quest'anno" (2026) | Bozza inviata ad approvazione ad agosto 2025; pubblicazione finale non verificata | Nota |
| Teams 2 @ 0:22:52 | RSA-2048 battibile con "pochissime centinaia di qubit" | Stime pubbliche (Gidney 2025): circa un milione di qubit fisici, circa 1500 logici | Nota |
| Teams 2 @ 0:38:46-0:45:22 | In BB84 Alice comunica prima a Bob come orientare i polarizzatori; BB84 usa stati entangled | Bob sceglie le basi a caso, il confronto delle basi è successivo (*sifting*); BB84 non usa entanglement (E91 sì). La tabella della slide 2025 è corretta | Correzione |
| Teams 2 @ 0:35:31 | "Un teorema del 1984" | 1984 è il protocollo BB84; le dimostrazioni di sicurezza sono successive | Nota |
| Slide QKD (DI-03 @ 00:53:49) | Legenda polarizzazione 135° = 1, 45° = 0 | La tabellina di Alice usa la convenzione opposta (↗ = 1, ↖ = 0); la tabella è coerente con quest'ultima | Nota |
| DI-03 @ 01:02:05 | DMA per "gli operatori economici che vendono online"; obbligo di sede in UE | DSA: rappresentante legale per gli intermediari extra-UE (art. 13); DMA: gatekeeper | Nota |
| DI-03 @ 01:11:30 | X.509 "reso pubblico" nella RFC 5280 | RFC 5280 è il profilo Internet (PKIX) di X.509 | Nota |
| Teams 3 @ 0:15:33 | La raccomandazione ITU X.509 è a pagamento | Le Raccomandazioni ITU-T in vigore sono scaricabili gratuitamente | Nota |
| DI-03 @ 01:13:32 e Teams 3 @ 0:16:22 | I passaporti usano CVC invece di X.509 | I certificati Document Signer e CSCA dei passaporti sono X.509 (ICAO 9303); i CVC servono all'Extended Access Control (autenticazione del terminale) | Correzione |
| Teams 3 @ 0:14:21 | Certificati post-quantum fino a "qualche centinaio di kilobyte" | Con ML-DSA qualche KB; SLH-DSA fino a circa 50 KB di firma | Nota |
| DI-03 @ 01:32:29 | "WAC, Web Access Certificates" | Certificato di autenticazione di siti web (QWAC nella variante qualificata) | Correzione |
| DI-03 @ 01:41:43 | A DigiNotar "hanno rubato la chiave pubblica di CA" | Chiave privata (lapsus; poco prima il docente dice "chiavi private") | Correzione |
| DI-03 @ 01:41:43 | DigiNotar "olandese, forse belga", "2011 mi pare", "dopo WannaCry" | Olandese, 2011, fallita a settembre 2011; WannaCry è del 2017 | Nota |
| DI-03 @ 01:46:45 | "La legge 445 del 2000" | D.P.R. 445/2000 | Correzione |
| DI-03 @ 01:53:23 | Passaporti italiani emessi dal "Ministero della Giustizia, mi pare" | Questure (Ministero dell'Interno); all'estero rappresentanze consolari | Correzione |
| DI-03 @ 01:28:40 | Firma = hash cifrato con la chiave privata | Modello RSA; per ECDSA, EdDSA, ML-DSA la firma non è una cifratura dell'hash | Nota |
| Teams 3 @ 0:42:57 | Fiducia "spesso intransitiva" e poi "transitivamente" | Nelle gerarchie è transitiva; nelle reti può essere vincolata (name/policy constraints) | Nota |

### Verifiche per esecuzione

- Analogia del 37 (slide *00:17:35*, Teams 2 @ 0:01:54): $37$ primo; $22 + 15$ e $33 + 4$ coppie coprime di non primi; i fattori 2, 3, 5, 11 non dividono 37; $11 \cdot 2 + 5 \cdot 3 = 11 \cdot 3 + 2 \cdot 2 = 37$. Corretto.
- Tabella BB84 della slide QKD (*00:53:49*): chiave setacciata 1, 1, 0 nelle posizioni 2, 4, 6. Corretta.
- Teams 2 @ 0:50:33: $256 - 100 = 156$ bit residui. Corretto.
- Esempio aggiunto di omomorfismo moltiplicativo di RSA: $E(6) \cdot E(7) \bmod 3233$ decifra a 42. Corretto.

### Fonti e anomalie

- DI-03 è integra (1:57:53) e corrisponde alla data a schermo (2025-10-17 16:07 UTC). Inizia a metà di una risposta a una domanda (registrazione avviata dopo l'inizio).
- Buchi della trascrizione: *00:13:27-00:13:37* (circa 10 s) e *01:24:22-01:24:51* (circa 30 s). A *01:40:42* interruzione di connessione di circa 30 s segnalata dagli studenti.
- Fra *00:12:34* e *00:12:44* il docente scorre il mazzo e passano per un istante slide di altre lezioni (firma, PAdES, JWE, PET).
- Trascrizione automatica, errori principali corretti nel manuale: "PADES" per PAdES; "AIDAS", "EIDAS" per eIDAS; "Agile", "agide" per AgID; "Digital Nota", "Digital Notar" per DigiNotar; "Bansi Castle" per Bouncy Castle; "samelle" per SAML; "IS-509" per X.509; "C.I.A.", "CIA", "Cia", "scia" per CA; "Task Service Provider" per Trust Service Provider; "ES", "AS", "a essa" per AES; "credito agilità" per cripto-agilità; "la litografia" per la crittografia; "Fips 203204205" per FIPS 203, 204, 205. Nelle trascrizioni Teams: "Delicious" per Dilithium; "ML cam", "ML chem" per ML-KEM; "Mary in the middle" per man in the middle; "hillsdropper" per eavesdropper; "route CA", "rut.ca" per root CA; "colder" per holder; "selfish" per self-issued.

### Differenze 2025 / 2026

- Nel 2026 il calcolo quantistico e la PQC sono spostati in Teams 1 (fine) e Teams 2; il digital trust parte in Teams 3.
- Nel 2026 gli standard NIST sono quattro (aggiunto FIPS 206, FN-DSA) e i nomi definitivi (ML-KEM, ML-DSA, SLH-DSA, FN-DSA) sostituiscono quelli colloquiali.
- Argomenti nuovi 2026: migrazione ibrida e rischio che diventi permanente, downgrade attack, inventario e catena di fornitura, ricifratura dei dati senza rompere la catena di custodia (sezione 9); BB84 spiegato per esteso e "inversione dell'onere della prova" della QKD; relying party; tre tipi di certificati elettronici eIDAS spiegati; chiavi di certificazione e certificati intermedi; topologie mesh e ad anello commentate, trust anchor, bridge CA; convalida a ritroso della catena; mercato B2B delle CA radice; RA e VA.
- Nel 2025 sono più ampi: cifratura per più destinatari, cifratura omomorfa in formule, slide sull'hardware quantistico, casi DigiNotar e Nvidia, libreria SAML insicura, esempio dei gate ICAO.


## Capitolo 04

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 04. Le voci "Correzione" sono certe; le "Nota" sono precisazioni o semplificazioni.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| DI-04 @ 00:43:40 | Diffie-Hellman inventato "negli anni Ottanta" | Pubblicato nel 1976 ("New Directions in Cryptography"), prima di RSA (1977) | Correzione |
| Slide DH (DI-04 @ 00:43:52) e DI-04 @ 00:44:11 | "Classic" DH "based on RSA encryption" | Il DH classico si basa sul logaritmo discreto modulo un primo, non su RSA; ECDH sul logaritmo discreto su curva ellittica | Correzione |
| Slide DH (DI-04 @ 00:43:52) | Titolo "Diffie-Hellmann" | Hellman (una sola n) | Correzione (refuso) |
| DI-04 @ 00:48:58 | "vi sfido a trovare che fosse 9" | La chiave privata di Bob è 4; 9 è la sua chiave pubblica | Correzione (lapsus) |
| DI-04 @ 00:48:58 | L'inversione del DH "è alla base della crittografia RSA" | Il problema difficile del DH è il logaritmo discreto (problema di Diffie-Hellman), non la fattorizzazione | Correzione |
| DI-04 @ 00:41:04; slide PFS (00:40:12); Teams 4 @ 0:43:53 | PFS = key wrapping della chiave effimera con la chiave pubblica del destinatario | Il wrapping con chiavi a lungo termine non dà forward secrecy (chi ottiene la privata decifra tutte le sessioni registrate); serve un accordo di chiave effimero (DHE/ECDHE), con le chiavi a lungo termine usate solo per firmare | Correzione |
| Slide DH (00:43:52) | "DH also employs PFS and, therefore, key-wrapping techniques" | È il DH effimero a fornire la PFS; il DH non usa key wrapping | Nota |
| DI-04 @ 00:35:31; Teams 3 @ 1:10:17 | La CRL è "solo per aggiunzione", X.509 vieta di rimuovere certificati | RFC 5280 prevede `certificateHold` (sospensione reversibile) e `removeFromCRL` | Correzione |
| Slide OCSP (00:33:02); Teams 3 @ 1:08:14 | Stati OCSP: valido, scaduto, sospeso, revocato | RFC 6960: *good*, *revoked*, *unknown*; "sospeso" = *revoked* con motivo `certificateHold`; la scadenza si legge dal certificato | Nota |
| Slide OCSP (00:33:02) | "one queried", "SSL/TSL", server etichettato "Web Client" | *once queried*, SSL/TLS, *Web Server* | Correzione (refusi) |
| DI-04 @ 00:33:54 | L'OCSP è consultato ogni volta che si convalida una firma | Molti browser non interrogano l'OCSP in linea; Let's Encrypt ha tolto gli URL OCSP il 7/5/2025 e spento i responder il 6/8/2025 | Nota |
| DI-04 @ 00:30:13, 00:36:01 | Carte di pagamento bloccate con CRL, sospese con OCSP | Analogia: nei circuiti EMV il blocco avviene nei sistemi autorizzativi dell'emittente (dato esterno) | Nota |
| Teams 3 @ 1:04:30-1:05:51 | X.509 nato negli anni '80 per la revoca; "il nome X.509 è il nome della CRL" | X.509 è la raccomandazione ITU-T del 1988 (serie X.500) che definisce certificati e CRL; il numero non è il nome della CRL | Correzione |
| DI-04 @ 00:15:20 | `google.com` registrato ad "Alphabet SA" | Alphabet Inc.; il dominio è intestato a Google LLC. Per i certificati DV basta la prova tecnica di controllo del dominio | Nota |
| DI-04 @ 01:05:16; Teams 4 @ 1:05:05 | Repubblica è "del gruppo La Stampa" | Entrambe sono testate del gruppo GEDI (dato esterno, al 2025) | Nota |
| DI-04 @ 00:59:53 | Certificato "dura due anni, scusate, un anno e un mese" | 395 giorni, meno un secondo (verificato) | Nota (autocorretta) |
| Teams 4 @ 1:12:40 | Firma RSA "poche decine di byte" | Una firma RSA-2048 è lunga 256 byte | Nota |
| Teams 4 @ 1:25:51-1:26:18 | Google ha annunciato certificati da 47 giorni entro il 2030 | Ballot CA/B Forum SC-081, proposto da Apple, approvato l'11/4/2025: 398 giorni fino al 14/3/2026, 200 dal 15/3/2026, 100 dal 15/3/2027, 47 dal 15/3/2029 | Correzione |
| Teams 4 @ 1:25:25 | Prima del 2012 standard certificati da 10 anni | Prassi di mercato; poi i Baseline Requirements hanno fissato massimi decrescenti (39 mesi, 825 giorni, 398 giorni) | Nota |
| Teams 4 @ 1:15:50 | Symantec siede nel CA/Browser Forum | L'attività CA di Symantec è passata a DigiCert nel 2017, le sue radici sono state rese non fidate nel 2018 | Nota |
| Teams 4 @ 1:29:55 | Il motore di Safari è basato su Chrome | Safari usa WebKit; Chrome/Edge usano Blink, fork di WebKit | Correzione |
| Teams 4 @ 0:53:27 | SSL è "un'implementazione matematica di Diffie-Hellman", sostituito da TLS | SSL e TLS sono protocolli; lo scambio di chiavi è una loro componente | Correzione |
| Teams 4 @ 0:52:39 | Alice e Bob "usano le chiavi private l'uno dell'altra" | Ciascuno usa la propria privata e la pubblica dell'altro | Correzione (lapsus) |
| Teams 4 @ 0:59:54 | DoS: la cifratura simmetrica di molte sessioni satura il server | La parte costosa è soprattutto l'handshake asimmetrico | Nota |
| Teams 4 @ 1:27:58 | TSP europeo fallito dopo un incidente (senza nome) | Con buona probabilità DigiNotar (2011); attribuzione non confermata | Nota |
| DI-04 @ 01:24:36 | "i 60 giga di un DVD" | Un DVD contiene 4,7 GB (singolo strato) o 8,5 GB (doppio) | Correzione |
| DI-04 @ 01:28:53; slide KDM (01:32:27); Teams 4 @ 0:17:13 | KDM firmata dal key management dell'esercente / dal Mastering Lab / dal distributore | Fonti discordanti fra loro: vedi Punti incerti | Divergenza fra fonti |
| Teams 4 @ 0:14:06 | Chiave del media block RSA "1024 o 2048 bit" | Le specifiche DCI indicano RSA-2048 (dato esterno, non verificato) | Nota |
| Teams 4 @ 0:34:22 | Nel chip del passaporto certificati CVC, l'unica alternativa a X.509 | I dati del chip sono firmati con certificati X.509 (Document Signer, CSCA); i CVC servono alla Terminal Authentication EAC e stanno nei terminali | Nota |
| Teams 3 @ 1:19:47 | SSCD come termine eIDAS | SSCD è il termine della direttiva 1999/93/CE; eIDAS parla di QSCD | Nota |
| Slide PKCS (DI-04 @ 01:41:29) | "PKCS – Public-Key Exchange (PKIX)", "PKIX Cryptography Standards" | PKCS = Public-Key Cryptography Standards (RSA Labs); PKIX = gruppo IETF Public-Key Infrastructure (X.509); la numerazione 1-13 della slide non è quella ufficiale (CSR = PKCS #10) | Correzione |
| Slide e-Passports (01:39:58) | "Part 2: … eIDAS" | Schema della BSI TR-03110: "eIDAS token" tedesco, non il regolamento UE | Nota |
| DI-04 @ 01:42:46 | Il GDPR è globale perché riguarda tutti i cittadini UE anche fuori dall'Unione | Art. 3 GDPR: conta lo stabilimento del titolare o che l'interessato si trovi nell'Unione, non la cittadinanza | Correzione |
| DI-04 @ 01:51:57 | Vigilanza "mi sembra almeno ogni due anni" | Art. 20 eIDAS: audit almeno ogni 24 mesi da un organismo di valutazione della conformità; l'organo di vigilanza può ispezionare in ogni momento | Nota (confermata) |
| DI-04 @ 01:57:06; slide DLT (01:57:49) | Ogni blocco è firmato da chi ha il permesso di scrivere | Vero per i registri *permissioned*; nelle blockchain pubbliche l'immutabilità viene da hash concatenati e consenso | Nota |
| DI-04 @ 02:05:56-02:09:10 | Con la VPN la radice della VPN compare per una mutua autenticazione | Il fenomeno è l'ispezione TLS: il software riemette il certificato del sito con una propria CA installata nel trust store | Correzione |
| DI-04 @ 01:37:28 | CieSign "non è firma remota… è firma remota nel senso che la smart card fa da HSM" | Autocontraddizione; nel 2026 il docente chiarisce: firma locale, "remota tra virgolette" | Nota |

### Fonti e anomalie

- DI-04: parlato fino a 2:11:10, poi solo silenzio e la lista dei partecipanti fino a 2:25:44. La domanda sulla VPN (01:03:39) ha risposta a registrazione formalmente conclusa (02:03:48-02:10:45).
- Durante tutta la spiegazione del cinema digitale (01:22:24-01:32:27) resta a schermo la slide "Key Registration"; la slide "Key Delivery Messages" compare solo alla fine.
- Le slide fra 00:19:12 e 00:20:38 sono di DI-03, scorse all'indietro per richiamare l'anatomia del certificato (capitolo 03).
- Nella dimostrazione dal vivo i frame conservati mostrano i visualizzatori di certificati solo per `repubblica.it`; per New York Times, Apple e Google solo le home page.
- Trascrizione automatica (correzioni principali): "Fjellman", "di Fjellman", "Fielman", "Diffielman", "DF hellman", "Difi hellman" = Diffie-Hellman; "Perfair for World Security", "Perfect for World Secrecy", "perfect for war sicre si" = perfect forward secrecy; "key-ropping", "key dropping" = key wrapping; "AIDAS", "EIDAS", "aidas" = eIDAS; "CED", "scie", "C", "Cie" = CIE; "CSI", "CESAR", "CESIGN", "shesign", "CSign" = CieSign; "KTM" = KDM; "Cia", "scia", "CAA" = CA; "lo CSP", "o CSP", "OCSPE" = OCSP; "UAC", "uac", "WAC" = WAC; "route", "RUT" = root (Amazon Root CA 1); "anti-tumper" = anti-tamper; "HSME", "LHSM", "h SM" = HSM; "CESAR forum" = CA/Browser Forum; "astampa" = lastampa; "conseguuzio temporum" = consecutio temporum; "valgazione" = validazione; "THOT" [?]; "Rilla" [?]; "UB key" = YubiKey [?]; "Arrichetti" = Arrighetti.

### Differenze 2025 / 2026

- Nel 2025 la revoca, la gestione delle chiavi, TLS, HSM, KDM, firme remote e i servizi fiduciari stanno in una sola lezione (DI-04); nel 2026 sono distribuiti fra la seconda metà di Teams 3 (revoca, HSM, CSR), Teams 4 (KDM, firme remote, documenti, PFS, TLS) e Teams 5 (servizi fiduciari, capitolo 05).
- Nel 2026 l'esempio numerico di Diffie-Hellman non viene svolto.
- Il certificato de La Stampa cambia: 2025 emesso da Amazon RSA 2048 M02, valido 8/12/2024-7/1/2026; 2026 da "M04" [?], valido 8/11/2025-7/12/2026. L'intermedio (24/08/2022-24/08/2030) è lo stesso.
- Solo nel 2026: CA/Browser Forum, Web PKI, data governance, riduzione della durata dei certificati TLS, caso del prestatore fallito, DoS e load balancing, Teams come esempio di PFS, CIE con due chiavi ed "Entra con CIE" livello 3, controllo del passaporto al gate (tre foto, PACE), conto bancario sospeso e verifica nel passato con OCSP, attacchi agli HSM tramite i backup, Secure Enclave e TPM.
- Solo nel 2025: esempi su New York Times, Apple e Google; domanda sulla VPN; blockchain e marcatura temporale (nel 2026 nel capitolo 05).


## Capitolo 05

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 05. Le voci "Correzione" sono certe; le "Nota" sono precisazioni o semplificazioni.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| DI-05 @ 00:26:53 | "la firma elettronica **avanzata** ... è analoga in tutto e per tutto alla firma autografa" | Dal contesto è la **qualificata**: equivalenza all'autografa = art. 25(2) Reg. 910/2014, solo FEQ | Correzione (lapsus) |
| Teams 5 @ 0:01:13 | eIDAS = "Electronic identification and advanced signing" | electronic IDentification, Authentication and trust Services | Correzione |
| Teams 6 @ 0:20:42 | L'allegato II di eIDAS descrive i certificati qualificati di sigillo | Allegato I: certificati qualificati di firma; **II: QSCD**; **III: certificati qualificati di sigillo**; IV: siti web | Correzione |
| DI-05 @ 01:26:11 | Lo standard ISO dei LoA va da 0 "fino al 6 o al 5" | ISO/IEC 29115 ha quattro livelli, LoA 1-4; eIDAS usa (loosely) 2, 3, 4 | Correzione |
| Slide JAdES (DI-05 @ 00:58:18) | Token d'esempio presentato come JWT firmato JAdES | Il token è l'esempio di jwt.io: `HS256` (HMAC simmetrico, chiave `your-256-bit-secret`, verificato), payload "John Doe"; non corrisponde all'header `ES256` né al payload sanitario della slide | Correzione |
| DI-05 @ 00:57:50 | JAdES = "JSON Advanced Digital Electronic Signature" | ETSI TS 119 182-1: JSON Advanced Electronic Signatures | Correzione |
| DI-05 @ 00:56:44; Teams 6 @ 0:52:03 | JWT come "codifica in base 64" | base64url (RFC 4648 §5), senza padding | Nota |
| Teams 6 @ 0:51:59 | Il payload JSON viene "canonicalizzato" prima della firma | JWS (RFC 7515) firma i byte codificati, senza canonicalizzazione | Nota |
| Teams 6 @ 0:35:17, 0:36:52, 0:38:11, 0:49:38 | "enveloped" per il `.p7m` e per la firma a matrioska | Secondo la slide del docente il `.p7m` è **enveloping**; enveloped è il PDF | Correzione |
| Teams 5 / Teams 6, trascrizione | Acronimo "FEC", "FAQ" per la firma qualificata | FEQ | Correzione (trascrizione) |
| Slide "PDF signature wrapping attack" (DI-05 @ 00:52:36) | Titolo "signature wrapping" | Le figure illustrano uno *shadow attack* e un attacco alle firme di certificazione (pdf-insecurity.org); il signature wrapping è una famiglia distinta | Nota |
| DI-05 @ 01:39:40-01:41:52 | Kerberos nato nei primi anni '90; Microsoft lo usa "fin dagli anni '90"; algoritmo RC4 | MIT, metà anni '80 (v5: RFC 1510, 1993); Microsoft lo adotta con Windows 2000; v5 usava DES, RC4-HMAC è un'aggiunta Microsoft | Nota |
| DI-05 @ 01:17:44 | Il film di Salvatores è "di dieci anni fa" | "Il ragazzo invisibile: seconda generazione" è del 2018 (circa sette anni) | Nota |
| DI-05 @ 01:38:37 | PIN dispositivo come fattore "di possesso" | Un PIN è un fattore di conoscenza | Nota |
| DI-05 @ 01:34:40 | La carta "cifra" il blob con la chiave privata, il lettore chiede di "decifrare" | È una firma della challenge (la slide dice "signing a blob") | Nota |
| DI-05 @ 01:26:42 | Livelli eIDAS "basso, sostanziale, alto" | Testo italiano del regolamento (art. 8): basso, significativo, elevato | Nota |
| DI-05 @ 00:01:08 | QTSP fra i "fornitori di servizi essenziali" NIS 2 | NIS 2 parla di "soggetti essenziali" (allegato I); "OSE" era la terminologia NIS 1 | Nota |
| Teams 6 @ 0:25:33 | L'inversione dell'onere della prova vale solo per la FEQ, "non per il sigillo qualificato" | Vero per l'equivalenza all'autografa; il sigillo qualificato ha comunque una presunzione di integrità e origine (art. 35(2)) | Nota |
| DI-05 @ 00:25:51 vs Teams 6 @ 0:15:35 | 2025: per vendere casa la FEA non basta, serve il notaio; 2026: per la compravendita "la FEQ è sufficiente" | Coerenti: art. 21 c. 2-bis CAD richiede FEQ o firma digitale per gli atti dell'art. 1350 nn. 1-12; per la trascrizione serve comunque l'autentica notarile | Nota |
| Teams 5 @ 0:12:29 | Italia e Malesia si contendono il primato mondiale (1997) | Malesia: Digital Signature Act 1997; lo Utah aveva una legge nel 1995 (statale) | Nota |
| Teams 6 @ 0:29:03 | Autorità di vigilanza UK "se non sbaglio il Cabinet Office" | Lo SI 2016/696 indica l'Information Commissioner (ICO); verifica non conclusiva | Nota |
| Teams 5 @ 0:36:09 | Il libero professionista appone sigilli elettronici | eIDAS definisce il creatore di sigillo come persona giuridica | Nota |

### Fonti e anomalie

- **DI-05**: OCR indice assente (Apple Vision bloccato); le slide sono state individuate scorrendo i nomi dei frame e guardandone 91 su 145. La finestra del certificato qualificato nel laboratorio (00:39:36-00:42:20) non è catturata da nessun frame.
- Diverse slide scorrono in pochi secondi senza commento (00:52:27-00:52:36, 01:20:45-01:21:42, 01:39:02-01:39:36): elencate nel manuale.
- Trascrizione automatica, principali errori corretti: "EIDAS", "EITA", "EDAS", "AIDAS", "Aidas" per eIDAS; "Arrichetti", "Arighetti" per Arrighetti; "Agile" per AgID; "scia" per CIE; "JADES", "jales", "jaze" per JAdES; "PADES", "Pade", "CADES", "XADES" per PAdES, CAdES, XAdES; "Signature Ropping/hopping/dropping Attack" per signature wrapping; "pdf in security.org" per pdf-insecurity.org; "di Touched", "D touched" per detached; "OTPD" per OTP; "Speed" per SPID; "Entry ID" per Entra ID; "Gabriele Salvatore" per Gabriele Salvatores; "liride" per l'iride; "frescia" per refresh; "Pkcs7" per PKCS#7; "QTSPE" per QTSP; "JVS", "JX" per JWS, JAdES; "know how" per OAuth; "asic e" per ASiC-E; "Meta INF" per META-INF; "FEC", "FAQ" per FEQ.
- Nomi di studenti presenti nell'audio e nelle miniature Teams: omessi.

### Differenze 2025 / 2026

- Nel 2026 il docente introduce eIDAS da zero in Teams 5 (fonti normative italiane e internazionali, Brexit, modello fiduciario); nel 2025 lo aveva fatto nella lezione precedente (DI-04, capitolo 04).
- Nel 2026 i quattro requisiti della FEA, gli artt. 56 e 61 del DPCM firme, l'art. 21 c. 2-bis CAD, la firma grafometrica, il QSCD e il "bit" di qualifica sono spiegati per esteso; nel 2025 sono solo accennati.
- Nuovi nel 2026: PEC come FEA e come recapito certificato, marca temporale e TSA (con l'aneddoto dei due miliardi), registri distribuiti, ASiC-E, controfirma per le deleghe, profili LT/LTA, consiglio enveloping/detached.
- Nel 2026 non c'è il laboratorio live sul PDF: il docente descrive a parole la finestra del certificato in Acrobat.
- Nel 2025 la seconda metà della lezione (autenticazione, fattori, biometria, identity proofing, LoA, smart card, SSO, Kerberos) anticipa temi che nel 2026 sono trattati in Teams 6 da 1:01:49 e in Teams 7-8: integrazioni nel capitolo 06.


## Capitolo 06

Errori, imprecisioni e differenze fra fonti rilevati nel capitolo 06. Le voci "Correzione" sono certe; le "Nota" sono precisazioni, semplificazioni o fatti esterni aggiunti.

| Dove | Cosa dice la fonte | Cosa è corretto | Tipo |
|---|---|---|---|
| Slide "OAuth 2.0 – Authorization Code Grant" (DI-06 @ 00:54:12) e "Implicit Grant" (00:54:52) | Authorization Code Grant con `response_type=token`, Implicit Grant con `response_type=code` | Valori scambiati: RFC 6749 prevede `code` per l'Authorization Code Grant e `token` per l'Implicit Grant | Correzione |
| Slide "Implicit Grant" (DI-06 @ 00:54:52) | "Access token grant (GET)": `access_token=...&token_type=Bearer` | Il token torna nel fragment dell'URI di redirect; l'Implicit Grant è sconsigliato (RFC 9700, 2025) e assente da OAuth 2.1 | Nota |
| Slide "Authorisation flows with OAuth 2.0" (DI-06 @ 00:54:43) | Access token = JWT firmato | In RFC 6749 il token è opaco; il profilo JWT è RFC 9068, scelta comune ma non obbligatoria | Nota |
| Slide "SPID and its assurance levels" (DI-06 @ 01:14:44); voce DI-06 @ 01:12:54, Teams 8 @ 1:12:28 | LoA 2 = "MEDIUM", "medio" | eIDAS: low / substantial / high (testo italiano: basso / significativo / elevato). La slide di DI-06 @ 00:01:08 dice correttamente "LOW = LoA 2" | Correzione |
| DI-06 @ 01:00:27, Teams 8 @ 0:45:29-0:47:44 | Nel JWT c'è "l'hash del nome"; la disclosure è "la base64 della stringa del nome" | La disclosure è la base64url di `[sale, nome claim, valore]` e il digest è lo SHA-256 della disclosure (sale compreso), RFC 9901; la slide è corretta | Correzione |
| Teams 8 @ 0:37:24; DI-06 @ 00:57:51 | Nella VP i dati sono "tipicamente cifrati" | Non cifrati: sostituiti da digest; il docente si corregge in DI-06 e in Teams 8 @ 1:35:28 | Correzione (anche del docente) |
| Slide SD-JWT (DI-06 @ 00:58:08) | Esempio con header `HS256` e payload senza `_sd` | È il JWT di esempio di jwt.io (decodifica verificata); un SD-JWT VC reale è firmato con chiave asimmetrica e ha `_sd`, `_sd_alg`, `cnf` | Nota |
| Teams 7 @ 0:33:43 | SAML "nato in seno al W3C" | SAML è uno standard OASIS (2.0 del 2005); del W3C sono XML Signature/Encryption | Correzione |
| Teams 7 @ 0:24:46, 0:33:14 | Kerberos "primi anni '90" | MIT, Progetto Athena, metà anni '80; v5 RFC 1510 (1993), oggi RFC 4120. In Teams 1 il docente diceva "anni '80" | Correzione |
| Teams 7 @ 0:24:46 | Kerberos "protocollo di autorizzazione" | È di autenticazione: il docente si corregge a Teams 7 @ 0:32:55 | Correzione (del docente) |
| Teams 7 @ 0:37:28 | OAuth = "open authentication", poi "open authorization" | OAuth non è formalmente un acronimo; è un framework di autorizzazione | Nota |
| Teams 7 @ 0:40:16 | OIDC ha "un decennio scarso" | OpenID Connect Core 1.0: febbraio 2014, circa 12 anni nel 2026 | Nota |
| Teams 8 @ 0:58:04 | SPID = "servizio pubblico d'identità digitale" | Sistema Pubblico di Identità Digitale (anche nella slide DI-06 @ 01:12:35) | Correzione |
| Slide bibliografia (DI-06 @ 01:46:20) | Shannon, Towe, Tonguz, arXiv, 2003, arXiv:2003.07907 | L'ID 2003.07907 indica marzo 2020 | Correzione |
| Slide bibliografia (DI-06 @ 01:46:20) | "B. Diu, F. Laloë, C. Cohen-Tannoudji" | Ordine abituale: Cohen-Tannoudji, Diu, Laloë | Nota |
| Slide "Federated identity" (DI-06 @ 00:19:52) | "*either* ... *and*"; "wsers" | Dal parlato: condizioni alternative ("o ... o"); "users" | Nota |
| Slide "Identity federation and its providers" (DI-06 @ 00:20:03) | Sigla "EEA" accanto a "EAA" | La sigla eIDAS 2 è EAA | Nota |
| Slide "Identity delegation" (DI-06 @ 00:30:59) | "Bog Bingleby on behalf of Acme s.r.l." | Refuso per "Bob" | Nota |
| Slide "EUDI Wallet" (DI-06 @ 01:27:04) | "Strong customer authetication" | Refuso | Nota |
| Slide ARF (DI-06 @ 01:30:15) | "QEEA", "EEA" | QEAA, EAA | Nota |
| Teams 6 @ 1:40:04 | La PSD2 chiede di riautenticare "l'esercente" | Si riautentica l'utente pagatore (operazioni dispositive dell'home banking) | Nota |
| DI-06 @ 01:41:52 | Primi obblighi del wallet "nella primavera del 2026", privati nel 2027 | Calendario eIDAS 2: wallet di ogni Stato entro dicembre 2026; accettazione obbligatoria per i privati dei settori previsti entro circa dicembre 2027 | Nota |
| Teams 8 @ 1:42:04 | PagoPA "comprata nel 2026" da Poste e IPZS | Confermato: acquisizione perfezionata ad agosto 2026, Poste 49%, IPZS 51% | Nota (verificata) |
| DI-06 @ 01:24:01 | Obbligo di notificare almeno uno schema "entro sette anni" | Con eIDAS 1 la notifica risulta facoltativa; non verificato se l'obbligo venga da eIDAS 2 | Nota (incerta) |

### Fonti e anomalie

- DI-06 è completa (parlato fino a 1:46:32). A 00:41:01-00:42:51 il docente cambia file di slide perché "non era la versione giusta" e recupera la slide "Electronic Identification".
- Le prime slide di DI-06 (standard, identity proofing) sono le "slide ritrovate" della lezione precedente (DI-05): il testo è riportato qui perché DI-06 le riproietta.
- Fra 01:27:48 e 01:28:47 il docente torna indietro sulle slide SPID (numeri, CIE, livelli, attributi) e poi riparte dall'EUDI Wallet.
- Teams 2026 senza slide: le corrispondenze con le slide 2025 sono ricostruite dal parlato.

### Trascrizione automatica (Whisper e Stream): principali errori corretti nel manuale

- eIDAS: "EIDAS", "AIDAS", "aidas", "EGAS", "EDAS", "elas", "ODE Aidas" (= nodi eIDAS).
- SPID e CIE: "speed", "Speed", "CEO speed" (= CIE/SPID), "CE", "CED", "scie", "scive", "scia", "Cie", "CID", "CIAID" (= CieID).
- Ruoli: "lishware", "iswer", "ishuer", "l'issue" (= issuer); "loader", "hold" (= holder); "re line party", "Relay in Parti", "Reline party", "LINE Party" (= relying party); "Identities provider" (= identity provider); "Identities proofing" (= identity proofing).
- Protocolli: "Samen", "samelle", "samel", "Sunel" (= SAML); "out", "oaut", "ohouse", "House", "o off" (= OAuth); "JVT", "JVS" (= JWT, JWS); "J son", "Jason" (= JSON); "Selected Disclosure", "JSDJWT" (= selective disclosure, SD-JWT); "jaze", "JAIDS", "J" (= JAdES); "kr BTGT" (= krbtgt); "MSDS Allout delegate to" (= msDS-AllowedToDelegateTo); "V tre C" (= W3C).
- Nomi: "Bogbingabai", "BogBingoPi", "Bog Bing by", "bogbingleby" (= Bob Bingleby); "ACMES RL", "acma SRL", "yakno SRL" (= ACME S.r.l.); "Pargo.pa", "pago PA" (= PagoPA); "eT-wallet", ". it Wallet" (= IT-Wallet); "U di wallet", "UD Wallet", "Euding Wallet", "WD Wallet" (= EUDI Wallet); "arf" (= ARF); "agit", "Agid" (= AgID); "IMS", "IMSS" (= INPS); "PZS" (= IPZS); "Ial", "eal" (= IAL); "QB di sessione" (= cookie di sessione); "baseword", "password" nel senso di buzzword (Teams 8 @ 0:17:45, 0:23:55).

### Differenze 2025 / 2026

- **Struttura.** Nel 2025 tutto il blocco identità sta in una lezione (DI-06, più l'inizio in DI-05); nel 2026 occupa la seconda metà di Teams 6 (dal 1:01:44), Teams 7 e Teams 8, circa quattro ore.
- **Nuovo nel 2026:** identità digitale contro account; KYC e onboarding; livelli IAL spiegati a voce; deepfake e digital double nell'identity proofing; Secure Element; fattori di autenticazione (possesso reale, "quarto fattore", conteggio dei fattori); autenticazione locale con smart card; SCA e dynamic linking; riautenticazione PSD2; re-proofing; trasferimento del rischio e assicurazione cyber degli IdP SPID; Kerberos con TGT e service ticket; foreste AD; deleghe AD (unconstrained, constrained, RBCD); rischi del single sign-on; accountability nelle deleghe; esempi CILA, patente, laurea per VC/VP/SD-JWT; nodi eIDAS come "torre di Babele"; PID provider IPZS; acquisizione di PagoPA; previsione di "eclissamento di SPID"; problema politico dei dispositivi; fornitori di schemi di attributi.
- **Più breve nel 2026:** OAuth e OIDC (nessuna slide e "non lo vediamo nel dettaglio"); SAML solo descritto; nessun numero SPID dettagliato.
- **Esclusioni d'esame esplicite solo nel 2026** (attributi SPID/CIE, slide SD-JWT, frecce del diagramma EUDI); una sola indicazione positiva: i ruoli dell'EUDI Wallet.


