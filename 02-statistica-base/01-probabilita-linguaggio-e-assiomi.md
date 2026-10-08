# 01 - Probabilità: linguaggio e assiomi

> Fonte Notion: https://app.notion.com/p/3c612abc808d81fbbe0defcd84540340 — ultima modifica 2026-08-25T21:32:56.411Z

<table_of_contents color="gray"/>
Prima lezione. Si costruisce il **vocabolario** della probabilità (esito, evento, spazio campionario) e si enunciano le **tre regole** da cui discende tutto il resto. Ogni concetto è illustrato sullo stesso esempio: il **lancio di un dado**.
<callout icon="🎲" color="blue_bg">
	**Il dado di riferimento.** Un dado a sei facce, non truccato. Gli esiti possibili sono $`\Omega = \{1,2,3,4,5,6\}`$ e ogni faccia ha la stessa probabilità $`1/6`$.
	Regola di calcolo usata in tutta la pagina: **P(evento) = quanti esiti lo soddisfano ÷ 6**.
</callout>
---
## Cos'è la probabilità
Il docente la introduce così: **"p" misura il grado di confidenza**, cioè *quanto crediamo* che un evento accada.
$`P(E)`$ è un numero compreso fra 0 e 1:
- $`P(E) = 0`$ → l'evento non può accadere
- $`P(E) = 1`$ → l'evento accade di sicuro
- $`P(E) = 0.5`$ → accade o non accade con la stessa fiducia
Sul dado: $`P(\text{esce } 4) = 1/6 \approx 0.17`$ — un esito favorevole su sei possibili.
<details>
<summary>**\[integrazione\] Perché si parla di lettura "soggettiva", se il calcolo è aritmetico**</summary>
	Il calcolo $`1/6`$ è oggettivo, ma **solo dopo** aver deciso che il dado è equo. Quella decisione non è aritmetica: è un'assunzione sul mondo. Se il dado fosse truccato, la stessa aritmetica darebbe un altro numero. *L'aritmetica calcola le conseguenze del modello; non dice se il modello è giusto.*
	"Soggettiva" quindi **non** vuol dire arbitraria: due persone con le stesse informazioni arrivano allo stesso numero. Vuol dire che la probabilità esprime il grado di fiducia di chi la assegna, viste le informazioni di cui dispone.
</details>
---
## Il vocabolario
<table fit-page-width="true" header-row="true">
<tr>
<td>Termine</td>
<td>Simbolo</td>
<td>Cos'è</td>
<td>Sul dado</td>
</tr>
<tr>
<td>**Esito**</td>
<td>$`\omega`$</td>
<td>Un singolo risultato possibile</td>
<td>Esce 4</td>
</tr>
<tr>
<td>**Spazio campionario**</td>
<td>$`\Omega`$</td>
<td>L'insieme di **tutti** gli esiti che l'esperimento può produrre (non tutti i numeri esistenti: solo quelli ottenibili)</td>
<td>$`\{1,2,3,4,5,6\}`$</td>
</tr>
<tr>
<td>**Evento**</td>
<td>$`E, A, B`$</td>
<td>Un **sottoinsieme** di $`\Omega`$: uno o più esiti raggruppati da una condizione</td>
<td>"Esce pari" $`= \{2,4,6\}`$</td>
</tr>
<tr>
<td>**Evento certo**</td>
<td>$`\Omega`$</td>
<td>Contiene tutti gli esiti: accade sempre</td>
<td>"Esce un numero da 1 a 6"</td>
</tr>
<tr>
<td>**Evento impossibile**</td>
<td>$`\emptyset`$</td>
<td>Non contiene nessun esito: non accade mai</td>
<td>"Esce 7"</td>
</tr>
<tr>
<td>**Complementare**</td>
<td>$`\bar{E}`$</td>
<td>Tutto ciò che sta **fuori** da $`E`$</td>
<td>Se $`E`$ = pari, $`\bar{E}`$ = dispari $`= \{1,3,5\}`$</td>
</tr>
</table>
<callout icon="⚠️" color="yellow_bg">
	**\[integrazione\] Due termini del docente da tradurre.**
	- **"spazio delle fasi"** è linguaggio da fisico. Nei testi di statistica, Dekking compreso, lo stesso oggetto si chiama **spazio campionario** (*sample space*). Stessa cosa, nome diverso.
	- **"insieme degli eventi"**: a rigore $`\Omega`$ è l'insieme degli **esiti**; un **evento** è un *sottoinsieme* di $`\Omega`$. La distinzione conta perché la probabilità si assegna agli eventi, ed è ciò che permette di scrivere $`P(\text{pari}) = 3/6`$ sommando i tre esiti che compongono l'evento.
