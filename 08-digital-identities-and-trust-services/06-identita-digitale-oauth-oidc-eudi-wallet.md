# 06 - Identity proofing, autenticazione centralizzata e federata, deleghe, identità autosovrana, SAML, OAuth 2.0, OpenID Connect, SD-JWT, SPID, CIE ed EUDI Wallet

*DI-06, registrazione Teams del 30/10/2025 (portale), 1:46:38; parlato fino a 1:46:32. Ultima lezione del corso 2025. Integrazioni da Teams 6 (28/09/2026, dal punto 1:01:44 fino alla fine, 1:53:41), Teams 7 (29/09/2026, intera, 0:58:56) e Teams 8 (30/09/2026, intera, 1:59:31).*

> **Come leggere questo capitolo.** Nel 2025 la lezione riprende le slide "ritrovate" della lezione precedente (standard, identity proofing) e poi copre in un'ora e tre quarti tutto il blocco identità digitali: autenticazione centralizzata e federata, deleghe, identità autosovrana (SSI), SAML, OAuth 2.0, OpenID Connect, selective disclosure con SD-JWT, gli schemi italiani SPID e CIE, gli attributi e l'EUDI Wallet. Nel 2026 lo stesso blocco occupa la seconda metà di Teams 6, tutta Teams 7 e tutta Teams 8, con molto più spazio per identity proofing, fattori di autenticazione, Kerberos, deleghe di Active Directory, credenziali verificabili e governance del wallet. Fattori di autenticazione e Kerberos nel 2025 sono nel capitolo 05: qui hanno sezioni dedicate (3 e 4) perché il materiale 2026 sta nel perimetro di questo capitolo. Le registrazioni 2026 non hanno slide: dove il docente dice "questa slide" si tratta, per quanto ricostruibile dal parlato, delle stesse slide del 2025. Il docente rimanda più volte al corso di Cybersecurity (minaccia come capacità, opportunità e intento; gestione e trasferimento del rischio; sicurezza amministrativa): vedi guida [Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/README.md).

## Indice

1. Ripresa: standard e regolamenti dell'identità digitale
2. Identity proofing
3. Fattori di autenticazione, autenticazione locale e SCA (solo Teams 2026)
4. Kerberos e deleghe di Active Directory (solo Teams 2026)
5. Autenticazione centralizzata: identity provider e service provider
6. Single sign-on
7. Identità federata e fornitori di attributi
8. Deleghe di identità
9. Identità autosovrana (SSI)
10. Identificazione elettronica e biometria
11. SSI e privacy: credenziali e presentazioni verificabili
12. Autenticazione e autorizzazione: l'esempio della fatturazione elettronica
13. SAML
14. OAuth 2.0
15. OpenID Connect e OpenID Federation
16. Selective disclosure: SD-JWT e KB-JWT
17. Gli schemi eID italiani: SPID, CIE, IT-Wallet
18. L'ecosistema CIE/SPID: aggregatori, RAO, gestori di attributi, deleghe
19. Flusso SAML, livelli di garanzia e interfaccia di SPID e CIE
20. Attributi SPID e CIE, identità ad uso professionale
21. Attributi qualificati e non qualificati
22. eIDAS 2 e l'EUDI Wallet
23. Sicurezza del wallet, trust list e chiusura del corso
24. Bibliografia
25. Glossario
26. Punti incerti
27. Esame

## 1. Ripresa: standard e regolamenti dell'identità digitale

*DI-06 @ 00:00:01*

Il docente apre dicendo che nella lezione precedente aveva introdotto autenticazione e identità digitali e che ha "ritrovato le slide che mancavano". Riproietta la slide degli standard, già commentata in DI-05 (capitolo 05).

**Slide "Digital Identity standards and regulations"** (*DI-06 @ 00:01:08*). Intestazione: "eIDAS2 Regulation: https://eur-lex.europa.eu/eli/reg/2024/1183/oj". Colonna sinistra:

> **Electronic identification** (*Eid.*) is the process of using person identification data (PII) in electronic form uniquely representing a *natural person*, a *legal person*, or a *natural one representing a legal person*.
>
> Eid. ***means*** is a material or immaterial unit containing PII and used for online authentication.
>
> Eid. ***scheme*** is a system for Eid., whose Eid. means are issued to the above 3 kinds of persons.
>
> Currently, eIDAS Regulation provides for each MS to **notify** *at least* one Eid. scheme to the European Commission (**EC**), so that ***notified* schemes** (**eIDs**) can be peer-reviewed and become interoperable with each other for the mutual Eid. of EU citizens. eIDs may be certified pursuant to other legal acts.
>
> Each MS must provide at least for a national **EUDI Wallet** to be accessible by means of notified eID(s).
>
> \* eIDAS1 LoAs as currently *loosely* based on ISO 29115.

Colonna destra:

> eIDs may be subject to **certification** (e.g. pursuant to **Cybersecurity Act**).
>
> eIDs are classified according to a 3-levels LoA\*: LOW = LoA **2**; SUBSTANTIAL = LoA **3**; HIGH = LoA **4**.
>
> LoA has different requirements, ranging from persons' enrolment, to suspension/revocation/reactivation/renewal, authentication, scheme management (ISMS, record keeping, compliance) and governance.
>
> eIDs are notified at one or multiple LoAs but in order to attain a LoA, the scheme must be met *at least* that LoA against *all* the requirements.
>
> Italy shall have one public- and potentially multiple private-sector EUDI wallets: the **IT Wallet** System.
>
> Italian eIDs are: **SPID** (notified in 2018 with all 3 LoAs) and **CIE** (notified in 2019 with LoA HIGH).

> **Nota aggiunta:** il regolamento eIDAS è il Reg. (UE) 910/2014; eIDAS 2 è il Reg. (UE) 2024/1183 che lo modifica (in vigore dal 20/05/2024). I livelli di garanzia sono definiti dall'art. 8 del 910/2014 e dettagliati dal Reg. di esecuzione (UE) 2015/1502. La numerazione 2, 3, 4 viene dalla scala a quattro livelli di ISO/IEC 29115 (dove il livello 1 non ha corrispondente eIDAS). Sulla discrepanza fra "LOW" di questa slide e "MEDIUM" della slide di *01:14:44* vedi sezione 19.

## 2. Identity proofing

*DI-06 @ 00:00:57-00:03:52*

**Slide "Identity proofing"** (*DI-06 @ 00:02:14*, versione completa *00:03:03*). Testo in alto a sinistra: "In some contexts (e.g. issuance of physical or electronic IDs) the identity proofing phase is the only point in time in which the real identity of a user is checked." Sequenza in alto: (1) "Collect identifying information e.g. passport, driving license, answers to security questions"; (2) "Confirm information is authentic and accurate and the claimed identity exists"; (3) "Confirm the claimed identity belongs to the user". Livelli:

- **IAL1**: no requirement to link to real-life identity; any other attributes are self-asserted (or treated as such);
- **IAL2**: real-world existence claims (*either remote or physical-presence* required); pseudonyms could be used;
- **IAL3**: physical presence required; attributes need to be verified as well.

Testo a sinistra in basso: "Evidence is classified as FAIR, STRONG, and SUPERIOR; may include physical IDs and/or biometric data. Credentials are supplied by a CS. *This is not in SP800-63A* Identity (credentials) may also be suspended or revoked. Today, remote identification criteria are paramount." Schema a percorso stradale: *Applicant* → **1 Resolution** (core attributes and evidence collected; "Individual uniquely distinguished among a given population or context") → **2 Validation** (evidence validated; "Authenticity, validity, and accuracy of identity determined and related to a real-life subject") → **3 Verification** (evidence verified; "Linkage between claimed identity and real-life existence of subject presenting evidence confirmed and established") → *Subscriber*. A destra: "*This is not in SP800-63A* Identity proofing may be hardened by requiring re-proofing at set timeframes in the future, after the eID was issued (e.g. when a physical ID expires)."

L'**identity proofing** è il momento più cruciale del ciclo di vita di un'identità digitale: un'autorità tecnica o amministrativa assegna un **alias digitale**, un'identità virtuale, a una persona fisica, a una persona giuridica o anche a un sistema informatico. In quel momento vengono stabiliti i fattori di autenticazione: l'utente sceglie password e PIN, il dispositivo di cui dimostrare il possesso (*DI-06 @ 00:01:27*).

Se un attore della minaccia inganna questo processo, al termine (punto 3 dell'immagine) gli viene confermata l'identità: è il **furto di identità digitale**. Da quel momento può autenticarsi più e più volte con una falsa identità "legittimamente concessa", ed è molto difficile accorgersi in seconda battuta che l'identità è stata assegnata alla persona sbagliata. Diverso è attaccare una singola autenticazione: chi ruba una password e la usa una volta probabilmente la volta dopo non ci riesce o viene scoperto; chi si impossessa dell'identità la "rispende" ogni volta ed è considerato la persona che rappresenta, con molti più danni potenziali (*DI-06 @ 00:02:31-00:03:52*).

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 2 (identity proofing): nel 2026 il blocco identità digitali parte da qui*

- **Passaggio al nuovo argomento.** Chiusa la marcatura temporale, il docente dice che "questo termina l'argomento dei trust service" e porta all'ultimo argomento del corso, le identità digitali, dove "metteremo a terra tutti questi pezzi", compresi quelli del corso di Cybersecurity. (Teams 6 @ 1:01:44)
- **Persone dietro i sistemi.** Tutte le attività online, anche quelle demandate alle intelligenze artificiali, sono svolte da persone: invece di dire che un modello "ha fatto" qualcosa bisognerebbe dire che l'ha fatto l'azienda, ricordando che la responsabilità legale va in capo a persone fisiche; il diritto non dà ancora volontà giuridica a un sistema tecnico. Nel cyberspazio non interagiamo con persone ma con identità digitali, "alias di persone" che lasciano impronte. Il tema filosofico (Asimov, robotica) è rimandato "per chi farà il master di secondo livello nel corso dedicato alla cyber intelligence e alle intelligenze artificiali". (Teams 6 @ 1:02:08-1:05:52)
- **Identità digitale non è account.** Ridurla a username e password è "estremamente fuorviante": dietro ci sono processi che danno valore legale alle azioni. L'account del servizio di pizza a domicilio non è un'identità digitale: al massimo permette di ordinare cento pizze all'indirizzo sbagliato (il rischio vero è il furto dell'intero database, tema di Cybersecurity). Lo diventa quando all'account sono conferiti, magari per legge, diritti con effetti giuridici: un'istanza a un tribunale, un certificato, l'iscrizione a un master a distanza, un'assunzione da remoto (casi di avatar fasulli assunti come dipendenti). (Teams 6 @ 1:05:52-1:09:46)
- **Identity proofing, onboarding, KYC.** In italiano l'identity proofing è l'**identificazione elettronica**, una tantum; nel mondo commerciale è l'**onboarding**, prima fase del **know your customer** (KYC) con cui il venditore comincia a profilarti. Un attore istituzionale fa solo l'identity proofing, perché per legge deve identificarti ma non può tracciarti. (Teams 6 @ 1:10:02-1:11:18)
- **I livelli IAL di NIST.** Nello standard NIST SP 800 sull'identità digitale l'identity proofing è chiamato **identity assurance**, con tre livelli: IAL1 senza collegamento a un'identità reale, attributi autodichiarati; IAL2 con un raffronto con il mondo reale, presenza fisica "anche se da remoto", pseudonimi ancora ammessi; IAL3, livello governativo, presenza fisica e tutti gli attributi (anche colore di occhi e capelli, email, telefono) verificati uno per uno. In eIDAS corrispondono ai livelli di garanzia sostanziale ed elevato. (Teams 6 @ 1:12:36-1:14:59)
- **Perché gli attaccanti investono qui.** Battere un identity proofing robusto costa molto, ma una volta ottenuta in buona fede un'identità altrui la si riusa senza più attaccare, in modo tecnicamente valido per tutte le controparti, e "nessuno si accorgerà poi mai più" che non sei tu. (Teams 6 @ 1:14:16-1:16:21)
- **Digital double e deepfake.** Per uno studio per la Commissione sul riconoscimento non in presenza, il docente usò come prova di concetto gli effetti speciali cinematografici: per un film del 2018 a cui ha lavorato fu costruito un *digital double* animabile in tempo reale da foto ad alta risoluzione prese da più angolazioni, con un computer "da supermercato" e qualche GPU. Oggi i deepfake video e audio richiedono ancora meno risorse, perché la risoluzione di un social o di un telefono è molto inferiore a quella del cinema. Sono più pericolosi nell'identity proofing che nell'autenticazione. (Teams 6 @ 1:16:25-1:21:29)
- **L'esempio del Secure Element.** Se un attaccante ottiene con un deepfake un'identità intestata a un'altra persona e registra la *propria* impronta sul *proprio* telefono, a ogni autenticazione l'impronta viene verificata solo dal Secure Element del telefono e non arriva mai al sito: non è nemmeno disponibile per un'indagine forense. L'associazione fasulla creata a monte è poi difficile da disconoscere. (Teams 6 @ 1:21:29-1:22:47)
- **Re-proofing.** Se emerge che un'identità potrebbe non essere stata concessa correttamente, si può tornare dal soggetto che l'ha emessa e chiedere un *identity re-proofing*, abbassando nel frattempo il grado di confidenza (e le operazioni consentite). Avviene in automatico quando scade o è revocato il documento d'identità fornito in fase di identificazione. (Teams 6 @ 1:41:44-1:42:59)

> **Nota aggiunta:** i livelli IAL sono definiti in NIST SP 800-63A (la serie SP 800-63 sulle *Digital Identity Guidelines*). Le classi di evidenza FAIR, STRONG, SUPERIOR della slide sono le categorie di forza delle evidenze della stessa serie; la slide stessa segnala con "This is not in SP800-63A" le parti aggiunte dal docente.

## 3. Fattori di autenticazione, autenticazione locale e SCA

*Sezione solo 2026: il 2025 tratta questi temi nel capitolo 05 (DI-05).*

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 3 (fattori di autenticazione, autenticazione locale, SCA)*

