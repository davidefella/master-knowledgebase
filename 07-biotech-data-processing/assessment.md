# Assessment

> Fonte Notion: https://app.notion.com/p/3e912abc808d81099520e028f6b4cf72 — ultima modifica 2026-09-28T17:30:12.084Z

## Test finale 2026 (`Test_Finale_BDP_26`, Teams)
"Test di valutazione di idoneità di fine corso." Esito: idoneità, non voto.
<table header-row="true">
<tr>
<td>Voce</td>
<td>Valore</td>
</tr>
<tr>
<td>Consegna</td>
<td>elaborato e allegati a [**ruccomatteo@gmail.com**](mailto:ruccomatteo@gmail.com)</td>
</tr>
<tr>
<td>Oggetto</td>
<td>`MDA 26 BDP – Nome Cognome – Test finale`</td>
</tr>
<tr>
<td>Scadenza scritta nella traccia</td>
<td>25/07/2026, confermata a voce (Teams 6 @ 1:08:04), nessuna proroga annunciata; già passata, si consegna comunque</td>
</tr>
</table>
### Esercizio teorico
<table header-row="true">
<tr>
<td>#</td>
<td>Domanda (verbatim)</td>
<td>Dove sta nel materiale</td>
</tr>
<tr>
<td>T1</td>
<td>Fornire una definizione di ABMS (max 3000 caratteri)</td>
<td>cap. 02; slide `ABMS.pdf`</td>
</tr>
<tr>
<td>T2</td>
<td>Fornire una definizione di ODE (max 3000 caratteri)</td>
<td>cap. 01; slide `Math_in_biology.pdf`</td>
</tr>
<tr>
<td>T3</td>
<td>Quali sono le caratteristiche principali di un ABMS?</td>
<td>cap. 02 (`BT-02 @ 00:32:17` caratteristiche degli agenti; `BT-02 @ 01:08:03` limiti)</td>
</tr>
<tr>
<td>T4</td>
<td>Quando usare ODE e quando ABMS?</td>
<td>cap. 02 (`BT-02` apertura: ABM "complementare" alle ODE), cap. 04</td>
</tr>
<tr>
<td>T5</td>
<td>Che tipo di studi possono essere fatti con l'epidemiologia computazionale?</td>
<td>cap. 04</td>
</tr>
<tr>
<td>T6</td>
<td>Cosa rende l'epidemiologia una scienza complessa? Elencare e descrivere i principali elementi di complessità.</td>
<td>cap. 04 (`BT-04 @ 00:42:08`, "l'epidemiologia è come un'orchestra")</td>
</tr>
</table>
### Esercizio pratico, uno a scelta
**Esercizio 1: simulazione ad agenti (Mesa), ecosistema preda-predatore.** Due tipi di agenti: prede (movimento casuale, riproduzione con probabilità fissa dopo un certo numero di passi, eliminate se catturate) e predatori (movimento casuale in cerca di prede vicine, muoiono se non trovano cibo entro un numero prefissato di passi, si riproducono dopo aver mangiato abbastanza). Griglia toroidale. Animazione in tempo reale con l'interfaccia grafica di Mesa. Registrare e visualizzare prede e predatori nel tempo.
Output: file Python completo, grafici dell'andamento delle popolazioni, breve rapporto con l'analisi dei risultati.
Materiale: cap. 02 (zombie e preda-predatore ad agenti), cap. 03 (Kuramoto e Vicsek con MESA), notebook `Zombie_ABMS_lezione_3_Biotech.ipynb`, `SIR_ABMS.ipynb`.
**Esercizio 2: crescita tumorale, modello di Gompertz.**
$`\frac{dT}{dt} = r\,T(t)\,\ln\frac{K}{T(t)}`$
con $`r = 0.05`$ giorno⁻¹, $`K = 10^9`$ cellule, $`T(0) = 10^6`$ cellule, $`t \in [0, 300]`$ giorni. Risoluzione con Eulero esplicito ($`\Delta t = 0.1`$ giorni) o `odeint`: simulare, rappresentare $`T(t)`$, determinare il tempo per arrivare a $`K/2`$.
Output: file Python completo, grafici, breve rapporto.
Materiale: cap. 01 (Eulero e `odeint`), notebook `01_eulero_crescita_batterica.ipynb`, `02_eulero_vs_odeint_bioreattore_batch.ipynb`, `03_odeint_farmacodinamica_biotech.ipynb`, `04_odeint_fed_batch_proteina_ricombinante.ipynb`.
> ⚠️ **Refuso nella traccia.** Dice "Si scelga di risolvere il modello tramite uno fra i due approcci seguenti" ma elenca un solo punto (1. Eulero esplicito o `odeint`). Il secondo approccio manca.
## Cosa ha detto il docente sull'esame (edizione 2025)
<table header-row="true">
<tr>
<td>Dove</td>
<td>Cosa</td>
</tr>
<tr>
<td>`BT-05 @ 00:03:39`</td>
<td>Il test si svolge all'ultimo incontro (3 ore): "sono principalmente delle domande e opzionale c'è anche una parte Python da sviluppare", circa un'ora, un'ora e mezza; non c'è obbligo di restituirlo durante l'incontro, si può lavorare offline</td>
</tr>
<tr>
<td>`BT-01 @ 01:15:20`</td>
<td>Gli esercizi del Colab non vanno inviati, ma "possono aiutarvi poi nell'affrontare la prova finale"</td>
</tr>
<tr>
<td>`BT-01 @ 01:19:04`</td>
<td>Sensitivity analysis (SALib): "non sarà argomento pratico dell'esame", possibile una domanda su come caratterizzare un modello</td>
</tr>
<tr>
<td>`BT-02 @ 01:30:45`</td>
<td>Il codice zombie ad agenti "potrebbe essere un esercizio utile per il test finale"</td>
</tr>
<tr>
<td>`BT-03 @ 00:44:48`</td>
<td>Modello di Jerne: per il test finale variare tipo e numero di anticorpi, idiotipo dell'antigeno iniziale</td>
</tr>
<tr>
<td>`BT-04 @ 00:40:13`</td>
<td>"Se al test finale dovessi dirvi quali sono le assunzioni importanti per utilizzare il modello SIR": la prima è la popolazione omogenea</td>
</tr>
<tr>
<td>`BT-04 @ 01:14:36`, `01:17:09`</td>
<td>SIR su grafo ed esercizio a tabella "non fondamentali" per il test finale</td>
</tr>
<tr>
<td>`BT-06 @ 00:56:11`</td>
<td>Dopo il TSP si legge insieme la traccia dell'assignment finale: **non registrato**</td>
</tr>
</table>
## Perimetro
- Il test 2026 copre **cap. 01, 02, 04** (teoria) e **cap. 01 oppure 02-03** (pratica).
- TDA (cap. 03, salvo MESA), bioinformatica (cap. 05) e algoritmi genetici (cap. 06) non compaiono nella traccia.
## Cosa ha detto il docente nel 2026 (Teams)
<table header-row="true">
<tr>
<td>Dove</td>
<td>Cosa</td>
</tr>
<tr>
<td>`Teams 1 @ 1:09:51`</td>
<td>Alla domanda su come si chiude il modulo: una traccia con 4-5 domande a risposta aperta sui concetti teorici delle lezioni, più un esercizio Python. Somministrata l'ultimo giorno (lunedì), con tempo per lavorarci anche offline e un intervallo di consegna; niente obbligo di presenza</td>
</tr>
<tr>
<td>`Teams 6 @ 58:12`</td>
<td>Dopo l'ultima lezione tecnica (epidemiologia computazionale) si legge insieme la traccia</td>
</tr>
<tr>
<td>`Teams 6 @ 1:07:24`</td>
<td>Assignment con parte teorica e parte pratica; si può affrontare in aula (il docente resta collegato per chiarimenti) o offline</td>
</tr>
<tr>
<td>`Teams 6 @ 1:08:04`</td>
<td>Consegna entro il **25 luglio**</td>
</tr>
<tr>
<td>`Teams 6 @ 1:08:13`</td>
<td>Domande teoriche "poche e semplici", "completamente allineate" ai contenuti del corso</td>
</tr>
<tr>
<td>`Teams 6 @ 1:09:10`</td>
<td>Pratica: se ne sceglie uno dei due esercizi. Il preda-predatore con Mesa è "un esercizio semplice, l'abbiamo già in parte affrontato assieme" (@ 1:11:14); il Gompertz è "una sfida un po' più complessa" (@ 1:11:20)</td>
</tr>
<tr>
<td>`Teams 6 @ 1:10:32`</td>
<td>Mesa: visualizzazione in tempo reale delle posizioni degli agenti e delle statistiche sul numero di agenti per tipo</td>
</tr>
<tr>
<td>`Teams 6 @ 1:12:50`</td>
<td>Gompertz: "potete scegliere di utilizzare uno fra i seguenti approcci, implementazione numerica, metodo di Eulero esplicito o metodo odeint". Chiarisce il refuso della traccia: le due alternative sono **Eulero o odeint**</td>
</tr>
<tr>
<td>`Teams 6 @ 1:13:48`</td>
<td>Eulero va codificato da zero, ma una codifica è già nelle slide e nei Colab, "soprattutto in quello relativo alla crescita delle cellule" (notebook `01_eulero_crescita_batterica`)</td>
</tr>
<tr>
<td>`Teams 6 @ 1:14:08`</td>
<td>Consegna: un file Python completo con codice della simulazione, grafici e analisi</td>
</tr>
<tr>
<td>`Teams 6 @ 1:14:21`</td>
<td>Consegna per email, oggetto "MDA 26 BDP", nome e cognome, "test finale"</td>
</tr>
<tr>
<td>`Teams 6 @ 1:14:47`</td>
<td>Il docente notifica via mail e Teams l'avvenuta correzione, con raccomandazioni se necessarie. Alla domanda "un voto?" risponde "Assolutamente" e poi "è un modo per confrontarci" su quanto è stato assorbito: se ci sia un voto resta ambiguo \[?\]</td>
</tr>
<tr>
<td>`Teams 6 @ 1:15:41`</td>
<td>Vanno bene sia il notebook sia il file `.py`</td>
</tr>
<tr>
<td>`Teams 6 @ 1:17:12`</td>
<td>La traccia (file doc) è caricata nel materiale condiviso del canale</td>
</tr>
</table>
> **Nota aggiunta:** la traccia a voce dice "K un milione di cellule" e poi "miliardo"; il testo scritto è quello da seguire: $`K = 10^9`$, $`T(0) = 10^6`$.
## Da chiarire
- Se la consegna oltre il 25/07 viene ancora accettata: conviene scriverlo nella mail di consegna.
