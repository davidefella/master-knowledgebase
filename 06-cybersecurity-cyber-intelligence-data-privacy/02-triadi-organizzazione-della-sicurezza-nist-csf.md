# 02 - Triadi, organizzazione della sicurezza, NIST CSF

> Fonte Notion: https://app.notion.com/p/3e712abc808d8178a79be76d02db97f0 — ultima modifica 2026-09-27T11:38:57.725Z

**Corso:** Cybersecurity, Cyber Intelligence and Data Privacy, docente Walter Arrighetti
**Registrazione:** CS-02 (portale, edizione 2025), Teams del 16/09/2025, durata 01:30:17
**Fonti:** solo la registrazione (parlato e slide a schermo). Il docente non ha distribuito materiale.
> **Contesto.** La lezione riprende quella del giorno prima ("ieri", più volte), cioè la lezione 1 del 15/09/2025, che **non è sul portale**: la pagina "lezione 1" carica un altro video. I rimandi a "ieri" (triade CIA, esempio della ricetta della Coca-Cola, discorso di von der Leyen, CrowdStrike) si riferiscono a quella lezione e qui restano come rimandi.
> **Guida unica.** Il capitolo segue la lezione 2025 (portale) e integra, nei riquadri "Integrazione Teams 2026", ciò che il docente ha aggiunto o cambiato nell'edizione 2026. Riferimenti: `CS-0N @` per il 2025, `Teams N @` per il 2026.
## Indice
1. Sicurezza informatica, cyber security, cyber resilience
2. La triade dei controlli di sicurezza
3. La triade della minaccia
4. La triade del rischio
5. Sicurezza organizzativa: SOC, NOC, CSIRT, CERT, ISAC
6. La triade dell'informazione: dati, informazioni, intelligence
7. Il NIST Cybersecurity Framework 2.0
8. Vettore d'attacco e superficie d'attacco
9. Il perimetro organizzativo: dal passato remoto al perimetro globale
10. Glossario
11. Punti incerti
12. Esame
---
## 1. Sicurezza informatica, cyber security, cyber resilience
*CS-02 @ 00:00:01*
La lezione si apre sulle differenze tassonomiche fra **sicurezza informatica**, **cyber security** e **cyber resilience** (o "resilienza cyber", come la chiama a volte la normativa europea). Il docente la colloca ancora nella parte introduttiva del corso e annuncia che sulla resilienza cyber si tornerà. La distinzione vera e propria fra cyber security e cyber resilience arriva con il framework NIST (sezione 7).
Il docente osserva che, soprattutto nei testi americani, la sicurezza si descrive spesso per **triadi**. La più importante resta la **triade CIA** (riservatezza, integrità, disponibilità), introdotta nella lezione precedente, che "ci accompagnerà in tutto questo corso e anche nel successivo", perché è centrale anche per il *digital trust*.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 02, sezione 1 (sicurezza informatica, triade CIA)*
- La triade CIA, data per nota nel 2025 ("introdotta ieri"), è spiegata per esteso: asset fisici, tecnologici e immateriali (le persone); riservatezza fino al **need to know**; integrità; disponibilità (Teams 1 @ 1:01:59). Vedi cap. 01, sez. 15.
- Paradigma della **ricetta della Coca-Cola** con budget infinito: la cassaforte perfetta per la riservatezza fallisce su integrità (chi rimette dentro cosa, chi la legge e si licenzia) e disponibilità (tre consiglieri su otto in presenza) (Teams 1 @ 1:04:06).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 1 (sicurezza informatica, cyber security, cyber resilience)*
Il 2025 si limitava ad annunciare la distinzione; il 2026 la sviluppa ampiamente.
- Sicurezza informatica e cyber security sono spesso usati come sinonimi fuori dal settore: approssimazione accettabile in conversazione, ma con differenze importanti. (Teams 2 @ 0:36:58 - 0:37:39)
- Sicurezza informatica: tutto ciò che protegge informazioni, dati e servizi IT dell'organizzazione. Disciplina già vastissima e trasversale: informatica teorica (crittografia, teoria dei codici), software (malware, antivirus), hardware (chip TPM, calcolo quantistico), processi; quasi ogni corso di informatica ha un omologo sulla sicurezza (compilazione sicura, sviluppo sicuro in C, Rust, Go, siti web, e-commerce). Comprende anche ambiti non informatici come l'informatica giuridica. (Teams 2 @ 0:37:39 - 0:40:40)
- Il sicurista informatico guarda soprattutto **verso l'interno** dell'organizzazione o della propria constituency. L'esperto di cyber security fa un lavoro simile ma è concentrato sulla **minaccia**, che proviene prevalentemente dall'esterno (nazioni ostili, terrorismo, attivismo, criminalità), guarda verso l'esterno e verso il futuro prossimo (due, tre, sei mesi). (Teams 2 @ 0:40:56 - 0:43:03, 0:47:08 - 0:47:38)
- Lo scenario della minaccia cambia per organizzazione e nel tempo, per congiunture tecnologiche (prodotti in dismissione, arrivo dei computer quantistici), politiche e geopolitiche, finanziarie, ambientali, normative (una legge che mette fuori uso un algoritmo o impone nuovi obblighi di notifica degli incidenti), sociologiche e psicologiche. (Teams 2 @ 0:43:16 - 0:44:56)
- Esempio: un gruppo specializzato nello sfruttare le vulnerabilità IoT della distribuzione del gas può spostarsi sul settore finanziario perché gli strumenti funzionano anche lì, perché è stato smantellato e si riforma, o perché è un attore statuale che cambia bersaglio per ordine del governo. Lo studio della minaccia è la cyber intelligence, mestiere diverso da quello del sicurista. (Teams 2 @ 0:45:29 - 0:47:08)
- Etimologia proposta: cyber security come crasi fra cyberspazio e information security. (Teams 2 @ 0:48:37)
- Cyber resilience: capacità di continuare a operare prima, durante e dopo un evento cyber, minimizzandone gli impatti e imparando dalle lezioni apprese. Si entra nella resilienza quando ci si chiede "che cosa fa la mia organizzazione se l'attacco riesce?". Il docente liquida come marketing lo slogan "non è più se sarete attaccati ma quando". Serve prima un programma di cyber security. (Teams 2 @ 0:49:26 - 0:51:07)
- Esempi: WannaCry ("se ti capita vuoi solo piangere"); un solo ransomware che passa può mettere offline un'intera organizzazione dotata di buone prassi di sicurezza ma non di resilienza. Caso recente citato: "pochi giorni fa" un attore della minaccia avrebbe impiantato un ransomware in un sito del governo tedesco e, senza riscatto pagato, pubblicato circa 6 TB di dati governativi \[?\]. (Teams 2 @ 0:51:22 - 0:52:44)
- Slide dei domini della cybersicurezza: molti domini in comune con quelli della sicurezza informatica, ma alcuni tipici della cyber security, come threat intelligence e awareness. La slide non è oggetto d'esame (vedi sotto). (Teams 2 @ 0:53:01)
## 2. La triade dei controlli di sicurezza
*CS-02 @ 00:00:36*
**Slide "The triad of security controls".** A sinistra tre colonne con icone: *Technical controls* (server, monitor con simbolo di pericolo, lucchetto), *Administrative controls* (documento, cartello di pericolo, figura con cappello e occhiali), *Physical controls* (telecamera, sbarra, cassaforte). A destra un diagramma a cerchi concentrici: al centro un triangolo verde "Information Systems" con i lati *Confidentiality*, *Integrity*, *Availability*; intorno, dall'interno verso l'esterno, gli anelli *Physical*, *Technical*, *Administrative*.
Il docente la definisce "leggermente meno rilevante" per il pubblico del master, perché riguarda soprattutto chi la sicurezza la applica ogni giorno. Il concetto: a presidio della sicurezza, anche dei dati, si mettono **controlli di sicurezza** di tre nature.
- **Controlli tecnici**, detti anche **di sicurezza logica**: tutto ciò che si fa con l'IT. Meccanismi di autenticazione, controllo degli accessi basato su ruoli o su attributi, firewall, ogni presidio hardware o software del mondo ICT, salvo eccezioni.
- **Controlli fisici**: agiscono su oggetti del mondo reale. Casseforti, sbarre, filo spinato, fossati, telecamere, bussole, badge identificativi, adesivi da portare sul vestito all'ingresso di un edificio.
- **Controlli amministrativi**, a volte detti **organizzativi**: norme, procedure, policy, buone condotte. Possono stare in un regolamento europeo, in un accordo interbancario, in un contratto fra privati o imprese, in un abbonamento, in condizioni d'uso, in una privacy policy, in uno standard tecnico o anche in una prassi non scritta. Criterio del docente: tutto ciò che non ha concretezza immediata né nell'IT né nel mondo materiale ma produce effetti, per esempio effetti giuridici.
I tre tipi possono concorrere insieme a proteggere gli asset.
### Non tutti i domini sono sempre pertinenti
*CS-02 @ 00:04:39*
Come per la CIA, di cui si è detto il giorno prima, non tutti e tre i domini sono necessariamente pertinenti in un caso specifico. L'esempio sono i **dati pubblici** e gli **open data**: vanno considerati nelle disponibilità di chiunque, compresi gli attori della minaccia, quindi la riservatezza pesa poco o nulla. Questo non rende meno importanti integrità e disponibilità.
- **Disponibilità.** Una pubblica amministrazione che per legge deve pubblicare dati per trasparenza non chiama l'esperto di sicurezza per renderli riservati, ma perché il sistema che li pubblica sia disponibile. Allo stesso modo gli oggetti su Amazon non sono riservati, ma l'indisponibilità del servizio produce un danno reputazionale ed economico.
- **Integrità, indipendente dagli altri due.** Un dataset pubblico aggiornato una volta l'anno può anche restare giù per ore o settimane, per un guasto e non per un attacco, senza un impatto rilevante. Ma se su quei dati qualcuno basa decisioni (investimenti in borsa, prestiti, prezzi di materie prime per un piano aziendale a due o tre anni) l'integrità diventa essenziale. Un dato modificato illegittimamente, un **dato avvelenato**, "può fare potenzialmente molti più danni di un dato mancante".
### Un esempio con tutti e tre i controlli
*CS-02 @ 00:10:48*
A volte una misura sta in un solo tipo di controllo, a volte serve una strategia che li combini. L'esempio del docente è un solo varco:
- il **cartello** ("vietato l'ingresso", "attenti al cane", l'obbligo di segnalare le telecamere per motivi di privacy) è un controllo **amministrativo**: di per sé non blocca nessuno, è un **deterrente** o un obbligo di legge;
- il **cancello**, il muro con i cocci di vetro, il filo spinato sono controlli **fisici**: bloccano materialmente l'accesso, anche senza cartello;
- il **lettore di badge** con il suo metodo di autenticazione è un controllo **tecnico/logico**: l'oggetto è fisico, ma l'autenticazione (nome, password, biometria) è un processo logico. Il docente rimanda al corso di Digital Trust.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 02, sezione 2 (non tutti i domini sono pertinenti: dati pubblici)*
- Esempio nuovo: il ministero che pubblica il numero di laureati; dato pubblico, ma la sua disponibilità, anche durante un attacco, è un compito di sicurezza (Teams 1 @ 1:08:33).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 2 (triade dei controlli) e Capitolo 04, sezione 12 ("Types of threat")*
- Denominazioni: controlli fisici, tecnici o logici (sicurezza tecnologica), amministrativi o organizzativi. Per il digital trust i controlli presidiano anche l'autenticità. (Teams 2 @ 0:15:47)
- La slide "Types of threat", saltata nel 2025, viene commentata: le minacce si esprimono in quattro tipi, intercettazione, interruzione, modifica e fabbricazione di informazioni (per esempio informazioni false). Il docente la definisce classificazione "molto accademica" e "un po' antiquata", utile per capire che i controlli servono a prevenire o individuare queste tipologie. (Teams 2 @ 0:16:58)
## 3. La triade della minaccia
*CS-02 @ 00:14:29*
**Slide "The Triad of Threat".** Diagramma di Venn con tre cerchi: *capability*, *hostile intent*, *opportunity*. Al centro, dove si intersecano tutti e tre, **Threat**. Le intersezioni a due sono etichettate:
- *capability* ∩ *hostile intent* (senza opportunità): **impending**
- *capability* ∩ *opportunity* (senza intento): **potential**
- *hostile intent* ∩ *opportunity* (senza capacità): **insubstantial**
A destra le definizioni:
- **(Hostile) Intent**: the purpose and motivations of the attack.
- **Capability**: the adversary's tradecraft and knowledge, as well as the tactics, techniques and procedures (TTPs) that may/shall be used.
- **Opportunity**: availability of means with which a threat actor can achieve its goals.
Fra le molte definizioni di minaccia, il docente preferisce quella degli ambienti di **Cyber Threat Intelligence**: c'è minaccia solo dove si combinano tre elementi.
1. **Intento ostile.** Qualcuno deve voler attaccare; senza intento manca una componente fondamentale.
2. **Capacità.** Tipicamente tecnica, ma in astratto anche la disponibilità di risorse umane competenti (hacker "a cappello nero") e, ancora più a monte, di risorse finanziarie: "nessuno lavora gratis".
3. **Opportunità.** La disponibilità di mezzi per raggiungere l'obiettivo. Esempi: essere geograficamente troppo lontani per un certo attacco; oppure, per un attacco cyber dove la distanza non conta, non avere le credenziali minime per entrare nel sistema, che "vedo da fuori e da fuori non riesco a far nulla".
Senza tutti e tre si ha qualcosa di imminente ma non reale, non sostanziato o solo potenziale. Nei report di cyber intelligence la minaccia si descrive proprio attraverso questi tre elementi.
### Attore della minaccia e attribuzione
*CS-02 @ 00:17:13*
Identificare una minaccia può essere relativamente semplice; identificare **chi** la perpetra spesso non è possibile, perché non si riesce ad "affibbiare un volto". Nel gergo si parla di **gruppo di minaccia** o **attore della minaccia** (*threat actor*); nel corso sono sinonimi e il docente userà "attore della minaccia".
L'attore non è necessariamente una persona o un gruppo di persone fisiche: può essere un'entità solo logica. Se abbiamo evidenza soltanto di un malware installato su un dispositivo o su una famiglia di dispositivi, e non siamo ancora riusciti a risalire a chi c'è dietro, lo chiamiamo comunque attore della minaccia, perché ha messo in atto la minaccia. L'**attribuzione**, cioè associare l'attore a una persona, un gruppo, uno stato o un gruppo criminale, non è sempre possibile.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 3 (triade della minaccia)*
- Chi descrive la minaccia (intento, capacità, opportunità) non è di solito il sicurista informatico ma l'esperto di cyber threat intelligence; chi attiva un controllo di sicurezza lo fa pensando a una minaccia precisa, che prima va sostanziata con le tre caratteristiche. (Teams 2 @ 0:09:16)
- Capacità: oltre a strumenti hardware e software, include un insieme di persone capaci di portare l'attacco. Analogia nuova: il cane piccolo che abbaia al cane grande non è una vera minaccia, perché manca la capacità. (Teams 2 @ 0:07:50, 0:08:17)
- Opportunità: spesso coincide con una vulnerabilità sfruttabile, ma non necessariamente. Se mancano uno o più elementi si parla di minaccia potenziale, insostanziale o non immediata. (Teams 2 @ 0:08:35)
- L'attore della minaccia è spesso un'entità astratta, identificata solo dall'evidenza delle tre caratteristiche (coerente con il 2025). (Teams 2 @ 0:10:15)
## 4. La triade del rischio
*CS-02 @ 00:19:17*
**Slide "The Triad or Risk"** (sic, nel titolo della slide). Venn con *Threat*, *Asset*, *Vulnerability*; l'intersezione dei tre, in rosso, è indicata come **Risk**. Nella versione completa (a schermo da 00:22:16) compaiono le definizioni:
- **Threat**: event or action that may negatively affect an organisation's assets, roles, reputation.
- **Asset**: anything that has a value to an organisation (real estates, ICT systems, software, IP, employees, **data**, …).
- **Vulnerability**: weakness that can be exploited by a threat (actor).
- **Risk**: effect of uncertainty on objectives.
Per esserci rischio servono tre cose.
1. Una **minaccia**, che a sua volta è la triade della sezione 3.
2. Un **asset**: qualunque cosa abbia valore per un'organizzazione. Il docente cita la ISO 27005 "se non sbaglio". Sono asset il palazzo, il computer, il software, gli impiegati ("senza il fattore umano non si va avanti"), la clientela, la proprietà intellettuale e più in generale i dati. \[?\] Segue una frase trascritta male ("Per esempio di Yauuma è evidente che oggi il valore economico può essere dato anche astrattamente ai soli dati"), CS-02 @ 00:20:43.
3. Una **vulnerabilità**: una debolezza specifica nell'asset, o in qualcosa accanto all'asset, che se sfruttata dalla minaccia può comportare una perdita di valore. È potenziale, perché può essere sfruttata.
Il fattore economico entra dall'asset. Se la minaccia riguarda un asset, le si associa un valore che può essere uguale, inferiore o **superiore** al valore dell'asset: la distruzione anche parziale di un asset può produrre, per esempio, un danno reputazionale molto maggiore del suo valore.
Il rischio è l'effetto delle **incertezze**: possiamo aver identificato una vulnerabilità e una minaccia senza sapere se la minaccia sfrutterà mai la vulnerabilità. Per questo serve la **probabilità**, che il docente riprenderà parlando di sicurezza amministrativa. Il rischio si definisce, numericamente o qualitativamente, come il **prodotto** fra la probabilità che l'evento accada e il controvalore associato al caso in cui accade.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 4 (triade del rischio)*
- Il docente annuncia che darà più avanti, con la sicurezza organizzativa, una definizione "più moderna, più pratica" di rischio e il suo calcolo; qui non riprende la formula probabilità per controvalore. (Teams 2 @ 0:17:51, 0:24:46)
- Approccio basato sul rischio: non si può investire ogni risorsa per proteggere tutto, e non tutto ciò che è proteggibile va protetto con lo stesso investimento. (Teams 2 @ 0:18:34)
- Esempio nuovo con le chiavette USB: asset presente e minaccia reale, ma se le porte sono bloccate manca la vulnerabilità e quindi il rischio. Modi per bloccarle: lucchetti fisici con chiave, ceralacca, adesivi tamper-proof (che non impediscono l'uso ma rivelano se qualcuno ha manomesso la porta), blocchi a livello di sistema operativo, firmware o software di terze parti, anche solo per consentire mouse e tastiera. (Teams 2 @ 0:21:02 - 0:22:46)
- Il rischio va sempre calato sull'organizzazione: la stessa analisi non si può trasferire da un'organizzazione A a una B, anche con la stessa infrastruttura e lo stesso consulente di sicurezza, perché un settore diverso (PA contro un'azienda di lacci da scarpe) attira attori della minaccia diversi con modus operandi diversi. (Teams 2 @ 0:23:03 - 0:24:39)
## 5. Sicurezza organizzativa: SOC, NOC, CSIRT, CERT, ISAC
*CS-02 @ 00:23:33*
**Slide "Organisational security".** Venn con tre cerchi: **SOC** (*Technology*), **CSIRT** (*Business*), **CERT** (*Threat Intelligence*). Intersezioni: SOC ∩ CSIRT = *Response*; SOC ∩ CERT = *Prevention*; CSIRT ∩ CERT = *Guidelines*; centro = *Understanding*. A destra:
- **SOC**: Security Operations Centre
- **CSIRT**: Computer Security Incident Response Team
- **CERT®**: Computer Emergency Response Team (® trademark owned by Carnegie Mellon University)
- **ISAC**: Information Sharing and Analysis Centre, in un colore diverso e staccato dagli altri tre
Anche questa triade è "meno rilevante ai vostri fini". Si tratta delle strutture preposte alla sicurezza informatica di un'organizzazione. Non sono necessariamente tutte presenti né tutte distinte: una piccola azienda familiare che fa lacci da scarpe può non averne nessuna, o averne una che fa tutto, magari esternalizzata. All'estremo opposto esistono tutte e tre, separate.
**SOC (Security Operations Centre)** *CS-02 @ 00:25:14*
Centro delle operazioni di sicurezza tecniche. Monitora gli **eventi di sicurezza**, che non sono solo attacchi: anche un computer che non si avvia, un hard disk che si rompe, una connessione che salta o non è abbastanza performante. Interviene anche nel continuo per mettere in sicurezza i sistemi, per esempio con una policy per applicare le patch a tutti i sistemi vulnerabili nel minor tempo possibile senza impattare il business.
**NOC (Network Operations Centre)** *CS-02 @ 00:26:09*
Può essere separato dal SOC, coincidere con esso, contenerlo o esserne contenuto. È dedicato alle performance della rete e alla qualità del flusso dei dati; il SOC è specializzato nella sicurezza.
**CSIRT (Computer Security Incident Response Team)** *CS-02 @ 00:27:35*
Può essere un sottoinsieme del SOC con competenze specifiche, lavorare in concerto con esso o esserne separato. Il suo compito è rispondere **prontamente** agli incidenti cyber. Serve sempre di più perché la minaccia agisce in tempi rapidissimi: l'attore della minaccia si prende il suo tempo per restare nel sistema e studiarne i punti deboli, ma quando agisce agisce in pochissimo tempo, con danni spesso economicamente incalcolabili (esempi: DoS, ransomware).
I CSIRT sono stati introdotti nella normativa primaria europea con la **direttiva NIS**, che prevede anche che si consorzino nella **rete dei CSIRT** di tutti i paesi europei. Oltre ai CSIRT di organizzazione esistono CSIRT (e SOC) **di settore** ed esternalizzati, pensati per PMI e piccole amministrazioni locali che non potrebbero mantenere un pronto intervento per una minaccia "che magari per n anni non si sostanzierà mai". La direttiva NIS prevede CSIRT di settore; nel privato sono spesso servizi a pagamento, con un modello di business concreto.
**CERT (Computer Emergency Response Team)** *CS-02 @ 00:32:22*
"CERT" è un marchio della Carnegie Mellon University, che lo ha introdotto per prima e richiede un **processo di accreditamento** a chi vuole usarlo. Molti CSIRT diventano CERT quando ottengono l'accreditamento; i compiti coincidono sempre di più. Ai CERT sono affidati sempre più spesso anche compiti di **cyber threat intelligence**, cioè ricerca e studio della minaccia.
**Analogia sanitaria del docente.** Il SOC è l'ospedale nella sua interezza e si occupa del *day by day*. Il CSIRT è il pronto soccorso, incardinato o meno nell'ospedale. Il CERT è l'istituto di ricerca medica, che a volte (come nei policlinici) sta dentro l'ospedale.
**ISAC (Information Sharing and Analysis Centre)** *CS-02 @ 00:34:37*
Introdotto da poco anche nella normativa europea, "anche se non ha necessariamente questo nome". Opera tipicamente per un settore merceologico o istituzionale (sanità, finanza, difesa): raccoglie informazioni di threat intelligence dagli affiliati e le ridistribuisce a tutti. Il riferimento è alla frase di von der Leyen citata il giorno prima: se tutto è interconnesso tutto è hackerabile, e per essere eccellenti nella cyber security bisogna "fare sistema". L'unico modo per difendersi da una minaccia **asimmetrica** è conoscere ciò che è successo a chi è stato meno fortunato.
Paragone del docente: le **riunioni di morbilità e mortalità** degli ospedali americani, in cui i reparti discutono i casi andati male e ne traggono lezioni, a volte pubblicate. Gli ISAC fanno lo stesso a livello plurisettoriale e internazionale, con in più un compito di **filtro**: anonimizzano le informazioni che rivelerebbero chi è stato colpito, dettagli tecnici o segreti industriali, conservando il contenuto utile per tutti. Esempio: un gruppo criminale telefona fingendosi il supporto tecnico di Linux; l'ISAC raccoglie i dati dalle vittime e redistribuisce una descrizione tecnicamente completa (nomi dei file, caratteristiche del malware) senza dire chi è stato attaccato. Il docente accenna a "due problematiche in più" che gli ISAC risolvono, ma rinvia i dettagli.
### Constituency
*CS-02 @ 00:39:29*
SOC, CSIRT e CERT agiscono di solito per la propria organizzazione, ma possono essere di settore. Gli ISAC sono sempre extra-organizzazione, per questo il docente li tiene fuori dalla triade. La **constituency** di ciascuno è l'insieme dei soggetti verso cui sono rivolte le sue operazioni. Per una struttura aziendale è l'organizzazione, eventualmente con alcuni fornitori o clienti. Per una struttura di settore, e sempre per un ISAC, deve essere ben definita, perché determina con chi comunicare, chi proteggere e come agire.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 02, sezione 5 (ISAC e fare sistema)*
- Obblighi di notifica e condivisione come risposta al silenzio delle vittime: il caso Yahoo mostra perché le aziende tacciono (danno reputazionale, titolo in borsa); oggi leggi europee e non solo impongono ai soggetti grandi o critici meccanismi di reporting; la maturità consiste nell'affrontare la minaccia insieme (Teams 1 @ 0:21\:02-0\:23:01).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 5 (SOC, CSIRT, CERT, ISAC)*
- Il docente la presenta come "triade delle operazioni di sicurezza". Il NOC non viene nominato. (Teams 2 @ 0:25:02)
- SOC: può essere interno, in outsourcing o erogato come SOC as a service da terzi che monitorano più organizzazioni. Analogia nuova: chi si installa telecamere di casa e le guarda da solo sul cellulare, contro chi si affida a un servizio di vigilanza che lo chiama se vede qualcosa. Il SOC monitora anche in assenza di incidenti, 24 ore su 24. (Teams 2 @ 0:25:43 - 0:27:27)
- CSIRT: si attiva in caso di incidente rilevato o sospetto. La direttiva NIS2 obbliga alcuni settori importanti e critici a dotarsi di CSIRT, che devono collaborare e scambiarsi rapidamente informazioni sugli incidenti. (Teams 2 @ 0:26:54, 0:27:27)
- CERT: l'accento è sulla parola "emergency", intesa come minaccia emergente anche nel medio e lungo periodo, non come risposta immediata all'incidente; per questo la threat intelligence è una delle sue funzioni principali. (Teams 2 @ 0:28:03)
- Differenza CSIRT/CERT: molti pensano che un CSIRT sia solo un CERT senza il marchio, ma secondo il docente la differenza c'è. Le organizzazioni mature possono avere entrambi, in combinazioni diverse di interno e outsourcing; altre hanno solo SOC e CSIRT, a seconda dell'appetito di rischio e della postura di sicurezza. (Teams 2 @ 0:29:09 - 0:29:41)
- Molte PMI italiane non hanno nessuna delle tre strutture, nemmeno in outsourcing, e sono quindi particolarmente esposte; il docente cita un report del 2023 \[?\]. (Teams 2 @ 0:29:58)
- ISAC come "quarto vertice": il docente parla quasi di un tetraedro. Nuovo il ragionamento sulla constituency del SOC as a service: l'insieme dei clienti paganti, fra i quali di norma il SOC non trasmette informazioni sugli incidenti; lo scambio fra soggetti diversi è il compito degli ISAC. (Teams 2 @ 0:30:31 - 0:32:25)
### Integrazione Teams 2026 (lezione 2 2026)
*Il ruolo del CISO e la percezione della sicurezza come centro di costo*
Assente nei manuali 2025 (che in sezione 7 parlano di governance solo in termini di ruoli e responsabilità). Punti chiave (Teams 2 @ 0:58:41 - 1:01:34):
- la cybersicurezza è spesso vista come puro costo perché il ritorno dell'investimento non è misurabile quando le cose vanno bene;
- la governance richiede una linea di reporting, di management e di spesa;
- il CISO può mancare, essere ad interim (CIO, CTO), stare sotto CIO o CTO, oppure essere un vero C-level che parla con il board;
- deve saper tradurre requisiti e scenari di rischio per il vertice.
## 6. La triade dell'informazione: dati, informazioni, intelligence
*CS-02 @ 00:40:48*
**Slide "The Triad of Information".** Una freccia che si restringe da sinistra a destra: *Operational Environment* → **Data** → **Information** → **Intelligence**, attraversando tre lenti etichettate *Collection*, *Processing and Exploitation*, *Analysis and Production*. Nella versione completa (da 00:43:00) a sinistra:
- **Data**: set of "raw" values and individual elements. Usually gathered and/or produced as part of automatic or semi-automatic processes.
- **Information**: collection of enriched data that, alone, can be used to answer to simple questions.
- **Intelligence**: curated information that stakeholders can immediately consume to take high-level decisions.
**Dati.** Insiemi di valori grezzi riferiti a elementi individuali, spesso molto granulari. Si parte sempre da dati il più possibile grezzi, "immacolati" e completi. L'analogia è il formato **RAW** della fotografia: il fotogramma salvato senza elaborazione permette di tornare indietro e ripartire da un'analisi nuova. Una foto già ridotta, in bianco e nero e con il filtro "beauty" va bene sullo smartphone, ma è inutilizzabile per stampare un poster 80×80.
**Informazioni.** Dai dati grezzi non si estrae direttamente la risposta alle domande: bisogna trattarli, con processi automatici o semiautomatici, soprattutto con i big data (esempio: i video di tutte le telecamere del mondo). Le informazioni sono una variante arricchita dei dati, frutto di uno o più processi di sintesi, e rispondono a domande semplici, "di tipo semplice" per uno sviluppatore: sì/no, quanto, quando, a che temperatura.
**Intelligence.** A volte il processo si ferma alle informazioni. Ma chi prende decisioni di altissimo livello (board, amministratore delegato, ministro) spesso non ha competenze tecniche e non entra nel merito. Serve allora distillare dalle informazioni l'**intelligence**, che deve essere **actionable**: costruita in modo che il decisore possa decidere direttamente. "Parlare in termini semplici non vuol dire semplificare il problema, vuol dire saperlo costruire dando a chi deve decidere tutti gli elementi."
Il docente prevede che questo lavoro sarà sempre più supportato dall'intelligenza artificiale, ma per ora l'elemento umano resta dirimente. La distinzione fra dati, informazioni e intelligence è meno netta di quella fra controllo fisico e logico, ma è fondamentale per la cyber intelligence, a cui è dedicata una parte del corso.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 02, sezione 6 (triade dell'informazione)*
- Nuovo esempio del **data center**: sensori di temperatura e umidità, dashboard per il responsabile dei sistemi e per la facility, decisione strategica a 2-3 anni del board (nuovo data center, sito più freddo, fornitore elettrico) come prodotto di intelligence (Teams 1 @ 0:58:34).
- L'intelligence può essere distillata in modo automatico, ma richiede una verifica umana contro le **allucinazioni** dell'AI; la raccolta è automatizzata dall'era industriale, l'estrazione di informazioni in gran parte (Teams 1 @ 1:00:44).
## 7. Il NIST Cybersecurity Framework 2.0
*CS-02 @ 00:47:41*
A schermo compare brevemente la slide di sezione **"Introduction: Information Security principles"**, poi **"The NIST Cybersecurity Framework 2.0"**: una ruota con al centro *NIST Cybersecurity Framework*, un anello interno **GOVERN** e, intorno, **IDENTIFY**, **PROTECT**, **DETECT**, **RESPOND**, **RECOVER**. A sinistra le scritte **CYBERSECURITY** (collegata alla parte alta della ruota) e **CYBER RESILIENCE** (collegata a Respond, segnata da una stella).
### Perché un framework
È il quadro di riferimento di cyber security più adottato a livello internazionale e serve a capire la differenza fra cyber security e cyber resilience. Il docente ricorda che è stato aggiornato alla versione 2.0 ("l'anno scorso, no, due anni fa… ho visto dei draft, quindi non ricordo quando è stato ufficialmente pubblicato").
> **Nota aggiunta:** il NIST CSF 2.0 è stato pubblicato ufficialmente il 26 febbraio 2024. Rispetto alla registrazione (settembre 2025) era quindi "l'anno scorso".
È un quadro che le organizzazioni possono adottare per impostare la cyber sicurezza al proprio interno. L'uso dei framework (il docente lo riprenderà con la sicurezza amministrativa) serve a riferirsi sempre alla **stessa tassonomia**, soprattutto nelle interazioni con altri soggetti: la cyber security non si fa da soli, e argomenti complessi e riservati vanno descritti "parlando la stessa lingua". Il NIST è l'organo di standardizzazione tecnologica americano, ma molti suoi standard (cyber security, crittografia, identità digitale) hanno un'eco internazionale e diventano riferimento ovunque, anche in ambito di governance.
### Cyber security e cyber resilience
*CS-02 @ 00:50:37*
Il framework chiede di mettere in atto processi di cyber security e processi di cyber resilience. La differenza sta nel **momento** in cui agiscono rispetto a un evento di sicurezza. Già nella versione precedente c'erano **cinque famiglie di attività**.
**Cyber security: prima e durante l'evento.**
- **Identify.** Nella descrizione del docente: controlli (fisici, logici e amministrativi) che servono a individuare una minaccia che sta per avvenire o sta avvenendo. Ne fa parte lo studio della minaccia cyber che non ha ancora colpito la mia azienda ma colpisce il mio paese, paesi affini o il mio settore (esempio: attacchi sistematici alle filiere delle centraline elettroniche per chi produce automobili). La cyber threat intelligence ricade in parte qui.
- **Protect.** Controlli che, anche se la minaccia arriva, le impediscono di impattare l'azienda.
- **Detect.** Avviene "in quell'istante".
L'analogia del docente: la vedetta sul muro che osserva la strada e il posto di blocco dove mostri i documenti sono *identify*; il muro e il filo spinato sono *protect*; la telecamera davanti alla porta è *detect*.
> **Correzione:** nel CSF 2.0 la funzione **Identify** riguarda la comprensione dei rischi dell'organizzazione: asset, valutazione del rischio, supply chain, miglioramento (vedi la tabella sotto: [ID.AM](http://ID.AM), ID.RA, [ID.SC](http://ID.SC), [ID.IM](http://ID.IM)). Individuare eventi in corso è invece compito di **Detect** ([DE.AE](http://DE.AE), [DE.CM](http://DE.CM)). La parte della spiegazione sulla conoscenza anticipata della minaccia e sulla threat intelligence è coerente con Identify (ID.RA comprende la threat intelligence); il riferimento alla minaccia "che sta avvenendo" no.
**Cyber resilience: dopo l'evento.** *CS-02 @ 00:54:55*
- **Respond.** L'evento è accaduto: non ci si fa trovare impreparati, si risponde (attacco incluso) per minimizzare gli impatti, imparare e migliorare.
- **Recover.** Dati distrutti, fondi sottratti: assicurazioni, backup, immagini sane dei dischi, una sede alternativa da cui ripartire. Il recupero riporta il sistema all'operatività originale. Spesso conta più della risposta, soprattutto quando la disponibilità è essenziale e il business è *time critical* ("ogni minuto conta, ogni secondo conta").
### Govern
*CS-02 @ 00:56:45*
La versione 2.0 ha introdotto come novità diverse fasi, \[?\] "come quella dedicata all'evoluzione della minaccia, tra le quali c'è anche la formazione nel continuo", ma soprattutto la funzione fondamentale di **governance**. Governance e rischio non sono concetti inventati da chi fa sicurezza ("i sicuristi") ma dai manager d'impresa, ed esistono anche nel pubblico, rispetto ai compiti istituzionali.
Portare la gestione della cyber sicurezza dentro un processo di governance significa avere chiare le strategie, il contesto in cui l'azienda opera (per distinguere le minacce rilevanti da quelle che non lo sono) e soprattutto **ruoli e responsabilità** di ciascun organo aziendale. Esempi di decisioni di governance: avere o no un SOC interno, un CSIRT, un servizio di threat intelligence interno o esterno. Dato il valore dei dati per le aziende, sono decisioni che chi si occupa di sicurezza dei dati deve conoscere.
### Tabella delle categorie CSF 2.0
*CS-02 @ 00:58:44* (e di nuovo @ 01:07:08, con Govern e Identify evidenziati)
A schermo, accanto alla ruota, la tabella delle categorie. Il docente non la commenta voce per voce.
<table header-row="true">
<tr>
<td>Function</td>
<td>Category</td>
<td>Identifier</td>
</tr>
<tr>
<td>Govern (GV)</td>
<td>Organizational Context</td>
<td>GV.OC</td>
</tr>
<tr>
<td></td>
<td>Risk Management Strategy</td>
<td>GV.RM</td>
</tr>
<tr>
<td></td>
<td>Roles and Responsibilities</td>
<td>GV.RR</td>
</tr>
<tr>
<td></td>
<td>Policies and Procedures</td>
<td>GV.PO</td>
</tr>
<tr>
<td>Identify (ID)</td>
<td>Asset Management</td>
<td>[ID.AM](http://ID.AM)</td>
</tr>
<tr>
<td></td>
<td>Risk Assessment</td>
<td>ID.RA</td>
</tr>
<tr>
<td></td>
<td>Supply Chain Risk Management</td>
<td>[ID.SC](http://ID.SC)</td>
</tr>
<tr>
<td></td>
<td>Improvement</td>
<td>[ID.IM](http://ID.IM)</td>
</tr>
<tr>
<td>Protect (PR)</td>
<td>Identity Management, Authentication, and Access Control</td>
<td>PR.AA</td>
</tr>
<tr>
<td></td>
<td>Awareness and Training</td>
<td>[PR.AT](http://PR.AT)</td>
</tr>
<tr>
<td></td>
<td>Data Security</td>
<td>PR.DS</td>
</tr>
<tr>
<td></td>
<td>Platform Security</td>
<td>[PR.PS](http://PR.PS)</td>
</tr>
<tr>
<td></td>
<td>Technology Infrastructure Resilience</td>
<td>[PR.IR](http://PR.IR)</td>
</tr>
<tr>
<td>Detect (DE)</td>
<td>Adverse Event Analysis</td>
<td>[DE.AE](http://DE.AE)</td>
</tr>
<tr>
<td></td>
<td>Continuous Monitoring</td>
<td>[DE.CM](http://DE.CM)</td>
</tr>
<tr>
<td>Respond (RS)</td>
<td>Incident Management</td>
<td>[RS.MA](http://RS.MA)</td>
</tr>
<tr>
<td></td>
<td>Incident Analysis</td>
<td>RS.AN</td>
</tr>
<tr>
<td></td>
<td>Incident Response Reporting and Communication</td>
<td>[RS.CO](http://RS.CO)</td>
</tr>
<tr>
<td></td>
<td>Incident Mitigation</td>
<td>RS.MI</td>
</tr>
<tr>
<td>Recover (RC)</td>
<td>Incident Recovery Plan Execution</td>
<td>RC.RP</td>
</tr>
<tr>
<td></td>
<td>Incident Recovery Communication</td>
<td>[RC.CO](http://RC.CO)</td>
</tr>
</table>
> **Nota aggiunta:** la tabella a schermo è riportata fedelmente. Nel CSF 2.0 la categoria GV.OC è accompagnata anche da [**GV.SC**](http://GV.SC) (Cybersecurity Supply Chain Risk Management) e **GV.OV** (Oversight), e la gestione del rischio della supply chain sta in Govern, non in Identify. La voce "[ID.SC](http://ID.SC)" e l'assenza di [GV.SC/GV.OV](http://GV.SC/GV.OV) fanno pensare a una versione non definitiva del framework o a una fonte secondaria, coerentemente con quanto dice il docente ("ho visto dei draft"). Da verificare sul documento ufficiale se serve per l'esame.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 7 (NIST CSF 2.0)*
- Nuovo il collegamento con la ISO 27001: gli standard esistenti si aggiornano incorporando elementi di cyber security, e framework nati dopo, come il CSF del NIST, rispondono a questa esigenza; il CSF è preso a riferimento da normative europee e nazionali. (Teams 2 @ 0:53:44 - 0:54:34)
- Risposta a una domanda posta in passato dagli studenti (non registrata): come si protegge un'organizzazione? Primo livello di risposta: in modo strutturato e con approccio basato sul rischio, anche per gestire la spesa (scegliere fra SOC interno, esterno o ibrido è una decisione strategica). (Teams 2 @ 0:54:52 - 0:56:18)
- Funzioni: identify, protect e detect sono cyber security; respond e recover sono cyber resilience (coerente con il 2025). Govern è trasversale ed è la funzione strategicamente più elevata. (Teams 2 @ 0:56:18 - 0:58:24)
- Contenuto nuovo sulla governance: la sicurezza è spesso percepita come puro centro di costo, perché quando funziona non si misura quanto si sarebbe perso senza. Un'organizzazione matura ha un **CISO**; spesso manca o il ruolo è svolto ad interim dal CIO o dal CTO, oppure il CISO sta sotto di loro. Nelle realtà più strutturate è un vero C-level, al pari di CTO e CIO, a volte riferisce direttamente al board e agli azionisti, e deve saper comunicare scenari e requisiti di cybersicurezza. Il docente racconta di aver ricoperto insieme i ruoli di CTO e CISO in una realtà media. (Teams 2 @ 0:58:41 - 1:01:34)
- I framework servono sia alle organizzazioni meno preparate, come guida, sia a quelle strutturate per confrontarsi anno per anno con gli obiettivi, dentro un sistema di gestione come quello della ISO 27001. Ridurli a una checklist è riduttivo. (Teams 2 @ 1:01:50 - 1:02:24)
## 8. Vettore d'attacco e superficie d'attacco
*CS-02 @ 00:59:16*
**Slide "Attack vector & attack surface".** Al centro, in un riquadro tratteggiato, *Information System* (edifici, fabbrica, banca). Tutto intorno, con frecce rosse verso il centro: *Virtualization and Cloud computing*, *Organized cyber crime*, *Un-patched software*, *Targeted malwares*, *Social networking*, *Insider threats*, *Botnets*, *Lack of cyber security professionals*, *Network applications*, *Inadequate security policies*, *Mobile device security*, *Compliance to Govt. Laws and regulations*, *Complexity of computer infrastructure*, *Hactivism* (sic).
Il **vettore d'attacco** è il mezzo con cui la minaccia passa dall'esterno all'interno dell'organizzazione. Esempi del docente: un malware veicolato da un'email che si installa su chi la apre; un gruppo criminale o attivista che conduce operazioni cyber; un'infrastruttura così complessa da essere difficile da mettere in sicurezza. Anche strutture **sovraorganizzate** possono essere inefficaci. Può essere un vettore d'attacco l'inesperienza di chi ha progettato il sistema o, peggio, la mancanza di consapevolezza di sicurezza del management.
### L'esempio delle telecamere
*CS-02 @ 01:01:23*
Il docente racconta, come sintesi di più casi reali della sua esperienza da **auditor**, un esempio ricorrente. Premessa sugli audit: sono voluti dall'azienda stessa, affidati a un consulente esterno indipendente dalle conseguenze di ciò che trova, si eseguono rispetto a un framework spesso di settore e danno al vertice aziendale una prospettiva chiara di ciò che va e non va. Quelli seri si fanno entrando fisicamente in tutte le zone dell'azienda.
L'azienda mostra con orgoglio decine di telecamere, ben posizionate anche nel rispetto della privacy (inquadrare il monitor e non la persona, o la porta e non la stanza), e un grande monitor con 30 inquadrature a rotazione: "la mia capacità di detection è totale". Alla domanda "chi guarda queste immagini?" la risposta è che sono registrate a ciclo continuo e nessuno le guarda, oppure che le controlla la persona della reception quando non ha altro da fare.
Conclusione: i **dati** ci sono, ma non diventano **informazioni** in tempo reale. Le telecamere così assolvono un compito di **respond** (ricostruire a posteriori chi è stato dopo un data breach), non di **detect** né di **protect**. Il management, poco attento alla sicurezza, era stato convinto che spendere molto in telecamere bastasse. Il punto è l'importanza della **governance**: la sicurezza non è fatta solo di controlli tecnici. Lo stesso esempio si potrebbe fare con firewall o policy sul software sicuro.
### Superficie d'attacco
*CS-02 @ 01:07:52*
La **superficie d'attacco** è la superficie, virtuale, da cui provengono le minacce esterne. Il concetto vale per tutta la sicurezza informatica ma è ancora più importante in ambito cyber.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezioni 8 e 9 (vettore, superficie d'attacco, perimetro)*
- Vettore d'attacco: mezzo tipicamente tecnologico ma anche umano, per esempio una persona che entra fisicamente o chi contatta un dipendente al telefono o su WhatsApp. Superficie d'attacco può includere anche regole, normative e strutture organizzative attaccabili. (Teams 2 @ 1:02:57 - 1:03:50)
- Passato remoto: aggiunta l'analogia igienica (si lava l'esterno del corpo, non l'interno) e il richiamo a Kevin Mitnick per le truffe telefoniche prima di Internet. (Teams 2 @ 1:05:35 - 1:06:25)
- Present perfect, esempio IoT ampliato: per vedere le telecamere dell'azienda ci si collega al cloud del produttore; se manca Internet non le si vede nemmeno dalla stessa rete locale, e si dipende dalla tecnologia proprietaria del fornitore. BYOD: sul telefono personale, dove anche un figlio può installare app, passano email aziendali confidenziali e autorizzazioni di pagamento. Conclusione: oggi si devono proteggere sempre di più gli asset interni. (Teams 2 @ 1:07:53 - 1:10:34)
## 9. Il perimetro organizzativo: dal passato remoto al perimetro globale
### Passato remoto
*CS-02 @ 01:08:25*
**Slide "Organisational perimeter (remote past)".** Un'ellisse *Exposure* che contiene l'edificio dell'azienda, alcuni server e un solo laptop, con poche frecce di scambio verso l'esterno.
Circa vent'anni fa la superficie d'attacco coincideva con il **perimetro di rete** dell'azienda. Pochi laptop aziendali (venditori, vertici, chi lavorava spesso fuori), niente telelavoro, un piccolo sito ospitato nel data center aziendale. Anche per una multinazionale il perimetro era grande ma ben definito e quasi statico: cambiava quando cambiava un computer o un laptop veniva assegnato o dismesso. Messo in sicurezza quel numero contabile di dispositivi, l'interno era difeso.
### Present perfect
*CS-02 @ 01:10:22*
**Slide "Organisational perimeter (present perfect)".** Due ellissi, *Exposure* e *New Exposure*. Dentro e sul bordo: *Remote Office* con *Access* via *VPN*, *Contractor*, *BYOD* con *Access*, *IoT*, *Cloud Apps*, *Internet* raggiunto con *Access*, un firewall, *Remote Workers* con *Access*. Molte frecce in entrata e in uscita.
Poi sono arrivati i consulenti esterni con telefono e laptop aziendali, il telelavoro sulla connessione di casa, il **BYOD** (*bring your own device*), i servizi in **cloud** ospitati nei data center di altri e i dispositivi **IoT** "come se piovesse". Molti IoT non dialogano direttamente con i nostri dispositivi ma con il cloud del produttore, ovunque si trovi; se aprono una porta, la porta di fatto la controlla il cloud del fornitore. Il perimetro diventa **fluido**, poi "vaporoso", "dissolto nel cloud": se non so che cosa devo proteggere, è difficile capire quali vettori d'attacco sono rilevanti.
### Dove stanno i dati nel cloud
*CS-02 @ 01:13:44*
Con un cloud pubblico (Azure, AWS, Google Cloud Platform) si ha solo una vaga idea di dove siano i dati. Il contratto, cioè una misura di sicurezza amministrativa, può imporre al **CSP** (*cloud service provider*) di tenerli in data center europei, oppure europei e nordamericani, oppure ovunque tranne in un certo continente. Ma se si vuole sapere in quale data center preciso si trovano in un dato momento, il fornitore può non rispondere: vincolarsi a uno stato specifico gli costa, e anche solo ricostruire dove fisicamente si trova un dato distribuito su più data center è oneroso. Si può chiedere, per esempio, "solo in Italia", ma lo si paga di più.
**Domanda di uno studente (CS-02 @ 01:15:52).** Se i dati personali stanno in Canada e non in Europa, non si perde la tutela del GDPR? Il docente chiarisce che nel suo esempio il vincolo contrattuale era "Europa e Nord America" e che la scelta dipende dalle esigenze: la compliance GDPR può poi chiedere per certi dati di restare in Europa, e a quel punto al fornitore va chiesto un servizio più specifico, e più caro.
Poi uno "spoiler" sul GDPR, con la premessa "non sono un giurista":
- il GDPR non protegge i dati personali ma gli **individui**;
- secondo il docente, tutti gli stati, anche extra UE, che riconoscono il diritto dell'Unione sono obbligati a rispettare il GDPR per i dati dei **cittadini europei**. Un'organizzazione americana deve trattare secondo il GDPR i dati di un cittadino francese che si registra sul suo sito, senza che serva il consenso del cittadino;
- cita il regolamento californiano, simile al GDPR per molti aspetti, più garantista verso le imprese, nato qualche anno dopo e ispirato al GDPR;
- il problema tecnico diventa: come faccio a sapere se l'utente è cittadino europeo? Chiederlo non basta, perché può mentire o non conoscere la propria cittadinanza. L'unico modo sicuro sarebbe chiedere un attestato di cittadinanza, impraticabile per chi deve solo fare login per vedere un episodio di una serie. Da qui lo scollamento fra requisito normativo e implementazione tecnica, e l'importanza della **privacy by design**.
> **Correzione:** l'ambito territoriale del GDPR (art. 3) non dipende dalla **cittadinanza** ma dalla **localizzazione**. Si applica a chi è stabilito nell'UE e, per chi non lo è, ai trattamenti di dati di interessati **che si trovano nell'Unione**, quando si offrono loro beni o servizi o se ne monitora il comportamento. Non dipende nemmeno dal fatto che lo stato del titolare "riconosca il diritto dell'Unione". Il problema pratico descritto dal docente (sapere chi ricade nel GDPR) esiste, ma riguarda dove si trova l'interessato, non il suo passaporto. Vale la premessa del docente stesso: "non sono un giurista".
> **Nota aggiunta:** il "regolamento californiano" è il **CCPA** (California Consumer Privacy Act), approvato nel 2018 ed efficace dal 2020; il GDPR è del 2016, efficace dal 25 maggio 2018.
### Perimetro globale (melt-down)
*CS-02 @ 01:24:17*
**Slide "Global perimeter (today – melt-down)".** Lo stesso schema del *present perfect* sovrapposto a un globo con collegamenti luminosi fra continenti; in basso, altri perimetri organizzativi (rosa, viola, blu, grigio, giallo), ciascuno con la propria struttura, collegati fra loro.
Oggi non solo il perimetro di rete è dissolto: tutte le frecce di ingresso e uscita del *present perfect* vanno verso **altre organizzazioni**. Partner B2B, istituzioni, fornitori tecnologici, fornitori cloud, i cloud dei produttori IoT (in Italia, Giappone, Corea, Russia, Canada: "non lo so, però ci sono"), il sistema operativo del telefono del contractor in missione. Il docente precisa che non sta condannando queste prassi: dice che non si possono ignorare vettori d'attacco molto più numerosi di un tempo. Una startup di tre persone con fatturato milionario, tutta esternalizzata in cloud, "si serve di servizi che stanno dappertutto e quindi da nessuna parte". Nessuno forse la conosce come preda, ma la sua infrastruttura è interconnessa con un sistema enorme: la difesa va impostata **a livello di sistema**.
**Monocultura e dipendenza.** *CS-02 @ 01:27:41* In Europa, e in parte in Nord America, i computer degli utenti aziendali usano quasi solo Microsoft Windows; i server si dividono fra Windows e Linux; i Mac, presenti in ambito enterprise nei primi anni 2000, sono rimasti di fatto solo nel multimedia. Gli aggiornamenti di Windows li controlla una sola azienda: se viene attaccata o subisce un incidente, rende potenzialmente vulnerabili le aziende di mezzo mondo. Il docente richiama l'**incidente CrowdStrike**, scelto il giorno prima "perché è qualcosa di tangibile davanti agli occhi di tutti", e aggiunge che incidenti simili accadono di continuo ma non tutti vengono dichiarati: a volte le aziende si rivolgono agli ISAC, e si sa quasi tutto dell'attacco ma non chi è stato colpito. Il contesto geopolitico ha aggravato il quadro, come la Commissione Europea aveva intercettato già nel 2021.
> **Nota aggiunta:** l'incidente CrowdStrike (19 luglio 2024) non fu un attacco né un problema degli aggiornamenti di Windows: un aggiornamento difettoso del sensore Falcon di CrowdStrike, un software di terze parti che gira in kernel su Windows, mandò in crash circa 8,5 milioni di macchine. L'esempio regge come caso di dipendenza da un unico fornitore in una filiera concentrata, ma la frase "chi controlla gli aggiornamenti di Windows? Una sola azienda" riguarda Microsoft, mentre l'incidente riguarda un altro fornitore.
La lezione si chiude a *CS-02 @ 01:29:30*, con il rimando alla prossima lezione per il tema del perimetro.
---
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 02, sezione 9 (perimetro globale, monocultura, CrowdStrike, GDPR)*
- Racconto completo di CrowdStrike: EDR con privilegi a basso livello, patch che impedisce il riavvio, deadlock "chiave lasciata nella toppa", costo in ore uomo nei data center senza disaster recovery automatico; slide con 8,5 milioni di sistemi e 10 miliardi di dollari (Teams 1 @ 0:27\:51-0\:36:22).
- Lettura "da analista": non fu un incidente degli aeroporti, colpì anche ospedali (interventi cancellati, pronto soccorso bloccati); il titolo dei media è un esempio di conclusione tratta fuori contesto (Teams 1 @ 0:31:28).
- Definizione tecnica di **privacy** e origine storica ("diritto a essere lasciati in pace") (Teams 1 @ 1:10:30).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 9 (perimetro globale) e Capitolo 04, sezione 11 (supply chain)*
- Esempio nuovo, la fatturazione elettronica: pochissime aziende hanno un sistema interno; il fornitore cloud a sua volta usa un CSP (Amazon, Google, Microsoft), un fornitore di pagamenti, un sistema di invio PDF via email, e librerie di terze parti open source mantenute da sconosciuti o closed source mai verificate. Le interdipendenze "non sono neanche più conoscibili". (Teams 2 @ 1:10:58 - 1:13:07)
- **DORA**: impone ai soggetti obbligati un elenco dei fornitori terzi e la conoscenza dell'intera filiera, perché l'attacco può venire dal fornitore del fornitore del fornitore. (Teams 2 @ 1:13:07)
- Casi citati: **Log4j** (libreria di logging, 2021) e **XZ** (libreria di compressione): un attore, statuale o meno, ottiene l'accesso a un progetto open source e vi inserisce una backdoor; nel caso XZ l'attore ha atteso anni per ottenere l'accesso e qualcuno se n'è accorto in tempo. Vedi Divergenze per le imprecisioni. (Teams 2 @ 1:14:01 - 1:16:03)
- Senza una **bill of materials** (elenco delle dipendenze) il cliente finale non sa se il suo software dipende da una libreria compromessa. (Teams 2 @ 1:15:04)
- Tre livelli di risposta a "come ci si difende": 1) approccio basato sul rischio; 2) fare sistema, con scambio informativo strutturato (von der Leyen); 3) "conosci te stesso": sapere che cosa si ha "in pancia" e quali sono le proprie interdipendenze, perché non si protegge ciò che non si conosce. Senza questo, una PMI è alla mercé dei supply chain attack. (Teams 2 @ 1:16:19 - 1:18:23)
---
## 10. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato nella lezione</td>
</tr>
<tr>
<td>Controlli tecnici / logici</td>
<td>Presidi IT: autenticazione, controllo accessi, firewall</td>
</tr>
<tr>
<td>Controlli fisici</td>
<td>Presidi materiali: sbarre, casseforti, telecamere, badge</td>
</tr>
<tr>
<td>Controlli amministrativi / organizzativi</td>
<td>Norme, policy, contratti, prassi con effetti anche giuridici</td>
</tr>
<tr>
<td>Dato avvelenato</td>
<td>Dato modificato illegittimamente; può fare più danni di un dato mancante</td>
</tr>
<tr>
<td>Minaccia (threat)</td>
<td>Combinazione di intento ostile, capacità e opportunità</td>
</tr>
<tr>
<td>Impending / potential / insubstantial</td>
<td>Minaccia a cui manca, rispettivamente, l'opportunità, l'intento o la capacità</td>
</tr>
<tr>
<td>Attore della minaccia (threat actor)</td>
<td>Chi mette in atto la minaccia; anche solo un malware se non c'è attribuzione</td>
</tr>
<tr>
<td>Attribuzione</td>
<td>Associare l'attore a persone, gruppi, stati</td>
</tr>
<tr>
<td>TTP</td>
<td>Tactics, techniques and procedures</td>
</tr>
<tr>
<td>Asset</td>
<td>Qualunque cosa abbia valore per un'organizzazione</td>
</tr>
<tr>
<td>Vulnerabilità</td>
<td>Debolezza sfruttabile da una minaccia</td>
</tr>
<tr>
<td>Rischio</td>
<td>Effetto dell'incertezza sugli obiettivi; probabilità × controvalore</td>
</tr>
<tr>
<td>SOC / NOC</td>
<td>Security / Network Operations Centre</td>
</tr>
<tr>
<td>CSIRT</td>
<td>Computer Security Incident Response Team</td>
</tr>
<tr>
<td>CERT®</td>
<td>Computer Emergency Response Team, marchio Carnegie Mellon, con accreditamento</td>
</tr>
<tr>
<td>ISAC</td>
<td>Information Sharing and Analysis Centre, di settore, condivide e anonimizza threat intelligence</td>
</tr>
<tr>
<td>Constituency</td>
<td>Insieme dei soggetti a cui sono rivolte le operazioni di SOC/CSIRT/CERT/ISAC</td>
</tr>
<tr>
<td>Dati / informazioni / intelligence</td>
<td>Grezzi / arricchiti per risposte semplici / curati e actionable per decisori</td>
</tr>
<tr>
<td>Actionable</td>
<td>Utilizzabile direttamente dal decisore</td>
</tr>
<tr>
<td>NIST CSF 2.0</td>
<td>Framework con sei funzioni: Govern, Identify, Protect, Detect, Respond, Recover</td>
</tr>
<tr>
<td>Cyber security / cyber resilience</td>
<td>Nel CSF: Identify-Protect-Detect / Respond-Recover</td>
</tr>
<tr>
<td>Vettore d'attacco</td>
<td>Mezzo con cui la minaccia entra nell'organizzazione</td>
</tr>
<tr>
<td>Superficie d'attacco</td>
<td>Superficie virtuale da cui provengono le minacce esterne</td>
</tr>
<tr>
<td>BYOD</td>
<td>Bring your own device</td>
</tr>
<tr>
<td>CSP</td>
<td>Cloud service provider</td>
</tr>
<tr>
<td>Privacy by design</td>
<td>Progettare la privacy fin dall'inizio</td>
</tr>
</table>
## 11. Punti incerti
- \[?\] *CS-02 @ 00:20:43*: "Per esempio di Yauuma è evidente che oggi il valore economico…". Parola non ricostruibile, da riascoltare.
- \[?\] *CS-02 @ 00:50:25*: "il NIST è l'organo di standardizzazione tecnologica americano, italiano di fatto fa scuola". Probabilmente "americano, di fatto fa scuola", con "italiano" errore di trascrizione.
- \[?\] *CS-02 @ 00:56:45*: "diverse fasi, come quella dedicata all'evoluzione della minaccia, tra le quali c'è anche la formazione nel continuo". Non è chiaro a quali categorie del CSF si riferisca ([ID.IM](http://ID.IM)? [PR.AT](http://PR.AT)?).
- *CS-02 @ 01:17:11*: "non voglio essere vendor neutral". Dal contesto il senso è l'opposto (non nominare un continente per restare neutrale); lapsus del docente o della trascrizione.
- Trascrizione automatica corretta nel testo: "XIRT/OXIRT" = CSIRT, "Fred Hector" = threat actor, "Fonderlion" = von der Leyen, "CloudyToon" = cloud di turno, "adeggenza" = degenza, "direttografia" (CS-05) = crittografia.
## 12. Esame
In questa lezione il docente non dice nulla sull'esame. Indica due volte argomenti "meno rilevanti ai vostri fini" (la triade dei controlli e quella delle strutture organizzative), segnale utile per pesare lo studio ma non un'esclusione esplicita.
