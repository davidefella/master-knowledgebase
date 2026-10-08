# 17 - Verosimiglianza: il calcolo per esteso

> Fonte Notion: https://app.notion.com/p/3c712abc808d81de8a03ef15466499ae — ultima modifica 2026-08-25T14:02:54.234Z

<table_of_contents color="gray"/>
Qui il principio del modulo 16 diventa un conto vero: dalla tabella osservata a un numero.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Immagina di dover indovinare quanto è truccata una moneta guardando solo una serie di lanci già fatti.
	Scrivi la probabilità di quella serie in funzione del truccaggio, poi cerchi il valore che la rende più alta. Fine: quello è il metodo.
</callout>
---
## Il quadro: mondo, campione, osservazione
![](notion-file-block://4e3c336f-37e1-467a-a3ab-efa66b26cec5/71c1bc4c-32a4-46ed-8788-b085c42aa82d?space_id=98012abc-808d-816f-9733-00030a2b4817&name=20-mondo-campione.svg)
Il **mondo** $`\Omega`$ contiene tutte le donne possibili. Noi ne osserviamo solo un gruppo, che il docente chiama **E** — il campione. Da E ricaviamo una tabella, e quella tabella è "descritta dal parametro $`p`$".
L'obiettivo dichiarato: **determinare **$`p`$** in modo esatto, o con errore trascurabile**.
---
## I mattoni
Dal modello geometrico del modulo 16:
<table fit-page-width="true" header-row="true">
<tr>
<td>Caso</td>
<td>Probabilità</td>
<td>Perché</td>
</tr>
<tr>
<td>Concepisce al ciclo $`k`$</td>
<td>$`P(x_i = k) = (1-p)^{k-1}\, p`$</td>
<td>$`k-1`$ fallimenti, poi il successo</td>
</tr>
<tr>
<td>Non concepisce entro 12</td>
<td>$`P(x_i > 12) = (1-p)^{12}`$</td>
<td>nessun successo nei tentativi 1–12</td>
</tr>
</table>
---
## Si moltiplica tutto
Le 100 fumatrici sono indipendenti, quindi la probabilità di vedere **esattamente quella tabella** è il prodotto dei singoli contributi, ciascuno elevato a quante donne lo hanno realizzato:
$$
L(p) = P(x_i = 1)^{29} \cdot P(x_i = 2)^{16} \cdot \ldots \cdot P(x_i = 12)^{3} \cdot P(x_i > 12)^{7}
$$
<callout icon="💡" color="blue_bg">
	Parole del docente: questa quantità è la **probabilità che le 100 fumatrici siano distribuite come la tabella osservata**.
	E qui avviene il salto: $`L`$ **nasce nel mondo della probabilità** (un numero) ma **diventa una funzione** — non di $`x`$, ma di $`p`$.
</callout>
Sostituendo i mattoni e raccogliendo le potenze di $`p`$ e di $`(1-p)`$:
$$
L(p) = C \cdot p^{93} \, (1-p)^{322}
$$
<details>
<summary>Da dove vengono 93 e 322</summary>
	Ogni donna che concepisce contribuisce con **un** fattore $`p`$: sono 93 (tutte tranne le 7 che superano i 12 cicli).
	Ogni ciclo fallito contribuisce con un fattore $`(1-p)`$. Sommando i cicli falliti di tutte:
	$$
	29\cdot 0 + 16\cdot 1 + 17\cdot 2 + 4\cdot 3 + 3\cdot 4 + 9\cdot 5 + 4\cdot 6 + 5\cdot 7 + 1\cdot 8 + 1\cdot 9 + 1\cdot 10 + 3\cdot 11 = 238
	$$
	A cui si aggiungono le 7 censurate, ognuna con 12 cicli falliti: $`7 \times 12 = 84`$. In totale $`238 + 84 = 322`$.
	$`C`$ raccoglie i fattori che non dipendono da $`p`$: essendo una costante, non sposta il massimo.
</details>
---
## Si cerca il massimo
Si annulla la derivata rispetto a $`p`$:
$$
\frac{dL}{dp} = C\, p^{92} (1-p)^{321} \,(93 - 415\,p) = 0
$$
Le soluzioni $`p = 0`$ e $`p = 1`$ il docente le scarta come "non interessanti": sono i due estremi in cui la verosimiglianza vale zero. Resta:
$$
93 - 415\,p = 0 \qquad\Longrightarrow\qquad \boxed{\;p = \frac{93}{415} \approx 0{,}224\;}
$$
<details>
<summary>Il passaggio della derivata</summary>
	Regola del prodotto sui due fattori:
	$$
	\frac{dL}{dp} = C\left[ 93\, p^{92}(1-p)^{322} - 322\, p^{93}(1-p)^{321} \right]
	$$
	Si raccoglie il fattore comune $`p^{92}(1-p)^{321}`$:
	$$
	= C\, p^{92}(1-p)^{321}\big[\, 93(1-p) - 322\,p \,\big] = C\, p^{92}(1-p)^{321}\,(93 - 415\,p)
	$$
</details>
---
## Il confronto
<table fit-page-width="true" header-row="true">
<tr>
<td>Metodo</td>
<td>Valore</td>
<td>Quali dati usa</td>
</tr>
<tr>
<td>Stima ingenua</td>
<td>$`29/93 \approx 0{,}31`$</td>
<td>solo la prima colonna</td>
</tr>
<tr>
<td>**Massima verosimiglianza**</td>
<td>$`93/415 \approx 0{,}22`$</td>
<td>tutta la tabella, censurate comprese</td>
</tr>
</table>
La differenza non è un dettaglio: usare l'informazione che c'è cambia la risposta di un terzo.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 21
