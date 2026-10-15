# Assessment

**Modalità, data, formato e consegna dell'esame non sono mai detti** in nessuna registrazione disponibile: né nelle 6 lezioni 2025 del portale (DI-01…DI-06), né nelle 8 lezioni Teams 2026. Sul sito SharePoint del corso non c'è materiale d'esame, solo le registrazioni. Il quadro è identico a quello di Cybersecurity, Cyber Intelligence and Data Privacy, stesso docente, dove l'esame è indicato come congiunto con un altro corso dell'area e "fa fede quello che dico a lezione" (vedi [Assessment di Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/assessment.md)). Che l'esame sia congiunto con Cybersecurity è un'ipotesi: in questo corso il docente non lo dice.

## Tipo di domande

Unica indicazione sullo stile (Teams 8 @ 1:16:53): "**non metto domande nozionistiche in cui dovete ricordare a memoria queste caratteristiche**" (riferito agli attributi SPID/CIE). L'insistenza costante del docente sui passaggi logici fa pensare a domande di comprensione dei concetti, non di memoria.

## Cosa può uscire (indicazioni positive)

| Dove | Indicazione |
|---|---|
| Teams 1 @ 1:02:53 | "All'esame al massimo potrebbe esserci qualche domanda sul **problema concreto alla base della crittografia post quantistica**" ([capitolo 03](03-post-quantum-certificati-e-pki.md), riquadro della sezione 4) |
| Teams 8 @ 1:40:00 | Diagramma EUDI Wallet: "**ci potrebbe essere qualche domanda sui ruoli, quello sì**" (issuer, holder, verifier/relying party, PID provider, fornitori di attestazioni, fonti autentiche, trusted list provider, wallet provider; [capitolo 06](06-identita-digitale-oauth-oidc-eudi-wallet.md)) |

## Esclusioni esplicite

| Edizione | Dove | Escluso |
|---|---|---|
| 2025 | DI-01 @ 00:50:44 | Uso di CyberChef ("non mi fate domande sull'utilizzo di CyberChef"); domande sulle funzioni crittografiche provate restano benvenute |
| 2025 | DI-02 @ 01:47:28 | Slide sull'hardware quantistico: "non guardate le slide, non saranno oggetto d'esame" |
| 2025 | DI-03 @ 00:13:37 | "Non ci saranno domande su questa parte di calcolo e meccanica quantistica" |
| 2026 | Teams 1 @ 1:02:53 | Nessuna domanda di meccanica quantistica né di calcolo quantistico |
| 2025 | DI-04 @ 00:44:27 | "Non ci saranno domande di matematica nel corso" |
| 2025 | DI-04 @ 00:46:12 | Funzionamento di Diffie-Hellman: "a me non interessa che impariate come funziona" |
| 2026 | Teams 8 @ 0:40:46 | Slide SD-JWT: "non ci saranno domande su questa slide" (frase incerta nella trascrizione) |
| 2026 | Teams 8 @ 1:16:53 | Attributi SPID/CIE |
| 2026 | Teams 8 @ 1:39:52 | Frecce e caselle del diagramma EUDI Wallet (sì ai ruoli) |
| 2026 | Teams 6 @ 1:05:29 | IA e identità digitale: rimandate al master di II livello |

## Fuori perimetro o solo di dettaglio (segnali deboli)

Non sono esclusioni dichiarate, ma il docente li presenta come approfondimenti o li salta:
- formule della cifratura omomorfa, "la slide più matematica di tutto il corso, solo per curiosità" (DI-03 @ 00:07:42); cifratura in uso "a scopo di cultura generale" (Teams 1 @ 0:33:30);
- Privacy Enhancing Technologies, capitolo saltato (DI-02 @ 01:39:04);
- notaio digitale (DI-03 @ 01:09:14), certificati di attributo (DI-03 @ 01:25:27), self-issued contro self-signed (Teams 3 @ 0:27:21), QKD ("non è un corso di fisica", Teams 3 @ 0:00:21);
- topologie non gerarchiche delle PKI (DI-04 @ 00:03:11), DRM e dettagli del cinema digitale (DI-04 @ 01:23:18, Teams 4 @ 0:10:46), PEC (DI-04 @ 01:45:13, poi trattata nel 2026), criptovalute (DI-04 @ 01:55:41);
- metadati dei certificati X.509 "per esperti" (DI-05 @ 00:42:20), standard AdES (DI-05 @ 00:52:31), firme XML selettive (Teams 6 @ 0:50:37);
- Kerberos "per specialisti" (DI-05 @ 01:20:40, Teams 7 @ 0:32:36), dettagli tecnici di OAuth e OpenID Connect "materia per sviluppatori professionisti" (Teams 7 @ 0:37:36, 0:41:08), varianti OIDC e aggregatori SPID (Teams 8 @ 1:08:53).

## Concetti su cui il docente insiste

Sono le priorità di studio più sicure, perché il docente le chiama esplicitamente centrali:
- **firma digitale**: "il concetto logico più difficile da capire dell'intero corso" (DI-02 @ 01:15:34); "il 90% del digital trust si comprende se si comprende a cosa serve la firma digitale e come funziona" (Teams 1 @ 0:52:46);
- **key wrapping**: "capire questo meccanismo significa capire gran parte della crittografia" (DI-02 @ 00:49:52);
- autenticità con la chiave privata come "chiave per capire tutto il meccanismo del digital trust" (Teams 1 @ 0:09:25);
- cripto-agilità e scadenza programmata delle carte; robustezza come antieconomicità;
- certificati, CA, PKI, catena di fiducia, scadenza e revoca;
- **firma digitale (tecnica) contro firma elettronica (giuridica)**; firma contro sigillo; FEA e FEQ; non discriminazione dei documenti elettronici; fa fede il momento della firma;
- **identity proofing contro autenticazione**: "uno dei concetti fondamentali che vorrei passasse da qui alla fine del corso" (Teams 6 @ 1:09:46); autenticazione contro autorizzazione; centralizzata e federata; SSO; delega contro impersonificazione; SSI e selective disclosure; ruoli dell'EUDI Wallet.

## Cose da chiedere al docente o alla segreteria

- Modalità, data e formato dell'esame; se è congiunto con Cybersecurity e con quale peso.
- Se le slide verranno distribuite (oggi non ce ne sono).
- Se la lezione del 14/10/2025, citata in DI-02 @ 01:02:28 come "non registrata", contiene argomenti d'esame.