</callout>
---
## Il "mondo": la natura degli esiti
Nella slide il docente disegna un insieme più grande, $`\{0,1,2,3,4,5,6,7,8,9,\dots\}`$, e lo chiama *il mondo*. Non è lo spazio campionario: è l'insieme in cui **vivono** i valori, cioè la loro natura. In questo caso, i numeri naturali.
Il dado non può dare 0, quindi quell'insieme **non** è lo spazio campionario del dado: è l'ambiente più ampio da cui il dado pesca solo $`\{1,\dots,6\}`$.
> **In termini informatici:** è il **tipo**. Dichiarare `int` dice quali valori sono ammissibili in generale; poi il fenomeno specifico ne usa un sottoinsieme.
![](notion-file-block://2261469a-31dd-4a8f-8761-e7802cabd20d/a5aaf50a-896a-4da4-b350-cd86abbcb6e0?space_id=98012abc-808d-816f-9733-00030a2b4817&name=mondo-omega-evento.svg)
Lo 0 c'è semplicemente perché fa parte dei numeri naturali, l'insieme disegnato dal docente. Il dado non lo produrrà mai — non ha una faccia con lo 0 — ed è proprio questo che mostra la differenza fra i due insiemi.
<callout icon="⚠️" color="yellow_bg">
	**Allora **$`\Omega`$** è il mondo, o è **$`\{1,\dots,6\}`$**?**
	È $`\{1,\dots,6\}`$. Nei libri — Dekking compreso — $`\Omega`$ indica **sempre** lo spazio campionario, cioè ciò che l'esperimento può produrre.
	Il "mondo" è l'insieme ancora più grande disegnato attorno, e **non ha un simbolo standard**: serve solo a dire di che natura sono i valori. Se sugli appunti del docente compare $`\Omega`$ accanto a quell'insieme grande, è una licenza sua: quando leggerai un libro, $`\Omega`$ sarà il rettangolo di mezzo dell'immagine qui sopra.
</callout>
---
## Diagrammi di Venn
Servono a ragionare sugli eventi come insiemi. Il rettangolo è $`\Omega`$, le regioni dentro sono eventi.
> **Modello mentale da tenere:** la probabilità si comporta come un'**area**. L'area totale vale 1; un evento che occupa più spazio è più probabile.
### 1. L'evento e il suo complementare
$$
\Omega \;=\; E \;\cup\; \bar{E}
$$
Preso un evento $`E`$ qualsiasi, $`\bar{E}`$ è tutto ciò che sta fuori da $`E`$. Insieme riempiono esattamente $`\Omega`$, senza sovrapporsi.
Si legge così: **lo spazio campionario è formato dall'evento che stai analizzando, unito a tutto ciò che non stai analizzando.** Sul dado: $`\{1,2,3,4,5,6\} = \{2,4,6\} \cup \{1,3,5\}`$, cioè i pari (l'evento) più i dispari (tutto il resto).
<callout icon="⚠️" color="yellow_bg">
	Un'unica precisazione: $`\Omega`$ **non** è "tutti i valori esistenti", ma solo i sei che il dado può davvero produrre. L'insieme di tutti i numeri è il *mondo* della sezione precedente, che è un'altra cosa.
