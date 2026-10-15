# 05 - Firme e sigilli elettronici, eIDAS, elenchi di fiducia, formati di firma, JAdES, autenticazione e identity proofing, Kerberos

*DI-05, registrazione Teams del 29/10/2025 (portale, data a schermo "2025-10-29 17:09 UTC"), 1:53:47. Integrazioni da Teams 5 (intera, 0:55:27) e Teams 6 (da 0:00:03 a 1:01:49).*

> **Come leggere questo capitolo.** La lezione 2025 ha due metà. Fino a circa 01:02 tratta i **servizi fiduciari**: firme e sigilli elettronici (semplici, avanzati, qualificati), elenchi di fiducia europei, laboratorio su un PDF con firme qualificate, formati di firma (enveloped, enveloping, detached, sequenziale, parallela), PAdES, JAdES, attacchi. Da circa 01:02 passa all'**identità digitale**: autenticazione e autorizzazione, fattori, biometria e deepfake, identity proofing, livelli di garanzia, smart card, SSO, Kerberos. Le integrazioni Teams 2026 riguardano solo la prima metà: nel 2026 il docente ha ripreso servizi fiduciari e firme in Teams 5 e nella prima ora di Teams 6, aggiungendo PEC, marca temporale, registri distribuiti, ASiC e controfirma (sezione 13). Le integrazioni 2026 su identità digitale e autenticazione sono nel **capitolo 06**. Le parti su PKI, certificati X.509, CRL, OCSP, HSM e *sole control* sono nel capitolo 04; la crittografia di base nel capitolo 01 e nella guida [Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/README.md) (capitolo 07).

## Indice

1. Riepilogo: servizi fiduciari qualificati e non qualificati
2. Firma digitale e firma elettronica: la tassonomia
3. Il sigillo elettronico e la persona giuridica
4. "Firma digitale" in Italia: il DPCM firme e la confusione dei termini
5. Firme e sigilli avanzati e qualificati
6. Elenchi di fiducia: EUTL, LOTL e Brexit
7. Laboratorio: un PDF con due firme qualificate e il certificato qualificato
8. Formati di firma: enveloped, enveloping, detached
9. Firme multiple: sequenziali, parallele, controfirma
10. Formati AdES, PAdES e l'attacco di signature wrapping
11. Firmare JSON: JWT, JWS e JAdES
12. Attacchi agli schemi di firma e cifratura
13. Novità 2026: PEC, marca temporale, registri distribuiti
14. Autenticazione e autorizzazione
15. I fattori di autenticazione
16. Inerenza, biometria e presentation attack
17. Digital twin e deepfake
18. Identity proofing
19. Standard e regolamenti dell'identità digitale: NIST SP 800-63 e livelli di garanzia eIDAS
20. Autenticazione locale e client/server
21. Autenticazione con smart card
22. Single sign-on, riautenticazione e PIN dispositivo
23. Kerberos
24. Glossario
25. Punti incerti
26. Esame

## 1. Riepilogo: servizi fiduciari qualificati e non qualificati

*DI-05 @ 00:00:02*

Il docente riparte dalla lezione precedente (capitolo 04): i servizi fiduciari si distinguono in **qualificati** e **non qualificati**. Tutti i fornitori di servizi fiduciari sono comunque registrati presso l'**organo di supervisione nazionale** (ogni Stato membro ne ha uno), ma quelli che si qualificano devono sottostare a un numero maggiore di controlli di sicurezza amministrativa, fisica e logica, e a un **regime di vigilanza**: al momento dell'ingresso e poi **almeno ogni due anni** devono far effettuare un'analisi di conformità da un ente indipendente, a sua volta certificato e accreditato presso l'organo nazionale. In caso di problemi di sicurezza hanno obblighi ulteriori, anche perché i prestatori di servizi fiduciari qualificati rientrano nella **direttiva NIS 2** fra i soggetti essenziali: i loro servizi, quando qualificati, hanno valore in tutta l'Unione e richiedono un regime di cybersicurezza aumentato (*DI-05 @ 00:00:36-00:01:41*).

> **Nota aggiunta:** il controllo biennale è l'art. 20(1) del Reg. (UE) 910/2014: i QTSP sono sottoposti "almeno ogni 24 mesi" a una verifica da parte di un organismo di valutazione della conformità. Nella NIS 2 (Dir. (UE) 2022/2555) i prestatori di servizi fiduciari qualificati sono nell'allegato I (infrastrutture digitali) e sono soggetti essenziali indipendentemente dalle dimensioni; il termine della direttiva è "soggetti essenziali", non "fornitori di servizi essenziali" (che era la terminologia della prima NIS).

Firme e sigilli, come gli altri servizi fiduciari, possono essere qualificati o no, ma hanno anche un **livello intermedio**: firma elettronica **avanzata** e sigillo elettronico **avanzato**. Precisazione: la firma e il sigillo di per sé **non sono** servizi fiduciari; sono servizi fiduciari la **creazione** di una firma o di un sigillo, la **conservazione** di un certificato fatto per creare firme o sigilli, la **convalida** di una firma o di un sigillo su un documento (*DI-05 @ 00:01:41-00:02:13*).

I prestatori qualificati possono fregiarsi di un **marchio** (il *trust mark*) che identifica il prestatore o il servizio qualificato. Il marchio ha una normativa secondaria, ma "è solo un marchio": è un'immagine, e come tale può essere contraffatto (*DI-05 @ 00:02:13*).

**Slide "eIDAS Regulation (2024, 2014)"** (*DI-05 @ 00:00:04*, versione completa *00:02:04*). A sinistra un ciclo di icone: *e-attestation of attribute(s)*, *e-archival*, *e-ledger*, *e-registered delivery service (eRDS)*, *e-time stamp*, *e-seal*, *remote e-signing/sealing + their validation*, *e-signature*, *web-authentication certificate (WAC)*, *notified eID schemes and EUDIW Framework*. Testo:

> PKIs are the technical bread-and-butter for market solutions offered by trust service providers (eTSPs).
>
> Trust services can be *qualified*: the eTSP providing them not only accredits itself to a MS' national eIDAS supervisory body (AgID for Italy), but also undergoes regular supervision in order to assure a highest and EU-harmonised level of digital trust.
>
> *Qualified* trust service providers (QTSPs) are listed in national trust lists freely available online at EC's website:

Nella versione a *00:02:04* compaiono in basso tre icone: *(simple) electronic signature / seal*, *Advanced electronic signature / seal*, *Qualified electronic signature / seal*.

### Integrazione Teams 2026 (lezione 5 2026)

*Sezione 1 (regolamento eIDAS, fonti normative, servizi fiduciari, qualifica): nel 2026 Teams 5 introduce da zero i servizi fiduciari*

- **Il regolamento.** Reg. (UE) 910/2014, "eIDAS". Essendo un regolamento, come il GDPR, si applica direttamente in tutta l'Unione senza recepimento; le leggi nazionali sono fonte secondaria e non possono contraddirlo; dipendono dagli Stati solo gli aspetti che il regolamento stesso demanda (per esempio la vigilanza sui QTSP). Nel 2024 è stato **integrato, non sostituito**, dal regolamento comunemente detto "eIDAS 2": si continua a citare il 910/2014 nel testo vigente. (Teams 5 @ 0:00:56-0:03:21)
- **Fonti italiane.** Il **DPCM 22 febbraio 2013** ("DPCM firme") norma gli aspetti che eIDAS demanda agli Stati e quelli che non tratta; prima del 2014 normava le "firme digitali" in senso legale, che il docente chiama "firme digitali **ex DPCM firme**" per distinguerle da quelle tecniche. Dopo eIDAS gli sono state tolte le parti ormai normate a livello europeo. Poi il **D.Lgs. 7 marzo 2005, n. 82**, Codice dell'Amministrazione Digitale (**CAD**), e le **linee guida AgID**, organo di accreditamento e vigilanza sia per le identità digitali sia per i servizi fiduciari (fra le più importanti: formazione, gestione e conservazione del documento informatico; regole tecniche sui certificati qualificati). Le firme qualificate di eIDAS sono "di bandiera italiana": derivano in gran parte dalla normativa italiana preesistente, confluita nel regolamento. (Teams 5 @ 0:02:17-0:08:37)
- **Fuori dall'UE.** Islanda, Liechtenstein e Norvegia (Spazio economico europeo) adottano eIDAS e compaiono nella trust list europea. Regno Unito: Electronic Communications Act 2000, poi dopo la Brexit un proprio regolamento del 2016 chiamato anch'esso eIDAS (l'"eIDAS britannico"); non esiste un accordo bilaterale di mutuo riconoscimento con l'UE, né, per quanto sa il docente, con nessun paese extraeuropeo, benché eIDAS lo preveda. USA: legge federale **E-SIGN** del 2000, più leggi statali e l'Uniform Electronic Transactions Act, con un approccio diverso da eIDAS. Svizzera, Canada, Australia, Nuova Zelanda hanno normative di fine anni '90 e inizio 2000, senza mutuo riconoscimento. L'Italia "si contende con la Malesia" il primato di prima legge al mondo (1997) a dare valore legale certo ad alcune firme digitali. (Teams 5 @ 0:08:37-0:12:51)
- **Consiglio operativo.** Con giuristi e amministrativi "firma digitale" significa firma elettronica qualificata; con matematici, crittografi, informatici significa la cifratura di un'impronta con una chiave privata. Meglio dire "firma elettronica qualificata" quando si intende il massimo valore probatorio, "firma digitale" per quella tecnica, e chiarirsi comunque prima. (Teams 5 @ 0:12:51-0:14:40)
- **I servizi fiduciari** del diagramma a cerchio, in senso orario: archiviazione elettronica, registro elettronico distribuito, recapito certificato elettronico, validazione temporale elettronica, sigillo elettronico, firma elettronica. eIDAS 2 ha introdotto la specie **remota** di firma e sigillo e, per ciascuna, il servizio che fornisce il certificato X.509, quello che convalida e quello che conserva. Non rappresentati: certificati di autenticazione di sito web, attestazione elettronica di attributi (ecosistema dei wallet). eIDAS è un regolamento "bifronte": metà tratta identificazione elettronica, schemi eID e wallet europeo; l'altra metà i servizi fiduciari. Tutti si basano tecnicamente su firme digitali a garanzia di integrità e autenticità. (Teams 5 @ 0:14:48-0:18:11)
- **Registrazione e qualifica.** Per offrire servizi fiduciari basta registrarsi presso l'autorità nazionale (AgID per l'Italia) e impegnarsi a notificare incidenti cyber e violazioni di dati personali entro un termine: nessun altro controllo. Chi si **qualifica** subisce una vigilanza *ex ante* (accreditamento, con assessor terzi che valutano sicurezza fisica, tecnica e amministrativa rispetto a requisiti minimi europei), poi vigilanza continua dell'organo nazionale e, per incidenti con impatti extraterritoriali, degli altri organi europei e della Commissione, e un nuovo assessment **ogni due anni** o quando serve. eIDAS è "una carta dei diritti" del servizio fiduciario: ai servizi non qualificati non garantisce alcun valore probatorio a priori né transfrontaliero (possono farlo le leggi nazionali); a quelli qualificati, finché restano tali, garantisce lo stesso valore in tutta l'Unione. (Teams 5 @ 0:18:14-0:24:18)
- **Il marchio di fiducia UE**: lucchetto azzurro con spunta gialla e stelle dell'Unione; è un'immagine e da sola non garantisce nulla, ma se usata legittimamente indica un servizio qualificato. (Teams 5 @ 0:28:02-0:28:28)
- **Il modello fiduciario.** Un primo soggetto (persona fisica o giuridica) produce dati di cui un secondo soggetto deve fidarsi (autenticità e integrità); entrambi si affidano a un terzo, il prestatore di servizi fiduciari ("testimone elettronico", "notaio elettronico"), che fornisce una PKI: ad Alice un dispositivo di creazione della firma (anche remoto), a Bob il certificato per verificare. Con un QTSP il modello vale in tutta l'Unione, qualunque sia lo Stato del prestatore. (Teams 5 @ 0:28:32-0:33:11)

> **Correzione:** a Teams 5 @ 0:01:13 il docente scioglie eIDAS come "Electronic identification and advanced signing". L'acronimo ufficiale è **electronic IDentification, Authentication and trust Services**.

> **Nota aggiunta:** eIDAS 2 è il Reg. (UE) 2024/1183 dell'11 aprile 2024, in vigore dal 20 maggio 2024, che modifica il 910/2014 (lo stesso URL `eur-lex.europa.eu/eli/reg/2024/1183/oj` compare nella slide di *DI-05 @ 01:22:23*). Le prime norme italiane sono la L. 59/1997 (art. 15, "Bassanini", citata dal docente a Teams 5 @ 0:33:42 con un "se non erro") e il DPR 513/1997. Sul primato: la Malesia ha il Digital Signature Act 1997, ma lo Utah aveva già una legge sulla firma digitale nel 1995 (statale, non nazionale); il "primato" dipende da come lo si conta. L'eIDAS britannico è lo SI 2016/696 (Electronic Identification and Trust Services for Electronic Transactions Regulations 2016).

## 2. Firma digitale e firma elettronica: la tassonomia

*DI-05 @ 00:02:57*

Nel corso "firma digitale" va **sempre** interpretata come **processo tecnico**: la cifratura, con la chiave privata del firmatario, dell'impronta crittografica dell'evidenza informatica. In formula: A è la firma digitale di B se, fissati gli algoritmi di hashing e cifratura, si ottiene A calcolando l'impronta di B e cifrandola con la chiave privata del firmatario:

$$A = \mathrm{Enc}_{\kappa^{\text{priv}}}\big(H(B)\big)$$

È un processo tecnico realizzabile in tantissimi modi (algoritmi diversi) e **di per sé non ha alcun valore legale**, perché può essere fatto in modo sicuro o insicuro (*DI-05 @ 00:03:28*).

Il regolamento **eIDAS** parla invece di **firme elettroniche** e **sigilli elettronici**. Tecnicamente entrambi si realizzano con firme digitali, ma la definizione è diversa: quella di firma digitale è tecnica (algoritmo, cifratura, impronta); quella di firma elettronica è scritta "in legalese" in un regolamento europeo e volutamente **non si riferisce a tecnologie**, perché domani, per esempio con la crittografia post-quantistica, le firme elettroniche potrebbero non essere più fatte con una firma digitale (*DI-05 @ 00:04:10-00:04:47*).

**Slide "Digital vs electronic signing: a taxonomy"** (*DI-05 @ 00:02:57*; nel titolo i due membri sono separati da un trattino, reso qui con i due punti). Testo:

> In the context of the present class, digital signing/signature means the technical process of encrypting the hash of a digital message/document via a signer's private key.
>
> The **eIDAS Regulation** defines several things, each with precise legal meanings uniformed across the EU, which *may* be technically realized as *digital* signatures:
> - *electronic* **signature**: «data in electronic form which is attached to, or logically associated with, other data which is **used by the signatory to sign**» (**signatory** is a **natural** person);
> - *electronic* **seal**: «data in electronic form attached to, or logically associated with, other data which is **used to ensure** the latter's **origin and integrity**» (**seal creator** is a **legal** person).
> - **advanced e-signature/seal**: an *e-signature/seal* with strict additional requirements.
> - *qualified* **e-signature/seal**: an *advanced e-s./s.* issued by a ***Q*TSP** by means of *qualified* certificates.
>
> Please note that Italian bylaws define a "***firma digitale***" as an e-signature explicitly based on public-key cryptography, pursuant to DPCM 2013 (so called "*DPCM firme*"), which currently and effectively corresponds to a species of *qualified* e-signature (more later). However, latter meaning for *firma digitale* shall never be meant throughout this class and shall no longer be used here.

