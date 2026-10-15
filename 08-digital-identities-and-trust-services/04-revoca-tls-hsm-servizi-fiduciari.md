# 04 - Convalida e revoca dei certificati, gestione delle chiavi, Diffie-Hellman e TLS, HSM, KDM, firme remote, servizi fiduciari eIDAS, blockchain e marcatura temporale

*DI-04, registrazione Teams del 27/10/2025 (portale; a schermo "2025-10-27 17:06 UTC"), 2:25:44; parlato fino a 2:11:10, poi silenzio. Integrazioni da Teams 3 (dalla revoca dei certificati, 1:00:00-1:34:17) e Teams 4 (intera, 1:31:35).*

> **Come leggere questo capitolo.** I primi venti minuti riprendono le infrastrutture a chiave pubblica spiegate in DI-03 (capitolo 03), qui riassunte con le slide mostrate. Il cuore della lezione è il "digital trust in pratica": scadenza e revoca dei certificati (sezioni 4-5), il secondo problema applicativo, cioè la segretezza delle chiavi segrete (sezioni 6-8), TLS con la dimostrazione dal vivo sui certificati di siti reali (sezioni 9-10), HSM, CSR, cinema digitale e firme remote (sezioni 12-16). Nell'ultima mezz'ora il docente introduce i servizi fiduciari eIDAS (sezioni 17-19): nel 2026 questi argomenti stanno nella lezione Teams 5, quindi i dettagli 2026 sono nel **capitolo 05**. La sezione 11 è contenuto solo 2026 (CA/Browser Forum e durata dei certificati TLS). Gli esempi numerici e crittografici sono **verificati per esecuzione** (Python), come indicato sezione per sezione.

## Indice

1. Ripresa: topologie delle PKI
2. Convalidare un certificato risalendo la catena
3. CA tecnica e CA amministrativa, Registration Authority e Validation Authority
4. La scadenza: la morte programmata dei certificati
5. La revoca: trust list, CRL, OCSP
6. Il secondo problema: la segretezza delle chiavi segrete e il loro ciclo di vita
7. Perfect forward secrecy
8. Diffie-Hellman con numeri piccoli
9. TLS, HTTP e HTTPS, certificati di autenticazione di sito web
10. Laboratorio: i certificati di Repubblica (La Stampa), New York Times, Apple, Google
11. Solo 2026: CA/Browser Forum, Web PKI e durata dei certificati TLS
12. Hardware Security Module (HSM)
13. Registrazione delle chiavi e Certificate Signing Request (CSR)
14. Gestione delle chiavi nel cinema digitale: le Key Delivery Message
15. Firme remote e firma con la CIE
16. Passaporti elettronici e standard PKCS
17. Servizi fiduciari eIDAS: qualificati e non qualificati
18. Registri distribuiti e blockchain
19. Marcatura temporale elettronica
20. Domanda finale: VPN e certificati radice
21. Glossario
22. Punti incerti
23. Esame

## 1. Ripresa: topologie delle PKI

*DI-04 @ 00:00:01-00:06:50*

La lezione riparte da DI-03: un'**infrastruttura a chiave pubblica** (PKI) è un insieme di autorità di certificazione (CA). Può essere un insieme di CA tecniche (computer e software) dentro la stessa azienda oppure un insieme di CA di aziende diverse, con ruoli diversi, che "si trustano", cioè si fidano digitalmente l'una dell'altra.

**Slide "Public Key Infrastructure"** (*DI-04 @ 00:00:04*). Testo: "A public key infrastructure (PKI) is a *directed graph* whose nodes are CAs and whose links are digital trust relations." Tre schemi: *Hierarchical PKI* (rosso: *Root CA* → due *intermediate sub-CA* e una *leaf sub-CA*; sotto le intermedie, due *leaf sub-CA*), *(full) Mesh PKI* (verde: cinque CA collegate tutte con tutte) e *Ring (mesh) PKI* (blu: cinque CA in anello orientato).

- **Gerarchica**: un albero capovolto. La CA radice emette certificati **intermedi** alle CA sottostanti; una CA intermedia può emettere direttamente certificati finali o certificare altre CA intermedie, fino alle CA **foglia**, che emettono solo certificati finali. La gerarchia può essere cortissima o molto lunga, secondo la complessità tecnica e organizzativa (*DI-04 @ 00:01:08*).
- **Certificati finali**, detti foglia o dell'**utente finale** (*end entity*): sono certificati a chiave pubblica che attestano le chiavi di Alice, Bob, Eva, oppure **certificati di attributo**, che attestano il possesso di un attributo invece della titolarità di una chiave. I certificati delle CA sono anch'essi a chiave pubblica: asseriscono la chiave che la CA usa per firmare altri certificati (*DI-04 @ 00:02:11*).
- **A grafo (mesh)**: cambia totalmente il modello di fiducia (*trust model*). Il docente non entra nei dettagli, "materia per specialisti" (*DI-04 @ 00:03:14*). L'analogia: nel gerarchico ci si fida via via di CA più alte, come nel medioevo, quando per una transazione fra villaggi o città-stato diverse si risaliva a un testimone fidato da entrambi, magari a 2, 3, 4, 5 livelli di distanza. Nella mesh più CA "in cerchio" si fidano l'una dell'altra, la "cerchia ristretta degli amici".

**Slide "PKI Taxonomy"** (*DI-04 @ 00:02:15*). Legenda: *Root certificate (self-signed)*, *Intermediate (CA) certificate*, *Leaf / End-user (public-key) certificate*. Testo: "CAs may be distinguished and qualified according to both their position with respect to the PKI topology, and to whether they issue leaf certificates (*aka* end-user certificates): root CA; subordinate CA ("sub-CA"); leaf / peripheral CA; internal CA; intermediate CA; bridge CA." A destra due gerarchie: una *Root CA* che certifica direttamente un *user*, e una *Root CA* con due *intermediate sub-CA*, una *leaf sub-CA* e utenti ai vari livelli.

**Slide "Hybrid PKI topologies, Trust Models"** (*DI-04 @ 00:05:51*). A sinistra un grafo di fiducia fra persone (*Ingo Myself*, *Eva Friend*, *Axel Friend*, *Manuel Stranger*, *Susi Stranger*, *Manfred Stranger*) con archi *direct trust* e *indirect trust*; a destra una *bridge CA* collegata a due *local root CA*, una con gerarchia rossa e una con gerarchia viola.

- **Bridge CA** (*DI-04 @ 00:04:41*): CA ponte che unisce le infrastrutture di fiducia di organizzazioni, nazioni, gruppi che altrimenti non si fiderebbero degli esterni. Ha un legame di trust con le radici di due PKI gerarchiche e consente a chi si fida di una di fidarsi anche dell'altra.
- **Scenario fra Stati** (*DI-04 @ 00:05:24*): ogni Stato ha la sua PKI (gerarchica, o ad anello per i servizi privati); per fidarsi a vicenda non si usa una sola CA ponte, che dovrebbe stare in uno degli Stati ("come si fa a fidarsi?"), ma una **mesh completa di più CA ponte**, una per Stato, ciascuna fidata da tutte le altre.

**Slide "Multi-tier PKIs"** (*DI-04 @ 00:06:52*), non commentata in dettaglio. A sinistra lo schema *Three-Tier CA Hierarchy*: TIER 1 *Root CA / Issuing CA* con "An Offline Hardware Security Module Stores the Root CA's Private Key" e *Root CA Certificate*; TIER 2 due *Intermediate CA* con "An Online HSM Stores the Intermediate & Issuing CAs' Private Keys"; TIER 3 due *Online Issuing CA* con *Online ICA Certificate*, sotto quattro *Leaf Certificate*. A destra una mesh di cinque CA rosa da cui pendono gerarchie di colori diversi (lo scenario "fra Stati" appena descritto).

## 2. Convalidare un certificato risalendo la catena

*DI-04 @ 00:06:50-00:11:21*

Come si realizza tecnicamente il digital trust? Dal basso, dal certificato finale (*end entity*) che contiene la chiave pubblica di Alice. Il problema a monte è sempre lo stesso: di chi è la chiave pubblica di Alice?

Il procedimento, sull'esempio colorato del docente (*DI-04 @ 00:07:29-00:10:14*):
1. il certificato di Alice (celeste) dice che la chiave verde è di Alice ed è firmato dalla **CA celeste**; recupero la chiave pubblica della CA celeste e verifico la firma. Tecnicamente so che la CA celeste ha firmato, ma non la conosco;
2. la chiave pubblica della CA celeste la recupero anche dal **certificato di certificazione** della CA celeste, pubblicato nel suo repository: è firmato dalla **CA intermedia arancione**; verifico la firma con la chiave pubblica dell'arancione;
3. non conosco nemmeno l'arancione (magari sta in un altro Stato): il suo certificato è firmato dalla **CA verde**, il cui certificato è **autofirmato**, cioè firmato con la chiave privata corrispondente alla chiave pubblica contenuta nel certificato stesso;
4. davanti a un certificato autofirmato "posso fare ben poco": o mi fido della CA radice, o non ho più alcun modo di fidarmi dell'intera catena. Se mi fido, e se tutti i certificati risultano tecnicamente validi, a cascata posso dare valore all'identità di Alice.

**Slide "More on hierarchical PKIs"** (*DI-04 @ 00:10:59*). A sinistra: *Root certificate (Root)*, *self-signed*, con *Digital signature / Issuer: Root / Public key*; firma (*sign*) due *Intermediate certificate* (CA1, CA2) con *Issuer: Root*; sotto, tre *End-entity certificate* (C1 con *Issuer: CA1*, C2 e C3 con *Issuer: CA2*). A destra la catena di verifica: certificato con *Owner's DN, Owner's public key, Issuer's (CA) DN, Issuer's (CA) signature* → *Get certificate* → certificato dell'emittente con *Issuer's (Root CA) DN* → *Get certificate* → *Root CA's DN, Root CA's public key, Root CA's signature*, con frecce *Verify signature* all'indietro.

Quando mi fido di una CA mi fido di **tre cose** (*DI-04 @ 00:10:48*): che sappia **identificare** Alice prima di rilasciarle un certificato; che sappia **mantenere privata** la propria chiave privata; che emetta certificati solo a soggetti che rispettano certi **limiti**, tipicamente normativi. Mi basta fidarmi di una qualunque CA della catena (verde, arancione o celeste) per fidarmi della chiave di Alice.

Fra 00:19:12 e 00:20:38 il docente scorre all'indietro alcune slide di DI-03 per richiamare l'anatomia del certificato: **"Certification authorities"** (*00:19:13*), **"Digital (and electronic) certificates"** (*00:19:17*), **"Trust taxonomy"** (*00:20:27*). Testo e commento sono nel capitolo 03. Della slide "Trust taxonomy" vale la pena ricordare i tre requisiti con cui le terze parti si fidano di una CA, che corrispondono a quelli appena detti a voce: "keep its own CA private key private; identify any subjects to whom it issues public-key or attribute certificates; confirm whether any information stated in its issued certificates is true, accurate and current (e.g. by means of certificate **validation**)".

## 3. CA tecnica e CA amministrativa, Registration Authority e Validation Authority

*DI-04 @ 00:11:21-00:16:22*

