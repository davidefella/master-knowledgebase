# 25 - Il p-value e i due tipi di errore

> Fonte Notion: https://app.notion.com/p/3c712abc808d81388d54fba1555cf533 — ultima modifica 2026-08-25T21:11:29.104Z

<table_of_contents color="gray"/>
Il numero che si calcola nei test ha un nome, e viene usato male più di qualsiasi altro concetto statistico.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Il p-value risponde a una domanda sola: **se l'ipotesi di partenza fosse vera, quanto sarebbe stato strano vedere quello che ho visto?**
	Piccolo = molto strano. E se è troppo strano, conviene smettere di credere all'ipotesi.
</callout>
---
## Definizione
Continuando l'esempio del modulo 24 — azienda, numeri di serie, $`T = \max\{x_i\}`$ — la quantità calcolata era:
$$
P\big(T \le \text{valore misurato} \;\mid\; H_0\big)
$$
Questa probabilità **è** il p-value.
![](notion-file-block://24b954eb-812b-4d6a-8c22-22be23c5ff6c/161ded3a-85e7-4da7-83ce-3b90983e21b8?space_id=98012abc-808d-816f-9733-00030a2b4817&name=28-pvalue.svg)
---
## La regola di decisione
<table fit-page-width="true" header-row="true">
<tr>
<td>p-value</td>
<td>Decisione</td>
<td>Parole del docente</td>
</tr>
<tr>
<td>$`\le 5\%`$</td>
<td>rifiuto $`H_0`$</td>
<td>“siamo **costretti** a rifiutare”</td>
</tr>
<tr>
<td>$`> 5\%`$</td>
<td>non rifiuto $`H_0`$</td>
<td>“**possiamo accettare** $`H_0`$”</td>
</tr>
</table>
Sull'esempio, al variare del massimo osservato:
<table fit-page-width="true" header-row="true">
<tr>
<td>Massimo T</td>
<td>p-value</td>
<td>Decisione</td>
</tr>
<tr>
<td>150</td>
<td>0,23%</td>
<td>rifiuto</td>
</tr>
<tr>
<td>200</td>
<td>0,99%</td>
<td>rifiuto</td>
</tr>
<tr>
<td>260</td>
<td>3,7%</td>
<td>rifiuto</td>
</tr>
<tr>
<td>**275**</td>
<td>**4,95%**</td>
<td>**la soglia è qui**</td>
</tr>
<tr>
<td>300</td>
<td>7,7%</td>
<td>non rifiuto</td>
</tr>
<tr>
<td>417</td>
<td>40%</td>
<td>non rifiuto — è il valore atteso</td>
</tr>
</table>
<callout icon="⚠️" color="yellow_bg">
	**\[nota\]** A lezione i due casi vengono letti come 0,36% (sotto soglia) e \~6% (sopra soglia). Rifacendo i prodotti vengono 0,23% e 3,7%: con questi numeri anche il secondo caso resta sotto il 5%, e la soglia cade attorno a un massimo di 275. Il ragionamento illustrato — un caso che costringe a rifiutare e uno che non lo fa — resta identico.
</callout>
---
## Il legame con l'errore di I tipo
Rifiutare $`H_0`$ quando $`H_0`$ è vera è l'**errore di I tipo** del modulo 21.
Il p-value è esattamente la probabilità di commettere quell'errore se decidessi di rifiutare sulla base di questi dati. Quindi:
$$
\text{rifiuto } H_0 \iff \text{p-value} \le \alpha
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Decisione / Realtà</td>
<td>$`H_0`$ vera</td>
<td>$`H_1`$ vera</td>
</tr>
<tr>
<td>**Rifiuto **$`H_0`$</td>
<td>errore di I tipo</td>
<td>ok</td>
</tr>
<tr>
<td>**Non rifiuto **$`H_0`$</td>
<td>ok</td>
<td>errore di II tipo</td>
</tr>
</table>
> Il docente chiama la riga “decision” e la colonna “true state of Nature”: la decisione è nostra, lo stato vero no.
---
## Che cosa il p-value non è
<callout icon="🎯" color="blue_bg">
	**Non è la probabilità che **$`H_0`$** sia vera.** È il contrario: si assume $`H_0`$ vera e si guarda quanto sono improbabili i dati.
	$`P(\text{dati} \mid H_0)`$ e $`P(H_0 \mid \text{dati})`$ sono due cose diverse — è il teorema di Bayes del modulo 19 a dire come si passa dall'una all'altra, e serve anche la prior.
</callout>
<callout icon="⚠️" color="yellow_bg">
	**La soglia del 5% è una convenzione, non una legge di natura.** Un p-value di 4,9% e uno di 5,1% dicono praticamente la stessa cosa, ma portano a decisioni opposte. Per questo conviene sempre riportare il valore, non solo il verdetto.
</callout>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 25