(Nella slide le voci dell'elenco sono separate dal termine con un trattino lungo, reso qui con i due punti.)

> **Nota aggiunta:** le definizioni citate sono quelle dell'art. 3 del Reg. 910/2014: n. 10 (firma elettronica), n. 9 (firmatario: "una persona fisica che crea una firma elettronica"), n. 25 (sigillo elettronico), n. 24 (creatore di un sigillo: "una persona giuridica che crea un sigillo elettronico").

### La firma elettronica e l'email "firmato Walter Arrighetti"

*DI-05 @ 00:05:23*

La prima parte della definizione ("dati associati, anche solo logicamente, ad altri dati") si segue anche da tecnici: è la questione della firma *detached* o *enveloped* (sezione 8). La seconda parte è giuridica: i dati sono usati **dal firmatario per firmare**, e il firmatario è una **persona fisica**. Ciò che rende qualcosa una firma elettronica è l'idoneità a dimostrare l'**intenzione** di una persona fisica di sottoscrivere (*DI-05 @ 00:05:58*).

Domanda alla classe: un'email di solo testo ad Alice, "Ciao Alice, ci vediamo domenica alle 8.30, firmato Walter Arrighetti". La scritta "Walter Arrighetti" è una firma elettronica? Lo stesso esempio era stato usato parlando di phishing (guida Cybersecurity, capitolo 04, sezione 8). Una studentessa risponde di no. La risposta personale del docente è **sì**: ci si deve attenere alla definizione. La risposta "vera" è che il regolamento eIDAS dice che spetta a un **giudice** stabilire caso per caso se qualcosa sia una firma elettronica; lo dice per quasi tutti i servizi fiduciari, quindi anche per sigillo e marcatura temporale (*DI-05 @ 00:07:06-00:07:46*).

Ma il regolamento dice anche che a una firma elettronica, "anche una sedicente firma elettronica", **non può essere negato valore giuridico solo perché elettronica**. È scritto in un regolamento europeo, quindi "pesa esattamente quanto ogni articolo del GDPR" (*DI-05 @ 00:07:46-00:08:18*). Chiunque avrebbe potuto scrivere quell'email (un criminale, magari con indirizzo falsificato): il giudice deciderà sugli elementi probatori del caso, ma non potrà mai dire "è scritta in un'email, quindi non vale" (*DI-05 @ 00:09:00-00:10:01*). Il regolamento non dice quali siano gli elementi per stabilirlo, perché i casi sono troppi e una definizione tecnica in un testo legislativo rischierebbe di essere superata "il giorno dopo" (*DI-05 @ 00:10:01*).

Conseguenza pratica: un documento con firma elettronica si può rifiutare, ma **non** con la sola motivazione che la firma è elettronica. Il rifiuto deve essere motivato, per esempio da una norma che impone per quel documento una firma di un certo tipo (avanzata o qualificata: nel Codice Civile ci sono articoli che richiedono la qualificata e altri per cui basta l'avanzata), o da un contratto in cui ci si è impegnati a firmare con firma autografa o qualificata. Non può bastare la volontà di qualcuno che "per sua naturale scelta" non accetta quella firma (*DI-05 @ 00:10:33-00:12:50*). Lo stesso vale per i sigilli.

> **Nota aggiunta:** il principio è l'art. 25(1) del Reg. 910/2014 (per le firme), l'art. 35(1) (per i sigilli) e l'art. 41(1) (per le validazioni temporali); che la valutazione spetti al giudice è detto nel considerando 22 ("spetta al diritto nazionale definire gli effetti giuridici") e, per l'Italia, nell'art. 20 c. 1-bis del CAD (documento informatico "liberamente valutabile in giudizio").

### Integrazione Teams 2026 (lezione 5 2026)

*Sezione 2 (definizioni di firma elettronica semplice)*

- La firma elettronica "normale" è detta, "con una forzatura della tassonomia", **semplice**. Nella definizione non c'è alcun riferimento alla crittografia né all'integrità o autenticità: una firma elettronica **può non essere basata sulla crittografia**. È la rappresentazione elettronica della firma fisica: "firmiamo per firmare", "sembra una tautologia, ma è così". (Teams 5 @ 0:24:18-0:24:35, 0:33:50-0:35:15)
- Esempio 2026: email da mario.rossi con "baci Mario Rossi": astrattamente una firma, ma chiunque (anche "Valeria Bianchi" alla tastiera, o "l'attore statuale dietro l'angolo" con un indirizzo falsificato) può scriverlo. Sono firme elettroniche anche le **spunte** con cui si accettano i termini di un servizio online; ci sono cause in cui il cliente sostiene di aver cliccato senza leggere. (Teams 5 @ 0:37:05-0:39:09)
- Il docente cita una sentenza della **Corte di Cassazione del 2026** secondo cui per le **clausole vessatorie** non basta una spunta: serve una firma specifica, proprio per evitare che chi spunta non legga. (Teams 5 @ 0:39:18-0:40:12)
- Motivazioni di rifiuto legittime: "non so stabilire se è davvero la firma di Mario Rossi" (per esempio un'immagine JPEG di un autografo illeggibile); "il mio archivio è solo cartaceo". Non legittima: "la voglio cartacea" senza altro motivo. Il docente precisa di non essere un giurista. (Teams 5 @ 0:25:46-0:27:43)

> **Nota aggiunta:** gli estremi della sentenza di Cassazione 2026 sulle clausole vessatorie non sono stati detti e non sono stati verificati. Il principio richiamato (doppia sottoscrizione specifica delle clausole vessatorie, artt. 1341-1342 c.c.) è comunque quello consolidato.

## 3. Il sigillo elettronico e la persona giuridica

*DI-05 @ 00:13:20*

Anche il **sigillo elettronico** si realizza con firme digitali (cifratura di un'impronta con la chiave privata di qualcuno), ma la sua definizione è: dati in forma elettronica, attaccati o logicamente associati ad altri dati, **usati per assicurare l'origine e l'integrità** dei primi. "Origine e integrità vi ricorda qualcosa? A me sì, a me ricorda la firma digitale": la convalida di una firma digitale verifica che il documento sia integro e **autentico**, e l'autenticità è la capacità di stabilire l'origine del dato (triade del digital trust, capitolo 01). Il creatore del sigillo, cioè il titolare del certificato di sigillo, è una **persona giuridica** (*DI-05 @ 00:13:53-00:14:23*).

L'esempio del **contratto con l'operatore telefonico** (*DI-05 @ 00:14:53*): un contratto, per il diritto italiano, europeo e internazionale, deve essere sottoscritto da **persone fisiche** con potere di firma (maggiorenni non dichiarati inabili) che esprimono la volontà di sottoscrivere; solo così è impugnabile. Di solito ci sono due firme di persone fisiche, parte e controparte: in regime eIDAS almeno due firme elettroniche. Una firma digitale il cui certificato indica come titolare "TIM S.r.l." (il docente poi corregge "non voglio fare pubblicità", e passa a Fastweb) **non è una firma elettronica**: al più è un **sigillo elettronico**, utile a chiunque per verificare che quel contratto sia davvero uscito da quell'azienda e sia integro, convalidando il certificato (valido, non scaduto, non revocato, emesso da una CA che attesta che il titolare è l'azienda). Per questo sotto un contratto con un'azienda c'è sempre il nome di un dirigente con potere di firma (*DI-05 @ 00:15:28-00:17:07*).

In un documento possono convivere **firme elettroniche** di chi sottoscrive e **sigilli elettronici** apposti per esempio da chi ha generato tecnicamente il file, per consentire di verificarne integrità e autenticità anche prima che qualcuno lo firmi (*DI-05 @ 00:17:07-00:17:38*).

### Integrazione Teams 2026 (lezione 5 2026)

*Sezione 3 (sigillo elettronico)*

- Il sigillo è apposto da una persona giuridica: pubblica amministrazione, impresa, ma anche un **libero professionista** quando agisce professionalmente (un ingegnere, un avvocato che esprime un parere), per attestare integrità e autenticità di ciò che produce. A differenza della firma, nella definizione di sigillo compare esplicitamente il riferimento a integrità e autenticità, ma non che sia realizzato con la crittografia. (Teams 5 @ 0:35:15-0:36:49)

> **Nota aggiunta:** l'esempio del professionista è del docente; nel Reg. 910/2014 il creatore di sigillo è definito come persona giuridica (art. 3 n. 24) e un professionista persona fisica di norma firma con una firma elettronica.

## 4. "Firma digitale" in Italia: il DPCM firme e la confusione dei termini

*DI-05 @ 00:17:38*

Uno studente aveva scritto in chat di pensare che la firma digitale "fosse quella con l'OTP". C'è "grande, grande confusione" nei termini, e nasce dal legislatore europeo che nel 2014 ha dato a oggetti giuridici un nome similissimo a quello che da 30 anni tecnici e crittografi davano alla firma digitale. Fuori dall'Italia, se si parla di firma digitale, o si pensa che si sia confuso "digitale" con "elettronico", o si capisce che si parla della cosa tecnica (*DI-05 @ 00:18:08-00:18:38*).

In Italia è "ancora più grave": siamo stati fra i primi paesi al mondo a dare riconoscimento giuridico alle firme digitali, con norme di fine anni '90. Il documento istitutivo, ancora parzialmente in vigore (gli sono stati tolti gli articoli confluiti in eIDAS, che come regolamento prevale sulla norma nazionale), chiamò **firma digitale** un oggetto giuridico basato su chiavi pubbliche e private, ma che **non è una qualunque firma digitale** (*DI-05 @ 00:18:38-00:19:59*). L'esempio di **Pierino**: la firma fatta con OpenSSL, con un certificato autofirmato, su un computer protetto dalla password `temp123`, con antivirus non aggiornato e collegato a qualunque rete, non può avere valore legale; basterebbe un errore di Pierino su un carattere della chiave privata per invalidare le firme (*DI-05 @ 00:19:59-00:20:31*).

La "firma digitale" del **DPCM firme** del 2013 è quindi "un'altra cosa ancora". Per fortuna chi ha scritto il DPCM ha anche partecipato in Commissione europea alla stesura di eIDAS (il docente dice di aver lavorato con alcuni di loro): oggi la firma digitale ex DPCM è di fatto una **specie italiana di firma elettronica qualificata**, e i prestatori di firma qualificata in Italia fanno lo stesso mestiere di prima del 2014 (*DI-05 @ 00:20:31-00:21:40*). Il termine resta perché esistono documenti firmati con certificati antecedenti a eIDAS (all'epoca i certificati duravano, "mi pare", al massimo 10 anni) che avranno effetto per decenni (*DI-05 @ 00:21:40*). Con un amministrativo italiano "firma digitale" significa quasi certamente FEQ italiana; i prestatori di firma digitale ex DPCM coincidono con i prestatori qualificati del 2014 (*DI-05 @ 00:22:10-00:22:40*).

L'invito del docente: sapere che questa definizione esiste, per capirsi con gli amministrativi, ma usare "firma digitale" **solo per il processo tecnico** (estrarre l'impronta e cifrarla con la chiave privata per verificare integrità e autenticità), senza alcuna presunzione di valore legale (*DI-05 @ 00:22:40-00:23:10*). Anche i gestori di firme qualificate nelle pubblicità televisive parlano di "firma digitale", un termine che "vuol dire almeno tre cose distinte" (*DI-05 @ 00:30:05*).

Sull'OTP (*DI-05 @ 00:28:28-00:30:05*): un'azienda che fornisce firme qualificate non vende necessariamente solo dispositivi qualificati. L'azienda citata dallo studente, a quanto ricorda il docente, vende in Italia sia dispositivi di firma qualificata (con i requisiti di sicurezza richiesti da AgID) sia, per chi vuole spendere meno, dispositivi non qualificati associati a HSM e CA con livelli di protezione inferiori. Una firma con OTP, se non è qualificata, magari rientra ancora fra le firme avanzate.

> **Nota aggiunta:** il documento istitutivo a cui allude il docente è il DPR 10 novembre 1997, n. 513, poi confluito nel DPR 445/2000 e quindi nel CAD (D.Lgs. 82/2005), dove la "firma digitale" è definita all'art. 1 c. 1 lett. s come "un particolare tipo di firma qualificata basata su un sistema di chiavi crittografiche". Il DPCM firme è il DPCM 22 febbraio 2013.

## 5. Firme e sigilli avanzati e qualificati

*DI-05 @ 00:23:10*

**Avanzati.** Per eIDAS firme e sigilli avanzati hanno una validità legale che dipende ancora da un giudice, ma può essere stabilita da un regolamento, e devono soddisfare requisiti che sono quelli di sicurezza visti per tutto il corso: ci si deve poter fidare della CA che emette i certificati di firma o sigillo avanzato, quindi le chiavi private sono protette (capitolo 04) e il fornitore, anche non qualificato, deve avere le caratteristiche di sicurezza che il regolamento specifica in un'appendice. Sono "una variante più professionale" (*DI-05 @ 00:23:41-00:24:13*). Se sia una firma elettronica l'email "firmato Walter Arrighetti" lo decide un giudice; che **non** sia una firma avanzata non ha bisogno di un giudice, perché chiunque potrebbe mandarla (*DI-05 @ 00:24:44*).

In Italia le FEA sono accettate da tutta la pubblica amministrazione quando riconosciute da norme specifiche. Esempio: la firma che ogni cittadino con **CIE** ha gratuitamente con l'app **Firma con CIE** è una firma elettronica avanzata, opponibile in Italia perché tutte le PA la riconoscono; di fatto dovrebbero riconoscerla anche i privati, anche se spesso è più complicato (*DI-05 @ 00:24:44-00:25:51*). Due o tre cose, specificate in articoli del Codice Civile, non si possono fare con la FEA: "non potete vendere la casa con una firma elettronica avanzata. C'è ancora bisogno del notaio" (*DI-05 @ 00:25:51*).

**Qualificati.** Il valore legale completo si ha con firma e sigillo **qualificati**, prodotti da un prestatore qualificato: qui non c'è più distinzione fra Italia e resto d'Europa, hanno pieno valore legale in tutta l'Unione. Il **sigillo qualificato** permette a chiunque di verificare in modo inoppugnabile integrità e autenticità di un documento: nessuno può rifiutarsi di verificarlo (*DI-05 @ 00:26:22*). La firma ha "una cosa in più": il regolamento dice che è analoga in tutto e per tutto alla **firma autografa**, e che spetta al **titolare** dimostrare che non è sua: l'**inversione dell'onere della prova** (*DI-05 @ 00:26:53*). Con una firma avanzata, se nessuna legge la impone (come nel caso della CIE), chi la rifiuta deve motivare, ma non può opporre come unica motivazione il fatto che è elettronica. Con una firma **qualificata** il documento ha i valori probatori di una firma autografa, "è come se aveste firmato con la vostra mano sulla carta", e se qualcuno dubita dell'autenticità spetta al titolare dimostrarlo: per esempio dimostrare di aver dato il PIN a qualcuno o che in quel momento il dispositivo di firma era nel controllo di qualcun altro. "Non basta che lo dite" (*DI-05 @ 00:27:24-00:28:31*).

> **Correzione:** a *DI-05 @ 00:26:53* il docente dice "la firma elettronica **avanzata** ha una cosa in più ... è analoga in tutto e per tutto alla firma autografa"; dal contesto (subito prima parla del sigillo qualificato, subito dopo della firma qualificata) intende la firma elettronica **qualificata**. L'equivalenza alla firma autografa a livello europeo è l'art. 25(2) del Reg. 910/2014 e vale solo per la firma qualificata.

> **Nota aggiunta:** in Italia la presunzione è nell'art. 20 c. 1-ter del CAD: l'utilizzo del dispositivo di firma qualificata o digitale "si presume riconducibile al titolare, salvo che questi dia prova contraria". Per il sigillo qualificato eIDAS prevede una presunzione diversa (art. 35(2)): presunzione di integrità dei dati e di correttezza della loro origine, non equivalenza a una sottoscrizione.

### Integrazione Teams 2026 (lezione 5 2026)

*Sezione 5 (FEA: requisiti europei e normativa italiana)*

- In Italia si usa l'acronimo **FEA**, che non esiste nel resto d'Europa. Come la semplice, la FEA è **liberamente valutabile in giudizio**, salvo norme nazionali che le diano valori specifici (come in Italia). La slide su questa parte è in italiano perché tratta normativa nazionale. (Teams 5 @ 0:42:05-0:43:02)
- **I quattro requisiti** della firma (e, *mutatis mutandis*, del sigillo) avanzata: (1) **connessa unicamente** al firmatario; (2) **idonea a identificarlo**: non basta "Mario Rossi", serve il **codice fiscale**; per il sigillo non basta "Acme S.r.l.", serve partita IVA, codice fiscale, codice IPA per le PA o un identificativo in un registro nazionale (Agenzia delle Entrate, registro delle imprese italiano, francese, lussemburghese...) che permetta di rintracciare legalmente il soggetto; (3) creata con **dati per la creazione** (in pratica la chiave privata) sotto il **controllo esclusivo** del firmatario, il *sole control*: solo Alice ha PIN, password, codice o biometria per usare tramite HSM la propria chiave privata, da cui il **non ripudio**; (4) collegata ai dati in modo da **rilevare ogni modifica successiva**: cambiare un solo bit di documento o firma fa fallire il confronto fra l'hash calcolato dal verificatore e quello decifrato dalla firma. (Teams 5 @ 0:43:02-0:46:48)
- Se un giudice stabilisce che i quattro requisiti sono soddisfatti, la firma ha il rango di FEA; questo permette alle leggi nazionali sulla FEA di applicarsi. Il **DPCM firme, art. 56**, descrive caratteristiche e obblighi dei prestatori che offrono FEA, compresi obblighi di trasparenza verso i clienti e modalità semplificate per PA e sanità. (Teams 5 @ 0:46:48-0:48:08)
- **Firma grafometrica**: la firma sul tablet in banca o in ospedale è una specie di FEA; la prima firma serve al fornitore per generare un certificato solo per voi, con cui si appongono le firme successive, riconosciute contrattualmente come FEA. Fino a un contenzioso le parti sono tutelate; in contenzioso decide il giudice. Le soluzioni sono vendute da fornitori registrati presso l'organo di vigilanza, non fatte dalla banca o dall'ospedale. (Teams 5 @ 0:48:08-0:49:53)
- **DPCM firme, art. 61**: sono FEA per legge, senza bisogno di un giudice, (a) l'invio di messaggi **PEC** conservati insieme alla **ricevuta completa** di consegna, perché l'identità del mittente è garantita dal gestore PEC (oggi un prestatore di servizi di recapito certificato ai sensi di eIDAS); (b) le firme con la **CIE** (la seconda chiave privata della carta, vista in Teams 4), con la **tessera sanitaria/CNS** abilitata (in alcune regioni il PIN si ritira al CUP), con alcune smart card di dipendenti pubblici e della Difesa. (Teams 5 @ 0:49:57-0:52:48)
- **Art. 21, comma 2-bis** (CAD): in Italia la FEA equivale alla firma autografa e può sottoscrivere qualunque documento pubblico o scrittura privata, **salvo** gli atti dell'**art. 1350 c.c., numeri 1-12** (il 13 è la clausola residuale): in sostanza quelli che richiedono la firma autenticata da un pubblico ufficiale, come le compravendite. Solo in Italia. (Teams 5 @ 0:52:48-0:54:10)
- **FEQ**: equiparata alla firma autografa a livello **europeo**. È una FEA con due caratteristiche in più: creata con un **dispositivo qualificato** di creazione della firma (o del sigillo), con certificazioni di cybersicurezza e controlli fisici, logici e amministrativi che danno un'ulteriore prova tecnica del controllo esclusivo; basata su un **certificato qualificato**. (Teams 5 @ 0:54:10-0:55:27)

> **Correzione:** la trascrizione automatica rende l'acronimo italiano della firma qualificata come "FEC" e "FAQ"; l'acronimo corretto è **FEQ** (firma elettronica qualificata).

> **Nota aggiunta:** il testo dell'art. 21 c. 2-bis CAD dice che le scritture dell'art. 1350 nn. 1-12, se fatte con documento informatico, vanno sottoscritte **a pena di nullità con FEQ o firma digitale**, mentre per il n. 13 basta anche la FEA. La FEQ quindi soddisfa la forma scritta anche per una compravendita immobiliare; per la trascrizione nei registri immobiliari serve comunque l'autenticazione (notaio). Questo concilia l'affermazione 2025 ("con la FEA non vendete la casa") con quella di Teams 6 @ 0:15:35 ("anche in Italia la FEQ è sufficiente"). L'art. 61 del DPCM, sul punto PEC, limita l'effetto ai rapporti "nei confronti della pubblica amministrazione": il docente non lo precisa (testo non riletto in questa sede).

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 5 (FEQ: dispositivo qualificato, certificato qualificato, validità nel tempo, valore omogeneo)*

- **QSCD.** Il dispositivo sicuro di creazione della firma (SSCD), per la FEQ, deve essere **qualificato** (QSCD): criteri di cybersicurezza che rendono impossibile estrarre la chiave privata, anche al QTSP che lo emette, il quale non deve poterla conoscere né usare. Eccezione: copie di backup. Chi perde il QSCD non può chiederne un duplicato: gli viene dato un nuovo dispositivo con una nuova chiave. Vale anche quando il QSCD è un HSM remoto nel data center del QTSP. È in preparazione uno schema europeo di certificazione ai sensi del **Cybersecurity Act**. Solo la FEQ garantisce ai terzi che il dispositivo lo può usare solo il titolare; nessun'altra firma, nemmeno l'avanzata, ha questa garanzia da eIDAS. Un QSCD implica anche un algoritmo robusto. (Teams 6 @ 0:00:05-0:04:54)
- **Certificato qualificato.** È emesso da un QTSP. Nel certificato X.509 di Mario Rossi (dati del titolare "in viola" nella slide) ci sono nome, cognome e, in Italia, **codice fiscale**; in un certificato qualificato di sigillo ragione sociale e partita IVA, codice fiscale o codice IPA. I dati dell'emittente ("in azzurro") indicano il QTSP. (Teams 6 @ 0:04:54-0:07:13)
- **Due verifiche online.** (1) Quella X.509: convalidare il sigillo del QTSP sul certificato, risalire la catena fino a una *trust anchor*, consultando CRL e OCSP di ogni certificato (come nel laboratorio sul certificato web della Repubblica, capitolo 04). (2) Quella della **qualifica**: con lo standard ETSI della **EUTL**, verificare che il QTSP fosse qualificato **al momento dell'apposizione**, cioè "se avesse legalmente il lucchetto". Per questo serve una connessione per verificare qualunque firma qualificata. (Teams 6 @ 0:07:13-0:11:48)
- **Il "bit" di qualifica.** I certificati qualificati hanno un metadato che dichiara "io sono un certificato qualificato": se manca, si esclude a priori la qualifica senza consultare la EUTL. Se c'è, la consultazione serve comunque: perché un attore della minaccia con una CA malevola "non costa nulla" mettere quel bit in un certificato forgiato, e perché il prestatore potrebbe essere stato escluso dalla qualifica o aver revocato i certificati. (Teams 6 @ 0:11:48-0:14:08)
- **Fa fede il momento della firma.** Per X.509 una firma digitale è valida se il certificato era valido al momento della firma; per le norme, un documento con firma avanzata o qualificata è valido se il certificato era valido (e, per le qualificate, qualificato) al momento dell'apposizione. Esempio: Mario Rossi firma con FEQ il contratto d'acquisto dell'appartamento sei mesi fa; due giorni dopo gli rubano lo smartphone, chiama il QTSP e fa revocare (o sospendere) il certificato: da quel momento le nuove firme non sono più nemmeno tecnicamente valide, ma il contratto resta valido. Lo stesso se due settimane fa il QTSP è stato escluso dalla qualifica per una grave violazione. (Teams 6 @ 0:14:12-0:19:16)
- **In Acrobat.** Nella finestra del certificato emesso da Banca d'Italia compaiono il logo del trust mark e due voci: certificato qualificato e chiave privata in un QSCD. Per un sigillo qualificato il campo O in cima sarebbe una persona giuridica e comparirebbe "allegato secondo" invece di "allegato primo". Il metodo sicuro per convalidare un PDF è il **pannello firme**: se non c'è, non c'è alcuna firma digitale; le rappresentazioni grafiche ("firmato digitalmente da...") da sole non vanno credute. (Teams 6 @ 0:19:16-0:21:53)
- **Valore omogeneo.** Tutte le FEQ hanno lo stesso valore in tutta Europa, qualunque sia il QTSP (italiano, spagnolo, lituano, croato): le soluzioni possono differire per tecnica e *user experience* ma non per livello. Non esistono FEQ "più forti": "nessun venditore vi potrà dire: la mia firma qualificata è più qualificata delle altre. Proprio è illegale dirlo". La FEQ è anzi più robusta dell'autografa: per un autografo serve una perizia calligrafica con campioni (difficile se il soggetto è morto o irreperibile), mentre il QTSP ha identificato il firmatario e conserva i dati, "mi pare per vent'anni", e su ordine del giudice deve fornirli. L'inversione dell'onere della prova vale solo per la FEQ, "non per il sigillo elettronico qualificato": basta un software di verifica con esito positivo perché la firma produca gli effetti dell'autografa. (Teams 6 @ 0:22:03-0:26:17)

> **Correzione:** a Teams 6 @ 0:20:42 il docente dice che l'**allegato II** di eIDAS descrive i certificati qualificati di **sigillo**. Nel Reg. 910/2014 l'allegato I riguarda i certificati qualificati di firma elettronica, l'**allegato II** i requisiti dei **dispositivi** qualificati per la creazione di una firma (QSCD), l'**allegato III** i certificati qualificati di **sigillo** e l'allegato IV quelli di autenticazione di siti web.

> **Nota aggiunta:** il "bit" di qualifica è l'estensione X.509 **qcStatements** (ETSI EN 319 412-5), con le dichiarazioni *QcCompliance* (certificato qualificato) e *QcSSCD* (chiave in un QSCD): sono le due voci che Acrobat mostra. Il termine di conservazione di vent'anni corrisponde all'art. 32 c. 3 lett. j del CAD (non riletto in questa sede).

## 6. Elenchi di fiducia: EUTL, LOTL e Brexit

*DI-05 @ 00:30:36*

A monte del trust c'è una **trust list**. I tre modi di convalidare il trust visti nella lezione precedente: **elenco di fiducia**, **CRL** e **OCSP**. CRL e OCSP servono a convalidare tutti i certificati, anche quelli foglia; per i certificati radice c'è il problema "dell'uovo e della gallina": alla fine ci si deve fidare di una CA in modo assiomatico. Per i servizi fiduciari europei questo è gestito dall'**elenco di fiducia europeo, EUTL** (*DI-05 @ 00:31:24*).

L'EUTL è un file **XML**. Il secondo link della slide scarica l'**elenco degli elenchi**, la **LOTL**: per ogni paese contiene il nome dell'agenzia di supervisione, il **certificato a chiave pubblica** con cui quell'agenzia sigilla elettronicamente l'elenco nazionale e l'indirizzo internet dell'elenco nazionale. L'elenco europeo è quindi "una specie di indice dei contenuti" che punta a un elenco per paese, gestito di solito dall'agenzia di vigilanza eIDAS (per l'Italia AgID). Nella versione navigabile si può cercare per paese, per servizio (per esempio tutti i servizi di recapito elettronico certificato qualificato in Francia) o per nome dell'azienda (*DI-05 @ 00:31:56-00:33:50*).

**Slide di sezione con il "EU/EEA Trusted List Browser"** (*DI-05 @ 00:32:47*). Schermata dell'*eIDAS Dashboard* della Commissione europea. Testo:

> The eIDAS Trust List (**EUTL**) trust model is composed by a List of Trusted Lists (**LoTL**), managed and e-sealed by the European Commission (**EC**), which points to several TLs (*national trust lists*), each managed and e-sealed by Member States (**MS**s)' supervisory bodies.
>
> The LoTL also contains the public-key certificates that can be used to validate the national TLs.
>
> Each TL contains a list of eTSPs, which mostly act as administrative CAs in Europe. They may be companies or PAs, each providing its own set of qualified and non-qualified trust services.

Schema: il riquadro LOTL (XML con bandiera UE, righe "BE: Link + certificato", "LU: Link + certificato", "RO: Link + certificato") punta a BE TL, LU TL, RO TL, ciascuno con QTSPs e QTSs. In basso: `https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls` e `https://ec.europa.eu/tools/lotl/eu-lotl.xml`. (Nell'originale "each providing" è preceduto da un trattino, reso qui con una virgola.)

**Slide "The eIDAS Trust List (EUTL)"** (*DI-05 @ 00:35:19*). Schermate: il *Trusted List Browser* con "Search by type", "Search by name", "Search with a signed file"; l'elenco dei paesi con le date di emissione (per esempio Belgium 2022-03-17, Germany 2022-05-05, Iceland 2022-04-25, Liechtenstein 2022-04-25, European Union 2022-05-23); la voce **United Kingdom, issue date 2020-12-31**, "Last known version of the TL of UK published just before leaving the eIDAS TLs Scheme", conservata "for the sole purpose of the verification of the outputs of qualified trust services (e.g. qualified electronic signatures) that were created before that moment"; una mappa *eID.AS* dei Trust Service Providers. Link: `https://eidas.ec.europa.eu/efda/home` e `https://ec.europa.eu/tools/lotl/eu-lotl.xml`.

**Brexit** (*DI-05 @ 00:33:50-00:35:39*). Nell'elenco compaiono anche paesi che non sono (più) nell'UE ma lo sono stati. Quando il docente lavorava in Commissione, prima della Brexit, i prestatori britannici erano qualificati eIDAS e sedevano in Commissione con gli altri. Dopo la Brexit l'eIDAS ha smesso di applicarsi al Regno Unito: le aziende fanno lo stesso business, ma legalmente non c'è più un *cross trust* ("ce n'è un altro, ma ora non entro nei dettagli"). I documenti firmati con firma qualificata britannica nel 2015, 2016, 2019 restano qualificati, perché **fa fede la data di firma**. Per questo negli elenchi, per ogni prestatore e servizio, ci sono i **periodi** in cui il servizio era qualificato, e il software di verifica interroga l'elenco per sapere se il certificato era qualificato al momento della firma.

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 6 (elenco degli elenchi, Regno Unito)*

- La LOTL è un piccolo file XML sigillato da una chiave privata della sola Commissione, la cui **chiave pubblica è pubblicata nella Gazzetta Ufficiale dell'UE**, un documento legale di primo livello. Ogni elenco nazionale è sigillato dal suo Stato. Negli elenchi nazionali ci sono **tutti** i TSP registrati, fra cui quelli qualificati. L'interfaccia web è disponibile in tutte le lingue dell'Unione e serve anche per aiutare qualcuno a trovare un QTSP. (Teams 6 @ 0:26:23-0:30:12)
- Regno Unito: elenco fermo al **31 dicembre 2020**; le firme di QTSP britannici fino a quella data sono qualificate eIDAS e valide in Europa; dal **1° gennaio 2021** le stesse soluzioni, tecnicamente identiche, non godono più in Europa dell'inversione dell'onere della prova (la hanno nel Regno Unito, ai sensi dell'eIDAS britannico). L'autorità di vigilanza britannica "se non sbaglio era il Cabinet Office". (Teams 6 @ 0:28:36-0:29:50)

> **Nota aggiunta:** il Regno Unito è uscito dall'UE il 31/1/2020, ma il diritto UE vi si è applicato fino alla fine del periodo di transizione, il 31/12/2020: da qui la data dell'elenco. Lo SI 2016/696 designa come organo di vigilanza britannico per i servizi fiduciari l'**Information Commissioner (ICO)**; il "Cabinet Office" detto dal docente con riserva non corrisponde (verifica non conclusiva: vedi Punti incerti).

## 7. Laboratorio: un PDF con due firme qualificate e il certificato qualificato

*DI-05 @ 00:35:39-00:43:25*

Il docente condivide lo schermo (Acrobat Reader) con un PDF dimostrativo con **due firme elettroniche qualificate** sue: il suo datore di lavoro, Banca d'Italia, è un prestatore di servizi fiduciari qualificato in Italia e fornisce firme solo ai dipendenti (*DI-05 @ 00:36:48*).

**Documento a schermo** (*DI-05 @ 00:36:45*, scheda "2- doc controfirmat..."). Testo leggibile: "Il presente documento è parte integrante delle attività di laboratorio del corso *Security* di detto Master, a cura del Dipartimento Informatica della Banca d'Italia (di seguito "Dipartimento IT"). La lingua adottata nel documento, in base allo Statuto del Master, è quella italiana. Agli studenti sono fornite più versioni del presente documento nel formato PDF (standard ISO/IEC 32000): la prima senza alcuna firma digitale apposta; una o più versioni con altrettanti sigilli elettronici *avanzati* e/o firme elettroniche **qualificate**, tutti tecnicamente realizzati nei tipi PADES e/o CADES." Due rappresentazioni grafiche con il logo della Banca d'Italia: "ARRIGHETTI WALTER 2024.02.14 18:09:36 +01'00'" e "ARRIGHETTI WALTER 2024.02.14 18:10:36 +01'00'"; fra le due: "Si sottoscrive che questo documento, a scopo puramente dimostrativo, non produce alcun effetto legale e non impegna in alcun modo né il firmatario del documento né il suo datore di lavoro."

Il formato PDF supporta **nativamente** la firma e permette, opzionalmente, di scegliere **dove** e **come appare graficamente** la firma: utile perché il PDF simula la carta e nei contratti spesso si firma in più punti per esprimere la volontà di sottoscrivere parti specifiche (*DI-05 @ 00:36:48-00:37:54*).

Procedura di convalida (*DI-05 @ 00:37:54-00:39:36*):
1. verificare che ciò che appare sia davvero un **campo firma**, con l'icona a sinistra (penna stilografica, "Certificati"; non confonderla con "Compila e firma"); se non c'è si attiva dal menu Strumenti, ma con un PDF firmato Acrobat la mostra di default;
2. il pannello elenca le firme: la prima già verificata, la seconda no (simbolo celeste, banner "Almeno una delle firme deve essere convalidata", *00:38:59*);
3. il pulsante di convalida avvia la verifica tecnica: il documento non è stato modificato dopo la firma e, con la chiave pubblica del certificato, si ricostruisce l'impronta e la si confronta. Dopo la convalida (*00:40:15*): "Firmato, tutte le firme sono valide", "Rev. 1: firmato da ARRIGHET[TI]", "Rev. 2: firmato da ARRIGHET[TI]", con voci "Firma valida", "Origine affidabilità da Europ[a]", "Firma elettronica qualificata ...", "Documento non è stato m[odificato]", "L'ora della firma proviene ...", "Ultimo controllo: 2025.10.29", "Campo: Signature3 a pagina ...", "Documento bloccato da Signa[ture]" (voci tagliate dal bordo del pannello).

**Il certificato qualificato** (*DI-05 @ 00:39:36-00:42:20*), aperto da Dettagli firma, Dettagli certificato. La finestra del certificato non è visibile in nessun frame acquisito: i dati che seguono sono quelli detti a voce.
- emesso da **Banca d'Italia**, che verso il docente svolge il ruolo di prestatore qualificato; nome e cognome del titolare; partita IVA del prestatore;
- validità **dal 20 febbraio 2023 al 20 febbraio 2028**;
- utilizzo: **non disconoscibilità** (*non-repudiation*), il modo tecnico di indicare un certificato di firma o sigillo, non di marcatura temporale né di autenticazione di sito web: serve a evitare che il soggetto possa dire "non l'ho firmata io";
- un link alla **trust list europea**, usato per verificare che il prestatore fosse qualificato nel momento in cui **quella specifica firma** è stata apposta: un dato recuperabile solo online, ed è per questo che la verifica è lenta. È mostrato il simbolo del **trust mark** e la dicitura "certificato qualificato conforme al regolamento europeo 910/2014 allegato I", l'allegato tecnico che dice come deve essere fatto un certificato qualificato di firma elettronica;
- algoritmo di firma **RSA con SHA-256**, più altri metadati X.509 "di cui non vi parlo, perché sono dettagli per esperti di questo argomento, non vi interessano" (*DI-05 @ 00:42:20*).

Dietro una singola firma qualificata c'è "una marea di tecnologia e di cybersecurity" che non si vede: "la crittografia, quando è fatta bene, non la si vede" (*DI-05 @ 00:42:51*). Le due firme sono state apposte indipendentemente: potrebbero essere di due soggetti diversi, parte e controparte.

> **Nota aggiunta:** le date nelle rappresentazioni grafiche (14/02/2024) sono la data di apposizione delle firme sul documento; 2023-2028 è il periodo di validità del certificato: le firme cadono dentro quel periodo, come richiesto (sezione 5).

## 8. Formati di firma: enveloped, enveloping, detached

*DI-05 @ 00:43:25*

**Slide "Enveloped, enveloping, detached signing"** (*DI-05 @ 00:43:51* titolo, completa *00:46:51*). Testo:

> Digital signatures over files is implemented according to three different modalities:
> - **enveloped**: The file format allows the embedding of signatures, as metadata, *within* the evidence.
>
> In this modality, only subsets of the evidence (i.e. the *signed* data) are *covered by* each signature.
> - **enveloping**: The signature is implemented as a container format *wrapping* the evidence.
> - **detached**: Signature is an external evidence which references the original evidence. This is usually implemented as a sidecar file (detached signature) containing a digest of another file (signed data).

(Nell'originale i termini sono separati dalla definizione con un trattino lungo, reso qui con i due punti.) Tre schemi: *ENVELOPED* (un *Signed document* con *Signed Data*, *Signature*, *Signed Data*), *ENVELOPING* (un *Signature document* che contiene *Signature* con dentro *Signed Data*), *DETACHED* (un *Original document* con *Signed Data* e un *Signature document* separato con *Signature*).

La firma può accompagnare il documento o essere separata (*DI-05 @ 00:43:57*):
- **Enveloped**: la firma è scritta **dentro** il file, ed è il caso del PDF, tanto che appare graficamente. È possibile solo se il formato lo supporta nativamente: il file viene "spezzato in due" e in un punto viene inserita una firma calcolata su un'impronta di **tutto il documento salvo la firma stessa**. Un JPEG no: lo standard non lo prevede; si può inventare una variante custom, ma i visori la ignorerebbero "nella migliore delle ipotesi" (*DI-05 @ 00:44:28-00:45:00*).
- **Enveloping**: si imbusta il documento in un **contenitore** più grande, di un altro formato, che contiene documento e firma. Esempio: i file **`.p7m`** (anche `.pdf.p7m`): **PKCS#7 message**, che contiene il documento non firmato e la firma digitale (*DI-05 @ 00:45:36*).
- **Detached**: il documento resta com'è, non firmato; si crea un altro file, in un formato specifico per firme, che contiene la firma e **referenzia logicamente** il documento (la definizione di firma elettronica ammette dati "logicamente associati"), per esempio con la sua impronta: l'impronta è scritta una volta in chiaro, per identificare a quale documento appartiene la firma, e una volta cifrata con la chiave privata, come firma da verificare (*DI-05 @ 00:46:10-00:47:21*).

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 8 (PKCS#7, ASiC, consigli operativi)*

- **Enveloping con PKCS#7.** Alice firma un file Excel con il suo certificato e il suo dispositivo (per esempio una smart card): la busta `.p7m` contiene il file Excel originale, bit a bit identico, la firma digitale e il certificato di Alice, che chiunque può usare per avviare la convalida. (Teams 6 @ 0:30:16-0:31:38)
- **ASiC-E**: in realtà un file **ZIP** con estensione rinominata. Esempio: traccia video, traccia audio e alcune immagini firmate insieme; nello ZIP ci sono i file e una sottocartella **META-INF** con il certificato e le firme di tutti i file. Nato in Europa, "molto poco diffuso"; unico vantaggio operativo: un solo file con una "firma" (in realtà firme distinte) che copre tutti i file. (Teams 6 @ 0:31:38-0:32:43)
- **Detached con PKCS#7.** Bob firma delle slide PowerPoint: né Excel né PowerPoint supportano nativamente una vera firma digitale (le loro opzioni di firma sono grafiche), quindi serve un formato esterno. La busta detached ha estensione **`.p7s`** e contiene firma, riferimento univoco (un hash) e certificato; `.p7m` e `.p7s` sono la stessa busta, con o senza il documento. Con la detached si portano sempre due file; con l'enveloping il file originale si apre solo "sbustandolo" con un programma di convalida, perché Excel non apre i `.p7m`. (Teams 6 @ 0:32:43-0:35:45)
- **Il consiglio del docente.** Per pigrizia chi usa l'enveloping finisce per tenere il `.p7m` e una copia sbustata: due file, entrambi grandi, e il rischio di modificare la copia senza accorgersene e dare per valide firme che non lo sono più. Se il file firmato va aperto spesso, meglio la **detached**; se va solo conservato, l'enveloping. Il fornitore della soluzione qualificata di solito fornisce anche il software; le firme sono interoperabili. (Teams 6 @ 0:35:45-0:37:23)

> **Correzione:** a Teams 6 @ 0:35:17 e 0:36:52 il docente dice "enveloped" parlando del `.p7m` (il file Excel "dentro la busta crittografica") e consiglia "il formato enveloped" per la conservazione; secondo la sua stessa slide il `.p7m` è **enveloping**. Lo stesso scambio a Teams 6 @ 0:38:11 ("firma sequenziale ... in formato enveloped ... a matrioska") e a 0:49:38.

## 9. Firme multiple: sequenziali, parallele, controfirma

*DI-05 @ 00:47:21*

**Slide "Sequential vs parallel signing"** (*DI-05 @ 00:47:19* testo iniziale, *00:49:53* prima parte, completa *00:51:53*). Testo:

> It is always possible to re-sign a document/file/evidence/payload multiple times. Depending on the **file format**, this may be accomplished via one or several methods:
> - **Sequential signing**: Each digital signature is applied ("covers") on the previously *signed* document; it *burns* chronological signing order onto the file.
> - **Parallel signings**: Each signature applies to the same very evidence (i.e. the *unsigned* document. It requires a file format designed to support it, e.g. PKCS#7/CMS (**CAdES**), XML-DSIG (**XAdES**), or JWS (**JAdES**).

(Nella slide manca la parentesi di chiusura dopo "unsigned document".) Schemi: *Sequential Signatures*: *Initial data* → Signer 1 → *Initial data + Signature 1* → Signer 2 → *+ Signature 2* → ... → Signer N → *Signature 1, 2, ..., N* annidate; *Parallel Signatures*: N copie di *Initial data*, ciascuna firmata da un firmatario, poi raccolte in un unico documento con *Signature 1, 2, ..., N*.

**Sequenziale** (*DI-05 @ 00:47:21*): è quanto fatto nel laboratorio. La prima firma (18:09) è sui dati iniziali; la seconda (18:10) è apposta sulla versione che conteneva già la prima. Acrobat permette, per ogni firma, di **visualizzare la versione firmata** (*00:48:55*: banner "La versione visualizzata correntemente è firmata. Sono disabilitate tutte le funzioni di modifica e interattive"): dal campo della prima firma si apre un documento che contiene solo la prima firma. Si possono confrontare le versioni; Acrobat e altri prodotti (il docente dice per lapsus "Word") avvisano se il file è stato modificato fra una firma e l'altra (*DI-05 @ 00:48:02-00:49:50*). Ogni firma è calcolata su un payload che contiene le precedenti: anche senza metadato orario si **cristallizza l'ordine di firma**. Uso tipico: workflow autorizzativi (direttore vendite, poi direttore tecnico, poi CFO, poi CEO, che può firmare solo un documento che contiene già le firme di CFO e CTO) (*DI-05 @ 00:49:50-00:50:55*).

**Parallela** (*DI-05 @ 00:50:55*): ogni firmatario firma sempre il documento **originale non firmato** e salva la propria firma (enveloped, enveloping o detached); le firme si raccolgono indipendentemente da chi firma prima o è più alto in grado, e si può creare un unico contenitore con le N firme e il documento originale: N firme "non scatolate a matrioska" ma in parallelo. Serve un formato apposito: **non** è possibile con il PDF, è possibile con XML, JSON e PKCS#7 (*DI-05 @ 00:51:28-00:52:31*).

**Slide "Sequential vs counter-signing"** (*DI-05 @ 00:52:27*): compare solo lo schema delle firme sequenziali; il docente passa oltre senza commentarla. La controfirma è spiegata solo nel 2026 (sotto).

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 9 (matrioska, firma parallela, controfirma)*

- **Matrioska.** In una firma sequenziale enveloping ogni firmatario reimbusta la busta precedente: N firme, N buste annidate. Ogni firma copre crittograficamente le precedenti e ne cristallizza la *consecutio temporum*. È la modalità più usata nei **processi autorizzativi**: capo reparto, poi capo della business unit, poi finance (che conferma la copertura), poi un alto dirigente che autorizza la spesa; nessuno firmerebbe senza la firma precedente. (Teams 6 @ 0:37:26-0:39:37)
- **Parallela**: firme **paritetiche**, ciascuna sull'originale; esempio tipico il **consiglio di amministrazione**, dove non importa chi firma per primo: il processo raccoglie le firme detached e alla fine le mette in un'unica busta. (Teams 6 @ 0:39:37-0:40:54)
- **Controfirma.** Una firma (enveloped o detached) che non copre il documento ma una **firma precedente**: il controfirmatario calcola l'impronta della sola firma "azzurra" del primo firmatario (che è a sua volta l'hash del documento cifrato con la chiave privata del primo) e la cifra con la propria chiave privata "verde". Non ha tecnicamente firmato il documento, ha firmato la firma. Uso: **deleghe**: il delegato (per esempio un tecnico) firma nel merito; il delegante (un alto dirigente non tecnico) controfirma per confermare che quello era il suo delegato, "nel metodo" e non nel merito, ma è la sua firma quella che conta. Sulle deleghe il docente tornerà (capitolo 06). (Teams 6 @ 0:40:54-0:43:31)

In formula, con $D$ il documento, $\kappa_1^{\text{priv}}$ e $\kappa_2^{\text{priv}}$ le chiavi dei due firmatari:

$$S_1 = \mathrm{Enc}_{\kappa_1^{\text{priv}}}\big(H(D)\big), \qquad S_2^{\text{contro}} = \mathrm{Enc}_{\kappa_2^{\text{priv}}}\big(H(S_1)\big)$$

mentre in una firma sequenziale sarebbe $S_2 = \mathrm{Enc}_{\kappa_2^{\text{priv}}}\big(H(D \,\|\, S_1)\big)$ e in una parallela $S_2 = \mathrm{Enc}_{\kappa_2^{\text{priv}}}\big(H(D)\big)$.

> **Nota aggiunta:** le tre formule sono una sintesi di quanto detto a voce (le slide 2026 non sono disponibili). Nella notazione del corso "cifrare l'hash con la chiave privata" è la firma; con ECDSA o RSA-PSS l'operazione non è letteralmente una cifratura, ma il modello resta valido. In CMS (RFC 5652) la controfirma è un attributo non firmato *countersignature* il cui contenuto firmato è il valore della firma del *SignerInfo* a cui si riferisce, coerente con quanto descritto.

## 10. Formati AdES, PAdES e l'attacco di signature wrapping

*DI-05 @ 00:52:31*

"Va bene, salto questa lezione sugli standard" (*DI-05 @ 00:52:31*): le slide sui formati ETSI scorrono in pochi secondi.

**Slide "ETSI advanced digital signature (AdES) formats"** (*DI-05 @ 00:52:30*, mostrata 3 secondi, solo la prima voce). Riquadro *PAdES, EN 319-142, Self-contained signature*: "Contains signatures within the PDF; Supports XML data; Included within the ISO PDF Standard; Includes signing and verifying in PDF software, no customized programming required; Supports serial form-fill and signatures for approval workflows; Supports a visual signature appearance in the document; Provides long-term validity; enveloped (special)". A destra: "**PAdES** (EN 319-142): ETSI variant of the original PDF Signature by Adobe®, published as ISO 32000: enveloped only, plus signatures' visual representation; PDF file format *only*." (Separatori originali resi con i due punti.)

**Slide "PAdES: PDF advanced digital signature"** (*DI-05 @ 00:52:34*, ricompare a *00:53:38*). Struttura del contenuto PDF: *Signature dictionary*, *Byte range*, *Contents*, *Certificate*, *Signed message digest*, *Document timestamp*, *Validation values*, *Document timestamp*, *EOF*, con le parentesi che indicano i livelli *PDF Signature*, *PAdES B-Level*, *PAdES T-Level*, *PAdES LT-Level*, *PAdES LTA-Level*. Al centro l'albero degli oggetti di un PDF firmato (`/AcroForm`, `/FT: /Sig`, `/Filter: /Adobe.PPKLite`, `/SubFilter: /ETSI.CAdES.d[etached]`, `/ByteRange: [0, 9247, 47137, 794]`). A destra le **revisioni incrementali**: *Original version, signature 1, %%EOF*, *Changes for version 2, signature 2, %%EOF*, *Changes for version 3, signature 3, %%EOF*, con "signature N applies to these bytes"; una finestra *Signature Properties*: "Signature is VALID, signed by GemBoxECDsa521", "Signing Time: 2020/05/08 13:57:12 +02'00'", "The document has not been modified since this signature was applied", "The signature includes an embedded timestamp".

Il docente "col cappello del sicurista" (*DI-05 @ 00:52:31-00:53:31*): il PDF è un formato molto avanzato, Adobe lo ha reso standard pubblico **ISO 32000**, scaricabile gratuitamente, per massimizzarne la diffusione; in Europa lo si usa con le firme qualificate. Ma la complessità lo espone ad attacchi.

**Slide "PDF signature wrapping attack"** (*DI-05 @ 00:52:36*, poi *00:55:25* e *00:58:35*). Link `https://pdf-insecurity.org/`. In alto: un *Certifier* firma un contratto ("Transfer to: Honest Corp., IBAN: US12 3456 7890, Amount: 100$") con "Further changes are allowed"; un *Attacker* applica "Evil but allowed changes" e la *Victim* riceve "Transfer to: Evil Corp., IBAN: US66 6666 6666, Amount: 100.000$", con il sigillo apparentemente intatto. Sotto: due viste di un lettore PDF che dicono entrambe "Signed and all signatures are valid": una mostra "Sign the document to get a reward!", l'altra "You are fired! Get out immediately"; le strutture `%PDF-2.0` mostrano un *Shadowed Document* con due versioni dell'oggetto `4 0 obj`, la *Digital Signature* e una sezione aggiunta in coda (`xref`, `trailer`) evidenziata in rosso come *Referencing Shadowed Content*.

L'attacco (*DI-05 @ 00:53:31-00:55:40*), chiamato a voce "signature wrapping" (la trascrizione automatica ha "ropping", "hopping"): sfruttando il fatto che una firma enveloped in un PDF può essere scritta "sostanzialmente ovunque", si fa in modo che le firme apposte non coprano le precedenti; se il documento è costruito in un certo modo e il software di convalida non è "particolarmente puntiglioso", può indicare come valida una firma totalmente invalida e permettere di **falsificare un documento firmato**. Dettagli su `pdf-insecurity.org`, "io non ho il tempo di mostrarveli". Rassicurazione: i PDF prodotti e firmati con software commerciali o open source robusti e aggiornati (anche l'Acrobat Reader gratuito firma e convalida) non sono vulnerabili; e anche un PDF vulnerabile già sfruttato viene segnalato dai software moderni in convalida. È un attacco che esiste ancora, ma ci sono **prevenzione** (creare i PDF con programmi sicuri) e **rilevazione** (convalidare con programmi aggiornati), "tornando al corso di cyber security".

> **Nota aggiunta:** `pdf-insecurity.org` (Ruhr-Universität Bochum) descrive più famiglie di attacchi alle firme PDF: *Universal Signature Forgery*, *Incremental Saving Attack*, *Signature Wrapping Attack* (2019) e poi *Shadow Attacks* (2020) e attacchi alle firme di certificazione (2021). La slide intitolata "signature wrapping" illustra in realtà uno **shadow attack** (il contenuto "ombra" referenziato da una revisione incrementale) e un attacco alle firme di certificazione ("evil but allowed changes"). ISO 32000-1:2008 è stata resa disponibile gratuitamente da Adobe; ISO 32000-2 è gratuita dal 2023 tramite la PDF Association.

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 10 (formati ETSI AdES e profili di conservazione)*

- L'UE ha delegato all'**ETSI** di partire dai formati più usati e creare standard con una *baseline* unica per firme e sigilli avanzati (e quindi qualificati): i formati **AdES**. **PAdES** evolve la firma PDF (ISO 32000); **CAdES** evolve PKCS#7 (le estensioni restano `.p7m` e `.p7s`, ma dentro ci sono caratteristiche aggiuntive di sicurezza e metadati per la validazione); **XAdES** evolve **XML-DSig** del W3C (l'ente che mantiene HTML); poi il contenitore **ASiC** e la firma JSON **JAdES**, alla cui stesura normativa il docente dice di aver partecipato. P sta per PDF, X per XML, C per CMS. (Teams 6 @ 0:43:39-0:46:58)
- Tutti hanno **quattro profili**, alcuni pensati per la conservazione a lunghissimo termine (**LT**, soprattutto **LTA**): permettono di convalidare a scopo archivistico anche quando le CA radice non esistono più e gli algoritmi sono deprecati. (Teams 6 @ 0:47:02-0:47:45)
- Il PDF supporta firme *embedded* e rappresentazioni grafiche (il rettangolo "Digitally signed by GemBox ECDsa"), a ognuna delle quali corrisponde una firma navigabile. L'attacco, chiamato a voce "signature dropping", è **annullato con il livello PAdES** (specifiche più stringenti), ma resta per documenti vecchi firmati con applicazioni non conformi. (Teams 6 @ 0:47:45-0:49:20)
- **XAdES/XML-DSig** è molto potente: firma enveloped (il file XML resta XML), enveloping, detached anche di file non XML (un JPEG o un MP3 restano tali, la firma sta in un contenitore XML), imbustamento di un file non XML in un XML; anche **firme selettive**, "troppo di dettaglio per il momento, non tratto". (Teams 6 @ 0:49:20-0:50:43)

> **Nota aggiunta:** i quattro livelli dei profili *baseline* ETSI sono **B** (base), **T** (con marca temporale), **LT** (*long-term*, con dati di validazione: certificati, CRL, OCSP) e **LTA** (*long-term with archive timestamps*, marche temporali d'archivio rinnovabili), gli stessi della slide PAdES 2025. Le norme: PAdES ETSI EN 319 142, CAdES EN 319 122, XAdES EN 319 132, ASiC EN 319 162, JAdES TS 119 182-1. La "C" di CAdES sta per CMS (*Cryptographic Message Syntax*, RFC 5652), l'evoluzione di PKCS#7.

## 11. Firmare JSON: JWT, JWS e JAdES

*DI-05 @ 00:56:10*

"Scordandoci un attimo le firme e i sigilli elettronici" e tornando alla definizione madre di firma digitale: si possono firmare anche **JSON**, messaggi tecnici usati nel web ogni giorno. Quando si apre Netflix, la posta web o un social, anche da app, lo scambio di dati con il service provider comporta l'invio di **JSON Web Token**, "la codifica in base 64" di strutture dati JSON, "praticamente strutture di database non strutturati" (*DI-05 @ 00:56:44*). Anche i JWT possono essere cifrati e firmati. Un JWT firmato si riconosce dai **due caratteri punto** che separano tre campi: (1) in verde l'**intestazione**, che descrive come è fatta la firma; (2) il **payload**, il JWT "pulito"; (3) la **firma digitale** calcolata sul secondo campo seguendo quanto scritto nell'intestazione (*DI-05 @ 00:57:16-00:57:50*).

Anche il JWT può essere reso conforme alle firme e ai sigilli avanzati europei con lo standard **JAdES**, che specifica come fare firme e sigilli avanzati (e quindi qualificati) su oggetti JSON; **PAdES** fa lo stesso per i PDF; **XAdES** e **CAdES** per altri formati (*DI-05 @ 00:57:50-00:58:26*).

**Slide "JAdES: JSON advanced digital signature"** (*DI-05 @ 00:58:18*). A sinistra un token in tre colori:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

A destra un riquadro verde *JOSE header*: `"alg":"ES256", "typ":"JOSE", "iat":21243431.33, "x5t#o":{"properties":{"digAlg":"…","digVal":"…"}}, "kid": κ^pub, "srCms":{...}, "sigPl":{...}, "etsiU":{...}, "crit":["iat","alg","x5t#o","srCms","sigPl"]`; un riquadro *payload* con una credenziale sanitaria: `"iss": "https://vc.vrs.digital.go.jp/issuer"`, `"nbf": 1648956149.461584, // ~= 2022-04-03`, `"vc"` di tipo `https://smarthealth.cards#health-card` con un *fhirBundle* (risorsa *Patient*, `"given": ["DAN"], "family": "YAMAMOTO"`, `"birthDate": "xxxx-xx-xx"`; risorsa *Immunization*, `"status": "completed"`, `"occurrenceDateTime": "2021-08-10"`); in basso *JWT signature* `1110100101`. Testo:

> **JAdES** introduces several new claims to a JWS' JOSE header to provide the same flexibility and trust level of CAdES, XAdES and PAdES for advanced electronic signatures and seals.
>
> It also extends JWS functionalities, namely:
> - multiple signatures;
> - [un-]signed payload and header (coverage);
> - detached signature.

**Verifica per esecuzione** (Python, `base64.urlsafe_b64decode` e `hmac`): il token della slide è l'esempio standard di `jwt.io`.
- Intestazione decodificata: `{"alg":"HS256","typ":"JWT"}`.
- Payload decodificato: `{"sub":"1234567890","name":"John Doe","iat":1516239022}` (`iat` = 18/01/2018 01:30:22 UTC).
- Firma: $\mathrm{HMAC\text{-}SHA256}\big(k,\ \texttt{base64url(header)} \,\|\, \texttt{"."} \,\|\, \texttt{base64url(payload)}\big)$ con la chiave di esempio `your-256-bit-secret` dà esattamente `SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c` (32 byte, 256 bit). Verificato.
- Il commento `~= 2022-04-03` accanto a `nbf: 1648956149.461584` è corretto (3/4/2022 03:22:29 UTC); `iat: 21243431.33` nel riquadro JOSE corrisponde invece al 3/9/1970: un valore segnaposto.

> **Correzione:** il token mostrato **non** corrisponde al riquadro JOSE né al payload della slide: dichiara `HS256`, cioè un **HMAC con chiave simmetrica condivisa**, non una firma con chiave privata (il riquadro dice `ES256`, ECDSA su P-256), e il suo payload è quello di esempio "John Doe", non la credenziale sanitaria. Un JWT `HS256` garantisce integrità e origine solo fra chi condivide la chiave e non può essere una firma o un sigillo avanzato. Inoltre la codifica dei JWT è **base64url** (alfabeto con `-` e `_`, senza padding `=`), non base64 standard. Lo sviluppo esteso di JAdES detto a voce, "JSON Advanced Digital Electronic Signature", non è quello ufficiale: ETSI TS 119 182-1 lo chiama **JSON Advanced Electronic Signatures**.

### Integrazione Teams 2026 (lezione 6 2026)

*Sezione 11 (JWS e JAdES)*

- Il docente dà più dettagli "perché oggi un data analyst deve conoscere JavaScript e JSON": JAdES è una variante della **JWS** (*JSON Web Signature*), il modo in cui sono firmate le asserzioni di tutte le applicazioni JSON; le JWS sono usate in **OAuth** e **OpenID Connect** e JAdES è la firma del **wallet europeo** dell'identità digitale (capitolo 06). JAdES aggiunge firma multipla e firma detached. (Teams 6 @ 0:50:43-0:51:45)
- La costruzione: il JSON del payload viene "canonicalizzato" (tolti gli spazi) e codificato in base64 (la parte grigia fra i due punti); si crea un'intestazione JSON (verde) con i metadati: algoritmo, orario della firma, riferimento alla chiave pubblica o la chiave stessa; anche questa canonicalizzata e codificata; si concatenano con un punto, si calcola la firma digitale e la si appende in base64 dopo il secondo punto (blu). È la forma più semplice; la stringa può essere più lunga del JSON ma viaggia in una POST, in una GET o in qualunque messaggio web, perché non usa caratteri di controllo di HTTP, HTML, CSS o JavaScript. (Teams 6 @ 0:51:45-0:53:35)

> **Nota aggiunta:** la JWS (RFC 7515) non richiede canonicalizzazione: firma esattamente i byte codificati in base64url, quindi il verificatore non deve riserializzare il JSON. È proprio la scelta che evita i problemi di canonicalizzazione di XML-DSig. La sicurezza URL della stringa deriva dall'alfabeto **base64url** (RFC 4648 §5).

## 12. Attacchi agli schemi di firma e cifratura

*DI-05 @ 00:58:26*

La firma digitale è robusta rispetto all'autografa perché **ogni firma digitale è unica**: le firme autografe tendono a essere il più simili possibile fra loro, e da qui gli attacchi in cui si ritaglia, fotocopia e incolla una firma, contando sul fatto che il grafologo valuta pressione e velocità del tratto. La firma digitale è un oggetto matematico: se la si altera cambiano i bit, e la stessa firma non può essere riusata per un altro messaggio (*DI-05 @ 00:58:26-00:59:27*). Ma non è imbattibile.

**Slide "Attacking signature and encryption schemes"** (*DI-05 @ 01:02:36*, mostrata durante la spiegazione). Testo:

> There are several ways for a threat actor (or a security researcher, for that matters) to attack digitally signed and/or encrypted documents. Some we have already covered:
> - crypto-analysis (direct or inverse, with varying degrees or sophistication and "noise" being generated), including
>   - *harvest-now-crack-later*: encrypted/signed files are gathered to be decrypted later (even *years* or *decades* later), when the TA has more computing power to successful perform crypto-analysis;
> - signature **forging**: attacking the signature itself (we've seen this to be substantially more robust than autograph);
> - signature **wrapping**: relying on vulnerabilities of the file format/container for the signature/cipher-text.
>
> Besides that, other tactics may be pursued:
> - attacking the signature / encryption **scheme**, i.e. its *processes*: this may loosely include also ↓
>   - **social engineering** based attacks: by tricking, coercing, or otherwise exploiting the "human factor" (signers/encryptors);
> - attacking the **CA** itself: breaching the security (C.I.A. triad) of a technical and/or administrative CA:
>   - digital identity theft against the RA (i.e. issuing certificates against fake subjects/holders),
>   - faking a CA (it is another higher-profile level of digital identity theft, of the CA's identity itself),
>   - DoS / DDoS attacks on the CRL/OCSP availability (so to thwart certificate validation processes),
>   - stealing or tampering with CA keys,
>   - any other forms of "traditional" cyber-attacks against the CAs (e.g. ransomware, espionage, wipers, insider threats, etc.);
> - and, of course, **stealing** or **eavesdropping secret keys**...

(Trattini lunghi dell'originale resi con i due punti o con la virgola.)

Il commento (*DI-05 @ 00:59:27-01:02:24*):
- **attacchi ai formati** (signature wrapping, sezione 10);
- **attacchi ai processi di firma**: ingannare il sistema tecnico o l'utente con l'ingegneria sociale, facendogli firmare un documento sbagliato credendolo giusto, o costringendolo a firmare, magari con un ricatto;
- **attacchi alla CA**: le CA fanno il mestiere di fiducia digitale per gli utenti, quindi attaccarle è efficiente; sono più difficili da attaccare (misure fisiche, logiche e amministrative più robuste), ma chi ruba o falsifica la chiave di certificazione può contraffare tutti i documenti dei clienti. L'esempio, già fatto, dell'azienda andata in bancarotta dopo l'esfiltrazione delle sue chiavi private (capitolo 04);
- **furto delle chiavi private** (lezione precedente);
- la tipologia più insidiosa: la crittoanalisi **harvest now, crack later**: si ruba oggi un documento cifrato o firmato, robusto al momento, e lo si attacca in futuro con più risorse (per esempio un calcolatore quantistico); se il documento ha ancora valore, è un problema di sicurezza. Vedi capitolo 01 e guida Cybersecurity, capitolo 07, sezione 13.

> **Nota aggiunta:** l'azienda andata in bancarotta dopo la compromissione della CA è con ogni probabilità **DigiNotar** (Paesi Bassi, 2011); il nome non è detto in questa lezione.

## 13. Novità 2026: PEC, marca temporale, registri distribuiti

*Contenuti di Teams 5 e Teams 6 senza corrispondente nella lezione 2025. Nella DI-05 la PEC compare solo come esempio di servizio richiesto a un identity provider (DI-05 @ 01:02:54) e la marcatura temporale solo come servizio per cui decide il giudice (DI-05 @ 00:07:46).*

### Integrazione Teams 2026 (lezioni 5 e 6 2026)

*Sezione 13 (PEC)*

- La **PEC** italiana è un servizio fiduciario confluito in eIDAS come **servizio elettronico di recapito certificato**; il gestore PEC è oggi un prestatore di servizi fiduciari. La PEC non ha un'alternativa europea: il suo valore probatorio vale solo per le PEC italiane e solo in Italia. Sono però in corso le qualifiche di alcuni gestori PEC come fornitori di **recapito certificato qualificato**, che con gli altri prestatori qualificati europei daranno valore legale transfrontaliero, soprattutto ai tempi di invio e consegna. (Teams 5 @ 0:50:12-0:51:38)
- Per il DPCM firme, art. 61, un messaggio PEC conservato con la **ricevuta completa** (il piccolo file allegato al messaggio, che le PA acquisiscono automaticamente con il protocollo) vale come FEA, perché il gestore garantisce a monte l'identità del mittente (sezione 5). (Teams 5 @ 0:49:57-0:50:48, 0:51:38-0:51:54)

*Sezione 13 (marca temporale)*

- La **validazione temporale elettronica** (*electronic timestamping*), in Italia **marca temporale**, è nata in Italia come la PEC ed è confluita in eIDAS nel 2014: la marca temporale italiana è diventata la validazione temporale elettronica **qualificata**. (Teams 6 @ 0:56:06-0:56:31)
- Tecnicamente è una **firma digitale** apposta da una **TSA** (*Time-Stamping Authority*), di cui ci si fida perché ha un **orologio sincronizzato**: la TSA non emette un certificato ma firma direttamente l'impronta del documento insieme a un orario con fuso: "una firma digitale calcolata sul documento più l'orario asserito dalla TSA". Non garantisce che il documento sia autentico né firmato: asserisce solo che un documento con quell'impronta **esisteva** in quell'istante, come un "certificato di esistenza in vita". (Teams 6 @ 0:56:50-0:58:45)
- **Aneddoto.** Nel 2018 o 2019, da consulente AgID, il docente era a una conferenza in Commissione in cui le agenzie nazionali riportavano il numero di servizi fiduciari: il responsabile AgID diede per le marche temporali qualificate un numero vicino a **due miliardi**, relativo al solo primo semestre dell'anno precedente, mentre gli altri paesi davano numeri inferiori di 4-6 ordini di grandezza. Il motivo: ogni PEC inviata e ricevuta riceve marche temporali dai gestori del mittente e del destinatario, e ogni protocollazione o conservazione a norma genera almeno una marca. (Teams 6 @ 0:58:45-1:01:07)
- Nel 2018, secondo il docente, un regolamento europeo ha confermato che le marcature temporali **non qualificate** possono essere realizzate anche con una **blockchain**: ogni blocco contiene una firma del blocco precedente, e con un orario nei metadati la catena di orari ricostruisce una marcatura temporale. (Teams 6 @ 1:01:07-1:01:44)

*Sezione 13 (registri distribuiti)*

- Niente blockchain ("avete fatto un corso a riguardo"), ma eIDAS (con eIDAS 2) prevede servizi fiduciari di creazione e convalida dei **registri elettronici distribuiti**, anche **qualificati**, cioè con garanzia europea sulla registrazione cronologica delle attività; i meccanismi di firma sui blocchi potranno essere qualificati se garantiti a monte da un QTSP. Una blockchain qualificata non basta però per la sicurezza di una criptovaluta: servono anche la **governance** (chi legge e scrive nei nodi, quale maggioranza cambia le policy, come si gestisce la scarsità con il *mining*, cosa si registra: transazioni, smart contract...). (Teams 6 @ 0:53:49-0:56:06)

> **Nota aggiunta:** la marca temporale è standardizzata da RFC 3161 (*Time-Stamp Protocol*) e dai profili ETSI EN 319 422; la TSA firma una struttura che contiene l'impronta inviata dal richiedente, l'ora e un numero di serie. Il "regolamento europeo del 2018" sulle marche temporali con blockchain non è stato identificato: eIDAS non esclude tecnologie per le validazioni temporali non qualificate (art. 41(1)), e il "registro elettronico" come servizio fiduciario è stato introdotto da eIDAS 2 nel 2024 (art. 45 nonies e seguenti). Da verificare.

## 14. Autenticazione e autorizzazione

*DI-05 @ 01:02:24*

Il passaggio all'identità digitale. Centrale per i servizi fiduciari è stabilire l'**identità dei titolari**: è il mestiere della CA e della **registration authority** quando Alice chiede un certificato. Astraendo dal servizio specifico (certificato di firma, di sigillo, TLS, casella PEC), quando Alice si presenta nel mondo digitale per ottenere un servizio deve da un lato **dimostrare chi è**: dominio dell'**autenticazione**; dall'altro c'è qualcuno che decide se, essendo lei, può avere quel servizio: dominio dell'**autorizzazione**. "Chi sei? Sei Alice? Sì, no: autenticazione. Ok, cosa vuoi? Quella cosa lì? Sì, no: quella è autorizzazione" (*DI-05 @ 01:02:54-01:03:58*).

**Slide di sezione "Authentication vs Authorisation"** (*DI-05 @ 01:03:41*): impronta digitale su un circuito.

I **fattori di autenticazione** sono gli elementi, nativamente digitali o trasformati in digitale dal mondo esterno, che permettono a un sistema più o meno automatizzato (un software che risponde sì o no e manda su una pagina o su un 404), o a un "omino" che guarda il video in tempo reale o registrato, di decidere se concedere il servizio: gli elementi digitali utili a stabilire chi siete (*DI-05 @ 01:03:58-01:04:38*).

Le integrazioni 2026 su autenticazione, autorizzazione e identità digitale (Teams 6 da 1:01:49, Teams 7 e 8) sono nel **capitolo 06**.

## 15. I fattori di autenticazione

*DI-05 @ 01:04:38*

**Slide "Authentication and its factors"** (*DI-05 @ 01:04:09*). Immagine: *POSSESION* ("Something you have", smartphone con spunta) + *KNOWLEDGE* ("Something you know", utente e asterischi) + *BEING* ("Something you are", impronta); a destra una chiave al centro di icone (SMS, email, token USB, impronta, smartwatch, tastierino...). Testo:

> - Something you know (*conoscenza*): e.g. password, PIN, passphrase;
> - Something you have (*possesso*): digital evidence (e.g. OTP) proving the physical possession of a token (e.g. smartcard, USB key, smartcard / e-payment/e-ID card);
> - Something you are (*inerenza*): digital evidence of **biometric** data matching.

(Nell'immagine "POSSESION" è scritto con una sola S; trattini dell'originale resi con i due punti.)

**Il fattore non è l'OTP** (*DI-05 @ 01:05:11*). Molti confondono, "e quando si confonde poi si commettono errori". Domanda alla classe: un account email protetto da **due password**, la prima lunga almeno 42 caratteri e la seconda di 18 con molti più simboli: perché, almeno formalmente, è un'autenticazione a **singolo fattore**? Nessuno risponde; il docente (*01:06:17*): perché l'attore della minaccia che bypassa la prima password probabilmente con la stessa tecnica bypassa la seconda. Se Bob del reparto vendite trova le password difficili, non se ne segna una sola sul foglietto sotto il tavolo o sul bordo del monitor: se le segna entrambe, o le mette uguali. E anche se restano segrete, un attaccante che le deduce o forza (password spraying, password guessing, brute forcing) con la stessa tecnica bypassa entrambe: si ottiene al massimo un **ritardo** (*DI-05 @ 01:06:53-01:07:26*). Password, PIN, parole chiave sono **implementazioni** di un solo fattore: **conoscenza**, qualcosa che in teoria conosci solo tu (*DI-05 @ 01:07:58*).

**Possesso** (*DI-05 @ 01:07:58-01:12:21*): fare affidamento su qualcosa che solo tu dovresti avere, e il fattore consiste nel **dimostrare** di averlo. I fattori sono evidenze digitali: il fattore di possesso è la **prova digitale** che hai in mano in quel momento la smart card, il token, la chiavetta, il telefono con l'app; non è l'OTP né il token in sé. Ci fu un **dibattito in Commissione europea**, in sede di notifica degli schemi di identità digitale, su cosa sia un fattore di possesso:
- per alcuni basta avere il token fisico con il numero che cambia (quelli usati fino a qualche anno fa per il conto in banca) o l'app installata sul telefono;
- per altri non è una prova di possesso: chiunque trovi per terra il token o sbirci il numero, o abbia il telefono sbloccato, lo usa; si dimostra solo che "c'era qualcuno nelle vicinanze", non che sei tu. Per questi paesi il token deve essere protetto da un **PIN** noto solo al titolare. Per alcuni lo sblocco del telefono (impronta, codice, volto) più la lettura del numero o il clic "sì, sono io" è complessivamente **un solo fattore di possesso**; per altri è un'autenticazione **a due fattori** (sblocco con password più prova di possesso).

È un dibattito ancora aperto, ma l'ambiguità sparisce scegliendo il documento di riferimento: i documenti europei e quelli americani dicono due cose leggermente diverse, ciascuno senza ambiguità (*DI-05 @ 01:11:51-01:12:21*).

## 16. Inerenza, biometria e presentation attack

*DI-05 @ 01:12:21*

Il terzo fattore è l'**inerenza**, *something you are*: quasi sempre una prova digitale che certi **dati biometrici** sono i tuoi. Controlli reali: scansione fotografica o infrarossa del volto, lettura (di solito capacitiva) dell'impronta, fino a sistemi più avanzati: iride, vene del palmo, timbro della voce (*DI-05 @ 01:12:54*).

I lettori non sono tutti uguali (*DI-05 @ 01:13:25-01:14:54*):
- Microsoft, per abilitare il riconoscimento facciale di **Windows Hello**, richiede telecamere con caratteristiche minime, sotto le quali sarebbe possibile un **presentation attack** (presentare una persona con un volto diverso);
- i lettori d'impronta dei cellulari economici, alcuni addirittura dietro lo schermo OLED, non hanno la qualità di un lettore "di tipo ISO" montato accanto alle porte, che fa appoggiare il dito su un vetrino in piano e ne fa una scansione 3D a infrarossi delle minuzie in diversi secondi;
- un lettore capacitivo "scatta una foto" dell'impronta e si confonde: con due gocce di pioggia smette di funzionare, "immaginate quanto può essere bypassabile con tecniche da telefilm di serie B".

Vedi anche guida Cybersecurity, capitolo 06, sezione 7 (frodi d'identità, presentation attack e deepfake).

## 17. Digital twin e deepfake

*DI-05 @ 01:14:54*

Un rischio enorme per l'identità digitale viene dall'intelligenza artificiale ma anche dagli **effetti speciali** cinematografici. Il docente ha lavorato al film italiano di Gabriele Salvatores **"Il ragazzo invisibile: seconda generazione"**; le immagini vengono da un video pubblico (*DI-05 @ 01:15:35*).

**Slide "Digital twins from cinematic VFX"** (*DI-05 @ 01:12:58*, *01:15:21*, *01:17:54*, *01:18:43*). Prima versione: *Actual Actor* (foto sul set di un antagonista truccato con pittura bianca e rossa), *3D Model* (il suo gemello digitale), e una foto di scena con l'attore accanto a una sfera cromata, una sfera grigia e due tabelle colore. Seconda versione: quattro fasi del modello (texture del volto, maschera senza occhi, modello muscolare con denti e lingua, render finale). Terza versione: la scena del furgone (modello 3D, wireframe, ripresa finale) e il link `https://vimeo.com/270983205`.

Il **digital twin** è una ricostruzione 3D basata solo sulle foto scattate sul set da più angolazioni ad alta risoluzione: con la **fotogrammetria** si ricostruisce il volto; gli animatori costruiscono un modello fisico con ossa, muscoli, denti, lingua e **rig** (aste virtuali che muovono i muscoli) con elasticità di tutte le componenti, "esattamente come si farebbe su un cadavere"; incollandovi le fotografie si ottiene un modello ad altissima risoluzione, mostrato senza occhi per far vedere che è sintetico (nel riflesso della sfera c'è solo una testa). Il gemello può parlare e interagire in tempo reale. Dieci anni fa bastavano fotocamere di qualità, un attore fermo in pose precise e **una sola workstation** con una scheda grafica, alla portata di un appassionato di videogiochi di oggi, più un software da qualche migliaio di dollari (*DI-05 @ 01:16:10-01:18:19*). Nel cinema serve a non usare controfigure: nella scena l'attore viene investito da un furgone ad alta velocità, ma "non c'è nulla di reale": il Porto Vecchio di Trieste è ricostruito in 3D, il camion è un modello comprato, l'attore è il gemello digitale (*DI-05 @ 01:18:19-01:18:57*).

"Se mi tolgo il cappello del post-producer e mi metto quello dell'attore della minaccia", questa tecnologia potenziata dall'AI "diventa diabolica": con video e immagini di qualità molto peggiore si realizzano **deepfake**. Si sorvola spesso sui deepfake **audio**, solo voce, più realistici di quelli video. Si può prendere un attore che parla, dargli il volto di un personaggio pubblico e fargli dire cose mai dette: danni reputazionali enormi. Con computer *off the shelf* il rischio di **presentazione** di un'identità falsa è estremamente concreto (*DI-05 @ 01:19:27-01:20:40*).

**Slide "Deepfakes and AI"** (*DI-05 @ 01:20:33*). Immagini di volti con mesh e landmark facciali (Zuckerberg, Obama), la sequenza (a)-(h) di ricostruzione 3D di un volto (Stallone), "Real" e "DeepFake" (Musk). Testo:

> Theatrical digital visual effects (**VFX**) result in synthetic, computer-graphic realistic "twins", animated in real time in the act of speaking or performing actions that real subjects would have never said or done. In recent past, AI-generated "**deep-fakes**" have been exploited in jokes and activism. They may be used in **presentation attack**s, i.e. for identity theft against a remote ID proofing's *liveness* detection mechanism.

> **Nota aggiunta:** "Il ragazzo invisibile: seconda generazione" è uscito nel 2018: rispetto al 2025 sono circa sette anni, non dieci.

## 18. Identity proofing

*DI-05 @ 01:20:40*

"Salto la parte di Kerberos che è per specialisti. E vi parlo invece dell'autenticazione" (*DI-05 @ 01:20:40*): le slide scorrono velocemente (*01:20:45-01:21:42*). Fra quelle che passano senza commento: "Authentication example: Kerberos tickets" e "Kerberos flow" (riprese nella sezione 23), "Active Directory delegation (proxying)" (*01:21:05*: delega vincolata, non vincolata e *resource-based constrained delegation*), "Digital Identity standards and regulations" (*01:21:17*), "Traditional vs SSI" (*01:21:22*), "Identity delegation" (*01:21:26*: una persona fisica, una persona giuridica "Acme s.r.l.", un sistema IT "www.acme.com", una persona fisica per conto di un'altra), "Single sign-on (SSO)" (*01:21:29*), "Kerberos flow 3/3" (*01:21:33*), "Local and client/server authentication" (*01:21:37*). Poi il docente toglie la condivisione e "va a braccio" (*01:21:26-01:21:56*).

Il problema dei deepfake e di tutti gli attacchi con un "manichino digitale" è che nel processo di identità c'è un **primo istante**: come quando si crea una password la si stabilisce una volta e poi la si riusa (ecco perché è critico il cambio password), nell'identità digitale c'è un momento in cui si va da un **identity provider** e ci si fa "staccare" un'identità digitale: l'**identity proofing**. Il risultato è che l'identity provider rilascia **credenziali** a uno, due o tre fattori con cui riautenticarsi più volte (*DI-05 @ 01:21:56-01:23:17*).

Se con un presentation attack o un altro attacco si inganna l'identity provider in questa fase, si compie un **furto d'identità digitale**: si hanno credenziali valide da quel momento in poi, e si può fare un attacco **in scala**, riautenticandosi molte volte. Probabilmente nessuno se ne accorgerà mai, perché l'associazione fra identità digitale e persona fisica (o malware: in molti casi l'identità rubata la usa un software in automatico) è stata accertata erroneamente **a monte** e non viene più riverificata (*DI-05 @ 01:23:17-01:24:35*). L'identity proofing è quindi il processo **più sensibile** del ciclo di vita dell'identità: se attaccato con successo porta a un attacco di **impersonificazione**, e i sistemi delle autenticazioni successive non vedono nulla, perché l'identità è tecnicamente valida. "Abbiamo consegnato a Carl, l'uomo nel mezzo, i fattori di autenticazione di Alice, il certificato a chiave pubblica e la chiave privata di Alice. Da quel momento in poi Carl è Alice per chiunque. Tutto quello di cui abbiamo parlato nelle scorse lezioni, basta, finito" (*DI-05 @ 01:24:35-01:25:08*).

**Slide "Identity proofing"** (*DI-05 @ 01:22:53*, mostrata di nuovo a *01:24:53*). In alto tre passi: (1) "Collect identifying information e.g. passport, driving license, answers to security questions"; (2) "Confirm information is authentic and accurate and the claimed identity exists"; (3) "Confirm the claimed identity belongs to the user". Testo:

> In some contexts (e.g. issuance of physical or electronic IDs) the identity proofing phase is the only point in time in which the real identity of a user is checked.
> - **IAL1**: no requirement to link to real-life identity; any other attributes are self-asserted (or treated as such);
> - **IAL2**: real-world existence claims (*either remote or physical-presence* required); pseudonyms could be used;
> - **IAL3**: physical presence required; attributes need to be verified as well.
>
> Evidence is classified as FAIR, STRONG, and SUPERIOR; may include physical IDs and/or biometric data.
>
> Credentials are supplied by a CS.
>
> *This is not in SP800-63A*: Identity (credentials) may also be suspended or revoked.
>
> Today, **remote** identification criteria are paramount.
>
> *This is not in SP800-63A*: Identity proofing may be hardened by requiring re-proofing at set timeframes in the future, after the eID was issued (e.g. when a physical ID expires).

Schema a strada: *Applicant* → (1) *Resolution*: core attributes and evidence collected, "Individual uniquely distinguished among a given population or context" → (2) *Validation*: evidence validated, "Authenticity, validity, and accuracy of identity information determined and related to a real-life subject" → (3) *Verification*: evidence verified, "Linkage between claimed identity and real-life existence of subject presenting evidence confirmed and established" → *Subscriber*. (Trattini dell'originale resi con i due punti.)

> **Nota aggiunta:** "CS" nella slide è con ogni probabilità il *Credential Service Provider* (CSP) di NIST SP 800-63. Nella revisione SP 800-63-4 (2025) la classificazione delle evidenze resta FAIR, STRONG, SUPERIOR.

## 19. Standard e regolamenti dell'identità digitale: NIST SP 800-63 e livelli di garanzia eIDAS

*DI-05 @ 01:25:08*

Proprio perché l'identity proofing è la fase più critica, ci sono standard che normano tutto il ciclo di vita dell'identità digitale, "e soprattutto l'identity proofing". Il riferimento internazionale, "rivisto proprio quest'anno" anche per l'evoluzione delle minacce degli ultimi due anni, è **NIST 800-63** (*DI-05 @ 01:25:08-01:25:41*).

**Slide "Digital Identity standards and regulations", NIST** (*DI-05 @ 01:25:28*). Riquadro *NIST Digital Identity Guidelines*, `https://pages.nist.gov/800-63-3/`. Testo:

> *Digital* identity is the online **persona** of a subject (natural person, legal person, IT system, etc.). *Electronic* identity is a kind of digital identity which is legally accepted within a context (e.g. a State).
>
> Currently, NIST Guidelines divide the realm of digital identities into 3 categories, each with its LoAs: **IAL**, **AAL**, **FAL**, ranging levels **1** to **3**:
> A. Identity Proofing;
> B. Authentication and Lifecycle Management;
> C. Federation and Assertions.

Infografica NIST: *PASSWORD* + *MULTIFACTOR AUTHENTICATION* → *LOGGED IN*.

In Europa c'è il regolamento eIDAS: non tutti gli schemi di identificazione elettronica hanno lo stesso valore di sicurezza, e la norma, rifacendosi a uno standard ISO, definisce i **livelli di garanzia** (*levels of assurance*, LoA). Secondo il docente, lo standard ISO va da un LoA 0 "fino al 6 o al 5"; il regolamento scarta i più alti e i più bassi e prende i LoA **2, 3 e 4**, ribattezzati livello di garanzia **basso**, **significativo** (il docente dice "sostanziale") e **elevato** (il docente dice "alto") (*DI-05 @ 01:25:41-01:26:42*). Tutte le identità digitali notificate in Europa (per l'Italia **SPID**, **CIE** e il futuro **IT Wallet**) sono notificate con uno di questi livelli. Per esserlo, **l'intero schema** (identity proofing, ma anche tutte le fasi successive, incluse sospensione e revoca) deve soddisfare i requisiti di quel livello: se tutte le caratteristiche sono "sostanziali" lo schema è sostanziale; per essere "alto" devono esserlo **tutte**, e ne basta una sostanziale perché lo schema resti sostanziale (*DI-05 @ 01:26:42-01:27:44*).

Il rating serve per l'**identificazione transfrontaliera**: un cittadino tedesco con la sua smart card deve potersi autenticare a un servizio francese che nativamente supporta solo **FranceConnect**, o a uno estone, che supporta i documenti estoni o la SIM card ("in Estonia ci sono sei schemi, poi lo vedremo nella prossima lezione") (*DI-05 @ 01:27:44-01:28:18*).

**Slide "Digital Identity standards and regulations", eIDAS2** (*DI-05 @ 01:22:23*, poi *01:27:54*). Riquadro *eIDAS2 Regulation*, `https://eur-lex.europa.eu/eli/reg/2024/1183/oj`. Testo:

> Electronic identification (*Eid.*) is the process of using person identification data (PII) in electronic form uniquely representing a *natural person*, a *legal* person, or a *natural one representing a legal person*.
>
> Eid. *means* is a material or immaterial unit containing PII and used for online authentication.
>
> Eid. *scheme* is a system for Eid., whose Eid. means are issued to the above 3 kinds of persons.
>
> Currently, eIDAS Regulation provides for each MS to **notify** *at least* one Eid. scheme to the European Commission (**EC**), so that *notified schemes* (**eIDs**) can be peer-reviewed and become interoperable with each other for the mutual Eid. of EU citizens. eIDs may be certified pursuant to other legal acts.
>
> Each MS must provide at least for a national **EUDI Wallet** to be accessible by means of notified eID(s).
>
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
>
> \* eIDAS1 LoAs as currently *loosely* based on ISO 29115.

> **Correzione:** lo standard a cui si rifanno i livelli è **ISO/IEC 29115**, che definisce **quattro** livelli, LoA 1-4 (non una scala da 0 a 5 o 6, come detto a voce a *DI-05 @ 01:26:11*). eIDAS scarta solo il LoA 1 e fa corrispondere, "loosely" come dice la slide, basso, significativo ed elevato ai LoA 2, 3 e 4. Nella versione italiana del Reg. 910/2014 (art. 8) i livelli si chiamano "basso", "significativo" ed "elevato".

> **Nota aggiunta:** la revisione "di quest'anno" è **NIST SP 800-63-4**, pubblicata in versione finale nell'agosto 2025; la slide rimanda ancora alla versione 3. I requisiti tecnici dei livelli eIDAS sono nel Regolamento di esecuzione (UE) 2015/1502.

## 20. Autenticazione locale e client/server

*DI-05 @ 01:28:18*

Se l'identity proofing è critico, lo sono altrettanto le **autenticazioni** successive. Nel caso più semplice client e server **coincidono**: aprire il proprio laptop personale o sbloccare lo smartphone è un'autenticazione **locale**, perché i dati con cui si confrontano i fattori risiedono nel client che fa anche da server. Nei contesti aziendali, quando ci si logga su un terminale (laptop, tablet, smartphone, server), si sta parlando con un **server di identità** dell'organizzazione (*DI-05 @ 01:28:56-01:29:33*).

Il flusso (*DI-05 @ 01:29:33-01:31:10*): il client dice "mi voglio autenticare come Walter Arrighetti"; il server risponde con una **challenge**, cioè lo sfida a fornire uno, due o tre fattori; il client invia i fattori, "tipicamente hash cifrati" della password, dell'OTP, delle minuzie dell'impronta; il server li confronta e, se sono "sufficientemente realistici" o bit a bit identici a quelli attesi, concede l'autenticazione e rilascia un **token** di qualche tipo, una prova dell'autenticazione con cui si entra nel sistema. "Non entro sui dettagli informatici di quello che avviene post autenticazione, dettagli che sono nel mio lavoro fondamentali", perché dicono come attaccare queste autenticazioni. Da lì si è nel regime dell'**autorizzazione**: un sistema, non necessariamente il server d'identità, decide se si ha diritto di accedere a un file, postare, cancellare, acquistare.

**Slide "Local and client/server authentication"** (*DI-05 @ 01:30:39*). Testo:

> In the traditional setting, a user (not necessarily a natural person, it may be an IT system like an application or a PC), acting as a **client**, authenticates to an IT resource, acting as a **server** (e.g. file / web / email / video streaming platform, ...).
>
> A client authenticates with authentication factor(s), which the server acknowledges.
>
> Hardware (HSM, secure elements, ...) may be used with AAL2+ to store factors.
>
> Client and server may coincide (e.g. standalone logon to one's private device).

Schema: (1) *NEGOTIATE* `U = Username`; il server *Generate Challenge*; (2) *CHALLENGE* `C = 8abf92ee93e5a2d3`; il client calcola `H = LM-Hash(Password)`; (3) *AUTHENTICATE* `Encrypt(H, 8abf92ee93e5a2d3)`; il server fa *Check* (spunta verde o croce rossa).

> **Nota aggiunta:** lo schema è il challenge-response di **NTLM** (Microsoft), l'altro dei "due metodi di autenticazione" Windows a cui il docente accenna a *01:40:47* insieme a Kerberos. Con LM-hash e NTLMv1 la risposta è derivata dall'hash della password, che quindi funziona da segreto: è ciò che rende possibile il *pass-the-hash*. LM-hash è obsoleto e insicuro (password divisa in due metà di 7 caratteri, maiuscole, DES).

## 21. Autenticazione con smart card

*DI-05 @ 01:31:10*

Con un dispositivo fisico crittografico (**smart card**: anche i token USB e le **SIM** sono smart card; la SIM è "una smart card ritagliata" con solo il chip; il token USB "è andato fuori moda") nella card c'è la **chiave privata**, utilizzabile solo inserendo il **PIN** (tralasciando le carte di pagamento contactless per piccoli importi e alcune operazioni della CIE in cui basta avvicinarla) (*DI-05 @ 01:31:10-01:32:30*).

Il passaporto elettronico: lo si apre alla prima pagina sul lettore del gate perché nella copertina rigida c'è il chip, letto da un'antenna **NFC** a pochi millimetri. Nel contactless il lettore invia anche un **segnale di potenza** che accende a distanza il processore della carta, finché è vicina (*DI-05 @ 01:32:30-01:34:10*).

Il protocollo (*DI-05 @ 01:34:10-01:35:46*): il lettore manda un **blob** di dati (di solito codificato in base64), con una parte molto casuale e, nei pagamenti, informazioni come l'importo, e chiede il certificato a chiave pubblica e l'elaborazione del blob. Il chip chiede il PIN, cioè l'**autorizzazione a usare la chiave privata**; se concessa, la chiave privata nella smart card cifra il blob e lo restituisce; il lettore, con la chiave pubblica del certificato, verifica che il certificato sia valido e che il blob sia stato cifrato con la chiave privata associata: allora POS, lettore di documenti o lettore del PC è "sufficientemente sicuro che siete voi" e concede autenticazione, pagamento, apertura del tornello. Norme diverse: europee per l'identità basata su carta (eIDAS), **ICAO** per i documenti di viaggio, **EMV** e **PCI PTS** per le carte di pagamento.

**Slide "Smartcard authentication"** (*DI-05 @ 01:31:39*, ricompare a *01:35:39*). Testo:

> Smartcard authentication/authorization (e.g. card-based IDs; payment cards; ...) are **digital signing** processes. Their details depend on the specific technologies (e.g. eIDAS / ICAO; EMV / PCI PTS; ...) and involve PKIs with different complexities, yet it all goes down to the private-key stored in the card's SE signing a *blob* of data sent by the other party (web server; **id**entity **p**rovider; PoS/PoI; ...).

Diagramma (fonte Oracle): *End User*, *Smartcard*, *Middleware* (PC/SC Workgroup), *Authentication Server*: 1. Insert card, enter PIN at prompt; 2. Verify PIN; 3. Get challenge from server; 4. Sign challenge; 5. Verify signature on server; 6. Authentication status returned (con "HTTPS + Validation" fra middleware e server). Sotto (fonte WalletHub) il circuito di pagamento: *Cardholder*, *Merchant*, *Acquirer*, *Credit card network*, *Issuing bank*.

> **Nota aggiunta:** a voce il docente dice che il lettore chiede di "decifrare" i dati e che la carta "cifra" il blob con la chiave privata; la slide parla, più correttamente, di **firma** della challenge. Il lettore verifica la firma con la chiave pubblica del certificato. "SE" è il *secure element* della carta.

## 22. Single sign-on, riautenticazione e PIN dispositivo

*DI-05 @ 01:36:22*

**Single sign-on (SSO)**: ci si autentica a un sito o app e, passando a un altro sito o app **federato**, non si deve riautenticarsi, perché questo prende per buona la prova di autenticazione rilasciata la prima volta. Esempi: i servizi Microsoft (autenticati con l'identità Xbox, la posta e OneDrive non chiedono la password: "l'identità Microsoft è una sola"); i siti che permettono di autenticarsi "con Google", "con Amazon", "con LinkedIn". Di solito significa che questi soggetti si fidano l'uno dell'altro a livello di **identity provider** (*DI-05 @ 01:36:22-01:38:04*).

**Slide "Single sign-on (SSO)"** (*DI-05 @ 01:36:21*). Icone di identità federate (SAML, OpenID Connect, G Suite, Salesforce...), l'ecosistema Microsoft (Windows 10, OneDrive, Outlook.com, Xbox Live, Microsoft Account), un utente che con username e password passa da un unico SSO a Website A, B, C. Testo:

> With **single sign-on (SSO)** several RPs effectively *trust* each other.
>
> No further re-authentication by an IdP is required when users switch from RP to RP.
>
> The issue of *linking* different accounts, as long as they relate to the same natural/legal person, is also briefly introduced in **eIDAS2 Regulation**, which reads about «unique identification».
>
> This privacy issue is called **unlinkability**.

Il contrario dell'SSO è la **riautenticazione**: in banca ci si autentica, si vede il saldo, ma per un bonifico o per cambiare un dato del profilo viene richiesto di nuovo un fattore, per dimostrare di essere ancora la stessa persona davanti al computer. Un tempo era il **PIN dispositivo**: un PIN per entrare e uno per le operazioni dispositive, o lo stesso PIN richiesto più volte: un fattore, "in questo caso di possesso", che garantisce che l'utente davanti allo schermo è ancora lo stesso (*DI-05 @ 01:38:04-01:39:08*).

> **Nota aggiunta:** il docente classifica il PIN dispositivo come fattore "di possesso"; un PIN in sé è un fattore di **conoscenza** (sezione 15). Il senso è che la richiesta ripetuta serve a provare la presenza attuale del titolare.

**Slide "Re-authentication, SCA, and all the rest"** (*DI-05 @ 01:39:02*, scorsa velocemente). Testo:

> Hardening authentication via different strategies, which depend on the security posture of each organization / sector (e.g. the usage of SCA in the financial sector):
> - "Dynamic-link" OTPs, time-based and unique per transaction / operation = Strong Customer Authentication (**SCA**);
> - Re-authentication (e.g. for payment initiations pursuant to **PSD2**), *even* identity *re-proofing*;
> - remote-identification security controls.

Infografica: *KNOWLEDGE* (e.g. password, pin or ID number) + *OWNERSHIP* (e.g. mobile device, token or smartcard) + *INHERENCE* (e.g. fingerprint, face or voice recognition) + *DYNAMIC LINK* (*Transaction value*, *Transaction payee*).

Fra *01:39:08* e *01:39:36* scorrono in pochi secondi anche "Kerberos flow 3/3", "Digital Identity standards and regulations", "Centralized authentication" (*01:39:20*: utente, uno o più *service providers* o *relying parties*, un *identity provider*; "Data involved in identity proofing and authentication is electronically **seal**ed by the relevant CA/PKI of involved parties (both IdPs and RPs) in order to be acknowledged, even with legal relevance") e "Authentication example: Kerberos flow".

## 23. Kerberos

*DI-05 @ 01:39:08*

"Mi fermerei qui per oggi, però invece che parlare di questo vi parlo di Kerberos. Va rapidamente" (*DI-05 @ 01:39:08*).

**Kerberos** è nato "nei primi anni '90" nel mondo Unix, ma oggi è in ogni ambiente aziendale perché Microsoft lo ha adottato "fin dagli anni '90" come uno dei suoi due metodi di autenticazione, quello preferenziale. Nelle aziende Microsoft usa **Active Directory**, il cui fulcro è il **Domain Controller**: un server o una batteria di server on-premise o nel cloud Microsoft (**Entra ID**), con il registro delle identità del dominio. La scelta fu commerciale: le aziende avevano spesso server Unix (oggi per lo più Linux), e per gestire con un unico sistema utenze di laptop e server serviva almeno un protocollo di autenticazione omogeneo. Il nome è Cerbero, il cane a tre teste (citato da Dante, "degli antichi greci") (*DI-05 @ 01:39:40-01:41:52*). Per questo ci si autentica in azienda una o due volte al giorno.

Nella variante più semplice Kerberos usa **solo crittografia simmetrica**: all'epoca i computer non avevano librerie e potenza per la chiave pubblica in tempi ragionevoli, quindi si usarono algoritmi simmetrici rapidi, "peraltro anche abbastanza deboli, l'RC4". Per realizzare l'autenticazione con sola crittografia simmetrica serve uno schema complesso con **tre tipi di messaggi**. Non lo descrive nel dettaglio "perché è materia per specialisti informatici", ma ne racconta l'idea, perché schemi simili servono "per capire i wallet dell'identità digitale europea, nella prossima e ultima lezione" (*DI-05 @ 01:41:52-01:43:36*).

**L'analogia del luna park** (*DI-05 @ 01:43:36-01:46:53*), come gliela spiegò il suo primo docente di cybersecurity che gli parlò degli attacchi a Kerberos. L'azienda è un enorme parco giochi; i messaggi si chiamano **ticket** (oggi, in un protocollo web, li chiameremmo *authentication token*).
- Prima di entrare si compra il **biglietto d'ingresso**: il **TGT** (*Ticket Granting Ticket*), rilasciato dall'amministrazione del parco, il **Domain Controller** (nella tassonomia Kerberos il **Key Distribution Center**), al primo login.
- Con il biglietto d'ingresso si gira ma non si fa nulla: per ogni attrazione (roller coaster, mensa, persino il bagno) serve un biglietto specifico. In azienda, per stampare, scansionare, accedere a una cartella di rete o al portale interno serve un **service ticket** per quel servizio: lo si ottiene presentando il TGT ancora valido, senza pagare.
- I biglietti sono messaggi cifrati con chiavi **simmetriche**, che devono essere condivise in sicurezza fra due parti: "ecco dove sta la magagna", ecco perché lo schema è complesso.

Le **tre entità** (*DI-05 @ 01:46:53-01:48:31*): il **client** (il computer con cui ci si autentica), il **servizio** (per esempio il server di stampa al terzo piano dell'edificio N, mentre l'utente magari è in VPN) e il **Domain Controller**, che contiene tutte le identità e gli **hash delle password** di tutti gli utenti (non le password: capitolo 01). Client e utenza di servizio dialogano con il DC con una chiave simmetrica **derivata dalla password**, che la conoscono solo loro e il DC. Per questo il DC è "il barattolo del miele" dell'azienda: chi lo compromette e si impossessa del file delle chiavi "ha il dominio dell'azienda in pugno", ed è oggetto di tutte le misure di protezione logica e fisica.

Il flusso (*DI-05 @ 01:48:31-01:52:19*):
1. il client chiede l'autenticazione e il DC risponde con il **TGT**, cifrato con la chiave del **DC stesso**: il client lo possiede ma non può decifrarlo;
2. per stampare il client non si riautentica (non serve reinserire la password né far viaggiare un hash in rete): ripresenta il TGT al DC, che decifrandolo verifica che è proprio quell'utente e produce un **service ticket**, cifrato con la chiave dell'**account di servizio** del server di stampa, che il client non conosce;
3. il client presenta il service ticket al server di stampa ("vorrei stampare, sono Walter Arrighetti"); il server lo decifra con la chiave che condivide solo con il DC, verifica che il richiedente è quello indicato nel ticket (il DC sapeva chi era) e concede la risorsa **senza chiedere alcuna password**. Il client non può né leggere né contraffare il ticket.

È uno schema degli anni '90, ancora oggi il principale nelle reti aziendali, irrobustito con algoritmi moderni; in Windows si può realizzare anche con crittografia a chiave pubblica ("non vi spiego come si fa perché è ancora più complesso"): con l'app Microsoft Authenticator, una smart card o un token si sostituiscono alcune chiavi simmetriche con chiavi pubbliche le cui private stanno nel sistema di autenticazione, rendendo lo schema più sicuro (*DI-05 @ 01:52:19-01:53:21*). La lezione chiude rimandando "a domani per l'ultima lezione sulle identità digitali".

**Slide "Authentication example: Kerberos tickets"** (*DI-05 @ 01:46:39*, prima a *01:20:45*). Diagramma: *Active Directory*, *Domain Controller (DC)* che contiene il *Key Distribution Center (KDC)* con *Authentication Server (AS)* e *Ticket Granting Server (TGS)*; *Client*; *Hosting Server*. Messaggi: (1) AS_REQ, (2) AS_REP con il TGT, (3) TGS_REQ con il TGT, (4) TGS_REP con il service ticket, (5) AP_REQ con il service ticket, (6) [AP_REP] opzionale. Icone *Ticket-granting ticket* e *Service ticket*. Testo: "**Kerberos**: in its simplest scheme, only uses symmetric encryption although, to achieve authenticity whereas PKIs are commonly adopted nowadays. It employs a 3-way handshake involving two different types of "**ticket**s" exchanged between the user/client and 3rd IT systems." (Incisi fra trattini resi con i due punti e le virgole.)

**Slide "Authentication example: Kerberos flow"** (*DI-05 @ 01:20:59*, poi *01:48:40*). Client (C) con $\kappa_{\text{AS}}$; KDC (*Active Directory domain controller(s)*) con AS ($\kappa_{\text{AS}}$, $\kappa_{\text{TGS}}$) e TGS ($\kappa_{\text{TGS}}$, $\kappa_{\text{svc}}$); Service Server (SS) con $\kappa_{\text{svc}}$. Testo: "Flags in tickets/REQs/REPs encode special *Kerberos* and ActiveDirectory features (not to be discussed further, as they are optional / advanced features of AD, and because their functionalities' extension increases the complexity of tickets/REQs/REPs' structures). *Kerberos* **realm** ≈ Active Directory **domain**. These features are: **pre-authentication** (*very common & treated here*); hardware-based authentication (e.g. via physical tokens, smartcards, HSMs, ...); cross-domain/-forest/-realm authentication; constrained/unconstrained/resource-based constrained delegation; forwarding / proxying; access-token level impersonation; post-dating; ticket renewal / self-invalidation." **Legenda**, *long-term keys*:

$$\kappa_{\text{AS}} = \#\mathit{pwd}_{\text{usr}}, \quad \kappa_{\text{TGS}} = \#\mathit{pwd}_{\text{krbtgt}}, \quad \kappa_{\text{svc}} = \#\mathit{pwd}_{\text{svc}}, \qquad \kappa_{\text{Sess}} = \mathrm{rand}(), \quad \kappa_{\text{subSess}} = \mathrm{rand}()$$

dove $\#$ indica l'hash.

**Slide "Kerberos flow 2/3: service ticket (TGS)"** (*DI-05 @ 01:51:05*) e **"Kerberos flow 3/3: application (APP)"** (*DI-05 @ 01:28:38*, scorsa durante un'altra spiegazione). Il flusso completo: *Client Authentication* AS-REQ (User ID + requested service); AS-REP con **Msg A** (chiave di sessione cifrata con $\kappa_{\text{AS}}$) e **Msg B** (TGT: chiave di sessione + client + address + validity, cifrato con $\kappa_{\text{TGS}}$); *Client Service Authorization* TGS-REQ con **Msg C** (ID del servizio richiesto + TGT) e **Msg D** (client + timestamp cifrati con la chiave di sessione); TGS-REP con **Msg E** (service ticket: chiave di sotto-sessione + client + address + validity, cifrato con $\kappa_{\text{svc}}$) e **Msg F** (chiave di sotto-sessione cifrata con la chiave di sessione); *Client Service Request* AP-REQ con **Msg E** e **Msg G** (client + timestamp cifrati con la chiave di sotto-sessione); AP-REP con **Msg H** (timestamp), "optional mutual auth. reply". Note: $\kappa_{\text{Sess}}$ "Session key. Signs exchanges between C and TGS"; $\kappa_{\text{subSess}}$ "For exchanges between C and S"; AP-REQ "(non-standard)" con SPN (*Service Principal Name*), ST ticket, client name e timestamp. I dettagli dei riquadri della slide 2/3 a *01:51:05* (TGS-REQ, TGS-REP con PAC) sono in caratteri troppo piccoli: [illeggibile].

> **Nota aggiunta:** il nome è Cerbero della mitologia greca, poi ripreso da Virgilio e da Dante. Kerberos nasce al MIT (Project Athena) a metà degli **anni '80**; la versione 5 è del 1993 (RFC 1510, oggi RFC 4120). Microsoft lo ha adottato come protocollo predefinito con **Windows 2000** (Active Directory), quindi a cavallo del 2000 più che "dagli anni '90". Kerberos v5 originale usava **DES**; **RC4-HMAC** è stato introdotto proprio da Microsoft con Windows 2000 ed è oggi deprecato a favore di AES. La chiave $\kappa_{\text{TGS}}$ deriva dalla password dell'account speciale **krbtgt**: chi ne ottiene l'hash può forgiare TGT arbitrari (*golden ticket*); vedi anche la nota su Rubeus nella guida Cybersecurity, capitolo 06, sezione 14.

## 24. Glossario

| Termine | Significato nel corso |
|---|---|
| Firma digitale | Processo tecnico: cifratura con la chiave privata del firmatario dell'impronta di un dato; di per sé senza valore legale |
| Firma digitale ex DPCM firme | Nome giuridico italiano (DPCM 22/2/2013, CAD) per una specie di firma elettronica qualificata; da non usare nel corso |
| Firma elettronica (semplice) | Dati elettronici associati ad altri dati, usati da una persona fisica per firmare; valutabile da un giudice, non rifiutabile solo perché elettronica |
| Sigillo elettronico | Dati elettronici associati ad altri dati per garantirne origine e integrità; creatore è una persona giuridica |
| FEA, firma/sigillo avanzato | Firma/sigillo connesso unicamente al titolare, idoneo a identificarlo, creato sotto suo controllo esclusivo, che rileva modifiche successive |
| FEQ, firma/sigillo qualificato | Avanzato, creato con un QSCD e basato su un certificato qualificato di un QTSP; FEQ equivalente all'autografa in tutta l'UE |
| eIDAS | Reg. (UE) 910/2014, integrato da eIDAS 2 (Reg. (UE) 2024/1183): identificazione elettronica e servizi fiduciari |
| TSP, QTSP | Prestatore di servizi fiduciari; qualificato se accreditato e vigilato (verifica almeno biennale) |
| Trust mark | Marchio UE dei servizi qualificati (lucchetto azzurro con spunta e stelle); un'immagine, falsificabile |
| QSCD | Dispositivo qualificato per la creazione di firma/sigillo: la chiave privata non è estraibile, nemmeno dal QTSP |
| Certificato qualificato | Certificato X.509 emesso da un QTSP secondo gli allegati di eIDAS; dichiara la qualifica (qcStatements) |
| Inversione dell'onere della prova | Con una FEQ spetta al titolare dimostrare di non aver firmato |
| EUTL, LOTL | Elenco di fiducia europeo: la LOTL (XML sigillato dalla Commissione) punta agli elenchi nazionali sigillati dagli Stati |
| Enveloped | Firma inserita dentro il file firmato (PDF) |
| Enveloping | Firma come contenitore che racchiude il file (`.p7m`) |
| Detached | Firma in un file separato che referenzia il documento (`.p7s`) |
| ASiC | Contenitore di firma ETSI: uno ZIP con i file e una cartella META-INF con firme e certificati |
| Firma sequenziale | Ogni firma copre il documento con le firme precedenti ("matrioska"); cristallizza l'ordine |
| Firma parallela | Ogni firma copre il documento originale; firme paritetiche |
| Controfirma | Firma calcolata su una firma precedente, non sul documento (deleghe) |
| AdES, PAdES, CAdES, XAdES, JAdES | Formati ETSI di firma avanzata per PDF, CMS/PKCS#7, XML, JSON |
| B, T, LT, LTA | Livelli dei profili AdES: base, con marca temporale, con dati di validazione, con marche d'archivio |
| Signature wrapping | Attacco al formato/contenitore della firma (per esempio PDF) che fa sembrare valida una firma che non copre il contenuto mostrato |
| JWT, JWS | Token JSON in tre parti base64url separate da punti (header, payload, firma) |
| Harvest now, crack later | Raccogliere oggi dati cifrati o firmati per attaccarli in futuro |
| Marca temporale, TSA | Firma di una Time-Stamping Authority su impronta e orario: prova che il documento esisteva in quell'istante |
| PEC | Posta elettronica certificata italiana: servizio di recapito certificato elettronico in eIDAS |
| Autenticazione / autorizzazione | Dimostrare chi si è / stabilire cosa si può fare |
| Fattori di autenticazione | Conoscenza (something you know), possesso (something you have), inerenza (something you are) |
| Presentation attack | Presentare a un sensore biometrico un volto, un'impronta o una voce falsi |
| Digital twin, deepfake | Gemello 3D fotorealistico da VFX; contenuto sintetico generato con AI |
| Identity proofing | Fase in cui l'identity provider accerta l'identità reale e rilascia le credenziali; la più critica |
| IAL, AAL, FAL | Livelli NIST SP 800-63 per identity proofing, autenticazione, federazione |
| LoA eIDAS | Livelli di garanzia: basso, significativo, elevato (≈ ISO/IEC 29115 LoA 2, 3, 4) |
| Challenge | Sfida inviata dal server al client, a cui il client risponde con i fattori o una firma |
| SSO | Single sign-on: una sola autenticazione accettata da più servizi federati |
| SCA | Strong Customer Authentication (PSD2): due fattori più *dynamic link* alla transazione |
| PIN dispositivo | PIN richiesto di nuovo per le operazioni dispositive (riautenticazione) |
| Kerberos | Protocollo di autenticazione a ticket con crittografia simmetrica, usato in Active Directory |
| KDC, TGT, service ticket | Centro di distribuzione delle chiavi (nel Domain Controller); biglietto d'ingresso; biglietto per un servizio |

## 25. Punti incerti

- La finestra del certificato qualificato Banca d'Italia (*DI-05 @ 00:39:36-00:42:20*) non compare in nessun frame: i dati riportati (emittente, validità 20/02/2023-20/02/2028, uso non ripudio, RSA con SHA-256, allegato I) sono solo quelli detti a voce.
- *DI-05 @ 00:21:40*: "mi pare che al massimo duravano 10 anni i certificati all'epoca": non verificato.
- *DI-05 @ 00:28:28*: il nome del "firmarolo" (il fornitore di firme con OTP citato in chat da uno studente) non è comprensibile nell'audio: [?].
- La slide AdES di *DI-05 @ 00:52:30* è visibile solo nella prima voce (PAdES); il resto è saltato.
- Slide "Kerberos flow 2/3" (*DI-05 @ 01:51:05*): riquadri laterali [illeggibile].
- Teams 6 @ 0:29:03: l'autorità di vigilanza britannica pre-Brexit indicata dal docente ("se non sbaglio il Cabinet Office"); lo SI 2016/696 indica l'ICO, ma la verifica sulle fonti è rimasta non conclusiva.
- Teams 5 @ 0:39:18: sentenza di Cassazione 2026 sulle clausole vessatorie: estremi non detti, non verificata.
- Teams 6 @ 1:01:07: "nel 2018 un regolamento europeo" sulle marcature temporali con blockchain: non identificato.
- Teams 5 @ 0:49:57-0:52:48: il contenuto esatto degli artt. 56 e 61 del DPCM firme è riportato come detto dal docente; non riletto sul testo.
- *DI-05 @ 01:28:18*: "in Estonia ci sono sei schemi": non verificato (rimandato dal docente alla lezione successiva).

## 26. Esame

In questa lezione non ci sono indicazioni esplicite d'esame, né nel 2025 né nelle parti 2026 integrate. Ci sono invece diverse indicazioni su cosa è **di dettaglio** o fuori perimetro:

- "tutte altre proprietà metadati del certificato X509, di cui non vi parlo, perché sono dettagli per esperti di questo argomento, non vi interessano" (*DI-05 @ 00:42:20*);
- "Va bene, salto questa lezione sugli standard" (slide AdES, *DI-05 @ 00:52:31*);
- sull'attacco ai PDF: "se volete dettagli ... io non ho il tempo di mostrarveli" (*DI-05 @ 00:54:04*);
- sul *cross trust* post-Brexit: "ora non entro nei dettagli" (*DI-05 @ 00:34:59*);
- "Salto la parte di Kerberos che è per specialisti" (*DI-05 @ 01:20:40*), poi ripresa solo come idea: "non ve lo descrivo nel dettaglio perché è materia per specialisti informatici" (*DI-05 @ 01:43:01*); la versione a chiave pubblica: "non vi spiego come si fa perché è ancora più complesso" (*DI-05 @ 01:52:49*); la slide stessa dice che i flag di ticket e messaggi "not to be discussed further";
- sull'autenticazione: "non entro sui dettagli informatici di quello che avviene post autenticazione" (*DI-05 @ 01:30:38*);
- nel 2026: firme XML selettive, "troppo di dettaglio per il momento, non tratto" (Teams 6 @ 0:50:37); blockchain e registri distribuiti "non vi parlo ... perché avete fatto un corso a riguardo" (Teams 6 @ 0:53:49); molti servizi fiduciari "non lo farò per motivi di tempo" (Teams 5 @ 0:29:53).

Concetti su cui il docente insiste, utili come priorità di studio: la distinzione **firma digitale (tecnica) / firma elettronica (giuridica)** e il divieto di usare "firma digitale" nel senso del DPCM; firma (persona fisica, volontà di sottoscrivere) contro sigillo (persona giuridica, origine e integrità); i quattro requisiti della FEA e i due in più della FEQ; il principio di **non discriminazione** dei documenti elettronici; **fa fede il momento della firma** (Brexit, revoca, perdita della qualifica); la differenza fra **identity proofing** e **autenticazione** (nel 2026: "uno dei concetti fondamentali che vorrei passasse da qui alla fine del corso", Teams 6 @ 1:09:46, capitolo 06). Per il quadro completo vedi la pagina [Assessment](assessment.md).
