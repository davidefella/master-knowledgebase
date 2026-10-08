# 07 - Framework di analisi, verifiche e crittografia

> Fonte Notion: https://app.notion.com/p/3e712abc808d81ac9a11d1b704b11ee4 — ultima modifica 2026-09-27T11:48:03.507Z

**Corso:** Cybersecurity, Cyber Intelligence and Data Privacy, docente Walter Arrighetti
**Registrazione:** due file del portale (edizione 2025), entrambi Teams del 26/09/2025
- CS-07 (file portale `lezione_7`), 16:08 UTC, 105 secondi
- CS-08 (file portale `lezione_8`), 16:15 UTC, circa 01:10:00
**Fonti:** solo la registrazione (parlato e slide a schermo). Il docente non ha distribuito materiale.
> **Contesto.** La lezione 7 del 26/09/2025 è spezzata in due file. **CS-07** contiene solo l'avvio: il docente riprende il discorso sulle TTP e nomina MITRE ATT&CK, uno studente segnala che la condivisione dello schermo non si vede ("Scusi, questo si sta condividendo e non vediamo nulla"), il docente prova a sistemare anche la telecamera e la registrazione si interrompe. **CS-08**, cioè il file del portale chiamato `lezione_8`, è in realtà **la seconda parte della lezione 7**: riparte sette minuti dopo dallo stesso punto (TTP, MITRE ATT&CK) e arriva fino a chiavi pubbliche e private. Non è un'ottava lezione. Anche la pagina "lezione 1" del portale carica per errore questo stesso video (CS-08). I timestamp indicano il file: *CS-07 @ hh\:mm\:ss* o *CS-08 @ hh\:mm\:ss*.
>
> Il docente dichiara che è l'ultima lezione del corso: "nessun sistema è cyber sicuro, come spero di avervi trasmesso in questo corso **che oggi finisce**" (*CS-08 @ 00:49:59*). La crittografia è solo introdotta e verrà ripresa nel corso successivo, **Digital Identities and Trust Services**. "Ieri" (*CS-08 @ 00:22:24*) si riferisce alla lezione 6 del 25/09/2025.
> **Guida unica.** Il capitolo segue la lezione 2025 (portale) e integra, nei riquadri "Integrazione Teams 2026", ciò che il docente ha aggiunto o cambiato nell'edizione 2026. Riferimenti: `CS-0N @` per il 2025, `Teams N @` per il 2026.
## Indice
1. Ripresa: analisi strutturata e TTP
2. Il framework MITRE ATT&CK
3. Un modello-giocattolo di intrusione
4. La Cyber Kill Chain
5. Cyber Kill Chain e ATT&CK combinati
6. La Unified Kill Chain
7. Il Diamond Model, l'attribuzione e le combinazioni
8. Slide mostrate senza commento: Pyramid of Pain, ACH, matrice CoA
9. Verifiche di sicurezza: VA, PT, VAPT
10. Verifiche di cyber resilienza: red, purple e golden teaming, TLPT
11. Crittografia: dalla triade CIA alla triade del digital trust
12. Breve storia della crittografia
13. Robustezza e cripto-agilità
14. Crittologia, crittoanalisi e security through obscurity
15. Riservatezza: la cifratura
16. Crittografia simmetrica
17. Crittografia a chiave pubblica
18. Glossario
19. Punti incerti
20. Esame
---
## 1. Ripresa: analisi strutturata e TTP
*CS-07 @ 00:00:10*
A schermo in CS-07 compare solo la schermata iniziale di Teams (titolo "Cybersecurity, Cyber Intelligence & Data Privacy 2025", 2025-09-26 16:08 UTC) e poi le icone dei partecipanti: la condivisione non è visibile.
Il docente annuncia che la lezione "sarà più breve", pur essendo "un po' più lunga sempre per recuperare" (frase contraddittoria, riportata com'è; più avanti chiarisce che la parte di crittografia è "una mezza lezione", un po' più lunga perché ci sono ore da recuperare). Riprende il concetto introdotto la volta precedente: l'**analisi strutturata**, cioè la suddivisione delle metodologie usate dagli attori della minaccia, o più in generale dai ricercatori di sicurezza che simulano un attacco, in **tattiche, tecniche e procedure** (TTP). Esistono molti quadri di riferimento per le TTP; quello universalmente più usato, almeno da qualche anno, è il framework **ATT&CK** del consorzio **MITRE**.
A *CS-07 @ 00:01:06* uno studente interrompe: "Scusi, questo si sta condividendo e non vediamo nulla". Il docente prova a capire cosa succede ("non riesco neanche ad attivare la telecamera") e la registrazione si chiude.
*CS-08 @ 00:00:01*
Nel secondo file il docente riparte: i quadri di riferimento per le TTP servono a studiare la minaccia cyber sia negli **attacchi reali** sia negli **attacchi simulati**, condotti da specialisti e ricercatori di sicurezza, membri di **red team** e gruppi simili (argomento ripreso nella sezione 10).
## 2. Il framework MITRE ATT&CK
*CS-08 @ 00:00:34*
**Slide "The MITRE® ATT&CK™ framework"** (*CS-08 @ 00:02:04*). Una matrice ridotta a otto colonne (tattiche), ciascuna con il numero di tecniche e le celle delle tecniche; alcune celle hanno a destra una barra che indica sotto-tecniche (numero fra parentesi):
<table header-row="true">
<tr>
<td>Tattica</td>
<td>Tecniche a schermo</td>
</tr>
<tr>
<td>Initial Access (3 techniques)</td>
<td>Exploit Public-Facing Application; External Remote Services; Valid Accounts (2)</td>
</tr>
<tr>
<td>Execution (4 techniques)</td>
<td>Container Administration Command; Deploy Container; Scheduled Task/Job (1); User Execution (1)</td>
</tr>
<tr>
<td>Persistence (4 techniques)</td>
<td>External Remote Services; Implant Internal Image; Scheduled Task/Job (1); Valid Accounts (2)</td>
</tr>
<tr>
<td>Privilege Escalation (4 techniques)</td>
<td>Escape to Host; Exploitation for Privilege Escalation; Scheduled Task/Job (1); Valid Accounts (2)</td>
</tr>
<tr>
<td>Defense Evasion (6 techniques)</td>
<td>Build Image on Host; Deploy Container; Impair Defenses (1); Indicator Removal on Host; Masquerading (1); Valid Accounts (2)</td>
</tr>
<tr>
<td>Credential Access (2 techniques)</td>
<td>Brute Force (3); Unsecured Credentials (2)</td>
</tr>
<tr>
<td>Discovery (3 techniques)</td>
<td>Container and Resource Discovery; Network Service Scanning; Permission Groups Discovery</td>
</tr>
<tr>
<td>Impact (3 techniques)</td>
<td>Endpoint Denial of Service; Network Denial of Service; Resource Hijacking</td>
</tr>
</table>
Sotto, due link: `https://mitre-attack.github.io/attack-navigator` e `https://attack.mitre.org`. In basso a sinistra il logo MITRE ATT&CK.
> **Nota aggiunta:** le tecniche a schermo (Deploy Container, Escape to Host, Build Image on Host, Implant Internal Image) indicano che la matrice mostrata è quella di ATT&CK per l'ambito **Containers**, non la matrice Enterprise completa, che compare dopo.
Il framework suddivide gli attacchi in una **kill chain** (catena della compromissione, catena dell'attacco; letteralmente "catena dell'uccisione", gergo mutuato dalla dottrina militare, ripreso nella sezione 4). Il docente legge le fasi della slide: accesso iniziale, esecuzione, persistenza, scalata di privilegi, evasione dalle difese, accesso con credenziali, ricerca (*discovery*) e impatto. Per ciascuna fase individua delle **tattiche**: nelle colonne ci sono i nomi, "molto ad alto livello".
> **Nota aggiunta:** nella terminologia ufficiale di ATT&CK le colonne sono le **tattiche** (l'obiettivo tattico dell'attaccante), le celle sono le **tecniche**, e sotto le tecniche ci sono le **sotto-tecniche**; le "procedure" sono le implementazioni concrete osservate in attacchi reali. Il docente usa "fasi" per le colonne e fa corrispondere le procedure alle sotto-tecniche (vedi sotto).
Il docente invita a usare i due link: quello in basso è la pagina web del framework; quello in alto è una piccola applicazione web (il **Navigator**) con cui "giocare" con questo tipo di grafico, popolarlo e costruire una catena di compromissione.
*CS-08 @ 00:02:26*
**Slide "The MITRE® ATT&CK™ framework"**, seconda versione: un grafico di attacco reale costruito sulla matrice. Colonne: *Execution*, *Persistence*, *Defense Evasion*, *Discovery*, *Command And Control*, *Impact*, *Lateral Movement*; alcune tecniche evidenziate in rosso, arancione o azzurro e collegate da frecce a riquadri di evidenze. Legenda in basso: "How attack method was discovered/investigated": *Initial investigation using alerts and logs* (rosso), *Forensics* (arancione), *Reverse engineering threat intelligence OSINT* (azzurro). Riquadri leggibili:
- "ps" and "p" detected as [TROJAN.SH](http://TROJAN.SH).BOTGET.AA
- HKLM regsvr32 [js.mykings.top:280](http://js.mykings.top:280); HKLM msiexec.exe [js.mykings.top:280](http://js.mykings.top:280)
- Aegis log flagging malicious use of regsvr32.exe
- Mysa, Mysa1, Mysa2, Mysa3, ok
- EventConsumer: fuckyoumm2_consumer; EventFilter: fuckyoumm2_filter; FilterToConsumerBinding
- Aegis log flagging malicious use of msiexec.exe
- **Bootkit**: Disables AV scanners; Searches and disables other coinminers; APC injection; List of alternative C&Cs IPs from [upme0611.info/address.txt](http://upme0611.info/address.txt); Overall use of various domains to download components and configurations (ex. [ftp0118.info](http://ftp0118.info), [mykings.top](http://mykings.top), [oo000oo.me](http://oo000oo.me)); Downloads coinminer payload
- Download of additional components: [http://js/mykings.top:280/helloworld.msi](http://js/mykings.top:280/helloworld.msi), [http://js.mykings.top:280/v.sct](http://js.mykings.top:280/v.sct)
Tecniche evidenziate leggibili: in Execution *Command-Line Interface*, *PowerShell*, *Regsvr32*, *Rundll32*, *Scheduled Task*, *Scripting*, *Signed Binary Proxy Execution*, *Windows Management Instrumentation*; in Persistence *Bootkit*, *Registry Run Keys / Startup Folder*, *Scheduled Task*, *Windows Management Instrumentation Event Subscription*; in Defense Evasion *Disabling Security Tools*, *Process Injection*, *Regsvr32*, *Rundll32*, *Scripting*; in Discovery *Process Discovery*, *Security Software Discovery*; in Command And Control *Multi-Stage Channels*, *Remote File Copy*, *Standard Application Layer Protocol*; in Impact *Resource Hijacking*; in Lateral Movement *Remote File Copy*. Il resto delle celle è \[illeggibile\].
> **Nota aggiunta:** dai nomi a schermo ([mykings.top](http://mykings.top), coinminer, bootkit) il caso è la botnet di cryptomining nota come **MyKings**. Il docente non lo commenta.
**Slide "The MITRE® ATT&CK™ framework"**, versione Enterprise, *CS-08 @ 00:02:53* (testo da OCR, non verificato visivamente: una matrice più vecchia con conteggi del tipo "34 items", "63 items", "73 items") e *CS-08 @ 00:03:34* (verificata visivamente): matrice completa con quattordici colonne.
<table header-row="true">
<tr>
<td>Tattica</td>
<td>Tecniche</td>
</tr>
<tr>
<td>Reconnaissance</td>
<td>10</td>
</tr>
<tr>
<td>Resource Development</td>
<td>7</td>
</tr>
<tr>
<td>Initial Access</td>
<td>9</td>
</tr>
<tr>
<td>Execution</td>
<td>12</td>
</tr>
<tr>
<td>Persistence</td>
<td>19</td>
</tr>
<tr>
<td>Privilege Escalation</td>
<td>13</td>
</tr>
<tr>
<td>Defense Evasion</td>
<td>40</td>
</tr>
<tr>
<td>Credential Access</td>
<td>15</td>
</tr>
<tr>
<td>Discovery</td>
<td>29</td>
</tr>
<tr>
<td>Lateral Movement</td>
<td>9</td>
</tr>
<tr>
<td>Collection</td>
<td>17</td>
</tr>
<tr>
<td>Command and Control</td>
<td>16</td>
</tr>
<tr>
<td>Exfiltration</td>
<td>9</td>
</tr>
<tr>
<td>Impact</td>
<td>13</td>
</tr>
</table>
Le singole celle sono troppo piccole per essere trascritte in modo affidabile; si leggono per esempio *Active Scanning*, *Phishing for Information* (Reconnaissance), *Drive-by Compromise*, *Phishing*, *Supply Chain Compromise*, *Valid Accounts* (Initial Access), *Brute Force*, *OS Credential Dumping* (Credential Access), *Data Encrypted for Impact*, *Defacement*, *Resource Hijacking* (Impact).
### Tattiche, tecniche, sotto-tecniche
*CS-08 @ 00:02:26*
A livello delle tattiche il docente si ferma qui. Ogni tattica dispone di una serie di **tecniche** e ogni tecnica di una serie di **sotto-tecniche**. Il framework, che viene aggiornato nel tempo, permette di descrivere un attacco con il grado di precisione voluto: fermandosi alle tattiche, scendendo alle tecniche o a quello che il docente chiama livello delle procedure, "che in questo framework sono chiamate appunto sottotecniche".
L'uso del framework è riservato agli esperti. Serve soprattutto, come ricordato la lezione precedente, ad avere una **tassonomia** comune: capirsi fra pari quando ci si scambiano informazioni sulla minaccia, evitare che ciascuno chiami la stessa cosa con nomi diversi o, peggio, che si usi lo stesso nome per cose diverse. Tutti usano lo stesso vocabolario.
### Bibliografia e attribuzione
*CS-08 @ 00:03:40*
ATT&CK è molto potente perché sul sito del MITRE, accanto a ciascuna tecnica e sotto-tecnica, c'è una vera **bibliografia**: consente di risalire all'elenco degli attori della minaccia, almeno quelli noti, che usano quella sotto-tecnica, magari per una specifica tattica o fase della compromissione. Quindi, descrivendo un attacco che si sta ricostruendo durante un'indagine, si può usare il framework anche **allo scopo di attribuire** l'attacco: farsi dire dalla versione online dinamica quali attori della minaccia usano una catena di compromissione simile. "Il navigator serve a questo. Oltre che a fare tanti bei grafici che vengono usati nei rapporti."
## 3. Un modello-giocattolo di intrusione
*CS-08 @ 00:04:00*
**Slide "Some IT intrusion toy-model".** A sinistra un ciclo numerato: **01 READINESS** → **02 INTELLIGENCE GATHERING (OSINT)** → **03 ENTRY POINT ANALYSIS & EXPLOITATION** → **04 POST EXPLOITATION** → **05 LATERAL MOVEMENT** → **06 DATA EXFILTRATION** → **07 REPORTING**, con frecce di ritorno. In basso tre righe di pallini numerati:
- *(Application) Penetration test:* 01 e 03 e 07 pieni, 02 a metà, 04, 05, 06 grigi;
- *Ethical hacking & APT test:* 01–07 tutti pieni;
- *Custom test:* 01 e 07 pieni, 02–06 a metà.
A destra due screenshot. Il primo è Windows, finestra **"oil.crude.corp Properties"**, scheda *Security*: selezionato il gruppo *Domain Admins (OILDomain Admins)* (riquadro rosso); sotto, fra i *Permissions for Domain Admins*, in un riquadro rosso con *Allow* spuntato: *Replicating Directory Changes*, *Replicating Directory Changes All*, *Replicating Directory Changes In Filtered Set*. Il secondo è macOS, finestra **"Art Info"** di una cartella (2.7 MB, modificata il 7 settembre 2016), sezione *Sharing & Permissions*: "You can read and write"; *emilyparker* Read & Write, *staff* Read only, *everyone* Read only. Una freccia blu indica questa finestra.
Nell'immaginario collettivo, "usato e abusato" da letteratura e filmografia di genere, l'attaccante è una persona sola che opera dall'esterno, entra nella rete e ruba un segreto o modifica un dato. È solo uno dei possibili attacchi, tutt'altro che rappresentativo, e anche questo si può svolgere in tantissimi modi. Gli attori della minaccia raggiungono obiettivi diversi a seconda del loro fine ultimo, che non è sempre lo stesso.
Le due finestre sui permessi (di una cartella in macOS e del suo analogo in Windows) servono a sottolineare che l'attore della minaccia cerca una strada dentro un ambiente di rete che **non conosce**. A parte il caso dell'**insider threat**, in cui la minaccia viene dall'interno e l'attore ha già una conoscenza parziale dell'ambiente, o è stato istruito da un interno su dove andare, cosa fare e cosa trovare, di solito l'attore è esterno. In alcuni casi è un software automatizzato: "non necessariamente c'è il tizio nero col cappuccio dietro a tutto", spesso c'è un malware molto avanzato, un **APT**, capace di muoversi da solo nella rete. In ogni caso si opera **al buio**: bisogna trovare gli altri punti della rete dove spostarsi e acquisire i **diritti** necessari (amministratore, utente privilegiato, lettura o scrittura su file o risorse specifiche), senza i quali l'attacco non può proseguire lungo la catena della compromissione.
> **Nota aggiunta:** i permessi *Replicating Directory Changes* e *Replicating Directory Changes All* sul dominio sono quelli che consentono di replicare il database di Active Directory, compresi gli hash delle password; un account che li possiede può eseguire l'attacco noto come **DCSync**. È verosimilmente il motivo del riquadro rosso, ma il docente non lo dice.
## 4. La Cyber Kill Chain
*CS-08 @ 00:06:40*
**Slide "The Cyber Kill Chain® & other cyber kill chains"** (*CS-08 @ 00:07:05*). Sette archi colorati concatenati, numerati: 1. Reconnaissance, 2. Weaponization, 3. Delivery, 4. Exploitation, 5. Installation, 6. Command & Control, 7. Actions on Objectives. Nelle versioni successive le fasi si arricchiscono di descrizioni (testo da OCR, non verificato visivamente, *CS-08 @ 00:09:05* e *00:14:05*):
- **1. Reconnaissance**: Targets' research, identification, and selection.
- **2. Weaponization**: Pairing remote access malware with exploit into a deliverable payload (e.g. PDF and/or Office files). Customisation of the offensive infrastructure (C2).
- **3. Delivery**: Transmission of malware to target (e.g. via email, email attachments, websites, USB drives, ...).
- **4. Exploitation**: Once delivered, the malware is triggered, exploiting vulnerable applications or systems.
- **5. Installation**: The malware installs a backdoor on a target's system allowing persistent access (it becomes an implant).
- **6. Command & Control** e **7. Actions on Objectives**: descrizioni non presenti nell'OCR né nei frame \[illeggibile\].
Poiché i modus operandi sono tantissimi, ad alto livello si usa la **catena della compromissione**. Ne esistono molte; una delle più usate, soprattutto in ambito **difensivo** (da chi difende le organizzazioni e studia la minaccia da quel punto di vista, inclusi i ricercatori di sicurezza), è la **Cyber Kill Chain**, scritta con le iniziali maiuscole perché marchio registrato. Consta di sette fasi.
> **Nota aggiunta:** la Cyber Kill Chain® è un marchio di **Lockheed Martin**, che l'ha pubblicata nel 2011.
1. **Reconnaissance.** L'attore della minaccia fa ricerca sulla vittima, tipicamente dall'esterno o da una parte molto perimetrale, per identificare le informazioni utili alle fasi successive.
2. **Weaponization.** L'attore prepara le sue armi. Come la reconnaissance, avviene all'esterno del perimetro dell'organizzazione. In queste due fasi chi difende può fare ancora poco, perché l'attore non si è ancora manifestato: non si sa chi sta preparando le armi o chi sta verificando dall'esterno, magari con ricerche **OSINT**. Al massimo ci si prepara in modo **proattivo**.
3. **Delivery.** L'attore trasporta all'interno del perimetro il malware preparato nella weaponization, tipicamente con le informazioni raccolte nella reconnaissance: un'email o un allegato malevolo costruiti durante la weaponization, trasmessi con phishing, spear phishing o whaling, per invogliare qualcuno a fare un'operazione che mandi in esecuzione il malware su un computer aziendale.
4. **Exploitation.** Il malware eseguito prova, nella descrizione del docente, a compiere operazioni di **movimento laterale** o di **scalata di privilegi** per raggiungere le applicazioni vulnerabili.
5. **Installation**, detta anche fase di **persistenza**. Non tutte le minacce ce l'hanno. Il malware cerca di rimanere il più possibile persistente nell'ambiente. Molti malware girano nel contesto di un browser o del sistema operativo: se l'utente chiude il browser o riavvia, possono sparire del tutto, oppure lasciare tracce (file sul disco) che però richiedono di nuovo qualche azione. Per questo una delle prime operazioni dopo l'exploitation iniziale è eseguire tattiche per guadagnarsi la persistenza, anche se "l'attore" è il malware stesso programmato per farlo. Lo scopo: che il bersaglio non sia più in grado di rimuovere il malware o che, rimosso (anche solo perché il computer è stato spento), riappaia all'avvio successivo o poco dopo. È una delle fasi tecnicamente più importanti, essenziale negli attacchi che durano giorni, settimane o mesi, in cui l'attore resta nella rete cercando di rimanere invisibile.
6. **Command and Control.** Il malware, come visto nelle prime lezioni, dialoga con il command and control, con la **botnet**, in attesa di istruzioni da remoto. Non tutti gli attacchi sono uguali, quindi serve spesso un controllo più o meno manuale che arriva dall'esterno, da un attore nella "rete rossa" (dell'attaccante), mentre il malware risiede nella "rete blu" (della vittima). Il C2 permette di comandare "a bacchetta" il malware, o meglio il sistema in cui è installato.
7. **Actions on Objectives.** L'attore persegue i suoi obiettivi: se il fine è l'estorsione, lancia un ransomware; se è distruggere dati o rendere un sistema indisponibile, lancia le azioni per modificarli o cancellarli; se è appropriarsi di un segreto industriale, militare o comunque di un'informazione confidenziale, la trova e cerca di esfiltrarla.
> **Nota aggiunta:** nella slide (fase 4) l'exploitation è l'innesco del malware che sfrutta applicazioni o sistemi vulnerabili; movimento laterale e scalata di privilegi, che il docente associa a questa fase, in ATT&CK sono tattiche a sé (Lateral Movement, Privilege Escalation).
### Linearità: basta un anello
*CS-08 @ 00:12:39*
Si parla di **catena** perché è **lineare**: presuppone che l'attore percorra tutti gli step. Di solito l'unica fase opzionale è l'installazione, e in alcuni casi anche il command and control; ma per le minacce cyber di un certo livello, nello scenario attuale, sono tutti passaggi obbligati. L'attore deve riuscire in tutte le fasi, senza poterne saltare, e se viene interrotto in una la catena si spezza. Quindi, "come dicono gli ottimisti", **ai difensori basta individuare e interrompere un anello** per interrompere la minaccia, che si sostanzia davvero solo se arriva alla settima fase; l'attaccante invece deve riuscire in tutte e sette.
## 5. Cyber Kill Chain e ATT&CK combinati
*CS-08 @ 00:14:17*
**Slide "CKC vs ATT&CK™, compared".** A sinistra due colonne: *STAGES FOR CYBER KILL CHAIN* (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives) e *TACTICS FOR MITRE ATT&CK* (Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact). A destra sette frecce, ciascuna con le domande della fase e, sotto "+ MITRE ATT&CK", tecniche corrispondenti:
<table header-row="true">
<tr>
<td>Fase CKC</td>
<td>Domande</td>
<td>  • MITRE ATT&CK</td>
</tr>
<tr>
<td>Recon</td>
<td>Motivation; Preparation</td>
<td>Active scanning; Passive scanning; Determine domain & IP address space; Analyze 3rd party IT footprint</td>
</tr>
<tr>
<td>Weaponise</td>
<td>Configuration; Packaging</td>
<td>Malware; Scripting; Service Execution</td>
</tr>
<tr>
<td>Delivery</td>
<td>Mechanism of Delivery; Infection Vector</td>
<td>Spearphishing attachment / link; Exploit public-facing application; Supply chain compromise</td>
</tr>
<tr>
<td>Exploitation</td>
<td>Technical or human?; Application affected; Method & Characteristics</td>
<td>Local job scheduling; Scripting; Rundll32</td>
</tr>
<tr>
<td>Installation</td>
<td>Persistence; Characteristics of change; Acquiring additional components</td>
<td>App shimming; Hooking; Login items</td>
</tr>
<tr>
<td>C2</td>
<td>Communication between victim & adversary</td>
<td>Data obfuscation; Domain fronting; Web service</td>
</tr>
<tr>
<td>Actions & Objectives</td>
<td>What the adversary does when they have control of the system</td>
<td>Email collection; Data from local system / network share</td>
</tr>
</table>
**Slide "CKC + ATT&CK™ combined"** (*CS-08 @ 00:14:51*). A sinistra l'infografica "MITRE Kill Chain": le sette fasi con brevi descrizioni (Reconnaissance: Collecting email addresses, profile lists, conference information, etc.; Weaponization: Combining exploit through backdoors into deliverable payload; Delivery: Transferring weaponized bundle to the victim or targets via email, web, usb etc.; Exploitation: Exploiting a vulnerability to execute code on victim's system; Installation: Installing malware on the asset; Command & Control (c2): Remote manipulation of the victim's system(s) begin; Action on Objectives: "Hands on Keyboard" access to the intruders as they now have full read, write privileges), una barra temporale (*HOURS TO MONTHS* per le prime fasi, *SECONDS* per delivery ed exploitation, *MONTHS* per le ultime) e, accanto a ogni fase, riquadri con identificativi di tattiche. Leggibili: Pre-Attack TA0017 Organization Information Gathering, TA0012 Priority Definition Planning, TA0013 Priority Definition Direction, TA0019 People Weakness Identification, TA0015 Technical Information Gathering, TA0014 Target Selection, TA0020 Organization Weakness Identification, TA0016 People Information Gathering, TA0018 Technical Weakness Identification, TA0025 Stage Capabilities, TA0022 Establish & Maintain Infrastructure, TA0024 Test Capabilities, TA0021 Adversary OPSEC, TA0023 Build Capabilities; Attack TA0007 Discovery (24 Techniques), TA0001 Initial Access (9 techniques), TA0005 Defense Evasion (34 Techniques), TA0002 Execution (10 Techniques), TA0003 Persistence (18 Techniques), TA0011 Command and Control (16 Techniques), TA0004 Privilege Escalation (12 Techniques), TA0008 Lateral Movement (9 Techniques), TA0006 Credential Access (14 Techniques), TA0009 Collection (16 Techniques), TA0010 Exfiltration (9 Techniques), TA0040 Impact (13 Techniques). A destra:
> Combining two established structured analytic methodologies to provide a comprehensible, unique description of almost any attack chains. It is in fact:
> - divided into the 7 phases of the CKC and, for each phase
> - the TTPs employed according to the ATT&CK™ taxonomy is also provided
>
> Beneficial for information sharing outside own organisation.
Le kill chain come la CKC si possono usare insieme ad ATT&CK riempiendo ciascuna delle sette fasi con le tattiche, tecniche e procedure usate in quella fase. ATT&CK ha una sua kill chain, ma la più usata resta quella appena vista. Così non si descrive più la compromissione a grandi linee ma **fase per fase**, con tattiche, tecniche e, meglio ancora se disponibili, procedure o sotto-tecniche. Si ha un quadro più chiaro di come opera l'attore e quindi di quali **controlli di sicurezza fisica, logica e amministrativa** mettere in campo per difendersi da attacchi simili. La combinazione di queste due tecniche di analisi strutturata è particolarmente utile ai difensori.
> **Nota aggiunta:** gli identificativi TA0012–TA0025 della colonna "Pre-Attack" appartengono alla vecchia matrice PRE-ATT&CK, dismessa da MITRE nel 2020 e sostituita dalle tattiche Reconnaissance (TA0043) e Resource Development (TA0042). L'infografica è quindi precedente a quella data.
## 6. La Unified Kill Chain
*CS-08 @ 00:15:23*
**Slide "The Unified Kill Chain (UKC)"** (*CS-08 @ 00:15:51*). Tre cicli di frecce su una banda orizzontale, con il link `https://www.UnifiedKillChain.com`:
- **IN phase** (verde, cerchio "In"): sulla banda *Reconnaissance*, *Resource Development*; nel ciclo *Delivery*, *Social Engineering*, *Exploitation*, *Persistence*, *Defense Evasion*, *Command & Control*.
- **THROUGH phase** (arancione, cerchio "Through"): sulla banda *Pivoting*, *Discovery*, *Lateral Movement*; nel ciclo *Privilege Escalation*, *Execution*, *Credential Access*.
- **OUT phase** (rosso, cerchio "Out"): sulla banda *Collection*, *Objectives*; nel ciclo *Impact*, *Exfiltration*.
Non esiste un'unica kill chain; una particolarmente famosa in letteratura è la **Unified Kill Chain**. Il docente comincia a descriverla ("una catena di compromissione usata prima…"), chiede se c'è una domanda ("No, ok") e riprende a *CS-08 @ 00:16:33*; i circa 30 secondi intermedi non sono trascritti.
La UKC descrive l'attacco dal punto di vista dell'attaccante in tre macrofasi.
- **In.** L'attore cerca di inserirsi nel sistema; corrisponde sostanzialmente a reconnaissance, weaponization e delivery della kill chain classica, ma può essere molto profonda e arrivare fino al command and control. Il sistema raggiunto però **non è il sistema finale**: l'attore spesso deve farsi strada fra più sistemi e comprometterli tutti per arrivare ai **crown jewel**, i sistemi che deve davvero colpire nella riservatezza, integrità o disponibilità. Quindi le fasi di persistenza, command and control e installazione eseguite su computer del perimetro esterno la UKC le colloca nella fase *in*, perché riguardano i sistemi più esterni, da cui arriva la minaccia.
- **Through.** L'attraversamento dell'infrastruttura della vittima. Anche qui l'attore può fare più giri: per questo la UKC ha **convoluzioni circolari**, che strutturano il comportamento dell'attore nei sistemi intermedi che probabilmente (non è detto) deve attraversare uno dopo l'altro fino ai sistemi finali.
- **Out.** L'attore compie l'azione sugli obiettivi; si mappa sostanzialmente sull'*action on objectives* della CKC. Anche questa può ripetersi, perché l'attore può avere più obiettivi. Esempio: il **ransomware a multipla estorsione**, dove ogni leva estorsiva comporta attività diverse: cifrare i file; esfiltrarne una parte per dimostrare di aver avuto accesso alla rete; cancellarli; lasciare una lettera di riscatto o impiantare un sistema che la mostri a certi orari sui computer di altre persone.
Per questo le tre macrofasi possono avere "circonvoluzioni": possono ripetersi più volte all'interno di una catena.
## 7. Il Diamond Model, l'attribuzione e le combinazioni
*CS-08 @ 00:19:28*
**Slide "The "Diamond model"".** Al centro un rombo rosso con i vertici **Adversary** (in alto, icona di un personaggio con cappello), **Infrastructure** (sinistra), **Capability** (destra, icona di un razzo), **Victim** (in basso). In alto a sinistra un riquadro *Meta-Features*: Timestamp, Phase, Result, Direction, Methodology, Resources (accanto, una mascotte robot). In basso a destra un esempio di analisi con frecce numerate sul rombo:
1. Victim discovers malware (Victim → Capability)
2. Malware contains C2 domain (Capability → Infrastructure)
3. C2 Domain resolves to C2 IP address (Infrastructure, freccia circolare)
4. Firewall logs reveal further victims contacting C2 IP address (Infrastructure → Victim)
5. IP address ownership details reveal adversary (Infrastructure → Adversary)
L'ultimo modello della giornata è il **modello a diamante** di analisi strutturata. Descrive la minaccia ad altissimo livello e, almeno in questa forma, non usa le TTP. Si basa su un concetto semplice: per conoscere una minaccia basta sapere chi è l'**avversario** e chi è la **vittima** (i vertici in alto e in basso), e conoscere a sinistra l'**infrastruttura** e a destra la **capacità** tecnica, cioè le caratteristiche tecniche che l'avversario ha sfruttato.
> **Correzione:** a *CS-08 @ 00:20:16* il docente descrive l'infrastruttura come quella "che l'avversario colpisce". Nel Diamond Model l'**Infrastructure** è l'infrastruttura **usata dall'avversario** per veicolare la capacità (domini e IP di C2, server, account), come mostra l'esempio della slide stessa (C2 domain, C2 IP address); ciò che viene colpito è la **Victim**. Poco dopo (*00:20:47*) il docente cita correttamente "l'infrastruttura usata dall'attaccante per attaccare", accanto a "quale è l'infrastruttura attaccata".
Da solo il modello a diamante è **pressoché inutilizzabile in pratica**, ma si usa spesso ad altissimo livello nei **brief strategici**, per far capire a chi non mastica la minaccia cyber chi è la vittima e chi il carnefice, qual è l'infrastruttura usata dall'attaccante e quale quella attaccata. In realtà è un modello molto più complesso, con tantissime estensioni.
**Slide "Attribution of cyber incidents"** (*CS-08 @ 00:21:05*, non commentata esplicitamente). A sinistra un diamante esteso: in alto **Adversary** (WHO), in basso **Victimology** (WHO), al centro WHAT **Infrastructure**, HOW **Capabilites** (sic), WHY **Motivation**; sui bordi *Technical Contextual Indicators* e *Socio-political Contextual Indicators*, con *False flags* ai lati. Sopra *Cyber Threat Actor Profiling* (freccia *Profiling* verso il basso), sotto *Cyber Attack Investigation* (freccia *Investigation* verso l'alto). A destra una piramide: **Level 1: Cyberweapon** (base), **Level 2: Country or City**, **Level 3: Person or Organization** (vertice); a sinistra una freccia verso l'alto *Difficulty in attribution*, a destra una doppia freccia *Identification for attribution*.
### CKC + Diamond Model
*CS-08 @ 00:20:47*
**Slide "CKC + Diamond Model, combined"** (*CS-08 @ 00:22:08*). Una tabella: righe = le sette fasi (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, C2, Action on Objectives); colonne = *Thread₁ / Adversary₁ / Victim₁*, *Thread₂ / Adversary₁ / Victim₂*, *Thread₃ / Adversary₂ / Victim₃*. In ogni cella piccoli diamanti numerati da 1 a 14 collegati da frecce etichettate con lettere da A a O (il diamante 9 è tratteggiato; alcune frecce attraversano i thread, per esempio dal 7 verso l'8 e il 10). A destra:
> Combining two established structured analytic methodologies to provide a comprehensible, unique description of almost any attack chains. It is in fact:
> - is divided into the 7 phases of the CKC and, for each phase
> - a diamond is provided highlighting what is known for that phase, and what it not
> - TTPs according to ATT&CK™ framework may still be provided for further detailing
Il Diamond Model diventa particolarmente efficace **combinato con una kill chain**: si suddivide l'attacco nelle fasi (qui la CKC, ma potrebbe essere la UKC) e per ciascuna si descrive con un diamante chi è stato vittima o bersaglio e quali infrastrutture e capacità sono state usate. Soprattutto negli attacchi con più attività in contemporanea da parte dell'attore, il Diamond Model combinato con gli altri, magari associando a ogni fase anche le TTP secondo ATT&CK, permette una descrizione **molto oggettiva** dell'attacco, utile per trasferire informazioni di **cyber threat intelligence di tipo operativo** a un'altra controparte.
## 8. Slide mostrate senza commento: Pyramid of Pain, ACH, matrice CoA
*CS-08 @ 00:22:16*
Passando alle verifiche di sicurezza, il docente scorre in circa tre secondi tre slide senza commentarle. Si riportano per completezza.
**Slide "The Pyramid of Pain"** (*CS-08 @ 00:22:16*). Piramide a sei livelli, dal basso: **HASH VALUES** (EASY), **IP ADDRESS**, **DOMAIN NAME** (SIMPLE), **NETWORK/HOST ARTIFACTS** (ANNOYING), **TOOLS** (CHALLENGING), **TTP** (TOUGH, al vertice).
**Slide "Analysis of competing hypotheses (ACH)"** (*CS-08 @ 00:22:17*). A sinistra una matrice: colonne "Hackers are stealing commercial information", "Insiders are selling commercial information", "Listening devices have been placed in our offices"; righe (EVIDENCE) con valori C = Consistent, I = Inconsistent:
<table header-row="true">
<tr>
<td>Evidence</td>
<td>Hackers</td>
<td>Insiders</td>
<td>Listening devices</td>
</tr>
<tr>
<td>Our quotes are consistently and narrowly beaten on price</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Many of our exact phrases in competitor bids</td>
<td>C</td>
<td>C</td>
<td>I</td>
</tr>
<tr>
<td>Leaked information is from all departments</td>
<td>C</td>
<td>I</td>
<td>I</td>
</tr>
<tr>
<td>Network security is unsophisticated</td>
<td>C</td>
<td>I</td>
<td>I</td>
</tr>
<tr>
<td>Network traffic heightened prior to major bids</td>
<td>C</td>
<td>I</td>
<td>I</td>
</tr>
</table>
A destra:
- **Traditional ACH**: analysts operating over several intelligence sources ("INTs") have relied on a way to effectively test both their producers and the data coming from them in order to measure evidence against them.
- **ACH in CTI**: producers and consumers of CTI have largely relied on ACH to evaluate data and analyse it on the basis of identifying attribution, patterns, and more.
In basso una tabella di punteggio (1 = Evidence maps positive towards the hypothesis; 0 = neutral; -1 = negative):
<table header-row="true">
<tr>
<td></td>
<td>H1</td>
<td>H2</td>
<td>H3</td>
<td>H4</td>
<td>H5</td>
</tr>
<tr>
<td>Evidence 1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>-1</td>
</tr>
<tr>
<td>Evidence 2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>-1</td>
</tr>
<tr>
<td>Evidence 3</td>
<td>1</td>
<td>-1</td>
<td>-1</td>
<td>1</td>
<td>-1</td>
</tr>
<tr>
<td>Evidence 4</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>-1</td>
</tr>
<tr>
<td>Evidence 5</td>
<td>1</td>
<td>-1</td>
<td>-1</td>
<td>-1</td>
<td>-1</td>
</tr>
<tr>
<td>**Scoring**</td>
<td>**5**</td>
<td>**1**</td>
<td>**-1**</td>
<td>**2**</td>
<td>**-5**</td>
</tr>
</table>
Le somme per colonna sono state verificate con Python e coincidono con la riga *Scoring*.
**Slide "The Courses of Action (CoA) matrix"** (*CS-08 @ 00:22:18*).
<table header-row="true">
<tr>
<td>Phase</td>
<td>Detect</td>
<td>Deny</td>
<td>Disrupt</td>
<td>Degrade</td>
<td>Deceive</td>
<td>Destroy</td>
</tr>
<tr>
<td>Reconnaissance</td>
<td>Web analytics</td>
<td>Firewall ACL</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Weaponization</td>
<td>NIDS</td>
<td>NIPS</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Delivery</td>
<td>Vigilant user</td>
<td>Proxy filter</td>
<td>In-line AV</td>
<td>Queuing</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Exploitation</td>
<td>HIDS</td>
<td>Patch</td>
<td>DEP</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Installation</td>
<td>HIDS</td>
<td>"chroot" jail</td>
<td>AV</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>C2</td>
<td>NIDS</td>
<td>Firewall ACL</td>
<td>NIPS</td>
<td>Tarpit</td>
<td>DNS redirect</td>
<td></td>
</tr>
<tr>
<td>Actions on Objectives</td>
<td>Audit log</td>
<td></td>
<td></td>
<td>Quality of Service</td>
<td>Honeypot</td>
<td></td>
</tr>
</table>
> **Nota aggiunta:** la Pyramid of Pain (David Bianco, 2013) ordina gli indicatori per quanto "fa male" all'attaccante vederseli bloccare: cambiare un hash è banale, cambiare TTP è difficilissimo. La matrice CoA è quella del paper Lockheed Martin sulla kill chain (Hutchins, Cloppert, Amin, 2011). Nessuno dei due riferimenti è citato nella lezione.
## 9. Verifiche di sicurezza: VA, PT, VAPT
*CS-08 @ 00:21:52*
**Slide di sezione** (*CS-08 @ 00:22:19*): immagine di un cavallo di Troia robotico con occhio rosso e le scritte **RED TEAMING**; titolo **"Cyber security & resilience testing"**, sottotitolo *Cybersecurity controls and tactics*.
"Adesso due parole rapidissime sulle verifiche di sicurezza." Molti presidi di sicurezza sono di tipo tecnico, ma **verificare** è un presidio di tipo **amministrativo**. "Come dicevo ieri, fidarsi delle cose è bene, ma verificare è sempre meglio."
**Slide "Vulnerability Management"** (*CS-08 @ 00:22:40*). A sinistra la scheda NVD di **CVE-2023-5625 Detail**: *Description*: "A regression was introduced in the Red Hat build of python-eventlet due to a change in the patch application strategy, resulting in a patch for CVE-2021-21419 not being applied for all builds of all products." *Severity*, CVSS Version 3.x, NIST: NVD, **Base Score: 7.5 HIGH**, **Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H**. Sotto, *Known Affected Software Configurations*: cpe:2.3\:a\:redhat\:openshift_container_platform_for_arm64\:4.12, …_for_linuxone:4.12, …_for_power:4.12, openshift_container_platform_ibm_z_systems:4.12; *Running on/with* cpe:2.3\:o\:redhat\:enterprise_linux\:8.0 e 9.0. A destra un diagramma di insiemi: un'ellisse *All Known vulnerabilities* che contiene *Found Vulnerabilities* ed *Exploitable Vulnerabilities*; una freccia indica la loro intersezione come *Vulnerabilities to mitigate first*. In basso: "The purpose of a **vulnerability assessment (VA)** is to discover as many vulnerabilities as possible, decide how risky they are to your environment, and the reduce the risk they pose."
Il punteggio 7.5 è coerente con il vettore mostrato: ricalcolato in Python con la formula CVSS 3.1 (impatto solo sulla disponibilità, alto; attacco di rete, bassa complessità, nessun privilegio né interazione) dà 7.5.
Da un lato ci sono le verifiche volte a individuare le **singole vulnerabilità nei singoli prodotti**: il **CVE**, ad esempio, è il database di cui si è parlato che raccoglie le vulnerabilità pubblicate a livello globale. Dall'altro, molto spesso serve un'analisi, un **vulnerability assessment**, all'interno della propria struttura.
**Slide "Vulnerability assessment (VA)"** (*CS-08 @ 00:22:59*):
- In a "*white-box*" testing scenario the auditor has complete knowledge of the environment to be evaluated (topology, configurations, network addresses, OS versions, test accounts, ...);
	- This typically happens when an organisation hires an **external** assessor to security-test it.
- In a "*black-box*" testing scenario, instead, the auditor has limited or no knowledge at all of the environment under evaluation;
	- Organisation may still hire external assessor to minimise biases and get a clear picture of their external security perimeter that closely matches what a real threat actor may independently assess.
Sotto, tre cubi: *BLACK-BOX TESTING* (ZERO KNOWLEDGE), *GRAY-BOX TESTING* (SOME KNOWLEDGE), *WHITE-BOX TESTING* (FULL KNOWLEDGE); a destra due schemi *Input → Output*: *Black-Box* (scatola nera piena) e *White-Box* (scatola con i blocchi interni visibili).
In alcuni casi si usano VA che tengono conto di **come è fatto dentro** il sistema: se si ha il codice sorgente, si testa direttamente quello e non il prodotto finito, per cercare falle di sicurezza (**white box**). Altre volte si usa un approccio **black box**: lo strumento o il soggetto (l'auditor) che fa la verifica è esterno e non conosce nulla dell'ambiente interno dell'organizzazione né degli aspetti tecnici del prodotto hardware o software, per verificare che cosa viene effettivamente rilevato.
**Slide "Penetration testing (PT)"** (*CS-08 @ 00:23:57*). Cinque voci con icone (il trattino lungo della slide è reso qui con i due punti):
- **External testing**: External penetration tests target a company's assets that are visible on the internet, such as the web application itself, the company website, and email and domain name servers (DNS). The purpose of this testing method is for the tester to access and extract meaningful information.
- **Internal testing**: Penetration testers with access to a program behind its firewall imitate an attack during internal testing. Engaging with an employee whose personal information was taken as a result of a phishing attempt is a popular testing scenario for this strategy.
- **Blind testing**: When a blind testing method is carried out, ethical hackers are provided only with the company's name. This gives the company and its employees insight into what an attack would look like and the potential consequences.
- **Double-blind testing**: When double-blind testing is carried out, employees in charge of security are not informed in advance that a simulated attack will take place. This way, they won't have any time to prepare their defences before an attempted breach, just like an actual attack. *This is common to most types of red-team testing & to all TLPTs (cfr. below).*
- **Targeted testing**: With the targeted testing approach, both the security professionals and the pen tester collaborate and keep each other informed of their whereabouts. This approach is a fantastic training exercise that delivers feedback from the perspective of a hacker to the company's security staff. *This is in common with all purple-team testing.*
Poi ci sono attività più pratiche, che consistono nel provare a **rompere**, a **penetrare** un sistema: il **penetration testing** (PT). Spesso VA e PT si fanno uno dopo l'altro: il VA individua potenziali vulnerabilità, poi un PT, tipicamente affidato a un esterno "che non ha bias informativi", verifica se le vulnerabilità trovate nel VA (black o white box) siano **effettivamente sfruttabili**. Nel gergo si parla di **VAPT** per questo processo unico fatto da un VA prima e da un PT dopo. Sono verifiche a scopo difensivo e proattivo che, almeno in teoria, le organizzazioni mature dovrebbero eseguire periodicamente per prepararsi a un'eventuale minaccia.
### Integrazione Teams 2026 (lezione 5 2026)
*Capitolo 07, sezione 9 (Verifiche di sicurezza: VA, PT, VAPT)*
- **Scopo del blocco.** L'obiettivo dichiarato è dare a chi lavora sui dati un **vocabolario** per capire come mettere in sicurezza i dati; a volte è lo stesso data scientist o data analyst a dover dire quale test serve, perché la natura del dato (generazione, acquisizione, trattamento, conversione, condivisione, backup) dà indicazioni sui presidi. Il firewall oggi è necessario ma di utilità "molto limitata". (Teams 5b @ 0:57:20 - 0:59:26)
- **Vulnerability and Patch Management (VPM).** Nuovo rispetto al 2025 (che partiva dal VA): processo, per lo più automatizzato, che scarica più volte al giorno le nuove CVE e le incrocia con l'**asset management**, l'inventario completo e aggiornato di hardware, software e firmware (punto dolente di molte organizzazioni). L'inventario non basta coi numeri seriali dei cespiti: servono indirizzi IP, numeri di licenza, versione esatta del sistema operativo e livello di patching (un laptop spento due giorni per malattia o ferie può restare indietro). Se l'elenco dei prodotti vulnerabili della CVE combacia con un asset, il sistema marca le macchine e, se buono, lancia l'aggiornamento. Esempio: la CVE su Red Hat Enterprise Linux 8 e 9 e OpenShift 4.12 (la stessa slide del 2025). Solo le aziende più grandi e mature lo fanno seriamente; le altre si affidano agli aggiornamenti del sistema operativo o alla buona volontà dei dipendenti. (Teams 5b @ 0:59:26 - 1:04:32)
- **Vulnerabilità presente ma non esposta: controllo compensativo.** Esempio nuovo: server SQL vulnerabile perché l'utente amministratore **SA** non supporta l'autenticazione a più fattori; i sicuristi mettono davanti al portale web un filtro che nega a monte ogni richiesta di login come SA. È un **controllo compensativo**: non elimina la vulnerabilità ma la compensa; se l'attaccante bypassa il portale e arriva al database da riga di comando, il VPM deve comunque aggiornare il server. Da qui la necessità del VA per misurare l'esposizione reale. (Teams 5b @ 1:04:39 - 1:06:35)
- **VA automatico e manuale.** Il VA può essere una mera **vulnerability scanning** automatizzata (spesso fatta dagli stessi sistemi di VPM), un software assistito, o un'attività manuale di un auditor. (Teams 5b @ 1:06:35 - 1:07:38)
- **White, grey, black box.** Il 2026 aggiunge che l'auditor interno fa per forza white box o al massimo **grey box**, perché è impossibile che non conosca l'ambiente, mentre il black box è il più tipico con l'assessor esterno; all'esterno si può anche dare deliberatamente la conoscenza di un interno (white box). (Teams 5b @ 1:07:38 - 1:09:09)
- **Tipi di penetration test.** Esterno (sito web, server email, servizi cloud), interno (il pentester, anche consulente esterno, riceve un accesso dentro la rete), e il nuovo **out-to-in**: bisogna prima entrare nella rete dall'esterno e poi testare il sistema interno, per verificare la reale sfruttabilità dall'esterno. Blind = black box: il pentester sa solo ciò che è pubblico. (Teams 5b @ 1:09:09 - 1:11:09)
- **Double blind: il perché.** Nuovo e ben argomentato: se i sicuristi sanno che domani c'è un pentest, anche in buona fede guardano di più i monitor o "blindano" il sito per un giorno per fare bella figura; oppure, a un allarme, pensano "è il pentester" mentre è un disco rotto o un'intrusione reale in contemporanea. Il doppio cieco elimina questi bias comportamentali ed è caratteristica fondamentale dei TLPT e di molti red team. (Teams 5b @ 1:11:09 - 1:13:17)
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 07, sezione 9 e 10 (verifiche di sicurezza e di cyber resilienza)*
- **Terminologia delle verifiche.** Il docente distingue tre parole del gergo: *test* (verifica), *assessment* (valutazione), *analysis* (analisi), che stanno alla base di varie procedure organizzative. Il risk assessment non riguarda solo il rischio cyber ma anche quello operativo e di business. (Teams 6 @ 0:01:06)
- **BIA accompagnata da test.** La business impact analysis resta fuori dal corso (come nel 2025), ma aggiunge che, quando l'oggetto del cambiamento di business è un sistema informatico, la BIA può essere accompagnata almeno da un VA e da un PT. (Teams 6 @ 0:02:07)
- **DPIA più dettagliata.** La valutazione d'impatto sulla protezione dei dati (nella trascrizione "DPA") è un'analisi di tutti i tipi di dati personali trattati, per l'intera organizzazione, per un servizio, per una linea di business o per l'oggetto di un test. Il GDPR la prescrive in alcuni casi; va presentata alle funzioni che gestiscono la protezione dei dati; può far scattare obblighi di tutela, normativi e informativi verso la clientela. Rientra "nel cappello" della privacy e del GDPR. Rispetto al 2025 non ripete l'affermazione sul DPO che decide le DPIA facoltative. (Teams 6 @ 0:02:53)
- **TLPT: solo nel finanziario, con questo nome.** Oggi i TLPT con questo nome esistono solo nel settore finanziario perché previsti da DORA; con altri nomi e framework restano red team molto avanzati. Il docente ripete le tre caratteristiche (CTI, segretezza, red team che emula la minaccia) con dettagli nuovi elencati sotto. (Teams 6 @ 0:04:32)
- **Scenari e red team misti.** Il TLPT si basa su uno o più scenari, anche interdipendenti, che possono coinvolgere funzioni critiche diverse. Il red team può essere interno, esterno o misto. (Teams 6 @ 0:05:37)
- **Il team di controllo e la de-escalation.** Nuovo esempio operativo: se il SOC rileva il red team e avvia le procedure interne e le notifiche obbligatorie (Garante privacy, Agenzia per la cybersicurezza nazionale come punto di contatto NIS, forze dell'ordine in caso di intrusione fisica), il team di controllo deve de-escalare subito: calmierando, rivelando che è in corso un test (e allora si passa di solito in purple team) oppure simulando un altro tipo di incidente. Il team di controllo "fino a qualche anno fa" si chiamava white team. (Teams 6 @ 0:06:24)
- **Segretezza per evitare bias.** Il test deve restare totalmente segreto al team di difesa, quasi tutto all'oscuro, perché misura la capacità di resistere e riprendersi. (Teams 6 @ 0:07:47)
- **Esperienza diretta.** Il docente dice di aver fatto parte di un red team. (Teams 6 @ 0:08:55)
- **Test in produzione (argomento nuovo).** Il TLPT si esegue tipicamente nell'**ambiente di produzione**, non in sviluppo, collaudo o certificazione. Un PT tradizionale su un singolo sistema (un database, un domain controller) può invece essere fatto su una copia isolata o in sandbox, il più possibile uguale alla produzione. Una funzione critica è un intreccio di sistemi, procedure, dati (pagamenti, ordini, dati fiscali, *cardholder data*) e persone (supporto tecnico, dipendenti bersaglio di phishing): replicarla in certificazione è impossibile o produce un test artificiale che non vede le vulnerabilità reali. Esempio ricorrente: la ditta di lacci da scarpe con e-commerce e sistema di pagamento certificato PCI DSS. (Teams 6 @ 0:09:16 - 0:13:10)
- **Report ai vertici.** I risultati dei test avanzati vengono approvati e distribuiti ai vertici; la cosa peggiore per un amministratore delegato è sentirsi dire "tutto a posto" e poi subire un attacco reale sfruttando un dettaglio procedurale non replicato in certificazione. Gli attori della minaccia dedicano settimane, mesi o anni a trovare proprio quelle piccole falle. (Teams 6 @ 0:12:19)
- **Perché tanta enfasi sui test.** Test di sicurezza e resilienza avanzati sono richiesti a vari soggetti dalla normativa europea: il docente cita la direttiva NIS, il Cyber Resilience Act, il Cybersecurity Act e il Digital Services Act ("ne parleremo più avanti"). Chi tratta molti dati è più esposto perché "il bottino è più grande", e le interdipendenze (cloud, filiere di fornitori) rendono insufficiente il singolo VAPT su un sistema. Vedi la precisazione in "Divergenze". (Teams 6 @ 0:14:00)
- **Morale: verificare da soli.** Nessun fornitore rivela al cliente i propri problemi di sicurezza, anche se risolti; la dichiarazione di conformità o un report del fornitore può non bastare: il cliente deve tipicamente verificare da solo. Collegamento con il "fidarsi è bene" del Capitolo 06, sezione 3. (Teams 6 @ 0:16:12 - 0:17:05)
## 10. Verifiche di cyber resilienza: red, purple e golden teaming, TLPT
*CS-08 @ 00:25:09*
**Slide "Cyber Resilience"** (*CS-08 @ 00:24:51*). A sinistra: "Cyber resilience refers to an entity's **ability to continuously deliver the intended outcome, despite cyber attacks**, responding and recovering its essential functionalities." E: "While **cybersecurity** focuses on defence (identify, deter, detect, prevent), **cyber resilience** focuses on protecting the entity once that its security has been compromised (respond, sustain, recover)." A destra un ciclo di frecce attorno a *CYBER RESILIENCE*, con una stella rossa *INCIDENT*: **IDENTIFY** (Identify the risks and gaps) → **PROTECT/DETECT** (Protect systems and detect intrusion) → **RESPOND** (Respond to incidents) → **SUSTAIN** (Sustain critical organizational operations during an incident) → **RECOVER** (Recover from an incident). In basso: "The continuously evolving cyber threat scenario forces organisations to enact their **situational awareness**: it is no longer a matter of *if*, but rather of *when* one shall be compromised."
Ci sono anche verifiche che cercano di capire **come reagisce** un'organizzazione o un sistema ICT quando è colpito o preso di mira da un vero attore della minaccia: le **verifiche di cyber resilienza**, evoluzioni del penetration testing. Il docente ne cita tre: **red teaming**, **purple teaming**, **golden teaming**.
**Slide "Cyber resilience testing and TLPT"** (costruita progressivamente da *CS-08 @ 00:25:23*, completa a *00:30:23*):
- Organisations that need to verify their **cyber-resilience** may enact scenario-based simulations of realistic attacks, as would be relevant to the organisation's evolutionary threat landscape.
- The G-7 already framed in 2018 the need for these tests to be based on three main characteristics:
	- **secrecy** about the tests, whose knowledge is restricted to a very limited **control team** (aka "white team");
	- **cyber threat intelligence (CTI)** processes to guide the test, tailored to relevance of the specific organisation;
	- being **covertly** performed by an independent (internal or external) **red team**, that emulates adversaries and their TTPs, according to threat-led scenarios provided by the above CTI.
- Una sequenza di frecce di intensità crescente: *vulnerability scanning* → *vulnerability assessment* → *penetration testing* → *red teaming* → *purple teaming* → *golden teaming*.
- All other members of the entity being tested are part of the **blue team** (i.e. the defenders).
- Sometimes, a **purple team** contact-group can be instituted, with members from the red and blue teams, to maximise the value of the test by cooperatively interacting *either* during *and* after it.
- Such higher-profile red team engagements are called **Threat-Led Penetration Tests (TLPTs)**.
- A **golden teaming** is a mostly *table-top* exercise to assess administrative resilience procedures.
### Red teaming e il G7
*CS-08 @ 00:25:41*
Di red teaming si parla già dalla metà degli anni Dieci. Diverse organizzazioni internazionali ne hanno colto l'opportunità: il **G7 nel 2018** ha consigliato attività di red teaming periodiche, uscendo con un documento mirato in particolare al **settore finanziario** che suggerisce verifiche di red teaming **guidate dalla minaccia**, e ha sottolineato l'importanza di sottoporle a processi di **cyber threat intelligence**: test avanzati basati sul reale scenario della minaccia, cioè sulle minacce concrete che nel periodo del test sono rilevanti per l'entità.
> **Nota aggiunta:** il documento è *G7 Fundamental Elements for Threat-Led Penetration Testing*, pubblicato dal G7 Cyber Expert Group nell'ottobre 2018.
Un **red team** è un test in cui una squadra (quindi "non una persona sola"), interna o esterna all'organizzazione, esattamente come un VAPT può essere affidato a un assessor, un auditor o un penetration tester interno o esterno, verifica sia la **concreta possibilità di sfruttare tecniche avanzate** contro un sistema ICT, sia la capacità del resto dell'organizzazione, il **blue team**, di **difendersi**. Verifica per esempio se l'organizzazione individua un attacco che sta per avvenire; se non lo individua prima, se lo individua mentre avviene. Molti attacchi reali sono molto silenziosi: più lunga è l'attività dell'attore nel sistema, più silenziosa deve essere per non farsi individuare. Quindi il red teaming non è solo un penetration test avanzato (verificare la concreta sfruttabilità di una minaccia) ma verifica anche **se il blue team ti individua** e, se sì, **se è in grado di interromperti**.
### Purple teaming
*CS-08 @ 00:27:48*
Spesso si ricorre a un **purple team**, un team viola, che può essere istituito anche durante l'esercizio. Se il blue team individua il red team, il red team potrebbe "togliersi la maschera": "aspetta, è un test, è un'esercitazione, fermiamoci". Invece di interrompere il test, che non darebbe vantaggio a nessuno, lo si prosegue facendo finta di non conoscersi oppure cooperativamente, così che il red team continui a imparare dal blue team e viceversa. È un concetto mutuato dalle esercitazioni di red teaming del **comparto difesa**; nel cyber il purple teaming è molto utile proprio perché consente di continuare a lavorare in modo collaborativo.
### TLPT
*CS-08 @ 00:28:39*
Quando gli attacchi di tipo red teaming sono **basati sulla minaccia**, cioè condotti per **emulare un reale attore** con TTP ben note (si spera) e quindi replicabili, e servono a verificare la concreta esposizione di un'organizzazione a una minaccia cyber, prendono il nome di **test di penetrazione guidati dalla minaccia**, **TLPT** (*Threat-Led Penetration Testing*). "Questa è tra l'altro una delle attività di cui mi occupo."
### Golden teaming
*CS-08 @ 00:29:41*
C'è poi una tipologia che in alcuni ambiti si chiama **gold teaming** o **golden teaming**, anche se il docente non ha ancora trovato un documento ufficiale, uno standard tecnico o una policy che la chiami così. Sono esercizi **tabletop**, cioè non pratici: non si effettua una compromissione reale né si cerca di simularla, se non in modo "cartolare". Blue team e red team si siedono allo stesso tavolo (e allora si conoscono) oppure a due tavoli diversi senza conoscersi, e simulano, scambiandosi messaggi o dialogando, non tanto il comportamento di un firewall quanto quello che avverrebbe a livello manageriale: come reagirebbe l'organizzazione, quali stratagemmi di **business continuity plan** o **disaster recovery plan** metterebbe in campo. Un esercizio che, se simulato realmente durante un \[?\] (probabilmente "red teaming"), potrebbe durare settimane o mesi, viene compresso in poche ore. Serve soprattutto a verificare la **cyber resilienza da un punto di vista organizzativo**.
Non tutte le organizzazioni fanno questi test: solo le più mature sono in grado di eseguire, e di eseguire periodicamente, le tipologie più avanzate. Tutti mirano ad aumentare le capacità di cyber security e cyber resilienza.
**Slide "Red, Purple and Golden teaming"** (*CS-08 @ 00:31:58*). Al centro una piramide, dal basso: *vulnerability scanning*, \[Patching and Updates\], *vulnerability assessment (VA)*, \[Patching and Updates\], *penetration testing (PT)*, \[Remediation\], *red / purple teaming*, \[Threat Hunting\], al vertice *gold teaming & TLPT*. A sinistra: "TLPT is a highly specialized flavour of red teaming engagement, where the **red team** performs **adversary emulation**." "The **red team** performs a *controlled* attempt against the tested entity's **critical function**(s), by emulating TTPs used by real adversaries." "TLPTs are routinely performed by entities whose cyber-resilience is regulated, e.g. **DORA** for financial entities." In alto a destra: "Also watch EP.3 - *Red Team* from the *Hacking Google* series: [www.youtube.com/watch?v=TusQWn2TQxQ](http://www.youtube.com/watch?v=TusQWn2TQxQ)". A destra tre riquadri tratteggiati: **business impact analysis (BIA)**, **risk assessment (RA)**, **data protection impact assessment (DPIA)**.
Queste verifiche sono contornate dall'altra classe di assessment già vista: la **business impact analysis** (non trattata, "non è oggetto di questo corso"), il **risk assessment** (già trattato: una verifica spesso anch'essa cartolare, a monte di un processo) e la **valutazione d'impatto sulla protezione dei dati personali**, la **DPIA**, in alcuni casi obbligatoria per legge: si fa sui sistemi che trattano dati personali ed è obbligatoria per alcune tipologie di trattamento e di sistemi; secondo il docente "tipicamente il DPO può decidere su quelle facoltative".
> **Correzione:** nel GDPR (art. 35) la DPIA è un obbligo e una decisione del **titolare del trattamento**, che deve **consultarsi** con il DPO (art. 35, par. 2). Il DPO fornisce un parere e ne sorveglia lo svolgimento (art. 39), ma non decide lui se farla.
> **Nota aggiunta:** DORA è il Regolamento (UE) 2022/2554 sulla resilienza operativa digitale del settore finanziario, applicabile dal 17 gennaio 2025; prevede TLPT periodici (almeno ogni tre anni) per le entità finanziarie individuate dalle autorità.
**Slide "The triad of "red-team testing""** (*CS-08 @ 00:33:10*). A sinistra un Venn a tre cerchi: *people*, *technologies*, *processes*. A destra tre figure incappucciate con laptop: *Red Team*, *Purple Team*, *Blue Team*; sotto un Venn a due cerchi: **RED TEAM** (Vulnerability Assessments, Penetration tests, Social Engineering, Physical intrusion), **BLUE TEAM** (Implementing Controls, Security Monitoring, Incidence response, Intrusion Detection), all'intersezione **PURPLE TEAM** (Proactive security). In alto lo stesso rimando alla serie *Hacking Google*.
Tornando ai red team: si differenziano da un penetration test per ambito e per scopo e soprattutto perché di fronte a un red team siede tipicamente almeno un **blue team** (può non esserci un purple team): il red team serve a testare anche la capacità del blue team. I red team più avanzati, e soprattutto i TLPT, **non sono test solo tecnologici**: come nella minaccia reale, coinvolgono anche la sicurezza e la resilienza dei **processi** aziendali e delle **persone**. In alcuni TLPT si possono simulare tentativi di **ingegneria sociale** e attacchi di **phishing**, e si possono inscenare davvero **compromissioni fisiche**: un red team esterno, di persone non note, prova a entrare fisicamente nell'azienda, magari nel data center, o a installare un piccolo dispositivo, un **access point Wi-Fi rogue**, nella rete, per poi fare altro da un camion parcheggiato fuori. Nel complesso sono attività di red team avanzato, che comprendono non solo il penetration testing ma anche l'**intrusione fisica** e l'**ingegneria sociale**.
A *CS-08 @ 00:33:55* compare per un istante la slide di titolo **"Threat-Led Penetration Testing (TLPT)"**, vuota, subito superata: il docente chiude la parte sulla sicurezza.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 07, sezione 10 (triade del red teaming), anticipata*
- Nel 2026 la triade del red teaming compare già in lezione 2. L'uso dei colori deriva dalla dottrina militare: soldati divisi in due squadre avversarie che si addestrano a vicenda. (Teams 2 @ 0:32:41 - 0:34:02)
- Mappatura nuova delle intersezioni della triade persone, processi, tecnologie: persone + tecnologie = intrusione fisica; persone + processi = social engineering; tecnologie + processi = penetration test tradizionale. In un test di red team ci sono di solito almeno due dei tre aspetti. (Teams 2 @ 0:35:23 - 0:35:56)
- Il red team non testa solo le tecnologie: attaccando persone (ingegneria sociale) o processi poco presidiati si può arrivare, con una catena di sfruttamenti, a sfruttare seriamente una vulnerabilità. (Teams 2 @ 0:34:35)
### Integrazione Teams 2026 (lezione 5 2026)
*Capitolo 07, sezione 10 (Verifiche di cyber resilienza)*
- **Sicurezza e resilienza.** Richiamo al NIST: i test visti finora verificano identificazione, protezione e prevenzione (cybersecurity); quelli di cyber resilienza verificano come l'organizzazione risponde all'incidente e recupera. (Teams 5b @ 1:13:17 - 1:13:54)
- **Tabletop exercise.** Nuovo come categoria autonoma e dettagliata (nel 2025 compariva solo dentro il golden teaming): "molti dicono che non serve a nulla, ma dipende a che livello lo fai". È un gioco di ruolo tipo wargame, anche su più giorni, con tutte le figure potenzialmente coinvolte, dall'AD (che di solito manda un delegato) al singolo informatico o impiegato. Può essere aziendale o di settore: l'ISAC bancario che verifica se l'attacco a una banca compromette le altre; l'ISAC sanitario che simula un nuovo **WannaCry** con ospedali che chiudono uno dopo l'altro; esistono tabletop non cyber (pronto soccorso in caso di cataclisma). Meccanica: si fa avanzare il tempo ("sono passate 20 ore e non hai mandato l'email: è cambiato il turno, chi sapeva sta dormendo"; "chi ha il DRP oggi non c'è, il DRP non si trova"). Serve a rivelare **buchi procedurali** prima degli esercizi reali: di solito si fa prima il tabletop e poi un test completo. (Teams 5b @ 1:14:04 - 1:17:58)
- **Red team e blue team.** Il blue team in astratto è "tutto il resto dell'organizzazione", il complementare del red team; in pratica si sceglie un gruppo di difensori, che in un red team doppio cieco può non sapere di essere il blue team. Il test **serve al blue team**, non al red team: conta la resilienza dell'organizzazione. Red team spesso esterni per le competenze elevate; aziende mature hanno red team interni o misti con specialisti esterni per parti specifiche. Nel 2026 il docente dice che del red teaming "avevamo parlato all'inizio del corso". (Teams 5b @ 1:17:58 - 1:20:14)
- **Purple team e targeted testing.** Sottoinsieme di membri di red e blue team che lavorano in modo cooperativo, senza segreti (*targeted testing*). Tre casi: il blue team individua l'attaccante e si prosegue informandolo; il blue team capisce da solo che è un esercizio; oppure, in alcuni framework, il purple teaming si fa **sempre alla fine**, "calando la maschera", come recap in forma di tabletop. Red e purple team sono le tipologie di test più mature. (Teams 5b @ 1:20:14 - 1:22:15)
- **G7 2018: tre caratteristiche, spiegate.** Segretezza (doppio cieco, conoscenza limitata al minimo: il CEO e probabilmente il CISO sì, CFO e CMO probabilmente no; è il gruppo di controllo, o **white team**); basati su minacce reali e rilevanti; emulazione delle **TTP** reali. Esempio nuovo di scelta dello scenario: se in questo trimestre il settore è preso di mira da un gruppo criminale che ricatta dipendenti con informazioni particolari per ottenere dati confidenziali, il TLPT deve emulare quello, non un attore statuale del Sud-est asiatico che spia la vita privata del board, rilevante in passato o in futuro ma non ora. (Teams 5b @ 1:22:15 - 1:25:46)
- **Golden teaming dentro il TLPT.** Nuovo: il golden teaming può essere uno degli scenari di un TLPT, eseguito a tavolino anziché praticamente dal red team; coinvolge solo l'alto management e verifica cosa accade se l'attaccante raggiunge i suoi obiettivi. (Teams 5b @ 1:26:02 - 1:26:48)
- **Piramide dei test.** VA risolti tipicamente con patch; PT che verificano catene di vulnerabilità concatenate (in cui "sono molto brave" le IA, richiamo alla lezione precedente); test a scenario con attaccante con obiettivi di alto livello (statuale, criminale, ideologico); TLPT guidati dalla minaccia, con remediation più ampie. Consiglia di nuovo l'episodio 3 della serie *Hacking Google* sul red team interno di Google ("se la cantano, come si dice a Roma", ma istruttivo). (Teams 5b @ 1:26:57 - 1:29:26)
- Non menziona in questa lezione BIA, DPIA, DORA né la triade people/technologies/processes del red teaming.
## 11. Crittografia: dalla triade CIA alla triade del digital trust
*CS-08 @ 00:33:41*
**Slide di sezione "Cryptography"** (*CS-08 @ 00:33:57*): un lucchetto su un circuito stampato.
Come anticipato, il docente comincia a parlare di **crittografia**. Sarà solo una lezione introduttiva, "una mezza lezione", un po' più lunga perché ci sono ore da recuperare; l'argomento sarà sviluppato nel corso di **Digital Identities and Trust Services**. Gli studenti hanno seguito altri corsi di crittografia più specifici; qui la crittografia è trattata da un punto di vista **applicato**.
**Slide "The Triad of Information Security"** (*CS-08 @ 00:34:35* e *00:35:35*, testo da OCR, non verificato visivamente). Un triangolo *INFORMATION SECURITY* con i lati CONFIDENTIALITY, INTEGRITY e, secondo l'OCR, AUTHENTICITY \[il terzo lato potrebbe essere mal letto dall'OCR\], e il testo:
- **Confidentiality**: Assurance that data can only be accessed by authorised subjects.
- **Integrity**: Assurance that data are neither unduly modified, nor tampered with, nor deleted.
- **Availability**: Assurance that (authorised) users may access data / IT services whenever they need.
- **Safety** (aggiunta a *00:35:35*): Assurance that information processing is neither harmful nor life-threatening to humans.
Delle triadi della sicurezza il docente ne aveva lasciata fuori una, tenuta per ultima. La prima vista è quella di **riservatezza, integrità e disponibilità**; si è parlato anche della sfera della **safety**. Quando però ci si concentra sui **dati**, la crittografia diventa uno snodo chiave.
Per la sicurezza dei dati valgono sempre i domini della **riservatezza** (ci sono dati che sono e devono essere riservati, come visto parlando di classificazioni di sicurezza) e dell'**integrità** (serve che il dato non sia corrotto). Serve certamente anche che il dato sia disponibile, ma quando si parla di **data security** nel senso dei presidi messi **dentro i dati** per renderli sicuri, la **disponibilità non è un dominio rilevante**, perché "il dato o c'è o non c'è". I presidi a protezione della disponibilità non sono fatti con i dati ma con altri controlli di sicurezza, fisici, logici o amministrativi.
**Slide "The Triad of Digital Trust"** (transizione a *CS-08 @ 00:36:27*, in cui il titolo si legge solo come "…l Trust"; versione completa a *00:36:28* e *00:39:28*, testo da OCR per il triangolo e la voce Privacy). Triangolo *CRYPTOGRAPHY* con i lati CONFIDENTIALITY, INTEGRITY, AUTHENTICITY. Testo (le prime tre voci verificate visivamente nel frame di transizione):
- **Confidentiality**: Assurance that data can only be accessed by authorised subjects.
- **Integrity**: Assurance that data are neither unduly modified, nor tampered with, nor deleted.
- **Authenticity**: Assurance that the origin of data can be identified (be it either a natural person, a legal person, or a technical source).
- **Privacy** (aggiunta a *00:39:28*, da OCR): Assurance that data subjects (interessati)'s personal data are processed in compliance with laws and regulations (e.g., for EU nationals, pursuant to GDPR).
Quando si parla di sicurezza dei dati intendendo **come i dati proteggono se stessi**, la sicurezza prende anche il nome di **digital trust** e poggia su una triade leggermente cambiata: al posto della **disponibilità**, che non si applica perché "il dato non può rendersi autodisponibile", c'è l'**autenticità**. La triade di riferimento da qui in poi è **riservatezza, integrità, autenticità**.
L'**autenticità** consiste nell'assicurare che l'**origine del dato** possa essere identificata. La fonte può essere:
- una **persona fisica**;
- una **persona giuridica**: un'organizzazione, una pubblica amministrazione, un'azienda, e secondo il docente anche "un libero professionista dotato di partita IVA, in Italia è una persona giuridica";
- un **sistema tecnico**: per un filmato di una telecamera che ha ripreso un reato in corso, potrei volere mezzi che garantiscano che il dato sia certificato, la famosa **catena di custodia**: sono sicuro che quel dato è stato generato proprio da quella telecamera. La telecamera potrebbe dover corredare il filmato di dati che ne provino l'autenticità.
> **Correzione:** un libero professionista con partita IVA è, nel diritto italiano, una **persona fisica** che esercita un'attività in forma individuale. La partita IVA è una posizione fiscale e non crea una persona giuridica distinta (a differenza, per esempio, di una S.r.l.).
L'autenticità è forse il dominio più importante nella sicurezza dei dati. Quando ha un valore così forte da essere **opponibile in giudizio**, cioè un valore legale, si parla appunto di **digital trust**.
### Privacy dal punto di vista tecnico
*CS-08 @ 00:38:05*
Di contorno c'è la **privacy**, finora vista dal punto di vista giuridico, che si declina anche dal punto di vista **tecnico** (esempi rimandati al corso successivo). A volte i dati devono essere protetti perché i diritti degli interessati sui propri dati personali siano trattati in conformità con le policy di volta in volta applicabili, per esempio in Europa per i dati dei cittadini europei ("abbiamo visto anche al di fuori dell'Europa"). La privacy dal punto di vista tecnico si traduce nell'insieme delle caratteristiche messe nei dati, tutte basate sulla crittografia, per garantire che i diritti degli interessati siano salvaguardati: che il dato sia trattato solo se l'interessato ha dato il **consenso** e soprattutto che, se lo **revoca**, il dato non sia più trattabile. Ci sono modi per garantire che, alla revoca del consenso, il dato, anche se rimane fisicamente nello storage, non sia più utilizzabile dal titolare, perché protetto con tecniche crittografiche (il docente non sa se ci sarà tempo di vederli).
> **Nota aggiunta:** come già segnalato per la lezione 2, l'ambito del GDPR dipende dalla localizzazione dell'interessato nell'Unione o dallo stabilimento del titolare, non dalla cittadinanza; la slide ("for EU nationals") e il parlato ripetono l'impostazione basata sulla cittadinanza. La tecnica a cui il docente allude per la revoca del consenso è nota come *crypto-shredding*: cifrare i dati con una chiave per interessato e distruggere la chiave.
### La crittografia è ovunque; autenticità e non ripudio
*CS-08 @ 00:40:22*
**Slide "The realms of Cryptography"** (*CS-08 @ 00:41:18*). Testo:
> Nowadays almost any data processing, in the Cloud or on-prem, involves cryptographic operations ("crypto"), even if that's usually transparent (i.e. invisible) to end users. Crypto is a key enabling factor of data security, as it enforces the CIA triad, as well as implementing **privacy** (from a technical standpoint), **authenticity** and non-repudiation, collectively referred to as ***digital trust*** (which will be reprised further on).
>
> Each time we surf the internet, enjoy streaming content (like music and films), pass by airport or e-customs borders, perform any electronic payment ("contact" of contactless), use any wireless devices, or authenticate online via our digital identities or simpler forms of authentication, cryptography is what actually enables all those data processing and movements, in a secure and trusted way.
Quattro riquadri illustrati (mittente, destinatario, intruso): **Confidentiality**: *Interception*, "Is Private?"; **Integrity**: *Modification*, "Has been altered?"; **Authentication**: *Forgery*, "Who am I dealing with?"; **Non-Repudiation**: *Claim* (con "Not SENT!"), "Who sent/received it?".
La crittografia la usiamo tutti i giorni, molto più spesso di quanto si pensi: ogni volta che si naviga su un sito internet avviene un'operazione crittografica; ogni volta che si striscia una carta di pagamento, fisica o contactless o virtuale sul telefono, c'è crittografia a salvaguardia della transazione e di entrambe le parti, chi paga e chi riceve.
Il **digital trust** è tipicamente una forma di **autenticità** così forte da ricevere spesso qualche forma di **valore legale**. Si dice spesso che è un'autenticità accompagnata dal **non ripudio**: l'impossibilità, anche per lo stesso titolare del dato, di dichiarare semplicemente che quel dato non è suo. Quando la tecnologia, oltre ad associare con un certo grado di garanzia un dato alla sua fonte, rende anche difficile per la fonte stessa negare che il dato provenga da lei, si parla di autenticità con non ripudio, cioè di digital trust.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 07, sezione 11 (triadi CIA, safety, privacy)*
- **Safety** vs security: sicurezza della salute e della vita; esempi di robot chirurgici, ecografi, sistemi di triage del pronto soccorso (Teams 1 @ 1:12\:08-1\:14:00).
- Privacy come "informatica della privacy": misure tecnologiche di conformità al GDPR e a regolamenti analoghi (Teams 1 @ 1:11:52).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 07, sezione 11 (triade del digital trust), anticipata*
- Nel 2026 la triade del digital trust (riservatezza, integrità, autenticità) viene presentata già nella seconda lezione, accanto alla CIA, perché ha in comune due vertici su tre. Il docente la chiama anche "triade della fede digitale" e precisa che sarà oggetto principale dell'altro corso (identità digitali e servizi fiduciari). (Teams 2 @ 0:00:25)
- Definizione operativa di fede digitale: la caratteristica che deve avere un servizio digitale perché soggetti diversi possano davvero usarlo, non solo per transazioni economiche ma per qualunque scambio di informazioni che porta a decisioni con conseguenze. Nel mondo analogico l'equivalente è controllare se un documento è firmato: da qui il tema delle firme digitali ed elettroniche. (Teams 2 @ 0:01:11)
- Autenticità: certezza che dati e informazioni provengano dal soggetto che ne è asseritamente l'autore, che sia persona fisica, persona giuridica o sorgente tecnica (computer, sito web). (Teams 2 @ 0:02:11)
- Esempio nuovo, il deepfake: gli studenti non hanno alcuna certezza che il video del docente in Teams non sia un deepfake. In una riunione in cui si prendono decisioni, acquisti o assunzioni, la mancanza di autenticità diventa critica; molti attacchi di furto d'identità sfruttano proprio questa mancanza. (Teams 2 @ 0:03:01)
- Legame esplicito con il master: riservatezza, integrità e autenticità sono garantite da tecniche hardware e software basate sulla crittografia, ed è per questo che nel master c'è "tanta crittografia". Sicurezza del dato = digital trust. (Teams 2 @ 0:04:45)
- Integrità: il dato va protetto non solo da manipolazioni malevole ma anche da modifiche per errore. Autenticità: se non si riesce a verificare l'origine di un'informazione importante, probabilmente la si scarta prima ancora di farsi altre domande. (Teams 2 @ 0:05:39, 0:06:08)
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezione 11 (dalla triade CIA al digital trust)*
- **Crittografia usata da entrambi i lati.** Nuovo inquadramento: la crittografia è usata dagli attaccanti (per esempio per un attacco ransomware) e dai difensori (sicurezza delle reti, integrità e autenticità dei sistemi). (Teams 7 @ 0:01:00)
- **Digital trust: dati che proteggono dati.** I presidi di digital trust usano dati crittografati per mettere in sicurezza altri dati; la disponibilità si presidia con altri sistemi, non con la crittografia. Come per la triade CIA, non tutte le applicazioni usano tutti e tre i vertici: a volte due, a volte uno solo. (Teams 7 @ 0:01:50 - 0:03:28)
- **Il browser come superficie d'attacco.** Dietro ogni HTTPS ci sono cifrature dei canali, scambi di certificati e verifiche di firme; il browser è un software complesso, aggiornato spesso con cadenza settimanale, con una superficie d'attacco ampia, e può essere oggetto o vettore di attacchi. (Teams 7 @ 0:04:47 - 0:06:29)
## 12. Breve storia della crittografia
*CS-08 @ 00:42:09*
**Slide di sezione "Of ciphers and men"**, sottotitolo *A very brief history of Cryptography* (*CS-08 @ 00:42:06*): a sinistra una scena del film *The Imitation Game* (un uomo accanto a una macchina elettromeccanica), a destra una parete di cassette postali numerate (574, 584, 604, 614, 624).
**Slide "Ancient ciphers"** (*CS-08 @ 00:43:12*). Testo: "A **scytale** was a tool to manually encrypt via transposition ciphers, like **Cæsar**'s, where characters are shifted by a predefined number (the **key**). Substitution ciphers were also common, where single characters are statically replaced according to a predetermined rule." In alto a destra una scitala (striscia di cuoio avvolta su un bastone con lettere) e sotto una tabella di corrispondenza a due righe: A B C D E F G H I J K L M sopra N O P Q R S T U V W X Y Z; poi **HELLO** → **URYYB** (e, sbiadito, il ritorno a HELLO). In basso a destra un disegno di due opliti che si passano una scitala. In basso a sinistra: "The Phaistos' Disc (Crete, II millennium B.C.) is a yet undecrypted *unicum*. Among many hypotheses, it may have been a sort of scytale."
L'esempio è stato verificato in Python: HELLO → URYYB è uno spostamento di 13 posizioni (ROT13), coerente con la tabella A↔N, …, M↔Z.
> **Correzione (slide):** il cifrario di Cesare, in cui ogni lettera è spostata di un numero fisso di posizioni, è un cifrario a **sostituzione** (monoalfabetica), non a **trasposizione**. La scitala invece è effettivamente un dispositivo di trasposizione: le lettere restano le stesse ma cambiano ordine. La slide mette sotto "transposition" l'esempio di Cesare, e lo schema HELLO → URYYB è una sostituzione.
Il docente si sofferma poco, perché gli studenti hanno fatto altri corsi. Nell'antichità la crittografia nasce soprattutto in **ambito militare**: bisognava trasferire informazioni tattiche da una parte all'altra di un campo di battaglia, e si sono inventate le tecniche più disparate. Il **disco di Festo** (a sinistra) non è un oggetto crittografico, anche se da alcuni è considerato un crittogramma; la **scitala** (a destra) era usata dagli antichi greci in guerra.
L'aneddoto: "persino nei poemi omerici" ci si riferisce al fatto che, per trasferire un'informazione tattica, si rasava a zero la testa di una persona, le si tatuava sulla cute l'informazione militare e la si mandava a piedi ad attraversare le linee nemiche. Il viaggio (camminate o cavalcate di giorni o settimane) bastava perché i capelli ricrescessero prima della frontiera; se il messaggero fosse stato preso, torturato o ucciso, non avrebbe potuto rivelare nulla. Il metodo si basava su quella che oggi si chiama **security through obscurity**: sul fatto che l'avversario non avrebbe pensato di radere la testa al messaggero.
> **Correzione:** l'episodio del messaggero con la testa rasata e tatuata non viene dai poemi omerici ma dalle *Storie* di **Erodoto** (Istieo che invia un messaggio ad Aristagora di Mileto). Inoltre tecnicamente è un esempio di **steganografia** (nascondere l'esistenza del messaggio), non di crittografia (renderlo incomprensibile); la lettura come security through obscurity del docente è coerente con questo.
I primi usi della crittografia sono militari, e la crittografia è diventata una delle primissime **discipline tecniche**: ben presto, per rendere i crittogrammi difficili da interpretare, si dovettero costruire **macchine** che rendessero impossibile il lavoro manuale di decifratura dell'avversario. La crittografia antica e soprattutto medievale si basava sul fatto che i due estremi della comunicazione avessero macchinari e tecnologie di cui l'avversario non doveva disporre. (Quello che oggi si chiama attore della minaccia, nella letteratura crittografica si chiama **avversario**.) Questa crittografia "arcaica", fino sostanzialmente al secondo dopoguerra, presidiava **un solo dominio**, la **riservatezza**: l'unico scopo di governi e militari era mantenere il dato riservato.
**Slide "Medieval and modern era ciphers"** (*CS-08 @ 00:44:41*, non commentata nel dettaglio). Testo:
> As decryption capabilities became *de facto* among war cabinets, diplomacy and espionage, more complex substitution ciphers were invented, with the aid of smart stratagems, even **clockwork** devices (sorts of legacy physical tokens). **Polyalphabetic** ciphers were born, based on the work of Arab mathematicians like Al-Qalqashandī (1355–1418) and Ibn Durayhim al-Mawsilī (1312–1359/62), who actually invented an early implementation of what was later (1508) called *tableau*, or *tabula recta*, which XVI-century ciphers were based upon: **Trithemius**' (described in book *Steganographia*), and **Vigenère**'s (invented by Leon Battista Alberti), which both used 26×26 matrices. **Nomenclator** ciphers were also common: one was used on the Babington Plot to assassinate Queen Elizabeth I (cracked in 1586 by her spymaster, Sir Walsingham); Rossignol's *Grand chiffre* (used by King Louis XIV, which was cracked only in 1893).
(Nella slide il trattino lungo prima di "even clockwork" è reso qui con una virgola.) Immagini: un cofanetto dorato con dischi cifranti (un libro-cifrario rinascimentale), una *tabula recta* 26×26 e un **cryptex** cilindrico a rotelle con lettere.
> **Nota aggiunta:** alcune attribuzioni della slide sono discusse. Alberti (*De cifris*, 1467) inventò il disco cifrante polialfabetico; il cifrario oggi detto "di Vigenère" fu descritto da Giovan Battista **Bellaso** nel 1553 e attribuito a Vigenère solo nell'Ottocento. La *tabula recta* compare nella *Polygraphia* di Tritemio (pubblicata nel 1518, scritta nel 1508), non nella *Steganographia*. Il *Grand Chiffre* fu decifrato da Étienne Bazeries nel 1893, come indicato.
**Slide "Ciphers up to "mechanical" cryptography"** (*CS-08 @ 00:45:03*; testo completo da *00:50:03*, da OCR, non verificato visivamente). Immagine di una macchina **Enigma** (pannello delle lampade con i rotori, tastiera, pannello dei collegamenti), accanto a un foglio di chiavi giornaliere tedesco ("Geheime Kommandosache… Achtung!") e il logo ENIGMA. Riquadro, verificato visivamente: "Cryptography is **robust** only if it is **anti-economic** for adversaries to attempt to reverse, or crack the mathematic algorithm it is based upon." Testo aggiunto (OCR):
> Rotor cipher machines started to be used as encryption devices in XIX century. They had to be "transportable" by military and covert agents, like SIGABA and Typex (Allies) and the famed German Enigma, which was initially "cracked" by Polish intelligence and mathematicians (Rejewski, Różycki and Zygalski), who built "bomb" machines for that. Alan Turing's electro-mechanical early computers, at MI6's Bletchley Park, could even brute-force Enigma codes within a few hours from Nazi forces using it to covertly communicate target positions for next dawn bombings to their aviation (Luftwaffe). However, Enigma codes could be cracked only in the afternoons after the bombings.
> **Correzione (slide):** le macchine cifranti a rotori entrarono in uso nel **XX secolo** (brevetti fra il 1917 e il 1919, Enigma commerciale dal 1923), non nel XIX.
### Enigma: la parabola della crittografia moderna
*CS-08 @ 00:44:40*
Ben presto le macchine crittografiche divennero così complesse da dover essere azionate prima meccanicamente e poi elettricamente. L'esempio più calzante è la **seconda guerra mondiale**: il docente invita a leggere o vedere *The Imitation Game*, che racconta come gli Alleati riuscirono a battere **Enigma**, nella versione militare usata dai nazisti, dando un contributo pesante alla vittoria. Lo racconta perché è "una specie di parabola della crittografia moderna".
La **Luftwaffe** usava queste macchine, camuffate da macchine da scrivere ma estremamente complesse, per trasmettere per telegrafo, di notte, le coordinate dei luoghi da bombardare all'alba. Gli Alleati intercettavano i messaggi e si erano procurati copie delle macchine, ma senza conoscere le **chiavi** (le combinazioni di bottoni da premere, di cavi da collegare fra loro come in un centralino telefonico dell'epoca e dei numeri da impostare sui tre rotori) era praticamente impossibile decifrare, anche disponendo di diverse macchine identiche.
Non perché fosse matematicamente impossibile: ogni algoritmo crittografico, "almeno classico", con un numero sufficiente di tentativi può essere rotto per **brute force**, provando tutte le combinazioni di chiavi fino a trovare quella usata. La questione, fondamentale anche oggi che si parla di crittografia **quantistica** e **post-quantistica**, era il **tempo**: le coordinate venivano telegrafate verso mezzanotte e il bombardamento avveniva prima dell'alba.
> **Nota aggiunta:** esiste un'eccezione classica al "tutto è rompibile per forza bruta": il **cifrario di Vernam** con chiave davvero casuale, lunga quanto il messaggio e usata una sola volta (one-time pad), è perfettamente sicuro nel senso di Shannon, perché provando tutte le chiavi si ottengono tutti i messaggi possibili della stessa lunghezza.
A **Bletchley Park** furono ingaggiati crittografi, matematici e ingegneri, fra cui **Alan Turing**, che propose di costruire una macchina, "quello che oggi viene universalmente considerato il primo calcolatore della storia", capace di calcolare a una velocità irraggiungibile per i crittografi che facevano i conti a mano e quindi di fare brute force molto più in fretta. Eppure, pur avendo abbattuto di diversi ordini di grandezza il tempo della ricerca esaustiva delle chiavi, la crittografia si rivelò **robusta**.
> **Correzione:** la macchina di Turing per Enigma, la **Bombe** (1940, derivata dalla *bomba* polacca), era un dispositivo **elettromeccanico specializzato**, non un calcolatore generale, e non è considerata "universalmente" il primo calcolatore della storia. A Bletchley Park il primo calcolatore elettronico programmabile fu **Colossus** (1943–44, Tommy Flowers), usato però contro la cifratura Lorenz, non contro Enigma. La Bombe inoltre non faceva una forza bruta pura: sfruttava i *crib* (porzioni di testo in chiaro presunte) per eliminare le impostazioni incompatibili. La slide stessa parla più correttamente di "electro-mechanical early computers".
### Robustezza come antieconomicità
*CS-08 @ 00:48:23*
Qui il docente introduce un po' di tassonomia. Una crittografia è **robusta** se diventa **antieconomico** per l'avversario cercare di "craccarla" (qui solo con la forza bruta). Nel caso di Enigma l'avversario erano gli Alleati, che cercavano di rompere la crittografia dei nazisti, ed era antieconomico perché **non c'era abbastanza tempo**: quando le macchine di Turing trovavano la chiave e quindi le coordinate, il bombardamento era avvenuto da diverse ore ("mi sembra che le prime volte riuscivano a decifrare il messaggio nel tardo pomeriggio"). Il dato decifrato non aveva più alcun valore: erano coordinate di un posto ormai raso al suolo. È lo stesso problema che si pone oggi con la crittografia post-quantistica.
La crittografia, quindi, non aveva l'obiettivo di essere inespugnabile per sempre. Come nessun sistema è cyber sicuro, "come spero di avervi trasmesso in questo corso che oggi finisce", nessun algoritmo crittografico, almeno classico, è imbattibile: tutti sono battibili avendo risorse sufficienti. L'approccio difensivo di chi adotta la crittografia per presidiare la riservatezza (come con Enigma) e, come si vedrà nel corso successivo, anche integrità, autenticità e forse privacy, è **portare l'asticella dei difensori un po' sopra la testa degli avversari**. L'attore della minaccia potrà in astratto rompere la crittografia, ottenere un dato riservato, modificare un dato integro o cambiarne l'origine, ma solo con un enorme dispendio di tempo, denaro e tecnologia, tanto che il vantaggio ottenuto non gli conviene più e, in termini d'impresa, "non investe".
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezione 12 (storia della crittografia)*
- **Scitala spiegata nel dettaglio.** Bastoni poligonali prodotti in coppie identiche; si avvolgeva una striscia di cuoio, si scriveva il messaggio su un solo lato e lettere casuali sugli altri; solo il destinatario con lo scitala gemello lo ricostruiva. Gli scitali in coppia sono l'analogo della chiave. Messaggi di pochi caratteri (una città, una sigla di strategia). (Teams 7 @ 0:08:21 - 0:10:03)
- **Disco di Festo.** Ipotesi più probabile secondo il docente: un abecedario per imparare una scrittura sillabica o ideografica di Creta del II millennio a.C., oppure un gioco dell'oca. Nel 2025 diceva solo che non è un oggetto crittografico. (Teams 7 @ 0:10:03 - 0:11:08)
- **Dal dispositivo alla chiave.** Nuovo passaggio logico: lo scitala poteva essere usato da chiunque lo trovasse; i congegni a orologeria medievali richiedevano una combinazione (la chiave), quindi restavano inutilizzabili anche se catturati. La robustezza dipendeva da quanto era complicato provare tutte le combinazioni in tempo umano. (Teams 7 @ 0:11:39 - 0:14:14)
- **Cifrari polialfabetici e congiure.** Citazione del complotto contro la regina Elisabetta, sventato decifrando il cifrario dei congiurati (vedi "Divergenze" sul nome). (Teams 7 @ 0:14:31 - 0:15:22)
- **Enigma, dettagli nuovi.** Versione militare trasportabile in valigetta; tentativo iniziale dell'intelligence polacca, poi gli inglesi con molti operatori e operatrici in parallelo; i nazisti cambiavano codice ogni giorno; la macchina dava il risultato a mezzogiorno del giorno dopo. Un'intuizione (secondo il docente, le prime lettere indicavano la sigla dell'operatore) semplificò il problema. Nuovo collegamento con la cyber intelligence: un'informazione decifrata troppo tardi è "intelligence non azionabile, non tempestiva". (Teams 7 @ 0:15:59 - 0:19:37)
- **One-time pad citato dal docente.** Nel 2025 era una nota aggiunta; ora il docente dice che una crittografia mai rompibile esiste in teoria (one-time pad) ma è praticamente inutilizzabile; quella utilizzabile è sempre rompibile con potenza di calcolo illimitata. (Teams 7 @ 0:20:47 - 0:21:12)
## 13. Robustezza e cripto-agilità
*CS-08 @ 00:51:36*
**Slide "Crypto-agility"** (*CS-08 @ 00:51:58*, poi con testo a *00:52:58*). Immagini: una carta *Visa Classic Credit*, una *STUDENT CARD* (Ben Manly, Student # 8123-42, 2018-2019), una smartcard *tivùsat 4K ULTRA HD* con modulo *CAM 4K ULTRA HD tivùsat*, due finestre "Sicurezza di Windows" (*Smart card: Immettere il PIN di autenticazione*; *Smart card: Selezionare un dispositivo smart card, Connettere una smart card, Alcor Micro USB Smart Card Reader 0*), e un facsimile di **Carta d'Identità Elettronica** italiana (Repubblica Italiana, Ministero dell'Interno, scritta FAC-SIMILE). Testo:
> Crypto-agility is the capability to enact technical, organisational and physical (e.g. logistics) procedures to migrate towards different cryptographic algorithms, on time before they are no longer considered robust.
>
> Quantum computing is a "*doubly*" convincing argument towards reaching crypto-agility, because:
> - current encryption, hashing and signing algorithms shall be broken by next-generation quantum computers; \[riga tagliata in basso nel frame, parzialmente leggibile; il seguito è illeggibile\]
Poiché la crittografia moderna si basa su algoritmi eseguiti da computer sofisticati, e computer sofisticati sono usati anche per romperla, è essenziale parlare di **cripto-agilità**: una **capacità organizzativa** che consiste nel disporre di tecnologia, caratteristiche fisiche, procedure logistiche e organizzative per **migrare** gli algoritmi crittografici usati, abbandonando quelli via via considerati non più sufficientemente robusti verso algoritmi più forti, capaci di resistere all'attore della minaccia.
È un problema "del gatto e del topo": nel tempo l'attore della minaccia acquisirà tecnologie e risorse più economiche per rompere la crittografia, cioè "diventerà più alto". La cripto-agilità permette all'organizzazione di prevederlo e di **spostare l'asticella più in alto** in tempo: quando l'attore sarebbe in grado di saltarla, l'organizzazione è già migrata a un algoritmo più robusto che la nuova tecnologia dell'avversario non può battere, e i dati restano al sicuro. Degli attacchi alla crittografia si parlerà nel corso successivo.
> **Nota aggiunta:** la frase della slide va presa con cautela per gli **hash**: l'algoritmo di Grover dà solo un vantaggio quadratico, per cui funzioni di hash con output sufficientemente lungo (per esempio SHA-256, SHA-384) non sono considerate "rotte" dal calcolo quantistico; lo stesso vale per la cifratura simmetrica con chiavi lunghe (AES-256). A rischio sono soprattutto gli algoritmi **a chiave pubblica** attuali (RSA, curve ellittiche), vulnerabili all'algoritmo di Shor. Il "doppiamente" della slide si riferisce plausibilmente anche al rischio *harvest now, decrypt later*, ma il seguito è illeggibile.
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezione 13 (robustezza e cripto-agilità)*
- **L'attaccante aggira, non rompe (argomento nuovo).** Oggi gli attori raramente provano a rompere un algoritmo quando sanno che è antieconomico: sfruttano vulnerabilità del software, falle di processo nello schema crittografico, costringono due sistemi a **negoziare un algoritmo più debole** o una chiave più corta, oppure trovano la chiave "a monte". Il docente dice di farlo anche lui di mestiere. La prima difesa resta usare algoritmi robusti. (Teams 7 @ 0:21:55 - 0:23:54)
- **Smart card e PIN.** Esempi: carte di pagamento, smart card per la TV via cavo o satellitare, CIE e passaporto elettronico. Il PIN verifica che la carta sia in mano al titolare; esistono smart card con lettore d'impronta integrato o che usano il lettore del POS (rinvio al corso DITS per la firma digitale sottostante). (Teams 7 @ 0:24:06 - 0:25:47)
- **Chip poveri di risorse.** Le carte contactless sono alimentate dal campo elettromagnetico del lettore per pochi secondi; ogni bit in più costa potenza e tempo. (Teams 7 @ 0:26:46 - 0:27:50)
- **Perché le carte scadono (argomento nuovo e centrale).** Oltre ai motivi finanziari e amministrativi c'è un motivo crittografico: l'emittente ha la certezza che dopo la scadenza dell'ultima carta emessa con il vecchio algoritmo non ne circolino più. Quando la valutazione del rischio indica che la rottura futura dell'algoritmo diventa probabile, l'emittente progetta un chip più robusto e inizia a emettere carte nuove; la finestra di rischio si chiude alla scadenza dell'**ultima** carta vecchia, non alla data della decisione. Servono anche logistica e sostituzione di lettori, tornelli aeroportuali, POS. (Teams 7 @ 0:28:07 - 0:31:20)
- **Cripto-agilità come capacità organizzativa.** Ribadita con un esempio concreto: posso aver scelto un algoritmo resistente agli attacchi quantistici, ma quanti produttori mi forniscono una smart card personalizzabile a un costo accettabile? Le carte di pagamento sono gratuite per il cliente, i documenti d'identità hanno un contributo che copre in parte il costo di produzione. Rinvio al corso DITS per la crittografia post-quantistica. (Teams 7 @ 0:31:35 - 0:33:51)
- **Asticella né troppo bassa né troppo alta (nuovo).** Un algoritmo molto più robusto del necessario significa spendere troppo: una smart card post-quantum "più robusta al mondo" oggi costerebbe centinaia o migliaia di euro e ucciderebbe il caso d'uso. Approccio basato sul rischio: asticella un po' sopra la testa dell'attaccante, abbastanza da lasciare tempo alla cripto-agilità. Collegamento con l'esempio della cassaforte dell'inizio del corso (riservatezza a scapito di integrità e disponibilità). (Teams 7 @ 0:33:59 - 0:36:49)
## 14. Crittologia, crittoanalisi e security through obscurity
*CS-08 @ 00:53:47*
**Slide di sezione "Cryptology & Crypto-analysis"** (*CS-08 @ 00:53:50*, verificata a *00:59:33*). Sfondo con un lucchetto digitale e un toro (la curva ellittica come superficie). In alto a sinistra la struttura di una chiave privata EC in PEM/DER, con un dump esadecimale (inizio `30 74`, poi `02 01 01`, `04 20 …`) e la sua decodifica ASN.1:
```javascript
119 Bytes [ECPrivateKey]
  1 Byte [ecPrivkeyVer1] 01
  32 Bytes [privateKey]   8.43[...] e75
  10 Bytes [ 0 ] (ECDomainParameters)
     8 Bytes [secp256k1]
        1.3.132.0.10
  68 Bytes [ 1 ] (Key Data)
     66 Bytes [publicKey]
        { 8.79[...] e76,
          7.78[...] e76 }
```
Legenda *ASN.1 Types*: 02 xx Integer; 03 xx Bit String; 04 xx Octet String; 06 xx OID; 30 xx Sequence.
> **Nota aggiunta (verifica con Python):** generando in Python (libreria `cryptography`) una chiave secp256k1 in formato ECPrivateKey DER si ottengono **118 byte** con intestazione `30 74`, come nel dump a schermo: versione 3 byte, chiave privata 34 byte (32 di valore), parametri `[0]` 9 byte, chiave pubblica `[1]` 70 byte (BIT STRING di 66 byte con il punto non compresso di 65 byte). Le etichette della slide ("119 Bytes", "10 Bytes", "8 Bytes") non coincidono con il dump (differiscono di un byte o contano solo il contenuto); l'OID 1.3.132.0.10 di secp256k1 è corretto. Da notare: la chiave **pubblica** (65 byte) è più lunga della **privata** (32 byte), il che smentisce l'analogia del docente nella sezione 17.
Le due branche della crittografia teorica sono, secondo il docente, la **crittologia**, cioè lo studio degli algoritmi crittografici per individuarne di nuovi e verificarne la robustezza, e la **crittoanalisi**, la branca che prova a **rompere** la crittografia, "se vogliamo, l'analogo del red team": rompere un algoritmo senza conoscere la chiave oppure arrivare a conoscere la chiave quando inizialmente non la si conosce.
> **Correzione:** nella terminologia standard la **crittologia** è la disciplina complessiva, che comprende la **crittografia** (progettazione degli algoritmi) e la **crittoanalisi** (attacco agli algoritmi). Il docente usa "crittologia" per quella che di solito si chiama crittografia; il titolo della slide ("Cryptology & Crypto-analysis") non chiarisce.
### Algoritmi segreti contro algoritmi pubblici
*CS-08 @ 00:55:01*
Il docente va "a braccio", senza slide. La crittografia può basare parte della robustezza sulla **segretezza dell'algoritmo**. Molte soluzioni commerciali, ancora oggi ma soprattutto in passato ("oggi si è capito l'errore, si cerca di non ripeterlo"), si basano sul fatto che l'algoritmo non sia noto: di nuovo **security through obscurity**. "Non ti dico come ho cifrato il dato": l'avversario ha davanti il testo cifrato ma non conosce neanche l'algoritmo, e parte in forte svantaggio. Molti prodotti, soprattutto hardware ma anche software, magari brevettati, funzionano così: non si sa che cosa faccia quel codice o quel dispositivo, si sa solo che si inseriscono dati ed escono cifrati. Spesso queste soluzioni di mercato pubblicizzano, soprattutto a chi non ha le basi scientifiche per valutarlo, che la robustezza deriva dall'essere un algoritmo "supersegreto".
È stato però dimostrato più volte che l'efficacia degli algoritmi crittografici si basa su una politica che ha un analogo nella cyber security, la **responsible disclosure** (anticipato nella lezione dedicata). Esempio del docente: un'azienda di prodotti di sicurezza ha un team di crittologi e crittoanalisti di primissimo livello, pagati profumatamente da anni, che testano l'algoritmo ogni giorno e garantiscono che è super sicuro. Ma:
- per quanto bravi, numerosi e pagati, **non valgono quanto l'intera comunità scientifica mondiale** messa insieme;
- lavorando sempre per la stessa azienda che paga loro lo stipendio possono avere **bias**: dopo anni smettono di pensare come un vero attaccante e possono non notare una vulnerabilità che diventa sempre più evidente a un occhio neutro e disincantato;
- dopo tanti anni potrebbero **non voler trovare** una vulnerabilità, perché rischierebbero il posto.
Motivi "più o meno stupidi, più o meno oggettivi", molti dei quali sono accaduti: ci sono stati disastri quando gli attori della minaccia hanno dimostrato di poter rompere un algoritmo molto più facilmente del previsto. La conclusione: gli algoritmi più robusti sono quelli sottoposti, prima di essere adottati e tanto più prima di essere venduti, a una **peer review** della comunità scientifica che può durare anni o decenni ma che, essendo l'algoritmo pubblico, consente a chiunque di testarlo in tutti i contesti possibili, molti più di quelli che potrebbe coprire la sola organizzazione. Esempio: chi fa sistemi operativi testa l'algoritmo al proprio interno, ma il sistema operativo viene poi installato su macchine in settori con scenari di minaccia specifici che né i crittologi della ditta né l'amministratore delegato avevano previsto, e si scopre che in un uso molto particolare l'algoritmo non è robusto. Un algoritmo valutato per anni da un'intera comunità scientifica non è "la verità assoluta", ma tipicamente dura e viene usato molto più a lungo, perché ci sono prove inconfutabili della sua robustezza.
> **Nota aggiunta:** è il **principio di Kerckhoffs** (1883): un sistema crittografico deve restare sicuro anche se tutto, tranne la chiave, è pubblico. Il docente non lo nomina.
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezione 14 (algoritmi segreti contro algoritmi pubblici)*
- **Argomento a favore del segreto, esposto meglio.** Chi sostiene gli algoritmi segreti invoca la difesa a strati del castello: l'attaccante deve prima capire l'algoritmo. Protezioni fisiche: chip annegati in **resina epossidica** anti-tamper, che blocca le radiografie e distrugge il chip se lo si seziona; server in gabbie inaccessibili nei data center. (Teams 7 @ 1:01:12 - 1:03:35)
- **Canali laterali (nuovo).** Anche senza aprire il chip, si può capire come funziona per grandi linee osservando quali cicli consumano più potenza o scaldano di più una parte della CPU. (Teams 7 @ 1:03:51 - 1:04:26)
- **Peer review e interessi commerciali.** Nuovi dettagli: prima che il NIST raccomandi un algoritmo passano anche uno o due decenni di test della comunità; un'azienda che trova una falla insanabile dopo 12 anni non butta tutto, al più studia tre o quattro algoritmi in parallelo; chi lo ha analizzato senza firmare un accordo di riservatezza (NDA) è "praticamente nessuno". (Teams 7 @ 1:04:26 - 1:07:02)
## 15. Riservatezza: la cifratura
*CS-08 @ 00:59:59*
**Slide "Confidentiality – Encryption"** (costruita progressivamente: *CS-08 @ 00:53:59* per un istante e poi *00:59:57* con il solo *plaintext*; *01:00:57* con la *key pair*, una chiave arancione e una verde; completa a *01:02:57*, testo del diagramma da OCR). Diagramma: *plaintext* → **Encryption** → *cipher-text* (`A4$h*L@9. T6=#/>B#1 R06/J2.>1L 1PRL39P20`) → **Decryption** → *plaintext*, con la *key pair* che alimenta le due operazioni. Testo in basso, verificato visivamente: "Encryption via a robust algorithm means that it is **computationally hard** for adversaries who know the cipher-text alone to derive either the plaintext or the key to decrypt the cipher-text."
Il docente introduce un po' di tassonomia, "per concludere oggi". Quando si usa la crittografia per la **riservatezza**, come in tutti gli esempi storici dall'antichità alla seconda guerra mondiale, si parla di presidi di riservatezza, e il principale è la **cifratura**. Si basa su un algoritmo che deve rendere **computazionalmente difficile** per gli avversari ottenere il dato in chiaro conoscendo solo il dato cifrato.
La cifratura è una funzione matematica che trasforma un dato in chiaro, **plaintext**, in un dato cifrato, **ciphertext**, usando una chiave (quella rossa in figura), detta **chiave di cifratura**. Una chiave verde, **matematicamente legata** alla rossa, detta **chiave di decifratura**, serve per riottenere il testo in chiaro dal testo cifrato.
L'algoritmo è **robusto** quando:
- dalla chiave usata per cifrare non è facile derivare quella per decifrare: l'avversario che venga in possesso di una delle due chiavi non deve poter derivare la seconda, almeno nei casi in cui sono distinte;
- l'avversario che conosca anche l'**algoritmo** (bisogna presupporre che sia pubblico) e il **testo in chiaro**, senza la chiave, non possa risalire né alla chiave di decifratura né a decifrare il testo.
Matematicamente è sempre possibile per l'avversario ottenere la chiave o il testo in chiaro; deve però risultargli **antieconomico**. Nel gergo tecnico: **computazionalmente difficile**. Non significa matematicamente impossibile: significa che per un dato avversario sarebbe troppo oneroso, perché dovrebbe mettere in piedi un supercomputer che probabilmente non può permettersi, oppure lavorare con quello che ha impiegando così tanto tempo che il dato decifrato non avrebbe più valore.
> **Nota aggiunta:** la slide definisce la robustezza rispetto a un avversario che conosce **solo il testo cifrato** (*ciphertext-only*); il docente la estende a un avversario che conosce anche l'algoritmo e il testo in chiaro (*known-plaintext*), che è un requisito più forte e quello effettivamente richiesto agli algoritmi moderni.
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezioni 15 e 16 (cifratura, chiave simmetrica)*
- Contenuto ripetuto, con una formulazione esplicita: la chiave di cifratura e di decifratura possono essere uguali (cifrari simmetrici) o diverse; nel simmetrico la sicurezza sta nel fatto che K_sym sia nota solo a mittente e destinatario. Il docente dice che si dilungherà meno sul simmetrico perché gli studenti lo vedono in un altro corso di crittografia. (Teams 7 @ 0:00:23, 0:59:30 - 1:00:48)
## 16. Crittografia simmetrica
*CS-08 @ 01:03:16*
**Slide "Symmetric cryptography"** (*CS-08 @ 01:04:57*). Diagramma: una sola chiave, *(one) symmetric key*, che alimenta sia *Encryption* sia *Decryption* (etichette K\^sym su entrambi i rami); *plaintext* → *cipher-text* → *plaintext*. Testo:
> Digital analogue to previous-eras' cryptography, symmetric cryptography relies on *one* key represented as a *k*-bits string (roughly speaking, a usually very large number in a **key-space** of cardinality 2\^k), which is hard to guess and which is used for *both* encryption of the plaintext and decryption of its cipher-text.
>
> Common "classic" ciphers are: AES, Blowfish, DES/3DES, RC4, Serpent, SM4, Twofish.
Gli algoritmi crittografici si distinguono in due grandi famiglie. Negli algoritmi **simmetrici** le chiavi di cifratura e decifratura sono **la stessa chiave**, detta **chiave simmetrica**. Il docente cita **Blowfish**, "una vecchia variante usata nelle vecchie versioni del protocollo Bluetooth", e soprattutto **AES** (*Advanced Encryption Standard*), oggi lo standard universale fra gli algoritmi simmetrici classici, "che in realtà è a sua volta un insieme di algoritmi".
> **Correzione:** Blowfish (Schneier, 1993) non è stato usato nel Bluetooth. Il Bluetooth classico (BR/EDR) usava il cifrario a flusso **E0** per la cifratura e **SAFER+** per autenticazione e generazione delle chiavi; dal Secure Connections e nel Bluetooth Low Energy si usa **AES-CCM**.
> **Nota aggiunta:** "insieme di algoritmi" si riferisce alle tre varianti di AES (AES-128, AES-192, AES-256), sottoinsieme del cifrario Rijndael con blocco fisso di 128 bit e chiave di 128, 192 o 256 bit.
### Il problema della distribuzione della chiave
*CS-08 @ 01:03:56*
Poiché la chiave simmetrica serve sia a cifrare sia a decifrare, deve essere **condivisa** fra chi deve ricevere il dato. Se è sufficientemente robusta, la crittografia simmetrica porta con sé il fondamentale **problema della distribuzione della chiave**: se **Alice** deve inviare un dato cifrato a **Bob** con un algoritmo simmetrico, Alice e Bob devono aver condiviso una chiave che hanno solo loro; Alice la userà per cifrare e Bob per decifrare.
### Password e funzioni di derivazione della chiave
*CS-08 @ 01:04:26*
L'esempio più semplice, ad alto livello, di chiave simmetrica è una **password**. In realtà, quando si digita una password per cifrare qualcosa, la chiave non è direttamente la password: è tipicamente un numero molto più grande, **derivato in modo deterministico** dalla password con una **funzione di derivazione della chiave** (KDF). Secondo il docente, anche con una password semplice non è detto che la chiave associata sia altrettanto semplice; anzi, le KDF servono proprio a mitigare il rischio che una password semplice produca una chiave debole, che l'attore della minaccia potrebbe derivare.
> **Correzione (precisazione):** una KDF non aumenta l'**entropia**: la chiave derivata ha l'aspetto di un numero grande e casuale, ma se la password è debole un attaccante può provare le password probabili (attacco a dizionario) e ricalcolare la chiave. Le KDF per password (PBKDF2, bcrypt, scrypt, Argon2) mitigano il rischio **rallentando** ogni tentativo (*key stretching*, con molte iterazioni o molta memoria) e impedendo calcoli precomputati grazie al **salt**; non rendono sicura una password debole.
## 17. Crittografia a chiave pubblica
*CS-08 @ 01:05:39*
**Slide "Public-key cryptography"** (*CS-08 @ 01:05:39*). A sinistra: "With asymmetric cryptography, decryption must be accomplished with the opposite key of the key-pair that was used for the encryption of a plaintext." Al centro l'*asymmetric key pair* (chiave arancione e verde): sul ramo di cifratura K\^priv *or* K\^pub, sul ramo di decifratura K\^pub *or* K\^priv; *plaintext* → *Encryption* → *cipher-text* → *Decryption* → *plaintext*. In alto a destra un riquadro **Alice**: *Large random number* → *Key generation program* → chiave verde *Public* e chiave rossa *Private*. In basso:
> It relies on solving number-theoretical / algebro-geometric problems, relatively easy to compute one way, yet computationally difficult to invert. Different algorithms follow radical approaches in key-pair definition. When **public** \[**private**\] is used for encryption, the private \[public\] key **must** be used for decryption.
>
> "Classic" ciphers are: **RSA**; **ECDSA**, **ECDH**, EdDSA (elliptic curve cryptography), ElGamal, DSS/DSA, Paillier.
"Ed è questa l'ultima slide per oggi." Opposti ai simmetrici ci sono gli algoritmi **asimmetrici**, detti anche, "proprio per non dover sottolineare tutte le volte la A privativa", algoritmi **a chiave pubblica**. Le due chiavi di cifratura e decifratura sono **diverse** ma **matematicamente legate**: una è la **chiave pubblica**, l'altra la **chiave privata**. Hanno due caratteristiche.
1. **Chiavi opposte.** Se si cifra con una delle due (per esempio la privata), per come sono definiti matematicamente questi algoritmi la decifratura va fatta necessariamente con l'altra (la pubblica), e viceversa. Se si cifra con la privata e si prova a decifrare con la stessa privata "non ottengo nulla, certamente non riottengo il plain text".
2. **Legame univoco.** Per ogni chiave pubblica esiste una sola chiave privata che le si accoppia, e viceversa.
Ciò che distingue la chiave pubblica dalla privata non è quale si usa per cifrare e quale per decifrare (argomento del corso successivo). Il docente invita a ragionare, in preparazione del corso successivo, su questa definizione: si chiama **chiave privata quella usata per derivare la chiave pubblica**. Quando si chiede a un software di generare una coppia di chiavi, il software o l'hardware genera una chiave privata, un numero molto, molto grande, estratto casualmente; da essa, con un processo matematico **deterministico**, si deriva **facilmente** la chiave pubblica. L'operazione inversa è **computazionalmente difficile**, cioè "praticamente impossibile se l'algoritmo è robusto": è la caratteristica che definisce gli algoritmi a chiave pubblica.
> **Nota aggiunta:** la proprietà "si cifra con una chiave e si decifra con l'altra, in entrambi i versi" vale per **RSA**, non per tutti gli algoritmi della lista. **ECDSA**, **EdDSA** e **DSS/DSA** sono schemi di **firma digitale** (non cifrano), **ECDH** è un protocollo di **accordo di chiave**; ElGamal e Paillier cifrano solo con la chiave pubblica. Per questo, in generale, "cifrare con la chiave privata" va inteso come **firmare**, e le due operazioni sono distinte in molti schemi. Il docente rimanda al corso successivo proprio la distinzione fra i due usi.
### L'analogia del doblone
*CS-08 @ 01:07:52*
**Slide "Public-key cryptography"**, seconda versione (*CS-08 @ 01:08:39*). A sinistra: "Private and public keys can be thought of as very large numbers (whose length is measured in bits): from the **private key** the **public key** can be easily derived; From the **public key** it's computationally hard (i.e. practically impossible) to derive the **private key**." Al centro una moneta con un monogramma (una lettera B intrecciata) e decorazioni: una porzione a sinistra, minore della metà, è in colore pieno; il resto è sbiadito. Ai lati la chiave verde *Public* (sinistra) e la chiave rossa *Private* (destra). Restano il riquadro Alice e il testo in basso della versione precedente.
L'analogia del docente: immaginiamo una moneta, un **doblone**. La chiave privata rappresenta una fetta **maggiore della metà**: "la chiave privata è molto più grande". Dalla privata, una volta generata ("inventata, estratta casualmente"), si deriva facilmente la pubblica; l'inverso è computazionalmente difficile. La chiave pubblica rappresenta invece una porzione **minore della metà**. Se si ha solo la parte sinistra, meno della metà, non si può ricostruire il doblone, perché manca la simmetria completa: graficamente servirebbe almeno metà doblone per dire "lo copio uguale a se stesso". E siccome al centro c'è una **lettera B**, che non è simmetrica, anche con metà doblone non si riuscirebbe a ricostruirlo tutto. Se invece si disponesse della porzione corrispondente alla chiave privata, con un semplice processo intellettivo, o anche con un'intelligenza artificiale molto semplice, si saprebbe ricostruire l'intero doblone.
> **Correzione:** l'analogia va intesa solo sul piano dell'**informazione** (dalla privata si ricava la pubblica, non il contrario), non della **dimensione**. Non è vero in generale che la chiave privata sia "molto più grande" della pubblica: nelle curve ellittiche la privata è un intero di 256 bit e la pubblica un punto di 512 bit (65 byte non compressa), come mostra la slide "Cryptology & Crypto-analysis" della stessa lezione (32 byte contro 66); in RSA le due chiavi condividono lo stesso modulo e hanno dimensioni comparabili. Inoltre il passaggio sulla lettera B è ambiguo nel parlato: sembra riferirsi alla metà pubblica, ma detto così vale per qualunque metà.
"Questa è l'analogia con la quale mi sento di lasciarvi in preparazione del prossimo corso", dove di chiavi pubbliche e private si parlerà in modo molto approfondito. Il docente chiude chiedendo se ci sono domande (*CS-08 @ 01:09:42*); la registrazione termina subito dopo, senza domande trascritte.
---
### Integrazione Teams 2026 (lezione 7 2026)
*Capitolo 07, sezione 17 (chiave pubblica e privata)*
- **Definizione confermata.** Dalla privata si ricava facilmente la pubblica con una funzione nota; l'inverso è computazionalmente difficile. Le chiavi sono grandi numeri o insiemi di numeri; data una chiave, l'altra esiste ed è unica. (Teams 7 @ 1:07:40 - 1:10:46)
- **Nuova analogia: la moneta da 1 euro.** Sostituisce il doblone con la lettera B. Se si dà a un'IA la parte di moneta che contiene gli elementi asimmetrici (la "privata") e le si chiede di completarla, ci riesce; se le si danno solo le due "manine" e le stelle (la "pubblica"), non può ricostruire la figura centrale (l'opera di Leonardo) se non è addestrata sulle monete vere. Resta un'analogia sull'informazione, non sulla dimensione delle chiavi (vedi la correzione già nel manuale 2025). (Teams 7 @ 1:08:32 - 1:10:31)
- **Terminologia.** Preferisce "a chiave pubblica" ad "asimmetrica" perché nella registrazione l'alfa privativo potrebbe non sentirsi (motivazione analoga al 2025). (Teams 7 @ 1:10:55 - 1:11:11)
### Integrazione Teams 2026 (lezione 7 2026)
*Funzioni di hash crittografico (Teams 7 @ 0:37:12 - 0:50:28)*
- **Scelta didattica:** invece di partire dalla riservatezza, come fanno i testi, parte da **integrità** e autenticità, per mostrare che la crittografia non serve solo a nascondere. (0:37:12)
- **Definizione:** funzione che mappa un messaggio di lunghezza finita arbitraria in una stringa di **h bit** costante (lunghezza dell'impronta). L'output si chiama **digest**, ma nel gergo si dice "hash" anche per l'output. Formalismo matematico mostrato in slide ma non commentato ("non è questo l'oggetto del corso"). (0:38:00 - 0:40:02)
- **Proprietà elencate dal docente:**
	1. output di lunghezza costante;
	2. cambiando anche un solo bit dell'input il digest cambia radicalmente (effetto valanga);
	3. dato un digest è computazionalmente difficile trovare un messaggio che lo produce (resistenza alla preimmagine);
	4. dato un messaggio è computazionalmente difficile trovarne un secondo con lo stesso digest (resistenza alla seconda preimmagine / alle collisioni). (0:40:20 - 0:42:11)
- **Collisioni:** esistono sempre, perché la funzione non è iniettiva (infinite controimmagini); la robustezza consiste nel rendere antieconomico trovarle. Se un attaccante trova una collisione, l'impronta non prova più che il dato è integro. Più bit di output, codominio più grande, più difficoltà. Tabella in slide con h = 32, 64, 160 bit e le relative probabilità, riferita a versioni di SHA ormai deprecate. (0:42:11 - 0:44:57, 0:49:21)
- **Laboratorio CyberChef:** strumento online sviluppato dal GCHQ britannico, funziona lato client nel browser, installabile anche in locale, codice sorgente scaricabile. Dimostrazione con SHA-2 a 256 bit: cambiando "i" in "j" l'impronta cambia completamente. Da terminale Linux o macOS esistono comandi equivalenti (il docente cita `md5sum`). Il docente invita a rifare l'esercizio a casa, ma precisa: "non a me interessa che sappiate usare CyberChef", interessa poter replicare i concetti. (0:45:14 - 0:50:28)
- **Password memorizzate come hash.** Il server non deve conoscere la password in chiaro (esempio della pizzeria online che potrebbe ordinare pizze a nome del cliente). Secondo il docente il client calcola l'impronta, cancella la password dalla memoria e invia solo l'impronta; il server la confronta con quelle memorizzate. Vedi "Divergenze". (0:50:28 - 0:52:22)
- **Rischio del riuso delle password.** Un attaccante che viola un servizio poco protetto (la piccola pizzeria artigianale) ottiene email e hash; se lo stesso hash compare in un altro servizio sa che la password è riusata e può tentare l'accesso al PC di lavoro, alla posta, alla banca. (0:52:25 - 0:54:20)
- **Il sale.** A ogni creazione di password si genera un numero usato una sola volta (il docente lo chiama *nonce*), memorizzato **in chiaro** sul server insieme all'hash calcolato su nonce concatenato alla password. Non semplifica la forza bruta, ma la stessa password su due servizi produce hash diversi: chi compra nel dark web due archivi di password rubate non può dedurre il riuso. Aumenta il costo per l'attaccante e migliora la postura di sicurezza. Consiglio esplicito: non riusare password tipo "Walter123". (0:54:36 - 0:58:13)
### Integrazione Teams 2026 (lezione 7 2026)
*RSA (Teams 7 @ 1:11:33 - 1:19:18)*
- Scelto come esempio perché è il più semplice e tra i più usati fra gli algoritmi non quantum-safe. Inventato da Rivest, Shamir, Adleman alla fine degli anni '70; poco implementato negli anni '80 per mancanza di potenza di calcolo, poi diffuso negli anni '90, 2000 e 2010.
- Spiegazione del docente: la chiave pubblica è il prodotto di due numeri primi molto grandi e comparabili; la privata è uno dei due fattori; trovato un fattore, l'altro si ottiene per divisione. Richiamo della scomposizione in fattori primi (6 = 3×2, 22 = 11×2, 33 = 11×3). Sapere che i fattori sono solo due semplifica la crittoanalisi, ma con numeri così grandi la fattorizzazione resta computazionalmente impossibile. Vedi "Divergenze" per la precisazione sulla struttura reale delle chiavi RSA.
- **Notizia settembre 2026:** secondo il docente, pochi giorni prima era uscita la notizia della fattorizzazione di un numero della sfida RSA, con premio riscosso, ma con poche centinaia di bit: lontano da RSA-1024, già deprecato da anni. Oggi si usa almeno RSA-2048, anche 4096, e si pensa di deprecare il 2048 nei prossimi anni. Vedi "Punti incerti".
- **Allungare la chiave o cambiare algoritmo?** In software allungare la chiave costa solo tempo di calcolo, e cambiare algoritmo è facile se la libreria lo supporta. Su una smart card raddoppiare i bit significa riprogettare il chip: più consumo, più lentezza, più costo. Può convenire passare a un algoritmo diverso che lavora con lo stesso numero di bit, per esempio da RSA alle curve ellittiche. Il docente dice di essersi occupato in passato di questa progettazione. (1:17:31 - 1:19:18)
### Integrazione Teams 2026 (lezione 7 2026)
*Crittografia a curve ellittiche (Teams 7 @ 1:19:25 - 1:29:03)*
- Non è un solo algoritmo ma una famiglia; non tutte le curve sono adatte, come non tutti i primi sono adatti a RSA (devono poter essere generati casualmente senza che due utenti ottengano le stesse chiavi).
- Il docente precisa che non è un corso di matematica e che non è un crittoanalista di professione, pur essendosi occupato di curve ellittiche.
- Curva ellittica come luogo delle soluzioni di un polinomio di terzo grado in due variabili con coefficienti interi, considerato **modulo p** (p tipicamente primo); le soluzioni discrete si rappresentano come punti. Le curve con buone proprietà vengono parametrizzate e ricevono un nome: `secp256r1`, `secp256k1` e simili, con coefficienti e modulo pubblicati in tabelle standard.
- Problema matematico diverso da RSA: invece della fattorizzazione, il **logaritmo discreto**. L'esponenziale modulare è facile da calcolare, l'inverso è computazionalmente complesso.
- **Confronto con RSA:** a parità di robustezza le chiavi a curve ellittiche sono molto più corte. Il docente cita RSA-2048 ≈ ECC-256 e RSA-4096 ≈ ECC-512 (vedi "Divergenze").
- **Criterio di scelta:** RSA dove i dispositivi lavorano bene con molti bit e conviene una matematica più semplice; curve ellittiche dove lavorare con pochi bit è essenziale per efficienza e costo, accettando un'algebra più complessa. Considerazioni quantistiche rinviate al corso successivo. (1:28:08 - 1:29:03)
## 18. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato nella lezione</td>
</tr>
<tr>
<td>TTP</td>
<td>Tattiche, tecniche e procedure usate in un attacco reale o simulato</td>
</tr>
<tr>
<td>Analisi strutturata</td>
<td>Descrizione di un attacco con un modello o framework condiviso (ATT&CK, kill chain, Diamond)</td>
</tr>
<tr>
<td>MITRE ATT&CK</td>
<td>Framework di tattiche, tecniche e sotto-tecniche con bibliografia degli attori noti</td>
</tr>
<tr>
<td>ATT&CK Navigator</td>
<td>Applicazione web per costruire e visualizzare catene di compromissione sulla matrice</td>
</tr>
<tr>
<td>Kill chain</td>
<td>Catena lineare di fasi di un attacco; basta interrompere un anello</td>
</tr>
<tr>
<td>Cyber Kill Chain®</td>
<td>Sette fasi: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives</td>
</tr>
<tr>
<td>Weaponization</td>
<td>Preparazione dell'arma (payload, infrastruttura C2) fuori dal perimetro</td>
</tr>
<tr>
<td>Persistenza (installation)</td>
<td>Restare nel sistema anche dopo riavvii o rimozioni</td>
</tr>
<tr>
<td>C2 (Command and Control)</td>
<td>Canale con cui l'attaccante comanda il malware dall'esterno</td>
</tr>
<tr>
<td>Unified Kill Chain</td>
<td>Tre macrofasi cicliche: In, Through, Out</td>
</tr>
<tr>
<td>Crown jewel</td>
<td>I sistemi di reale valore, bersaglio finale dell'attacco</td>
</tr>
<tr>
<td>Diamond Model</td>
<td>Adversary, Infrastructure, Capability, Victim, più meta-feature</td>
</tr>
<tr>
<td>Insider threat</td>
<td>Minaccia proveniente dall'interno dell'organizzazione</td>
</tr>
<tr>
<td>APT</td>
<td>Malware o attore avanzato e persistente, anche autonomo</td>
</tr>
<tr>
<td>OSINT</td>
<td>Intelligence da fonti aperte</td>
</tr>
<tr>
<td>Pyramid of Pain</td>
<td>Gerarchia di indicatori: da hash (facile da cambiare) a TTP (difficile)</td>
</tr>
<tr>
<td>ACH</td>
<td>Analysis of Competing Hypotheses: matrice evidenze/ipotesi</td>
</tr>
<tr>
<td>Matrice CoA</td>
<td>Azioni difensive (detect, deny, disrupt, degrade, deceive, destroy) per fase</td>
</tr>
<tr>
<td>CVE / NVD</td>
<td>Catalogo delle vulnerabilità pubbliche / database NIST che le valuta</td>
</tr>
<tr>
<td>CVSS</td>
<td>Punteggio di gravità di una vulnerabilità (es. 7.5 HIGH)</td>
</tr>
<tr>
<td>VA</td>
<td>Vulnerability assessment, white, gray o black box</td>
</tr>
<tr>
<td>PT</td>
<td>Penetration testing: provare a sfruttare davvero le vulnerabilità</td>
</tr>
<tr>
<td>VAPT</td>
<td>VA seguito da PT, come processo unico</td>
</tr>
<tr>
<td>Red / blue / purple team</td>
<td>Attaccanti simulati / difensori / gruppo di contatto cooperativo</td>
</tr>
<tr>
<td>White team (control team)</td>
<td>Gruppo ristretto che conosce e governa il test</td>
</tr>
<tr>
<td>TLPT</td>
<td>Threat-Led Penetration Testing: red teaming che emula un attore reale guidato da CTI</td>
</tr>
<tr>
<td>Golden teaming</td>
<td>Esercizio tabletop sulla resilienza organizzativa</td>
</tr>
<tr>
<td>DORA</td>
<td>Regolamento UE sulla resilienza operativa digitale del settore finanziario</td>
</tr>
<tr>
<td>BIA / RA / DPIA</td>
<td>Business impact analysis / risk assessment / data protection impact assessment</td>
</tr>
<tr>
<td>Cyber resilience</td>
<td>Capacità di continuare a erogare i risultati attesi nonostante gli attacchi</td>
</tr>
<tr>
<td>Triade del digital trust</td>
<td>Riservatezza, integrità, autenticità</td>
</tr>
<tr>
<td>Autenticità</td>
<td>Garanzia che l'origine del dato sia identificabile</td>
</tr>
<tr>
<td>Non ripudio</td>
<td>Impossibilità per la fonte di negare di aver prodotto il dato</td>
</tr>
<tr>
<td>Digital trust</td>
<td>Autenticità con non ripudio, con valore legale</td>
</tr>
<tr>
<td>Catena di custodia</td>
<td>Garanzia sull'origine e integrità di un reperto digitale</td>
</tr>
<tr>
<td>Security through obscurity</td>
<td>Sicurezza basata sulla segretezza del metodo</td>
</tr>
<tr>
<td>Avversario</td>
<td>Nella letteratura crittografica, l'attore della minaccia</td>
</tr>
<tr>
<td>Robustezza</td>
<td>Rompere l'algoritmo è antieconomico per l'avversario</td>
</tr>
<tr>
<td>Computazionalmente difficile</td>
<td>Possibile in teoria, troppo oneroso in pratica</td>
</tr>
<tr>
<td>Brute force</td>
<td>Ricerca esaustiva di tutte le chiavi</td>
</tr>
<tr>
<td>Cripto-agilità</td>
<td>Capacità di migrare in tempo verso algoritmi più robusti</td>
</tr>
<tr>
<td>Crittoanalisi</td>
<td>Studio di come rompere gli algoritmi crittografici</td>
</tr>
<tr>
<td>Plaintext / ciphertext</td>
<td>Testo in chiaro / testo cifrato</td>
</tr>
<tr>
<td>Chiave simmetrica</td>
<td>Unica chiave per cifrare e decifrare</td>
</tr>
<tr>
<td>Distribuzione della chiave</td>
<td>Problema di condividere la chiave simmetrica in modo sicuro</td>
</tr>
<tr>
<td>KDF</td>
<td>Funzione di derivazione della chiave da una password</td>
</tr>
<tr>
<td>Crittografia a chiave pubblica</td>
<td>Coppia di chiavi diverse e legate; la pubblica si deriva dalla privata</td>
</tr>
</table>
## 19. Punti incerti
- *CS-07 @ 00:00:10*: "oggi sarà più breve la lezione, perché sarà un po' più lunga… però sarà più breve". Frase contraddittoria, riportata com'è.
- *CS-08 @ 00:15:55–00:16:33*: circa 30 secondi senza trascrizione fra l'inizio della descrizione della UKC e la sua ripresa.
- *CS-08 @ 00:22:24*: "individuare le singole vulnerabilità in dei singoli prodotti a ist il cv ad esempio è quel database". Ricostruito come "il CVE, ad esempio, è quel database"; "a ist" potrebbe essere "NIST" (la slide mostra la scheda NVD del NIST). \[?\]
- *CS-08 @ 00:30:17*: "se simulato realmente durante un ora timini". Probabilmente "durante un red teaming". \[?\]
- *CS-08 @ 00:24:34*: "ci sono anche le verifiche che avvengono non a scopo difensivo e proattivo che vengono eseguiti…". Dal contesto il senso è "a scopo difensivo e proattivo" (il "non" sembra spurio o sta per "non solo"). \[?\]
- *CS-08 @ 00:36:18* e *00:35:48*: lapsus del docente, corretti nel testo: "al posto della riserva te della disponibilità" = al posto della disponibilità; "i presidi… a protezione dell'autenticità non sono fatti con i dati" = a protezione della **disponibilità** (il ragionamento riguarda la disponibilità).
- *CS-08 @ 00:36:49*: "la triade della riservatezza, costituita dalla riservatezza, dall'integrità e dall'autenticità". Lapsus per "triade del digital trust" (titolo della slide).
- *CS-08 @ 01:01:05*: la chiave verde è detta "chiave di cifratura" come la rossa; dal contesto è la **chiave di decifratura**.
- *CS-08 @ 01:08:40*: passaggio sulla lettera B non simmetrica ambiguo (vedi Correzione nella sezione 17).
- Slide "The Triad of Information Security" (*00:34:35*): l'OCR legge AUTHENTICITY fra i lati del triangolo anche nella versione con Availability; non verificato visivamente.
- Slide "Crypto-agility": l'elenco puntato dopo "because:" è tagliato nel frame; leggibile solo in parte la prima voce.
- Descrizioni delle fasi 6 e 7 della slide Cyber Kill Chain: non presenti né nei frame né nell'OCR.
- Trascrizione automatica corretta nel testo: "inmitter" = in MITRE; "cyber che il cipre" = cyber kill chain; "l'Attack" = ATT&CK; "sfiltrare/sfiltrazione" = esfiltrare/esfiltrazione; "percora" = percorra; "calarsi la maschera" = togliersi la maschera; "facendo fin da non conoscerci" = facendo finta di non conoscerci; "wifi ROG" = access point Wi-Fi rogue; "DPA" = DPIA; "falli di sicurezza" = falle; "non plastica" = non mastica; "security to obscurity" = security through obscurity; "partita IME" = partita IVA; "polisi" = policy; "rotori autori" = rotori; "brutte forze attacca" = brute force attack; "tossonomia" = tassonomia; "clittografia" = crittografia; "si astrettamente" = in astratto; "criptografio" = crittografico; "si è aggiunti" = si è giunti; "ricompia" = compia; "è ridotto" (00:06:09) = è stato istruito \[?\].
## 20. Esame
In questa lezione il docente non dice nulla sull'esame. Indicazioni utili per pesare lo studio, ma non esplicite sull'esame:
- *CS-08 @ 00:49:59*: il docente dice che il corso "oggi finisce": questa è l'ultima lezione del corso.
- *CS-08 @ 00:31:22*: la business impact analysis "non è oggetto di questo corso".
- *CS-08 @ 00:34:12*, *00:53:47*, *01:09:42*: la crittografia è solo introdotta e sarà approfondita nel corso Digital Identities and Trust Services; la definizione di chiave privata come "quella da cui si deriva la pubblica" è indicata come argomento su cui ragionare "in preparazione per il prossimo corso" (*01:07:22*).
- Le slide Pyramid of Pain, ACH e matrice CoA (*00:22:16–00:22:18*) sono state scorse senza commento.