- **Autenticazione contro identity proofing.** L'autenticazione è il processo con cui la persona fisica, o il sistema informatico, ogni volta dimostra di essere veramente lei. (Teams 6 @ 1:22:47)
- **I tre fattori.** *Something you know* (conoscenza: password, PIN, parole e frasi segrete, passphrase); *something you have* (possesso o prossimità di un dispositivo fisico che fa da token); *something you are* (inerenza: retina, vasi sanguigni del palmo, impronte di uno o più polpastrelli o della mano, timbro vocale, iride). (Teams 6 @ 1:23:03-1:24:12)
- **Il possesso deve essere vero possesso.** Ricordando i processi di notifica di SPID e CIE in Commissione (2017-2018), il docente riporta la posizione di alcuni Stati membri: un OTP visibile su un telefono sbloccato può essere letto da chiunque passi davanti, quindi è una prova di *lettura*, non di possesso. Per esserlo il codice deve comparire solo dopo uno sblocco (biometrico, PIN, gesto) del telefono o dell'app. Analogia con i token bancari di dieci anni fa: quello col numero sempre visibile contro quello che lo mostra solo dopo una password. Alcuni Stati consideravano questa seconda variante un'autenticazione a due fattori, altri no. (Teams 6 @ 1:24:12-1:27:56)
- **Il "quarto fattore".** C'è chi parla di *somewhere you are*: la posizione (rete aziendale, VPN aziendale, GPS dentro il perimetro dopo un badge) può "scontare" un fattore. Lo standard NIST ne prevede solo tre. (Teams 6 @ 1:28:00-1:29:05)
- **I fattori si contano solo se diversi.** Tre password non fanno un'autenticazione a tre fattori: chi ne aggira una (file di password, post-it virtuale, *authentication bypass*, ingegneria sociale ripetuta, foglio sotto il cassetto) aggira le altre allo stesso modo. Password + token + impronta letta da un altro token sono tre fattori; aggiungere altri quattro dati biometrici non aggiunge fattori. (Teams 6 @ 1:29:05-1:31:55)
- **Autenticazione locale.** Il sistema che presenta la *challenge* è lo stesso che conserva i dati di raffronto (l'hash della password, l'impronta crittografica delle minuzie dell'impronta digitale) e dà il responso. Vale per il laptop di casa ma anche per il servizio di pizza online che tiene l'elenco dei suoi clienti: client e server possono essere macchine diverse. (Teams 6 @ 1:32:07-1:34:56)
- **Smart card e token.** Anche con più fattori l'autenticazione può restare locale: il sistema invia un *blob* di dati (spesso casuali), il piccolo HSM nella carta (pagamento, passaporto, badge) lo firma con una chiave privata di autenticazione, il verificatore convalida la firma con il certificato e ne estrae i dati identificativi ("benvenuto Mario Rossi"; alcuni POS americani mostrano il nome letto dal certificato della carta). (Teams 6 @ 1:35:02-1:37:17)
- **SCA e dynamic linking.** Nel settore finanziario la **strong customer authentication** è un'autenticazione a più fattori in cui il blob firmato contiene i dati della specifica transazione (*dynamic linking*): finestra temporale, importo e valuta, identificativo del POS e dell'esercente. La firma non è riutilizzabile per un'altra spesa, nemmeno dello stesso importo; è l'analogo digitale dello scontrino firmato a mano. Per questo dopo un pagamento fallito l'esercente deve reinserire tutto. (Teams 6 @ 1:37:27-1:40:01)
- **Riautenticazione per le operazioni dispositive.** La PSD2 prevede che, già dentro l'home banking autenticati a due fattori, le operazioni dispositive (bonifico, ricarica, compravendita di titoli) richiedano di nuovo almeno un fattore, tipicamente biometrico o di possesso: protegge dal furto del cookie di sessione dopo che l'utente è stato distratto. (Teams 6 @ 1:40:01-1:41:44)

> **Nota aggiunta:** il docente dice che la PSD2 chiede di riautenticare "l'esercente"; nel contesto dell'home banking si intende l'utente (il pagatore). La SCA con collegamento dinamico è disciplinata dalla direttiva (UE) 2015/2366 (PSD2) e dal Reg. delegato (UE) 2018/389.

## 4. Kerberos e deleghe di Active Directory

*Sezione solo 2026: Kerberos nel 2025 è trattato nel capitolo 05 (DI-05); a DI-06 @ 00:03:52 il docente lo richiama soltanto.*

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 4 (Kerberos, Active Directory, deleghe AD)*

- **Perché simmetrico.** Kerberos, nato nel mondo Unix e oggi usato ovunque (anche da Active Directory come protocollo di default), fu progettato su crittografia **simmetrica** perché i computer dell'epoca avevano poca capacità di calcolo e operazioni a chiave pubblica a ogni logon avrebbero rallentato la rete. Le versioni moderne, soprattutto in Active Directory, supportano autenticazione multifattoriale con certificati (smart card, token USB, app authenticator) e quindi chiave pubblica. È l'esempio, anticipato in Teams 1, di autenticazione basata solo su cifratura simmetrica. (Teams 7 @ 0:24:36-0:27:33)
- **Il Luna Park.** Al logon il **domain controller** (che fa da identity provider) rilascia il **ticket granting ticket** (TGT), il biglietto d'ingresso, che dura alcune ore e si rinnova in automatico. Per ogni servizio (stampante di rete, database, sito intranet, tornelli) il client presenta in modo invisibile il TGT al domain controller, che ne verifica autenticità e validità e rilascia un **service ticket**, da presentare al server finale, senza chiedere di nuovo la password (che sarebbe un'occasione in più di esfiltrazione). Oggi a "ticket" si direbbe "token". (Teams 7 @ 0:27:33-0:31:55)
- **Chiavi.** I messaggi sono cifrati con chiavi simmetriche derivate dagli hash delle password degli account; il TGT con la chiave dell'account di servizio `krbtgt`; altre chiavi sono effimere, valide per la sessione. "Non è mia intenzione descrivervi come funziona tecnicamente il protocollo". (Teams 7 @ 0:31:55-0:32:49)
- **Autocorrezione.** "Prima ho fatto un errore": Kerberos è un sistema di **autenticazione**, non di autorizzazione. (Teams 7 @ 0:32:55)
- **Federazione aziendale.** Una *foresta* di domini Active Directory, anche di aziende acquisite in momenti diversi, collegate da **relazioni di fiducia** (*trust relationship*, lo stesso termine usato nell'identità federata) è un esempio di identità federata interna. (Teams 7 @ 0:12:07-0:13:10)
- **Delega in Active Directory = proxying.** In AD "delegation" indica in realtà l'*identity proxying* (proxy = procura): il sistema A chiede una risorsa al sistema B per conto dell'utente autenticato su A. Esempio: "Bob from Sales", che non sa SQL, usa un portale web (A) che interroga il database (B) "on behalf of" Bob, così B restituisce solo i dati che Bob può vedere (i suoi clienti), mentre il suo responsabile vede tutte le vendite, il finance solo aggregati, l'amministratore delegato dati più aggregati e più riservati. (Teams 7 @ 0:43:07-0:48:37)
- **Tre generazioni di delega.** (1) *Unconstrained delegation*: A può impersonare qualunque utente verso qualunque sistema, vulnerabile ma ancora supportata per compatibilità; (2) *constrained delegation*: nell'account di A l'attributo `msDS-AllowedToDelegateTo` elenca i servizi verso cui A può delegare; (3) *resource-based constrained delegation* (RBCD): il modello di fiducia è invertito e l'elenco dei sistemi autorizzati a chiedere in delega sta su B. Poiché tutte e tre sono attive di default, un dominio mal configurato ha le vulnerabilità di tutte: meglio usare le deleghe il meno possibile e, dove servono, solo RBCD. (Teams 7 @ 0:48:37-0:51:45)

> **Correzione:** il docente data Kerberos "ai primi anni '90" (Teams 7 @ 0:24:46, 0:33:14). Kerberos nasce al MIT nel Progetto Athena a metà degli anni '80 (versione 4 alla fine del decennio); la versione 5 è del 1993 (RFC 1510, oggi RFC 4120). In Teams 1 lo stesso docente aveva detto "anni '80". L'estensione a chiave pubblica per il logon con smart card è PKINIT (RFC 4556).

## 5. Autenticazione centralizzata: identity provider e service provider

*DI-06 @ 00:03:52*

**Slide "Centralized authentication"** (*DI-06 @ 00:03:02*, ripresa *00:13:59* e *00:14:59*). Schema: *User* al centro; freccia "requests to use service(s)" verso *SPs / RPs* (un server grande e quattro piccoli); freccia "authenticates" verso *IdP*; fra SP e IdP una chiave e la scritta "trust relationship". Testo:

> Multiple subjects are involved:
> - users *or* clients;
> - one or more service providers (**SP**s) *or* relying parties (**RP**s);
> - one identity provider (**IdP**);
>
> Data involved in identity proofing and authentication is electronically **seal**ed by the relevant CA/PKI of involved parties (both IdPs and RPs) in order to be acknowledged, even with legal relevance.

(Nella slide l'ultimo inciso è introdotto da un trattino lungo, reso qui con una virgola.)

Nell'autenticazione locale vista con Kerberos i ruoli non sono solo due (client, che può essere il computer o il browser, e server, il fornitore del servizio): spesso c'è un terzo soggetto, che in Kerberos si chiama domain controller e in astratto **identity provider**, gestore dell'identità digitale. Quando l'autenticazione passa per un IdP si parla di **autenticazione centralizzata** (*DI-06 @ 00:04:41*). Il service provider in alcune tassonomie si chiama **relying party**, nel regolamento eIDAS "parte facente affidamento sulla certificazione": si fida del terzo soggetto, l'IdP (*DI-06 @ 00:05:11*).

I due motivi per cui esiste l'IdP:

1. **Un'identità, molti servizi.** L'identity proofing si fa una volta presso l'IdP e quell'identità si riusa presso service provider diversi, senza registrarsi ogni volta. Senza IdP ogni service provider dovrebbe acquisire, con il proprio identity proofing, e conservare un'identità: il negozio di pizza online e quello di giocattoli chiedono entrambi dati personali, email, carta di credito (*DI-06 @ 00:09:13-00:10:33*). In azienda è il vantaggio di Kerberos: onboarding una volta sola e login da qualunque computer, anche da un "muletto" (*DI-06 @ 00:11:05*).
2. **Trasferimento delle responsabilità.** Il service provider si toglie le responsabilità legali di protezione dei dati e quelle di cybersicurezza di detenere le identità dei clienti; può anche non memorizzare chi sei, salvo i dati minimi richiesti per legge (per esempio per rivalersi in caso di problemi su una transazione), e il GDPR gli chiede proprio di non memorizzare più del necessario. Non deve pagare piattaforme di onboarding e identity proofing (*DI-06 @ 00:11:39-00:13:10*).

**Il flusso** (*DI-06 @ 00:13:10-00:15:59*): scegli la pizza (condimento, cottura, "orlo alto, orlo basso"), al pagamento il service provider ti rimanda alla pagina dell'IdP ("se questo vi ricorda SPID siamo esattamente in questo contesto, ma non è solo di SPID"); l'IdP presenta le challenge di autenticazione adeguate al **livello di garanzia** richiesto dal service provider (per una transazione economica almeno due fattori). Il service provider non deve mettere in piedi OTP, token o letture biometriche: fa l'*offload* di tutto e deve solo costruire "il piedino informatico" per dialogare con l'IdP. Dietro c'è uno scambio di messaggi firmati digitalmente e certificati. Il service provider non deve più fidarsi di te (email falsa, carta falsa, indirizzo falso) ma dell'IdP; se c'è un problema si rifà sull'IdP, che a sua volta si rifà su di te.

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 5 (autenticazione centralizzata)*

- **L'IdP come RA e VA.** Per analogia con la PKI, l'IdP fa da registration authority (identity proofing iniziale) e da validation authority verso i service provider. Il service provider dice "io non so chi tu sei, ma mi informo presso l'IdP"; l'utente viene reindirizzato al sito dell'IdP, che gli presenta le challenge a uno, due o tre fattori e, solo in caso di esito positivo, risponde con un messaggio tecnico contenente i dati richiesti (email, codice fiscale, eventualmente un metodo di pagamento). (Teams 6 @ 1:42:59-1:45:48)
- **A chi conviene.** Il venditore di pizza o di lacci da scarpe "di mestiere non identifica né autentica": se è obbligato (dalla normativa o dai clienti che non si fidano senza 2FA) lo fa con la spesa minima, e "quando spendi il meno possibile e non capisci quello che stai facendo" ti cabli dentro qualcosa di vulnerabile, oltre a diventare un bersaglio per furti di credenziali in massa. I grandi fornitori offrono invece decine di modalità di autenticazione, OTP su più dispositivi, authenticator, token NFC, il tutto protetto da TLS. (Teams 6 @ 1:45:48-1:51:27)
- **Trasferimento del rischio.** In alcuni contesti normativi con la complessità tecnologica passa all'IdP anche il rischio: SPID impone agli identity provider di dotarsi di un'assicurazione cyber, e nell'analisi del rischio dei service provider il rischio di identificare o autenticare male un cliente viene quasi sempre trasferito all'IdP ("me la fattura la paghi te"). Rimando alla sicurezza amministrativa della guida Cybersecurity. (Teams 6 @ 1:51:27-1:53:38)

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 5 (autenticazione centralizzata)*

- **Modalità di identity proofing dell'IdP.** Identificazione video con avatar, colloquio in tempo reale con una persona, colloquio preregistrato poi convalidato da una persona, un avatar o un'intelligenza artificiale, secondo il profilo di rischio dell'IdP. (Teams 7 @ 0:01:01-0:01:52)
- **Dove sta l'identità.** Il dato che rappresenta l'identità risiede presso l'IdP; una parte può stare nel Secure Element dello smartphone dell'utente; nella firma remota tutto sta nelle componenti sicure dell'IdP. (Teams 7 @ 0:01:52-0:02:38)
- **Esito negativo e sessione.** Se l'IdP non è convinto, manda un responso negativo e il service provider decide se negare il servizio o reindirizzare alla parte non autenticata (utente non pagante, visitatore). Se l'esito è positivo, il service provider "stacca" una sessione autenticata finché non scade un timeout o un token, l'utente fa logoff o smette di mandare l'heartbeat. Non è l'utente a dire chi è: è l'IdP a dire "è Mario Rossi, nato a Cagliari nell'87". (Teams 7 @ 0:03:48-0:06:08)

## 6. Single sign-on

*DI-06 @ 00:06:16-00:09:13*

Il **single sign-on** (SSO) va di pari passo con l'autenticazione centralizzata ma è un concetto diverso: riguarda solo meccanicamente l'assenza di ulteriori autenticazioni quando si passa da un sito a un altro. Può derivare dal fatto che il secondo service provider si fida dell'autenticazione fatta sul primo (ti autentichi su Xbox e su Outlook sei già dentro) oppure dal fatto che più service provider si fidano dello stesso IdP. "Autenticazione centralizzata non vuol dire single sign-on": in un contesto centralizzato il secondo service provider può dirti "chi ti conosce?" e farti riautenticare presso lo stesso IdP (*DI-06 @ 00:07:21-00:08:27*).

Esempio: con SPID e CIE la normativa nazionale prevede che **non ci sia single sign-on**. Se ti autentichi all'INPS con SPID e poi vai sul sito del comune per uno stato di famiglia, il comune ti fa riautenticare presso l'identity provider (*DI-06 @ 00:08:27-00:09:13*).

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 6 (single sign-on)*

- **Precisazione su SPID e CIE.** Nel 2026 il docente dice che in SPID e CIE il single sign-on è escluso *by design* "a partire dal livello di autenticazione due in su". (Teams 7 @ 0:15:13)
- **Come funziona.** I token di autenticazione della sessione (OAuth, OIDC o SAML) vengono "rispesi" presso altri siti che si fidano l'uno dell'altro, tipicamente servizi della stessa azienda: è "una specie di identità federata" in cui sono i service provider a parlarsi fra loro. (Teams 7 @ 0:15:22-0:16:35)
- **Usabilità contro superficie d'attacco.** L'SSO riduce la "fatica da login", ma è anche un punto d'attacco: compromettere l'autenticazione sul sito A, magari più facile, dà accesso al sito B senza autenticarsi, un **movimento laterale**. Se i siti appartengono ad aziende diverse c'è anche un problema di ripartizione del rischio e delle responsabilità. L'SSO permette inoltre di **collegare** (*linking*) account che vivrebbero separati, e una volta collegati è difficile separarli. (Teams 7 @ 0:16:44-0:18:26)

## 7. Identità federata e fornitori di attributi

*DI-06 @ 00:15:59*

L'autenticazione centralizzata diventa **identità federata** quando vale almeno una di due condizioni (*DI-06 @ 00:15:59-00:17:01*):

1. i service provider che si affidano a un unico IdP sono così numerosi ed eterogenei da dover instaurare un forte legame di trust con lui; più crescono, più cresce la superficie d'attacco, perché gli attacchi possono arrivare anche dai service provider e, viceversa, i service provider devono proteggersi da un IdP compromesso. Nasce una federazione con accordi e convenzioni, se del caso pubbliche;
2. gli IdP di riferimento sono **più d'uno**: "autenticati con Google, con Amazon, con Twitter", Facebook, LinkedIn, Microsoft, PayPal, Apple. Il negozio di pizza accetta queste identità perché come minimo l'utente ha dato loro un'email verificata e spesso una carta di credito verificata.

**Slide "Federated identity"** (*DI-06 @ 00:17:52*, *00:19:52*). Testo: "Federated identity refers to contexts with the involvement of *either* multiple heterogeneous **RP**s (e.g. using different authentication technologies, or within multiple jurisdictions/countries/policies) *and* multiple **IdP**s: users/clients opt in an IdP of choice to authenticate to multiple RPs." (Nella slide "wsers", refuso per "users".) Sotto: "The RPs don't need to store any personal data of data subjects they authenticate, for any longer than they need (e.g. for GDPR compliance), as recurring users shall re-authenticate to them via their IdPs, providing **fresh** and **authentic** identification attributes that the SP may trust. IdPs may be legal subjects with responsibility to identify-proof natural or legal persons." A destra i pulsanti "Entra con SPID" (con l'elenco degli IdP: InfoCamere, Poste ID, Namirial ID, TeamSystem ID, SpidItalia, TIM id, Aruba ID, Sielte id, Intesi Group, InfoCert ID, Lepida, EtnaID) ed "Entra con CIE" (logo CieID).

> **Nota aggiunta:** la slide scrive "*either* ... *and*": dal parlato (due condizioni alternative) il senso è "o ... o".

**SPID e CIE** (*DI-06 @ 00:18:32-00:19:40*). Si parla di federazione CIE-SPID perché i due schemi parlano due linguaggi comuni, con piccole differenze tecniche. SPID oggi ha **12 identity provider**, tutti privati salvo Poste e **Lepida** (società in house della Regione Emilia-Romagna), parzialmente pubbliche. CIE ha un solo identity provider, il **Ministero dell'Interno**. In Italia le identità CIE e SPID sono equiparate: tecnicamente due federazioni, di fatto una.

**Slide "Identity federation and its providers"** (*DI-06 @ 00:20:03*). Schema: *SP = RP*, *User*, *IdP*, "trust relationship", e una freccia rosa "electronic attestation of attributes (EAA)" dall'IdP agli SP. Testo: "There may be several different IdPs, RPs / SPs, EAAPs / AAs in a federation, a key feature of which is how they set up to mutually trust each other. Other forms of non-identification attributes exist, usually provided in the form of electronic attestations of attributes (**EEA**) by additional subjects called EAA providers (**EAAP**s) = attribute authorities (**AA**s)." In basso un diagramma a tre sistemi: *System A* (Attribute Requester/SP), *System B* (Attribute Authority/IdP for System A, Attribute Requester/SP to System C), *System C* (Third-party IdP/Attribute Authority), con i passi 1 "user authenticates, assertion passed", 2 "assertion passed", 3 "original attribute query", 4 "proxied attribute query", 5 "returns response", 6 "returns response".

Nella federazione possono esserci anche le **attribute authority**: in SAML e OpenID si chiamano così, in italiano "gestori di attributi", nella tassonomia eIDAS **fornitori di attestazioni elettroniche di attributo**, il nome che il docente userà perché oggi il più diffuso (*DI-06 @ 00:20:11-00:20:42*).

> **Nota aggiunta:** la slide usa sia "EAA" sia "EEA" per la stessa cosa; la sigla corretta in eIDAS 2 è EAA (*electronic attestation of attributes*).

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 7 (identità federata)*

- **"Centralizzazione decentralizzata".** L'identità federata è un'identità centralizzata in cui la centralizzazione è distribuita: molti relying party eterogenei, oppure più gestori, "tutti tipicamente equivalenti", paritetici almeno amministrativamente. Te ne accorgi quando il sito ti chiede di scegliere fra Apple ID, PayPal, Microsoft, GitHub, Meta, X, Amazon, Google: cliccando scegli un IdP della federazione, e il service provider di fatto li accetta tutti perché il linguaggio tecnico è omogeneo. (Teams 7 @ 0:08:30-0:11:17)
- **Federazione aziendale globale.** Dipendenti identificati presso le sedi in Corea, Stati Uniti, Francia devono potersi autenticare a tutti i servizi aziendali ovunque: i service provider sono i servizi aziendali, gli IdP le sedi che registrano i dipendenti. (Teams 7 @ 0:11:17-0:12:07)
- **SPID in numeri, 2026.** 12 identity provider, quasi tutte le PA federate, "intorno ai 250" soggetti privati. Scegliendo "Entra con CIE" non si sceglie un IdP (è il Ministero dell'Interno); con "Entra con SPID" si apre il menu a tendina. (Teams 7 @ 0:13:10-0:14:58)

## 8. Deleghe di identità

*DI-06 @ 00:20:42*

Un altro concetto fondamentale è la **delega**. Ci si presenta a un servizio online come persona fisica o come persona giuridica, ma in entrambi i casi chi si autentica è sempre una persona fisica, tipicamente un rappresentante (*DI-06 @ 00:20:42-00:21:16*).

**Slide "Identity delegation"** (*DI-06 @ 00:20:58*, costruita progressivamente fino a *00:30:59*). Otto righe, ciascuna con un'icona del soggetto a sinistra, una freccia colorata e l'identità presentata a destra:

| Riga | Testo | Colore |
|---|---|---|
| 1 | *Bob Bingleby*, a physical person | rosso |
| 2 | *Acme s.r.l.*, a legal person | blu |
| 3 | *the www.acme.com website*, an IT system | verde |
| 4 | *Bob Bingleby on behalf of Mario Rossi*, a physical person on behalf of another physical person | rosso |
| 5 | *Bog Bingleby on behalf of Acme s.r.l.*, a physical person on behalf of a legal person | blu |
| 6 | *the www.acme.com website on behalf of Mario Rossi*, an IT system on behalf of a natural person | rosso |
| 7 | *account.google.com service on behalf of acme.com*, an IT system on behalf of another IT system | verde |

(La quinta riga riporta "Bog Bingleby", refuso della slide per "Bob". Le icone: un passaporto con chiave per le persone fisiche, un documento con chiave per la persona giuridica, una chiave per i sistemi; nelle righe in delega l'icona del delegato è sovrapposta a quella del delegante.)

**Delega contro impersonificazione** (*DI-06 @ 00:21:49-00:27:17*). Nei casi pratici Bob Bingleby è delegato di Mario Rossi (delegante): si autentica con la **propria** identità e i **propri** fattori (la sua password, il suo token, la sua app, "mettendoci la faccia" sua), ma il sistema, sapendo che ha una delega valida, lo fa operare come Mario Rossi: per esempio gli mostra la dichiarazione precompilata, l'indirizzo e il codice fiscale di Mario Rossi, sapendo che dietro c'è Bob. Il caso "mio nonno mi ha dato password SPID e PIN del telefono, fai tu" **non è una delega ma un'impersonificazione**, vietata dalla legge (anche eIDAS vieta di cedere le credenziali dell'identità digitale nazionale): il sistema vede Mario Rossi e non sa che dietro c'è Bob, tecnicamente è un furto di identità. Gli effetti per il servizio sono gli stessi; la differenza è che solo nella delega il sistema sa chi opera davvero.

I casi d'uso previsti dalla legge: CAF, commercialista, avvocato, rappresentante legale, tutore, genitore per il figlio minore, con delega ai sensi del **DPR 445/2000** (*DI-06 @ 00:25:42*). Per la persona giuridica: Bob, membro del consiglio di amministrazione o rappresentante legale, entra con le proprie credenziali e il sistema lo riconosce come ACME S.r.l. sapendo chi è. Il caso dell'azienda che si autentica con una credenziale "dell'azienda" (seconda riga) "non si è mai visto", perché una persona giuridica non esiste materialmente (*DI-06 @ 00:26:46-00:27:48*).

**Deleghe a sistemi tecnici** (*DI-06 @ 00:27:48-00:30:59*). Si può delegare un sistema informatico a fare accessi per proprio conto: oggi un'intelligenza artificiale agentica, con "tantissimi rischi di tipo legale ed etico", che sa di operare per conto di Mario Rossi. Oppure un sistema opera per conto di un altro sistema: il sito di un giornale nella DMZ chiede le notizie a un back-end che a sua volta interroga il database sulla rete interna "presentandosi con le credenziali del sito web"; con le credenziali di un sito non autenticato il database restituisce solo le prime cinque righe e una foto, con quelle di un utente pagante tutto l'articolo.

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 8 (deleghe): i tre soggetti senza delega*

- **Un concetto "sfuggevole".** "Delegation" in informatica indica due concetti simili ma diversi (la delega amministrativa e il *proxying* di Active Directory, sezione 4): senza chiarire cosa si intende si rischia di non capirsi, come quando i professionisti di sicurezza parlano di IA. (Teams 7 @ 0:43:07-0:44:19)
- **Le prime tre righe non sono deleghe.** Persona fisica, persona giuridica, sistema informatico: tre soggetti con tre chiavi private diverse (passaporto, documento in cassaforte anche virtuale, chiave del sistema). L'impiegato che ordina "99 bottiglie di Coca Zero e 100 bustine di arachidi" con l'account `acquisti@acme` si presenta come ACME S.r.l.: chi riceve l'ordine non sa quale dipendente l'ha fatto e non gli interessa. Il sito che si autentica a un altro sito per un feed RSS è riconosciuto per dominio: è il tipo di autenticazione di TLS, fra client web e server web, anche se dietro ci sono la "vicina di casa" e un'azienda coreana. (Teams 7 @ 0:51:45-0:58:56)

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 8 (deleghe): accountability e tracciamento*

- **Accountability.** Le PA devono sapere a chi erogano un servizio: chi paga una multa per un altro deve presentare una delega ai sensi del DPR 445/2000 con copia del documento del delegante. Online il sistema deve tracciare **entrambe** le identità: che si è loggato Bob (il delegato) e che operava per Mario Rossi (il delegante). Se Bob si rivela un attore della minaccia, anche munito di delega, il gestore deve poter dimostrare all'autorità giudiziaria chi si è materialmente collegato. (Teams 8 @ 0:03:06-0:07:31)
- **Lato usabilità.** Riconosciuta la delega, il portale mostra l'interfaccia e i dati di Mario Rossi, non di Bob: sui portali INPS e Agenzia delle Entrate viene chiesto se si opera per sé o per altri (minori del nucleo familiare, assistiti del commercialista, tutele, CAF). Concettualmente è lo stesso meccanismo del proxying di Active Directory, visto dal lato amministrativo. Il docente si è occupato, quando era all'Istituto Poligrafico e Zecca dello Stato, del sistema di gestione delle deleghe per SPID e CIE. (Teams 8 @ 0:07:31-0:10:58)
- **Lato delegante.** Senza un sistema di deleghe l'unica alternativa per Mario Rossi è consegnare le proprie credenziali: si perde l'accountability e il controllo su ciò che Bob fa. Con la delega il delegante (o i controller dell'azienda) può verificare che il delegato abbia fatto solo ciò per cui era delegato. Gli attaccanti che rubano un account, se vogliono **persistenza**, cambiano subito password e metodi di recupero; se basta un'azione sola (un versamento su un conto bitcoin) non perdono tempo. (Teams 8 @ 0:10:58-0:16:26)
- **Sistemi delegati.** Un sistema con delega di una persona si logga in automatico (per esempio da un indirizzo no-reply) e il servizio legge la delega; il caso sistema-per-sistema comprende anche le deleghe di Active Directory, "che sono però un sistema di doppie deleghe". (Teams 8 @ 0:16:26-0:17:27)

## 9. Identità autosovrana (SSI)

*DI-06 @ 00:31:11*

L'**identità autosovrana** (*self-sovereign identity*, SSI; al docente non piace tradurla) nasce per risolvere due problemi. Il primo è di **data governance**: intorno al 2014-2016, dopo problemi di sicurezza che misero offline alcuni identity provider nazionali, alcuni dissero di non volere un'identità "di Stato" né credenziali custodite da un terzo, e di voler riprendere il controllo della propria identità. Il docente lo lega a una "narrazione" geopolitica di cui non c'è tempo di parlare (temi di data governance e cyber intelligence dell'altro corso: guida Cybersecurity) (*DI-06 @ 00:31:11-00:32:56*).

**Slide "Self-Sovereign Identity (SSI)"** (*DI-06 @ 00:31:10*, *00:40:57*). Testo: "SSI was born to **disintermediate** credentials' **verifiers** from credentials' **issuers**, putting the user (credentials' **holder**) at the centre and mitigating privacy risks of third parties colluding to profile users themselves." Schema: *Issuer* (Bosch, Bundesdruckerei, Bank) → *Holder* (uno smartphone con quattro carte) ↔ *Verifier* (IAM Service, eCommerce Service, Other Service) con le frecce "Requests" e "Presents Proof"; in basso "Verifies" verso una *Decentralized Network*.

L'utente è l'**holder** delle proprie credenziali, che però devono essere certificate da terzi, gli **issuer** pubblici e privati (nell'esempio un'azienda tedesca, un ente pubblico tedesco, una banca), che forniscono pezzo per pezzo credenziali, identità e attributi. L'holder li colleziona in un posto sotto il suo controllo esclusivo, oggi il **wallet**, e presenta solo i pezzi richiesti ai **verificatori**: per un acquisto online indirizzo e dati di pagamento, nient'altro (*DI-06 @ 00:32:56-00:34:35*).

Ma per verificare, il verificatore deve tipicamente confrontarsi con chi ha emesso i dati: "altrimenti è il regno di Eva, di Carl" e di tutti gli attaccanti nel mezzo. Cambia il **modello di presentazione**, non la necessità di una verifica a monte sugli issuer (*DI-06 @ 00:34:35-00:35:09*).

**Slide "Traditional vs SSI"** (*DI-06 @ 00:36:06*, *00:40:58*). A sinistra quattro utenti collegati a un'unica sfera piena di servizi (LinkedIn, YouTube, Work, Twitter, Xing, Facebook, gaming, smart home, bank, med); a destra un solo utente al centro collegato direttamente a ciascun servizio.

Nel modello tradizionale l'utente dipende dall'IdP: se l'IdP è indisponibile, attaccato, fallisce, o se IdP e utente non sono più d'accordo per motivi politici, culturali, etici, "c'è una guerra", l'utente resta senza identità (*DI-06 @ 00:35:09-00:36:27*).

**L'opinione del docente** (*DI-06 @ 00:36:27-00:41:01*): "lavorando da qualche anno in questo settore", l'unico problema davvero risolto dal modello SSI è lo **scenario offline**: l'utente senza connessione ("in una grotta", al piano -2 di un negozio) ha già nel wallet gli attributi e può presentarli anche se l'issuer è irraggiungibile o sotto DoS. Il verificatore magari non può verificarli subito e può concedere il servizio provvisoriamente, differire la verifica o spedire a casa la lampada appena verificato. Altro caso: due wallet che si scambiano via NFC un attributo emesso da un issuer (un contatto). In tutti gli altri casi il verificatore deve comunque verificare con l'issuer (data di nascita, patente straniera presso il ministero dei trasporti, carta di credito: come il POS che rifiuta la transazione perché non riesce a verificare il certificato X.509), quindi "non è che se hai il wallet ti stacchi dalla realtà e diventi un autarca": l'identità, o l'attributo, te la deve sempre fornire qualcuno autorizzato per legge, normativa, contratto o convenzione. È "una mia opinione personale".

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 9 (SSI)*

- **Il "prurito".** Rispondendo a una domanda di uno studente, il docente riformula il problema con i termini della minaccia cyber di Cybersecurity: il gestore dell'identità ha certamente la **capacità** e l'**opportunità** di usare le nostre credenziali; manca solo l'**intento**. Per i privati sarebbe contro il loro modello di business (vendono fiducia) e il danno reputazionale sarebbe enorme; in alcuni Stati, "per fortuna non in Europa", il governo può obbligare le aziende a consegnare i dati. Non spetta a lui dire se possa accadere, ma porsi la domanda serve a gestire il rischio. (Teams 8 @ 0:17:27-0:23:28)
- **Buzzword.** L'SSI è stata una buzzword per un paio d'anni, presto abbinata alla blockchain, con improvvisi "guru evangelist della blockchain autosovrana"; critica a parte, è una soluzione tecnicamente valida, tanto che dal 2020 è alla base del ridisegno europeo dell'identità digitale. Oggi non si dice più "autosovrana" ma "basata su wallet", "perché la sovranità comunque ci sta da qualche parte". (Teams 8 @ 0:23:28-0:24:45, 0:52:33-0:52:48)
- **Il diagramma è "commerciale".** Mettere il cittadino "al centro" di qualcosa di profondamente tecnico è, da tecnico, sbagliato, ma efficace nel mostrare il cambio di paradigma. (Teams 8 @ 0:24:52-0:25:24)
- **Non tutto il vecchio è da buttare.** Nell'identità centralizzata la relazione di fiducia SP-IdP non passa (apparentemente) per l'utente, e nei contesti privati l'utente non sa cosa l'IdP ha svelato. Ma in SAML richiesta e risposta transitano per lo *user agent* (il browser dello smartphone) e, volendo, si possono ispezionare: SAML "è stato pensato proprio per questo", per essere *privacy preserving*. Il wallet europeo parla sotto OpenID Connect. (Teams 8 @ 0:25:57-0:29:29)
- **L'esempio della CILA.** L'architetto che apre una CILA per conto della proprietaria presenta in un'unica presentazione verificabile quattro credenziali: identità (PID), iscrizione all'ordine, delega della proprietaria, titolo di possesso dell'immobile; il comune verifica. Un'altra: comprare un superalcolico online (maggiore età, indirizzo). (Teams 8 @ 0:31:26-0:33:06, 0:36:06-0:37:13)
- **Holder.** Il termine "holder" si usa anche per i certificati di attributo X.509 visti nel corso. L'holder è il dispositivo (tablet, smartphone) con il software wallet, che richiede gli attributi agli issuer anche in automatico quando servono. (Teams 8 @ 0:29:42-0:30:28)

## 10. Identificazione elettronica e biometria

*DI-06 @ 00:41:01-00:44:38*

Il docente si accorge di non aver proiettato la versione giusta delle slide e recupera una slide mancante.

**Slide "Electronic Identification"** (*DI-06 @ 00:43:09*, *00:44:09*). Testo: "All our online activities are effectively mediated by digital representations of ourselves: one or more *digital personæ* which represent our unique *digital footprint* in the cyberspace. A digital identity may be just a (username, password) couple, or it can be a complex process including means, schemes and a legal framework such that third entities can digitally trust that a real natural (or legal) person is "behind" that persona and that *is* whoever he/she/it asserts oneself to be." Immagini di riconoscimento facciale con punti di repere e triangolazioni.

L'identità digitale è la corrispondenza fra una persona fisica e i suoi dati, che spesso vanno confrontati con dati biometrici (impronta digitale, caratteristiche facciali). Perché l'identità abbia effetti giuridici, operativi, amministrativi, non basta la conoscenza di username e password: serve un legame più forte fra l'account e la persona, da cui più fattori, anche biometrici. "Come al solito è un discorso di digital trust" (*DI-06 @ 00:42:51-00:44:03*).

## 11. SSI e privacy: credenziali e presentazioni verificabili

*DI-06 @ 00:44:03*

**Slide "SSI and privacy preservation"** (*DI-06 @ 00:40:59*, *00:48:57*). Fonte in alto: `https://speakerdeck.com/yamdan/linked-data-based-verifiable-credentials-with-selective-disclosure-unlinkability-and-range-proofs`. Schema: *Issuer* → **Verifiable Credential (VC)** (riquadro "name: John Smith; birthdate: 1980-01-01; (issuer's signature)") → *Holder* → **Verifiable Presentation (VP)** (tre credenziali) → *Verifier*. Testo:

> With SSI, new security, privacy and social-inclusion concerns arise and need be solved in order for such a paradigm to be globally adopted (e.g. with EUDI Wallet pursuant to **eIDAS2**):
> - **Selective disclosure**: Holder decides which subset of his/her personal data to disclose to a verifier for each verifiable presentation (**VP**) of the same verifiable credential (**VC**).
> - **Unlinkability**: Holder must not be identified by VP presented to different verifiers (including the case whereby the VC issuer colludes with 1+ verifiers).
> - **Pseudonymicity**: Decentralized identifiers (**DID**s) rather than unique ones (**UID**s) to avoid the holder's anonymous uniqueness to be inferred in case of verifiers'/VPs' aggregation.

(Nella slide gli incisi dopo i nomi delle tre proprietà sono introdotti da trattini lunghi, resi qui con i due punti.)

Uno o più issuer emettono **credenziali verificabili** all'holder, che in un secondo momento le presenta come **presentazione verificabile** al verificatore. "Verificabili" perché l'holder deve poter verificare le credenziali quando le riceve e il verifier la presentazione, appoggiandosi a un controllo in capo all'issuer (*DI-06 @ 00:44:38-00:45:41*).

**Il problema privacy del modello centralizzato** (*DI-06 @ 00:45:41-00:47:30*): più service provider possono colludere, in violazione del GDPR, aggregando i dati per profilare l'utente (chi ti ha dato un bonus e chi ti ha venduto il bene); oppure il service provider può essere d'accordo con l'IdP e ricevere più dati del necessario. In SPID e CIE al massimo l'IdP avvisa l'utente ("sto per mandare ad ACME S.r.l. nome, cognome, email, telefono") e l'utente può rifiutare.

Nel modello a wallet è l'holder a formare la presentazione con i soli dati necessari, la **selective disclosure**; può inviare dati in forma anonima o **pseudonimizzata**, usando **identificatori decentralizzati** (DID) diversi per ogni verificatore e perfino per ogni transazione con lo stesso verificatore, così che nessuno possa tracciarlo. Con un IdP sarebbe ancora tecnicamente possibile tracciare, e l'holder non potrebbe accorgersene perché il flusso va dall'IdP al verifier; "c'è chi obietta" che in SAML tutti i flussi passano dal computer dell'utente, ma non esistono standard tecnici che lo sfruttino (*DI-06 @ 00:47:30-00:49:50*).

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 11 (VC, VP, privacy)*

- **Sigilli dell'issuer.** In pratica le credenziali verificabili sono messaggi protetti dal **sigillo elettronico** dell'issuer: holder e verificatori convalidandolo verificano autenticità (provengono dall'issuer titolato per legge o competenza) e integrità (nessuno, "nemmeno l'holder" che potrebbe averne interesse, le ha modificate). (Teams 8 @ 0:33:06-0:34:51)
- **Tutto passa per l'holder.** Il modello tecnico non consente a un issuer di dare credenziali a un verifier senza passare dall'holder; esistono protocolli che impediscono a un verificatore di verificare una credenziale se non ha prima accertato che provenga dall'holder a cui si riferisce. (Teams 8 @ 0:34:59-0:35:59)
- **VC contro VP.** Una VP può riunire più VC e consente al verificatore di leggere solo ciò che deve leggere. (Teams 8 @ 0:36:06-0:37:51)
- **Unlinkability.** Contro la collusione fra IdP e service provider, poiché tutto passa dall'holder, questi può anonimizzare ogni presentazione così che verificatori distinti non possano collegare le attività; non sempre servono dati personali (esempio: il voto elettronico, dove il doppio voto si impedisce in altri modi). Sulla pseudonimicità "preferisco non parlare". (Teams 8 @ 0:37:57-0:40:30)

> **Correzione:** a voce il docente dice che nella presentazione verificabile i dati sono "tipicamente cifrati" (Teams 8 @ 0:37:24; anche DI-06 @ 00:57:51, dove si corregge subito). Nella selective disclosure i dati non svelati non sono cifrati: nel token firmato compaiono solo i loro digest, e il docente stesso lo precisa più avanti ("sono sostituiti da un hash, in realtà non sono cifrati", Teams 8 @ 1:35:28).

## 12. Autenticazione e autorizzazione: l'esempio della fatturazione elettronica

*DI-06 @ 00:49:17*

**Slide "Authentication vs Authorisation"** (*DI-06 @ 00:48:56*, *00:49:28*). Legenda: freccia blu "Authentication flux", freccia rosa "Authorization flux". Al centro un'area tratteggiata con cloud storage e posta in cloud, collegati da anelli rosa; a sinistra un'app di fatturazione (icona con il simbolo dell'euro) e una finestra di consenso Google ("Test Authentication App would like to: Know your basic profile info and list of people in your circles; View your email address", pulsanti *Deny* e *Allow*); a destra l'IdP e l'utente. Riquadro: "inter-company trust implemented as implicit SSO among services from the same SaaS provider".

**Slide "Authentication vs Authorisation example"** (*DI-06 @ 00:51:54*). Le stesse frecce con Google Drive e Gmail su Google Cloud, il logo IdP e l'utente; a sinistra il fumetto "Everyone needs bad puns!" con il flusso: scegli il provider di posta (fleaMail, Outlost, Yafool!, LOL), "Already logged in?" no → *Sign in*, sì → "Do you want to give TerriblePunOfTheDay access to your contacts?" *Deny / Allow* → "Thank you! We'll send reminders to everyone you know every day for all eternity! You're the best friend ever!". Testo: "In this scenario the customer using an e-invoicing SaaS, also uses IdP, e-mail and e-drive SaaS's from one cloud service provider (**CSP**), which is accidentally the same CSP used by the e-invoicing SaaS. The customer thus **authenticates** *once only*, while rest of the workflow is handled via just **authorization** tokens."

L'esempio (*DI-06 @ 00:49:50-00:52:18*): un'azienda usa un servizio di fatturazione elettronica in cloud (magari di una piccola impresa locale) che usa la posta aziendale per inviare le fatture e ricevere gli ordini e il cloud storage per salvarli; posta e storage sono legati a un account aziendale presso un fornitore terzo con il suo IdP (`accounts.google.com`). Al servizio di fatturazione servono quelle che nel gergo cloud si chiamano **API key**, cioè un'**autorizzazione** a operare sugli account di posta e storage: legge la posta, trasforma gli ordini in fatture, le invia, le archivia. L'autenticazione c'è, anzi probabilmente due volte: una al servizio di posta e storage, una all'IdP allo scopo di **concedere la delega** al servizio di fatturazione. I due flussi sono diversi e "di solito parlano linguaggi differenti".

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 12 (autenticazione e autorizzazione)*

- **Il grant.** Durante la configurazione il software di fatturazione chiede, una tantum, il consenso: leggere e inviare posta, creare cartelle e scrivere in alcune cartelle del drive. Cliccando "Autorizza" si concede un **grant** (termine di OAuth), in pratica un **token al portatore** firmato digitalmente da Google Cloud, con date di inizio e fine validità, che l'applicazione "rispende" presso Gmail e Drive senza riautenticarsi e senza conoscere la password dell'account aziendale. Sono due flussi logicamente separati che richiedono controlli di sicurezza separati. (Teams 7 @ 0:18:26-0:24:27)
- **Libertà di scelta.** Il fornitore di fatturazione non ha né interesse né competenza per offrire posta e archiviazione: lascia al cliente scegliere Google, Amazon, Dropbox o altri. (Teams 7 @ 0:19:13-0:20:46)

## 13. SAML

*DI-06 @ 00:52:18*

Per l'autenticazione il linguaggio di riferimento per anni è stato **SAML**, *Security Assertion Markup Language*. Dietro SPID e CIE, "probabilmente nel 90% dei service provider" c'è ancora un flusso SAML, perché SPID (2014-2016) e CIE (qualche anno dopo) sono nati quando SAML era lo stato dell'arte; AgID ha pubblicato "da circa tre anni" le linee guida OpenID Connect (alle quali il docente ha partecipato), ma i service provider hanno **inerzia tecnologica**. È un linguaggio di richieste e risposte di autenticazione (*DI-06 @ 00:52:18-00:53:40*).

**Slide "Security Assertion Markup Language (SAML)"** (*DI-06 @ 00:53:20*, *00:54:44*). Tre attori: *Service Provider*, *User Agent*, *Identity Provider*. Passi: (1) *Request* target resource (lo user agent al SP), (Discover the IdP); (2) *Redirect* to SSO service; (3) *Request* SSO service (allo IdP), (Identify the user); (4) *Respond* with XHTML form; (5) *Request* assertion consumer service (al SP); (6) *Respond* with requested resource. Riquadri: "SAML Request (via GET or POST)" con `<samlp:AuthnRequest>.........</...>`; "SAML Response (with 1+ Assertions)":

```xml
<samlp:Response>
 <saml:Assertion>
   <saml:AuthnStatement>...</...>
   <saml:AttributeStatement>
   <saml:AttributeStatement>
     <saml:Attribute>IdAttribute1</...>
     <saml:Attribute>IdAttribute2</...>
     ⋮
   </saml:AttributeStatement>
 </saml:Assertion>
 <saml:Assertion>...</saml:Assertion>
</samlp:Response>
```

SAML è basato su **XML**, quindi i messaggi firmati sono **firme XML** (XAdES, viste nella lezione precedente) (*DI-06 @ 00:54:18*).

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 13 (SAML)*

- **Dove si usa.** Nel web, anche per web app e applicazioni che usano internamente i protocolli del browser, l'autenticazione è "in gran parte" SAML, che rappresenta anche scenari di identità federata molto articolati; la maggior parte delle implementazioni SPID e CIE è SAML, con cui SPID è nato nel 2014. (Teams 7 @ 0:33:43-0:34:56)
- **Firme e federazione.** Richieste e risposte (con tutti gli attributi identificativi) sono messaggi XML firmati, anzi **sigillati elettronicamente** perché SP e IdP sono persone giuridiche: l'SP si fida che l'IdP faccia parte della federazione, e l'IdP, prima di dare dati personali, verifica che l'*authentication request* provenga davvero dall'SP. Le chiavi pubbliche sono scambiate su canale fidato al momento della federazione. Il docente precisa che la firma di richiesta e risposta "è una caratteristica facoltativa" nello standard. (Teams 7 @ 0:34:56-0:37:11)

> **Correzione:** in Teams 7 @ 0:33:43 il docente dice che SAML è "nato in seno al W3C". SAML è uno standard **OASIS** (SAML 2.0 del 2005); del W3C sono invece gli standard XML Signature e XML Encryption su cui SAML si appoggia.

## 14. OAuth 2.0

*DI-06 @ 00:53:40*

Per le **autorizzazioni**, cioè le schermate con cui si concede a un servizio cloud l'uso del proprio account Gmail, Microsoft o PayPal, lo standard è **OAuth**, "arrivato alla versione 2.0", oggi stato dell'arte soprattutto online (*DI-06 @ 00:53:40-00:54:18*).

**Slide "Authorisation flows with OAuth 2.0"** (*DI-06 @ 00:53:33*, *00:54:43*). Quattro attori: *Client*, *Resource Owner*, *Authorization Server*, *Resource Server*. Passi: (A) Authorization Request e (B) Authorization Grant fra client e resource owner; (C) Authorization Grant e (D) Access Token fra client e authorization server; (E) Access Token e (F) Protected Resource fra client e resource server. Riquadri:

- "Authorization request (GET)": `GET /endpoint?client_id=...&redirect_uri=...&response_type=...[&scope=...][&state=...]`
- "Access token grant (GET or POST)": `code=ACG & state=... [&...]`
- "**Access token** (JWT, i.e. a *signed* JWT)": "JWT header {claims for JWS validation}; JWT payload {claims for user-ID & JWT scope}; JWT signature {JWS (electronic seal)}"
- "Resource Request (POST or GET)": `Authorization: Bearer AccTknJWT`

**Slide "OAuth 2.0 – Authorization Code Grant"** (*DI-06 @ 00:54:12*, *00:54:42*). Passi: (1) Authorization Request (client → authorization server); (2) Resource Owner Authentication (authorization server ↔ resource owner); (3) Authorization Code Grant; (4) Access Token Request; (5) Access Token Grant; (6) Resource Request; (7) Resource Response (client ↔ resource server). Riquadro: "Authorization request (GET)": `GET /endpoint? ...& response_type=token &... redirect_uri=https://... &...`.

**Slide "OAuth 2.0 – Implicit Grant"** (*DI-06 @ 00:54:52*). Passi: (1) Authorization Request; (2) Resource Owner Authentication; (3) Access Token Grant; (4) Resource Request; (5) Resource Response. Riquadri: "Authorization request (GET)": `GET /endpoint? ...& response_type=code &... redirect_uri=https://... &...`; "Access token grant (GET)": `access_token=AccTknJWT & token_type=Bearer &...`.

Le tre slide scorrono in pochi secondi senza commento specifico: il docente le mostra mentre spiega che OAuth è stato poi esteso all'autenticazione (sezione 15).

> **Correzione:** nelle due slide i valori di `response_type` sono **scambiati**. Secondo RFC 6749 l'Authorization Code Grant usa `response_type=code` (il client riceve un codice e lo scambia con il token al token endpoint, passi 4-5), l'Implicit Grant usa `response_type=token` (il token arriva direttamente nel redirect, senza scambio del codice).

> **Nota aggiunta:** nell'Implicit Grant l'access token viene restituito nel **fragment** dell'URI di redirect (`#access_token=...`), non come parametro di una GET al server. L'Implicit Grant è oggi sconsigliato dalla *OAuth 2.0 Security Best Current Practice* (RFC 9700, 2025) e assente da OAuth 2.1; per le app pubbliche si usa l'Authorization Code Grant con PKCE (RFC 7636). In RFC 6749 l'access token è una stringa opaca; il formato JWT per gli access token è standardizzato a parte (RFC 9068). Il riquadro "Access token" della slide descrive quindi un JWT firmato, scelta comune ma non obbligatoria.

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 14 (OAuth 2.0): contenuto più esteso nel 2026*

- **Che cos'è.** OAuth (il docente prima dice "open authentication", poi si corregge in "open authorization") è il linguaggio di autorizzazione più usato su Internet; "non lo vediamo nel dettaglio perché è materia per sviluppatori professionisti". Ricalca il flusso avanti-indietro dell'autenticazione, con più soggetti. (Teams 7 @ 0:37:16-0:37:54)
- **Profili.** I più usati sono l'**Authorization Code Grant** e l'**Implicit Grant**, "un po' più semplificato", con tre soggetti, in cui viene chiesto un token da rispendere. (Teams 7 @ 0:37:57-0:38:16)
- **OAuth non autentica.** Il token è rilasciato a monte "se c'è stata un'autenticazione", ma il protocollo non se ne occupa: garantisce solo che l'authorization server ha dialogato con il resource owner. Gli authorization token sono **al portatore** e, in un'implementazione sicura, dovrebbero essere JWT cifrati e firmati (le firme JSON della lezione precedente), così che il gestore della risorsa (Gmail, Drive, Dropbox, AWS) possa verificare l'autorizzazione. (Teams 7 @ 0:38:16-0:39:42)
- **Quadro sinottico.** SAML, OpenID Connect e Kerberos sono protocolli di **autenticazione**; OAuth è l'unico di **autorizzazione**. (Teams 7 @ 0:39:42-0:40:10)

> **Nota aggiunta:** in RFC 6749 i ruoli sono quattro: *resource owner* (l'utente), *client* (l'applicazione, qui il software di fatturazione), *authorization server* (rilascia i token dopo aver autenticato il resource owner e ottenuto il consenso), *resource server* (Gmail, Drive). Lo *scope* della richiesta corrisponde ai permessi elencati nella schermata di consenso; il parametro *state* protegge dal CSRF. Un token "al portatore" (*bearer*, RFC 6750) è valido per chiunque lo presenti: per questo deve viaggiare solo su TLS e avere vita breve.

## 15. OpenID Connect e OpenID Federation

*DI-06 @ 00:53:59*

OAuth è stato esteso per occuparsi anche di autenticazione: ne è nato **OpenID Connect** (OIDC), che da anni si sta affermando al posto di SAML. Lo schema è "molto simile" a SAML ma il linguaggio è diverso: SAML è XML con firme XML, OAuth e OIDC usano i **JSON Web Token** (JWT), con sicurezza realizzata da **firme JWS** (*DI-06 @ 00:54:18-00:55:39*). Ad altissimo livello lo schema non è molto diverso; OIDC è "moderno" perché pensato per flussi con dispositivi di autenticazione mobili (SAML lo permette, ma va adattato). Sono passati completamente a OIDC, secondo il docente, Microsoft Office 365, Entra ID (Active Directory in cloud), i login Amazon e PayPal (*DI-06 @ 00:55:39-00:56:15*).

**Slide "OpenID Connect (OIDC)"** (*DI-06 @ 00:54:13*, *00:55:54*). Diagramma: (1) User opens browser; (2) Navigates to web app; (3) Redirected to Azure AD; (4) User enters credentials; (5) User consents to permissions; (6) Issues tokens (access & refresh token); (7) Redirects access tokens to web app; (8) Validates access token; (9) Returns secure page to user. Legenda "Connector Type": linea punteggiata nera *Authentication*, linea punteggiata blu *Token*.

**Slide "OpenID Federation"** (*DI-06 @ 00:56:15*, *00:59:07*). Due *Identity Provider* (A e B), ciascuno con tre *Relying Party* "under management (direct relationship)"; due *Trust Anchor* che "authorize" le rispettive *Intermediate Authority*; frecce "trust" dai relying party ai trust anchor; due riquadri "TRUST CHAIN"; in rosso "relationship established based on trust chains" fra Identity Provider A e Relying Party B-1.

OIDC gestisce anche vere federazioni con molti IdP e molti relying party, sopra un'infrastruttura a chiave pubblica che realizza il tessuto di digital trust. **OpenID Federation** è anche lo schema dietro le implementazioni moderne di SPID e CIE, anche se per inerzia si parla ancora prevalentemente SAML (*DI-06 @ 00:56:15-00:57:20*).

> **Nota aggiunta:** il diagramma OIDC della slide è quello di Microsoft (Azure AD, oggi Entra ID). In OIDC, rispetto a OAuth, l'elemento chiave è l'**ID token**, un JWT firmato dall'IdP (OpenID Provider) con le affermazioni sull'identità dell'utente (`iss`, `sub`, `aud`, `exp`, `nonce`...), distinto dall'access token, che serve ad accedere alle risorse. OpenID Connect Core 1.0 è del 2014. In OpenID Federation la fiducia non si basa su scambi bilaterali di metadati ma su **trust chain** di *entity statement* firmati che risalgono a un *trust anchor* comune, come la catena di certificati di una PKI.

### Integrazione Teams 2026 (lezione 7 2026)

*Sezione 15 (OpenID Connect, OpenID Federation)*

- **OIDC.** Il più recente dei protocolli visti, "un decennio scarso"; aperto, basato come OAuth su token JSON cifrati e/o firmati (JWS). Prende da OAuth gran parte del dialetto e dei meccanismi ma serve all'autenticazione. "Non ve lo spiego" (è una variante più complessa di SAML); nato per integrarsi con OAuth, la combinazione OIDC + OAuth è un buon mix per scenari con flussi sia autenticativi sia autorizzativi come la fatturazione elettronica. (Teams 7 @ 0:39:45-0:41:59)
- **OpenID Federation e università.** La variante per grandi federazioni, "un po' meno standardizzata", è OpenID Federation: grande impulso dalle **università**, che per prime hanno avuto bisogno di federarsi per gli studenti in mobilità ("grande kudos" ai responsabili dell'identità degli atenei). È il protocollo autenticativo di base del wallet europeo. "Non mi sento di dare per il momento dettagli ulteriori". (Teams 7 @ 0:41:59-0:43:07)

> **Nota aggiunta:** OpenID Connect Core 1.0 è stato pubblicato a febbraio 2014: nel 2026 ha circa dodici anni, non "un decennio scarso". Nell'architettura dell'EUDI Wallet i protocolli di rilascio e presentazione sono OpenID for Verifiable Credential Issuance (OID4VCI) e OpenID for Verifiable Presentations (OID4VP), della stessa famiglia OpenID.

## 16. Selective disclosure: SD-JWT e KB-JWT

*DI-06 @ 00:57:20*

Poiché OIDC parla JSON, si possono usare JWT firmati e una serie di standard collegati, fra cui il **Selective Disclosure JWT** (SD-JWT), che permette di svelare ai verificatori solo i dati strettamente necessari (*DI-06 @ 00:57:20-00:57:51*).

**Slide "Selective disclosure – SD-JWT and KB-JWT"** (*DI-06 @ 00:58:08*, *01:03:47*). Testo a sinistra: ""SD-JWT VC" is a data encoding format usable in both VCs and VPs: In a VC, the e-seal over it covers the digests of all presentable personal data (so-called *claims*) which are then appended to it, *unhashed*. Such composited VC is then sent to the holder." Schema: un JWT con **HEADER**, un payload con `"_sd": [ Digest 1, Digest 2, ..., Digest N ], ...` e `public key`, e **SIGNATURE**; tre riquadri `["salt1","name1","value1"]`, `["salt2","name2","value2"]`, `["saltN","nameN","valueN"]` che diventano, via **base64url**, *Disclosure 1*, *Disclosure 2*, *Disclosure N*, e il cui **hash** dà i *Digest* nel payload; una *Key pair* (public key, private key) con "Sign" verso la *Key Binding JWT*. In basso il formato: **SD-JWT** = *Issuer-signed JWT* ~ *Disclosure 1* ~ *Disclosure 2* ~ *Disclosure N* ~ *Key Binding JWT* (optional). In alto a destra un esempio colorato: `JWSheader_JIUzI1NiIsInR5cCI6IkpXVCJ9.JWSpayload_xMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.Signature_eKKF2QT4fwpMeJf36POk6yJV_adQssw5c~Disclosure1_6phoYia7JD01dubqJSwGuz_9M206E~Disclosure2_6DQW6xiQrkyjryn77Sbuc2N44ScEGlE~Disclosure3_cKeuvFppyAPl4rc_WE2Fn3f5fg3W1Ow~KB_JWT_45wfxz18dw`. Testo a destra: "In a VP, the holder sends the e-sealed part of the VC to the verifier, but only the *minimal* set of personal data, as requested by the verifier, are appended *unhashed*. The verifier shall be able to check each claims since it has their "e-sealed" digests."

La spiegazione (*DI-06 @ 00:57:51-01:03:44*). L'IdP (o l'issuer) rilascia una credenziale verificabile come un unico pacchetto JSON firmato, "tipicamente un sigillo elettronico dell'issuer", con tutti i dati: come un passaporto, nome, cognome, data e luogo di nascita, cittadinanza, età, sesso, altezza, peso, colore degli occhi, segni particolari, foto. Se fosse firmato così, l'holder dovrebbe presentarlo tutto: togliere anche un dato invaliderebbe la firma, "basta cambiare un bit, lo sapete ormai". Nella VC la parte firmata non contiene i dati personali ma i loro **digest**; i dati sono appesi in fondo. Nella presentazione l'holder inoltra la parte firmata **intatta** (il verificatore controlla il sigillo: certificato valido, non scaduto, impronta del blocco corrispondente) e allega solo le **disclosure** che servono. Esempio: per comprare un ebook servono email e maggiore età; se l'issuer fornisce un booleano "maggiorenne", l'holder non manda nemmeno la data di nascita. Il verificatore calcola l'hash delle disclosure ricevute e controlla che sia fra i digest firmati: se c'è, il dato è protetto dal sigillo dell'issuer ed è autentico. È "uno dei tanti formati" di selective disclosure usati nel wallet europeo, ed "ecco perché nel corso vi ho parlato di firme sui JSON".

### Verifica per esecuzione

Esempio costruito per questo capitolo (non mostrato a lezione), in Python con `hashlib` e `base64`, seguendo RFC 9901 (*Selective Disclosure for JSON Web Tokens*, novembre 2025). Una disclosure è la codifica base64url (senza padding) dell'array JSON `[salt, nome, valore]`; il digest è la codifica base64url dello SHA-256 calcolato sulla **stringa base64url della disclosure** (non sul valore in chiaro):

| Array JSON | Disclosure (base64url) | Digest SHA-256 (base64url) |
|---|---|---|
| `["c2FsdDAwMDAwMDAwMDAwMQ", "given_name", "Mario"]` | `WyJjMkZzZERBd01EQXdNREF3TURBd01RIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ` | `r5_gwLebcarkjqNnd5MpQc_A8noQJ6XYna4pKoZxaeo` |
| `["c2FsdDAwMDAwMDAwMDAwMg", "family_name", "Rossi"]` | `WyJjMkZzZERBd01EQXdNREF3TURBd01nIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0` | `tKach55NLWc7WV5E75-Bynag_yF-c7pbP0WXLt11wco` |
| `["c2FsdDAwMDAwMDAwMDAwMw", "expiry_date", "2028-03-21"]` | `WyJjMkZzZERBd01EQXdNREF3TURBd013IiwgImV4cGlyeV9kYXRlIiwgIjIwMjgtMDMtMjEiXQ` | `roBrkhwuCu4p7TiPECpoZB-nDbHxsZf_VjMtKaUf3Y4` |
| `["c2FsdDAwMDAwMDAwMDAwNA", "birthdate", "1980-01-01"]` | `WyJjMkZzZERBd01EQXdNREF3TURBd05BIiwgImJpcnRoZGF0ZSIsICIxOTgwLTAxLTAxIl0` | `6oeq6J8ww_w_HsJjvKl6-LcgEb6hHMkNTjB_h35xA3o` |

Il payload firmato dall'issuer contiene `"_sd_alg": "sha-256"` e `"_sd"` con i quattro digest (in ordine casuale o ordinato). L'holder presenta al noleggiatore solo le prime tre disclosure: il verificatore ne ricalcola i digest e li trova tutti in `_sd`; la data di nascita resta nascosta dietro il suo digest. Per controllare l'implementazione è stata ricalcolata anche la disclosure di esempio di RFC 9901 (`["2GLC42sKQveCfGfryNRN9w", "given_name", "John"]` → digest `jsu9yVulwQQlhFlM_3JlzMaSFzglhQG0DpfayQwLUK4`), che coincide con quella pubblicata nella RFC. **Verificato.**

Sui frammenti della slide: decodificati in base64url, l'header `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (la slide ne mostra la parte dopo il prefisso) è `{"alg":"HS256","typ":"JWT"}` e il payload è `{"sub":"1234567890","name":"John Doe","iat":1516239022}`: è il JWT di esempio di jwt.io, usato come illustrazione. **Verificato.** Le stringhe dopo "Signature", "Disclosure" e "KB_JWT" sono segnaposto.

> **Nota aggiunta:** il **sale** è indispensabile: senza, il digest di un valore con pochi casi possibili (una data di nascita, un booleano) si invertirebbe per forza bruta. Per questo il digest si calcola sull'intera disclosure, sale compreso. Il **KB-JWT** (*Key Binding JWT*) è un JWT firmato con la chiave privata dell'holder, la cui chiave pubblica è nella credenziale (il `public key` dello schema, claim `cnf`): contiene `iat`, `aud`, `nonce` e `sd_hash` (hash dell'SD-JWT presentato con le disclosure scelte) e impedisce che una presentazione intercettata venga riusata da altri o verso altri verificatori. Senza KB-JWT la stringa termina comunque con una tilde. L'issuer può aggiungere **digest civetta** (*decoy digests*) per nascondere quanti claim esistono. Il JWT di esempio della slide usa `HS256`, un MAC simmetrico: in un SD-JWT VC reale l'issuer firma con una chiave asimmetrica (ES256 e simili), altrimenti il verificatore non potrebbe verificare senza conoscere il segreto dell'issuer.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 16 (SD-JWT): l'esempio della patente*

- **Avvertenza del docente.** "Questa è una slide ovviamente solo per chi ha un po' di dimestichezza con il JSON e con il JSON Web Token. Chi ha un profilo un po' da sviluppatore... non ci saranno domande su questa slide" (la frase è sintatticamente incerta; vedi sezioni 26 e 27). Richiama la variante europea della firma JSON, JAdES, standard a cui dice di aver contribuito. (Teams 8 @ 0:40:31-0:41:19)
- **App IO.** L'app IO è la declinazione italiana del wallet; "al momento in cui abbiamo registrato queste lezioni" funziona con la patente, il permesso di soggiorno [?] e il tesserino del codice fiscale o tessera sanitaria. A un controllo delle forze dell'ordine il documento si mostra come **QR code**, mezzo fisico che non richiede Internet; dentro c'è un JSON con tutti i dati della patente. (Teams 8 @ 0:41:19-0:43:02)
- **Il problema.** Per noleggiare un'auto basta dimostrare di avere una patente B valida (nome, cognome, scadenza), ma la credenziale rilasciata dalla Motorizzazione contiene tutto (data di nascita, gruppo sanguigno, seriale, obbligo di lenti...): l'issuer non sa a cosa ti serve, a differenza di SPID dove il service provider dichiara prima quali dati chiede. (Teams 8 @ 0:43:02-0:44:51)
- **Il trucco.** Nel JWT sigillato (con sigillo qualificato della Motorizzazione) al posto dei valori ci sono le impronte crittografiche; dopo il JWT, separati da caratteri **tilde**, ci sono gli svelamenti in base64. Nella presentazione per il noleggiatore l'holder lascia intatto il JWT con tutti gli N digest e allega solo le tre disclosure necessarie; il verificatore convalida il sigillo, calcola le impronte delle tre disclosure e le ritrova nel token, capendo dalla posizione che "Mario" è il nome e "Rossi" il cognome. (Teams 8 @ 0:44:51-0:52:22)
- **Secondo esempio: la laurea.** Un'attestazione di laurea contiene i digest di voto, data, titolo della tesi, commissione, e di ogni esame con data e voto. Per iscriversi a una scuola di specializzazione in neurochirurgia basta svelare corso di laurea e data; i voti di singoli esami si potranno svelare in una seconda presentazione. (Teams 8 @ 1:34:28-1:36:12)

> **Correzione:** a voce (DI-06 @ 01:00:27-01:01:00, Teams 8 @ 0:45:29-0:47:44) il docente dice che nel token firmato al posto del valore c'è "l'hash del nome" e che la disclosure è "la rappresentazione in base64 della stringa del nome". Nello standard (e nella slide stessa) la disclosure è la base64url dell'array `[sale, nome del claim, valore]` e il digest è calcolato sulla disclosure, sale compreso; il nome del claim sta nella disclosure, non nel token in chiaro. La verifica per esecuzione sopra mostra il meccanismo esatto.

## 17. Gli schemi eID italiani: SPID, CIE, IT-Wallet

*DI-06 @ 01:03:44*

**Slide di sezione "Electronic identity schemes and the "EUDI Wallet""** (*DI-06 @ 01:04:04*): immagine di un profilo digitale con le voci *Name, Home Address, Business Address, Identity Card No, Passport No, Driving License, Income Tax No, Car Registration, Other* e un riquadro *Confidential Data*.

Con il regolamento eIDAS del 2014, quando "i tempi non erano maturi" per un'unica identità europea, ogni Stato membro è stato lasciato libero di creare il proprio schema di identificazione elettronica e notificarlo. In Italia **SPID**, notificato nel 2018 (procedura 2017-2018), e **CIE**, notificata nel 2019 (procedura 2018-2019): oggi gli unici due schemi italiani notificati. Con la revisione del 2024 l'**app IO** di PagoPA si è candidata a essere l'IT-Wallet italiano per i servizi pubblici (*DI-06 @ 01:03:44-01:05:31*).

**Slide "The Italian eID's – IT-Wallet, CIE and SPID"** (*DI-06 @ 01:04:32*): logo SPID con `https://www.spid.gov.it`; logo CieID e facsimile della CIE con `https://cartaidentita.interno.gov.it`; logo IO con `https://www.pagopa.it/it/prodotti-e-servizi/european-digital-identity-wallet`.

**Slide "SPID, by numbers (2025 over 2024)"** (*DI-06 @ 01:05:31*, *01:06:31*). Grafico delle identità SPID rilasciate per mese, con le serie 2020 (da 5.685.148 di gennaio a 13.489.155 di dicembre), 2021 (da 16.696.092 a 26.900.274), 2024 (da circa 37 milioni a 39.290.854 di novembre) e 2025 (primo valore [illeggibile]: due numeri sovrapposti, "37.070.441" o simile). A destra:

- **40.1M** issued eID's (+1%)
- YoY rates: +150% in 2019; +260% in 2020 (*Covid*); +200% in 2021; +23% in 2022; +9% in 2023; +1% in 2024
- ~**19.1k public** SP's (+20%)
- ~**210 private** SP's (+13%)
- **12** IdP's (--)
- **0** EEAPs / AAs

Fonti: `https://www.spid.gov.it/open-data-spid/`, `https://avanzamentodigitale.italia.it/it/progetto/spid`.

Commento (*DI-06 @ 01:05:31-01:06:36*): il docente ha cercato dati aggiornati ma la pagina non è più disponibile; i dati sono all'inizio del 2025. La crescita maggiore è negli anni pandemici 2019-2021; poi le identità si sono attestate intorno ai **40 milioni**, quasi tre quarti della popolazione. Ripreso più avanti (*DI-06 @ 01:27:48*): 19.000 PA aderenti, "la totalità" (le PA italiane sono "intorno alle 21-22 mila", dalle centrali fino alle scuole), contro circa **200** service provider privati, "due ordini di grandezza sotto"; proporzioni simili in Europa, perché per i privati non c'era obbligo.

**Slide "CIE – Carta d'Identità Elettronica"** (*DI-06 @ 01:07:06*, *01:07:45*). Facsimile della versione attuale (CIE v2.1) e della precedente (CIE v2.0), con le etichette: *ICAO symbol*; *EU flag with issuing country's abbreviation*; *optional "non valid for expat" text*; *serial number*; *nation's code*; *subject's signature raster*; *subject's photograph (ICAO standards)*; *CAN (Card Access Number)*; *expiry date*.

La CIE "parla lo stesso linguaggio" di SPID ma offre di più, perché è legata alla carta fisica: documento di riconoscimento e di viaggio valido in Europa, con caratteristiche di sicurezza anche elettroniche e la possibilità di **firme elettroniche avanzate** (app CieSign). Con l'app **CieID** si ha un'identità identica a SPID, anzi di livello 3 (*DI-06 @ 01:06:36-01:08:15*).

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 17 (schemi italiani)*

- **Notifiche.** Ogni Stato dovrebbe avere almeno uno schema notificato; l'Estonia ne ha sei, alcuni Stati nessuno, anche perché non tutti gli schemi avevano portata transfrontaliera. SPID e CIE parlano SAML oppure OpenID Connect, secondo il linguaggio del service provider. (Teams 8 @ 0:52:54-0:54:10)
- **SPID.** Federazione di 12 gestori, fra cui Poste Italiane, InfoCert, Aruba; Lepida, "comunemente chiamato l'IdP pubblico", è in realtà una S.p.A. partecipata, società in house della Regione Emilia-Romagna. (Teams 8 @ 0:54:10-0:54:50)
- **La doppia anima della CIE.** Una chiave privata con certificato per le **FEA** (di cui "oggi non parleremo") e un'altra per l'**autenticazione**; il certificato di autenticazione contiene numero seriale della carta e codice fiscale. Con la CIE di livello 3 è come mostrare la carta al service provider, "con la sola differenza che non mostriamo la foto". (Teams 8 @ 0:54:50-0:56:12)
- **Gratuità.** I privati entrano in SPID pagando gli IdP (business model che "non sembra aver funzionato tanto bene": più di 16.000 PA contro poco più di 200 privati); per i servizi pubblici SPID deve essere gratuito per legge, come la CIE (si paga solo la produzione della carta, come per il passaporto, entrambi fatti dal Poligrafico). Per CIE l'IdP è il Ministero dell'Interno, su infrastruttura dell'IPZS. (Teams 8 @ 0:56:12-0:59:31)

> **Correzione:** in Teams 8 @ 0:58:04 il docente scioglie SPID come "servizio pubblico d'identità digitale"; l'acronimo è **Sistema Pubblico di Identità Digitale** (come nella slide del flusso, *DI-06 @ 01:12:35*).

## 18. L'ecosistema CIE/SPID: aggregatori, RAO, gestori di attributi, deleghe

*DI-06 @ 01:08:15*

**Slide "The CIE / SPID ecosystem, at large"** (*DI-06 @ 01:07:43*): *public sector Service Providers*, *private sector Service Providers*, *USERs*, *Identity Providers*, *Attribute Authorities*, logo AGID.

**Slide "The CIE / SPID ecosystem – some details"** (*DI-06 @ 01:11:47*): *public sector Service Providers* con *Aggregators of public SPs*; *private sector Service Providers* con *Aggregators of private SPs*; *Identity Providers* (i loghi dei 12 IdP SPID e la bandiera italiana per CIE) affiancati dai *RAOs*; *Qualified Attribute Authorities* (loghi di SGD, ordine dei medici, ordine degli ingegneri di Napoli e altri) e "...*Non*-qualified Attribute Authorities"; riquadro "Supervisory AGID. Registries: SPID + OIDC; AA; GLs / *Avvisi*"; logo della Commissione europea.

I service provider sono distinti in pubblici e privati perché i privati pagano una *fee* per entrare nella federazione, i pubblici aderiscono per effetto di un decreto del 2014 rinnovato periodicamente (secondo il docente l'ultima volta "meno di un mese fa"). Le **attribute authority** nell'idea originaria sarebbero stati gli ordini professionali. Era previsto un **sistema nazionale di gestione delle deleghe** (persona fisica verso persona fisica e verso persona giuridica), dall'**art. 64-quater del CAD**, "almeno che io sappia" non ancora realizzato: nato in SAML (normativa a cui il docente ha partecipato), poi spostato su OpenID Connect; consentirà a chi non ha SPID, CIE o IT-Wallet (infermi, anziani, persone in *digital divide*, detenuti) di delegare compiti a un delegato, che userà la propria identità più un'**attestazione elettronica di attributo** che rappresenta il potere di rappresentanza (*DI-06 @ 01:08:15-01:10:02*).

**Aggregatori** (*DI-06 @ 01:10:02-01:11:35*): fornitori IT, cresciuti nel periodo pandemico, che fanno "l'ultimo miglio" con PMI e piccole PA (di solito locali) rendendo i loro servizi compatibili con SPID e CIE, e fanno da intermediari fra service provider e **AgID** (per SPID, di cui è *owner*) o **Poligrafico** (per CIE, per delega del Ministero dell'Interno), che curano l'onboarding tecnologico.

**Slide "Public- and private-services Aggregators"** (*DI-06 @ 01:20:17*). In alto: "There are ~130 *public-sector SP* aggregators (May 2022)". A sinistra un estratto AgID "Come diventare soggetti aggregatori": gli aggregatori offrono ai soggetti pubblici aggregati l'accesso con SPID ai servizi online; dopo l'iscrizione al Registro SPID gestiscono in autonomia i rapporti con gli aggregati nel rispetto della convenzione con AgID; modalità **"light"** (autenticazione tramite l'infrastruttura dell'aggregato, su cui è installata la soluzione dell'aggregatore: AgID rilascia un certificato di **CA intermedia (sub-CA)** con cui l'aggregatore genera certificati di sigillo elettronico per ciascun aggregato) e **"full"** (autenticazione tramite l'infrastruttura dell'aggregatore: AgID rilascia direttamente un certificato di sigillo elettronico); certificati regolati dall'**Avviso SPID n. 23**; uno stesso aggregatore può operare in entrambe; due procedure di adesione, tecnica e amministrativa. A destra:

- **Aggregators** sell authentication infrastructure / services to several ("aggregated") SPs.
- Aggregators become the PoCs *between* governing bodies (AgID and Ministry of Internals) and **SP**s.
- Aggregators may: be (themselves) companies or PAs; aggregate *public* or *private* SPs.
- Aggregator services may be part of larger service offerings to SPs.
- "Light" / "*Full*" Aggregations.

**RAO** (*DI-06 @ 01:11:35-01:12:24*): le *registration authority* (già viste parlando di certificati) quando sono pubbliche amministrazioni possono avere convenzioni con gli IdP SPID e CIE per rilasciare l'identità digitale a dipendenti o cittadini allo sportello: l'identity proofing l'ha già fatto la PA quando ha assunto il dipendente.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 18 (ecosistema)*

- **RAO e SPID professionale.** Una PA può istituire un servizio RAO per dare ai dipendenti uno SPID ad uso professionale della persona fisica, senza che si registrino o paghino un'identificazione da remoto presso l'IdP. (Teams 8 @ 0:59:31-1:00:44)
- **Attribute authority mai attivate.** Previste dal 2014 come terza componente di SPID, con linee guida AgID arrivate tardi ("nel 2019, se non sbaglio", a cui il docente ha contribuito), non si sono mai concretizzate perché era già in cantiere il modello europeo basato sul wallet, che ha preso "tanta italianità". (Teams 8 @ 1:01:04-1:02:21)
- **Governance.** AgID è l'organo di vigilanza nazionale e tiene i registri di IdP e service provider, consultati per accertare la validità dei sigilli elettronici su richieste e risposte SAML e messaggi OIDC. (Teams 8 @ 1:04:17-1:05:13)
- **Perché servono gli attributi.** Senza attributi l'identità digitale è "una mera presentazione dell'identità": SPID semplifica il login, ma poi per un permesso ZTL bisogna ancora caricare documenti (libretto, residenza, interesse legittimo) che qualcuno, persona o IA, deve leggere; pochi servizi sono totalmente digitali. (Teams 8 @ 1:05:51-1:07:43)
- **Aggregatori, 2026.** Vanno da service provider piccoli e poco organizzati (il venditore di pizza, ma anche l'asilo o la scuola media il cui referente informatico "lavora per 18 enti territoriali") e li portano nello schema; l'utente si autentica all'infrastruttura dell'aggregatore, che mostra il nome del service provider finale. "Non ritengo sia utile approfondire" le modalità tecniche. (Teams 8 @ 1:07:43-1:09:59)

## 19. Flusso SAML, livelli di garanzia e interfaccia di SPID e CIE

*DI-06 @ 01:12:24*

**Slide "SPID and CIE authentication flow (SAML based)"** (*DI-06 @ 01:12:35*). Loghi "spid Sistema Pubblico di Identità Digitale" e CieID; tre linee di vita: *Fornitore di Servizi / Service Provider (SP)*, *Utente SPID (browser)*, *Gestore Identità Digitale / Identity Provider (IdP)*. Passi: (A) Richiesta di accesso al servizio; (B) AuthnRequest (dal SP all'IdP passando per il browser); (C) Richiesta credenziali (Livello 1/2/3); Invio credenziali; (D) Response (dall'IdP al SP passando per il browser); (E) Accesso al servizio. Il docente non lo ricommenta: "è quello che vi ho raccontato".

**Livelli di garanzia** (*DI-06 @ 01:12:54-01:15:29*). eIDAS ha tre livelli che il docente chiama livello 2, 3 e 4 ("basata sullo standard ISO") ovvero "medio, sostanziale ed elevato"; negli schemi nazionali, "purtroppo c'è una differenza di più uno", diventano i livelli 1, 2 e 3 di SPID e CIE. SPID con sola username e password è livello 1 (medio); con 2FA (token, OTP) livello 2 (sostanziale); il livello 3, offerto solo da alcuni IdP e tipicamente a pagamento, con credenziali in HSM qualificati eIDAS, è equiparato all'elevato. La CIE fornisce di base il **livello 3**: i dati sono letti via NFC dal chip, protetti dalla chiave privata il cui certificato è rilasciato dal Ministero dell'Interno all'emissione. Da alcuni anni registrandosi sul portale CIE si ottengono credenziali di livello 1 e 2 che funzionano come SPID (primo fattore, secondo fattore, eventualmente sostituito dalla biometria). Il livello 3 richiede la carta a ogni autenticazione (letta con PIN).

**Slide "SPID and its assurance levels (LoA)"** (*DI-06 @ 01:14:44*):

> - SPs decide the minimum Level for each class of their own services;
> - IdPs may override those enforcing a higher-level authentication;
> - the **user** may freely decide to authenticate with a higher level.
> - SPID Level **1** uses **1FA**; Level **2** uses **2FA**; Level **3** uses **MFA** (2FA+);
> - CIE Level **1** uses **1FA**; Levels **2** and **3** use **2FA**;
>
> With respect to EU Levels of Assurance (**LoA**) pursuant to **eIDAS1** Regulation:
> - SPID and CIE Level **1** correspond to eIDAS LoA **2**, "MEDIUM";
> - SPID and CIE Level **2** correspond to eIDAS LoA **3**, "SUBSTANTIAL";
> - SPID and CIE Level **3** correspond to eIDAS LoA **4**, "HIGH".

> **Correzione:** il livello di garanzia più basso di eIDAS si chiama **low** ("basso" nel testo italiano), non "medium"/"medio": la prima slide della lezione (*DI-06 @ 00:01:08*) scrive infatti "LOW = LoA 2", in contraddizione con questa. Gli altri due sono *substantial* ed *high* (nel testo italiano del Reg. 910/2014 "significativo" ed "elevato"; il docente dice "sostanziale"). L'errore "medio" si ripete a voce in Teams 8 @ 1:12:28.

**Slide "SPID and CIE – a unified authentication UX"** (*DI-06 @ 01:15:16*): il menu "Entra con SPID" con alcuni IdP; la pagina di login SPID (nome utente, password, "Entra con SPID", timer "Tempo rimanente 02m 10s", "Tentativi rimanenti 5", in basso le etichette *SAML* e *Relay State*); la pagina InfoCert per l'INPS che chiede l'OTP via app; il pulsante "Entra con CIE".

**Slide "QR-code based 2FA in SPID – IdP example #1"** (*DI-06 @ 01:15:22*): pagina Poste ID "Richiesta di accesso di livello SPID 2 da Ministero del Lavoro e delle Politiche Sociali" con QR code ("Inquadra il QR Code con l'App PosteID. Il codice è valido per 118 secondi") e due schermate dell'app ("Autorizza con QR code", "Inquadra QR Code").

**Slide "QR-code based 2FA in SPID – IdP example #2"** (*DI-06 @ 01:15:30*): InfoCert ID, "Richiesta di accesso SPID di livello 2 da Università degli studi Roma Tre", QR code valido 26 secondi; a destra la schermata di consenso "Accedendo a questo servizio autorizzi InfoCert a trasmettere le seguenti informazioni": Partita IVA, Luogo di nascita, Domicilio fisico, Sesso, Documento d'identità, Ragione o denominazione sociale, Codice identificativo SPID, Data di nascita, Numero di telefono mobile, Cognome, Domicilio digitale, Nome, Provincia di nascita, Sede legale, Codice fiscale, Indirizzo di posta elettronica, Data di scadenza identità; pulsanti *Non autorizzo* / *Autorizza*.

**Slide "Access levels, MFA and login UI – CIE"** (*DI-06 @ 01:15:35*): schermate del Ministero dell'Interno. Livello 2: "Potrai accedere confermando la tua identità con codice OTP o App CieID"; livello 3: "Dovrai leggere la tua CIE con l'App CieID usando un telefono con tecnologia NFC o con un PC dotato di lettore NFC"; elenchi di ciò che si può fare con le credenziali di livello 2 e 3 (modificare password, aggiornare email e cellulare, gestire i dispositivi certificati, controllare gli accessi, sospendere o revocare le credenziali; con il livello 3 anche attivare le credenziali CIE); pagina "Richiesta d'accesso CIE livello 2" con "Entra con le tue credenziali CIE", "Entra con App CieID" (QR code, "Validità codice: 1':45''") e "Entra con lettura carta".

Il livello 1 "esiste ma di fatto non è quasi mai richiesto"; per i livelli 1 e 2 la CIE va attivata sul portale (*DI-06 @ 01:15:29-01:16:01*).

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 19 (livelli e consenso)*

- **Chi sceglie il livello.** L'utente può scegliere il livello, subordinato al minimo richiesto dal service provider secondo la sensibilità del servizio. I livelli di SPID e CIE sono equiparati; la normativa scrive "livello di garanzia elevato/sostanziale" e non "livello 3/2" perché i sistemi pubblici devono garantire l'identità a tutti i cittadini dell'Unione e parlare un linguaggio comprensibile in tutta Europa. (Teams 8 @ 1:09:59-1:13:18)
- **CIE livelli 1 e 2.** Per questi la CIE usa un modello analogo a SPID: un IdP "virtuale" del Ministero e l'app CieID sullo smartphone, senza carta. (Teams 8 @ 1:11:25-1:11:55)
- **La schermata di consenso.** InfoCert elenca, prima dell'autorizzazione, i dati che il service provider ha chiesto e chiede il consenso ai sensi del GDPR; il titolo (Università degli Studi Roma Tre) è preso da un metadato **sigillato elettronicamente** quando l'ente è entrato nella federazione, quindi da una fonte autoritativa: un soggetto non federato verrebbe rifiutato prima, e uno registrato con nome falso si potrebbe "sgamare". Le schermate si possono falsificare (la sua è uno screenshot preso da Internet). (Teams 8 @ 1:13:18-1:15:12)

## 20. Attributi SPID e CIE, identità ad uso professionale

*DI-06 @ 01:16:01*

**Slide "SPID and CIE attributes for natural persons"** (*DI-06 @ 01:16:12*, *01:17:01*). Testo: "Currently, identification data in the **CieID** scheme are *contactless* read by the card's filesystem itself (and are electronically sealed by the Italian Ministry of Interior); they are a subset of SPID's and are listed below in bold face." Elenco: **first / last** name; **date** / place of birth; **fiscal code** (*codice fiscale*); **e-mail** address; **mobile** phone number. "**SPID** scheme also adds the following attributes": "SPIDcode" (sort of UNIX UID); digital ID expiration date; gender; physical ID / unique ID serial #; residency (street address, zip code, municipality, province, nation); domicile (same 5 attributes as residency); digital domicile (currently, PEC) address. In basso: "By enrolling to the **CieID** website and activating Levels 1/2, also the subject's email address and telephone numbers, after validation, may be provided. Further identification data may be provided as long as the scheme federates with other authoritative sources (e.g. *Anagrafe Nazionale della Popolazione Residente* – **ANPR**)."

SPID e CIE hanno identità di **persona fisica** (non esiste una carta d'identità di un'azienda). La differenza: SPID può trasferire ulteriori dati (sesso, scadenza del documento, residenza e domicilio, domicilio digitale); CIE si limita a nome, cognome, data di nascita e codice fiscale, più email e telefono se si sono attivati i livelli 1 e 2 (*DI-06 @ 01:16:01-01:17:23*).

**Slide "SPID attributes for legal persons"** (*DI-06 @ 01:16:59*, *01:17:22*): organization name (*ragione sociale*); VAT number (*numero di partita IVA*); registered address (*sede legale*, 5 attributes as per residency); digital ID expiration date; digital domicile, currently the "registered email" (**PEC**) address.

L'identità digitale della **persona giuridica**, a pagamento, ha avuto "scarsissimo successo": per un contratto o una convenzione, anche con la PA, serve una **firma**, un'attestazione della volontà di qualcuno, non l'autenticazione di una persona giuridica (*DI-06 @ 01:17:23-01:18:26*).

**Slide "Professional use legal-/natural-person identities"** (*DI-06 @ 01:19:18*): "Same attributes as non-professional-use, **natural** person IDs, **plus**: For "*identità ad uso professionale della persona fisica*" only: personal VAT number (*partita IVA individuale*). For "*identità ad uso professionale della persona giuridica*" also the legal-person attributes (related to the subject's professionally affiliated organisation) can be attested by the IdP: organization name (*ragione sociale*); registered address (*sede legale*, 5 attributes as per residency); **organization** VAT number or fiscal code (*codice fiscale*); digital domicile (currently, PEC) address." (Nella slide "the the", refuso.)

Più interessanti le **identità ad uso professionale** (*DI-06 @ 01:18:26-01:19:57*): quella della persona fisica veicola anche la partita IVA del libero professionista (servizio a pagamento, fuori dalla convenzione degli IdP con AgID); quella della persona giuridica attesta anche l'organizzazione per conto della quale si opera. **Attenzione: non attesta una delega**, che non è potere dell'IdP attestare: attesta solo un'affiliazione, per esempio di un consulente che opera a proprio nome informando la controparte del rapporto con l'organizzazione.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 20 (attributi)*

- **Esame.** Elencati gli attributi CIE (nome, cognome, luogo e data di nascita, codice fiscale; con il livello 3 anche il seriale della carta; email e telefono se attivati i livelli 1 e 2): "Non vi preoccupate, non ci saranno domande su questi attributi. Non metto domande nozionistiche in cui dovete ricordare a memoria queste caratteristiche, è solo per vostra cultura." (Teams 8 @ 1:15:18-1:17:02)
- **ANPR.** È previsto che la CIE sia agganciata all'Anagrafe Nazionale della Popolazione Residente per dare dati puntuali e aggiornati (residenza, domicilio) e non quelli stampati sulla carta. (Teams 8 @ 1:17:07-1:17:24)
- **SPID professionale.** La partita IVA individuale non sta nello SPID della persona fisica: serve lo SPID ad uso professionale della persona fisica. Lo SPID ad uso professionale della persona giuridica veicola nome e cognome della persona e ragione sociale, sede legale, partita IVA dell'organizzazione. Esistono solo in Italia e **non sono un sistema di gestione deleghe**: per un'operazione con esposizione legale (cambiare la ragione sociale, un acquisto da un milione) il service provider deve chiedere una vera delega ai sensi dell'art. 47 del DPR 445/2000, di cui SPID non si occupa. (Teams 8 @ 1:17:24-1:20:28)

## 21. Attributi qualificati e non qualificati

*DI-06 @ 01:19:57*

"E veniamo infine agli attributi, l'ultimo argomento del corso." Lo schema SPID originario (2014) prevedeva il quarto ruolo delle **attribute authority qualificate**, che attestano stati, qualifiche, abilitazioni professionali e poteri di rappresentanza perché una legge glielo consente. Esempi: titoli di studio; titoli professionali di ordini e albi (medico, psicologo, ingegnere, architetto, geometra, avvocato); titoli accademici (professore ordinario e associato, rettore, prorettore, decano); gradi militari, anche nella scala NATO OF per l'equiparazione internazionale; ruoli nella PA (funzionario, dirigente di prima e seconda fascia, direttore generale); patenti (di guida, nautica, da manutentore di caldaie a gas); titoli di possesso di beni mobili e immobili (catasto); poteri di rappresentanza e delega. Erano previsti anche gestori qualificati di attributo con una propria normativa (a cui il docente ha partecipato), superata dalla revisione eIDAS del 2024 prima di essere attuata: probabilmente li vedremo direttamente come **fornitori di EAA** (*DI-06 @ 01:06:04-01:06:36, 01:19:57-01:21:41*).

Gli attributi **non qualificati** sono attestati senza che una legge lo imponga: il possesso di un oggetto (l'operatore virtuale che, prima di attivare una eSIM, chiede allo store la conferma che il telefono è tuo); i ruoli in un'azienda, che l'azienda stabilisce in autonomia (il negozio che, prima di vendere un cestino di penne con la carta aziendale, chiede all'azienda la conferma che sei "addetto agli acquisti") (*DI-06 @ 01:22:21-01:24:01*).

**Slide "Qualified and non-qualified Attributes"** (*DI-06 @ 01:21:19*, *01:23:19*). Testo:

> **Attributi qualificati**: «le qualifiche, le abilitazioni professionali e i poteri di rappresentanza e qualsiasi altro tipo di attributo attestato da un gestore di attributi qualificati, ivi compresi i dati relativi al possesso di abilitazioni o autorizzazioni richieste dalla legge ovvero stati, qualità personali e fatti contenuti in albi, elenchi o registri pubblici o comunque accertati da soggetti titolari di funzioni pubbliche, secondo le modalità stabilite da AgID con Linee guida», pursuant to Italian DPCM 24/10/2014, art. 1 *comma* 1.
>
> **eIDAS2 Regulation** treats [qualified] electronic attestations of attributes ([Q]eAAs) rather than attributes themselves; it also qualifies the electronic *attestations* rather than the attributes themselves. Italian law, instead, *qualifies* the attributes as whether they are provided by subjects which attest them by law, or not.

Esempi qualificati: education (Dr, MEng, BSc, MPhil, PhD); M.D., *Ing.*, *Arch.*, *Geom.*, *Avv.*; academic (Prof., Rett.); military grades (LT, Col., Gen.; NATO OF-*n*...); roles within PA (officer, DG, ...); driving or LTZ licenses; real estate ownership; organizations' representations / delegations. Esempi non qualificati: items' ownership; phone number/email ownership; bank accounts and CCs; company roles; social media statuses; sport/gaming ranks; other employment information.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 21 (attributi qualificati)*

- **Esempi 2026.** Ordini professionali (medico, avvocato, geometra, ingegnere, architetto), attestato da sub, patentino per impianti a gas, porto d'armi, titolo di studio (dal Ministero dell'Istruzione o dell'Università per conto di scuola o ateneo), grado militare dal Ministero della Difesa. Nel mondo fisico sarebbero "certificati di attributo"; nel wallet europeo sono **attestazioni elettroniche di attributo**, la cui emissione è un servizio fiduciario eIDAS. Sono tutti sigillati elettronicamente: l'Ordine degli architetti di Novara attesta che Tizio è architetto; l'ordine dei medici che Valeria Bianchi è endocrinologa e quindi non può prescrivere interventi di ortopedia. (Teams 8 @ 1:02:21-1:05:51)

## 22. eIDAS 2 e l'EUDI Wallet

*DI-06 @ 01:24:01*

**La storia** (*DI-06 @ 01:24:01-01:27:15*). Nel 2014 si decise che ogni Stato notificasse i propri schemi: nonostante l'obbligo, secondo il docente, di notificarne almeno uno "entro sette anni, mi pare", ci sono ancora 4 o 5 Stati senza schemi notificati, quasi tutti ne hanno uno, alcuni più d'uno (oltre all'Italia "mi sembra" Germania, Portogallo, Francia, Olanda e Belgio; per l'Olanda forse uno per il privato con persone giuridiche e uno per il pubblico, "ma non sono sicuro"). Persino il Regno Unito notificò uno schema prima della Brexit. Il docente era a Bruxelles alla notifica degli schemi estoni, il Paese con più schemi: sei notificati contemporaneamente a SPID, cinque legati a documenti (carta d'identità, permesso di soggiorno, passaporto ordinario e diplomatico, un'altra carta) e uno legato alla **SIM** fisica del telefono, "l'unico schema europeo basato su SIM". Il framework di interoperabilità, in Italia "nodo eIDAS", funziona solo parzialmente, fra alcune coppie di Paesi. Da qui, nel 2024, lo schema a **wallet**: un'unica identità su un unico framework tecnologico standardizzato, con il codice sorgente in un repository pubblico su GitHub, e con obblighi di adesione non più solo per le PA (con eIDAS 1 aderirono di fatto solo i soggetti pubblici obbligati; i privati solo dove conveniente).

**Obblighi** (*DI-06 @ 01:28:19-01:29:58*): il **Reg. 2024/1183** impone ad alcuni settori privati di aderire **entro il 2027**, consentendo l'autenticazione con l'**EUDI Wallet**, "il passaporto europeo dell'identità digitale", modello basato su self-sovereign identity. Non un'app unica: ogni Stato può avere più soluzioni. In Italia la normativa del 2024 prevede un unico **IT-Wallet pubblico**, gestito tramite l'app IO da PagoPA, e in futuro più IT-Wallet privati. I wallet devono consentire l'uso transfrontaliero di attestazioni di identità e di attributi: chi li sviluppa può usare il linguaggio che vuole, purché almeno le funzioni di base previste dalla legge siano compatibili con l'**architettura di riferimento**, il cui codice (non di produzione, riusabile in parte) è su GitHub.

**Slide "European Digital Identity (EUDI) Wallet"** (*DI-06 @ 01:27:04*): mappa mentale attorno a un telefono "EU ID Wallet" (con *National eID, Driving License, Diploma, Insurance, Travel, Payment*). Rami: **General** (Proofs: of insurance, of account ownership, permissions, enter into contract (signature), social security card, proof of tax record, of training, of qualifications, of loyalty tier, of eligibility for discounts, of entitlements for restricted products (age, fire arms), student card, library card, of qualifications (driver license ++), of representation (person, company), of residency; Strong customer authentication; Customer enrollment; Password-less logon); **Work** (access card, access management, proof of profession, proof of role); **Tourism** (check in, payments); **Commerce** (loyalty card, payments); **Financial sector** (payments, initial due diligence); **Telecom**; **Education**; **Public sector**. (Nella slide "authetication", refuso.)

**Slide "Architecture & Reference Framework (ARF)"** (*DI-06 @ 01:30:15*). URL: `https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/`. Schema: *Authentic Source* (Civil register, Diplomas database, Tax authority) → **ISSUER** (Person Identification Data provider (PID); Qualified electronic attestation of attribute provider (QEEA); Other, non-qualified providers (EEA); Qualified electronic signature/seals (QES)) con le frecce "Provide PID", "Provide qualified attestation", "Provide non-qualified attestation", "Provide qualified signature" verso **HOLDER** (EUDI Wallet), che "Provide interface to share: PID, QEAA, EAA, QES" verso **VERIFIER** (Relying party: Citizen portal, Police, Company, Bank, Online Platform, Airport proxies). In basso: "Providers of registries of trust source (e.g. public key directory, trusted list)" e "Catalogues of attributes and EAA schemes providers", con le frecce "Provide public keys, list entries" e "Provide information for verification of EUDI Wallet, PID, QEAA, EAA, relying parties".

**Ruoli** (*DI-06 @ 01:30:32-01:34:44*): gli identity provider nell'architettura del wallet si chiamano **PID provider** (*Person Identification Data*); i **fornitori di attestazioni elettroniche di attributo** possono essere **pubblici** (le autorità che per legge già possiedono gli attributi: i "gestori qualificati di attributo" di SPID) oppure **privati**, che in quel caso devono essere **prestatori di servizi fiduciari qualificati** eIDAS, presenti nella trust list, e rilasciare attestazioni qualificate per conto di **fonti autentiche** non pubbliche, verosimilmente a pagamento: dovrebbe fare "da volano" per i privati. La differenza rispetto al modello del 2014: **non è l'attributo a essere qualificato, ma l'attestazione elettronica**. Ciò che qualifica l'attributo è la fonte autentica; quando è pubblica può attestare da sola, perché una legge glielo dice (non si può imporre a un'università di farsi attestare i titoli da un privato; "al massimo" delegare al ministero, opinione personale del docente). Quando la fonte autentica non è pubblica (il titolo di possesso di un bene mobile), la qualifica deve stare sull'attestazione e può garantirla solo un prestatore qualificato, che dialoga con la fonte, verifica i dati e li attesta sotto la propria responsabilità.

**Slide "The EUDI Wallet (EUDIW) roles"** (*DI-06 @ 01:28:46*, *01:31:53*, *01:43:53*). Diagramma dell'ARF con i ruoli numerati: *User (1)*, *Wallet Provider (2)*, *PID Provider (3)*, *Trusted List Provider (4)*, *QEAA Provider (5)*, *PuB-EAA Provider (6)*, *EAA Provider (7)*, *QES (QESRC) Provider (8)*, *Authentic Source (9)*, *Relying Party (10)*, *Conformity Assessment Body (11)*, *Supervisory Body (12)*, *Device Manufacturers and Related Subsystems Provider (13)*, *Attribute Schema Provider (14)*, *National Accreditation Body (15)*, *Registrar (16)*, *Access Certificate Authority (17)*, *Provider of Registration Certificates (18)*; componente *Wallet Unit*. Frecce principali: "Issues PID", "Issues QEAA", "Issues EAA", "Provides QC" verso la Wallet Unit; "Presents PID or attestations" verso il Relying Party; "Controls / Activates" dall'utente; "Offers services", "Provides Wallet Solution", "Provides support" dal Wallet Provider; "Provides support, tools and libraries" e "Provides device" dai costruttori; "Provides verification service" e "Provides qualified data" dalla fonte autentica; "Issues access certificate" e "Issues registration certificates"; più frecce "Is notified" verso il Trusted List Provider. Legenda: giallo *Primary Role*, viola *Component*, rosa *Governance Role*; linea continua "In scope of the ARF", tratteggiata "NOT in scope of the ARF".

**Firma qualificata gratuita** (*DI-06 @ 01:34:44-01:37:53*): eIDAS 2 garantisce che ogni wallet permetta ai cittadini di apporre **firme elettroniche qualificate**, **gratuite** se per uso non professionale: oggi in Italia le firme qualificate si comprano da un QTSP (salvo alcuni operatori pubblici che le danno ai dipendenti, come nel caso del docente); il principio è che, come non si paga per firmare a mano un contratto per proprio conto, così deve essere digitalmente. Polemiche: distinguere tecnicamente uso personale e professionale "col cappello dell'informatico mi viene mal di testa", "col cappello del red teamer mi metto a ridere" pensando agli abusi. Una proposta letta di recente: è personale se la firma la avvia il cittadino, professionale se la avvia il relying party, che allora può tracciarla, attestarla e fatturarla; "non lo sto condividendo", è un tema vivo.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 22 (eIDAS 2 ed EUDI Wallet)*

- **I nodi eIDAS.** Con eIDAS 1 gli Stati si impegnavano a rendere interoperabile entro sei mesi ogni nuovo schema notificato: ne è nata un'organizzazione **matriciale** di nodi in cui ogni Stato traduceva le autenticazioni degli schemi esteri, "una torre di Babele", obbligatoria solo per il pubblico, mai decollata per il privato in più di dieci anni, e asimmetrica: alcuni Stati accettano perfettamente tre o quattro identità estere, altre male, altre per niente. Mancava un'**architettura di riferimento**, un *proof of concept* che fissasse le caratteristiche minime comuni; imporre nel 2014 un sistema unico a Stati sovrani (alcuni monarchie, con carte ancora cartacee) "sarebbe stata una follia". (Teams 8 @ 1:20:28-1:25:44)
- **Dal 2020.** La Commissione, con il Covid "alle porte", decide di correggere lenta adozione, scarso privato e cattiva interoperabilità; sondaggi agli stakeholder; il modello wallet, allora SSI "di moda", è ritenuto sostenibile. eIDAS 2 non cancella gli schemi esistenti ma impone entro il 2027 l'accettazione dei wallet a pubblico e ad alcuni settori privati (finanziario, telecomunicazioni, istruzione). L'obbligo è per i fornitori, non per i cittadini, che potranno sempre non usare il wallet. Quattro consorzi pubblico-privati hanno sperimentato casi d'uso; l'architettura è su GitHub ("andate al sito eudi.dev"). (Teams 8 @ 1:20:53-1:21:29, 1:25:44-1:29:00)
- **PID provider italiano.** Per il wallet italiano l'unico PID provider previsto dalla normativa nazionale è l'**IPZS**, che già produce la CIE. (Teams 8 @ 1:29:30-1:30:16)
- **Tre tipi di fornitori di attestazioni.** Pubblici (a titolo gratuito, "tra virgolette"), qualificati (QTSP vigilati, per ragioni di business), non qualificati (commerciali senza qualifica, come in Italia la FEA rispetto alla firma qualificata). Esempio: un'università piccola può affidarsi al Ministero dell'Università come fornitore pubblico di attestazioni, che raccoglie dagli atenei (anche privati parificati, anche certificati cartacei degli anni '60) e attesta. (Teams 8 @ 1:30:16-1:34:28, 1:47:02-1:48:00)
- **Firma qualificata gratuita.** Ribadita: abbatte il modello commerciale dei QTSP verso i cittadini; per uso professionale (il radiologo che firma il referto, l'avvocato, il promotore finanziario) si continuerà a usare il wallet ma con una firma a pagamento. (Teams 8 @ 1:36:12-1:37:34)
- **IT-Wallet.** Il sistema si chiama **IT-Wallet**: un IT-Wallet pubblico gestito da **PagoPA** (fornitrice dell'app IO), "comprata nel 2026" da Poste Italiane e IPZS; possibili più IT-Wallet privati, tutti appoggiati a un'infrastruttura tecnica unica e centralizzata e all'unico PID provider: si è accentrato ciò che richiede il massimo di fede pubblica. L'Italia è stata fra i primi Stati a notificare il proprio wallet; l'obbligo era di registrarne almeno uno per Stato "entro il 2026". (Teams 8 @ 1:41:18-1:43:08)
- **Interoperabilità reale.** Il diagramma "si replica N volte", uno per ogni wallet, e tutti devono interoperare grazie all'ARF, ciò che "mancava nei nodi eIDAS". Il docente prevede però che per molti servizi privati l'olandese in vacanza in Italia dovrà comunque installare un wallet privato italiano, accedendovi con la propria identità olandese. (Teams 8 @ 1:43:08-1:44:52)
- **Accesso all'app IO e futuro di SPID.** Oggi all'app IO ci si autentica con SPID o CIE; poiché per molti servizi eIDAS chiede il livello elevato, e il livello 3 SPID è offerto da pochi IdP e a pagamento (gratuito solo per un periodo durante il Covid), mentre in CIE è il livello di default, il docente prevede "un eclissamento di SPID rispetto a CIE". (Teams 8 @ 1:44:52-1:46:15)

> **Nota aggiunta (verificata):** secondo il calendario di eIDAS 2, ogni Stato membro deve rendere disponibile almeno un EUDI Wallet certificato entro dicembre 2026 (24 mesi dall'entrata in vigore degli atti di esecuzione di fine 2024) e i relying party privati dei settori interessati (banche e finanza, telecomunicazioni, energia, trasporti, sanità, grandi piattaforme online) devono accettarlo circa dodici mesi dopo, entro dicembre 2027. In DI-06 @ 01:41:52 il docente parla di primi obblighi "nella primavera del 2026" e del "grande step" per i privati nel 2027. Sull'acquisizione di PagoPA: Poste Italiane (49%) e IPZS (51%) l'hanno perfezionata ad agosto 2026, acquistandola dal MEF (circa 500 milioni di euro). Il PID è rilasciato in Italia dall'IPZS anche secondo la documentazione IT-Wallet; il sito "eudi.dev" citato a voce non è stato verificato.

## 23. Sicurezza del wallet, trust list e chiusura del corso

*DI-06 @ 01:38:01*

**Superficie d'attacco** (*DI-06 @ 01:38:01-01:39:38*). Con il cappello di Cybersecurity: rendere disponibile a tutti un ecosistema paneuropeo interoperabile significa esporre decine di PID provider, centinaia o migliaia (forse decine di migliaia) di fornitori di attestazioni, centinaia di fornitori di firma qualificata, forse una decina di milioni di relying party e decine di fornitori di wallet, con crittografia eseguita sui dispositivi mobili degli utenti. Cybersecurity Act ed eIDAS prevedono schemi di **certificazione dei dispositivi** per i livelli di autenticazione più alti.

**Tutto corre sul filo della crittografia** (*DI-06 @ 01:39:38-01:41:52*): per far fidare milioni di soggetti in transazioni massicce serve un impianto di **digital trust**. "A conclusione del corso": tutto ciò che servizi digitali e identità digitali abilitano corre su elenchi di fiducia, liste di revoca, schemi di autenticazione e autorizzazione, PKI, certification authority, e alla fine sui sigilli e sulle firme elettroniche, implementate come firme digitali, "che a loro volta sono la cifratura tramite una chiave privata di un hash". Nel diagramma dei ruoli: il **Trusted List Provider**. "Dell'altro ieri" la notizia che sono stati pubblicati in Commissione gli ultimi atti di esecuzione di eIDAS sul wallet, che dicono come saranno fatte le **trust list** europee, il *backbone* fornito dagli Stati membri. A monte resta l'identity proofing degli utenti.

**Certificazione dei dispositivi ed etica** (*DI-06 @ 01:42:27-01:43:34*): non tutti gli smartphone sono gestiti in sicurezza né hanno gli stessi requisiti; alcuni vantano "un HSM nello smartphone", "cosa che non è così" (ci sono HSM da 100 dollari e da 89 mila euro). Imporre al cittadino, per il livello più alto, uno smartphone di fascia alta a sue spese è un problema etico, "nello stesso calderone" della self-sovereign identity, che secondo il docente sarà al centro della discussione dal prossimo anno. Diventerà dominante anche la *security awareness*, altrimenti l'attore della minaccia si sposterà sul wallet.

**Concentrazione del rischio** (*DI-06 @ 01:43:34-01:45:18*): rubare l'identità dal wallet permette di rispenderla in molti settori; un data breach in uno Stato membro che permetta di far soldi con identità rubate in un altro si ripercuote sull'intero ecosistema, con i danni d'immagine e i "rischi spesso non calcolabili" dell'altro corso.

### Integrazione Teams 2026 (lezione 8 2026)

*Sezione 23 (trust, dispositivi, chiusura)*

- **L'holder va certificato.** Anche l'holder, cioè hardware (smartphone, tablet) e app wallet, deve essere certificato: tutti i soggetti devono essere degni di digital trust, quindi serve un **elenco di fiducia**. "Ecco perché abbiamo iniziato questo corso parlando di certificati digitali." (Teams 8 @ 1:38:38-1:39:52)
- **Fiducia centralizzata.** "Non può esistere uno schema di identità autosovrana senza una fiducia centralizzata": serve una **radice di fiducia** (*root of trust*, *trust anchor*), assiomatica, come per i certificati (autofirmato, in un elenco di fiducia, cablato nel sistema operativo, nel BIOS, nel TPM). Wallet ed EUDI Wallet lo fanno con elenchi di fiducia che pubblicano wallet provider, PID provider, relying party, fornitori di attestazioni, con le CA e i loro certificati, così che tutti possano convalidare i sigilli: "alla base di tutto c'è una convalida di firme digitali". Il percorso del corso: chiave pubblica, certificati e PKI, servizi fiduciari, identity proofing. (Teams 8 @ 1:48:21-1:51:02)
- **Hardware e politica.** L'hardware crittografico di un iPhone di fascia alta "dall'iPhone 15 in su" resiste agli attacchi molto più di un Android da 100 euro di provenienza incerta; mettere i costruttori nello schema crea un problema politico se si limitano certi servizi (sanitari, psicologici, il voto) ai dispositivi sopra una fascia di prezzo: il criterio si mette sulle caratteristiche di sicurezza certificate, ma il costo della compliance ricade sul cittadino e limita un diritto digitale. Lo stesso problema si pose in Italia per il livello 3 di SPID. (Teams 8 @ 1:51:02-1:55:18)
- **Valutazione finale.** Architettura "fra le più complesse che abbia mai visto", che attraversa tutti i settori di tutti gli Stati: la possibilità che sia tutta sicura "è molto bassa" e gli attaccanti cercano sempre i punti deboli; "professionalmente preoccupato", ma è un progetto "estremamente ambizioso". Il docente non sa se maturerà prima di essere superato da una tecnologia più nuova. (Teams 8 @ 1:53:00-1:56:25)
- **Governance del wallet.** Registri che forniscono certificati a tutti i soggetti; organi di accreditamento, di valutazione della conformità, di vigilanza nazionali (come per i servizi fiduciari qualificati); i nuovi **fornitori di schemi di attributi**, che curano "l'ontologia" del wallet: una laurea a Bologna, con voti in 110 e settori scientifico-disciplinari, deve essere capita dalla Sorbona. (Teams 8 @ 1:56:25-1:58:08)
- **Chiusura.** La lezione si è allungata "per recuperare alcune lezioni che erano state più corte"; bibliografia minima su servizi fiduciari, standard di autenticazione e normativa secondaria di eIDAS 2 sul wallet (i *Commission Implementing Regulation*, di taglio giuridico, comprensibili anche senza background tecnico); di nuovo l'indirizzo dell'EUDI Wallet. (Teams 8 @ 1:58:08-1:59:19)

## 24. Bibliografia

*DI-06 @ 01:45:18-01:46:32*

Il docente lascia riferimenti su crittografia, firme elettroniche, wallet europei e normativa eIDAS, e per chi vuole approfondire gli aspetti quantistici (crittografia post-quantum, algoritmi *quantum safe*, *quantum key distribution*, "per motivi di tempo solo sfiorata", interessante "per chi mastica un po' di più il linguaggio dell'ottica quantistica") testi di base in italiano e in inglese. Poi chiude il corso e chiede se ci sono domande.

**Slide "A very essential bibliography on Cryptography"** (*DI-06 @ 01:46:20*):

- P. Ferragina, F. Luccio, *Crittografia: principi, algoritmi, applicazioni*, Bollati Boringhieri, 2001.
- S. Rubinstein-Salzedo, *Cryptography*, Springer, 2018.
- J. Buchmann, E. Karatsiolis, A. Wiesmaier, *Introduction to Public Key Infrastructures*, Springer, 2013.
- G. Manca, *Le Firme Elettroniche: normative, standard, scenari e modalità di utilizzo*, Themis, 2021.
- EUDI Wallet standards & technical specifications, `https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/`.
- Regulation (EU) №910/2014 ("eIDAS"), as amended by №1183/2024.

*Additional references on Quantum {Mechanics | Computing | Cryptography | Security}:*

- B. Diu, F. Laloë, C. Cohen-Tannoudji, *Quantum Mechanics* (2 volumes), 1991.
- R. Manenti, M. Motta, *Quantum Information Science*, Oxford, 2023.
- V. Kasirajan, *Foundations of Quantum Computing: theory and practice*, Springer, 2021.
- E. Filoramo, A. Giovannini, C. Pasquero, *Alla scoperta della crittografia quantistica*, Bollati Boringhieri, 2006.
- R. Wolf, *Quantum Key Distribution*, Springer, 2021.
- K. Shannon, E. Towe, O. Tonguz, 'On the use of quantum entanglement in secure communications: a survey', arXiv, 2003, `https://arxiv.org/abs/2003.07907`.
- S. Pirandola, 'Quantum Cyber-Security', arXiv, 2020, `https://arxiv.org/abs/1906.01645`.

> **Correzione:** l'identificativo arXiv 2003.07907 indica marzo **2020** (formato AAMM.numero), non il 2003 della slide. Il manuale di meccanica quantistica è di solito citato come Cohen-Tannoudji, Diu, Laloë.

Nel 2026 la bibliografia è annunciata a voce (Teams 8 @ 1:58:08) ma, senza slide, non è leggibile: la descrizione (servizi fiduciari, standard di autenticazione, atti di esecuzione eIDAS 2 sul wallet) è diversa da quella del 2025, che comprende anche la parte quantistica.

## 25. Glossario

| Termine | Significato nel corso |
|---|---|
| Identity proofing | Fase iniziale, una tantum, in cui si accerta l'identità reale e si assegnano i fattori di autenticazione; in italiano identificazione elettronica, nel commercio onboarding |
| IAL1/2/3 | Livelli di identity assurance di NIST SP 800-63A |
| KYC | *Know your customer*: profilazione commerciale del cliente che parte dall'onboarding |
| Re-proofing | Ripetizione dell'identity proofing (scadenza del documento, dubbi sull'identità) |
| Fattori di autenticazione | Conoscenza, possesso, inerenza; contano solo se di tipo diverso |
| SCA, dynamic linking | Autenticazione forte del cliente (PSD2) con i dati della transazione dentro il messaggio firmato |
| Identity provider (IdP) | Gestore dell'identità digitale: fa identity proofing e autentica per conto dei service provider |
| Service provider (SP), relying party (RP) | Fornitore del servizio; "parte facente affidamento" in eIDAS |
| Autenticazione centralizzata | Autenticazione per il tramite di un IdP |
| Identità federata | Molti RP eterogenei e/o più IdP legati da relazioni di fiducia |
| Single sign-on | Passare da un servizio a un altro senza riautenticarsi |
| TGT, service ticket | Ticket di Kerberos: biglietto d'ingresso e biglietto per il singolo servizio |
| Delega AD (unconstrained, constrained, RBCD) | Proxying dell'identità di un utente fra due sistemi di un dominio Active Directory |
| Delega | Il delegato opera con la propria identità per nome e per conto del delegante; il sistema traccia entrambi |
| Impersonificazione | Uso delle credenziali altrui: il sistema vede solo il titolare |
| SSI | Self-sovereign identity: l'holder conserva le credenziali e le presenta ai verificatori |
| Issuer, holder, verifier | Emittente, detentore (wallet), verificatore |
| VC, VP | Credenziale verificabile (dall'issuer all'holder), presentazione verificabile (dall'holder al verifier) |
| Selective disclosure | Svelamento selettivo dei soli dati necessari |
| Unlinkability | Impossibilità di collegare presentazioni diverse allo stesso holder |
| DID | Identificatore decentralizzato, diverso per verificatore |
| SAML | Standard XML (OASIS) per asserzioni di autenticazione, con firme XML |
| OAuth 2.0 | Framework di autorizzazione (RFC 6749): client, resource owner, authorization server, resource server |
| Grant, access token | Concessione dell'autorizzazione e token al portatore che la rappresenta |
| OpenID Connect | Strato di autenticazione sopra OAuth 2.0, con token JWT |
| OpenID Federation | Federazione OpenID basata su trust chain verso trust anchor |
| JWT, JWS | JSON Web Token; firma JSON in formato compatto `header.payload.firma` |
| SD-JWT | JWT con selective disclosure: digest firmati più disclosure `[sale, nome, valore]` separate da tilde (RFC 9901) |
| KB-JWT | Key Binding JWT firmato dall'holder per legare la presentazione a sé e al verificatore |
| SPID | Sistema Pubblico di Identità Digitale: federazione di 12 IdP |
| CIE, CieID | Carta d'Identità Elettronica e relativo schema di autenticazione (IdP: Ministero dell'Interno) |
| LoA | Livello di garanzia eIDAS: basso, significativo (sostanziale), elevato; SPID/CIE livelli 1, 2, 3 |
| Aggregatore | Intermediario che porta in SPID/CIE i service provider piccoli (modalità light o full) |
| RAO | Registration authority (anche una PA) convenzionata con gli IdP |
| Attribute authority, EAA provider | Gestore di attributi; in eIDAS 2 fornitore di attestazioni elettroniche di attributo |
| EAA, QEAA, PuB-EAA | Attestazione elettronica di attributo; qualificata; rilasciata da un ente pubblico |
| Fonte autentica | Soggetto che detiene l'attributo |
| PID, PID provider | Dati di identificazione personale e loro fornitore nel wallet (in Italia IPZS) |
| EUDI Wallet | Portafoglio europeo di identità digitale (eIDAS 2, Reg. 2024/1183) |
| IT-Wallet | Sistema italiano di wallet: uno pubblico (app IO, PagoPA) e possibili privati |
| ARF | Architecture and Reference Framework dell'EUDI Wallet |
| Trust list, trusted list provider | Elenco di fiducia dei soggetti dell'ecosistema e loro gestore |
| Root of trust, trust anchor | Radice di fiducia assiomatica su cui si basa tutta la catena |

## 26. Punti incerti

- **Teams 8 @ 0:40:41**: la frase sull'esame per la slide SD-JWT è sintatticamente incerta ("Chi ha un profilo un po' da sviluppatore non ci saranno domande su questa slide"); dal contesto il senso probabile è che non ci saranno domande sui dettagli della slide (per chi non ha un profilo da sviluppatore), ma non è certo.
- **Teams 8 @ 0:42:05**: fra i documenti dell'app IO il docente cita "il permesso di soggiorno" [?]; dubbio di trascrizione e di merito.
- **DI-06 @ 01:24:01**: l'"obbligo per tutti gli Stati membri entro sette anni" di notificare almeno uno schema eID: con eIDAS 1 la notifica era, per quanto noto, facoltativa (era obbligatorio il riconoscimento degli schemi notificati dagli altri, dal 2018); non verificato se l'obbligo di notifica sia stato introdotto da eIDAS 2. La slide di *00:01:08* dice "eIDAS Regulation provides for each MS to notify at least one Eid. scheme".
- **DI-06 @ 01:05:31**: il primo valore della serie 2025 nel grafico SPID è sovrapposto a un altro numero: [illeggibile].
- **Numero di PA in SPID**: slide 2025 ~19,1 mila SP pubblici; a voce nel 2025 "19.000", "la totalità" su "21-22 mila" PA; nel 2026 "più di 16.000" (Teams 8 @ 0:57:07). Privati: ~210 (slide), "intorno ai 250" (Teams 7 @ 0:13:37), "poco più di 200" (Teams 8).
- **DI-06 @ 00:08:27 contro Teams 7 @ 0:15:13**: nel 2025 SPID/CIE escludono il single sign-on tout court, nel 2026 "dal livello due in su".
- **Teams 6 @ 1:20:05**: "la risoluzione è 7810 volte inferiore a quella del cinema" [?]: numero probabilmente mal trascritto.
- **DI-06 @ 00:28:20**: il nome di sito citato come esempio di IA agentica ("internethackm.com"): [?].
- **DI-06 @ 01:08:23**: decreto del 2014 sull'adesione delle PA "rinnovato meno di un mese fa": non verificato.
- **DI-06 @ 00:52:18**: linee guida AgID OpenID Connect "da circa tre anni": non verificato.
- **Teams 8 @ 1:28:50**: il sito "eudi.dev": non verificato.

## 27. Esame

Nella registrazione 2025 (DI-06) **nessuna indicazione d'esame**: la lezione si chiude con la bibliografia e la richiesta di domande. Tutto ciò che il docente dice nel 2026 sull'esame e sul perimetro in questo blocco:

- **Teams 6 @ 1:05:26**: il rapporto fra IA e identità ("ne parleremo") è rimandato "per chi farà il master di secondo livello nel corso dedicato alla cyber intelligence e alle intelligenze artificiali": fuori perimetro.
- **Teams 7 @ 0:32:36**: Kerberos, "non è mia intenzione descrivervi come funziona tecnicamente il protocollo".
- **Teams 7 @ 0:37:36**: OAuth, "non lo vediamo nel dettaglio perché è materia per sviluppatori professionisti".
- **Teams 7 @ 0:41:08**: OpenID Connect, "non ve lo spiego"; **Teams 7 @ 0:43:02** OpenID Federation, "non mi sento di dare per il momento dettagli ulteriori".
- **Teams 8 @ 0:40:31-0:40:46**: slide SD-JWT, "solo per chi ha un po' di dimestichezza con il JSON e con il JSON Web Token... non ci saranno domande su questa slide" (frase incerta, vedi sezione 26).
- **Teams 8 @ 0:40:25**: pseudonimicità, "preferisco non parlare per il momento".
- **Teams 8 @ 0:55:17**: la parte FEA della CIE, "oggi non parleremo di quella parte".
- **Teams 8 @ 1:01:09**: attribute authority di SPID, "non vi parlo" (mai attivate).
- **Teams 8 @ 1:08:53**: modalità tecniche degli aggregatori, "non ritengo sia utile approfondire"; **Teams 8 @ 1:10:04** varianti OIDC di SPID, "non ve le dico".
- **Teams 8 @ 1:16:53**: attributi SPID/CIE, "non ci saranno domande su questi attributi. Non metto domande nozionistiche in cui dovete ricordare a memoria queste caratteristiche, è solo per vostra cultura".
- **Teams 8 @ 1:39:52-1:40:21**: diagramma dei ruoli dell'EUDI Wallet: "non ci saranno domande sulle frecce, sulle caselle"; "**ci potrebbe essere qualche domanda sui ruoli, quello sì**"; "non preoccupatevi se non riuscite a raccapezzarvici".

Indicazione positiva unica: i **ruoli** dell'ecosistema EUDI Wallet (issuer, holder, verifier/relying party, PID provider, fornitori di attestazioni pubblici, qualificati e non qualificati, fonti autentiche, trusted list provider, wallet provider, costruttori di dispositivi, organi di governance). Dal tono generale (domande non nozionistiche) sono centrali i concetti: identity proofing contro autenticazione, autenticazione contro autorizzazione, centralizzata e federata, SSO, delega contro impersonificazione, SSI e privacy (selective disclosure, unlinkability), qualificazione dell'attestazione contro qualificazione dell'attributo, digital trust come fondamento. Per il quadro completo vedi la pagina [Assessment](assessment.md).
