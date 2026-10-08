# 01 - Introduzione (Teams 2026)

> Fonte Notion: https://app.notion.com/p/3e812abc808d812ea7c2e79166c1e035 — ultima modifica 2026-09-27T11:01:45.442Z

**Corso:** Cybersecurity, Cyber Intelligence and Data Privacy, docente Walter Arrighetti
**Registrazione:** Teams 2026, "Cybersecurity, Cyber Intelligence and Data Privacy - Lezione 1-20260907_180736-Registrazione della [riunione.mp](http://riunione.mp)4", 07/09/2026, durata 1:26:19 (parlato fino a 1:25:41)
**Fonti:** solo la registrazione (parlato; poche slide viste con screenshot del player). Il docente non ha distribuito materiale.
> **Avviso.** Capitolo ricostruito dalla registrazione Teams 2026 (sola visualizzazione): testo riassunto, non trascritto; le slide non sono state lette dai fotogrammi, se non per ciò che il docente dice a voce. Fanno eccezione alcune slide guardate con uno screenshot del player per dare contesto: sono segnalate come "(slide vista a h\:mm\:ss)". Per l'edizione 2025 la lezione 1 non esiste sul portale: questo capitolo la sostituisce e colma i rimandi a "ieri" dei capitoli 02 e seguenti (triade CIA, ricetta della Coca-Cola, von der Leyen, CrowdStrike).
## Indice
1. Presentazione del docente e dei due corsi
2. Perché la sicurezza in un master di data analytics: Davenport e la fiducia
3. "Tutto è interconnesso, tutto può essere hackerato": von der Leyen 2021
4. Retrospettiva degli incidenti 2000-2020
5. Il data breach di Yahoo e il silenzio delle vittime
6. Lo scenario italiano secondo ACN (2023)
7. L'incidente CrowdStrike (luglio 2024)
8. Attacchi alle utility idriche (estate 2026): OT, ICS, sistemi cyber-fisici
9. Stuxnet e l'attribuzione: il false flag
10. I cercapersone di Hezbollah (2024)
11. Il cyberspazio come quinto dominio e la fisicità del cloud
12. Obiettivo del corso: igiene cibernetica e costo dei controlli
13. Le triadi della sicurezza: premessa di metodo
14. La triade dell'informazione: dati, informazioni, intelligence
15. La triade della sicurezza delle informazioni (CIA / RID)
16. Privacy
17. Safety
18. WannaCry e gli ospedali: il contesto prima della notizia
19. Chiusura: cultura cyber e vittime mai dichiarate
20. Glossario
21. Punti incerti
22. Esame
---
## 1. Presentazione del docente e dei due corsi
*Teams 1 @ 0:00:11*
Il docente apre presentando il corso: Cybersecurity, Cyber Intelligence and Data Privacy del master in Data Analytics Fundamentals di primo livello. Le sigle colorate sulla slide di presentazione sono certificazioni professionali, "c'è a chi piace metterle".
Il profilo che traccia di sé:
- circa 19 anni di lavoro nella sicurezza informatica e un dottorato alla Sapienza (*Teams 1 @ 0:00:41*);
- la prima parte della carriera nel **cinema**: sicurezza del contenuto multimediale, ciò che si chiamava e si chiama ancora "antipirateria" (DVD, Blu-ray, asset cinematografici). È lì che ha cominciato a fare quella che oggi si chiama **cyber threat intelligence**, quando ancora non aveva questo nome. Nel tempo la minaccia si è spostata nello spazio cibernetico e lui è passato al **settore finanziario** (*Teams 1 @ 0:00:59*);
- esperienza come **auditor di sicurezza**: pagato da terzi, visitava studi cinematografici e soprattutto di doppiaggio e valutava per conto di una major americana se le misure di sicurezza **fisiche, tecniche e amministrative** fossero adeguate a proteggere il contenuto (*Teams 1 @ 0:01:56*). Una caratteristica del settore: chi lavora il film **non possiede i dati** che tratta, che appartengono allo studio. È la stessa situazione di oggi nel cloud, dove il provider tratta per conto vostro dati che magari non sono né suoi né vostri: da qui gli aspetti di **data governance** che il corso vedrà brevemente (*Teams 1 @ 0:02:41*);
- insegnamento pluriennale di cyber intelligence e cybersecurity in atenei italiani ed esteri;
- nel 2021 ha vinto il primo concorso nazionale per esperti di cybersecurity e intelligence della **Banca d'Italia**, dove lavora da allora, sia nel **CERT** sia nel **Red Team** dell'istituto (*Teams 1 @ 0:03:37*). CERT e Red Team saranno approfonditi "se non nel primo corso, nel corso per il master di secondo livello";
- nel passaggio dal cinema alla finanza si è specializzato in **identità digitali** (*Teams 1 @ 0:04:07*).
**Due corsi con lo stesso docente.** Il docente parla di un "secondo corso che vedrete con me", evoluzione di questo, dedicato soprattutto agli aspetti di **identità digitale** attinenti all'analisi dei dati (*Teams 1 @ 0:04:24*). La ragione: oggi qualunque operazione sensibile sui dati si fa da un computer in cui ci si **autentica** con un'identità digitale, e questo ha risvolti non solo di privacy e gestione del dato ma di cybersicurezza.
## 2. Perché la sicurezza in un master di data analytics: Davenport e la fiducia
*Teams 1 @ 0:04:56*
Per giustificare un corso di sicurezza in un master di data analytics il docente cita **Davenport** e un suo saggio del 2014 sui big data. Allora il data scientist era una figura ancora da definire, a metà fra lo statistico e l'informatico. Davenport sottolineava che non basta essere un **analista quantitativo**: bisogna essere anche **esperto di business** e **consulente fidato** (*trusted advisor*).
- **Esperto di business**, perché non si possono leggere i dati di un settore senza conoscerlo: chi fa solo la parte tecnica rischia di fare "il lavoro a metà".
- **Consulente fidato**, perché chi riceve il risultato dell'analisi (che lo si chiami informazione o intelligence) deve potersi fidare di chi lo consegna. Nel mondo digitale chi analizza spesso non possiede il dato e consegna il risultato a un terzo: tornano le **tre parti** (proprietario del dato, analista, destinatario) che accompagneranno "tutti questi corsi" (*Teams 1 @ 0:07:05*).
La fiducia ha tre oggetti: che i dati siano **autentici**, che siano stati analizzati davvero da quella persona (di nuovo l'**identità digitale**), e che quella persona sia capace di analizzarli (*Teams 1 @ 0:07:35*). Con l'AI il tema si amplifica: le intelligenze artificiali attingono a enormi quantità di dati e, come si è visto "negli ultimi mesi", arrivano a sferrare attacchi, a volte sbagliando o "uscendo dal seminato" (*Teams 1 @ 0:07:52*).
La sintesi del docente (*Teams 1 @ 0:08:40*): chiunque forse può scrivere **buon codice** che fa lavorare una **buona AI** su **buoni dati**. Sono tre ipotesi, e anche se sono tutte vere il risultato va **convalidato**: lì il lavoro umano torna rilevante. La domanda del 2014 era "che mix di competenze deve avere un data scientist?"; quella di oggi è quali compiti si possano delegare a sistemi automatici e generativi e quali ruoli servano per controllare che gli output siano affidabili.
Seconda idea di Davenport: oggi si analizzano sempre più dati di ieri (*Teams 1 @ 0:09:50*). Per la sicurezza significa che più dati ci sono, più ampia è la **superficie d'attacco**, più materia sfruttabile ha l'attore della minaccia e più materia c'è da proteggere.
> **Nota aggiunta:** si tratta di Thomas H. Davenport, docente e consulente di management (Babson College), più che "giornalista". Il saggio del 2014 è con ogni probabilità *Big Data at Work*; la tesi del data scientist come figura ibrida è anche nel suo articolo del 2012 su Harvard Business Review con D. J. Patil.
## 3. "Tutto è interconnesso, tutto può essere hackerato": von der Leyen 2021
*Teams 1 @ 0:10:41*
La seconda citazione è di **Ursula von der Leyen**, dal discorso sullo **Stato dell'Unione del 2021**, formato che l'Europa ha mutuato dagli Stati Uniti. La Commissione stava per avviare pacchetti legislativi poi diventati legge: il docente cita **NIS**, **NIS2**, **DORA**, **Cyber Resilience Act**, **Cybersecurity Act** (*Teams 1 @ 0:11:17*).
Nel 2021 lo scenario era diverso da oggi, con meno conflitti cinetici in corso, ma la pandemia aveva già mostrato che la minaccia cyber è **asimmetrica**. La frase chiave: poiché tutto è interconnesso, tutto può essere hackerato. Per un tecnico è letteralmente vera: nello spazio cibernetico un attacco può raggiungere anche un dispositivo che, attaccato direttamente, non sarebbe raggiungibile. Chi 5-10 anni fa si riteneva immune oggi non lo è, perché i suoi sistemi sono interconnessi con altri: sono gli **attacchi alla filiera dell'approvvigionamento** (*supply chain*) (*Teams 1 @ 0:12:35*).
La risposta proposta da von der Leyen: l'unico modo di vincere l'asimmetria è **fare sistema**, unirsi e puntare alla leadership nella cybersicurezza, perché da soli non ci si difende da una minaccia globale (*Teams 1 @ 0:13:15*). Il tema sarà approfondito, "soprattutto per chi rimarrà per il master di secondo livello", con argomenti di cyber intelligence.
## 4. Retrospettiva degli incidenti 2000-2020
*Teams 1 @ 0:13:59*
Il docente mostra un elenco di incidenti, con in grassetto il numero di credenziali o record esfiltrati. Avverte esplicitamente che **l'elenco non sarà oggetto d'esame** (*Teams 1 @ 0:14:30*): serve a farsi un'idea dell'evoluzione degli attacchi.
(Slide viste a 0:14:20 e 0:16:40.) Le due slide si intitolano "A data security retrospective: 2000s-2010s" e "…: years 2020s". Voci principali, riassunte:
- **2000-2010:** Estonia 2007 (primo attacco su scala nazionale: 58 siti fra governo, banche e media); Stuxnet 2009; Sony PlayStation Network 2011 (77 milioni di credenziali); Yahoo 2014; Sony 2014 (attacco statuale con fuga di sceneggiature e piani strategici); rete elettrica ucraina 2015; Maersk 2017; WannaCry 2017; Microsoft 2019 (267 milioni di credenziali).
- **Anni 2020:** Marriott/Starwood 2020 (339 milioni di ospiti); SolarWinds Orion 2020; Microsoft Exchange 2021; Log4j 2021; LockBit 2022-2023 (doppia estorsione, anche contro aziende e PA italiane); MOVEit 2023 (circa 2000 organizzazioni, 60 milioni di utenti); backdoor in **xz** 2024; CrowdStrike 2024 (24 mila clienti, circa 10 miliardi di dollari di danni); cercapersone di Hezbollah 2024; un "attacco crittografico quantistico" dimostrativo con un computer D-Wave 2024.
A voce il docente sottolinea (*Teams 1 @ 0:14:48*):
- già negli anni 2000 due incidenti gravissimi mostrarono che gli attacchi potevano avere **conseguenze nel mondo materiale**: l'**Estonia** nel 2007, con mezza pubblica amministrazione bloccata, e nel 2009 l'attacco a una centrale nucleare scoperto anni dopo (Stuxnet, sezione 9);
- accanto a questi, gli attacchi cybercriminali a fine economico per esfiltrare credenziali;
- dal 2014 i primi **ransomware**, e il primo grande ransomware globale, **WannaCry**, "perché se colpiva la tua organizzazione ti faceva venire solo voglia di piangere" (*Teams 1 @ 0:15:52*). Da allora i ransomware non sono mai calati e possono paralizzare un'azienda, un settore o un paese;
- nell'ultimo decennio crescono i volumi esfiltrati: si trattano più dati (Davenport), quindi se ne rubano di più.
**Il mercato dei dati rubati.** *Teams 1 @ 0:16:54* I dati hanno un valore **intrinseco** e uno **estrinseco**: chi li ruba spesso non li sfrutta direttamente ma li **rivende** a chi sa aggregarli e interpretarli, tipicamente gruppi cybercriminali. Secondo il docente, "soprattutto dal 2025 in poi" l'**Europol** ha individuato un vero mercato nero di questi dati, venduti al miglior offerente. Dal 2022, inoltre, si è visto che gran parte dei conflitti armati si combatte anche con attacchi cyber.
## 5. Il data breach di Yahoo e il silenzio delle vittime
*Teams 1 @ 0:18:04*
(Slide vista a 0:18:50: "The largest known data breach in history".) Il più grande data breach pubblicamente noto per numero di dati coinvolti resta quello di **Yahoo** (2013-2014). Un attore statuale, poi ricondotto alla **Russia**, entrò nei sistemi e restò per mesi, con accesso potenziale a tutta la base utenti, stimata in **3 miliardi di account**: nomi, telefoni, email, password, domande di sicurezza. Non è chiaro quanto sia stato davvero esfiltrato, ma potenzialmente tutto.
Yahoo si limitò a notificare gli utenti fra il 2016 e il 2017 invitandoli a cambiare la password. La data **non è casuale** (*Teams 1 @ 0:19:39*): la rivelazione produsse un enorme danno reputazionale e fece crollare il titolo proprio mentre Yahoo negoziava la vendita a **Verizon**, che la comprò "per due spicci" (un'operazione comunque miliardaria, ma molto sotto il valore di poche settimane prima). Il caso è citato, dicono al docente i colleghi economisti, in testi di economia, diritto e storia dell'informatica.
> **Nota aggiunta:** Yahoo subì due violazioni distinte. Quella del **2013** coinvolse tutti i circa 3 miliardi di account (annunciata a dicembre 2016, cifra rivista a 3 miliardi nell'ottobre 2017); quella del **2014**, circa 500 milioni di account, fu attribuita dall'FBI ad agenti dell'FSB russo e a hacker da loro ingaggiati (incriminazioni del 2017). Verizon ottenne una riduzione del prezzo di circa 350 milioni di dollari, chiudendo a circa 4,48 miliardi.
**Perché le aziende tacciono.** *Teams 1 @ 0:21:02* Il caso insegna che le aziende private tendono a non rivelare gli incidenti per paura del danno reputazionale: azionisti che perdono fiducia, titolo che crolla, oppure, per chi non è quotato, clienti che se ne vanno. Oggi però, come ripetono i sensazionalisti del web, "non è questione di se, ma di quando" si verrà attaccati: frase a effetto ma abbastanza vera. Nel 2026 non basta più dire agli utenti di cambiare la password "pregando che lo facciano". In Europa e altrove molte leggi impongono ai soggetti grandi o critici per un paese o un mercato di **segnalare** gli incidenti, se non al pubblico almeno attraverso meccanismi di **reporting** (*Teams 1 @ 0:22:09*).
Il senso torna a von der Leyen: se tutti cadono vittima e nessuno parla, gli attori proliferano; se si condividono le informazioni e si fa massa critica, si matura insieme. In questo consiste, "in due o tre parole", la **maturità** di un programma di cybersicurezza: affrontare la minaccia in modo strutturato, spesso insieme alle altre organizzazioni (*Teams 1 @ 0:22:45*).
## 6. Lo scenario italiano secondo ACN (2023)
*Teams 1 @ 0:23:17*
(Slide vista a 0:24:00: "Italian Cybersecurity scenario, as of 2023 H1", con citazione di Bruno Frattasi, direttore generale ACN.) Il docente fa riferimento a un documento dell'**Agenzia per la Cybersicurezza Nazionale** del 2023: nel primo semestre 175 ransomware e 100 attacchi DDoS in Italia; DoS e ransomware "li vedremo nel corso del master di secondo livello" (*Teams 1 @ 0:23:40*). Le criticità rilevate, "e nel 2026 non siamo molto distanti":
1. **Scarsa maturità**: molte organizzazioni non sanno fronteggiare da sole certe minacce; un'azienda su quattro non ha capacità avanzate di **risposta agli incidenti**.
2. **Nessuna sensibilizzazione** del personale. Oggi la **security awareness** è spesso un obbligo, ma il docente non ama inquadrarla come formazione: la letteratura scientifica mostra che erogare corsi è poco efficace, meglio **programmi di coinvolgimento** più evoluti (*Teams 1 @ 0:24:30*). Serve perché molti attacchi hanno come vettore il **fattore umano**, cioè le vulnerabilità della psicologia umana oltre a quelle tecniche.
3. **Mancanza di controllo sulle soluzioni di sicurezza** (*Teams 1 @ 0:25:24*). Molte aziende si affidano quasi del tutto a prodotti di terzi, spesso esteri. Un firewall anche ben configurato non basta: va controllato e aggiornato, e molte minacce, soprattutto quelle che sfruttano il fattore umano, gli sono invisibili. Lo stesso vale per l'antivirus. Soprattutto, non si controllano i **fornitori** di software di sicurezza che entrano così in profondità nei sistemi: se falliscono, o diventano essi stessi vettore d'attacco, "c'è ben poco che si può fare" (anticipazione di CrowdStrike).
4. **Sottostima statistica** (*Teams 1 @ 0:27:04*): molte aziende non dichiarano gli attacchi, quindi tutte le statistiche sono stime per difetto. In molti settori c'è un obbligo di notifica, ma non tutti vi sono soggetti e non tutti quelli soggetti lo rispettano.
## 7. L'incidente CrowdStrike (luglio 2024)
*Teams 1 @ 0:27:51*
(Slide vista a 0:29:20: "Example of recent cyber incident", "Microsoft/CrowdStrike global tech crash, July 2024", 8,5 milioni di sistemi andati in crash e incapaci di ripartire, circa 10 miliardi di dollari di danni stimati; foto di schermi blu in aeroporto.)
**Cosa è successo.** Chi partiva per le ferie a luglio 2024 lo ha forse vissuto di persona. I server Windows di mezzo mondo, cioè i sistemi back-end dietro ai servizi agli utenti, smisero di funzionare, a notte fonda per l'Italia; al risveglio molti erano già stati identificati e ripristinati. Ci furono comunque disservizi anche a **Roma Termini**. Non fu un attacco: ad oggi si esclude un intento malevolo, fu un **evento di sicurezza** (*Teams 1 @ 0:28:39*).
**CrowdStrike** produce uno dei software "antivirus" più diffusi per Windows. Il docente precisa che oggi si chiamano **EDR** (*endpoint detection and response*), anche se tutti continuano a dire antivirus perché fanno molto di più (*Teams 1 @ 0:29:14*). Li usano clienti enterprise di Microsoft di ogni settore: aeroporti, ospedali, sanità. CrowdStrike sbaglia una patch e la manda in produzione.
**Perché un aggiornamento di sicurezza può fermare il sistema.** *Teams 1 @ 0:29:51* Per fare bene il loro lavoro gli antivirus devono operare con gli stessi meccanismi a basso livello dei virus, con privilegi molto elevati, per vedere cosa non va prima che succeda. Si installano così in profondità che un loro aggiornamento comporta il riavvio del sistema operativo. Una patch che impedisce il riavvio, mandata su un server che si riavvia automaticamente per tornare operativo, produce un server che non torna più su: le **schermate blu**, e con i server tutti i sistemi che ne dipendono, come i monitor degli aeroporti.
**Il contesto contro il titolo.** *Teams 1 @ 0:31:28* Da analista di cyber threat intelligence il docente invita i futuri "business expert e trusted business consultant" a guardare il contesto. I media parlarono prima di attacco informatico agli aeroporti, poi di incidente; ancora oggi lo si ricorda come "l'incidente che ha paralizzato gli aeroporti". Ma furono colpiti anche **ospedali** che dovettero cancellare interventi e bloccare pronto soccorso, perché i server che gestivano triage, pazienti e immagini non funzionavano. A luglio la notizia che fa scalpore è quella dei viaggiatori, ma il problema riguardava sistemi operativi enterprise presenti in qualunque azienda, non software aeroportuali. Guardare un fatto fuori contesto porta a conclusioni sbagliate, che è ciò che un analista deve evitare.
**Perché costò così tanto.** *Teams 1 @ 0:33:55* Il danno non venne dalle poche ore offline ma dai sistemi che non si potevano rimettere in piedi rapidamente: server in data center poco presidiati, che si affidano a procedure automatiche di riavvio. Se a non funzionare è proprio il riavvio, si crea un **deadlock**: come uscire di casa lasciando la chiave nella toppa interna e tirarsi dietro la porta. I data center con disaster recovery automatico (dopo n minuti senza riavvio ricaricano una versione precedente) ripartirono; gli altri richiesero tecnici sul posto, macchina per macchina, con una chiavetta USB e una procedura manuale. Un data center può avere mille macchine bloccate; i grandi provider, con migliaia di clienti e decine di migliaia di server, due ordini di grandezza in più: da qui il costo in ore uomo.
> **Nota aggiunta:** l'aggiornamento difettoso (19 luglio 2024, circa le 04:09 UTC, le 06:09 in Italia) era un file di contenuto ("channel file 291") del sensore Falcon, che gira in kernel su Windows; il ripristino manuale consisteva nell'avviare in modalità provvisoria o nell'ambiente di ripristino e cancellare quel file, reso lento dalle chiavi BitLocker da recuperare, più che nel reinstallare il sistema operativo. Il problema non riguardava gli aggiornamenti di Microsoft. Vedi anche la nota sul capitolo 02, sezione 9.
## 8. Attacchi alle utility idriche (estate 2026): OT, ICS, sistemi cyber-fisici
*Teams 1 @ 0:36:27*
(Slide vista a 0:36:40: "Cyber-attacks on Utilities (OT/ICS)", schemi e foto di impianti di trattamento acque.) Esempio recentissimo, questa volta di **attacco**: una serie di incidenti agli impianti idrici degli **Stati Uniti**, "ma non solo", nell'estate 2026. Il docente non entra nel merito: non gli piace parlare in pubblico di incidenti con l'analisi ancora in corso, a differenza dei sensazionalisti che vogliono mostrare di avere la notizia di prima mano; e si tratta di infrastrutture critiche di un altro paese, i cui dettagli tecnici sono poco noti.
Il punto: un attore della minaccia collegato via Internet dall'esterno a un'azienda (probabilmente una utility o un suo fornitore, magari un software usato su quei computer) è entrato così in profondità da manipolare i **sistemi di gestione industriale** (*Teams 1 @ 0:37:33*). Due sigle sempre più frequenti:
- **OT** (*Operational Technology*): tecnologia non informatica ma operativa;
- **ICS** (*Industrial Control Systems*): sistemi di controllo industriale.
In italiano si parla anche di **sistemi cyber-fisici**: da un lato sono in rete e controllabili da remoto come un software qualsiasi, dall'altro manipolano impianti fisici (idroelettrico, riscaldamento, gas, nucleare, trasporti, robot di assemblaggio). Nel caso dell'acqua è in gioco la **salute** delle persone. È l'esempio di come un attore motivato possa ottenere, via Internet, **effetti cinetici**.
## 9. Stuxnet e l'attribuzione: il false flag
*Teams 1 @ 0:39:16*
Tornando indietro nel tempo, il docente riprende **Stuxnet**, già accennato. Nella sua ricostruzione l'incidente fu scoperto appena in tempo per evitare "forse la più grande catastrofe nucleare del mondo" in **Iran**. Negli anni fu ricondotto a due **superpotenze cyber alleate**, probabilmente decise a rallentare lo sviluppo nucleare del paese, come era già stato fatto e come si è fatto anche dopo.
- Fu un attacco **ICS/OT** con un sistema informatico come vettore (*Teams 1 @ 0:40:21*).
- I sistemi più interni della centrale erano **air-gapped**, segregati da Internet: il malware fu veicolato con una **chiavetta USB**, molto diffuse attorno al 2010. È stata trovata la chiavetta infetta, ma la ricostruzione non è mai stata certa.
- Obiettivo, secondo il docente: far sembrare che una ventola di raffreddamento funzionasse mentre era ferma, per portare l'impianto a surriscaldarsi (*Teams 1 @ 0:41:30*). Lo schema è stato ripreso, citato o copiato, in vari film.
- Si ritiene che la chiavetta sia stata **lanciata oltre il muro** nel cortile dove i dipendenti con i computer segregati facevano pausa, sfruttando la **curiosità** ("magari contiene dati importanti, o è una chiavetta gratis"). Inserita in un computer altrimenti irraggiungibile via email, ha permesso al codice di spostarsi fino alla rete di controllo industriale (*Teams 1 @ 0:42:01*).
**Attribuzione e false flag.** *Teams 1 @ 0:43:09* Analizzando il malware si trovarono stringhe e **commenti** degli sviluppatori; dalla lingua si dedusse la provenienza di uno di loro da un paese ostile all'Iran, da cui un'ipotesi di attribuzione. Tecnica facile, se l'attore è così poco scaltro da lasciare commenti; tanto che qualcuno ha sospettato che fossero stati lasciati apposta per indirizzare un'attribuzione sbagliata o affrettata: un'operazione **false flag**, "falsa bandiera", quella che 20-30 anni fa si sarebbe chiamata **disinformazione**.
> **Correzione:** Stuxnet colpì l'impianto di **arricchimento dell'uranio di Natanz**, non una centrale elettrica, e non agiva su ventole di raffreddamento: riprogrammava i PLC Siemens che controllavano la velocità delle **centrifughe**, alterandola per danneggiarle, mentre mostrava agli operatori valori normali registrati in precedenza. Non c'era quindi un rischio di "catastrofe nucleare" del tipo fusione del nocciolo (la slide a 0:14:20 parla però di "reactor's meltdown"). Resta corretto il senso del discorso: attacco statuale a un sistema OT air-gapped, veicolato probabilmente via USB.
> **Nota aggiunta:** l'attribuzione più diffusa è a Stati Uniti e Israele (operazione "Olympic Games"). Gli indizi più citati nel codice non sono commenti in una lingua ma stringhe come "myrtus" e il valore "19790509", interpretati da alcuni come riferimenti a Israele e da altri come possibili depistaggi: coerente con il discorso del docente sul false flag, meno con il dettaglio dei "commenti".
## 10. I cercapersone di Hezbollah (2024)
*Teams 1 @ 0:44:42*
Altro esempio del 2024 con conseguenze fisiche: le immagini di **cercapersone** che esplodevano. Le vittime furono esponenti di **Hezbollah** che portavano un certo modello di pager, raggiungibile via rete, a cui si poteva inviare un comando per far esplodere la batteria. Si dimostrò poi che i dispositivi erano stati intercettati dall'intelligence di un paese nemico, che si era inserita nella **filiera di approvvigionamento** fornendo pager con batterie alterate, poi fatte esplodere in modo coordinato, ferendo o uccidendo molti esponenti del gruppo (*Teams 1 @ 0:45:13*). È un altro esempio di attacco cyber con conseguenze cinetiche e di attacco alla **supply chain** (nella slide a 0:16:40: "IoT, OT and physical devices").
> **Nota aggiunta:** gli attacchi avvennero il 17 e 18 settembre 2024 (cercapersone il primo giorno, radio ricetrasmittenti il secondo). Secondo le ricostruzioni pubbliche nei dispositivi era nascosto un esplosivo, attivato da un messaggio ricevuto via rete radio dei pager, non via Internet. Le cifre in slide (20 morti, 450 feriti) sono più basse di quelle più citate (circa 40 morti e alcune migliaia di feriti nei due giorni).
## 11. Il cyberspazio come quinto dominio e la fisicità del cloud
*Teams 1 @ 0:46:18*
Proprio perché tutto è interconnesso, lo spazio cibernetico va considerato il **quinto dominio del conflitto**, dopo terra, mare, cielo e spazio: un dominio in cui tutto è interconnesso "ancor più che nei cieli e nei mari", e quindi tutto va protetto.
(Slide vista a 0:46:20: "Cyberspace…", immagine di una città digitale al neon.) Il docente smonta l'immaginario **cyberpunk**, in cui il cyberspazio vive solo dentro gli elaboratori e nelle schede grafiche (*Teams 1 @ 0:46:43*). Nulla del cyberspazio è etereo, e "nessuna parola è stata così fuorviante come **cloud computing**": nulla sta sulle nuvole, se non le onde verso i satelliti. Le connessioni importanti fra data center viaggiano quasi tutte in **fibra ottica**; tutto sta staticamente nei **data center**, in una rete molto fisica e quindi esposta anche ad **attacchi fisici** (*Teams 1 @ 0:47:32*).
Per questo prima gli Stati Uniti e poi l'Unione Europea hanno riconosciuto il cyberspazio come quinto dominio, in cui gli interessi statali si esplicano come in una guerra. I conflitti in corso mostrano che anche molti attacchi cinetici sono orchestrati ed eseguiti in gran parte nel cyberspazio (*Teams 1 @ 0:48:32*).
## 12. Obiettivo del corso: igiene cibernetica e costo dei controlli
*Teams 1 @ 0:49:15*
**Obiettivo dichiarato.** Il corso non vuole formare esperti di sicurezza ma **data analyst** che abbiano in mente i concetti principali della sicurezza informatica e della cybersicurezza (la differenza fra i due termini verrà più avanti) e li applichino ai dati e alle soluzioni che li trattano. I servizi che trattano grandi quantità di dati sono spesso i più esposti (*Teams 1 @ 0:49:51*).
Non ci si improvvisa esperti di sicurezza. È impensabile che tutti gli analisti siano esperti di cybersicurezza, ma anche il contrario; l'ottimo sta nel mezzo: chi tratta dati deve avere **sufficiente consapevolezza** dei temi cyber legati a quei dati e comportarsi, anche nel lavoro non tecnico, secondo regole di **igiene cibernetica** (*Teams 1 @ 0:50:27*).
**Soluzioni artigianali.** *Teams 1 @ 0:51:00* Senza questa consapevolezza si applicano soluzioni artigianali quasi sempre inefficaci e spesso **controproducenti**. E sono sempre **costose**: ogni controllo fra un dato e un altro costa, direttamente (acquisto di una soluzione) o indirettamente (trasmissione più lenta, qualcuno che deve approvare con un clic, sistemi in più). Aggiungere sicurezza aumenta sempre i costi: bisogna sperare che i presidi siano efficaci e soprattutto impedire che, inefficaci, siano anche dannosi.
**La slide comica.** *Teams 1 @ 0:52:19* Una provocazione con misure fisiche inutili: un **criptex** (serratura a combinazione) con la password scritta sopra; un cancello senza staccionata; un lucchetto metallico su un cancello metallico, ma fissato con **fascette di plastica**. Sono battute, ma mostrano come si sbaglia un controllo quando non si conosce lo **scenario della minaccia**: non devi impedire a una persona di passare nel vialetto, devi impedire a un ladro di entrare nella proprietà. Per progettare una soluzione cyber sicura serve un occhio critico che conosca **il business dei dati** (non della sicurezza): il valore reale del dato in ogni punto della catena e dove è più probabile che venga esfiltrato, alterato, cancellato o reso indisponibile (*Teams 1 @ 0:53:23*).
## 13. Le triadi della sicurezza: premessa di metodo
*Teams 1 @ 0:53:54*
Comincia la parte **tassonomica** del corso, che il docente non è sicuro di finire in giornata (infatti prosegue nella lezione successiva, vedi capitolo 02). La chiama complessivamente **le triadi della sicurezza**, perché i testi di riferimento sono americani: anche chi studia in Italia usa spesso traduzioni fedeli di testi anglosassoni, o testi italiani che ne traducono passaggi.
**L'aneddoto del "silicone".** *Teams 1 @ 0:54:48* Un celebre testo di microelettronica degli anni '90, un collage di testi americani tradotti male da studenti, parlava di "microelettronica del silicone": traduzione sbagliata di *silicon*, cioè silicio. Il silicone non si usa né come dielettrico né come isolante in nessun componente elettronico.
I testi americani riducono i concetti a forme geometriche (il cerchio della fiducia, il triangolo della sicurezza). Il docente non ama queste schematizzazioni, spesso troppo semplificate, ma riconosce che per un'introduzione funzionano e che alcune triadi fanno parte del **linguaggio dei professionisti** (*Teams 1 @ 0:55:51*).
## 14. La triade dell'informazione: dati, informazioni, intelligence
*Teams 1 @ 0:56:27*
(Slide vista a 1:01:40: "The triad of Information", la freccia *Operational Environment* → *Data* → *Information* → *Intelligence* con le lenti *Collection*, *Processing and Exploitation*, *Analysis and Production*, come nel capitolo 02, sezione 6.) La prima triade presentata è quella dell'**informazione**, perché tornerà nel master di secondo livello parlando di cyber intelligence.
- **Dati.** Quando il docente parla di dati intende spesso grandi moli raccolte anche automaticamente da fonti disparate: sensori IoT indossati, telecamere in ogni stanza, sensori della temperatura di ogni processore e di ogni armadio del data center (*Teams 1 @ 0:56:59*). Sono grezzi e da soli non consentono di analizzare nulla: vanno lavorati, trattati, sfruttati.
- **Informazioni.** Una mole più o meno ridotta rispetto ai dati di partenza, già più utilizzabile, che fa una **sintesi**: un trend, una media, una mediana, una varianza. Si può analizzare ancora, ma di solito non è abbastanza precisa perché un decisore prenda decisioni informate (*Teams 1 @ 0:57:48*).
- **Intelligence.** Informazione "distillata di secondo livello", intesa come **prodotto**.
**L'esempio del data center.** *Teams 1 @ 0:58:34* Temperature e umidità dei computer di un data center vengono filtrate in una dashboard per il responsabile dei sistemi informativi (temperatura complessiva, carico delle CPU) e in un'altra, più sintetica, per il responsabile della facility (costi di smaltimento di energia e calore, stima della bolletta del mese dopo). All'amministratore delegato del cloud provider però servono decisioni strategiche a 2-3 anni: costruire un nuovo data center, migrare in un luogo più freddo, rifare il sistema di smaltimento o riciclo del calore, cambiare fornitore elettrico. Queste informazioni sono utili ma non bastano: i responsabili (sistemi, facility, appalti, rapporti con le banche) devono mettere insieme le loro e costruire un piano strategico, ulteriormente distillato, da presentare al **board**. Quel prodotto è **intelligence** (*Teams 1 @ 1:00:12*).
**Automazione.** *Teams 1 @ 1:00:44* L'intelligence si può distillare anche con sistemi automatici o semiautomatici, ma oggi richiede almeno una **verifica di veridicità umana**, per evitare le **allucinazioni** dell'AI. La raccolta dei dati è automatizzata da sempre, nata con l'era industriale. L'estrazione di informazioni lo è in gran parte, ma c'è ancora chi elabora a mano enormi tabelle Excel. L'intelligence è ancora prodotta soprattutto dall'uomo, ma il docente non sa se sarà così negli anni a venire.
## 15. La triade della sicurezza delle informazioni (CIA / RID)
*Teams 1 @ 1:01:44*
(Slide vista a 1:12:00: "The triad of Information Security", triangolo con *Integrity*, *Availability*, *Confidentiality* attorno a *Information Security* e le definizioni in inglese; in basso, aggiunta, la voce *Privacy*.) È la triade su cui lavora qualunque professionista: in inglese **CIA**, in italiano **RID**.
**Asset.** La sicurezza delle informazioni protegge gli **asset** dell'organizzazione (*Teams 1 @ 1:01:59*): asset fisici e materiali (un edificio, un server, un disco), asset tecnologici (i dati trattati nei server, trasferiti nei sistemi di comunicazione, memorizzati su dischi, memorie flash, nastri), asset immateriali, come le **persone**: i dipendenti hanno un valore perché svolgono gran parte del lavoro.
**Le tre proprietà.** *Teams 1 @ 1:02:59*
- **Riservatezza**: le informazioni sono accessibili solo ai soggetti autorizzati. Portata al massimo diventa **need to know**: solo chi ha davvero bisogno di conoscere un'informazione deve poterla conoscere.
- **Integrità**: i dati non possono essere modificati, alterati o distrutti da chi non ne ha il permesso.
- **Disponibilità**: gli utenti autorizzati possono accedere ai dati quando serve.
### La ricetta della Coca-Cola
*Teams 1 @ 1:04:06*
Il paradigma che il docente usa sempre. Siete pagati per conservare e mantenere riservata la **ricetta della Coca-Cola**, l'asset più prezioso dell'azienda, con **budget infinito** (prima ipotesi assurda: il budget di chi fa sicurezza è tutt'altro che infinito). Il principiante costruisce una cassaforte a prova di bomba atomica, saldata alle tre travi ortogonali dell'edificio, che si apre solo se sono presenti almeno 3 degli 8 consiglieri d'amministrazione, ciascuno con una goccia di sangue, l'iride, l'impronta digitale e un codice di 79 cifre. La **riservatezza** è garantita, ma il progettista ha dimenticato il resto (*Teams 1 @ 1:05:36*).
- **Integrità.** Quando la ricetta esce dalla cassaforte, come si è certi che rientri la stessa ricetta e non una versione "edulcorata"? Che rientri affatto, e non venga di fatto cancellata da chi ha il diritto di accedere? E chi si fa chiudere dentro, la legge e se ne va, e il giorno dopo si licenzia per andare da un concorrente? (*Teams 1 @ 1:06:08*)
- **Disponibilità.** Se per aprire servono tre consiglieri in presenza, la ricetta non è disponibile quando la produzione ne ha bisogno, "né dall'oggi al domani, né tantomeno dall'oggi all'oggi". In termini aziendali è come se non esistesse, sicura solo finché resta in quella cassaforte "iperurania": è come averla cancellata (*Teams 1 @ 1:07:15*).
La morale: sicurezza informatica **non significa solo riservatezza** (lo si rivedrà con la crittografia) e può non includere affatto vincoli di riservatezza.
### I dati pubblici
*Teams 1 @ 1:08:33*
Esempio: il Ministero dell'Istruzione/Università pubblica il numero di laureati in Italia. Non è riservato, anzi deve essere noto a tutti. Allora il ministero non ha bisogno di esperti di sicurezza? No: può subire un attacco o un incidente che rende indisponibile il sito, e se una legge impone che il dato sia sempre consultabile serve qualcuno che ne garantisca la **disponibilità** anche durante un evento avverso. Forse non il mestiere più entusiasmante per un esperto di sicurezza ("certamente non lo sarebbe per me"), ma è un mestiere di sicurezza informatica.
## 16. Privacy
*Teams 1 @ 1:10:04*
Oltre alla triade RID il corso tratta la **privacy dei dati**, vista da un tecnico. La prima definizione storica, di fine Ottocento "se non sbaglio", è il diritto delle persone a **essere lasciate in pace**. In senso tecnico, la privacy è l'insieme delle misure che garantiscono che i **dati personali degli interessati** siano trattati nei sistemi informatici in conformità alle leggi e ai regolamenti sulla protezione dei dati personali: l'**informatica della privacy** (*Teams 1 @ 1:10:45*).
Nella versione del docente, per i dati dei **cittadini europei** questo vale in tutti i paesi che "riconoscono il diritto dell'Unione", cioè quasi tutti, in conformità alla "direttiva privacy" e soprattutto al **GDPR**; altri paesi hanno regolamenti più o meno vicini (*Teams 1 @ 1:11:03*).
> **Correzione:** come già segnalato nel capitolo 02 (sezione 9), l'ambito territoriale del GDPR (art. 3) non dipende dalla cittadinanza né dal fatto che uno stato "riconosca il diritto dell'Unione": si applica ai titolari stabiliti nell'UE e, per quelli non stabiliti, ai trattamenti di dati di interessati **che si trovano nell'Unione** quando si offrono loro beni o servizi o se ne monitora il comportamento. La definizione della slide ("for EU nationals") riflette la stessa semplificazione.
> **Nota aggiunta:** il "diritto a essere lasciati in pace" (*right to be let alone*) viene da Warren e Brandeis, "The Right to Privacy", Harvard Law Review, 1890. La direttiva 95/46/CE è stata abrogata dal GDPR; resta in vigore la direttiva ePrivacy 2002/58/CE per le comunicazioni elettroniche.
## 17. Safety
*Teams 1 @ 1:12:08*
Un altro aspetto, fuori dalla triade ma spesso insieme alla sicurezza informatica: in inglese si distingue **security** da **safety**, entrambe tradotte in italiano con "sicurezza". **Safety** è la sicurezza del benessere fisico e della salute delle persone: i sistemi di safety garantiscono che il trattamento delle informazioni **non nuoccia alla salute e alla vita** degli individui.
Perché parlarne in un corso di cybersecurity e dati (*Teams 1 @ 1:13:09*): sempre più macchinari interagiscono con noi, fanno diagnosi, somministrano cure; i **robot chirurgici**, anche operati a distanza, lavorano su tessuti molto delicati e sono sistemi interamente informatici. Un attacco che rende indisponibile un ecografo, un robot chirurgico o anche solo il sistema di **triage** di un pronto soccorso ad alta affluenza (che non può più trattare i pazienti presenti né ammetterne di nuovi) può avere impatti sulla salute e sulla vita.
## 18. WannaCry e gli ospedali: il contesto prima della notizia
*Teams 1 @ 1:14:00*
Per alleggerire la parte tassonomica il docente torna su **WannaCry**, un **ransomware** (che cos'è si vedrà "la prossima o le prossime lezioni"). Si diffuse a macchia d'olio non perché progettato per farlo, ma al contrario perché probabilmente privo di **guardrail** sufficienti a impedirne la diffusione incontrollata: sfruttando l'interconnessione, colpì indiscriminatamente aziende di ogni settore, ospedali compresi ma non solo (*Teams 1 @ 1:14:32*).
**La notizia sensazionale.** *Teams 1 @ 1:15:19* I media parlarono di "attacco agli ospedali", prima inglesi poi americani, come se qualcuno volesse metterli in ginocchio. L'**NHS** dovette rimandare interventi appena iniziati perché i macchinari di sala non funzionavano. Il docente lo attribuisce a un giornalismo dilettantistico che cerca di dare la notizia per primo informandosi meno: più si aspetta, più emergono dettagli che la rendono meno interessante. Precisa che fra il 2016 e il 2026 è cresciuto un ottimo **giornalismo cyber specializzato**, oggi con professionisti anche in ruoli di vertice; dieci anni fa mancava, e spesso gli errori erano in buona fede (*Teams 1 @ 1:16:47*).
Il punto è di nuovo il **contesto**: gli analisti devono conoscere il business per dare ai decisori ciò che serve (dati, informazioni, intelligence). WannaCry non poteva diffondersi solo negli ospedali. Perché allora le prime settimane parlarono di ospedali? Due fattori, con il senno di poi (*Teams 1 @ 1:18:10*):
1. **Obbligo di reporting.** Gli ospedali, pubblici o privati, più di qualunque azienda devono avvisare subito le autorità se qualcosa non funziona (un'epidemia, un reparto che chiude, sistemi fuori uso), perché altre strutture della zona devono farsi carico dei pazienti. È un obbligo di legge in quasi tutti i paesi, con sanzioni, e una questione di salute pubblica: i media lo sanno il minuto dopo.
2. **Informatica ospedaliera fragile.** *Teams 1 @ 1:19:45* Dieci anni fa molte strutture sanitarie non avevano informatici né tantomeno esperti di sicurezza e usavano software datati. Il docente, in visita a laboratori ospedalieri, ha visto per anni ecografi e radiografi con **Windows XP**. Questi macchinari sono **OT/ICS**, costosissimi (TAC, risonanze ad alto campo, robot chirurgici), ma controllati da un **PC normale** accanto, con un sistema operativo comune e spesso connesso a Internet (*Teams 1 @ 1:20:32*).
**Il dilemma dell'aggiornamento.** *Teams 1 @ 1:21:35* Chi forniva il robot (il docente cita il **da Vinci**, centinaia di migliaia di euro) consegnava il PC ma decideva lui quando aggiornarlo, magari una volta ogni due anni, perché solo lui poteva certificare che l'aggiornamento non rompesse il dialogo con il robot. Il direttore sanitario a cui l'informatica chiede di aggiornare "perché ci sono i virus" sa che il produttore non garantirà più il funzionamento di un robot con interventi prenotati per otto mesi: probabilmente non aggiorna, e aggiornare "sarebbe irresponsabile" (*Teams 1 @ 1:22:20*). Lo stesso problema lo avevano, e in parte lo hanno ancora, molti sistemi industriali; il docente lo ha visto da auditor anche nel cinema.
> **Correzione:** WannaCry si diffuse il **12 maggio 2017**, non nel 2016 come detto più volte a voce (la slide a 0:14:20 riporta correttamente 2017). Il riferimento temporale "dal 2016 al 2026" va letto come "dal 2017".
> **Correzione:** una TAC o una risonanza ad alto campo costano da alcune centinaia di migliaia a qualche milione di euro, non "diversi miliardi" (*Teams 1 @ 1:20:50*): evidente lapsus.
## 19. Chiusura: cultura cyber e vittime mai dichiarate
*Teams 1 @ 1:22:44*
Da qui l'importanza della **cultura cyber**. "Dal 2016 al 2026" (in realtà dal 2017, vedi la correzione nella sezione 18) l'atteggiamento è cambiato: più strutture sanitarie e settori industriali hanno un apparato di cyber difesa, spesso non autonomo (come rilevava ACN nel 2023), e anche i produttori di macchinari OT proteggono di più le infrastrutture IT a cui i loro sistemi sono collegati, comprese le utility (acqua, gas, elettricità, nucleare). Ma ci sono voluti dieci anni di incidenti.
**L'aneddoto dell'azienda farmaceutica.** *Teams 1 @ 1:23:49* Nel 2017 o 2018 il docente va da un'azienda farmaceutica come consulente per un programma di **security awareness**. Gli chiedono di includere il tema delle **chiavette USB** e spiegano candidamente che la loro sede era stata la **prima al mondo** del gruppo a prendere WannaCry, entrato proprio da una chiavetta. Non gli avevano fatto firmare alcun accordo di riservatezza; per correttezza deontologica il docente non fa il nome, ma nota che rivelarlo è stato a sua volta un problema di awareness e di maturità. La notizia non è mai stata pubblica: ancora oggi molte vittime di quell'incidente, e di molti altri, non sono note, e forse non si conoscerà mai l'entità completa della diffusione (*Teams 1 @ 1:25:08*).
La lezione si chiude a *Teams 1 @ 1:25:41* con l'invito alle domande e "ci sentiamo domani". Nessuna domanda di studenti è registrata in tutta la lezione (a *Teams 1 @ 0:13:53*: "non vedo domande, quindi proseguo").
> **Nota aggiunta:** WannaCry si propagava come worm sfruttando la vulnerabilità SMB EternalBlue (MS17-010), non tramite chiavette. Una chiavetta può però aver portato il malware dentro la rete di quella sede, da cui si è propagato: l'aneddoto non è in contraddizione, riguarda solo il punto d'ingresso locale.
---
## 20. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato nella lezione</td>
</tr>
<tr>
<td>Trusted advisor / consulente fidato</td>
<td>Per Davenport, requisito del data scientist oltre alla competenza quantitativa</td>
</tr>
<tr>
<td>Supply chain attack</td>
<td>Attacco che raggiunge la vittima attraverso un fornitore o un componente della filiera</td>
</tr>
<tr>
<td>Fare sistema</td>
<td>Condividere informazioni e collaborare contro una minaccia asimmetrica (von der Leyen)</td>
</tr>
<tr>
<td>Minaccia asimmetrica</td>
<td>Minaccia in cui l'attaccante ha un vantaggio strutturale sul difensore</td>
</tr>
<tr>
<td>Data breach</td>
<td>Violazione con esfiltrazione o esposizione di dati</td>
</tr>
<tr>
<td>Valore intrinseco / estrinseco dei dati</td>
<td>Valore per chi li possiede / valore di rivendita a terzi che sanno sfruttarli</td>
</tr>
<tr>
<td>Reporting (obbligo di)</td>
<td>Obbligo di segnalare gli incidenti ad autorità o al pubblico</td>
</tr>
<tr>
<td>Maturità di sicurezza</td>
<td>Capacità di affrontare la minaccia in modo strutturato, anche insieme ad altri</td>
</tr>
<tr>
<td>Security awareness</td>
<td>Sensibilizzazione del personale, più efficace come coinvolgimento che come corso</td>
</tr>
<tr>
<td>EDR</td>
<td>Endpoint Detection and Response, evoluzione dell'antivirus</td>
</tr>
<tr>
<td>Evento di sicurezza vs attacco</td>
<td>L'evento può essere un guasto o un errore; l'attacco presuppone intento malevolo</td>
</tr>
<tr>
<td>Deadlock</td>
<td>Blocco circolare: il meccanismo di ripristino è esso stesso bloccato</td>
</tr>
<tr>
<td>OT</td>
<td>Operational Technology, tecnologia operativa</td>
</tr>
<tr>
<td>ICS</td>
<td>Industrial Control Systems, sistemi di controllo industriale</td>
</tr>
<tr>
<td>Sistemi cyber-fisici</td>
<td>Sistemi in rete che controllano processi fisici</td>
</tr>
<tr>
<td>Effetto cinetico</td>
<td>Conseguenza materiale nel mondo fisico di un attacco cyber</td>
</tr>
<tr>
<td>Air gap</td>
<td>Segregazione di una rete da Internet</td>
</tr>
<tr>
<td>Attribuzione</td>
<td>Associare un attacco a un attore identificato</td>
</tr>
<tr>
<td>False flag</td>
<td>Operazione che lascia indizi falsi per far attribuire l'attacco ad altri</td>
</tr>
<tr>
<td>Quinto dominio</td>
<td>Il cyberspazio, dopo terra, mare, cielo e spazio</td>
</tr>
<tr>
<td>Igiene cibernetica</td>
<td>Regole di comportamento che riducono il rischio per i dati trattati</td>
</tr>
<tr>
<td>Dati / informazioni / intelligence</td>
<td>Grezzi / sintetizzati / distillati per decisioni strategiche</td>
</tr>
<tr>
<td>Allucinazione</td>
<td>Output falso di un sistema di AI, da verificare con controllo umano</td>
</tr>
<tr>
<td>Asset</td>
<td>Qualunque bene di valore: fisico, tecnologico, immateriale (anche le persone)</td>
</tr>
<tr>
<td>Triade CIA / RID</td>
<td>Confidentiality, Integrity, Availability / Riservatezza, Integrità, Disponibilità</td>
</tr>
<tr>
<td>Need to know</td>
<td>Riservatezza massima: accesso solo a chi ne ha effettivo bisogno</td>
</tr>
<tr>
<td>Privacy</td>
<td>Tecnicamente: trattamento dei dati personali conforme alle norme (GDPR)</td>
</tr>
<tr>
<td>Informatica della privacy</td>
<td>Misure tecnologiche per la conformità alle norme sulla protezione dei dati</td>
</tr>
<tr>
<td>Safety</td>
<td>Sicurezza della salute e della vita delle persone rispetto al trattamento delle informazioni</td>
</tr>
<tr>
<td>Guardrail</td>
<td>Meccanismi che limitano il comportamento di un software (qui: la diffusione di un malware)</td>
</tr>
<tr>
<td>Ransomware</td>
<td>Malware che cifra i dati e chiede un riscatto (dettagli nel capitolo 03)</td>
</tr>
</table>
## 21. Punti incerti
- \[?\] *Teams 1 @ 0:17:32*: "soprattutto dal 2025 in poi l'Europol ha individuato" un mercato dei dati rubati. Non è chiaro a quale rapporto Europol si riferisca (forse IOCTA 2025).
- \[?\] *Teams 1 @ 0:36:27*: attacchi agli impianti idrici USA "nell'estate 2026". Evento successivo alle fonti a disposizione di chi scrive, non verificabile; il docente stesso non entra nei dettagli perché l'analisi è in corso.
- \[?\] *Teams 1 @ 0:29:30*: "CrowdStrike che vende soluzioni EDR anche alla Microsoft": non chiaro se intenda che Microsoft sia cliente o partner; probabilmente intende i clienti enterprise di Microsoft.
- \[?\] *Teams 1 @ 0:01:18* e *0:13:30*: il docente dice "cyber threat intelligence" dove la trascrizione riporta "Cybertrade Intelligence"; corretto nel testo.
- *Teams 1 @ 0:24:09*: "non essere sufficientemente immature": evidente lapsus per "mature" (o "essere immature").
- *Teams 1 @ 1:11:36*: "la direttiva di privacy" senza ulteriori specificazioni (vedi nota nella sezione 16).
- Lezione "prossima": il docente dice che il ransomware si vedrà "la prossima o le prossime lezioni" (*Teams 1 @ 1:14:17*), ma a *0:23:40* rinvia DoS e ransomware al master di secondo livello. Da verificare con le lezioni 2026 successive (vedi sezione Esame).
- Trascrizione automatica corretta nel testo: "Cybertrade Intelligence/Cybercreat Intelligence" = cyber threat intelligence; "IAU" = Yahoo; "Cloudstrike/cloudstry" = CrowdStrike; "IDR and point detection response" = EDR, endpoint detection and response; "staxnet" = Stuxnet; "sbolla" = Hezbollah; "[sondaggioa.cn](http://sondaggioa.cn)", "l'a CN" = ACN; "igienesi cibernetico" = igiene cibernetica; "triade scia o triade read" = triade CIA o RID; "Moana Cry/Mona Crai/buona kreimap/One Cry/wannacry" = WannaCry; "nis, due direttive al nis, due di regolamento d'ora" = direttive NIS e NIS2, regolamento DORA; "LNHS" = l'NHS; "Esecurity awareness" = security awareness; "Air gaped" = air-gapped; "IAE" = IA.
## 22. Esame
Tutto ciò che la lezione dice su esame, organizzazione e rapporto con gli altri corsi:
- **Esclusione esplicita** (*Teams 1 @ 0:14:30*): l'elenco degli incidenti 2000-2020 (slide "A data security retrospective") "non sarà oggetto di esame"; serve solo a farsi un'idea dell'evoluzione degli attacchi.
- **Obiettivo del corso** (*Teams 1 @ 0:49:21*): non formare esperti di sicurezza ma data analyst consapevoli, capaci di applicare i principi della sicurezza ai dati e alle soluzioni che li trattano. Segnale di livello atteso: concetti e ragionamento, non dettagli tecnici da specialista.
- **Due corsi con lo stesso docente** (*Teams 1 @ 0:04:24*, *0:07:05*): questo è il "primo corso"; il "secondo corso che vedrete con me" ne è l'evoluzione e tratta soprattutto le **identità digitali** applicate all'analisi dei dati.
- **Rinvii al master di secondo livello.** Il docente colloca esplicitamente alcuni argomenti nel master di secondo livello:
	- CERT e Red Team: "se non nel primo corso, nel corso per il master di secondo livello" (*Teams 1 @ 0:03:52*);
	- approfondimento del "fare sistema" con temi di cyber intelligence, "soprattutto per chi rimarrà per il master di secondo livello" (*Teams 1 @ 0:13:30*);
	- **DoS e ransomware**: "poi li vedremo nel corso del master di secondo livello" (*Teams 1 @ 0:23:40*); ma a *1:14:17* dice che il ransomware si vedrà "la prossima o le prossime lezioni";
	- la **triade dell'informazione** tornerà "nel master di secondo livello, quando parleremo di cyber intelligence" (*Teams 1 @ 0:56:27*).
	Nell'edizione 2025 questi argomenti erano tutti trattati nel corso di primo livello (capitoli 02, 03, 06, 07): per capire che cosa sia davvero in programma per l'esame 2026 va verificato con le lezioni 2026 successive.
- **Argomenti annunciati per le lezioni successive:** differenza fra sicurezza informatica e cybersicurezza "più avanti" (*Teams 1 @ 0:49:36*); data governance "brevemente" (*Teams 1 @ 0:03:15*); crittografia (*Teams 1 @ 1:08:18*); ransomware (*Teams 1 @ 1:14:17*).
- **Calendario:** la parte tassonomica "non so se la finiremo entro oggi" (*Teams 1 @ 0:53:54*); chiusura con "ci sentiamo domani" (*Teams 1 @ 1:25:41*), quindi lezione il giorno successivo, 08/09/2026.
- In questa lezione il docente **non** parla di modalità d'esame, date, consegne, materiali o bibliografia. Nell'edizione 2025 aveva detto che "fa fede solamente quello che vi dico nelle lezioni" (capitolo 05, sezione 16): vale come criterio anche per le definizioni di questo capitolo, fermo restando che i riquadri **Correzione** servono a non portare fuori un'informazione imprecisa.