</callout>
**Sul dado:** $`E`$ = "esce pari" $`= \{2,4,6\}`$, quindi $`\bar{E}`$ = "esce dispari" $`= \{1,3,5\}`$. Uniti danno tutte e sei le facce.
![](notion-file-block://08b56542-c9a9-48c7-843f-fe12c7e450b1/c0f32f24-ead1-438f-828d-00dd2d8a0622?space_id=98012abc-808d-816f-9733-00030a2b4817&name=venn-01-complementare.svg)
### 2. Intersezione e "né l'uno né l'altro"
$$
C = A \cap B \qquad D = \bar{A} \cap \bar{B}
$$
- $`C = A \cap B`$ → la zona di sovrapposizione: gli esiti che stanno **sia** in $`A`$ **sia** in $`B`$.
- $`D = \bar{A} \cap \bar{B}`$ → la zona fuori da entrambi: gli esiti che non stanno **né** in $`A`$ **né** in $`B`$.
**Sul dado**, con $`A`$ = "pari" $`= \{2,4,6\}`$ e $`B`$ = "maggiore di 3" $`= \{4,5,6\}`$:
- $`A \cap B = \{4,6\}`$ → pari **e** maggiore di 3
- $`\bar{A} \cap \bar{B} = \{1,3\}`$ → dispari **e** minore o uguale a 3
![](notion-file-block://8db92442-da2c-4874-a3d2-b2a8416d5ea9/19649a84-f943-4e01-970f-26c54b80a29a?space_id=98012abc-808d-816f-9733-00030a2b4817&name=venn-02-intersezione.svg)
### 3. La partizione
Partizionare vuol dire **dividere** $`\Omega`$ **in gruppi**, rispettando due regole contemporaneamente: i gruppi devono **coprire tutto** e **non sovrapporsi**.
Sono le due regole formalizzate qui sotto come *esaustivi* ed *esclusivi*.
> **L'immagine da tenere in mente è una cassettiera.** Prendi tutti gli esiti possibili e li distribuisci nei cassetti, con un vincolo: **ogni esito deve finire in uno e un solo cassetto**.
> *Nessun esito resta sul tavolo* — è la prima regola. *Nessuno viene fotocopiato in due cassetti* — è la seconda.
I cassetti si chiamano $`H_1, H_2, \dots, H_n`$, e le due regole sono queste:
<table fit-page-width="true" header-row="true">
<tr>
<td>Regola</td>
<td>In simboli</td>
<td>In parole</td>
</tr>
<tr>
<td>**Esaustivi**</td>
<td>$`\Omega = \bigcup_i H_i`$</td>
<td>Messi insieme, i cassetti coprono tutti gli esiti: nessuno resta fuori</td>
</tr>
<tr>
<td>**Mutuamente esclusivi**</td>
<td>$`H_i \cap H_j = \emptyset`$ per ogni $`i \neq j`$</td>
<td>Due cassetti diversi non hanno mai un esito in comune</td>
</tr>
</table>
**Sul dado**, una partizione possibile è in tre cassetti da due facce ciascuno:
$$
H_1 = \{1,2\} \qquad H_2 = \{3,4\} \qquad H_3 = \{5,6\}
$$
Verifica delle due regole: tutte e sei le facce compaiono da qualche parte (esaustivi), e nessuna faccia compare due volte (esclusivi).
![](notion-file-block://93ac1333-05d4-4482-946e-7c1e49e2f3b5/e930af26-0872-43fc-87d8-07c1da047df3?space_id=98012abc-808d-816f-9733-00030a2b4817&name=venn-03-partizione.svg)
**Attenzione: non tutte le divisioni sono partizioni.** Basta che salti una delle due regole e non lo è più.
- $`\{1,2,3,4\}`$ e $`\{4,5,6\}`$ → **no**, il 4 finirebbe in due cassetti
- $`\{1,2\}`$ e $`\{5,6\}`$ → **no**, il 3 e il 4 resterebbero fuori
![](notion-file-block://1599511d-80e0-44a2-9c0b-84db26b3b0d2/ade7ae5c-a603-48e6-a00c-b928db7536a8?space_id=98012abc-808d-816f-9733-00030a2b4817&name=partizione-controesempi.svg)
**A cosa serve tutto questo.** Se i cassetti sono una vera partizione, le loro probabilità sommano esattamente a 1 — sul dado $`2/6 + 2/6 + 2/6 = 1`$. Questo permette di calcolare la probabilità di un evento **un cassetto alla volta**, sommando i pezzi, invece di affrontarla tutta insieme: è la mossa che rende gestibili i problemi complicati.
> La lettera $`H`$ sta per *ipotesi*: i cassetti rappresentano scenari alternativi, di cui **uno solo è quello vero, ma di sicuro uno lo è**. La partizione torna in azione nel modulo [02 - Probabilità condizionata](02-probabilita-condizionata.md), con la legge della probabilità totale.
Il caso 1 di questa pagina — evento e complementare — è la partizione più semplice possibile: due soli cassetti, $`E`$ e $`\bar{E}`$.
---
## Gli assiomi
Tre regole che **non si dimostrano**: sono la definizione stessa di "probabilità". Qualunque assegnazione di numeri agli eventi che le rispetti è una probabilità valida.
### Assioma 1 — la probabilità sta fra 0 e 1
$$
0 \le P(E) \le 1
$$
Non esistono probabilità negative né maggiori di 1. Se un calcolo produce $`1.4`$ o $`-0.2`$, c'è un errore.
### Assioma 2 — qualcosa deve accadere
$$
P(\Omega) = 1
$$
Lanciando il dado, "esce un numero fra 1 e 6" è certo. È questo assioma a fissare la scala: senza, la probabilità sarebbe un numero senza riferimento.
### Assioma 3 — eventi incompatibili si sommano
$$
P(E_1 \cup E_2) = P(E_1) + P(E_2) \qquad \text{se} \qquad E_1 \cap E_2 = \emptyset
$$
Se due eventi **non possono accadere insieme** (intersezione vuota), la probabilità che accada l'uno *oppure* l'altro è la somma delle due.
**Sul dado:** $`E_1`$ = "esce 1" e $`E_2`$ = "esce 2" non possono verificarsi insieme, quindi
$$
P(\{1\} \cup \{2\}) = \tfrac{1}{6} + \tfrac{1}{6} = \tfrac{2}{6}
$$
<callout icon="🚨" color="red_bg">
	**L'errore classico: sommare eventi che si sovrappongono.**
	Con $`A`$ = "pari" $`= \{2,4,6\}`$ e $`B`$ = "maggiore di 3" $`= \{4,5,6\}`$, entrambi hanno probabilità $`3/6`$. Sommandole verrebbe $`6/6 = 1`$, cioè "è certo che esca un numero pari oppure maggiore di 3" — falso, basta che esca 1.
	Il vero risultato è $`A \cup B = \{2,4,5,6\}`$, quindi $`4/6`$. L'assioma 3 **non si applica**, perché $`A \cap B = \{4,6\} \neq \emptyset`$: il 4 e il 6 verrebbero contati due volte.
</callout>
<details>
<summary>\[integrazione\] La formula generale, quando gli eventi si sovrappongono</summary>
	Per due eventi qualsiasi vale sempre:
	$$
	P(A \cup B) = P(A) + P(B) - P(A \cap B)
	$$
	Si sottrae l'intersezione perché altrimenti verrebbe contata due volte. Sul dado: $`3/6 + 3/6 - 2/6 = 4/6`$, che coincide col conteggio diretto.
	Quando $`A \cap B = \emptyset`$ il termine sottratto vale 0 e si ricade nell'assioma 3.
</details>
<details>
<summary>\[integrazione\] Nota di rigore sull'assioma 1</summary>
	Nella formulazione standard (assiomi di Kolmogorov) si richiede solo $`P(E) \ge 0`$: il limite superiore $`P(E) \le 1`$ **si dimostra** a partire dagli altri assiomi, non va postulato.
	Il docente lo enuncia comunque per comodità, ed è una scelta didattica comune. Non cambia nulla nella pratica.
</details>
---
## I corollari
Non sono regole nuove: **discendono** dai tre assiomi. Sono le tre scorciatoie che si usano continuamente.
### Corollario 1 — la regola del complementare
$$
P(E) = 1 - P(\bar{E})
$$
**Sul dado:** $`P(\text{pari}) = 1 - P(\text{dispari}) = 1 - 3/6 = 3/6`$.
> **A cosa serve davvero.** Spesso calcolare "almeno uno" è complicato mentre calcolare "nessuno" è facile. Esempio: la probabilità di ottenere **almeno un 6** in tre lanci richiederebbe di enumerare molti casi; il suo complementare è "nessun 6 in tre lanci" $`= (5/6)^3`$, immediato. Quindi $`1 - (5/6)^3 \approx 0.42`$.
<details>
<summary>Da dove viene</summary>
	$`E`$ e $`\bar{E}`$ non si sovrappongono e insieme danno $`\Omega`$ (primo diagramma di Venn). Applicando l'assioma 3 e poi l'assioma 2:
	$$
	P(E) + P(\bar{E}) = P(\Omega) = 1
	$$
	Da cui, spostando un termine, $`P(E) = 1 - P(\bar{E})`$.
</details>
### Corollario 2 — l'evento impossibile ha probabilità zero
$$
P(\emptyset) = 0
$$
**Sul dado:** "esce 7" non contiene nessun esito, quindi ha probabilità 0.
<details>
<summary>Da dove viene</summary>
	È il corollario 1 applicato a $`E = \Omega`$: il complementare dell'evento certo è l'evento impossibile, quindi $`P(\emptyset) = 1 - P(\Omega) = 1 - 1 = 0`$.
</details>
### Corollario 3 — monotonìa
$$
A \subseteq B \implies P(A) \le P(B)
$$
Se ogni esito di $`A`$ sta anche in $`B`$, allora $`B`$ è "più grande" e non può essere meno probabile.
**Sul dado:** $`A`$ = "esce 6" $`= \{6\}`$ è contenuto in $`B`$ = "esce pari" $`= \{2,4,6\}`$. Infatti $`1/6 \le 3/6`$.
> È la formalizzazione dell'intuizione dell'area: una regione contenuta in un'altra non può avere area maggiore. Detto altrimenti, **una condizione più restrittiva è sempre meno probabile** — "esce 6" è più difficile di "esce pari".
<details>
<summary>Da dove viene</summary>
	Se $`A \subseteq B`$, allora $`B`$ si può spezzare in due pezzi che non si sovrappongono: $`A`$ e la parte di $`B`$ fuori da $`A`$, cioè $`B \cap \bar{A}`$. Per l'assioma 3:
	$$
	P(B) = P(A) + P(B \cap \bar{A})
	$$
	Per l'assioma 1 il secondo termine non è negativo, quindi $`P(B) \ge P(A)`$.
</details>
---
## Riepilogo
<table fit-page-width="true" header-row="true">
<tr>
<td>Simbolo</td>
<td>Si legge</td>
<td>Significato</td>
<td>Esempio sul dado</td>
</tr>
<tr>
<td>$`\Omega`$</td>
<td>Omega</td>
<td>Spazio campionario: tutti gli esiti</td>
<td>$`\{1,2,3,4,5,6\}`$</td>
</tr>
<tr>
<td>$`\emptyset`$</td>
<td>Insieme vuoto</td>
<td>Evento impossibile</td>
<td>"Esce 7"</td>
</tr>
<tr>
<td>$`\bar{E}`$</td>
<td>E negato</td>
<td>Tutto ciò che non è $`E`$</td>
<td>Pari → dispari</td>
</tr>
<tr>
<td>$`A \cup B`$</td>
<td>A unito B</td>
<td>Accade $`A`$ **oppure** $`B`$</td>
<td>$`\{2,4,6\} \cup \{4,5,6\} = \{2,4,5,6\}`$</td>
</tr>
<tr>
<td>$`A \cap B`$</td>
<td>A intersecato B</td>
<td>Accadono **entrambi**</td>
<td>$`\{2,4,6\} \cap \{4,5,6\} = \{4,6\}`$</td>
</tr>
<tr>
<td>$`A \subseteq B`$</td>
<td>A contenuto in B</td>
<td>Ogni esito di $`A`$ sta in $`B`$</td>
<td>$`\{6\} \subseteq \{2,4,6\}`$</td>
</tr>
</table>
**Le tre regole in una riga ciascuna:**
1. Le probabilità stanno fra 0 e 1.
2. Qualcosa deve accadere: $`P(\Omega) = 1`$.
3. Eventi che non possono accadere insieme si sommano.
Tutto il resto della lezione — complementare, evento impossibile, monotonìa — discende da queste tre.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 2 ("Outcomes, events, and probability")
- [Wikipedia — Assiomi di Kolmogorov](https://it.wikipedia.org/wiki/Assiomi_della_probabilit%C3%A0)
