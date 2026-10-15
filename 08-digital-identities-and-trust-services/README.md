# Digital Identities and Trust Services

Modulo del Master Data Analytics, docente **Walter Arrighetti**, lo stesso di [Cybersecurity, Cyber Intelligence and Data Privacy](../06-cybersecurity-cyber-intelligence-data-privacy/README.md), di cui questo è il "secondo corso". Il corso parte dalla crittografia applicata (hash, simmetrica, chiave pubblica, key wrapping, firma digitale, post-quantum), costruisce il digital trust (certificati, CA, PKI, revoca, HSM) e arriva ai servizi fiduciari eIDAS (firme e sigilli elettronici, elenchi di fiducia, formati di firma) e alle identità digitali (identity proofing, autenticazione, SSO, OAuth e OpenID Connect, SPID, CIE, EUDI Wallet).

Il ponte con Cybersecurity è il capitolo 07 di quella guida (sezioni 11-17): la prima ora del capitolo 01 qui lo ripete, con rimandi invece di ripetizioni.

## Fonti

| Fonte | Uso |
|---|---|
| Registrazioni del portale `learn.master-data-analytics.it` (`DI-01` … `DI-06`), **edizione 2025** (Teams, 07-30/10/2025, circa 11 h 45) | **fonte di verità** del manuale |
| Materiale del docente | **nessuno**: niente slide distribuite. Tutto ciò che è a schermo è letto dai fotogrammi |
| Registrazioni Teams 2026 (SharePoint `MDA2026-DigitalIdentitiesandTrustServices`, "Solo visualizzazione", 21-30/09/2026, 8 lezioni, circa 11 h) | **integrate nei capitoli**: riquadri "Integrazione Teams 2026" dentro la sezione a cui si riferiscono; argomenti nuovi del 2026 in sezioni dedicate. Trascrizioni lette in pagina, mai salvate |

> ⚠️ **DI-01 perde l'audio da 01:09:08 a 01:47:42** (silenzio digitale, slide che avanzano). Quella parte (curve ellittiche, casi d'uso della chiave pubblica, svantaggi della simmetrica, key wrapping) è ricostruita dalle slide e dal commento di DI-02 e Teams 1. I 6 file del portale hanno tutti lo stesso nome con timestamp `20251007_181621`, ma sono lezioni distinte (date verificate sul banner Teams del primo frame). In DI-02 il docente cita una lezione del giorno prima "non registrata".

## Come sono fatte queste pagine

Ogni capitolo segue una lezione 2025 per sezioni tematiche, con riferimenti `DI-0N @ hh:mm:ss` e, per il 2026, `Teams N @ h:mm:ss`. Il testo delle slide è riportato fedelmente (in inglese se la slide è in inglese). Gli esempi crittografici e numerici mostrati a schermo (digest SHA-256, AES e RSA in CyberChef, JWT, Diffie-Hellman, SD-JWT, tabelle sulle collisioni) sono **verificati per esecuzione**.

Convenzioni:
- `[?]`: parola non chiara nell'audio o contenuto dubbio
- `[illeggibile]`: schermo non leggibile
- **Nota aggiunta**: integrazione non detta a lezione
- **Correzione**: affermazione del docente imprecisa, dettagli nella pagina [Divergenze](divergenze.md)

## Capitoli

| Capitolo | Lezione 2025 | Durata | Teams 2026 integrate | Contenuto |
|---|---|---|---|---|
| [01 - Crittografia, cripto-agilità, hash, RSA](01-crittografia-cripto-agilita-hash-rsa.md) | 07/10/2025 | 1:48:12 (parlato 1:09) | Teams 1 fino a 0:29 | Il docente, cripto-agilità (carte, documenti, lettori, ICAO), funzioni di hash e collisioni, salting, CyberChef SHA-256, cifratura simmetrica e a chiave pubblica, crittoanalisi, RSA, ECC, key wrapping |
| [02 - Chiave pubblica, firma digitale, calcolo quantistico](02-chiave-pubblica-firma-digitale-calcolo-quantistico.md) | 15/10/2025 | 1:54:57 | Teams 1 da 0:29 | Usi della chiave pubblica, CyberChef AES e RSA, key wrapping, tre stati della cifratura, cifratura omomorfa, firma digitale contro autografa, PAdES, JWT/JWS/JWE/JAdES, introduzione al calcolo quantistico |
| [03 - Post-quantum, certificati e PKI](03-post-quantum-certificati-e-pki.md) | 17/10/2025 | 1:57:53 | Teams 2, Teams 3 fino a 0:58 | Cifratura per più destinatari, omomorfa in formule, standard NIST PQC, harvest now decrypt later, QKD, migrazione ibrida, notai e CA, certificato X.509, certificati eIDAS, PKI gerarchica |
| [04 - Revoca, TLS, HSM, servizi fiduciari](04-revoca-tls-hsm-servizi-fiduciari.md) | 27/10/2025 | 2:25:44 (parlato 2:11) | Teams 3 da 0:58, Teams 4 | Convalida della catena, RA e VA, scadenza, CRL e OCSP, PFS, Diffie-Hellman, TLS e certificati di siti reali, CA/Browser Forum, HSM, CSR, KDM del cinema, firme remote e CIE, passaporti, servizi fiduciari, blockchain, marcatura temporale |
| [05 - Firme e sigilli, eIDAS, autenticazione](05-firme-e-sigilli-eidas-autenticazione.md) | 29/10/2025 | 1:53:47 | Teams 5, Teams 6 fino a 1:01 | Servizi fiduciari qualificati, firma digitale e firma elettronica, sigilli, DPCM firme, FEA e FEQ, EUTL e Brexit, formati e firme multiple, PAdES e attacchi, JAdES, PEC (2026), fattori di autenticazione, identity proofing, livelli di garanzia, Kerberos |
| [06 - Identità digitale, OAuth, OIDC, EUDI Wallet](06-identita-digitale-oauth-oidc-eudi-wallet.md) | 30/10/2025 | 1:46:38 | Teams 6 da 1:01, Teams 7, Teams 8 | Identity proofing, autenticazione centralizzata e federata, SSO, deleghe, SSI, credenziali verificabili, SAML, OAuth 2.0, OpenID Connect, SD-JWT, SPID, CIE, IT-Wallet, eIDAS 2 ed EUDI Wallet, bibliografia |

- [Assessment](assessment.md): tutto ciò che il docente dice sull'esame, 2025 e 2026
- [Divergenze](divergenze.md): correzioni e note, capitolo per capitolo

## Qualità dell'audio

Ottima: avg_logprob p5 circa -0.18, la soglia -0.3 non discrimina (2-5 segmenti per lezione). Gli errori veri sono sigle e nomi propri trascritti con sicurezza ("AIDAS"/"EITA" per eIDAS, "Fjellman" per Diffie-Hellman, "CED" per CIE, "iswer" per issuer), corretti nel testo ed elencati nelle divergenze.

## Dove sta il materiale

Sul Mac: `~/Work/Projects/data-science/data-analytics/90-digital-identities-and-trust-services/`
- `video/DI-0N.mp4`: le registrazioni del portale
- `out/lezione-0N/`: manuale e divergenze in markdown (stesso contenuto di queste pagine)
- `out/DI-0N/`: trascrizioni, frame, OCR (manca l'OCR indice di DI-05)
- `out/teams-2026/`: riassunti delle integrazioni Teams 2026 per capitolo (nessuna trascrizione salvata)
- `out/controlli-iniziali.md`: identità dei file, sovrapposizioni, esame
- `scripts/`: pipeline
