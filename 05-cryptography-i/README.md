# Cryptography I

> Fonte Notion: https://app.notion.com/p/3e312abc808d816eae45f8e5c398b7d9 — ultima modifica 2026-09-22T13:27:07.471Z

Modulo del Master Data Analytics, docente **Elia Onofri** (IAC-CNR e Dipartimento di Matematica e Fisica, Roma Tre). Sulle slide il titolo dei deck è *Cryptography I \| Deep-dive N/5*.
Il corso è un'introduzione alla crittografia in quattro lezioni: storia e concetti base, crittografia simmetrica, crittografia asimmetrica, funzioni di hash e firme digitali. È il primo dei due moduli, seguito da **Crittografia Case Study**.
## Fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Uso</td>
</tr>
<tr>
<td>4 registrazioni del portale `learn.master-data-analytics.it` (`CR-01` … `CR-04`), 1920×1080</td>
<td>**fonte di verità** del manuale</td>
</tr>
<tr>
<td>4 deck PDF da Teams (`crypto1_session1` … `session4`)</td>
<td>solo di contorno, per chiarire passaggi oscuri</td>
</tr>
<tr>
<td>14 PDF di progetto (8 `assignment_*`  • 6 `project_L2_*`)</td>
<td>esame, vedi pagina Assessment</td>
</tr>
</table>
> ⚠️ **I deck non sono le slide delle registrazioni.** Sono quattro sessioni *deep-dive* separate, che partono tutte da «recap — what the recordings already established». Corrispondenze per contenuto: `CR-02` ↔ deck 2, `CR-03` ↔ deck 3, `CR-04` ↔ deck 4. **`CR-01`**** non ha un deck corrispondente.** I deck si dichiarano «1/5»…«4/5»: il quinto non è fra i file distribuiti.
## Come sono fatte queste pagine
La regola di questo corso è diversa da quella usata per TensorFlow: **la registrazione è la fonte di verità**, il materiale del docente serve solo quando un passaggio a lezione resta oscuro. Un manuale che ripete il libro non serve — serve la lezione, resa studiabile.
Ogni capitolo segue la lezione per sezioni tematiche, con riferimenti `CR-0N @ hh:mm:ss`.
Convenzioni:
- `[?]` — parola non chiara nell'audio o contenuto dubbio
- `[illeggibile]` — schermo non leggibile
- **Nota aggiunta** — integrazione non trattata a lezione
- ✅ — conto verificato per esecuzione in Python
- ⚠️ / 🔴 — divergenza, dettagli nella pagina Divergenze
## Capitoli
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Durata</td>
<td>Contenuto</td>
<td>Stato</td>
</tr>
<tr>
<td>01 - Introduzione alla crittografia</td>
<td>02:04:21</td>
<td>Storia, 4 obiettivi, attori, simmetrica/asimmetrica, modelli di attacco</td>
<td>completo</td>
</tr>
<tr>
<td>02 - Crittografia simmetrica</td>
<td>01:14:54</td>
<td>Vernam/OTP, segretezza perfetta, stream cipher, LFSR, block cipher, AES</td>
<td>completo</td>
</tr>
<tr>
<td>03 - Crittografia asimmetrica</td>
<td>02:10:53</td>
<td>Key exchange, Diffie–Hellman, RSA, ElGamal, Paillier, Rabin, OT, curve ellittiche</td>
<td>completo</td>
</tr>
<tr>
<td>04 - Integrità, hash e firme</td>
<td>**01:20:27**</td>
<td>Hash, Merkle–Damgård, spugna/SHA-3, MAC/HMAC, firme elettroniche</td>
<td>**incompleto**: registrazione troncata</td>
</tr>
</table>
> 🔴 **La lezione 4 è troncata.** Il file dura 02:04:21 ma il parlato finisce a `01:20:27`, a metà di un elenco. Gli **schemi di impegno** (commitment schemes, Lamport, alberi di Merkle), annunciati a `CR-04 @ 00:01:15` e già nella roadmap di `CR-01 @ 00:15:45`, **non compaiono nella registrazione**. È l'unica lacuna di contenuto del corso.
## Stato delle fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Stato</td>
</tr>
<tr>
<td>`CR-01` … `CR-04` (portale)</td>
<td>scaricate in 1080p, trascritte (\~7h di video)</td>
</tr>
<tr>
<td>Frame delle slide</td>
<td>584 estratti, 456 dopo deduplica, **350 slide logiche** dopo triage</td>
</tr>
<tr>
<td>4 deck PDF (174 pagine)</td>
<td>scaricati, testo estratto per pagina</td>
</tr>
<tr>
<td>14 PDF di progetto</td>
<td>scaricati</td>
</tr>
<tr>
<td>Deck 5/5</td>
<td>**non trovato** — da cercare su Teams</td>
</tr>
</table>
## Qualità dell'audio
Ottima su tutte e quattro: logprob mediano −0.12, e alla soglia −0.6 prevista dalla pipeline **2 segmenti dubbi su 3.100**. Il segnale utile, su questo corso, stava piuttosto a −0.3, e risultava concentrato su `CR-03` e `CR-04`.
Un'eccezione da conoscere: i 43 minuti di coda vuota di `CR-04` hanno prodotto **88 «Grazie a tutti.»** allucinati, rimossi dalla trascrizione.
## Dove sta il materiale
Sul Mac: `~/Work/Projects/data-science/data-analytics/50-cryptography-i/`
- `video/CR-0N.mp4` — le registrazioni
- `out/lezione-0N/` — manuale e divergenze in markdown
- `out/CR-0N/` — trascrizioni, frame, OCR, triage
- `Materiale/Teams/{Slides,Assessment}` — deck e progetti
- `scripts/` — pipeline completa e script di verifica dei conti

[02 - Crittografia simmetrica](02-crittografia-simmetrica.md)

[01 - Introduzione alla crittografia](01-introduzione-alla-crittografia.md)

[03 - Crittografia asimmetrica](03-crittografia-asimmetrica.md)

[04 - Integrità, hash e firme](04-integrita-hash-e-firme.md)

[Assessment](assessment.md)

[Divergenze](divergenze.md)