Chi rilascia i certificati? Per le **CA tecniche** (prodotti software o hardware: "l'OpenSSL di turno o l'HSM") si dice che "la CA rilascia il certificato": è vero, il mestiere di formare il file, applicare la firma e pubblicarlo lo fa una componente tecnica. Ma una **CA amministrativa** (un'azienda) ha, oltre alla componente tecnica che genera i certificati e custodisce le chiavi private, **altre due componenti organizzative** (*DI-04 @ 00:11:55*).

**Slide "Registration and validation authorities"** (*DI-04 @ 00:11:20*). Schema a scrivanie: il titolare manda la richiesta alla *RA*, che passa l'*OK* alla *CA*; la *CA* rilascia il certificato al titolare e pubblica i certificati verso la *VA*; il titolare usa il certificato con *shop.com*, che chiede alla *VA* e riceve un *OK*. Testo:

> A **registration authority** (**RA**) takes care, on behalf of the administrative CA, of the identity proofing / verification of entities requesting to the CA the issuance of public-key / attribute certificates.
>
> A **validation authority** (**VA**) provides services for third parties to validate certificates issued by the CA. Validation may be sought after at either current time, or at a past/future date-time.

**Registration Authority** (*DI-04 @ 00:12:25-00:15:51*): è lo sportello dove va Alice per chiedere un certificato.
- Persona fisica: un documento d'identità.
- Persona giuridica: un documento che attesti la registrazione come impresa, cooperativa, società in nome collettivo; poiché a registrarsi va comunque una persona fisica, le si chiede di provare che siede nel board, che è amministratore delegato, presidente del CdA, o che ha la delega con potere di firma (*power of attorney*), per esempio dal registro delle imprese o dall'indice delle pubbliche amministrazioni.
- Macchina: processo simile ma digitale.

"Sportello" è un'analogia: oggi la registrazione (*onboarding*) avviene anche online, a volte con un contatto di persona via webcam, a volte in modo del tutto automatico, soprattutto per i nomi macchina. Per un certificato di sito web bisogna dimostrare di essere titolari del dominio: non si può chiedere un certificato per `google.com` presentando la propria chiave pubblica. Chi emette controlla nei registri dei domini (non uno solo, uno per ogni Stato) a chi è registrato il dominio e chiede la prova del *power of attorney* della società titolare.

> **Nota aggiunta:** il docente dice che `google.com` è registrato ad "Alphabet SA". La capogruppo è Alphabet Inc. (Delaware, sede in California, come dice lui stesso in Teams 4 @ 0:57:49) e il dominio risulta intestato a Google LLC. Inoltre per i certificati TLS comuni (*Domain Validated*) la prova richiesta è solo tecnica: controllo del dominio via DNS, HTTP o email (protocollo ACME e simili), senza verifiche societarie; queste ultime servono per i certificati OV ed EV.

**Validation Authority** (*DI-04 @ 00:15:51*): a lei si rivolgono le terze parti che devono convalidare i certificati. Il processo di convalida comporta recuperare i certificati della catena: nel certificato stesso c'è scritto come risalire alle chiavi pubbliche, ma nei sistemi più sicuri c'è un **registro online** per verificare la validità "in maniera puntuale". Il perché sta nelle due sezioni seguenti.

## 4. La scadenza: la morte programmata dei certificati

*DI-04 @ 00:16:22-00:25:50*

I certificati digitali sono file che seguono lo standard **X.509**. Una volta creati non si possono modificare, perché vengono distribuiti "a pioggia" a tutti quelli che li usano per convalidare chiavi e attributi: sono oggetti pubblici, chiunque può averli. Che succede se il titolare non vuole più usare la chiave, o se un attore della minaccia compromette, ruba, modifica la chiave privata, o c'è anche solo il **sospetto**? I certificati non si possono ritirare. Il primo strumento è la **scadenza** (*DI-04 @ 00:16:54-00:18:29*).

Oltre ai quattro campi minimi visti in DI-03 (chiave pubblica o attributi, nome distintivo della CA emittente, nome del titolare, firma digitale), nello standard X.509, e anche nel formato **CVC**, è obbligatorio il **periodo di validità**: una data *not before* e una data *not after*, nella parte firmata del certificato, quindi non contraffabili senza invalidare la firma (*DI-04 @ 00:19:01-00:20:05*).

L'analogia biologica: l'**apoptosi**, la morte programmata. Firmando il certificato la CA ne "sancisce la data di morte", fra un secondo o fra 60 anni, anche fra 600, ma una data finita è obbligatoria (*DI-04 @ 00:20:05-00:20:35*).

Durante la convalida, **staticamente**, senza interrogare nessuno all'esterno, si controlla l'orario per tutti i certificati attraversati, dal finale alla radice (se mi fido già della CA celeste convalido solo il certificato di Alice e quello della CA celeste). Se anche uno solo è fuori tempo massimo, la convalida ha esito negativo, anche se tutte le firme sono tecnicamente valide (*DI-04 @ 00:21:07-00:22:14*).

Il collegamento con la **cripto-agilità** del capitolo 01 (*DI-04 @ 00:22:44-00:25:18*): tutte le smart card (passaporto, carta d'identità, permesso di soggiorno elettronico) e tutte le carte di pagamento, anche virtuali, scadono perché dentro c'è una chiave privata e il **certificato** della chiave pubblica corrispondente con una data di scadenza. Sulla carta si legge "12/26", nel certificato "31 dicembre 2026 23:59:59". Dopo quella data il gate o il POS rifiuta la carta anche se tecnicamente tutto funziona come prima: il chip si accende, la chiave privata "fa il suo dovere", ma il dispositivo di convalida legge che il certificato è scaduto. Chi emette ha così il tempo di passare ad algoritmi più robusti: entro una certa data tutte le carte vecchie saranno comunque scadute.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 4 (scadenza)*

- Stesso ragionamento: la scadenza è codificata all'origine nei metadati del certificato, quindi non serve chiederla online; è "quel piedino tecnico" che chiude il cerchio aperto parlando di crittografia. Esempi: documento "valido fino al 1 ottobre 2025", carta di pagamento "valida fino a novembre 2026", cioè certificati scaduti dal primo giorno del mese successivo. Un certificato scaduto non è valido e non serve consultare né CRL né OCSP né trust list. (Teams 3 @ 1:08:24-1:10:02)

## 5. La revoca: trust list, CRL, OCSP

*DI-04 @ 00:25:18-00:37:32*

La VA consente anche di **ritirare un certificato prima della sua morte programmata**: carta d'identità smarrita, portafoglio rubato, attacco cyber con evidenza, anche ipotetica, che qualcuno abbia avuto accesso alla chiave privata. Chi ha la chiave privata di Alice "può fare tutto spacciandosi per Alice": è lo scenario più pericoloso (*DI-04 @ 00:25:18-00:26:21*). La VA raccoglie le segnalazioni dei titolari (smart card o telefono persi, token rubato, incidente cyber, anche password per sbloccare la chiave privata dimenticata: come aver perso PIN e PUK, la carta è "un mattone", tanto vale revocarla) e offre un servizio online per sapere se un certificato è ancora valido (*DI-04 @ 00:17:58-00:19:01*).

Il docente presenta **tre modi** (*DI-04 @ 00:26:21*).

**Slide "Trust list (TL) vs Certificate revocation list (CRL)"** (*DI-04 @ 00:30:20*). A sinistra: *Publishing Authority* → *Certificate Trust List* (elenco di CA) → *Smart Grid Device*, *User*, *Service*. A destra: *Root Certification Authority* con la sua *CRL*, *Subordinate CA* con la sua *CRL*, *End Entity*. Testo:

> A **trust list** (**TL**) works by *allowlisting* certificates. It is often used as the source of trust anchors: EU electronic trust services (**eIDAS**) are based on a TL.
>
> Certificates enlisted in a **certificate revocation list** (**CRL**) are *denylisted* (i.e. "revoked"), even if they would be technically valid otherwise.
>
> TLs and CRLs are static files, and may be further digitally signed by a higher-rank CA.

**1. Trust list (elenco di fiducia)** (*DI-04 @ 00:26:21-00:29:06*): una *allow list* (un tempo *white list*) di certificati, di solito radice ma non necessariamente, di cui ci si fida. Sono trust list l'elenco dei certificati installati nel sistema operativo e quello del browser, che servono a fidarsi dei siti web. È basata su trust list anche la fiducia nei prestatori di servizi fiduciari europei **eIDAS** (l'elenco di fiducia europeo). Ci si fida dei certificati in lista e di quelli emessi dalle CA in lista; per smettere di fidarsi di qualcuno lo si rimuove. È un modello **poco permissivo**: degno di fiducia è solo ciò che è esplicitamente elencato. Le trust list sono a loro volta firmate, per verificarne autenticità e integrità: "di chi mi fido allora?". Il docente cita l'aneddoto della signora anziana e Stephen Hawking (l'universo poggia su tartarughe una sopra l'altra): un problema di ricorsività, ma la trust list è il modo più autoritativo di dichiarare le proprie fonti di fiducia.

**2. CRL, Certificate Revocation List** (*DI-04 @ 00:29:06-00:32:52*): il modello duale, una *deny list* (un tempo *black list*): l'elenco dei certificati revocati. Quando si denuncia lo smarrimento di una carta (alla banca) o di un documento (in questura), la VA dovrebbe iscrivere nell'elenco il **numero di serie** del certificato. La CRL è un file pubblico che contiene solo numeri seriali (nessun dato personale) e data e ora della revoca. In convalida, oltre a firme e date, si consulta l'indirizzo delle CRL: se il certificato è in CRL, anche se tecnicamente valido e non scaduto, la convalida è negativa.

**L'importanza dell'orario di revoca** (*DI-04 @ 00:31:14-00:32:52*): un contratto firmato in tre il mese scorso non perde validità se oggi il certificato di firma di uno dei firmatari scade o viene revocato (smart card rubata): conta che al momento della firma il certificato fosse valido. Ogni firma apposta **dopo** l'istante della revoca è invece invalida.

**3. OCSP, Online Certificate Status Protocol** (*DI-04 @ 00:32:52-00:37:32*): le CRL sono file statici che vengono riscritti a ogni revoca; si scaricano e si cerca il seriale. L'OCSP è invece un **servizio web dinamico** a cui si fanno domande; secondo il docente viene consultato ogni volta che si convalida una firma, senza che l'utente se ne accorga.

**Slide "Online certificate status protocol (OCSP) vs CRL"** (*DI-04 @ 00:33:02*). A sinistra lo schema: "Step 1. The server sends its SSL/TSL certificate to the client." (il server è etichettato *Web Client*); "Step 2. The client sends an OCSP request to the OCSP responder to check the status of the certificate." (verso *CA or CRL Issuer* e *Certificate Revocation Server*); "Step 3. Using the certificate's serial number, the OCSP responder checks the status and sends a response back to the client, good, revoked, or unknown." A destra la stessa gerarchia con CRL della slide precedente. Testo:

> The **online certificate status protocol** (**OCSP**) is an API-like service that, one queried, provides accurate data about the status of queried certificate(s), which may be either valid, expired, suspended or revoked.
>
> A **CRL** (like a TL) is a static file: only the date of revocation, the serial number and, *optionally*, the revocation reason are provided for each certificate.

(Refusi della slide: "one queried" per *once queried*, "SSL/TSL", e il server chiamato "Web Client"; nello Step 3 il trattino lungo è reso con una virgola.)

Ogni certificato della catena può avere CRL e OCSP diversi, perché le CA verde, arancione e celeste possono essere organizzazioni diverse: per convalidare la firma di Alice controllo il suo certificato sulla CRL della CA azzurra, il certificato della CA azzurra sull'OCSP dell'arancione, quello dell'arancione sulla CRL della verde. Anche la radice ha scadenza e CRL, ma sono autogenerate: se non mi fido della radice, non mi fido neanche di quelle (*DI-04 @ 00:33:54-00:34:58*).

Che cosa dà in più l'OCSP (*DI-04 @ 00:34:58-00:37:32*):
- può verificare gruppi di certificati insieme;
- prevede nativamente lo stato **sospeso**. In una CRL ci sono solo certificati revocati permanentemente; secondo il docente X.509 vieta di rimuoverli, la CRL è "solo per aggiunzione", anche se molte CA lo fanno per simulare uno stato temporaneo;
- caso d'uso: la carta di pagamento che si può disattivare temporaneamente dall'app. Durante la sospensione le transazioni sono rifiutate con motivo "sospeso", non "revocato"; riattivandola il certificato torna valido, se nel frattempo non è scaduto. Con una denuncia di smarrimento invece non si torna indietro ("la potete tagliare con le forbici"), ma questo dipende dalla normativa dei sistemi di pagamento. Tecnicamente la riattivazione è sempre possibile solo entro la durata programmata.

> **Correzione:** la CRL non è "solo per aggiunzione" in senso assoluto: RFC 5280 (profilo X.509 di Internet) prevede fra i motivi di revoca `certificateHold`, cioè la **sospensione**, che è reversibile; il certificato sospeso può uscire dalla CRL (con il motivo `removeFromCRL` nelle *delta CRL*). Sono irreversibili le revoche con gli altri motivi.
>
> **Nota aggiunta:** in OCSP (RFC 6960) le risposte standard sono tre, *good*, *revoked*, *unknown*, come nello Step 3 della slide; "sospeso" è una risposta *revoked* con motivo `certificateHold`, e "scaduto" non è uno stato OCSP ma si ricava dalle date del certificato. Inoltre non è vero che l'OCSP sia consultato sempre: molti browser non lo interrogano in linea (Chrome usa liste di revoca proprie) e Let's Encrypt ha tolto gli URL OCSP dai certificati il 7 maggio 2025 e spento i responder il 6 agosto 2025 (verificato sul sito di Let's Encrypt). Infine l'esempio delle carte di pagamento è un'analogia: nei circuiti EMV il blocco di una carta avviene nei sistemi autorizzativi dell'emittente, non con una CRL o un OCSP X.509 per singola carta (dato esterno).

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 5 (revoca: trust list, CRL, OCSP)*

- **Perché serve la revoca.** Il certificato è un file pubblico: se il titolare, un anno dopo l'emissione di un certificato quinquennale, subisce un attacco e non può escludere l'esfiltrazione della chiave privata, la CA non può farsi restituire tutte le copie; l'unico rimedio è un **registro consultabile online**. La fiducia si sposta così dal singolo soggetto all'intera infrastruttura a chiave pubblica. (Teams 3 @ 0:58:48-1:00:13)
- **Trust list.** La fiducia "assiomatica" in una radice non sta tanto nell'essere autofirmata ("come l'Alice che non conosci che ti dice fidati, l'ho firmato io") ma nell'essere iscritta in una trust list firmata da qualcuno di cui ci si fida. La **trust list europea** eIDAS è "l'esempio più fulgido", il più globale che il docente conosca. (Teams 3 @ 1:00:13-1:02:13)
- **CRL.** Anche le CRL possono essere gerarchiche e sono sigillate elettronicamente dalla CA che fa da VA, con un proprio certificato dedicato: prima di usarla si verifica che la CRL sia autentica e integra. (Teams 3 @ 1:02:18-1:04:26)
- **X.509 e la revoca.** Secondo il docente X.509 è uno standard della fine degli anni '80, nato proprio per risolvere la revoca: "il nome dello standard X.509 in realtà è proprio il nome della Certificate Revocation List", e per descrivere la revoca si è descritto tutto il resto. È considerato vetusto ma è il formato più pervasivo. (Teams 3 @ 1:04:30-1:05:51)

> **Correzione:** X.509 è una raccomandazione ITU-T del 1988 della serie X.500 sulle directory (*authentication framework*): definisce sia il formato dei certificati a chiave pubblica sia quello delle CRL. "X.509" è il numero della raccomandazione, non il nome della CRL, e lo standard non è nato per la sola revoca.

- **Limite delle CRL.** Crescono molto (anche decine di MB) con l'aumento delle emissioni e delle revoche, anche cautelative, legate agli incidenti cyber. Esempio: un fitbit che, per caricare i dati della corsa, dovesse scaricare tre CRL da 2 MB per ciascuno di tre certificati consumerebbe la batteria per quello. Da qui l'OCSP. (Teams 3 @ 1:05:51-1:07:18)
- **OCSP.** Servizio applicativo, "un'API si direbbe oggi", che risponde per una data specifica con un messaggio sigillato dal responder: valido, scaduto, revocato o sospeso. Secondo il docente lo standard prevede la revoca come stato definitivo ("un ordine del giudice magari sì") e la sospensione come temporanea. (Teams 3 @ 1:07:18-1:11:02)
- **Esempio nuovo: il conto bloccato nel fine settimana.** Le banche che permettono di "bloccare e sbloccare il conto con un clic" sospendono i certificati del correntista (carte, operazioni dispositive). L'OCSP **memorizza** gli intervalli di sospensione: se fra quattro mesi arriva un addebito di 12.500 euro fatto di domenica, quando il conto aziendale era bloccato, si può dimostrare che in quell'intervallo il certificato era sospeso e che ogni firma apposta allora, anche con una catena passante per quel certificato, è invalida. È la verifica "a una data del passato" della slide sulla VA. (Teams 3 @ 1:11:02-1:14:09)
- **Pratica attuale.** I sistemi professionali usano soprattutto l'OCSP e, come *fallback* se il servizio non è disponibile, fanno scaricare la CRL, che però è statica, riguarda tanti certificati e non contiene le sospensioni. (Teams 3 @ 1:14:14-1:14:46)

## 6. Il secondo problema: la segretezza delle chiavi segrete e il loro ciclo di vita

*DI-04 @ 00:37:32-00:40:50*

**Slide di sezione "Secrets' Management"** (*DI-04 @ 00:35:04*, poi *00:37:44*).

**Slide "Two yet unravelled practical issues"** (*DI-04 @ 00:37:54*):
1. "Can we really **trust** the authenticity of **public keys**? Rephrasing: *Is Alice's public key really Alice's?*" (in grigio: già risolto);
2. "How can we really enforce the **secrecy** of **secret keys**? Rephrasing: *Was Alice's secret key really born secret? Can I trust it stays secret?*", con il fumetto "symmetric as well as private keys".

Il primo problema (la chiave pubblica di Alice è davvero sua, non sostituita da Carl in un registro) è stato risolto tecnicamente con PKI, scadenza e revoca. Il secondo: "professore, lei ci ha detto per tutto il corso che la crittografia funziona finché funziona la segretezza delle chiavi segrete", cioè simmetriche e private, "ma in pratica come si ottiene?". La crittografia teorica dice poco; non c'è una ricetta unica (*DI-04 @ 00:37:32-00:38:39*).

La prima tattica è istituire un **ciclo di vita delle chiavi**. Il certificato gestisce il ciclo di vita della chiave **pubblica** (nascita, scadenza, revoca, sospensione); ma il ciclo davvero sensibile è quello della chiave **segreta**: come generarla, registrarla, trasportarla ai legittimi titolari, controllare che la usino solo loro, distruggerla in modo sufficiente quando non serve più, gestirne le "seconde copie della chiave di casa". Una buona gestione delle chiavi segrete è ciò che rende uno schema robusto non solo in teoria ma in pratica (*DI-04 @ 00:38:39-00:40:34*).

**Slide "Key Management Lifecycle"** (*DI-04 @ 00:39:52*). Ciclo: *Key Generation* → *Key Registration* → *Key Storage* → *Key Distribution & Installation* → *Key Usage* → *Key Rotation* → *Key Backup & Recovery* → *Key Revocation & Suspension* → *Key Destruction* → di nuovo *Key Generation*.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 6 (gestione dei segreti e ciclo di vita)*

- La **quantum key distribution**, già vista in una lezione precedente, è un modo moderno di gestire i segreti, ma richiede canali quantistici costosi da realizzare e mantenere. La gestione dei segreti è un problema antico quanto la crittografia, "dagli albori dei tempi". (Teams 3 @ 1:14:51-1:15:46)
- Il **key management** richiede strette misure di sicurezza fisica, tecnica e logica (rimando alla guida [Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/README.md)), a carico del titolare e spesso del prestatore di servizi fiduciari, lungo **tutto** il ciclo di vita: ogni utilizzo, e soprattutto ogni momento di non utilizzo, è una superficie d'attacco. (Teams 3 @ 1:16:24-1:17:32)
- **La distruzione.** Il modo migliore per impedire l'uso di una chiave privata che nessuno deve più usare è distruggerla. Da qui l'indicazione di **tagliare con le forbici** la carta scaduta (si interrompono le piste del microcircuito), o di riconsegnarla all'emittente, perché un attore della minaccia potrebbe fare *dumpster diving* (vedi guida Cybersecurity, capitolo 06, sezione 12), recuperare le due metà e risaldarle; e la richiesta di consegnare il documento vecchio, o la denuncia di smarrimento, quando lo si rinnova. (Teams 3 @ 1:17:47-1:19:31)

## 7. Perfect forward secrecy

*DI-04 @ 00:40:50-00:43:40*

La prima tecnica, "una tattica" a livello alto, è la **perfect forward secrecy** (PFS), "segretezza in avanti perfetta". Il docente la presenta come il **key wrapping** del capitolo 01 "in un'altra salsa": si protegge una chiave simmetrica **effimera** trasferendola cifrata con chiavi pubbliche (*DI-04 @ 00:41:04*).

**Slide "Perfect Forward Secrecy (PFS)"** (*DI-04 @ 00:40:12*). Testo:

> **Perfect forward secrecy** (**PFS**) employs ephemeral\* symmetric keys $\kappa^{\text{sym}}_{\text{PFS},1}, \kappa^{\text{sym}}_{\text{PFS},2}, \kappa^{\text{sym}}_{\text{PFS},3}, \ldots$ for encrypting each communication, and requires peers to have a long-term asymmetric key pair $(\kappa^{\text{pub}}_{\text{PFS}}, \kappa^{\text{priv}}_{\text{PFS}})$ each, to preserve authentication and confidentiality of the former\* keys' exchange phase. Ephemeral keys are generated and immediately used only once, then they are securely deleted on both ends of he communication.
>
> PFS (e.g. Diffie-Helman algorithms) mitigates attack aiming at deriving, stealing, or at harvest-now-decrypt-later the private key(s). Even if a TA gets to the private key and a copy of the encrypted communications, he still can't decrypt the communications themselves as the ephemeral keys have been eventually destroyed.

Schema: *Application Clients / End Users* ($\kappa^{\text{pub}}_{\text{PFS}}$) ↔ *Encryption* ($\kappa^{\text{sym}}_{\text{PFS}}$) ↔ *Key Exchange Algorithm* ↔ *Decryption* ↔ *Web Servers* ($\kappa^{\text{priv}}_{\text{PFS}}$), con la *Ephemeral Key* sotto. (Refusi: "of he communication", "Diffie-Helman"; TA = *threat actor*.)

Il meccanismo a voce (*DI-04 @ 00:41:35-00:43:40*): Alice e Bob usano la simmetrica perché più rapida, ma non una sola: tante chiavi simmetriche, una per ogni nuova esigenza di comunicazione. **Ruotare** la chiave fa sì che, se Carl intercetta oggi e ottiene la chiave di oggi (anche con un attacco *harvest now, decrypt later*), al massimo decifra la comunicazione di oggi, non quella di domani. La chiave va poi **buttata**, non conservata insieme alla comunicazione; ogni nuova chiave viaggia cifrata con la chiave pubblica del destinatario. Per decifrare "per sempre" bisognerebbe risalire ogni volta a una chiave diversa. (A *00:42:07* il docente dice "se Bob dispone della chiave simmetrica": dal contesto intende Carl.)

> **Correzione:** il key wrapping con la chiave pubblica **a lungo termine** del destinatario **non** dà forward secrecy: chi registra il traffico e un giorno ottiene quella chiave privata può decifrare tutte le chiavi di sessione incapsulate, quindi tutte le sessioni passate (era il caso di TLS con scambio di chiave RSA, eliminato in TLS 1.3 proprio per questo). La forward secrecy richiede un **accordo di chiave effimero** (Diffie-Hellman o ECDH effimeri, DHE/ECDHE): le chiavi a lungo termine servono solo ad **autenticare** lo scambio (firma), non a cifrare le chiavi di sessione. È coerente con la seconda frase della slide ("Even if a TA gets to the private key…"), meno con la prima, che attribuisce alla coppia a lungo termine anche la riservatezza dello scambio.

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 7 (perfect forward secrecy)*

- Il docente la descrive di nuovo come "una key encapsulation" in cui la chiave simmetrica non viene mai memorizzata in chiaro ed è **effimera**, usata per un intervallo molto ristretto. Distingue la **cifratura in transito** (canali di comunicazione, dove si usa la PFS) dalla **cifratura a riposo** (le DCP del cinema, le firme digitali, quest'ultima per l'autenticità e non per la riservatezza). (Teams 4 @ 0:43:36-0:45:02)
- **Esempio nuovo: Teams.** Audio e video della lezione sono cifrati in tempo reale con chiavi simmetriche dal laptop del docente al cloud Microsoft e dal cloud ai dispositivi degli studenti, su due tratte distinte; la chiave viene ruotata periodicamente e la vecchia cancellata. Le **VPN** tengono la stessa chiave effimera per alcune ore e la rinegoziano poco prima che scada, concordando l'istante esatto del passaggio. (Teams 4 @ 0:45:10-0:47:45)
- **Motivazione.** Se la chiave cambia, per decifrare un'ora e mezza di lezione registrata l'attaccante dovrebbe forzare "diverse centinaia" di chiavi simmetriche: lo sforzo si moltiplica fino a rendere l'attacco non conveniente, che è lo scopo di uno schema robusto. (Teams 4 @ 0:47:45-0:49:38)

## 8. Diffie-Hellman con numeri piccoli

*DI-04 @ 00:43:40-00:51:11*

Un algoritmo usato per realizzare la PFS è **Diffie-Hellman** (DH), dai cognomi dei due matematici che lo inventarono, secondo il docente "negli anni Ottanta". Ne esistono varianti: secondo il docente una "basata su RSA" e una su curve ellittiche (*DI-04 @ 00:43:40-00:44:11*).

> **Correzione:** Diffie e Hellman pubblicarono lo scambio di chiavi nel **1976** ("New Directions in Cryptography"), prima di RSA (1977). Il DH "classico" non è basato su RSA ma sul **logaritmo discreto** nel gruppo moltiplicativo degli interi modulo un primo $p$; la variante ECDH sul logaritmo discreto su curva ellittica. Anche il titolo della slide scrive "Diffie-Hell**mann**": il cognome è Hellman.

**Slide "Diffie-Hellmann (DH) key exchange protocol"** (*DI-04 @ 00:43:52*). A sinistra, *"Classic" DH (based on RSA encryption)*, con Alice e SpongeBob (fonte: Practical Networking .net):
- *Agree upon two numbers*: P *Prime Number* 13, G *Generator of P* 6;
- *Randomly generate a Private Key*: Alice *Private = 5*, SpongeBob *Private = 4*;
- *Calculate Public Key* $(G^{\text{Private}}) \bmod P$: Alice $(6^5) \bmod 13 = (7776) \bmod 13$, *Public = 2*; SpongeBob $(6^4) \bmod 13 = (1296) \bmod 13$, *Public = 9*;
- *Exchange Public Keys*;
- *Calculate the Shared Secret* $(\text{Shared Public}^{\text{Private}}) \bmod P$: Alice $(9^5) \bmod 13 = (59049) \bmod 13$, *Shared Secret = 3*; SpongeBob $(2^4) \bmod 13 = (16) \bmod 13$, *Shared Secret = 3*.

A destra, *ECDH (based on ECC encryption)*: *Private key (a)* e *Private key (b)*, *G - Base point on curve*, *Public key: A = a × G*, *B = b × G*; *Shared secret: Share = a × B = a × b × G*, *Shared key: Share = b × A = b × a × G*; ciascun lato passa il segreto in una **HKDF** per ottenere la chiave. In basso: "DH is a **key-exchange** protocol allowing two parties to send partial secrets to each other across an untrusted communication channel, agreeing in the end on a symmetric key that is later used for securing communications across the same untrusted channel. In fact, DH also employs **PFS** and, therefore, **key-wrapping** techniques as well."

Il contesto a voce (*DI-04 @ 00:44:43-00:45:49*): Alice e Bob non si conoscono e si scambiano certificati; a volte si autenticano entrambi (**mutual authentication**), a volte, come quando un utente interroga un'autorità, solo il server (**server-side authentication**). Nello scambio concordano anche l'algoritmo più sicuro fra quelli in comune. Ma non hanno ancora una chiave in comune e il canale, Internet, per definizione non è fidato.

Il calcolo, come lo spiega il docente (*DI-04 @ 00:46:19-00:50:31*): $p = 13$ e $g = 6$ sono **pubblici**; i numeri segreti $a = 5$ (Alice) e $b = 4$ (Bob) non vengono mai scambiati.

$$A = g^a \bmod p = 6^5 \bmod 13 = 7776 \bmod 13 = 2, \qquad B = g^b \bmod p = 6^4 \bmod 13 = 1296 \bmod 13 = 9$$

Alice manda 2, Bob manda 9, in chiaro. Poi:

$$s_{\text{Bob}} = A^b \bmod p = 2^4 \bmod 13 = 16 \bmod 13 = 3, \qquad s_{\text{Alice}} = B^a \bmod p = 9^5 \bmod 13 = 59049 \bmod 13 = 3$$

"Guarda caso" lo stesso valore, per le proprietà dell'algebra modulare: $(g^a)^b = (g^b)^a = g^{ab} \pmod p$. In chiaro sono passati solo 13, 6 (la struttura algebrica comune, che per le curve ellittiche "è sempre la stessa praticamente") e le due chiavi pubbliche 2 e 9; né 5, né 4, né il segreto condiviso 3. Con numeri piccoli un computer inverte all'istante, con numeri enormi no.

**Verifica per esecuzione** (Python, `pow`): $6^5 = 7776 \equiv 2$, $6^4 = 1296 \equiv 9$, $9^5 = 59049 \equiv 3$, $2^4 = 16 \equiv 3 \pmod{13}$: tutti i valori della slide sono corretti. Inoltre 6 è davvero un **generatore** modulo 13 (ordine 12: le sue potenze danno tutti i residui 1-12), e la ricerca esaustiva del logaritmo discreto ritrova subito 5 da 2 e 4 da 9, come dice il docente per i numeri piccoli.

> **Correzione:** a *00:48:58* il docente dice "vi sfido a trovare che fosse 9": dal contesto intende la chiave privata di Bob, che è **4** (9 è la sua chiave pubblica). Subito dopo dice che l'inversione di questo problema "è alla base della crittografia RSA": il problema difficile del DH è il **logaritmo discreto** (e, più precisamente, il problema di Diffie-Hellman: da $g^a$ e $g^b$ ricavare $g^{ab}$), non la fattorizzazione su cui poggia RSA.
>
> **Nota aggiunta:** la frase finale della slide ("DH also employs PFS and, therefore, key-wrapping techniques") va letta al contrario: è il DH **effimero** a fornire la PFS, e non usa key wrapping (vedi la correzione della sezione 7). Nella pratica i valori segreti devono essere nuovi a ogni sessione e lo scambio va autenticato con le firme delle chiavi a lungo termine, altrimenti un uomo nel mezzo può fare due scambi DH separati con Alice e con Bob.

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 8 (Diffie-Hellman)*

- Stessa slide; "cambiano i dettagli algebrici ai quali non sono interessato per gli scopi di questo corso". La "magia" è che Alice e Bob **non si scambiano mai la chiave simmetrica**: se se la scambiassero, anche cifrata, un uomo nel mezzo potrebbe risalire al momento in cui viene comunicata. Come tutti i protocolli di scambio di chiavi, anche quelli post-quantum visti in una lezione precedente, il DH si scambia informazioni "molto parziali" dalle quali solo chi possiede l'altra metà del segreto ricava la chiave. (Teams 4 @ 0:49:38-0:52:54)
- Nel 2026 l'esempio numerico **non viene fatto** ("anzi, direi che l'esempio non lo facciamo") e si passa subito a TLS. (Teams 4 @ 0:52:57-0:53:15)
- A *0:52:39* il docente dice che Alice e Bob "usano le chiavi private l'uno dell'altra": è un lapsus, ciascuno usa la propria chiave privata e la chiave pubblica dell'altro.

## 9. TLS, HTTP e HTTPS, certificati di autenticazione di sito web

*DI-04 @ 00:51:11-00:54:26*

Il protocollo di comunicazione sicura dei siti web, oggi chiamato **TLS** (*Transport Layer Security*), realizza la PFS con uno scambio di chiavi Diffie-Hellman fra il client (il browser: Edge, Firefox, Chrome, Opera, Safari) e il sito (*DI-04 @ 00:51:11*).

- **HTTP** (*DI-04 @ 00:52:16*): la comunicazione non è cifrata. Chi "sniffa" la rete legge in chiaro username e password, al massimo codificati, e anche le risposte, per esempio l'elenco dei bonifici di una banca. Le reti Wi-Fi poco protette sono nella guida Cybersecurity, capitolo 04, sezione 6. Per questo oggi anche i siti pubblici, per l'integrità, usano HTTPS.
- **HTTPS** (*DI-04 @ 00:53:22*): prima di scaricare un solo carattere avviene l'**handshake TLS** e si stabilisce una chiave simmetrica unica per quella sessione. Un'altra scheda sullo stesso sito apre una nuova sessione con una nuova chiave; le due comunicazioni "non si vedono" a vicenda.

**Slide "Client-server authentication: TLS and WACs"** (*DI-04 @ 00:51:15*; nel titolo il trattino lungo è reso con due punti). A sinistra:

> (EC)DH is e.g. used at the start of communications btw web clients (browsers) and servers: i.e. the **https://** URLs. The web-client trusts a "**website auth. certificate**" (**WAC**, according to **eIDAS Regulation**) associated to the public key of the web server, registered by an allegedly legitimate owner at a generically *trusted* eTSP.

Sotto, cinque barre degli indirizzi (Internet Explorer, Firefox, Chrome, Opera, Safari) sul sito `https://www.certs4less.com/` con l'indicazione "4 Less Communications, Inc. [US]". A destra lo schema *HTTP vs HTTPS*: *Normal HTTP (80)*, *Insecure Connection*; *Secure HTTPS (443)*, *Encrypted Connection*, *SSL Certificate*. Testo:

> The **Internet**'s root of trust (its trust anchors) is effective by means of many **certificate stores**, not all containing the same WACs, like those provided by: OSs (Microsoft, Apple, Google/Android); web browsers (*above* + Mozilla); CA/Browser Forum (*above* + other CAs); organizationally trusted CAs; Individual application-trusted CAs; user-provided & other custom certificates.

(Nell'originale l'inciso "not all containing the same WACs" è fra trattini lunghi, resi con una virgola.)

> **Nota aggiunta:** in TLS 1.3 (RFC 8446) lo scambio di chiavi è sempre (EC)DH effimero, quindi la forward secrecy è garantita; in TLS 1.2 dipendeva dalla suite scelta (con lo scambio RSA non c'era). Nel commento il docente usa "Diffie-Hellman" in senso generico per "accordo di chiave".

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 9 (TLS e certificati di sito web)*

- **SSL e TLS.** Il docente racconta che un tempo si parlava di crittografia SSL; SSL, "un'implementazione matematica di Diffie-Hellman", è stato trovato pieno di vulnerabilità e sostituito da TLS. Per questo i certificati di sito web sono noti come "certificati TLS", a volte ancora "SSL", in Europa **certificati di autenticazione di sito web** (WAC). (Teams 4 @ 0:53:18-0:54:07)

> **Correzione:** SSL e TLS sono **protocolli**, non implementazioni di Diffie-Hellman: TLS è l'evoluzione standardizzata da IETF di SSL 3.0, e lo scambio di chiavi (RSA, DH, ECDH) è solo una delle loro componenti.

- **Che cosa controlla il browser.** Scarica il WAC, lo convalida come ogni certificato X.509 fino a un *trust anchor*, e in più controlla che il sito da cui l'ha preso sia quello scritto nel certificato. Esempio: un certificato tecnicamente valido per `www.google.com`, intestato ad Alphabet "con la partita IVA, l'indirizzo, l'email, con tutti i fiocchetti", servito però da `www.g00gle.com` (con gli zeri): il browser blocca subito la connessione. Se il dominio coincide, la chiave pubblica serve a negoziare con TLS (Diffie-Hellman, PFS) il canale cifrato con chiavi simmetriche che ruotano. (Teams 4 @ 0:54:07-0:58:53)
- **Autenticazione mono e bidirezionale.** Il browser resta anonimo; alcuni siti governativi o militari richiedono l'autenticazione bidirezionale. (Teams 4 @ 0:55:53-0:56:40)
- **Nuovo: il costo computazionale e i DoS.** Con 140 utenti connessi il server cifra 140 canali con 140 chiavi diverse: per questo, "senza scomodare i DDoS volumetrici" (vedi guida Cybersecurity, capitolo 03, sezione 14), si può saturare la capacità crittografica di un server con migliaia di connessioni, e i siti ad alto traffico usano il *load balancing*. (Teams 4 @ 0:58:57-1:00:38)

> **Nota aggiunta:** nel DoS sui server TLS la parte costosa è soprattutto l'**handshake** (operazioni asimmetriche: firma del server, accordo di chiave), non la cifratura simmetrica dei dati, che le CPU moderne accelerano in hardware (AES-NI).

## 10. Laboratorio: i certificati di Repubblica (La Stampa), New York Times, Apple, Google

*DI-04 @ 00:54:26-01:13:13*

Il docente condivide il browser (Chrome). Parte da CyberChef (`https://gchq.github.io`), poi passa a un quotidiano. Il browser mostra il prefisso `https://` solo cliccando, perché tende a nascondere i dettagli tecnici; sui siti HTTP Chrome avvisa "il sito non è sicuro", a volte blocca o chiede conferme ripetute ("giurate col sangue per tre volte") (*DI-04 @ 00:54:59-00:55:59*). Ma HTTPS non basta: anche Carl può firmarsi da solo un certificato malevolo e spacciarsi per `google.com` in una campagna di phishing (vedi guida Cybersecurity, capitolo 04, sezioni 8-9).

**`www.repubblica.it`** (*DI-04 @ 00:56:32-01:10:37*). Frame *00:56:44*: la pagina con il banner cookie di iubenda; frame *00:59:03*: il **Visualizzatore certificati: www.lastampa.it**, scheda *Generali*:
- *Rilasciato a*: Nome comune (CN) `www.lastampa.it`; Organizzazione (O) e Unità organizzativa (OU) "<Non parte del certificato>";
- *Emesso da*: CN `Amazon RSA 2048 M02`, O `Amazon`;
- *Periodo di validità*: emesso domenica 8 dicembre 2024 alle 01:00:00, scade mercoledì 7 gennaio 2026 alle 00:59:59;
- *Impronte SHA-256*: certificato `bfe0c6b1fb4e242b0aee0963c19224e25a05702ede2a21c1873a21ce32719d34`, chiave pubblica `6177cc11843d621997627bb0f3d323a6b45f3316d4c500f33f0db1089fe20857`.

Il commento:
- "Connessione sicura" vuol dire che la convalida dei certificati è andata a buon fine e che il dominio appartiene al soggetto indicato (*DI-04 @ 00:58:13*).
- **Subject DN** ("rilasciato a", il titolare della chiave), **Issuer DN** ("emesso da"), **periodo di validità** (*DI-04 @ 00:59:53*). L'emittente è una CA tecnica di Amazon con chiave RSA; il docente legge "M02" come "la seconda CA automatica".
- **Validità**: dall'8/12/2024 alle 01:00, cioè la mezzanotte di Greenwich, al 7/1/2026 alle 00:59:59. Il docente dice prima "due anni", poi si corregge: "un anno e un mese". **Verifica per esecuzione**: 395 giorni (meno un secondo).
- **Gerarchia** (scheda *Dettagli*, frame *01:01:03*): `Amazon Root CA 1` → `Amazon RSA 2048 M02` → `www.lastampa.it`. Campi: *Versione, Numero di serie, Algoritmo di firma certificato, Autorità emittente, Validità (Non prima, Non dopo), Oggetto, Info sulla chiave pubblica del soggetto*. L'intermedio (frame *01:02:03*: *Oggetto* `CN = Amazon RSA 2048 M02, O = Amazon, C = US`) ha un **numero di serie**, "quello che userei per cercarlo in una CRL", ed è valido, a voce, dal 24 agosto 2022 al 24 agosto 2030: un livello superiore ha una validità più ampia (*DI-04 @ 01:01:30*). Radice e intermedio appartengono alla stessa CA amministrativa (Amazon) ma sono due CA tecniche diverse.
- **Trust store**: il certificato radice di Amazon è nella trust list del browser o del sistema operativo, nel **certificate store**; senza, non ci si potrebbe fidare della radice. Fidarsi di Amazon significa fidarsi che verifichi chi possiede il dominio (*DI-04 @ 01:02:05-01:03:08*).
- **URL di OCSP e CRL** nel certificato (*DI-04 @ 01:08:56*).

**La domanda che il docente si aspettava** (*DI-04 @ 01:04:40-01:10:37*): "sono andato su repubblica.it e qui c'è scritto `www.lastampa.it`, non è venuto a nessuno questo dubbio?". Il docente nota che Repubblica è "del gruppo La Stampa" ("non lo sapevo, l'ho scoperto adesso"), ma "un conto è la società, un conto è il certificato". Se usassi un certificato intestato a La Stampa su un sito *typosquatting* (a voce "republic.co4" o "republic4.it" [?]), la convalida fallirebbe: il nome nel certificato non corrisponde al dominio, il browser (Chrome, Firefox, Safari) avvisa che il sito potrebbe essere contraffatto. È ciò che succede anche con certificati scaduti o revocati, ed è la difesa contro il ladro che ruba certificato e chiave privata di un sito e li riusa su un sito pirata per il phishing ("il tuo abbonamento a Repubblica è scaduto, cambia subito la password"). Perché allora è valido? Per risparmiare, chi compra un certificato per `www.lastampa.it` può chiedere che valga anche per altri servizi: è il campo **Nome alternativo del soggetto del certificato** (*Subject Alternative Name*). Frame *01:10:08*: *Valore campo* "Nome DNS: lab.lastampa.it; Nome DNS: www4.repubblica.it; Nome DNS: milano.repubblica.it; Nome DNS: lab.repubblica.it; Nome DNS: torino.repubblica.it" (l'elenco prosegue; a voce anche `roma.repubblica.it` e `www.repubblica.it`). Un solo certificato e una sola chiave privata per tutti i siti ospitati sullo stesso servizio.

> **Nota aggiunta:** la Repubblica e La Stampa sono entrambe testate del gruppo editoriale GEDI (dato esterno, al 2025): non è Repubblica a essere "del gruppo La Stampa". Il punto tecnico non cambia. Il browser oggi confronta il dominio con le voci SAN; il CN è di fatto ignorato.

**Altri siti** (*DI-04 @ 01:10:37-01:13:13*; nei frame conservati compaiono solo le home page con i banner cookie, non i visualizzatori dei certificati, per cui i nomi sono a voce):
- `nytimes.com`: certificato "THOT" [?] della **DigiCert**, un'altra CA, assegnato al dominio giusto; catena foglia, intermedio, radice; nel browser c'è solo la radice DigiCert, non il certificato del New York Times, che "dopo qualche anno tipicamente uno cambia";
- `apple.com`: anche lei DigiCert;
- `google.com`: emesso da **GTS** (Google Trust Services): "Google li compra a se stesso, è talmente grande che fa da solo".

Le CA radice del web sono "poche decine in tutto il mondo": aziende presenti dall'inizio di Internet, alcune nate dopo, altre decadute per problemi di sicurezza (capitolo 03); a parte Amazon, Google, Microsoft, nomi poco noti, ma multinazionali potentissime in un business "altamente lucrativo ma per pochi". Compromettere una di esse compromette tutto il digital trust che ne deriva. Tre eventi sarebbero un disastro reputazionale: compromissione di una chiave privata di CA, emissione a un soggetto non identificato, emissione di certificati per cui la CA non è abilitata (come se Microsoft emettesse il certificato di un passaporto canadese: nessun governo, che il docente sappia, ha autorizzato Google o Microsoft a farlo) (*DI-04 @ 01:12:42-01:15:18*).

**Slide "Certification authorities"** (DI-03, rivista a *00:19:13*): "There is, in general, an ecosystem of eTSPs / administrative CAs out there. The business is the **digital trust** itself, and those who framed first are today very profitable, yet not much known, companies."

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 10 (laboratorio sui certificati)*

- Stesso esperimento su `www.repubblica.it` (il docente aveva prima provato un sito di fake news con un carattere cambiato, bloccato dal browser). "Connessione sicura" garantisce due cose: il WAC è un X.509 tecnicamente valido e il dominio visitato è nel certificato. (Teams 4 @ 1:00:57-1:04:07)
- **Certificato 2026**: ancora `www.lastampa.it`, emesso dalla CA tecnica di Amazon "RSA 2048 M04" [?] (a voce "la quarta certification authority di Amazon"; nel 2025 era M02), valido dall'8 novembre 2025 alle 01:00 al 7 dicembre 2026 alle 00:59:59: "per chi vedrà il video negli anni successivi, potete fidarvi che oggi siamo fra queste date, altrimenti la connessione non avrebbe avuto luogo". **Verifica per esecuzione**: 394 giorni. Il docente precisa che il nome "M04" non è uno standard ma la nomenclatura di Amazon. (Teams 4 @ 1:05:34-1:06:29)
- **Dettagli nuovi**: chiave pubblica in formato PKCS #1 con RSA, mostrata in esadecimale, "la chiave verde del sito lastampa.it"; SAN acquistati in *bundling*; i **Certificate Policies** come OID (*object identifier*) che rimandano alle condizioni d'uso e alle policy di sicurezza a cui il titolare si impegna verso la CA; l'**Authority Information Access** con l'URL dell'OCSP e l'URL da cui scaricare il certificato **intermedio** (file `.cer`), "come faccio a trovare il prossimo certificato della catena"; le **Basic Constraints** che dicono che non è un certificato di CA; firma RSA con SHA-256, "poche decine di byte" [?]. L'intermedio vale dal 24/08/2022 al 24/08/2030, "dura 8 anni" (verificato: 2922 giorni). La radice è **autofirmata**: emittente uguale al titolare `Amazon Root CA 1`. (Teams 4 @ 1:06:44-1:14:11)
- "O ci fidiamo assiomaticamente di Amazon Root CA 1, oppure non ci rimane altro che interrompere la connessione." Chi decide? La sezione 11. (Teams 4 @ 1:14:14-1:14:48)

> **Nota aggiunta:** una firma RSA-2048 è lunga 256 byte (512 cifre esadecimali), non "poche decine di byte".

## 11. Solo 2026: CA/Browser Forum, Web PKI e durata dei certificati TLS

*Contenuto senza corrispondente nel 2025. Teams 4 @ 1:14:48-1:31:11*

- **CA/Browser Forum.** Chi decide di quali radici fidarsi è il CA/Browser Forum, associazione internazionale ma con stakeholder principali americani: produttori di sistemi operativi (Microsoft, Apple, Alphabet per Android), alcune realtà Linux (Red Hat, Debian), Mozilla, e le CA, fra cui Amazon e Symantec. (Teams 4 @ 1:14:48-1:16:15)

> **Nota aggiunta:** il CA/Browser Forum è formato da CA (*certificate issuers*) e produttori di browser e software che consumano certificati (*certificate consumers*); i root store veri e propri sono però gestiti da ciascun produttore (Microsoft, Apple, Google, Mozilla) con i propri *root program*. Symantec non è più una CA: la sua attività di certificazione è stata ceduta a DigiCert nel 2017 e i browser hanno revocato la fiducia nelle sue radici nel 2018 (dati esterni).

- **Web PKI.** L'insieme delle PKI le cui radici stanno nei certificate store (CA/Browser Forum, sistemi operativi) è chiamato colloquialmente **Web PKI**, "l'Internet della fiducia". La lista è "*bolted*", saldata nel browser (Firefox) o in una cartella di sistema (Edge su Windows, Safari sui sistemi Apple, Android, Google TV) e vale anche per le app. Le PKI della Web PKI hanno di solito due livelli, alcune 4-6. (Teams 4 @ 1:16:21-1:19:40)
- **Una CA fatta in casa.** Nessuno vieta di creare una CA tecnica con OpenSSL sul laptop o con un piccolo HSM USB ("le famose YubiKey" [?]) e firmarsi un certificato: tecnicamente la connessione cifrata funzionerebbe, ma una radice "Walter Arrighetti" non è in nessun certificate store e la convalida fallisce. Per entrare nella Web PKI servono iscrizione, una tassa e un **audit** che dimostri misure di sicurezza tecniche, fisiche e amministrative pari a quelle di Google, Microsoft, Amazon (vedi guida Cybersecurity, capitolo 06, audit e certificazioni): ci riescono solo i grandi player e chi fa questo mestiere B2B. (Teams 4 @ 1:19:45-1:22:33)
- **Data governance.** Senza Web PKI "avremmo già buttato Internet", non la useremmo per la PA né per i pagamenti. Il rovescio: il consorzio è "di facciata internazionale, ma di fatto statunitense" (ci sono anche un paio di prestatori italiani). In caso di guerra commerciale i big player potrebbero togliere dalle liste dei certificati e i siti che vi si appoggiano verrebbero tagliati fuori da un giorno all'altro, senza appello: un potere indiretto superiore a quello negoziale di un piccolo Stato. Per questo, secondo il docente, la Commissione europea è intervenuta con il Digital Services Act e altre norme. Vedi guida Cybersecurity, capitolo 05, sezione 8 (data governance). (Teams 4 @ 1:22:33-1:24:44)
- **Durata dei certificati foglia.** Prima del 2012 era standard comprare certificati da 10 anni; oggi circa un anno, già meno. Secondo il docente Google, "uno dei principali responsabili della riduzione", ha annunciato l'obiettivo di certificati "mensili" entro il 2030: **47 giorni**, cioè un mese più un periodo di grazia di circa mezzo mese. Scopo: chi ruba la chiave privata di un certificato TLS non può usarla per più di un mese. È la risposta ad attacchi in cui chiavi rubate o certificati falsificati venivano usati per anni, per esempio con i certificati di firma del codice. (Teams 4 @ 1:24:44-1:27:58)

> **Correzione:** la riduzione è stata decisa dal CA/Browser Forum con il ballot **SC-081**, proposto da **Apple** (gennaio 2025) e approvato l'11 aprile 2025 con il voto favorevole di tutti i browser (Apple, Google, Microsoft, Mozilla). Calendario della durata massima: **398 giorni** fino al 14 marzo 2026, **200 giorni** dal 15 marzo 2026, **100 giorni** dal 15 marzo 2027, **47 giorni** dal 15 marzo 2029 (verificato). Google aveva proposto in precedenza i 90 giorni. I certificati de La Stampa mostrati (395 e 394 giorni) rispettano il limite di 398 giorni allora vigente.
>
> **Nota aggiunta:** il limite di 10 anni "prima del 2012" va inteso come prassi di mercato: i Baseline Requirements del CA/Browser Forum (in vigore dal 2012) hanno poi fissato massimi via via più brevi: 39 mesi, 825 giorni (2018), 398 giorni (2020) (dato esterno).

- **Il caso del prestatore fallito.** Un prestatore di servizi fiduciari europeo che offriva "notariato digitale" ebbe alcuni anni fa un incidente di sicurezza enorme e fallì nel giro di pochi mesi: un'azienda che vende digital trust "può permettersi qualunque causa legale, salvo la palese disapplicazione delle regole di sicurezza". (Teams 4 @ 1:27:58-1:28:46)

> **Nota aggiunta:** il docente non fa nomi. Il caso più noto che corrisponde è **DigiNotar** (Paesi Bassi), compromessa nel 2011 con l'emissione di certificati fraudolenti, fra cui uno per `*.google.com`, e dichiarata fallita nel settembre 2011; offriva anche servizi notarili digitali (dato esterno, attribuzione non confermata dal docente).

- **Come Google impone le regole.** Controlla l'ultimo miglio: Chrome è il browser più usato, predefinito su Android e Google TV, e il motore di Edge è basato su Chrome; secondo il docente anche Safari. Basta un controllo "saldato" nel codice di Chrome che rifiuti certificati con validità troppo lunga, anche se tecnicamente validi; è l'analogo delle sanzioni negli organi paritari. Il docente dice di non usare Chrome personalmente. (Teams 4 @ 1:28:46-1:31:11)

> **Correzione:** Safari non è basato su Chrome: usa **WebKit** (Apple). Chrome e Edge usano **Blink**, motore di Chromium nato nel 2013 come fork di WebKit.

- Chiusura: la lezione "conclude la parte dedicata al digital trust"; dalla successiva si passa ai servizi fiduciari elettronici (capitolo 05). (Teams 4 @ 1:31:11-1:31:35)

## 12. Hardware Security Module (HSM)

*DI-04 @ 01:15:18-01:19:00*

Le CA di questo calibro hanno CA tecniche sparse nel mondo e a volte "miliardi di chiavi segrete", gestite in dispositivi sicuri anche dal punto di vista hardware: gli **Hardware Security Module** (HSM), che gestiscono in sicurezza il ciclo di vita delle chiavi (*DI-04 @ 01:15:18*).

**Slide "Hardware Security Modules (HSM)"** (*DI-04 @ 00:54:30*, rimostrata a *01:14:07* e *01:16:07*). Testo:

> **HSM** has restricted-access segregated subsystem called **secure element/enclave** (**SE**), dedicated to: generation, storage and archival of secret keys; digital signing via stored private keys; encrypting/decrypting via stored symmetric keys.
>
> Secret keys cannot be exported from an HSM, with the optional exception of strictly controlled workflows, exclusively for key material backup purposes.
>
> Several HSM types exist, with prices ranging 100€'s – 100k€'s, hardware-/software-based, and several form factors like: rackable units/servers (like the one in the figure below); chips (in smartphones); PCI-Express cards; Smartcards (e.g. ID cards and payment cards); USB tokens.
>
> HSMs with certain security features may implement *secure* or ***qualified*** **e-signature/seal creation devices** (**SSCD**s or **QSCD**s) pursuant to **eIDAS Regulation**.

Immagine: un HSM rack 1U con uno scudo e una spunta.

A voce (*DI-04 @ 01:15:49-01:19:00*):
- le chiavi segrete sono **generate dentro** l'HSM e **restano** dentro; al massimo si estrae un certificato di chiave pubblica;
- oppure l'HSM esporta la chiave, ma solo dentro un **contenitore cifrato** con una chiave altrettanto sicura;
- oppure comunica con la macchina che produce le smart card e **scrive la chiave privata direttamente nel chip**;
- "ancora meglio": l'HSM non gestisce affatto le chiavi private dei titolari, solo le pubbliche (sezione 13);
- esistono implementazioni software, ma quelle professionali, da un centinaio a un centinaio di migliaia di euro, stanno nei data center e rendono la chiave non estraibile anche con forzatura fisica; alcune, se rilevano un'intrusione anche logica, **cancellano** il repository delle chiavi; quelle di livello militare **bruciano il chip** piuttosto che rivelarle;
- molti hanno un **orologio sicuro** (*anti-tamper clock*): i certificati contengono orari che devono essere fidati. Se si potesse posticipare l'orologio di un HSM, si emetterebbero certificati "postdatati" di decenni, utilizzabili quando gli algoritmi saranno stati violati: "il rischio crittografico è alle porte". Questi aspetti sono oggetto delle certificazioni di sicurezza richieste anche dalla normativa, per esempio europea.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 12 (HSM)*

- **SSCD.** Le chiavi private sono protette da dispositivi chiamati *secure signature creation device* (SSCD), in ambito europeo *secure e-signature or seal creation device* quando custodiscono le chiavi dei certificati di firma o sigillo; l'esempio pratico, l'hardware, è l'HSM. (Teams 3 @ 1:19:36-1:20:27)

> **Nota aggiunta:** "SSCD" è il termine della vecchia direttiva 1999/93/CE; il regolamento eIDAS (910/2014) parla di dispositivi per la creazione di una firma (o sigillo) elettronica qualificata, **QSCD**. La slide usa entrambi.

- **Cassaforte digitale.** HSM più software di autenticazione di fronte si chiamano in italiano **cassaforti digitali**. Presidiano la riservatezza ma anche integrità e **disponibilità**: una chiave chiusa dove nessuno può usarla non serve (l'esempio della cassaforte dalla prima lezione di Cybersecurity, vedi guida Cybersecurity, capitolo 01). (Teams 3 @ 1:20:27-1:22:06)
- **Come si usa.** Le chiavi non escono: per cifrare si forniscono i dati all'HSM dopo essersi autenticati e li si riceve cifrati. Una CA inserisce il **pre-certificato** (non firmato), sblocca la chiave privata di certificazione e riceve il certificato firmato. Un utente finale che ha affidato la propria chiave a un'azienda, per scelta o per obbligo di legge, si autentica al servizio di cassaforte, manda l'**impronta** del documento e riceve l'impronta cifrata, cioè la firma. Se l'amministratore di sistema, o l'amministratore delegato, entra come root e chiede di esportare tutte le chiavi, l'HSM "gli dice marameo", come a un hacker. (Teams 3 @ 1:22:12-1:25:20)
- **Protezioni fisiche.** Gli HSM da decine o centinaia di migliaia di euro, spesso prodotti da fornitori della difesa, distruggono le chiavi o vanno in *lockdown* (come un iPhone) se rilevano una compromissione; il chip è annegato in **resina epossidica**, così chi apre l'HSM per cinque minuti non può estrarlo senza romperlo, e l'apertura fa scattare l'allarme che invalida le chiavi. Esistono chiavette USB HSM da 20-30 euro, alcune certificate, ma non paragonabili. (Teams 3 @ 1:25:23-1:27:41)

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 12 (HSM)*

- Gli HSM ad alto profilo non danno le chiavi altrui **nemmeno a root**: si comportano diversamente da un sistema operativo, che a root concede ogni privilegio; un attaccante che scala fino a root può renderli indisponibili ma non deve poter leggere le chiavi. Gli HSM economici, fatti per un singolo utente, spesso consentono al titolare di esportarle. (Teams 4 @ 0:27:54-0:29:58)

## 13. Registrazione delle chiavi e Certificate Signing Request (CSR)

*DI-04 @ 01:19:00-01:22:24*

A volte la sicurezza della chiave privata è tale che **nemmeno l'HSM** la conosce. Se so generarmi da solo la coppia di chiavi e presentare una prova convincente della mia identità, invio una richiesta firmata, la **Certificate Signing Request** (CSR), alla CA amministrativa; se la mia identità è convalidata, la CA tecnica prende la chiave pubblica dalla CSR, la "avvolge" in un certificato e lo firma **dentro l'HSM** con la chiave privata di certificazione. L'unico compito dell'HSM è custodire la propria chiave di certificazione (*DI-04 @ 01:19:00-01:20:48*).

Perché: se dovessi mandare la mia chiave privata all'HSM, qualcuno potrebbe intercettarla (e torneremmo al problema di comunicare in sicurezza con l'HSM), e potrei sospettare che la CA la usi. "Se non mi fido non posso escludere che la usino." Comunico solo la chiave pubblica; spetta alla CA verificare che io sia io (*DI-04 @ 01:20:48-01:22:24*).

**Slide "Key Registration"** (*DI-04 @ 01:16:38*, poi *01:18:58*). Schema: l'*Applicant* (*Identifying Information*: x.509 extensions, distinguished name; *Public Key* $\kappa^{\text{pub}}$; *Private Key (Applicant)* $\kappa^{\text{priv}}$) → "1. Generate CSR" → *CA (HSM)*: "2. Validate Identity" → "3. Generate Signed Certificate and Send to Applicant" ($C^{\text{pub}}$, firmato con *Private Key (CA)* $\kappa^{\text{priv}}_{\text{CA}}$). Testo:

> In a **CSR** workflow the CA and its **HSM** only handle subject public-key/certificate pair $(\kappa^{\text{pub}}, C^{\text{pub}})$, *not* its $\kappa^{\text{priv}}$.
>
> Usually CAs, are forbidden to handle private keys they generate public-key certificates for, for privacy and confidentiality reasons. In general subjects do not want (or *must not*, for compliance reasons) the CA to be in any position to know the subjects' private key(s).
>
> According to **x.509**/RFC-5280 private keys are generated by subjects, who issue a **certificate signing request** (**CSR**) to a CA. It optionally: indicates the CA public key which the request to issue a certificate is sent for; is signed with the subject's private key; stores additional certificate metadata (e.g. DNs, x.509 extensions, …) which the subjects request may/must be present in the certificate (and which the CA may discretionally honour, ignore, or modify).
>
> If the CA accepts the CSR, it generates a digital certificate $C^{\text{pub}}$ and sends it to the subject.

> **Nota aggiunta:** il formato standard della CSR è **PKCS #10** (RFC 2986). La firma della CSR con la chiave privata del richiedente è la **prova di possesso** (*proof of possession*): dimostra alla CA che chi chiede il certificato per quella chiave pubblica possiede davvero la privata corrispondente.

### Integrazione Teams 2026 (lezione 3 2026)

*Sezione 13 (registrazione delle chiavi e CSR)*

- **Primo modello: l'HSM genera entrambe le chiavi.** In alcuni stabilimenti l'HSM esporta **una sola volta** la chiave privata alla macchina che la scrive nel chip della smart card (documento d'identità, carta di pagamento) e poi cancella la propria copia utilizzabile, tenendola al più come **backup** cifrato: l'unica eccezione ammessa da alcune norme. Per questo molti attacchi agli HSM passano dai **sistemi di backup**, ingannando l'HSM con una finta richiesta di esportazione per backup ("ve lo dico col cappello rosso del Red Team"). (Teams 3 @ 1:28:00-1:29:39)
- **Secondo modello: CSR.** La coppia di chiavi può essere generata dall'utente o da un terzo direttamente nel chip: smart card, chiavetta USB, chip del cellulare (la **Secure Enclave** di Apple), **TPM** nei laptop, che danno a ogni dispositivo una chiave privata che neanche il produttore conosce, poi certificata da un HSM terzo. La CSR "assomiglia molto a un certificato" (dati identificativi, chiave pubblica, firma con la chiave privata) "ma non è nel formato X.509". La RA identifica l'istante; se l'esito è positivo la CA appone con la chiave di certificazione (la viola) il sigillo elettronico sul certificato nuovo, generato nell'HSM, e lo restituisce; da quel momento l'istante lo dà ai suoi *relying parties*. La catena si ripete a livello organizzativo: la chiave di certificazione è a sua volta certificata da un'altra CA, con un altro HSM a monte. (Teams 3 @ 1:29:40-1:33:44)
- Chiusura di Teams 3: con questa parte "abbiamo recuperato parte della lezione di ieri"; nella successiva "altri meccanismi per proteggere le chiavi segrete". (Teams 3 @ 1:33:55-1:34:17)

## 14. Gestione delle chiavi nel cinema digitale: le Key Delivery Message

*DI-04 @ 01:22:24-01:32:53*

Esempio dal "vecchio settore merceologico" del docente, il cinema. In tutte le sale, salvo i festival di pellicola, c'è un **proiettore digitale** che manda in playback un file. Lo stesso principio vale per le piattaforme sui televisori (**DRM**), ma il docente non lo spiega: è più complesso e meno robusto, "la crittografia vale il valore economico del televisore", mentre il digital cinema, essendo B2B, usa crittografia "a livello militare" (*DI-04 @ 01:22:24-01:24:05*).

**Slide "Key Delivery Messages"** (*DI-04 @ 01:32:27*; durante la spiegazione a voce resta a schermo la slide della sezione 13, la KDM compare solo alla fine). A sinistra *Distribution (Mastering Lab)* ed *Exhibition (theatre projector)*: il film (Charlie Chaplin) cifrato con $\kappa^{\text{sym}}_{\text{Content}}$; *Content*: video track, audio tracks, subtitles, … metadata; "KDM is signed by the Mastering Lab for integrity & authentication"; "Symmetric Key Encrypted in KDM using Public Key"; al centro la *KDM* con $C^{\text{pub}}_{\text{MB}}$, $\kappa^{\text{pub}}_{\text{MB}}$ e $\kappa^{\text{sym}}_{\text{Content}}$; "Public Key from Media Block" ($\kappa^{\text{pub}}_{\text{MB}}$), *Key Pair*, $\kappa^{\text{priv}}_{\text{MB}}$; "Symmetric Key Decrypted from KDM by Private Key"; "Signed KDM is validated against a Mastering Lab accredited by DCI/SMPTE". A destra:

> **Digital Cinema** (**DC**) has been using a sustainable reliable **business model** since 2003, for countering **piracy** while daily distributing movies (~100–500GiB each), to theatres worldwide, across the internet.
> - A **content key** (AES) is associated to each movie, generated *only once* by the mastering software.
> - All DC projectors worldwide have an embedded HSM (**media block**), whose private keys (RSA) are associated with each projector's serial number.
> - Media blocks' public-key certificates are published online by the respective manufacturers.
> - Movie theatres purchase a license to show a movie, within a time window, for their projector.
> - Studios deliver to them a **Key Delivery Message** (**KDM**): a tiny file binding that content and time window with the media block's public key, which is e-sealed by the distributor's private key.
>
> To playback the movie, a DC projector validates the KDM's e-seal, the KDM's validity period vs the current time of day (in its media block's anti-tamper internal clock) and, if ok, retrieves the content key.

(Nell'originale "within a time window" è fra trattini lunghi, reso con virgole.)

Il flusso a voce (*DI-04 @ 01:24:05-01:32:03*):
1. il proiettore, o meglio il computer al suo interno, il **media block**, manda in play una versione **cifrata con chiave simmetrica** del film: 100-500 GB, compresso ad altissima qualità; cifrarlo richiede ore al computer di mastering, e lo si fa **una volta sola**. La chiave è la **chiave di contenuto**;
2. la chiave non può viaggiare in chiaro. Ogni media block ha un piccolo **HSM** con un **orologio anticontraffazione** di derivazione militare, che neanche il proiezionista può alterare, e una **chiave privata**;
3. il film arriva all'esercente via Internet, via satellite o "vecchia scuola" su hard disk in una valigetta Pelican che gira fra i cinema della zona (una per circuito); viene ingerito nello storage del proiettore. Tutte le copie al mondo sono lo stesso file cifrato con la stessa chiave;
4. l'esercente compra il diritto di proiettare, per esempio, per due settimane nelle sale 2, 6 e 8, e comunica al distributore i **numeri di serie** dei proiettori (più qualche sala di backup). I costruttori (pochi: Dolby, Barco, alcuni in Cina; il nome del primo è incerto) pubblicano registri con i **certificati a chiave pubblica** di tutti i media block, indicizzati per seriale;
5. l'esercente riceve una **KDM** (*Key Delivery Message*), un file **XML** firmato, che contiene la chiave di contenuto **cifrata tre volte**, con le chiavi pubbliche dei tre media block: "key wrapping". Nessuno conosce la chiave di contenuto tranne il laboratorio di mastering, che già detiene il film in chiaro (quindi è già esposto a quel rischio); la passa cifrata al distributore, che "senza mai sbustarla" la reimbusta per tutti i seriali degli esercenti;
6. nella KDM, "una specie di certificato", ci sono una data di inizio e una di fine. Se si prova a proiettare fuori dalla finestra pagata, l'orologio anti-tamper, che non si può retrodatare né postdatare, fa rifiutare il playback. Nella crittografia teorica nulla limita la validità temporale: è la stessa logica dei certificati X.509. Per un'altra settimana serve una nuova KDM.

È una variante del key wrapping, "niente di nuovo dal punto di vista tecnico"; a memoria del docente, che ha lasciato il settore da una decina d'anni, nessun attacco crittografico ha mai rotto questo modello. Le copie pirata uscivano da Blu-ray e DVD, o dalle sale "per altri motivi che però non vi spiego" (*DI-04 @ 01:32:03-01:32:53*).

> **Correzione:** a *01:24:36* il docente paragona il film ai "60 giga di un DVD": un DVD contiene 4,7 GB (singolo strato) o 8,5 GB (doppio strato). Il confronto regge comunque, un DCP è molto più grande.

Sul **firmatario della KDM** le fonti divergono: a voce "firmato dal sistema di gestione delle chiavi dell'esercente, un servizio fornito in cloud da qualcun altro" (*DI-04 @ 01:28:53*); nella slide, a sinistra, "signed by the Mastering Lab", a destra "e-sealed by the distributor's private key"; in Teams 4 "sigillo elettronico generato con la chiave privata di quel distributore, di quell'azienda di mastering". Vedi Punti incerti.

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 14 (key encapsulation e KDM)*

- **Ripasso della key encapsulation**, in apertura di Teams 4: la content key generata per quel contenuto (nel DRM, "una specie di chiave usa e getta"), cifratura simmetrica, anche con algoritmi post-quantum, cifratura della sola chiave con la pubblica del destinatario, busta crittografica; più destinatari = più copie della stessa chiave cifrate con pubbliche diverse, ciascuno sceglie la sua copia grazie ai metadati. Novità rispetto al capitolo 01: la busta non è sempre un unico file; nel cinema chiave cifrata e contenuto cifrato **viaggiano in file separati**. (Teams 4 @ 0:00:04-0:06:32)
- **Il contesto industriale.** A metà degli anni 2000 gli studios americani passano dalla pellicola 35 mm al **DCP** (*Digital Cinema Package*), cifrato o in chiaro; quello commerciale è cifrato. Due problemi: il **modello di licenza** a tempo (Spider-Man nella sala 1 per tre settimane: un file, anche cifrato, non deve poter essere proiettato all'infinito; con la pellicola il distributore la ritirava e alla fine la distruggeva) e la **pirateria digitale**. Oggi l'industria valuta il passaggio ad algoritmi *quantum safe*. (Teams 4 @ 0:06:57-0:10:16)
- **Dettagli nuovi**: per semplicità una sola chiave simmetrica per tutto il film, ma "in realtà il sistema è più complesso", con un **doppio imbustamento** intermedio fra mastering e sale, complessità che "ai fini didattici non serve"; il 2K pesa 100-500 GB, il 4K circa il doppio; i file sono **MXF** con essenze audio e video, anche i sottotitoli possono essere cifrati; la chiave di contenuto è **AES-128**, standard dell'industria, possibile anche AES-256; la chiave del media block è RSA "a 1024 o 2048 bit"; costruttori: Dolby, Barco, Fuji, Sony e aziende asiatiche, ciascuno con un database pubblico per seriale. Nella KDM ogni copia cifrata della chiave ha un intervallo con giorno, mese, anno, ora, minuto, secondo e fuso; la KDM è sigillata dal distributore o dall'azienda di mastering: chi sostituisse una copia della chiave o cambiasse gli orari invaliderebbe il sigillo. (Teams 4 @ 0:10:16-0:18:14)

> **Nota aggiunta:** secondo le specifiche DCI le chiavi dei media block sono RSA a **2048** bit (dato esterno da verificare sulle specifiche, non controllato in questa sede).

- **Logistica e playback.** Hard disk con connettore proprietario "preso in prestito dall'esercito americano" che il proiettore ingerisce automaticamente; oggi trasferimento via Internet; KDM piccolissime, via email o automatiche. Al playback servono tre condizioni: KDM riferita a quel DCP, una copia della chiave cifrata con la pubblica di quel proiettore, istante corrente dentro l'intervallo. Allora il media block, che è un HSM, "sbusta" la chiave, la tiene in memoria solo durante il playback e **decifra in tempo reale**: in nessun punto esiste una copia in chiaro del film. L'orologio ha una batteria indipendente; se si scarica serve il manutentore, così non si può "fare la macchina del tempo". (Teams 4 @ 0:18:14-0:24:43)
- **Altro**: self-provisioning con carta di credito e KDM consegnata direttamente al proiettore, anche da telefonino; il DCP può contenere metadati per luci, tenda, pubblicità, intervallo: sale gestibili senza personale, "come alcuni tipi di hotel". (Teams 4 @ 0:24:46-0:26:13)

## 15. Firme remote e firma con la CIE

*DI-04 @ 01:32:53-01:39:35*

Finora le chiavi private stavano in smart card o token del titolare. C'è un'altra modalità: la **firma remota**. La chiave privata è ospitata nell'HSM di un terzo, di cui ci si fida per forza; la CA che lo gestisce fornisce un'app per lo smartphone che verifica l'identità con un'**autenticazione forte** (argomento della lezione successiva, "stiamo arrivando finalmente all'argomento finale del corso"), calcola l'**impronta** del documento e la manda all'HSM. L'HSM riceve solo l'impronta, non il documento, e la firma con la chiave privata del titolare solo se ha una prova tecnica dell'autorizzazione (PIN, biometria): "l'HSM sa che deve usare la chiave privata di Walter Arrighetti". La firma torna allo smartphone e può valere, entro certi limiti giuridici, come firma elettronica. In alcuni modelli si invia l'intero documento e anche l'hash è calcolato da remoto (*DI-04 @ 01:32:53-01:35:51*).

**Slide "Remote e-signatures (and e-seals)"** (*DI-04 @ 01:33:57*). Testo:

> Remote digital signature means the document (or its digest) are sent to a remote HSM that (hashes it and) encrypts the digest via a private key, stored in the HSM but under the *sole control* of the e-signatory / e-seal creator (e.g. only the signatory only knows the passcode/PIN to unlock it). The **eIDAS2 Regulation** thus refers to remote HSMs as **remote e-signature/seal creation devices** (**RSCD**s), i.e. as a *remote* species of SSCDs.

Schema: *Application/Service Provider(s)*, *Registration Authority*, *Certificate Authority*, *Business Support Systems*, *MSSP Platform* (con riferimento *ETSI TS 102 204*), collegati via *HTTPS* e *APNS / Firebase* allo smartphone, e a un *SAM* / *Hardware Security Module*; in basso il flusso *Signatory* → *Document to be signed* → *Open a signing app* → *Authenticate to access a qualified certificate on a qualified signature creation device* → *Electronically signed document*; a sinistra un telefono con una firma tracciata col dito.

**I due modelli di fiducia opposti** (*DI-04 @ 01:35:51-01:37:28*): con la CSR non mi fido dell'HSM al punto da non dargli la chiave privata, gli chiedo solo di certificare la pubblica; con la firma remota mi fido tanto dell'HSM che preferisco non custodire io la chiave: potrei non saper proteggere la mia infrastruttura, mentre il processo remoto è più distante da un attore della minaccia o da un ladro.

**Slide "CIE-based Electronic Signature "Firmo con CIE""** (*DI-04 @ 01:37:35*). Immagini dell'app **CieSign**: "portata di smartphone", "REGISTRA LA TUA CARTA" con la CIE appoggiata al telefono; "STAI FIRMANDO IL DOCUMENTO… Trattieni la Carta di Identità Elettronica in prossimità dello smartphone per completare la firma."; una firma "Mario Ros[si]" tracciata col dito; l'esito su *Contratto_firmato.pdf*, "contiene 1 firma": MARIO ROSSI, codice fiscale, "DATA DI FIRMA Non disponibile", "La firma è valida", "Il certificato è valido", "Il certificato non è stato revocato", e l'emittente "C=IT, O=Ministero dell'Interno, OU=Direz. Centr. per i Servizi Demografici - CNSD, CN=Issuing sub CA for the Italian Electronic Identity Card - SUBCA1". In basso `https://www.cartaidentita.interno.gov.it`.

Il funzionamento (*DI-04 @ 01:37:28-01:40:06*): dopo una registrazione iniziale, l'app calcola l'hash del PDF e lo invia via **NFC** (pochi millimetri) insieme a un'onda di potenza sufficiente ad alimentare il chip; il chip della CIE cifra l'hash con la **chiave privata di firma** e restituisce via radio la firma, che l'app inserisce nel PDF. L'app permette anche di aggiungere una firma col dito come "timbro" grafico. Il docente prima dice che "non è un'applicazione di firma remota, è un'applicazione di firma locale", poi che lo è "nel senso che la smart card fa da HSM": l'HSM è la carta, "remoto ma a pochi millimetri". Nella CIE c'è anche il certificato usato dalle terze parti per convalidare la firma.

### Integrazione Teams 2026 (lezione 4 2026)

*Sezione 15 (firme remote, passaporto, CIE)*

- **Firma remota passo per passo**: l'HSM in cloud, *remote signature creation device*, non dà mai la chiave privata ad Alice; è Alice a dare all'app l'evidenza da firmare; l'app calcola l'impronta e la manda su canale sicuro con la prova dell'autenticazione (biometria, PIN, OTP); l'HSM cifra l'hash con la chiave di Alice; l'app imbusta la firma nel documento. La **busta** contiene di solito documento originale, firma e certificato o catena di certificati per la convalida da parte dei "Bob". (Teams 4 @ 0:26:17-0:32:25)
- **Documenti e carte come HSM.** Anche carte di pagamento, passaporti, permessi di soggiorno e CIE funzionano così: il chip fa da HSM e contiene spesso **più chiavi private**, una per autenticarsi e una per firmare. (Teams 4 @ 0:32:30-0:33:12)
- **Passaporto al gate (nuovo).** ICAO norma l'aspetto esterno (foto nello stesso posto, codice leggibile a macchina) e la sicurezza elettronica del chip, che contiene chiavi private e certificati **CVC**, "l'unica alternativa effettivamente usata al mondo" a X.509. Al gate si confrontano **tre fotografie**: quella ripresa dalla telecamera, quella stampata e quella a colori e a risoluzione maggiore nel chip, **sigillata elettronicamente**; per falsificare il documento bisognerebbe alterare sia la foto stampata sia quella sigillata. Il gate non chiede il PIN: legge la zona a lettura ottica della prima pagina (o del retro della CIE) con lo standard **PACE**, l'equivalente digitale di mostrare il passaporto aperto al doganiere; poi la chiave privata di identificazione firma un blob di dati mandato contactless, e la firma si convalida con la PKI dello Stato emittente: i gate hanno le PKI di tutti i paesi ICAO, e i dati del certificato devono coincidere con quelli stampati: "un controllo a doppio cieco". (Teams 4 @ 0:33:15-0:39:07)

> **Nota aggiunta:** nella specifica ICAO 9303 l'integrità dei dati del chip (foto compresa) è garantita dalla **Passive Authentication**, con la firma del *Document Signer* dello Stato verificata tramite i certificati X.509 della CSCA; la firma di una sfida con la chiave privata del chip è la **Active (o Chip) Authentication**, contro la clonazione. I certificati **CVC** servono soprattutto alla *Terminal Authentication* dell'EAC, cioè ad autorizzare il **lettore** ad accedere alle impronte digitali, e risiedono nei terminali; nel chip c'è la chiave pubblica della CVCA come ancora di fiducia (dato esterno).

- **CIE, due chiavi.** La CIE ha due chiavi private: una di **autenticazione**, che segue le norme ICAO ed è quella di "Entra con CIE" al **livello 3** (il sito manda un codice che passa via NFC alla carta, che lo firma dopo PIN o biometria; il service provider convalida la firma e legge dal certificato nome, cognome, data di nascita, codice fiscale); i livelli 1 e 2 non usano la carta, analoghi a SPID, basati su un'attivazione una tantum sullo smartphone. La seconda chiave è di **firma** e segue il **regolamento eIDAS**: le due porzioni del chip hanno requisiti di sicurezza simili ma PKI di natura completamente diversa. (Teams 4 @ 0:34:40-0:35:46, 0:39:15-0:41:00)
- **CieSign.** "Non è una firma remota, o meglio è una firma locale" che usa l'HSM della carta: la chiave non esce dalla CIE, la si tiene a pochi millimetri dal telefono; "remota tra virgolette", con la prossimità della CIE al posto della nuvola del cloud nello schema della firma remota. È spesso preferita perché né l'impronta né il documento lasciano il telefono. Firma col dito come forma "molto semplice, poco robusta" di **firma grafometrica**; gratuita con tutte le CIE, serve solo il PIN. Firme elettroniche nel capitolo 05. (Teams 4 @ 0:41:00-0:43:30)

## 16. Passaporti elettronici e standard PKCS

*DI-04 @ 01:39:58-01:42:05*

Le norme sui documenti d'identità e di viaggio elettronici prescrivono anche le caratteristiche di sicurezza dei chip: per i passaporti l'**ICAO**, uguale in tutto il mondo, perché ogni gate deve autenticare cittadini di qualunque paese aderente; per la CIE, secondo il docente, la normativa europea, il regolamento **eIDAS** (per la chiave di firma, come precisato nel 2026). Le smart card sono **HSM portatili**: per questo un passaporto ha un valore commerciale che non è solo carta e filigrana ma la tecnologia del chip; lo stesso vale, in modo meno visibile, per le carte di pagamento (*DI-04 @ 01:40:06-01:41:42*).

**Slide "e-Passports and eIDAS standards"** (*DI-04 @ 01:39:58*). A sinistra lo schema delle quattro parti: *Part 1: ePassports*, *Part 2: Protocols for electronic IDentification, Authentication and trust Services (eIDAS)*, *Part 3: Common Specifications*, *Part 4: Applications and Document Profiles*. A destra la linea del tempo 2005-2020: **1st Generation** (*Facial image*): "Storage of high-resolution facial image; Symmetric cryptography (BAC) to protect contactless communication"; **2nd Generation** (*Addition of fingerprints*): "Additional storage of fingerprints; EAC to protect fingerprints via chip and terminal authentication"; **3rd Generation** (*PACE protocol*): "PACE protocol (Password Authenticated Connection Establishment); Encryption of contactless communication to avoid skimming & eavesdropping"; **Next Generation** (*eVisa, eStamps*): "Storage of eVisa and eStamps; Faster and more secure border control for visa holders; Addition of biometrics post-issuance; Transparent travel history". Bande: *BAC Basic Access Control*, *EAC Extended Access Control*, *SAC Supplementary Access Control*, *LDS 2.0*.

> **Nota aggiunta:** lo schema in quattro parti è quello della linea guida tecnica tedesca **BSI TR-03110** ("Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token"); qui "eIDAS" indica il *token* eID tedesco e non coincide con il regolamento UE (dato esterno).

**Slide "PKCS – Public-Key Exchange (PKIX) standards"** (*DI-04 @ 01:41:29*). A sinistra uno schema di provider Java-like: *HTTP(S) Connection Handler*, *LDAP(S) Connection Handler*, *OAuth 2.0 Authorization Mechanism* (tutti "Uses TLS, Refers to providers") → *Key Manager Provider* (*Provider name, Keystore PIN, Other properties*) → *Keystore* (*Key pair: Public key certificate, Private key*) e *Trust Manager Provider* (*Truststore PIN*) → *Truststore* (*Trusted certificate*); "Implemented as keystores (JKS, JCEKS, LDAP, PKCS#11, PKCS#12 and others)". A destra: "PKIX Cryptography Standards (PKCS) support several aspects of public-key infrastructures: 1. RSA Cryptography std.; 2. Diffie-Hellman (DH) Key Agreement; 3. Password-based encryption std.; 4. Extended-Certificate syntax std.; 5. Cryptographic Message Syntax (CMS); 6. Private-key information syntax std.; 7. Selected attribute types; 8. Certification Request std.; 9. Cryptographic Token Interface ("CTI"); 10. Personal Information Exchange syntax std.; 11. Elliptic-curve cryptography (ECC) std.; 12. Pseudo-Random Number Generation (PRNG); 13. "CTI" Format std."

Il docente: dietro tutti gli esempi crittografici ci sono standard come i **PKCS**, documenti pubblici scaricabili, per informatici e crittografi (*DI-04 @ 01:41:42*).

> **Correzione:** **PKCS** sta per *Public-Key Cryptography Standards* (RSA Laboratories); **PKIX** è il gruppo di lavoro IETF *Public-Key Infrastructure (X.509)*, autore fra l'altro di RFC 5280: la slide li fonde ("PKIX Cryptography Standards", "Public-Key Exchange"). Inoltre la numerazione della slide (1-13) non è quella ufficiale: PKCS #1 RSA, #3 DH, #5 cifratura basata su password, #6 certificati estesi, #7 CMS, #8 chiavi private, #9 attributi, #10 richiesta di certificato (la CSR della sezione 13), #11 interfaccia dei token crittografici (Cryptoki), #12 scambio di informazioni personali, #13 ECC, #14 PRNG, #15 formato delle informazioni dei token. Per chi lavora in Java: `JKS`/`JCEKS` sono keystore Java, `PKCS#12` è il formato `.p12`/`.pfx`, `PKCS#11` è l'interfaccia verso HSM e smart card.

## 17. Servizi fiduciari eIDAS: qualificati e non qualificati

*DI-04 @ 01:42:05-01:54:58. I dettagli 2026 sui servizi fiduciari (lezione Teams 5) sono nel **capitolo 05**.*

**Slide di sezione "Digital Identity & Trust Services"** (*DI-04 @ 01:42:05*) e **"Electronic Trust Services"** (*01:42:18*).

Si parla di **servizi fiduciari** quando il digital trust (garanzia forte di **autenticità**, cioè dell'origine del dato) è così forte da avere **effetti giuridici** (*DI-04 @ 01:42:14*).

Il **regolamento eIDAS**, nato nel 2014 e aggiornato nel 2024, è come il GDPR un regolamento europeo applicato allo stesso modo in tutti gli Stati membri, ma a differenza del GDPR non ha valore fuori dall'Europa: uno Stato estero non deve riconoscere le firme legate ai servizi fiduciari eIDAS. Ha "due teste": l'**identificazione elettronica** (ultima parte del corso) e la disciplina omogenea dei **servizi fiduciari** (*DI-04 @ 01:42:46-01:43:55*).

> **Nota aggiunta:** eIDAS è il regolamento (UE) **910/2014**; l'aggiornamento è il regolamento (UE) **2024/1183** ("eIDAS 2"), che introduce fra l'altro il portafoglio europeo di identità digitale (EUDIW) e nuovi servizi fiduciari (archiviazione elettronica, registri elettronici, attestazioni elettroniche di attributi).
>
> **Correzione:** il docente dice che il GDPR "è un regolamento globale perché riguarda tutti i cittadini dell'Unione, anche quelli al di fuori dell'Unione". L'ambito territoriale del GDPR (art. 3) non dipende dalla cittadinanza: si applica ai titolari stabiliti nell'UE e, per quelli extra-UE, ai trattamenti di dati di persone **che si trovano nell'Unione** (offerta di beni o servizi, monitoraggio del comportamento). Vedi guida Cybersecurity, capitolo 05, sezione 9.

**Slide "eIDAS Regulation (2024, 2014)"** (*DI-04 @ 01:45:48*, completa a *01:54:48*). Icone dei servizi: *e-attestation of attribute(s)*, *e-archival*, *e-ledger*, *notified eID schemes and EUDIW Framework*, *e-registered delivery service (eRDS)*, *web-authentication certificate (WAC)*, *e-time stamp*, *e-signature*, *e-seal*, *remote e-signing/sealing + their validation*; al centro il marchio UE (lucchetto con stelle e spunta), *citizens*, *businesses*, *public administrations*; in basso *(simple) electronic signature / seal*, *Advanced electronic signature / seal*, *Qualified electronic signature / seal*. Testo:

> PKIs are the technical bread-and-butter for market solutions offered by **trust service providers** (**eTSPs**).
>
> Trust services can be *qualified*: the eTSP providing them not only accredits itself to a MS' national eIDAS supervisory body (**AgID** for Italy), but also undergoes regular supervision in order to assure a highest and EU-harmonised level of digital trust.
>
> *Qualified* **trust service providers** (**QTSPs**) are listed in national trust lists freely available online at EC's website:

(Il testo si interrompe con i due punti: il link non è a schermo.)

I servizi fiduciari elencati a voce (*DI-04 @ 01:43:55-01:46:08*), con trattazione breve "in questi dieci minuti":
- **archiviazione elettronica**, in Italia "conservazione digitale";
- **registri elettronici**, distribuiti o no (sezione 18);
- **attestazioni elettroniche di attributi**, con le identità digitali;
- emissione dei **certificati di autenticazione di sito web** (WAC), i certificati TLS di oggi: in Europa sono un servizio fiduciario;
- **servizi elettronici di recapito certificato** (*e-registered delivery service*), che in Italia corrispondono grosso modo alla **PEC**. La PEC esiste solo in Italia e ha valore legale solo in Italia ("non parlerò della PEC"); alcuni gestori aderiscono alle norme europee con la "PEC europea", il cui vero nome è servizio di recapito certificato elettronico, riconosciuto fra Stati membri;
- **marcature temporali** o validazioni temporali elettroniche (sezione 19);
- **firme e sigilli elettronici** (lezione successiva, capitolo 05).

**Qualificati e non qualificati** (*DI-04 @ 01:46:08-01:54:27*):
- il **prestatore di servizi fiduciari** (*Trust Service Provider*) è una persona giuridica, di solito privata e a pagamento ma non necessariamente, che fornisce servizi delle sole categorie previste da eIDAS ed è riconosciuto da un organo di vigilanza nazionale: per l'Italia l'**AgID** (Agenzia per l'Italia Digitale), "che ha sede all'EUR";
- **qualificato** significa che il prestatore non è solo registrato ma si è **accreditato** presso l'organo di vigilanza: documentazione per lo più cartolare, un **security assessment** fatto da un soggetto terzo indipendente che attesta le misure di sicurezza fisica, tecnica e amministrativa richieste (vedi guida Cybersecurity, capitolo 06, sezione 2); diventa **QTSP**, e sono qualificati solo i servizi erogati secondo il manuale operativo approvato da AgID;
- scopo: valore giuridico e riconoscimento **transfrontaliero** identici in tutta Europa. Ogni Stato ha la sua autorità (Francia, Italia, Germania, Lettonia…), che vigila sui propri prestatori. Esempio: una firma qualificata di un cittadino estone, da un prestatore estone che non conosco ma che risulta qualificato, ha dietro un processo amministrativo e verifiche di sicurezza omogenee: "per fidarmi non devo essere un esperto di cyber security, ci ha pensato una governance europea". In eIDAS "si distilla" tutto il corso, comprese molte cose di Cybersecurity;
- **vigilanza**: secondo il docente "mi sembra almeno ogni due anni" si rifanno da capo tutte le ispezioni; l'autorità può chiederne una *ad hoc* in caso di sospetti e collabora con le autorità degli altri Stati, anche per furti di identità o di certificati. Il docente ha partecipato a queste sessioni quando lavorava in AgID;
- **firme e sigilli**: qualificati o non qualificati; i non qualificati sono "semplici" (nome giuridico: firme elettroniche, sigilli elettronici) o **avanzati**. Solo i servizi **qualificati** hanno validità piena e **obbligatoria** in tutta Europa: tutti gli organismi pubblici e privati devono riconoscerli; per i non qualificati decade l'obbligo di riconoscimento transfrontaliero;
- il **marchio di fiducia UE** (lucchetto con le stelle e la "V") identifica i servizi qualificati; è formale e si può contraffare (*DI-04 @ 01:54:27*).

> **Nota aggiunta:** l'art. 20 eIDAS prevede che i QTSP siano sottoposti a **audit almeno ogni 24 mesi**, a proprie spese, da un organismo di valutazione della conformità accreditato, che trasmette la relazione all'organo di vigilanza; l'organo di vigilanza può in ogni momento disporre audit o ispezioni. Il "due anni" del docente è corretto; a rifare le verifiche è l'organismo di valutazione, non l'autorità.

Nella lezione successiva il docente mostrerà una firma elettronica convalidata in un PDF (capitolo 05).

## 18. Registri distribuiti e blockchain

*DI-04 @ 01:54:58-01:58:46*

Un **registro distribuito** è un tipo di registro elettronico; diventa servizio fiduciario solo se fornito da un gestore registrato in Europa. Una **blockchain** è un modo possibile di realizzarlo. Le **criptovalute** "sono un mondo a parte" e hanno un corso dedicato nel master: oltre alla blockchain hanno norme, regolamenti, una governance dei permessi di lettura e scrittura, la scarsità delle risorse (*mining*), il **consenso**; altre blockchain servono per gli *smart contract* o per gli **NFT**, che danno valore concreto a un oggetto immateriale (*DI-04 @ 01:54:58-01:56:33*).

**Slide "Distributed ledgers (DLT, blockchain)"** (*DI-04 @ 01:57:49*). Testo:

> In general terms, a **blockchain** is a cryptographically implemented *linked list*, where each node: is identified by some UID (a digest or a signature); links *back* to the previous node's UID; it is itself digitally signed (electronically sealed).
>
> An **electronic ledger** is a *distributed* database (**DLT**) where modifications are allowed only when set rules are met (e.g. permissions, smart contracts, …).
>
> After a block is stored in a blockchain it is not possible to change it without invalidating all the blocks following it.
>
> **Crypto-assets** ("*digital representations of values and/or rights*") *may* be implemented using DLTs, although additional mechanisms are required to ensure transactions' security, e.g.: governance (permissions); resources' scarcity (e.g. *mining*); consensus (*proof-of-work*/*-stake*); infrastructure and networking; digitally implemented framework (smart contracts); *optional* crypto-physical interface e.g. non-fungible tokens (NFTs).

Schema: *"genesis" block (1)* con *Hash: 6U9P2*, *Previous Hash: 0000*; *block 2* con *Hash: 8Y5C9*, *Previous Hash: 6U9P2*; *block 3* con *Hash: 9l4z1*, *Previous Hash: 8Y5C9*; sotto, una catena principale con rami laterali (fork) e il dump di un blocco ("Block 0x43a5f078").

Il punto di vista del docente (*DI-04 @ 01:56:33-01:58:46*): una blockchain è un registro di transazioni, che possono essere anche solo un nome o il **seriale di un certificato revocato**: una **CRL** si può realizzare con una blockchain. In ogni blocco si calcola l'**impronta del blocco precedente** e il blocco è firmato con la chiave privata di chi ha il permesso di scrivere. Se qualcuno modifica il blocco 2, si invalida la sua firma e anche l'impronta del blocco 2 contenuta nel blocco 3, e così via: non si può modificare un blocco senza invalidare tutti i successivi. Utile per una CRL, ma anche per rappresentare una *consecutio temporum*, una linea del tempo. Per questo un **decreto legge del 2018** ha stabilito in Italia che una marcatura temporale elettronica può essere prodotta tramite un registro distribuito.

**Verifica per esecuzione** (Python, SHA-256): una catena di tre blocchi in cui ogni impronta è calcolata sul campo "hash precedente" più i dati ("genesis: CRL vuota", "revoca seriale 0A1B", "revoca seriale 77FF"; hash precedente del genesis = 64 zeri). La catena verifica; modificando il blocco 2 la verifica fallisce dal blocco 2; ricalcolando anche l'impronta del blocco 2 per nascondere la modifica, la verifica fallisce dal blocco 3, perché il suo campo "hash precedente" non coincide più. È esattamente la proprietà della slide. Gli hash della slide (6U9P2, 8Y5C9, 9l4z1) sono segnaposto illustrativi, non digest reali.

> **Nota aggiunta:** il decreto è il D.L. 14 dicembre 2018, n. 135 ("decreto Semplificazioni"), art. 8-ter, convertito dalla legge 11 febbraio 2019, n. 12: la memorizzazione di un documento informatico tramite tecnologie basate su registri distribuiti produce gli effetti giuridici della validazione temporale elettronica dell'art. 41 di eIDAS. In una blockchain pubblica come Bitcoin i blocchi non sono firmati da chi scrive: l'immutabilità viene dal concatenamento degli hash più il consenso (proof-of-work). La firma di ogni blocco descritta dal docente e dalla slide è tipica dei registri **permissioned**.

## 19. Marcatura temporale elettronica

*DI-04 @ 01:58:46-02:03:47*

Un'altra applicazione della firma digitale. La **marcatura temporale** (o validazione temporale) elettronica si realizza con un sistema che tecnicamente è una CA, ma si chiama **TSA**, *Time Stamping Authority*. Di una CA ci si fida perché identifica correttamente chi riceve i certificati; di una TSA ci si fida perché l'**ora** che attesta è corretta: i suoi orologi sono particolarmente ben sincronizzati con l'orario universale, come quelli dei media block del cinema, che però non hanno lo stesso valore legale (*DI-04 @ 01:58:46-02:00:20*).

**Slide "Electronic time stamping"** (*DI-04 @ 01:58:45*). A sinistra il ciclo *SEND A DOCUMENT* → *TIMESTAMP REQUEST* → *TSA* (con *RELIABLE TIME SOURCE*) → *TIMESTAMPING*. Testo:

> **electronic time stamp**, **eIDAS**: «*data in electronic form which binds other data in electronic form to a particular time establishing evidence that the latter data existed at that [exact] time*».
>
> **Time Stamping Authorities** (**TSA**s) are "CAs" specialised for the above purpose, whose 3rd CA feature is being **trusted** for reporting their **correct time** and the ability to associate it to documents.
>
> The digest of a document is sent to a TSA which couples it with an exact time (by its own *trusted* clock), wraps with other optional metadata (e.g. document's name, file size, …) and remotely digitally signs it with its private TSA key, associated to a digital certificate with `timestamping` keyUsage.
>
> Times stored in DLTs can be used as **electronic time-stamps**. **eIDAS2** defines both **qualified TSAs** and **DLTs**.

Sulla linea del tempo (*Past* → *Future*): *Document is created* 2010/03/12 10:08:30; *TS is issued* 2010/03/12 14:25:09, con il timbro "Korea Digital Time Stamp Service, e-timing, 2010/03/12 14:25 KST" ("Verifying the document's existence at a certain time"); *TS is verified* 2010/09/21 18:15:29, timbro "2010/09/21 18:15 KST", *OK* ("Verifying the document's authenticity as of the time at which such verification is conducted").

Il procedimento (*DI-04 @ 02:00:20-02:02:11*): è un processo di firma remota. Si calcola l'impronta del documento e la si invia alla TSA, che restituisce un oggetto firmato con in pratica due dati: l'**orario** di ricezione dell'impronta e la **firma** dell'insieme. Una marca temporale è di fatto un certificato che non attesta una chiave pubblica ma l'**associazione fra un orario e un hash**. Se la TSA coreana attesta che il 12 marzo 2010 alle 14:25 ora coreana ha ricevuto quell'impronta, il documento con quell'impronta esisteva in quel momento: non si può "inventare" l'hash di un documento che non esiste (le proprietà delle funzioni di hash del capitolo 01). È la prova dell'"esistenza in vita" di un documento. La TSA **non firma** il documento e non appone sigilli elettronici: attesta solo l'esistenza.

"Noi italiani abbiamo imparato a farlo tanti anni fa": un modo semplice di avere una marca temporale è mandarsi il documento via **PEC**, perché l'orario attestato dai gestori ha valore legale in Italia (per esempio per la ricezione di una domanda di concorso) (*DI-04 @ 02:02:11-02:03:13*).

> **Nota aggiunta:** il protocollo standard è RFC 3161 (*Time-Stamp Protocol*); il certificato della TSA ha nell'*Extended Key Usage* lo scopo `id-kp-timeStamping`. La definizione della slide è quella dell'art. 3 n. 33 di eIDAS ("validazione temporale elettronica"); l'aggettivo "[exact]" fra parentesi è un'aggiunta della slide.

## 20. Domanda finale: VPN e certificati radice

*DI-04 @ 01:03:08-01:04:40 (domanda), 02:03:48-02:10:45 (risposta, a registrazione formalmente conclusa)*

**La domanda.** Uno studente ripete l'esperimento su `repubblica.it` con due VPN su due computer, una personale e una aziendale: nella gerarchia dei certificati la radice è quella della VPN, sopra `www.lastampa.it` compare il nome della VPN.

**La risposta del docente.** Una VPN crea di fatto una nuova interfaccia di rete virtuale verso il gateway di uscita, come staccare il cavo del proprio gestore e attaccare quello dell'azienda: cambia l'identità del calcolatore (vedi guida Cybersecurity, capitolo 05, sezione 3). Normalmente l'autenticazione è solo lato server: Alice (il browser) deve essere certa di Bob (Repubblica), a Bob non interessa chi sia Alice ("Alice o Gilbestro"). Con la VPN, secondo il docente, c'è una **mutua autenticazione**: il gestore VPN presenta al server un certificato che per privacy non contiene il nome dell'utente ma quello del gestore, e la sicurezza è garantita dal software VPN e dalla chiave privata impiantata nel certificate store. Sul laptop aziendale la VPN l'ha installata l'IT con i diritti amministrativi; su quello personale l'utente l'ha autorizzata dando la password di amministratore. Da qui un consiglio di igiene: usare il computer con un **utente non amministrativo** non è "la panacea", "qualunque cosa si bypassa", ma almeno un buon 20% degli attacchi meno sofisticati fa comparire un pop-up che chiede i privilegi (*DI-04 @ 02:03:48-02:10:45*).

> **Correzione:** l'autenticazione del client non cambia la catena del **server** mostrata dal browser. Se sopra `www.lastampa.it` compare una radice della VPN, il software VPN (o di sicurezza) fa **ispezione TLS**: termina la connessione verso il sito e la ricrea verso il browser con un certificato di `www.lastampa.it` generato al volo e firmato da una **propria CA**, la cui radice è stata installata nel certificate store del computer durante l'installazione, con i diritti di amministratore. È un "uomo nel mezzo" autorizzato. La parte finale della risposta del docente (installazione con diritti amministrativi, certificate store) è proprio il punto chiave: chi controlla il trust store controlla di chi si fida il browser.

## 21. Glossario

| Termine | Significato nel corso |
|---|---|
| PKI | Grafo orientato di CA collegate da relazioni di fiducia: gerarchica, mesh, ad anello, ibrida |
| CA radice, intermedia, foglia | Posizione della CA nella gerarchia; la radice ha un certificato autofirmato, la foglia emette solo certificati finali |
| Bridge CA | CA ponte che collega le radici di PKI diverse |
| Certificato autofirmato | Firmato con la chiave privata corrispondente alla chiave pubblica che contiene |
| CA tecnica / amministrativa | Il software o hardware che firma i certificati / la persona giuridica (eTSP) che offre il servizio |
| RA (Registration Authority) | Componente che identifica chi chiede un certificato (*identity proofing*, *onboarding*) |
| VA (Validation Authority) | Componente che consente alle terze parti di verificare la validità di un certificato, anche a una data passata |
| Not before / not after | Periodo di validità del certificato, obbligatorio in X.509 e CVC; la "morte programmata" |
| Trust list | *Allow list* firmata di certificati (di solito radice) di cui fidarsi; es. elenco di fiducia eIDAS, certificate store |
| CRL | *Deny list* firmata dei seriali dei certificati revocati, con data e ora di revoca |
| OCSP | Servizio online che risponde sullo stato di un certificato (valido, revocato, sospeso; in RFC 6960 *good*, *revoked*, *unknown*) |
| Sospensione | Invalidità temporanea e reversibile (`certificateHold`) |
| Key management | Gestione del ciclo di vita delle chiavi segrete: generazione, registrazione, conservazione, distribuzione, uso, rotazione, backup, revoca, distruzione |
| PFS (perfect forward secrecy) | Uso di chiavi di sessione effimere, distrutte dopo l'uso, così che la compromissione futura delle chiavi a lungo termine non esponga le sessioni passate |
| Chiave effimera | Chiave simmetrica di sessione usata per poco tempo e poi cancellata |
| Diffie-Hellman (DH, ECDH) | Accordo di chiave su canale non fidato basato sul logaritmo discreto ($g^{ab} \bmod p$; $abG$ su curva ellittica) |
| TLS | Protocollo dei siti `https://`: handshake, autenticazione del server, chiave di sessione |
| WAC | *Website authentication certificate*: il certificato TLS nel lessico eIDAS |
| SAN | *Subject Alternative Name*: elenco dei domini coperti da un certificato |
| Certificate store | Trust store di sistema operativo o browser con i certificati radice |
| Web PKI | Insieme delle PKI le cui radici sono nei certificate store dei browser (CA/Browser Forum) |
| HSM | Hardware Security Module: genera, custodisce e usa chiavi segrete senza esportarle |
| SSCD / QSCD / RSCD | Dispositivo sicuro / qualificato / remoto di creazione di firma o sigillo |
| Cassaforte digitale | HSM più software di autenticazione di fronte |
| CSR | *Certificate Signing Request* (PKCS #10): chiave pubblica e dati del richiedente firmati con la sua chiave privata |
| Media block | HSM del proiettore digital cinema, con chiave privata RSA e orologio anti-tamper |
| Chiave di contenuto | Chiave simmetrica (AES) con cui è cifrato il film, generata una volta sola |
| KDM | *Key Delivery Message*: file XML firmato con la chiave di contenuto cifrata per i media block autorizzati e la finestra temporale |
| DCP | *Digital Cinema Package*: il film in formato digitale per le sale |
| Firma remota | Firma calcolata da un HSM remoto con la chiave del titolare, sotto il suo controllo esclusivo |
| CieSign | App del Ministero dell'Interno per firmare con la CIE via NFC |
| PACE, BAC, EAC | Protocolli di accesso ai chip dei passaporti elettronici |
| PKCS | *Public-Key Cryptography Standards* (RSA Labs) |
| eIDAS | Regolamento (UE) 910/2014, aggiornato dal regolamento (UE) 2024/1183 |
| (Q)TSP | Prestatore di servizi fiduciari (qualificato) |
| AgID | Agenzia per l'Italia Digitale, organo di vigilanza eIDAS per l'Italia |
| Blockchain | Lista concatenata crittograficamente: ogni blocco contiene l'impronta del precedente |
| DLT | *Distributed ledger technology*, registro distribuito |
| TSA | *Time Stamping Authority*: CA specializzata che associa un orario fidato a un'impronta |

## 22. Punti incerti

- **Firmatario della KDM**: a voce "il sistema di gestione delle chiavi dell'esercente, un servizio in cloud" (*DI-04 @ 01:28:53*); nella slide "signed by the Mastering Lab" e "e-sealed by the distributor's private key"; in Teams 4 "il distributore, l'azienda di mastering". Le fonti non coincidono.
- **Nomi dei certificati non visibili nei frame**: per New York Times, Apple e Google i frame conservati mostrano solo le home page. "THOT" (a voce, per il New York Times) potrebbe essere Thawte, marchio di DigiCert, o il nome di un intermedio: [?]. "GTS" è con buona probabilità Google Trust Services.
- **Intermedio Amazon nel 2026**: "M04" a voce in Teams 4 contro "M02" nel frame del 2025; nel 2026 non c'è il frame. Anche la durata dell'intermedio (24/08/2022-24/08/2030) è solo a voce.
- **Dominio typosquatting** dell'esempio: "republic.co4", "republic4.it", "www.republic4.it" nella trascrizione: [?].
- **Costruttori di proiettori**: il primo nome a voce nel 2025 è trascritto "Rilla" [?]; nel 2026 Dolby, Barco, Fuji, Sony.
- **"Seconda" o "quarta" CA di Amazon**: è la lettura del docente del suffisso M02/M04, non un dato del certificato.
- **YubiKey**: in Teams 3 e 4 la trascrizione dice "UB key" [?].
- **Vigilanza "ogni due anni"**: il docente dice "mi sembra"; verificato sull'art. 20 eIDAS (audit almeno ogni 24 mesi).

## 23. Esame

Nessuna indicazione esplicita sull'esame in DI-04 né nelle parti di Teams 3 e Teams 4 di questo capitolo. Le frasi su ciò che **non** verrà chiesto o che non interessa ai fini del corso:

- "Non ci saranno domande di matematica nel corso" (*DI-04 @ 00:44:27*), prima dell'esempio Diffie-Hellman con numeri piccoli.
- "A me non interessa che impariate come funziona Diffie-Hellman, adesso ve lo descrivo molto rapidamente, facendo riferimento a un po' di algebra modulare, ma non mi interessa" (*DI-04 @ 00:46:12-00:46:21*); i dettagli si vedranno "in altri corsi di crittografia più teorica".
- Sulle topologie non gerarchiche delle PKI: "non entro nei dettagli, perché questa è una materia che comincia a essere materia per specialisti" (*DI-04 @ 00:03:11*).
- Sul DRM dei televisori: "non vi spiego quello perché è più complesso" (*DI-04 @ 01:23:18*); sulle cause della pirateria nelle sale: "per altri motivi che però non vi spiego" (*DI-04 @ 01:32:53*).
- "La PEC è una cosa che c'è solo in Italia, non parlerò della PEC in questo corso" (*DI-04 @ 01:45:13*); sulle criptovalute "avete anche un corso a riguardo, quindi non entro nel merito" (*DI-04 @ 01:55:41*).
- Nel 2026, sul cinema digitale: "ai fini di questo corso, ai fini del vostro master in Data Analytics, non rileva questa ulteriore complessità" (Teams 4 @ 0:10:46) e "una complessità che ai fini didattici non serve" (Teams 4 @ 0:12:22); su Diffie-Hellman: "cambiano i dettagli algebrici ai quali non sono interessato per gli scopi di questo corso" (Teams 4 @ 0:50:25).

Due momenti in cui il docente verifica la comprensione con una domanda attesa: "mi aspetto almeno una domanda… che mi serve per capire se avete capito" (*DI-04 @ 01:03:08*), cioè perché un certificato intestato a `www.lastampa.it` sia valido su `www.repubblica.it` (risposta: il SAN, sezione 10). Per il quadro completo vedi la pagina [Assessment](assessment.md).
