# 13 - Marginali e covarianza

> Fonte Notion: https://app.notion.com/p/3c712abc808d81b58e8af23ceecc9815 — ultima modifica 2026-08-25T10:57:05.794Z

<table_of_contents color="gray"/>
Avendo la tavola congiunta di due statistiche, si possono fare due cose in più: **tornare indietro** a una variabile sola, e **misurare quanto le due si muovono insieme**.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	La **marginale** è quello che resta quando di una coppia guardi solo un numero e dimentichi l'altro.
	La **covarianza** risponde a: quando una delle due cresce, l'altra tende a crescere anche lei, a calare, o non c'entra niente?
</callout>
---
## Distribuzione marginale
Dalla tavola congiunta si ottiene la distribuzione di una sola variabile **sommando via** l'altra:
$$
p(a) = \sum_b p(a, b)
$$
Sulla tavola del modulo 12: sommare una riga intera dà la probabilità di quel valore della somma, qualunque sia stato il massimo. "Marginale" perché il risultato si scrive **a margine** della tabella.
---
## Cumulativa congiunta
Stesso passaggio già fatto nel caso a una variabile, ma con due indici:
$$
F(a, b) = P(X \le a,\; Y \le b)
$$
E la marginale si recupera lasciando correre l'altra variabile fino in fondo:
$$
F_X(a) = P(X \le a) = \lim_{b \to \infty} F(a, b)
$$
> Il limite dice "non mi interessa quanto vale $`Y`$": lo lascio libero di essere qualsiasi cosa.
---
## Il caso continuo
Una sola formula da tenere: la probabilità di finire dentro un **rettangolo** del piano è l'integrale doppio della densità.
$$
P(a_1 \le X \le b_1,\; a_2 \le Y \le b_2) = \int_{a_2}^{b_2}\!\!\int_{a_1}^{b_1} f(x,y)\,dx\,dy
$$
Detto dal docente: è **la somma vista finora, ma in 2D**. Da qui discendono le altre due:
<table fit-page-width="true" header-row="true">
<tr>
<td>Da cosa a cosa</td>
<td>Formula</td>
<td>Operatore</td>
</tr>
<tr>
<td>densità → cumulativa</td>
<td>$`F(a,b) = \int_{-\infty}^{a}\!\int_{-\infty}^{b} f(x,y)\,dx\,dy`$</td>
<td>integrale, due volte</td>
</tr>
<tr>
<td>cumulativa → densità</td>
<td>$`f(x,y) = \dfrac{\partial^2}{\partial x\, \partial y} F(x,y)`$</td>
<td>derivata, due volte</td>
</tr>
</table>
---
## Valore atteso di una funzione delle due
Se $`g(X,Y)`$ è una qualsiasi quantità calcolata dalla coppia, il suo valore atteso si costruisce come sempre: valore per peso, poi si somma.
<table fit-page-width="true" header-row="true">
<tr>
<td>Caso</td>
<td>Formula</td>
</tr>
<tr>
<td>**Discreto**</td>
<td>$`E[g(X,Y)] = \sum_i \sum_j g(a_i, b_j)\, P(X = a_i,\, Y = b_j)`$</td>
</tr>
<tr>
<td>**Continuo**</td>
<td>$`E[g(X,Y)] = \int\!\!\int g(x,y)\, f(x,y)\,dx\,dy`$</td>
</tr>
</table>
Lo schema si estende a $`n`$ variabili: un integrale per ciascuna.
---
## Covarianza
Si sceglie come $`g`$ il **prodotto dei due scarti**:
$$
\mathrm{Cov}(X,Y) = E\big[(x - E[x])(y - E[y])\big]
$$
È la varianza con una variabile sola sostituita dall'altra: se al posto di $`Y`$ si mette di nuovo $`X`$, si ritrova esattamente $`\mathrm{Var}[X]`$.
<table fit-page-width="true" header-row="true">
<tr>
<td>Segno</td>
<td>Cosa vuol dire</td>
</tr>
<tr>
<td>**positiva**</td>
<td>quando una sta sopra la sua media, di solito ci sta anche l'altra</td>
</tr>
<tr>
<td>**negativa**</td>
<td>quando una sale, l'altra tende a scendere</td>
</tr>
<tr>
<td>**vicina a zero**</td>
<td>non si muovono insieme in modo sistematico</td>
</tr>
</table>
<callout icon="⚠️" color="yellow_bg">
	**\[integrazione\]** Somma e massimo di due dadi hanno covarianza **positiva**: tirando numeri alti sale sia la somma sia il massimo. Non è un caso isolato — sono due statistiche calcolate sullo stesso lancio, quindi è normale che siano legate.
</callout>
---
## Riepilogo degli oggetti
<table fit-page-width="true" header-row="true">
<tr>
<td>Simbolo</td>
<td>Nome</td>
</tr>
<tr>
<td>$`f(x,y)`$</td>
<td>densità congiunta (pdf 2D)</td>
</tr>
<tr>
<td>$`F(x,y)`$</td>
<td>cumulativa congiunta</td>
</tr>
<tr>
<td>$`F_X(a)`$, $`F_Y(b)`$</td>
<td>le due marginali</td>
</tr>
<tr>
<td>$`\mathrm{Cov}(X,Y)`$</td>
<td>covarianza</td>
</tr>
</table>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 9–10
